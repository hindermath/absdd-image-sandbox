#Requires -Version 7
<#
.SYNOPSIS
Offline-Regressionspruefung fuer Pin-Quellen und sichere Payloads.
Offline regression checks for pin sources and safe payloads.
.DESCRIPTION
Nur synthetische Herstellerantworten; kein Netzwerk und keine Container.
Synthetic upstream responses only; no network or container operations.
.EXAMPLE
pwsh -NoProfile -File scripts/tests/test-toolchain-pin-updates.ps1
#>
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$root=Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
Import-Module (Join-Path $root 'scripts/lib/toolchain-pins.psm1') -Force
$script:Assertions=0
function Assert-Pin {
    param([bool]$Condition,[string]$Message)
    $script:Assertions++
    if(-not $Condition){throw "FAIL: ${Message}"}
}
function Assert-PinThrows {
    param([scriptblock]$Operation,[string]$Message)
    $failed=$false
    try { & $Operation | Out-Null } catch { $failed=$true }
    Assert-Pin $failed $Message
}
function ConvertTo-PinFixtureJson { param($Value) ConvertTo-Json -InputObject $Value -Depth 20 -Compress }
$context=Get-AdePinContext $root
Assert-Pin ($context.values.Count -eq 29) 'all existing ARGs have explicit coverage'
$before=Get-AdePinTextHash $context.text
$fixtures=@{}
$fixtures['https://api.adoptium.net/v3/info/available_releases']='{"available_lts_releases":[21,25]}'
$fixtures['https://nodejs.org/dist/index.json']='[{"version":"v24.22.1","lts":"Fixture"}]'
$fixtures['https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/maven-metadata.xml']='<metadata><versioning><versions><version>3.10.1</version><version>4.0.0-rc-1</version></versions></versioning></metadata>'
$fixtures['https://archive.apache.org/dist/maven/maven-3/3.10.1/binaries/apache-maven-3.10.1-bin.tar.gz.sha512']='c'*128
$fixtures['https://static.rust-lang.org/dist/channel-rust-stable.toml']="[pkg.rust]`nversion = `"1.99.2 (fixture)`"`n"
$fixtures['https://static.rust-lang.org/rustup/release-stable.toml']="schema-version = '1'`nversion = '1.99.2'`n"
$fixtures['https://go.dev/dl/?mode=json&include=all']=ConvertTo-PinFixtureJson @(@{version='go1.27.4';stable=$true;files=@(
    @{os='linux';arch='amd64';kind='archive';filename='go1.27.4.linux-amd64.tar.gz';sha256=('a'*64)},
    @{os='linux';arch='arm64';kind='archive';filename='go1.27.4.linux-arm64.tar.gz';sha256=('b'*64)})})
$fixtures['https://dotnetcli.blob.core.windows.net/dotnet/release-metadata/10.0/releases.json']=ConvertTo-PinFixtureJson @{releases=@(@{sdks=@(
    @{version='10.0.304';files=@(@{rid='linux-x64';url='https://builds.dotnet.microsoft.com/dotnet/Sdk/10.0.304/dotnet-sdk-10.0.304-linux-x64.tar.gz';hash=('a'*128)},@{rid='linux-arm64';url='https://builds.dotnet.microsoft.com/dotnet/Sdk/10.0.304/dotnet-sdk-10.0.304-linux-arm64.tar.gz';hash=('b'*128)})},
    @{version='10.0.499';files=@()})})}
$fixtures['https://api.github.com/repos/astral-sh/python-build-standalone/releases/latest']=ConvertTo-PinFixtureJson @{tag_name='20261022';draft=$false;prerelease=$false;assets=@(
    @{name='cpython-3.15.2+20261022-x86_64-unknown-linux-gnu-install_only_stripped.tar.gz';digest=('sha256:'+('a'*64))},
    @{name='cpython-3.15.2+20261022-aarch64-unknown-linux-gnu-install_only_stripped.tar.gz';digest=('sha256:'+('b'*64))})}
