[CmdletBinding()]
param(
    [string]$ImageName = "",
    [string]$SbomDir = "",
    [ValidateSet("auto", "docker", "podman")]
    [string]$Runtime = "auto",
    [string]$SyftImage = "",
    [switch]$SkipBuild
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($ImageName)) {
    if ($env:IMAGE_NAME) {
        $ImageName = $env:IMAGE_NAME
    } else {
        $ImageName = "localhost/ade-dev-sandbox-ade:latest"
    }
}

if ([string]::IsNullOrWhiteSpace($SbomDir)) {
    if ($env:SBOM_DIR) {
        $SbomDir = $env:SBOM_DIR
    } else {
        $SbomDir = "sboms"
    }
}

if ([string]::IsNullOrWhiteSpace($SyftImage)) {
    if ($env:SYFT_IMAGE) {
        $SyftImage = $env:SYFT_IMAGE
    } else {
        $SyftImage = "docker.io/anchore/syft:latest"
    }
}

if ($Runtime -eq "auto" -and $env:CONTAINER_RUNTIME) {
    $Runtime = $env:CONTAINER_RUNTIME
}

function Resolve-ContainerRuntime {
    param([string]$Name)

    if ($Name -ne "auto") {
        $cmd = Get-Command $Name -ErrorAction Stop
        return $cmd.Source
    }

    foreach ($candidate in @("podman", "docker")) {
        $cmd = Get-Command $candidate -ErrorAction SilentlyContinue
        if ($cmd) {
            return $cmd.Source
        }
    }

    throw "Neither podman nor docker was found in PATH."
}

function Invoke-Native {
    param(
        [string]$FilePath,
        [string[]]$Arguments
    )

    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code ${LASTEXITCODE}: $FilePath $($Arguments -join ' ')"
    }
}

$runtimeExe = Resolve-ContainerRuntime -Name $Runtime
New-Item -ItemType Directory -Force -Path $SbomDir | Out-Null
$sbomDirPath = (Resolve-Path $SbomDir).ProviderPath

if (-not $SkipBuild) {
    Invoke-Native -FilePath $runtimeExe -Arguments @("build", "--pull", "-t", $ImageName, ".")
}

$dateStamp = Get-Date -Format "yyyy-MM-dd"
$safeImage = $ImageName -replace "[/:@\\]+", "-" -replace "[^A-Za-z0-9._-]", ""
$outFile = "$dateStamp-$safeImage.cdx.json"
$outPath = Join-Path $sbomDirPath $outFile

$syft = Get-Command syft -ErrorAction SilentlyContinue
if ($syft) {
    Invoke-Native -FilePath $syft.Source -Arguments @($ImageName, "-o", "cyclonedx-json=$outPath")
} else {
    $tempDir = Join-Path ([System.IO.Path]::GetTempPath()) ("ade-sbom-" + [guid]::NewGuid().ToString())
    New-Item -ItemType Directory -Force -Path $tempDir | Out-Null
    try {
        $archivePath = Join-Path $tempDir "image.tar"
        Invoke-Native -FilePath $runtimeExe -Arguments @("save", $ImageName, "-o", $archivePath)
        Invoke-Native -FilePath $runtimeExe -Arguments @(
            "run",
            "--rm",
            "-v",
            "${tempDir}:/work:ro",
            "-v",
            "${sbomDirPath}:/out",
            $SyftImage,
            "docker-archive:/work/image.tar",
            "-o",
            "cyclonedx-json=/out/$outFile"
        )
    } finally {
        Remove-Item -LiteralPath $tempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}

if (-not (Test-Path -LiteralPath $outPath)) {
    throw "SBOM was not created: $outPath"
}

if ((Get-Item -LiteralPath $outPath).Length -eq 0) {
    throw "SBOM is empty: $outPath"
}

Write-Output "SBOM written: $outPath"
