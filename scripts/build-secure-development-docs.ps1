<#
.SYNOPSIS
Builds and validates the generated secure-development compendium.

.DESCRIPTION
DE: Prueft eindeutige, vollstaendige aktive Metadaten gegen das Manifest und
erzeugt den Sammelband aus den zwoelf kanonischen Checklisten.
EN: Validates unique complete active metadata against the manifest.
Validates the secure-development manifest, checklist IDs and versions, then
generates the checklist compendium from the twelve canonical checklist files.

.PARAMETER Check
DE: Nur pruefen, keine Dateien aendern.
EN: Check only, without changing files.
Checks that the generated compendium is current without changing files.

.EXAMPLE
pwsh -NoProfile -File scripts/build-secure-development-docs.ps1

.EXAMPLE
pwsh -NoProfile -File scripts/build-secure-development-docs.ps1 -Check
#>
[CmdletBinding()]
param([switch]$Check)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$RepoRoot = Split-Path -Parent $PSScriptRoot
$DocRoot = Join-Path $RepoRoot 'docs/secure-development'
$ManifestPath = Join-Path $DocRoot 'baseline-manifest.json'
$HeaderTemplate = Join-Path $PSScriptRoot 'templates/secure-development-compendium-header.md'

if (-not (Test-Path $ManifestPath)) { throw "Manifest missing: ${ManifestPath}" }
if (-not (Test-Path $HeaderTemplate)) { throw "Header template missing: ${HeaderTemplate}" }

$manifest = Get-Content $ManifestPath -Raw | ConvertFrom-Json
if ($manifest.schemaVersion -ne 1 -or $manifest.checklists.Count -ne 12) {
    throw 'Manifest must use schema version 1 and contain exactly 12 checklists.'
}

# DE: Der erste zusammenhaengende Metadatenblock ist aktiv; doppelte Felder
# oder Treffer im Text duerfen einen falschen aktiven Wert nicht verdecken.
# EN: The first contiguous metadata block is active; duplicate fields and
# body matches must never hide an incorrect active value.
function Assert-DocumentMetadata {
    param([string]$Relative, [string]$Prefix, [string]$Value)
    $path = Join-Path $DocRoot $Relative
    if (-not (Test-Path $path -PathType Leaf)) { throw "Controlled document missing: ${Relative}" }
    $started = $false
    $active = $false
    $count = 0
    $matched = 0
    foreach ($line in Get-Content $path) {
        if (-not $started -and $line -cmatch '^\*\*[^*]+:\*\*') { $started = $true; $active = $true }
        if ($started -and $line -cnotmatch '^\*\*[^*]+:\*\*') { $active = $false }
        if ($line.StartsWith($Prefix, [StringComparison]::Ordinal)) {
            $count++
            if ($active -and $line -ceq "${Prefix} ${Value}") { $matched++ }
        }
    }
    if ($count -ne 1 -or $matched -ne 1) { throw "Active metadata mismatch or duplicate: ${Relative} (${Prefix})" }
}
foreach ($relative in @('README.md') + @($manifest.checklists.path) + @($manifest.relatedDocuments.path) + @($manifest.learningDocuments.path)) {
    Assert-DocumentMetadata $relative '**Baseline-Version / Baseline version:**' $manifest.baselineVersion
}
$actualIds = @($manifest.checklists.id | Sort-Object)
$expectedIds = @(1..12 | ForEach-Object { 'CL-{0:00}' -f $_ })
if (($actualIds -join ',') -cne ($expectedIds -join ',')) { throw 'Expected unique checklist IDs CL-01..CL-12.' }
if ($manifest.guideline.version -cne $manifest.baselineVersion) { throw 'Guideline/baseline version mismatch.' }
$catalog = Get-Content (Join-Path $PSScriptRoot 'config/spec-kit-preset-profiles.json') -Raw | ConvertFrom-Json
$alignment = Get-Content (Join-Path $DocRoot 'mitgeltende-dokumente/Verzahnung_Richtlinie_Checklisten_Spec-Kit-Presets.md') -Raw
foreach ($presetProfileName in $catalog.profiles.PSObject.Properties.Name | Where-Object { $_ -ne 'none' }) {
    if (-not $alignment.Contains('`' + $presetProfileName + '`')) { throw "Profile missing from alignment: ${presetProfileName}" }
}

