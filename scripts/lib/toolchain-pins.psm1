#Requires -Version 7
<#
.SYNOPSIS
Begrenzte Herstellerabfragen und atomare Pin-Vorschlaege.
Bounded upstream discovery and atomic pin proposals.
.DESCRIPTION
Liest nur feste HTTPS-Quellen; fuehrt heruntergeladene Inhalte nicht aus.
Reads fixed HTTPS sources only; downloaded content is never executed.
#>
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$script:PinFixtures = $null
$script:PinCache = @{}
$script:PinHosts = @('api.github.com','registry.npmjs.org','proxy.golang.org','go.dev',
    'static.rust-lang.org','repo.maven.apache.org','dlcdn.apache.org','archive.apache.org',
    'dotnetcli.blob.core.windows.net','api.adoptium.net','nodejs.org',
    'powershellinfraartifacts-gkhedzdeaghdezhr.z01.azurefd.net')

function Set-AdePinFixtures {
    param([AllowNull()][System.Collections.IDictionary]$Responses)
    $script:PinFixtures = $Responses
    $script:PinCache = @{}
}

function Invoke-AdePinRequest {
    param([Parameter(Mandatory)][string]$Uri, [switch]$Hash)
    $address = [uri]$Uri
    if (-not $address.IsAbsoluteUri -or $address.Scheme -cne 'https' -or
        $address.Host -cnotin $script:PinHosts -or $address.Port -ne 443 -or
        $address.UserInfo -or $address.Fragment) { throw 'Unapproved metadata source.' }
    $key = "${Hash}:${Uri}"
    if ($script:PinCache.ContainsKey($key)) { return $script:PinCache[$key] }
    if ($null -ne $script:PinFixtures) {
        if (-not $script:PinFixtures.Contains($Uri)) { throw "Missing offline fixture: ${Uri}" }
        $value = $script:PinFixtures[$Uri]
        if ($Hash -and $value -cnotmatch '^[a-f0-9]{64}$') { throw 'Invalid fixture digest.' }
        $script:PinCache[$key] = $value
        return $value
    }
    # Kein Redirect und kein Token ausserhalb api.github.com. Downloads bleiben Daten.
    # No redirects or token forwarding; package downloads are hashed, never executed.
    $handler = [Net.Http.HttpClientHandler]::new()
    $handler.AllowAutoRedirect = $false
    $client = [Net.Http.HttpClient]::new($handler)
    $timer = [Threading.CancellationTokenSource]::new([timespan]::FromSeconds(60))
    $request = [Net.Http.HttpRequestMessage]::new([Net.Http.HttpMethod]::Get, $address)
    $response = $null; $stream = $null; $memory = $null; $digest = $null
    try {
        $request.Headers.UserAgent.ParseAdd('absdd-toolchain-pins/1')
        if ($address.Host -ceq 'api.github.com') {
            $request.Headers.Accept.ParseAdd('application/vnd.github+json')
            if ($env:GH_TOKEN) { $request.Headers.Authorization = [Net.Http.Headers.AuthenticationHeaderValue]::new('Bearer',$env:GH_TOKEN) }
        } elseif ($address.Host -ceq 'registry.npmjs.org' -and -not $address.AbsolutePath.EndsWith('/latest',[StringComparison]::Ordinal)) {
            $request.Headers.Accept.ParseAdd('application/vnd.npm.install-v1+json')
        }
        $response = $client.SendAsync($request,[Net.Http.HttpCompletionOption]::ResponseHeadersRead,$timer.Token).GetAwaiter().GetResult()
        if (-not $response.IsSuccessStatusCode) { throw "Upstream HTTP $([int]$response.StatusCode): $($address.Host)" }
        $limit = if ($Hash) { 256MB } else { 32MB }
        if ($response.Content.Headers.ContentLength -gt $limit) { throw 'Upstream response exceeds size limit.' }
        $stream = $response.Content.ReadAsStreamAsync($timer.Token).GetAwaiter().GetResult()
        if ($Hash) { $digest = [Security.Cryptography.IncrementalHash]::CreateHash([Security.Cryptography.HashAlgorithmName]::SHA256) }
        else { $memory = [IO.MemoryStream]::new() }
        $buffer = [byte[]]::new(65536); $total = 0
        while (($count = $stream.ReadAsync($buffer,0,$buffer.Length,$timer.Token).GetAwaiter().GetResult()) -gt 0) {
            $total += $count
            if ($total -gt $limit) { throw 'Upstream response exceeds size limit.' }
            if ($Hash) { $digest.AppendData($buffer,0,$count) } else { $memory.Write($buffer,0,$count) }
        }
        if ($total -eq 0) { throw 'Empty upstream response.' }
        $value = if ($Hash) { [Convert]::ToHexString($digest.GetHashAndReset()).ToLowerInvariant() }
            else { [Text.UTF8Encoding]::new($false,$true).GetString($memory.ToArray()) }
        $script:PinCache[$key] = $value
        return $value
    } finally {
        foreach ($resource in @($digest,$memory,$stream,$response,$request,$timer,$client)) {
            if ($null -ne $resource) { $resource.Dispose() }
        }
    }
}

