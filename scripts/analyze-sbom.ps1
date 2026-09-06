#Requires -Version 7
<#
.SYNOPSIS
    Analysiert eine CycloneDX-SBOM. / Analyzes a CycloneDX SBOM.
.DESCRIPTION
    Fasst Komponenten zusammen und startet optional ausschliesslich das
    version- und digest-gepinnte Grype-Image mit read-only SBOM-Mount. / Summarizes
    components and optionally runs only the version- and digest-pinned Grype
    image with a read-only SBOM mount.
.PARAMETER SbomPath
    SBOM-Datei; leer waehlt die neueste lokale Datei. / SBOM path; empty selects the latest local file.
.PARAMETER Scan
    Gepinnten Scan ausfuehren / run the pinned scan.
.PARAMETER Scanner
    `auto` und `grype` waehlen beide den gepinnten Pfad. / Both values select the pinned path.
.PARAMETER ScanOutput
    Optionaler JSON-Ausgabepfad / optional JSON output path.
.EXAMPLE
    pwsh -NoProfile -File scripts/analyze-sbom.ps1 -Scan -Scanner grype -WhatIf
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$SbomPath = "",
    [string]$Search = "",
    [string]$ComponentType = "",
    [int]$Top = 20,
    [switch]$Scan,
    [ValidateSet("auto", "grype")]
    [string]$Scanner = "auto",
    [string]$ScanOutput = "",
    [string]$GrypeImage = "ghcr.io/anchore/grype:v0.117.0@sha256:ddf9e9f204049f3a4a0955ef70873cabab6a31432125ad4f20a490b54950a253"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if ($WhatIfPreference) {
    Write-Output "WHATIF: summarize CycloneDX input without writes"
    if ($Scan) {
        Write-Output "WHATIF: podman run --rm <read-only-sbom-mount> $GrypeImage sbom:/work/<sbom>"
    }
    exit 0
}

if ([string]::IsNullOrWhiteSpace($SbomPath)) {
    $latest = Get-ChildItem -Path "sboms" -Filter "*.cdx.json" -File -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1

    if (-not $latest) {
        throw "No SBOM found. Generate one with .\scripts\build-and-sbom.ps1 first."
    }

    $SbomPath = $latest.FullName
}

$resolvedSbom = (Resolve-Path -LiteralPath $SbomPath).ProviderPath
$sbom = Get-Content -Raw -LiteralPath $resolvedSbom | ConvertFrom-Json
$allComponents = @($sbom.components)

function Get-PurlType {
    param([string]$Purl)

    if ([string]::IsNullOrWhiteSpace($Purl)) {
        return "<none>"
    }

    if ($Purl -match "^pkg:([^/]+)/") {
        return $Matches[1]
    }

    return "<unknown>"
}

function Get-ComponentValue {
    param(
        $Component,
        [string]$Name
    )

    if ($Component.PSObject.Properties.Name.Contains($Name)) {
        return $Component.$Name
    }

    return ""
}

function Get-LicenseNames {
    param($Component)

    if (-not $Component.PSObject.Properties.Name.Contains("licenses")) {
        return @("<none>")
    }

    $names = @()
    foreach ($entry in @($Component.licenses)) {
        if ($entry.PSObject.Properties.Name.Contains("license")) {
            if ($entry.license.PSObject.Properties.Name.Contains("id") -and $entry.license.id) {
                $names += $entry.license.id
            } elseif ($entry.license.PSObject.Properties.Name.Contains("name") -and $entry.license.name) {
                $names += $entry.license.name
            }
        } elseif ($entry.PSObject.Properties.Name.Contains("expression") -and $entry.expression) {
            $names += $entry.expression
        }
    }

    if ($names.Count -eq 0) {
        return @("<none>")
    }

    return $names
}

$components = $allComponents
if (-not [string]::IsNullOrWhiteSpace($ComponentType)) {
    $components = @(
        $allComponents |
            Where-Object { (Get-ComponentValue -Component $_ -Name "type") -eq $ComponentType }
    )
}

Write-Output "SBOM: $resolvedSbom"
Write-Output "Format: $($sbom.bomFormat) $($sbom.specVersion)"
Write-Output "Generated: $($sbom.metadata.timestamp)"
Write-Output "Components: $($allComponents.Count)"
if (-not [string]::IsNullOrWhiteSpace($ComponentType)) {
    Write-Output "Filtered components: $($components.Count) type=$ComponentType"
}

if ($sbom.metadata.PSObject.Properties.Name.Contains("tools")) {
    $tools = @(
        @($sbom.metadata.tools.components) |
            ForEach-Object { "$($_.name) $($_.version)" } |
            Where-Object { -not [string]::IsNullOrWhiteSpace($_) }
    )
    if ($tools.Count -gt 0) {
        Write-Output "Tools: $($tools -join ', ')"
    }
}

if ($sbom.metadata.PSObject.Properties.Name.Contains("component")) {
    Write-Output "Target: $($sbom.metadata.component.name) $($sbom.metadata.component.version)"
}

Write-Output ""
Write-Output "Component types:"
$components |
    Group-Object type |
    Sort-Object Count -Descending |
    Select-Object -First $Top Count, Name |
    Format-Table -AutoSize

Write-Output "Package ecosystems from purl:"
$components |
    ForEach-Object { Get-PurlType -Purl (Get-ComponentValue -Component $_ -Name "purl") } |
    Group-Object |
    Sort-Object Count -Descending |
    Select-Object -First $Top Count, Name |
    Format-Table -AutoSize

Write-Output "Licenses:"
$components |
    ForEach-Object { Get-LicenseNames -Component $_ } |
    Group-Object |
    Sort-Object Count -Descending |
    Select-Object -First $Top Count, Name |
    Format-Table -AutoSize

if (-not [string]::IsNullOrWhiteSpace($Search)) {
    Write-Output "Search results for '$Search':"
    $components |
        Where-Object {
            (Get-ComponentValue -Component $_ -Name "name") -match $Search -or
            (Get-ComponentValue -Component $_ -Name "version") -match $Search -or
            (Get-ComponentValue -Component $_ -Name "purl") -match $Search
        } |
        Select-Object -First 100 type, name, version, purl |
        Format-Table -AutoSize
}

if ($Scan) {
    $podman = Get-Command podman -ErrorAction Stop
    $sbomDirectory = Split-Path -Parent $resolvedSbom
    $sbomName = Split-Path -Leaf $resolvedSbom
    Write-Output ""
    Write-Output "Vulnerability scan with pinned Grype image: $GrypeImage"
    $arguments = @("run", "--rm", "-v", "${sbomDirectory}:/work:ro", $GrypeImage, "sbom:/work/$sbomName")
    if ($ScanOutput) {
        $outputDirectory = Split-Path -Parent $ScanOutput
        if ($outputDirectory) { New-Item -ItemType Directory -Force -Path $outputDirectory | Out-Null }
        & $podman.Source @arguments -o json | Set-Content -LiteralPath $ScanOutput -Encoding utf8
    } else {
        & $podman.Source @arguments
    }

    if ($LASTEXITCODE -ne 0) {
        throw "Scanner exited with code $LASTEXITCODE."
    }
}
