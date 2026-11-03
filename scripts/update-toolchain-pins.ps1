#Requires -Version 7
<#
.SYNOPSIS
Prueft Toolchain-Pins und bereitet gepruefte Update-Payloads vor.
Checks toolchain pins and prepares verified update payloads.
.DESCRIPTION
Check liest Hersteller-Metadaten ohne Repository-Schreibzugriff. Prepare
erzeugt genau einen gruppengebundenen Vorschlag ausserhalb des Repositorys.
Verify prueft eine Payload ohne Netzwerk; Apply schreibt nur den vorher
verifizierten Dockerfile-Inhalt. Keine Installation, Container-Aktion oder
Git-Lieferung. Check reads upstream metadata without repository writes.
Prepare emits one group-bound proposal outside the repository. Verify checks
a payload offline; Apply writes only its verified Dockerfile content.
No installation, container operation, or Git delivery occurs in this script.
.PARAMETER Action
Check (Standard), Prepare, Verify oder Apply. Check is the read-only default.
.PARAMETER Repo
Repository-Wurzel / repository root.
.PARAMETER OutputDirectory
Neues externes Payload-Verzeichnis fuer Prepare; optionale Check-Ausgabe.
New external payload directory for Prepare; optional Check report output.
.PARAMETER PayloadDirectory
Externes Payload-Verzeichnis fuer Verify/Apply. External Verify/Apply input.
.PARAMETER SkipGroups
Gruppen mit bereits offenem PR ueberspringen / skip groups with an open PR.
.PARAMETER Json
JSON-Ausgabe statt Kurzbericht / emit JSON instead of a short report.
.EXAMPLE
bash scripts/update-toolchain-pins.sh --action Check --json
.EXAMPLE
pwsh -NoProfile -File scripts/update-toolchain-pins.ps1 -Action Prepare -OutputDirectory /tmp/new-pin-payload
.EXAMPLE
pwsh -NoProfile -File scripts/update-toolchain-pins.ps1 -Action Apply -PayloadDirectory /tmp/new-pin-payload -WhatIf
#>
[CmdletBinding(SupportsShouldProcess, ConfirmImpact='Low')]
param(
    [ValidateSet('Check','Prepare','Verify','Apply')][string]$Action='Check',
    [string]$Repo=(Split-Path $PSScriptRoot -Parent),
    [string]$OutputDirectory='',
    [string]$PayloadDirectory='',
    [string[]]$SkipGroups=@(),
    [switch]$Json
)
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
Import-Module (Join-Path $PSScriptRoot 'lib/toolchain-pins.psm1') -Force

function Get-AdePinGitHead {
    param([string]$Directory)
    $result = & git -c core.fsmonitor=false -C $Directory rev-parse HEAD
    if ($LASTEXITCODE -ne 0 -or $result -cnotmatch '^[a-f0-9]{40}$') { throw 'Cannot bind the source Git revision.' }
    $result
}

function Assert-AdeExternalPinDirectory {
    param([string]$Path,[string]$Root,[switch]$New)
    if (-not $Path) { throw 'An external payload directory is required.' }
    $full = [IO.Path]::GetFullPath($Path)
    $comparison = if ($IsWindows) {[StringComparison]::OrdinalIgnoreCase} else {[StringComparison]::Ordinal}
    if ($full.Equals($Root,$comparison) -or $full.StartsWith($Root+[IO.Path]::DirectorySeparatorChar,$comparison)) { throw 'Payload must stay outside the repository.' }
    $cursor = $full
    while ($cursor) {
        if ((Test-Path -LiteralPath $cursor) -and (Get-Item -LiteralPath $cursor -Force).LinkType) { throw 'Symlink payload paths are not allowed.' }
        $cursor = Split-Path $cursor -Parent
    }
    if ($New -and (Test-Path -LiteralPath $full)) { throw 'Payload output directory must be new.' }
    $full
}