function Get-AdePinJson {
    param([string]$Uri)
    Invoke-AdePinRequest $Uri | ConvertFrom-Json -AsHashtable -Depth 64
}

function Get-AdePinVersion {
    param([string]$Value)
    $plain = $Value -replace '^v','' -replace '-noble$',''
    if ($plain -cnotmatch '^\d+\.\d+(?:\.\d+){0,2}$') { throw "Invalid stable version: ${Value}" }
    if (($plain -split '\.').Count -eq 2) { $plain += '.0' }
    [version]$plain
}

function Get-AdePinContext {
    param([Parameter(Mandatory)][string]$Repo)
    $root = (Resolve-Path -LiteralPath $Repo).Path
    $path = Join-Path $root 'Dockerfile'
    $registryPath = Join-Path $root 'scripts/config/toolchain-pins.json'
    foreach ($owned in @($path,$registryPath)) {
        if ((Get-Item -LiteralPath $owned).LinkType) { throw 'Pin sources must not be symlinks.' }
    }
    $text = [IO.File]::ReadAllText($path)
    $registry = [IO.File]::ReadAllText($registryPath) | ConvertFrom-Json -AsHashtable
    if ($registry.schemaVersion -ne 1 -or $registry.runtime -cne 'podman' -or $registry.dockerfile -cne 'Dockerfile') { throw 'Unsupported pin registry.' }
    if ($registry.baseImage.owner -cne 'dependabot' -or $registry.baseImage.dependency -cne 'mcr.microsoft.com/dotnet/sdk' -or $registry.baseImage.tag -cne '10.0' -or
        $text -cnotmatch '(?m)^FROM mcr\.microsoft\.com/dotnet/sdk:10\.0@sha256:[a-f0-9]{64} AS dotnet-base\r?$') { throw 'Approved base-image channel/digest has drifted.' }
    $values = @{}
    foreach ($match in [regex]::Matches($text,'(?m)^ARG ([A-Z][A-Z0-9_]*)=([^\r\n]+)\r?$')) {
        $name = $match.Groups[1].Value
        if ($values.ContainsKey($name)) { throw "Duplicate ARG: ${name}" }
        $value = $match.Groups[2].Value.TrimEnd("`r")
        if ($value -cnotmatch '^(?:v?\d+(?:\.\d+){0,3}(?:-noble)?)$') { throw "Unsafe ARG value: ${name}" }
        $values[$name] = $value
    }
    $names = @($registry.pins | ForEach-Object { $_.arg })
    if ($names.Count -ne $values.Count -or @($names | Select-Object -Unique).Count -ne $names.Count -or
        @($names | Where-Object { -not $values.ContainsKey($_) }).Count) { throw 'Pin coverage differs from Dockerfile ARGs.' }
    $providers = @('github','npm','gomod','go','rust','rustup','maven','python','powershell','dotnet','java-channel','node-channel','companion')
    foreach ($pin in $registry.pins) {
        if ($pin.arg -cnotmatch '^[A-Z][A-Z0-9_]*$' -or $pin.group -cnotmatch '^[A-Z][A-Z0-9_]*$' -or
            $pin.provider -cnotin $providers -or $pin.package -cnotmatch '^[@A-Za-z0-9][A-Za-z0-9@:._/-]*$') { throw 'Invalid pin record.' }
        if ($pin.provider -ceq 'companion' -and $pin.arg -cne 'PYTHON_BUILD_DATE') { throw 'Unknown companion ARG.' }
    }
    @{ root=$root; text=$text; registry=$registry; values=$values }
}

