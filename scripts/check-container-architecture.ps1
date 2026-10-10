#Requires -Version 7
[CmdletBinding()]
param(
    [string] $Platform = '',
    [string] $ImageName = '',
    [switch] $AllowCrossArchitecture
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function ConvertTo-AdeArchitecture([string] $Architecture) {
    switch ($Architecture.ToLowerInvariant()) {
        { $_ -in 'arm64', 'aarch64' } { return 'arm64' }
        { $_ -in 'amd64', 'x86_64', 'x64' } { return 'amd64' }
        default { throw "Unknown architecture / Unbekannte Architektur: $Architecture" }
    }
}

function Get-AdePlatform([string[]] $NativeArguments) {
    $value = @(& podman @NativeArguments)
    if ($LASTEXITCODE -ne 0 -or $value.Count -ne 1 -or $value[0] -notmatch '^linux/([^/]+)$') {
        throw 'Cannot determine Linux platform from Podman.'
    }
    return 'linux/' + (ConvertTo-AdeArchitecture $Matches[1])
}

$hostArchitecture = [System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture.ToString()
if ($IsMacOS) {
    # Hardware detection also works when this PowerShell process is translated.
    $appleArm = & sysctl -n hw.optional.arm64
    if ($LASTEXITCODE -ne 0 -or "$appleArm" -notin '0', '1') { throw 'Cannot determine Apple hardware architecture.' }
    if ("$appleArm" -eq '1') { $hostArchitecture = 'arm64' }
} elseif (-not ($IsLinux -or $IsWindows)) {
    throw 'Unsupported host OS.'
}
$native = 'linux/' + (ConvertTo-AdeArchitecture $hostArchitecture)
if ($AllowCrossArchitecture -and -not $Platform) { throw 'Cross-build approval requires an explicit -Platform.' }
if (-not $Platform) { $Platform = $native }
if ($Platform -cnotin 'linux/arm64', 'linux/amd64') { throw "Unsupported target platform: $Platform" }
foreach ($setting in 'DOCKER_DEFAULT_PLATFORM', 'CONTAINER_DEFAULT_PLATFORM') {
    $value = [Environment]::GetEnvironmentVariable($setting)
    if ($value -and $value -cne $Platform) { throw "$setting=$value conflicts with target $Platform" }
}
$engine = Get-AdePlatform @('info', '--format', '{{.Host.OS}}/{{.Host.Arch}}')
if (-not $AllowCrossArchitecture -and ($Platform -ne $native -or $engine -ne $native)) {
    throw "Native architecture required: host=$native engine=$engine target=$Platform"
}
if ($ImageName) {
    $observed = Get-AdePlatform @('image', 'inspect', '--format', '{{.Os}}/{{.Architecture}}', $ImageName)
    if ($observed -ne $Platform) { throw "Image platform mismatch: expected=$Platform observed=$observed" }
}
[Console]::Error.WriteLine("Architecture OK: host=$native engine=$engine target=$Platform cross=$([bool]$AllowCrossArchitecture)")
$Platform
