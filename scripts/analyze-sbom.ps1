[CmdletBinding()]
param(
    [string]$SbomPath = "",
    [string]$Search = "",
    [string]$ComponentType = "",
    [int]$Top = 20,
    [switch]$Scan,
    [ValidateSet("auto", "grype", "trivy")]
    [string]$Scanner = "auto"
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = "Stop"

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
    $scannerCommand = $null
    if ($Scanner -eq "auto" -or $Scanner -eq "grype") {
        $scannerCommand = Get-Command grype -ErrorAction SilentlyContinue
    }
    if (-not $scannerCommand -and ($Scanner -eq "auto" -or $Scanner -eq "trivy")) {
        $scannerCommand = Get-Command trivy -ErrorAction SilentlyContinue
    }

    if (-not $scannerCommand) {
        throw "No vulnerability scanner found. Install grype or trivy, then rerun with -Scan."
    }

    Write-Output ""
    Write-Output "Vulnerability scan with $($scannerCommand.Name):"
    if ($scannerCommand.Name -eq "grype") {
        & $scannerCommand.Source $resolvedSbom
    } else {
        & $scannerCommand.Source sbom $resolvedSbom
    }

    if ($LASTEXITCODE -ne 0) {
        throw "Scanner exited with code $LASTEXITCODE."
    }
}