function Get-AdePinRelease {
    param([System.Collections.IDictionary]$Pin)
    if ($Pin.package -cnotmatch '^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$') { throw 'Invalid GitHub source.' }
    $release = Get-AdePinJson "https://api.github.com/repos/$($Pin.package)/releases/latest"
    if ($release.draft -or $release.prerelease) { throw 'Upstream latest release is not stable.' }
    $digits = if ($Pin.package -ceq 'jgm/pandoc') { '\d+\.\d+(?:\.\d+){0,2}' } else { '\d+\.\d+\.\d+' }
    $pattern = '^' + [regex]::Escape($Pin.tagPrefix) + '('+$digits+')' + [regex]::Escape($Pin.tagSuffix) + '$'
    $match = [regex]::Match($release.tag_name,$pattern)
    if (-not $match.Success) { throw 'Unrecognized upstream release tag.' }
    @{ version=$match.Groups[1].Value; data=$release }
}

function Get-AdePinAssetDigest {
    param([System.Collections.IDictionary]$Release,[string]$Name)
    $assets = @($Release.assets | Where-Object { $_.name -ceq $Name })
    if ($assets.Count -ne 1 -or -not $assets[0].ContainsKey('digest') -or $assets[0].digest -cnotmatch '^sha256:[a-f0-9]{64}$') {
        throw "Missing unique upstream asset/digest: ${Name}"
    }
    $assets[0].digest.Substring(7)
}