foreach($pin in $context.registry.pins){
    if($pin.provider -ceq 'gomod'){$fixtures["https://proxy.golang.org/$($pin.package)/@v/list"]="v9.0.0`nv99.0.0-beta`n"}
    if($pin.provider -ceq 'npm'){
        $url='https://registry.npmjs.org/'+[uri]::EscapeDataString($pin.package)
        if($pin.ContainsKey('channel')){$fixtures[$url]='{"versions":{"12.2.2":{},"13.0.0":{}}}'}
        else{$fixtures[$url+'/latest']='{"version":"9.0.0"}'}
    }
    if($pin.provider -cin @('github','powershell')){
        $plain=if($pin.arg -ceq 'SWIFT_DOCKER_TAG'){'6.4.3'}elseif($pin.arg -ceq 'POWERSHELL_VERSION'){'7.6.9'}elseif($pin.arg -ceq 'PANDOC_VERSION'){'9.0'}else{'9.0.0'}
        $assets=@()
        if($pin.ContainsKey('assets')){
            $assets=@(@{name=$pin.assets.amd64.Replace('{version}',$plain);digest=('sha256:'+('a'*64))},
                @{name=$pin.assets.arm64.Replace('{version}',$plain);digest=('sha256:'+('b'*64))})
        }
        $fixtures["https://api.github.com/repos/$($pin.package)/releases/latest"]=ConvertTo-PinFixtureJson @{tag_name=($pin.tagPrefix+$plain+$pin.tagSuffix);draft=$false;prerelease=$false;assets=$assets}
    }
}
$fixtures['https://powershellinfraartifacts-gkhedzdeaghdezhr.z01.azurefd.net/tool/7.6.9/PowerShell.Linux.x64.7.6.9.nupkg']='a'*64
$fixtures['https://powershellinfraartifacts-gkhedzdeaghdezhr.z01.azurefd.net/tool/7.6.9/PowerShell.Linux.arm64.7.6.9.nupkg']='b'*64
Set-AdePinFixtures $fixtures
$report=Get-AdePinReport $context
foreach($entry in $report.groups){ if($entry.status -ceq 'Blocked'){Write-Output "$($entry.group): $($entry.reason)"} }
Assert-Pin ($report.status -ceq 'Ready') 'all provider families resolve against fixtures'
Assert-Pin (@($report.groups).Count -eq 28) 'Python version and date are one atomic group'
Assert-Pin (@($report.groups|Where-Object status -eq 'Candidate').Count -gt 0) 'fixtures still produce mutable group proposals'
Assert-Pin (@($report.groups|Where-Object { $_.group -ceq 'SWIFT_DOCKER_TAG' -and $_.status -ceq 'PolicyHeld' }).Count -eq 1) 'Swift update awaits canonical Level-0 registry propagation'
foreach($arg in @('GO_VERSION','RUST_TOOLCHAIN')) {
    $entry=@($report.groups|Where-Object group -eq $arg)[0]
    $learnerProfile=Get-AdePinLearnerProfile $context $entry
    Assert-Pin ($learnerProfile.Contains($entry.updates[$arg])) 'derived learner version follows proposed runtime'
}
foreach($proposal in @($report.groups|Where-Object status -eq 'Candidate')){
    $changed=Update-AdePinDockerfile $context $proposal
    Assert-Pin ($changed -cne $context.text) "proposal changes only its owned pin group: $($proposal.group)"
    Assert-Pin ($changed.Contains('no-new-privileges') -eq $context.text.Contains('no-new-privileges')) 'unrelated content preserved'
}
Assert-Pin ((Get-AdePinTextHash $context.text) -ceq $before) 'discovery and preparation leave source bytes unchanged'
$npm=@($report.groups|Where-Object group -eq 'NPM_VERSION')[0]
Assert-Pin ($npm.status -ceq 'Current' -and $context.values.NPM_VERSION -ceq '12.2.2') 'npm retains its pinned major'
$sdk=@($report.groups|Where-Object group -eq 'DOTNET_COMPAT_SDK_VERSION')[0]
Assert-Pin ($sdk.updates.DOTNET_COMPAT_SDK_VERSION -ceq '10.0.304') 'compatibility SDK retains its feature band'
$uv=@($report.groups|Where-Object group -eq 'UV_VERSION')[0]
Assert-PinThrows {Update-AdePinDockerfile $context @{group='UV_VERSION';updates=@{UV_VERSION='9.0.0'};hashes=@{amd64=('a'*64)}}} 'missing ARM64 hash rejected'
Assert-PinThrows {Update-AdePinDockerfile $context @{group='UV_VERSION';updates=@{UV_VERSION='9.0.0'};hashes=@{amd64=('a'*63);arm64=('b'*64)}}} 'malformed hash rejected'
Assert-PinThrows {Update-AdePinDockerfile $context @{group='UV_VERSION';updates=@{CODEX_VERSION='9.0.0'};hashes=@{}}} 'unrelated ARG rejected'
Assert-PinThrows {Update-AdePinDockerfile $context @{group='UV_VERSION';updates=@{UV_VERSION='0.0.1'};hashes=@{}}} 'downgrade rejected'
Assert-PinThrows {Update-AdePinDockerfile $context @{group='CODEX_VERSION';updates=@{CODEX_VERSION='9.0.0; command'};hashes=@{}}} 'version command injection rejected'
Assert-PinThrows {Update-AdePinDockerfile $context @{group='PYTHON_RUNTIME';updates=@{PYTHON_VERSION='3.15.2'};hashes=@{amd64=('a'*64);arm64=('b'*64)}}} 'Python companion update required'
Assert-PinThrows {Update-AdePinDockerfile $context @{group='DOTNET_COMPAT_SDK_VERSION';updates=@{DOTNET_COMPAT_SDK_VERSION='10.0.499'};hashes=@{amd64=('a'*128);arm64=('b'*128)}}} 'SDK feature-band escape rejected'
foreach($url in @('http://api.github.com/repos/x/y','https://localhost/releases','https://api.github.com:444/x','https://user:secret@api.github.com/x','https://api.github.com/x#fragment')){
    Assert-PinThrows {Invoke-AdePinRequest $url} 'unapproved source boundary rejected before any network'
}
$missing=$fixtures.Clone();$missing.Remove('https://api.github.com/repos/anchore/syft/releases/latest')
Set-AdePinFixtures $missing
Assert-Pin ((Get-AdePinReport $context).status -ceq 'Blocked') 'missing source fails closed rather than claiming current'
$bad=$fixtures.Clone();$bad['https://api.github.com/repos/anchore/syft/releases/latest']='{"tag_name":"v9.0.0","draft":false,"prerelease":true,"assets":[]}'
Set-AdePinFixtures $bad
Assert-Pin ((Get-AdePinReport $context).status -ceq 'Blocked') 'prerelease metadata fails closed'
$bad=$fixtures.Clone();$bad['https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/maven-metadata.xml']='<!DOCTYPE metadata [<!ENTITY x SYSTEM "file:///etc/passwd">]><metadata>&x;</metadata>'
Set-AdePinFixtures $bad
Assert-Pin ((Get-AdePinReport $context).status -ceq 'Blocked') 'XML entity expansion rejected'
$held=$fixtures.Clone();$held['https://api.github.com/repos/swiftlang/swift/releases/latest']='{"tag_name":"swift-7.0.0-RELEASE","draft":false,"prerelease":false,"assets":[]}'
Set-AdePinFixtures $held
Assert-Pin (@((Get-AdePinReport $context).groups|Where-Object {$_.group -ceq 'SWIFT_DOCKER_TAG' -and $_.status -ceq 'PolicyHeld'}).Count -eq 1) 'Swift signing-key boundary retained'

