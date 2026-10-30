<#
.SYNOPSIS
Prüft Archiv-Link-Grenzen mit isolierten Positiv-/Negativfällen.
Tests archive-link boundaries with isolated positive and negative fixtures.
.DESCRIPTION
Erzeugt nur ein eigenes temporäres Fixture und entfernt dieses wieder.
Creates and removes only its own temporary fixture.
#>
[CmdletBinding()]
param()
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$checker = Join-Path $PSScriptRoot '../check-archived-markdown-links.ps1'
$temporary = Join-Path ([IO.Path]::GetTempPath()) ('archive-links-' + [guid]::NewGuid())
$null = New-Item -ItemType Directory -Path $temporary
try {
    $entries = @()
    foreach ($name in @('one', 'two', 'three')) {
        $path = "specs/intake-review-archive/11111111-1111-4111-8111-111111111111/22222222-2222-4222-8222-222222222222/$name.md"
        $file = Join-Path $temporary $path
        $null = New-Item -ItemType Directory -Path (Split-Path $file) -Force
        [IO.File]::WriteAllText($file, "[a](a.md) [b](b.md) [c](c.md)`n")
        $entries += [ordered]@{archivePath=$path;originalPath='original.md';rawSha256=(Get-FileHash $file).Hash.ToLowerInvariant();targets=@('a.md','b.md','c.md')}
    }
    foreach ($name in @('original', 'a', 'b', 'c')) {
        [IO.File]::WriteAllText((Join-Path $temporary "$name.md"), "# Fixture`n")
    }
    $workflow = Join-Path $temporary '.github/workflows/documentation-and-sandbox.yml'
    $null = New-Item -ItemType Directory -Path (Split-Path $workflow) -Force
    $lines = @($entries | ForEach-Object { "--exclude-path '^$($_.archivePath.Replace('.', '\.'))$'" }) -join "`n"
    [IO.File]::WriteAllText($workflow, $lines)
    $manifest = Join-Path $temporary 'manifest.json'
    $config = [ordered]@{schemaVersion='1.0';files=$entries}
    function Write-Fixture { [IO.File]::WriteAllText($manifest, ($config | ConvertTo-Json -Depth 10)) }
    function Assert-Rejected([string]$Case) {
        $caught = $false
        try { & $checker -Repo $temporary -Manifest manifest.json | Out-Null } catch { $caught = $true }
        if (-not $caught) { throw "Negative fixture unexpectedly passed: $Case" }
        Write-Output "PASS: reject $Case"
    }
    Write-Fixture
    & $checker -Repo $temporary -Manifest manifest.json
    $archive = Join-Path $temporary $entries[0].archivePath
    $originalBytes = [IO.File]::ReadAllBytes($archive)
    [IO.File]::AppendAllText($archive, 'changed')
    Assert-Rejected 'changed archive bytes'
    [IO.File]::WriteAllBytes($archive, $originalBytes)
    Move-Item (Join-Path $temporary 'a.md') (Join-Path $temporary 'a.saved')
    Assert-Rejected 'missing target'
    Move-Item (Join-Path $temporary 'a.saved') (Join-Path $temporary 'a.md')
    $entries[0].originalPath = '../outside.md'; Write-Fixture
    Assert-Rejected 'escaping original context'
    $entries[0].originalPath = 'original.md'
    $entries[0].targets = @('wrong.md'); Write-Fixture
    Assert-Rejected 'wrong declared destinations'
    $entries[0].targets = @('a.md','b.md','c.md'); Write-Fixture
    [IO.File]::WriteAllText($workflow, '--exclude-path specs/intake-review-archive')
    Assert-Rejected 'blanket workflow exclusion instead of exact paths'
    [IO.File]::WriteAllText($workflow, $lines)
    $config.files = @($entries[0],$entries[0],$entries[2]); Write-Fixture
    Assert-Rejected 'duplicate archive path'
    $config.files = $entries; Write-Fixture
    & $checker -Repo $temporary -Manifest manifest.json
    Write-Output 'PASS: archive-link fixture suite, 1 positive contract and 6 negative cases'
} finally {
    # Only this invocation owns this exact fresh fixture path.
    Remove-Item -LiteralPath $temporary -Recurse -Force
}