function Get-AdePinCandidate {
    param([System.Collections.IDictionary]$Pin,[System.Collections.IDictionary]$Values)
    $current = $Values[$Pin.arg]
    $updates = @{}; $hashes = @{}; $source = ''; $version = $null
    switch -CaseSensitive ($Pin.provider) {
        'java-channel' {
            $source = 'https://api.adoptium.net/v3/info/available_releases'
            $data = Get-AdePinJson $source
            if ([int]$Pin.channel -notin $data.available_lts_releases -or $current -cne $Pin.channel) { throw 'Pinned Java LTS channel is unavailable or has drifted.' }
            return @{group=$Pin.group;status='ChannelPinned';updates=@{};hashes=@{};source=$source}
        }
        'node-channel' {
            $source = 'https://nodejs.org/dist/index.json'
            $data = @(Get-AdePinJson $source | Where-Object { $_.version -match ('^v'+[regex]::Escape($Pin.channel)+'\.') -and $_.lts })
            if ($data.Count -eq 0 -or $current -cne $Pin.channel) { throw 'Pinned Node LTS channel is unavailable or has drifted.' }
            return @{group=$Pin.group;status='ChannelPinned';updates=@{};hashes=@{};source=$source}
        }
        'npm' {
            $encoded = [uri]::EscapeDataString($Pin.package)
            $source = "https://registry.npmjs.org/${encoded}"
            if ($Pin.ContainsKey('channel')) {
                $data = Get-AdePinJson $source
                $versions = @($data.versions.Keys | Where-Object { $_ -match ('^'+[regex]::Escape($Pin.channel)+'\.\d+\.\d+$') } | Sort-Object {[version]$_} -Descending)
                if ($versions.Count -eq 0) { throw 'No stable npm version in the pinned channel.' }
                $version = $versions[0]
            } else {
                $source += '/latest'
                $version = (Get-AdePinJson $source).version
            }
        }
        'gomod' {
            if ($Pin.package -cnotmatch '^[a-z0-9./-]+$') { throw 'Unapproved Go module path encoding.' }
            $source = "https://proxy.golang.org/$($Pin.package)/@v/list"
            $versions = @((Invoke-AdePinRequest $source) -split '\r?\n' | Where-Object { $_ -cmatch '^v\d+\.\d+\.\d+$' } | Sort-Object {Get-AdePinVersion $_} -Descending)
            if ($versions.Count -eq 0) { throw 'No stable Go module version.' }
            $version = $versions[0]
        }
        'go' {
            $source = 'https://go.dev/dl/?mode=json&include=all'
            $data = @(Get-AdePinJson $source | Where-Object { $_.stable -and $_.version -cmatch '^go\d+\.\d+\.\d+$' } | Sort-Object {[version]$_.version.Substring(2)} -Descending)
            if ($data.Count -eq 0) { throw 'No stable Go release.' }
            $version = $data[0].version.Substring(2)
            if ((Get-AdePinVersion $version) -gt (Get-AdePinVersion $current)) {
                foreach ($arch in @('amd64','arm64')) {
                    $files = @($data[0].files | Where-Object { $_.os -ceq 'linux' -and $_.arch -ceq $arch -and $_.kind -ceq 'archive' -and $_.filename -ceq "go${version}.linux-${arch}.tar.gz" })
                    if ($files.Count -ne 1 -or $files[0].sha256 -cnotmatch '^[a-f0-9]{64}$') { throw 'Missing Go architecture digest.' }
                    $hashes[$arch] = $files[0].sha256
                }
            }
        }
        'rust' {
            $source = 'https://static.rust-lang.org/dist/channel-rust-stable.toml'
            $match = [regex]::Match((Invoke-AdePinRequest $source),'(?ms)^\[pkg\.rust\]\s*\r?\nversion\s*=\s*"(\d+\.\d+\.\d+)\s')
            if (-not $match.Success) { throw 'Invalid stable Rust channel metadata.' }
            $version = $match.Groups[1].Value
        }
        'rustup' {
            $source = 'https://static.rust-lang.org/rustup/release-stable.toml'
            $match = [regex]::Match((Invoke-AdePinRequest $source),'(?m)^version\s*=\s*[''"](\d+\.\d+\.\d+)[''"]\s*$')
            if (-not $match.Success) { throw 'Invalid stable Rustup metadata.' }
            $version = $match.Groups[1].Value
        }
        'maven' {
            $source = 'https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/maven-metadata.xml'
            $settings = [Xml.XmlReaderSettings]::new(); $settings.DtdProcessing = [Xml.DtdProcessing]::Prohibit; $settings.XmlResolver = $null
            $reader = [Xml.XmlReader]::Create([IO.StringReader]::new((Invoke-AdePinRequest $source)),$settings)
            try { $xml = [Xml.XmlDocument]::new(); $xml.XmlResolver = $null; $xml.Load($reader) } finally { $reader.Dispose() }
            $versions = @($xml.SelectNodes('/metadata/versioning/versions/version') | ForEach-Object {$_.InnerText} | Where-Object {$_ -cmatch '^\d+\.\d+\.\d+$'} | Sort-Object {[version]$_} -Descending)
            if ($versions.Count -eq 0) { throw 'No stable Maven release.' }
            $version = $versions[0]
            if ((Get-AdePinVersion $version) -gt (Get-AdePinVersion $current)) {
                $major = ([version]$version).Major
                $checksum = Invoke-AdePinRequest "https://archive.apache.org/dist/maven/maven-${major}/${version}/binaries/apache-maven-${version}-bin.tar.gz.sha512"
                $match = [regex]::Match($checksum.Trim(),'^(?<hash>[A-Fa-f0-9]{128})(?:\s+[^\r\n]+)?$')
                if (-not $match.Success) { throw 'Invalid Maven SHA-512 metadata.' }
                $hashes['all'] = $match.Groups['hash'].Value.ToLowerInvariant()
            }
        }
        'dotnet' {
            $source = "https://dotnetcli.blob.core.windows.net/dotnet/release-metadata/$($Pin.channel)/releases.json"
            $data = Get-AdePinJson $source
            $sdks = @($data.releases | ForEach-Object {$_.sdks} | Where-Object { $_.version -cmatch '^\d+\.\d+\.\d+$' -and ([version]$_.version).ToString(2) -ceq $Pin.channel -and [math]::Floor(([version]$_.version).Build/100) -eq $Pin.featureBand } | Sort-Object {[version]$_.version} -Descending)
            if ($sdks.Count -eq 0) { throw 'No compatibility SDK in the pinned feature band.' }
            $version = $sdks[0].version
            if ((Get-AdePinVersion $version) -gt (Get-AdePinVersion $current)) {
                foreach ($arch in @('amd64','arm64')) {
                    $rid = if ($arch -ceq 'amd64') {'linux-x64'} else {'linux-arm64'}
                    $files = @($sdks[0].files | Where-Object { $_.rid -ceq $rid -and $_.url.EndsWith("/dotnet-sdk-${version}-${rid}.tar.gz",[StringComparison]::Ordinal) })
                    if ($files.Count -ne 1 -or $files[0].hash -cnotmatch '^[a-fA-F0-9]{128}$') { throw 'Missing compatibility SDK architecture digest.' }
                    $hashes[$arch] = $files[0].hash.ToLowerInvariant()
                }
            }
        }
        'python' {
            $source = 'https://api.github.com/repos/astral-sh/python-build-standalone/releases/latest'
            $release = Get-AdePinJson $source
            if ($release.draft -or $release.prerelease -or $release.tag_name -cnotmatch '^\d{8}$') { throw 'Unrecognized standalone Python release.' }
            $candidates = @($release.assets | ForEach-Object {
                if ($_.name -cmatch '^cpython-(\d+\.\d+\.\d+)\+(\d{8})-x86_64-unknown-linux-gnu-install_only_stripped\.tar\.gz$' -and $Matches[2] -ceq $release.tag_name) { $Matches[1] }
            } | Sort-Object {[version]$_} -Descending)
            if ($candidates.Count -eq 0) { throw 'No stable standalone Python assets.' }
            $version = $candidates[0]
            if ((Get-AdePinVersion $version) -lt (Get-AdePinVersion $current)) { throw 'Upstream standalone Python would downgrade the runtime.' }
            $date = $release.tag_name
            if ((Get-AdePinVersion $version) -gt (Get-AdePinVersion $current) -or $date -gt $Values['PYTHON_BUILD_DATE']) {
                foreach ($arch in @('amd64','arm64')) {
                    $target = if ($arch -ceq 'amd64') {'x86_64'} else {'aarch64'}
                    $hashes[$arch] = Get-AdePinAssetDigest $release "cpython-${version}+${date}-${target}-unknown-linux-gnu-install_only_stripped.tar.gz"
                }
                $updates['PYTHON_VERSION'] = $version; $updates['PYTHON_BUILD_DATE'] = $date
            }
        }
        { $_ -cin @('github','powershell') } {
            $source = "https://api.github.com/repos/$($Pin.package)/releases/latest"
            $release = Get-AdePinRelease $Pin
            $version = $release.version
            if ($Pin.ContainsKey('channel') -and ([version]$version).Major.ToString() -cne $Pin.channel) {
                return @{group=$Pin.group;status='PolicyHeld';updates=@{};hashes=@{};source=$source;reason='Review the signing key/channel policy before a major transition.'}
            }
            if ($Pin.ContainsKey('valueSuffix')) { $version += $Pin.valueSuffix }
            if ($Pin.arg -ceq 'SWIFT_DOCKER_TAG' -and (Get-AdePinVersion $version) -gt (Get-AdePinVersion $current)) {
                return @{group=$Pin.group;status='PolicyHeld';updates=@{};hashes=@{};source=$source;reason='Swift changes require coordinated Level-0 registry propagation before a sandbox pin proposal.'}
            }
            if ((Get-AdePinVersion $version) -gt (Get-AdePinVersion $current) -and $Pin.ContainsKey('hashVariable')) {
                foreach ($arch in @('amd64','arm64')) {
                    if ($Pin.provider -ceq 'powershell') {
                        $target = if ($arch -ceq 'amd64') {'x64'} else {'arm64'}
                        $uri = "https://powershellinfraartifacts-gkhedzdeaghdezhr.z01.azurefd.net/tool/${version}/PowerShell.Linux.${target}.${version}.nupkg"
                        $hashes[$arch] = Invoke-AdePinRequest $uri -Hash
                    } else {
                        $name = $Pin.assets[$arch].Replace('{version}',$release.version)
                        $hashes[$arch] = Get-AdePinAssetDigest $release.data $name
                    }
                }
            }
        }
        default { throw 'Unsupported provider group.' }
    }
    if ($Pin.provider -cne 'python') {
        $observed = Get-AdePinVersion $version
        $old = Get-AdePinVersion $current
        if ($observed -lt $old) { throw 'Upstream result would downgrade a pin.' }
        if ($observed -gt $old) { $updates[$Pin.arg] = $version }
    }
    @{group=$Pin.group;status=$(if($updates.Count){'Candidate'}else{'Current'});updates=$updates;hashes=$hashes;source=$source}
}

