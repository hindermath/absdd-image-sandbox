<#
.SYNOPSIS
Prüft exakt gebundene Archivlinks am ursprünglichen Dokumentort.
Checks hash-bound archive links relative to the original document path.
.DESCRIPTION
Bewahrt Archivbytes. Nur drei deklarierte Markdown-Dateien dürfen im normalen
Linkscan ausgenommen werden, nachdem Hash, Quellort und alle neun lokalen
Ziele geprüft wurden. Kein Netzwerkzugriff und keine Dateischreiboperation.
Preserves archived bytes. Exactly three declared files may leave the ordinary
link scan only after their hashes, source contexts and nine local destinations
pass validation. No network or filesystem writes.
.PARAMETER Repo
Repository-Wurzel / Repository root.
.PARAMETER Manifest
Repo-relatives Hashmanifest / Repository-relative hash manifest.
#>
[CmdletBinding()]
param(
    [string]$Repo = '.',
    [string]$Manifest = 'scripts/config/archived-markdown-links.json'
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$root = [IO.Path]::GetFullPath((Resolve-Path -LiteralPath $Repo).Path)
function Resolve-ArchiveLinkPath([string]$Relative) {
    if ([IO.Path]::IsPathRooted($Relative) -or $Relative.Contains('\')) {
        throw "AL001: invalid repository path: $Relative"
    }
    $full = [IO.Path]::GetFullPath((Join-Path $root $Relative))
    if (-not $full.StartsWith($root + [IO.Path]::DirectorySeparatorChar, [StringComparison]::Ordinal)) {
        throw "AL001: path escapes repository: $Relative"
    }
    # Archive checks must not follow a filesystem link outside the reviewed tree.
    $cursor = $root
    foreach ($part in [IO.Path]::GetRelativePath($root, $full).Split([IO.Path]::DirectorySeparatorChar)) {
        $cursor = Join-Path $cursor $part
        $item = Get-Item -LiteralPath $cursor -Force -ErrorAction Stop
        if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw "AL001: filesystem links are not archive evidence: $Relative"
        }
    }
    if (-not [IO.File]::Exists($full)) { throw "AL002: missing file: $Relative" }
    return $full
}
$config = Get-Content -LiteralPath (Resolve-ArchiveLinkPath $Manifest) -Raw | ConvertFrom-Json
if ($config.schemaVersion -ne '1.0' -or @($config.files).Count -ne 3) {
    throw 'AL003: expected schema 1.0 and exactly three archive files'
}
$workflow = Get-Content -LiteralPath (Resolve-ArchiveLinkPath '.github/workflows/documentation-and-sandbox.yml') -Raw
$seen = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$count = 0
foreach ($entry in $config.files) {
    if (-not $seen.Add($entry.archivePath) -or $entry.archivePath -notmatch '^specs/intake-(review|series)-archive/[0-9a-f-]+/[0-9a-f-]+/[a-z-]+\.md$') {
        throw 'AL003: duplicate or unbounded archive entry'
    }
    $archive = Resolve-ArchiveLinkPath $entry.archivePath
    $null = Resolve-ArchiveLinkPath $entry.originalPath
    $hash = (Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($hash -cne $entry.rawSha256) { throw "AL004: archive bytes changed: $($entry.archivePath)" }
    $pattern = '^' + $entry.archivePath.Replace('.', '\.') + '$'
    if (-not $workflow.Contains("--exclude-path '$pattern'")) {
        throw "AL005: missing exact workflow exclusion: $($entry.archivePath)"
    }
    $body = [IO.File]::ReadAllText($archive, [Text.UTF8Encoding]::new($false, $true))
    $linkMatches = [regex]::Matches($body, '\[[^\]\r\n]*\]\(([^)\r\n]+)\)')
    $targets = @()
    foreach ($match in $linkMatches) {
        $link = $match.Groups[1].Value
        # These exact snapshots contain only plain local links. Refuse a changed
        # link syntax instead of silently skipping an untested destination.
        if ($link -match '[:#?\s<>]' -or $link -eq '') { throw "AL006: unexpected link syntax: $link" }
        $relative = [IO.Path]::GetRelativePath($root, [IO.Path]::GetFullPath((Join-Path (Split-Path (Join-Path $root $entry.originalPath)) $link))).Replace('\', '/')
        $null = Resolve-ArchiveLinkPath $relative
        $targets += $relative
        $count++
    }
    if (($targets -join "`n") -cne (@($entry.targets) -join "`n")) {
        throw "AL007: link inventory/context changed: $($entry.archivePath)"
    }
}
if ($count -ne 9) { throw "AL007: expected nine archive links, found $count" }
Write-Output 'PASS: 3 immutable archive hashes and 9 original-context local links; no writes'