$tempBase=if($IsMacOS){'/private/tmp'}else{[IO.Path]::GetTempPath()}
$fixture=Join-Path $tempBase ('pin-workflow-test-'+[guid]::NewGuid().ToString('N'))
try{
    $null=New-Item -ItemType Directory -Path "$fixture/repo/scripts/config" -Force
    Copy-Item "$root/Dockerfile" "$fixture/repo/Dockerfile"
    Copy-Item "$root/scripts/config/toolchain-pins.json" "$fixture/repo/scripts/config/toolchain-pins.json"
    & git -c init.defaultBranch=main init --quiet "$fixture/repo"
    if($LASTEXITCODE){throw 'Fixture git init failed'}
    & git -C "$fixture/repo" add .
    & git -C "$fixture/repo" -c core.hooksPath="$fixture/no-hooks" -c user.name=Fixture -c user.email=fixture@example.invalid -c commit.gpgsign=false commit --quiet -m fixture
    if($LASTEXITCODE){throw 'Fixture commit failed'}
    $null=New-Item -ItemType Directory -Path "$fixture/payload"
    $changed=Update-AdePinDockerfile $context $uv
    $proposal=@{schemaVersion=1;baseHead=(& git -C "$fixture/repo" rev-parse HEAD);baseSha256=$before;resultSha256=(Get-AdePinTextHash $changed);group=$uv.group;updates=$uv.updates;hashes=$uv.hashes}
    $proposal | ConvertTo-Json -Depth 10 | Set-Content "$fixture/payload/proposal.json"
    [IO.File]::WriteAllText("$fixture/payload/Dockerfile",$changed,[Text.UTF8Encoding]::new($false))
    $entry=Join-Path $root 'scripts/update-toolchain-pins.ps1'
    & pwsh -NoProfile -File $entry -Action Verify -Repo "$fixture/repo" -PayloadDirectory "$fixture/payload" -Json | Out-Null
    Assert-Pin ($LASTEXITCODE -eq 0) 'offline payload verification succeeds'
    & pwsh -NoProfile -File $entry -Action Apply -Repo "$fixture/repo" -PayloadDirectory "$fixture/payload" -WhatIf | Out-Null
    Assert-Pin ($LASTEXITCODE -eq 0 -and (Get-AdePinTextHash ([IO.File]::ReadAllText("$fixture/repo/Dockerfile"))) -ceq $before) 'WhatIf does not mutate source'
    [IO.File]::AppendAllText("$fixture/payload/Dockerfile","`nRUN malicious-fixture`n")
    & pwsh -NoProfile -File $entry -Action Verify -Repo "$fixture/repo" -PayloadDirectory "$fixture/payload" 2> "$fixture/rejected.log" | Out-Null
    Assert-Pin ($LASTEXITCODE -eq 2) 'payload cannot inject unrelated Dockerfile instructions'
    [IO.File]::WriteAllText("$fixture/payload/Dockerfile",$changed,[Text.UTF8Encoding]::new($false))
    & pwsh -NoProfile -File $entry -Action Apply -Repo "$fixture/repo" -PayloadDirectory "$fixture/payload" -Json | Out-Null
    Assert-Pin ($LASTEXITCODE -eq 0 -and [IO.File]::ReadAllText("$fixture/repo/Dockerfile") -ceq $changed) 'Apply writes exactly the verified candidate'
    & pwsh -NoProfile -File $entry -Action Verify -Repo "$fixture/repo" -PayloadDirectory "$fixture/payload" 2> "$fixture/drift.log" | Out-Null
    Assert-Pin ($LASTEXITCODE -eq 2) 'payload cannot be replayed after source drift'
}finally{if(Test-Path $fixture){Remove-Item $fixture -Recurse -Force}}
Set-AdePinFixtures $null
Write-Output "PASS: $script:Assertions assertions; offline providers, hash coupling, payload boundaries and read-only checks."
# DE: Erwartete Fehlercodes der Negativtests nicht an CI vererben.
# EN: Do not leak expected negative-test exit codes into the CI caller.
exit 0