$guidelinePath = Join-Path $DocRoot $manifest.guideline.path
if (-not (Test-Path $guidelinePath)) { throw "Guideline missing: $($manifest.guideline.path)" }
# DE: Nur die erste Tabelle im benannten Metadatenabschnitt gilt; jeder aktive
# Sprachkopf und jedes Versionsfeld muss eindeutig sein. Historienzeilen bleiben erlaubt.
# EN: Only the first table in the named metadata section is active. Language
# headings and version fields must be unique; history rows remain allowed.
function Assert-GuidelineMetadata {
    param([string]$Heading, [string]$Field)
    $active = $false
    $table = $false
    $ended = $false
    $sections = 0
    $count = 0
    $matched = 0
    foreach ($line in Get-Content $guidelinePath) {
        if ($line.StartsWith('## ', [StringComparison]::Ordinal)) {
            $active = $line -ceq $Heading
            if ($active) { $sections++ }
            $table = $false
            $ended = $false
        }
        if ($active -and $line.StartsWith('|', [StringComparison]::Ordinal) -and -not $ended) { $table = $true }
        if ($active -and $table -and -not $line.StartsWith('|', [StringComparison]::Ordinal)) { $ended = $true }
        if ($line.StartsWith("| ${Field} |", [StringComparison]::Ordinal) -and ($line.Split('|')).Count -eq 4) {
            $count++
            if ($active -and $table -and -not $ended -and $line -ceq "| ${Field} | $($manifest.guideline.version) |") { $matched++ }
        }
    }
    if ($sections -ne 1 -or $count -ne 1 -or $matched -ne 1) {
        throw "Active guideline metadata mismatch or duplicate: $($manifest.guideline.path) (${Field})"
    }
}
Assert-GuidelineMetadata '## Dokumenten-Metadaten' 'Versionsnummer'
Assert-GuidelineMetadata '## Document Metadata' 'Version'

foreach ($document in @($manifest.relatedDocuments) + @($manifest.learningDocuments)) {
    $documentPath = Join-Path $DocRoot $document.path
    if (-not (Test-Path $documentPath)) { throw "Controlled document missing: $($document.path)" }
    Assert-DocumentMetadata $document.path '**Version / Version:**' $document.version
}

foreach ($relative in @($manifest.managedBinaryFiles) + @($manifest.managedReferenceFiles)) {
    if (-not (Test-Path (Join-Path $DocRoot $relative))) { throw "Managed reference missing: ${relative}" }
}

$header = Get-Content $HeaderTemplate -Raw
$content = $header.Replace('{{BASELINE_VERSION}}', [string]$manifest.baselineVersion)
$content = $content.Replace('{{COMPENDIUM_VERSION}}', [string]$manifest.compendium.version)
$content = $content.Replace('{{RELEASE_DATE}}', [string]$manifest.releaseDate)
$content = $content.TrimEnd("`r", "`n") + "`n"
$ids = [System.Collections.Generic.List[string]]::new()

foreach ($checklist in $manifest.checklists) {
    $sourceFile = Join-Path $DocRoot $checklist.path
    if (-not (Test-Path $sourceFile)) { throw "Checklist missing: $($checklist.path)" }
    $source = (Get-Content $sourceFile -Raw) -replace "`r`n", "`n"
    Assert-DocumentMetadata $checklist.path '**Dokument-ID / Document ID:**' $checklist.id
    Assert-DocumentMetadata $checklist.path '**Version / Version:**' $checklist.version
    foreach ($match in [regex]::Matches($source, '(?m)^#### (CL-[0-9]{2}-[0-9]{2}):')) {
        $ids.Add($match.Groups[1].Value)
    }
    $source = $source.Replace('](../Richtlinie_Sichere-Entwicklung.md', '](Richtlinie_Sichere-Entwicklung.md')
    $source = $source.Replace('](../../maintenance/', '](../maintenance/')
    $source = $source.Replace('](../../../constitution.md', '](../../constitution.md')
    $source = $source.Replace('](../README.md', '](README.md')
    $source = $source.Replace('](../mitgeltende-dokumente/', '](mitgeltende-dokumente/')
    $source = $source.Replace('](CL_', '](checklisten/CL_')
    $content += "`n---`n`n" + $source.TrimEnd("`r", "`n") + "`n"
}

if ($ids.Count -ne $manifest.checklistItemCount) {
    throw "Expected $($manifest.checklistItemCount) checklist items, found $($ids.Count)."
}
$duplicates = $ids | Group-Object | Where-Object Count -gt 1
if ($duplicates) { throw "Duplicate checklist IDs: $($duplicates.Name -join ', ')" }

$content += @"

---

## Versionshistorie / Version History

| Version | Datum / Date | Änderung / Change |
|---|---|---|
| $($manifest.compendium.version) | $($manifest.releaseDate) | Aus den zwölf kanonischen Einzelchecklisten der sicheren-Entwicklung-Basis $($manifest.baselineVersion) erzeugt; einheitliches zweiachsiges Statusmodell und klare Trennung zwischen Vorlage und Projektnachweis. / Generated from the twelve canonical individual checklists of secure-development baseline $($manifest.baselineVersion); unified two-axis status model and clear separation between template and project evidence. |
"@
$content = ($content -replace "`r`n", "`n").TrimEnd("`r", "`n") + "`n"
$output = Join-Path $DocRoot $manifest.compendium.path

if ($Check) {
    if (-not (Test-Path $output)) { throw "Generated compendium missing: ${output}" }
    $existing = (Get-Content $output -Raw) -replace "`r`n", "`n"
    if ($existing -ne $content) { throw "Generated compendium is stale: ${output}" }
    Write-Host 'Secure-development generated documents are current.'
} else {
    [System.IO.File]::WriteAllText($output, $content, [System.Text.UTF8Encoding]::new($false))
    Write-Host "Generated ${output}"
}
