#Requires -Version 7
[CmdletBinding()]
param(
    [Parameter(Mandatory, Position = 0)]
    [ValidateSet('build', 'up', 'recreate')] [string] $Action,
    [string] $Platform = '',
    [switch] $AllowCrossArchitecture,
    [switch] $HomeBaseline
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Invoke-AdeCompose([string[]] $NativeArguments) {
    & podman compose @composeFiles @NativeArguments
    if ($LASTEXITCODE -ne 0) { throw "Compose failed: $($NativeArguments -join ' ')" }
}

$architectureArguments = @{ Platform = $Platform; AllowCrossArchitecture = $AllowCrossArchitecture }
$targetPlatform = & "$PSScriptRoot/check-container-architecture.ps1" @architectureArguments
$image = 'localhost/absdd-image-sandbox_ade:latest'
$override = $null
Push-Location "$PSScriptRoot/.."
try {
    $composeFiles = @('-f', 'compose.yml')
    if ($HomeBaseline) { $composeFiles += @('-f', 'compose.home-baseline.yml') }
    $override = [System.IO.Path]::GetTempFileName()
    "services:`n  ade:`n    image: $image`n    platform: $targetPlatform" |
        Set-Content -LiteralPath $override -Encoding utf8NoBOM
    $composeFiles += @('-f', $override)
    Invoke-AdeCompose @('config') | Out-Null
    if ($Action -eq 'build') {
        Invoke-AdeCompose @('build', '--pull', '--', 'ade')
        $null = & "$PSScriptRoot/check-container-architecture.ps1" @architectureArguments -ImageName $image
        return
    }
    $null = & "$PSScriptRoot/check-container-architecture.ps1" @architectureArguments -ImageName $image
    $expectedImage = & podman image inspect --format '{{.Id}}' $image
    if ($LASTEXITCODE -ne 0) { throw 'Cannot inspect expected ADE image.' }
    if ($Action -eq 'recreate') {
        Write-Warning 'Recreate: back up non-persistent container files first. Volumes are retained.'
        Invoke-AdeCompose @('up', '-d', '--no-build', '--pull', 'never', '--force-recreate', 'ade')
    } else {
        $existing = @(Invoke-AdeCompose @('ps', '-q'))
        if ($existing.Count -gt 1) { throw 'Expected at most one ADE container.' }
        if ($existing.Count -eq 1 -and $existing[0]) {
            $existingImage = & podman inspect --format '{{.Image}}' $existing[0]
            if ($LASTEXITCODE -ne 0 -or $existingImage -ne $expectedImage) {
                throw 'Existing container uses an older image; back up its files, then use recreate.'
            }
        }
        Invoke-AdeCompose @('up', '-d', '--no-build', '--pull', 'never', '--no-recreate', 'ade')
    }
    $containers = @(Invoke-AdeCompose @('ps', '-q'))
    if ($containers.Count -ne 1 -or -not $containers[0]) { throw 'Expected exactly one ADE container.' }
    $containerImage = & podman inspect --format '{{.Image}}' $containers[0]
    if ($LASTEXITCODE -ne 0) { throw 'Cannot inspect ADE container.' }
    $null = & "$PSScriptRoot/check-container-architecture.ps1" @architectureArguments -ImageName $containerImage
    if ($expectedImage -ne $containerImage) {
        throw 'Existing container uses an older image; back up its files, then use recreate.'
    }
} finally {
    if ($override) { Remove-Item -LiteralPath $override -Force }
    Pop-Location
}
