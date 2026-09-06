#Requires -Version 7
<#
.SYNOPSIS
    Erzeugt eine CycloneDX-SBOM. / Creates a CycloneDX SBOM.
.DESCRIPTION
    Baut optional das lokale Podman-Image und nutzt ausschliesslich Syft aus
    dem Image oder die exakt angegebene Host-Version. Ein beweglicher
    Container-Fallback ist verboten. / Optionally builds the local Podman image
    and uses only image-integrated Syft or the exact host version. Moving
    container fallbacks are refused.
.PARAMETER ImageName
    Lokales Image / local image.
.PARAMETER SbomDir
    Zielverzeichnis / output directory.
.PARAMETER Runtime
    Nur Podman / Podman only.
.PARAMETER SyftVersion
    Exakt erlaubte Host-Version / exact allowed host version.
.PARAMETER SkipBuild
    Vorhandenes Image verwenden / use the existing image.
.EXAMPLE
    pwsh -NoProfile -File scripts/build-and-sbom.ps1 -SkipBuild -WhatIf
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [string] $ImageName = '',
    [string] $SbomDir = '',
    [ValidateSet('podman')] [string] $Runtime = 'podman',
    [string] $SyftVersion = '1.46.0',
    [switch] $SkipBuild
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Invoke-AdeNativeCommand {
    param([Parameter(Mandatory)] [string] $FilePath, [string[]] $Arguments = @())
    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code ${LASTEXITCODE}: $FilePath $($Arguments -join ' ')"
    }
}

function New-AdeSandboxSbom {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory)] [string] $TargetImage,
        [Parameter(Mandatory)] [string] $OutputDirectory,
        [Parameter(Mandatory)] [string] $ContainerRuntime,
        [Parameter(Mandatory)] [string] $RequiredSyftVersion,
        [switch] $UseExistingImage
    )

    if ($ContainerRuntime -ne 'podman') {
        throw "Unsupported container runtime: $ContainerRuntime. This repository uses Podman only."
    }
    $runtimeCommand = Get-Command podman -ErrorAction Stop

    if (-not $PSCmdlet.ShouldProcess($TargetImage, 'Build image and create CycloneDX SBOM')) {
        Write-Output "WHATIF: $($runtimeCommand.Source) build --pull -t <local-image> . (unless -SkipBuild)"
        Write-Output "WHATIF: require image-integrated Syft or host Syft exactly $RequiredSyftVersion; no moving container fallback"
        Write-Output "WHATIF: write one CycloneDX JSON file below $OutputDirectory"
        return
    }

    New-Item -ItemType Directory -Force -Path $OutputDirectory | Out-Null
    $resolvedOutput = (Resolve-Path -LiteralPath $OutputDirectory).ProviderPath
    if (-not $UseExistingImage) {
        Invoke-AdeNativeCommand -FilePath $runtimeCommand.Source -Arguments @('build', '--pull', '-t', $TargetImage, '.')
    }

    $safeImage = $TargetImage -replace '[/:@\\]+', '-' -replace '[^A-Za-z0-9._-]', ''
    $outPath = Join-Path $resolvedOutput "$(Get-Date -Format 'yyyy-MM-dd')-$safeImage.cdx.json"
    $sourceVersion = ($TargetImage -split ':')[-1]

    & $runtimeCommand.Source @('run', '--rm', '--entrypoint', 'syft', $TargetImage, 'version') *> $null
    $imageSyftAvailable = $LASTEXITCODE -eq 0
    $hostSyft = Get-Command syft -ErrorAction SilentlyContinue
    if ($imageSyftAvailable) {
        & $runtimeCommand.Source @(
            'run', '--rm', '--user', '0', '--entrypoint', 'syft', $TargetImage,
            'dir:/', '--select-catalogers', '+javascript-package-cataloger',
            '--source-name', $TargetImage, '--source-version', $sourceVersion,
            '-o', 'cyclonedx-json'
        ) | Set-Content -LiteralPath $outPath -Encoding utf8NoBOM
        if ($LASTEXITCODE -ne 0) { throw "Image-integrated Syft failed with exit code $LASTEXITCODE." }
    } elseif ($hostSyft) {
        $versionLine = @(& $hostSyft.Source version 2>$null | Where-Object { $_ -match '^Version:' } | Select-Object -First 1)
        $observedVersion = if ($versionLine.Count -eq 1) { ($versionLine[0] -split ':', 2)[1].Trim() } else { '<unknown>' }
        if ($observedVersion -ne $RequiredSyftVersion) {
            throw "Host Syft version mismatch: expected $RequiredSyftVersion, observed $observedVersion."
        }
        Invoke-AdeNativeCommand -FilePath $hostSyft.Source -Arguments @($TargetImage, '-o', "cyclonedx-json=$outPath")
    } else {
        throw "Syft is unavailable in the image and host Syft $RequiredSyftVersion is unavailable; refusing an unpinned fallback."
    }

    if (-not (Test-Path -LiteralPath $outPath -PathType Leaf) -or (Get-Item -LiteralPath $outPath).Length -eq 0) {
        throw "SBOM was not created or is empty: $outPath"
    }
    Write-Output "SBOM written: $outPath"
}

if (-not $ImageName) { $ImageName = if ($env:IMAGE_NAME) { $env:IMAGE_NAME } else { 'localhost/absdd-image-sandbox_ade:latest' } }
if (-not $SbomDir) { $SbomDir = if ($env:SBOM_DIR) { $env:SBOM_DIR } else { 'sboms' } }
New-AdeSandboxSbom -TargetImage $ImageName -OutputDirectory $SbomDir -ContainerRuntime $Runtime -RequiredSyftVersion $SyftVersion -UseExistingImage:$SkipBuild -WhatIf:$WhatIfPreference