function Get-AdePinReport {
    param([System.Collections.IDictionary]$Context)
    $groups = [Collections.Generic.List[object]]::new()
    foreach ($pin in $Context.registry.pins) {
        if ($pin.provider -ceq 'companion') { continue }
        try { $groups.Add((Get-AdePinCandidate $pin $Context.values)) }
        catch { $groups.Add(@{group=$pin.group;status='Blocked';updates=@{};hashes=@{};reason=$_.Exception.Message}) }
    }
    @{schemaVersion=1;status=$(if(@($groups | Where-Object status -eq 'Blocked').Count){'Blocked'}else{'Ready'});groups=@($groups)}
}

function Update-AdePinDockerfile {
    param([System.Collections.IDictionary]$Context,[System.Collections.IDictionary]$Proposal)
    $pins = @($Context.registry.pins | Where-Object {$_.group -ceq $Proposal.group})
    if (-not $pins.Count -or $Proposal.updates.Count -eq 0) { throw 'Unknown or empty proposal group.' }
    $text = $Context.text
    foreach ($arg in $Proposal.updates.Keys) {
        if ($arg -cnotin @($pins | ForEach-Object {$_.arg})) { throw 'Proposal changes an unrelated pin.' }
        $value = [string]$Proposal.updates[$arg]
        if ($arg -ceq 'PYTHON_BUILD_DATE') {
            if ($value -cnotmatch '^\d{8}$' -or $value -lt $Context.values[$arg]) { throw 'Invalid Python build date.' }
        } elseif ((Get-AdePinVersion $value) -lt (Get-AdePinVersion $Context.values[$arg])) { throw 'Pin downgrade rejected.' }
        $pin = @($pins | Where-Object {$_.arg -ceq $arg})[0]
        if ($pin.ContainsKey('channel') -and $pin.provider -ceq 'dotnet' -and (([version]$value).ToString(2) -cne $pin.channel -or [math]::Floor(([version]$value).Build/100) -ne $pin.featureBand)) { throw 'SDK feature-band drift.' }
        if ($pin.ContainsKey('channel') -and $pin.provider -cin @('npm','github') -and (Get-AdePinVersion $value).Major.ToString() -cne $pin.channel) { throw 'Pinned channel drift.' }
        if ($pin.ContainsKey('valueSuffix') -and -not $value.EndsWith($pin.valueSuffix,[StringComparison]::Ordinal)) { throw 'Pinned platform suffix drift.' }
        $pattern = '(?m)(^ARG '+[regex]::Escape($arg)+'=)[^\r\n]+'
        $text = [regex]::Replace($text,$pattern,[Text.RegularExpressions.MatchEvaluator]{param($match) $match.Groups[1].Value+$value})
    }
    $owner = @($pins | Where-Object provider -ne 'companion')[0]
    if ($owner.ContainsKey('hashVariable')) {
        $expected = if ($owner.provider -ceq 'maven') {@('all')} else {@('amd64','arm64')}
        if ((($Proposal.hashes.Keys | Sort-Object) -join ',') -cne (($expected | Sort-Object) -join ',')) { throw 'Incomplete architecture digest set.' }
        $bits = if ($owner.algorithm -ceq 'sha512') {128} else {64}
        foreach ($arch in $expected) {
            if ($Proposal.hashes[$arch] -cnotmatch ('^[a-f0-9]{'+$bits+'}$')) { throw 'Malformed archive digest.' }
        }
        $blocks = @([regex]::Matches($text,'(?ms)^RUN .*?(?=^[A-Z]+\s|\z)') | Where-Object { $_.Value.Contains('${'+$owner.arg+'}') -and $_.Value.Contains($owner.hashVariable+'="') })
        if ($blocks.Count -ne 1) { throw 'Ambiguous archive hash block.' }
        $block = $blocks[0].Value
        foreach ($arch in $expected) {
            $prefix = if ($arch -ceq 'all') {'(?m)(^\s*'} else {'(?m)(^\s*'+$arch+'\).*?\b'}
            $pattern = $prefix+[regex]::Escape($owner.hashVariable)+'=")[a-f0-9]{'+$bits+'}(".*)$'
            if ([regex]::Matches($block,$pattern).Count -ne 1) { throw 'Missing unique archive digest binding.' }
            $replacement = [string]$Proposal.hashes[$arch]
            $block = [regex]::Replace($block,$pattern,[Text.RegularExpressions.MatchEvaluator]{param($match) $match.Groups[1].Value+$replacement+$match.Groups[2].Value})
        }
        $text = $text.Substring(0,$blocks[0].Index)+$block+$text.Substring($blocks[0].Index+$blocks[0].Length)
    } elseif ($Proposal.hashes.Count) { throw 'Unexpected archive hashes.' }
    if ($owner.provider -ceq 'python' -and (@($Proposal.updates.Keys).Count -ne 2 -or -not $Proposal.updates.Contains('PYTHON_VERSION') -or -not $Proposal.updates.Contains('PYTHON_BUILD_DATE'))) { throw 'Python version/date must move together.' }
    $text
}