try {
    $context = Get-AdePinContext $Repo
    if ($Action -in @('Verify','Apply')) {
        $payload = Assert-AdeExternalPinDirectory $PayloadDirectory $context.root
        foreach ($leaf in @('proposal.json','Dockerfile')) {
            $file = Get-Item -LiteralPath (Join-Path $payload $leaf)
            if ($file.LinkType -or $file.Length -gt 2MB -or $file.PSIsContainer) { throw 'Invalid payload file.' }
        }
        $proposal = Get-Content (Join-Path $payload 'proposal.json') -Raw | ConvertFrom-Json -AsHashtable
        if ($proposal.schemaVersion -ne 1 -or $proposal.baseHead -cne (Get-AdePinGitHead $context.root) -or
            $proposal.baseSha256 -cne (Get-AdePinTextHash $context.text)) { throw 'Payload source revision/content has drifted.' }
        $expected = Update-AdePinDockerfile $context $proposal
        $received = [IO.File]::ReadAllText((Join-Path $payload 'Dockerfile'))
        if ($received -cne $expected -or $proposal.resultSha256 -cne (Get-AdePinTextHash $expected)) { throw 'Payload contains unapproved Dockerfile changes.' }
        $written = $false
        if ($Action -ceq 'Apply' -and $PSCmdlet.ShouldProcess('Dockerfile','Apply verified version and architecture hashes')) {
            $target = Join-Path $context.root 'Dockerfile'
            $temporary = Join-Path $context.root ('.pin-update-'+[guid]::NewGuid().ToString('N'))
            try {
                [IO.File]::WriteAllText($temporary,$expected,[Text.UTF8Encoding]::new($false))
                [IO.File]::Move($temporary,$target,$true)
                $written = $true
            } finally { if (Test-Path -LiteralPath $temporary) { Remove-Item -LiteralPath $temporary } }
        }
        $result = @{status='Verified';group=$proposal.group;changed=$written;sha256=$proposal.resultSha256}
    } else {
        foreach ($group in $SkipGroups) { if ($group -cnotmatch '^[A-Z][A-Z0-9_]*$') { throw 'Invalid skipped group identifier.' } }
        $result = Get-AdePinReport $context
        if ($OutputDirectory) {
            $output = Assert-AdeExternalPinDirectory $OutputDirectory $context.root -New
            $null = New-Item -ItemType Directory -Path $output
            $result | ConvertTo-Json -Depth 24 | Set-Content (Join-Path $output 'report.json') -Encoding utf8NoBOM
        } elseif ($Action -ceq 'Prepare') { throw 'Prepare requires OutputDirectory.' }
        if ($Action -ceq 'Prepare' -and $result.status -ceq 'Ready') {
            $status = @(& git -c core.fsmonitor=false -C $context.root status --porcelain=v1 --untracked-files=all)
            if ($LASTEXITCODE -ne 0 -or $status.Count) { throw 'Prepare requires a clean committed checkout.' }
            $candidates = @($result.groups | Where-Object {$_.status -ceq 'Candidate' -and $_.group -cnotin $SkipGroups})
            if ($candidates.Count) {
                $selected = $candidates[0]
                $changed = Update-AdePinDockerfile $context $selected
                $proposal = @{schemaVersion=1;baseHead=(Get-AdePinGitHead $context.root);baseSha256=(Get-AdePinTextHash $context.text);
                    resultSha256=(Get-AdePinTextHash $changed);group=$selected.group;updates=$selected.updates;hashes=$selected.hashes;source=$selected.source}
                [IO.File]::WriteAllText((Join-Path $output 'Dockerfile'),$changed,[Text.UTF8Encoding]::new($false))
                $proposal | ConvertTo-Json -Depth 16 | Set-Content (Join-Path $output 'proposal.json') -Encoding utf8NoBOM
                $result.selectedGroup = $selected.group
            }
        }
    }
    if ($Json) { $result | ConvertTo-Json -Depth 24 }
    else { Write-Output "Pin-Pruefung / Pin check: $($result.status). Keine Git-Lieferung / no Git delivery." }
    if ($result.status -ceq 'Blocked') { exit 1 }
    exit 0
} catch {
    [Console]::Error.WriteLine('Pin-Update blockiert / blocked: '+$_.Exception.Message)
    exit 2
}