function Get-AdePinTextHash {
    param([string]$Text)
    [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes($Text))).ToLowerInvariant()
}

function Get-AdePinLearnerProfile {
    param([System.Collections.IDictionary]$Context,[System.Collections.IDictionary]$Proposal)
    $argsByLanguage = @{Go='GO_VERSION';Rust='RUST_TOOLCHAIN'}
    $selected = @($argsByLanguage.Keys | Where-Object { $Proposal.updates.Contains($argsByLanguage[$_]) })
    if (-not $selected.Count) { return $null }
    $path = Join-Path $Context.root 'docs/fuer-lernende/sandbox-profil.md'
    if ((Get-Item -LiteralPath $path).LinkType) { throw 'Learner profile must not be a symlink.' }
    $text = [IO.File]::ReadAllText($path)
    foreach ($language in $selected) {
        $arg = $argsByLanguage[$language]
        $pattern = '(?m)(^\| \*\*'+$language+'\*\* \| )'+[regex]::Escape($Context.values[$arg])+'( \|)'
        if ([regex]::Matches($text,$pattern).Count -ne 1) { throw 'Learner version source has drifted.' }
        $value = [string]$Proposal.updates[$arg]
        $null = Get-AdePinVersion $value
        $text = [regex]::Replace($text,$pattern,[Text.RegularExpressions.MatchEvaluator]{param($match) $match.Groups[1].Value+$value+$match.Groups[2].Value})
    }
    $text
}

Export-ModuleMember -Function Set-AdePinFixtures,Invoke-AdePinRequest,Get-AdePinVersion,Get-AdePinContext,Get-AdePinCandidate,Get-AdePinReport,Update-AdePinDockerfile,Get-AdePinTextHash,Get-AdePinLearnerProfile
