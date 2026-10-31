[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [ValidateSet("auto", "podman", "podman-compose")]
    [string]$Engine = "auto",

    [switch]$Volumes,

    [switch]$RemoveOrphans,

    [switch]$DryRun,

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$DownArgs = @()
)

<#
.SYNOPSIS
    Stoppt die ADE-Sandbox nach geprüftem Auditexport. / Stops ADE after a verified audit export.
.DESCRIPTION
    Prüft den Audit-Mount, exportiert aktuelle Metadaten, bewahrt 30 UTC-Tage
    und führt erst danach Compose down aus. Fehler blockieren down. Vorschau
    mit -DryRun oder -WhatIf schreibt nichts. / Verifies the audit mount,
    exports current metadata, retains 30 UTC days, then runs Compose down.
    Failures block down. -DryRun and -WhatIf do not write.
.PARAMETER Engine
    Compose-Anbieter: auto, podman oder podman-compose. / Compose provider.
.PARAMETER Volumes
    Destruktive Volume-Löschung nur nach eigener Datenverlustentscheidung. /
    Destructive volume removal only after a separate data-loss decision.
.PARAMETER RemoveOrphans
    Verwaiste Container entfernen. / Remove orphan containers.
.PARAMETER DryRun
    Schreibfreie Vorschau. / Write-free preview.
.PARAMETER DownArgs
    Weitere Compose-down-Argumente in ihrer Reihenfolge. / Additional ordered arguments.
.EXAMPLE
    Stop-AdeSandboxWithAudit -Engine podman -WhatIf
.NOTES
    Bei Fehler: Auditbereich und Meldung prüfen, Wrapper erneut ausführen.
    Eine fremde Sperre nicht automatisch entfernen. / On failure, inspect
    audit area and message, then retry the wrapper. Never auto-remove a
    foreign lock.
#>
function Stop-AdeSandboxWithAudit {
  [CmdletBinding(SupportsShouldProcess = $true)]
  param(
    [ValidateSet("auto", "podman", "podman-compose")][string]$Engine = "auto",
    [switch]$Volumes,
    [switch]$RemoveOrphans,
    [switch]$DryRun,
    [Parameter(ValueFromRemainingArguments = $true)][string[]]$DownArgs = @()
  )

$ErrorActionPreference = "Stop"

if ($DryRun -or $WhatIfPreference) {
    Write-Host 'DRY-RUN: verify audit mount, export current metadata, retain 30 UTC days, then compose down'
    $script:AdeStopExitCode = 0
    return
}

function Test-CommandAvailable {
    param([string]$Name)
    return [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

$command = $null
$baseArgs = @()

switch ($Engine) {
    "podman" {
        $command = "podman"
        $baseArgs = @("compose")
    }
    "podman-compose" {
        $command = "podman-compose"
        $baseArgs = @()
    }
    default {
        if (Test-CommandAvailable "podman") {
            $command = "podman"
            $baseArgs = @("compose")
        } elseif (Test-CommandAvailable "podman-compose") {
            $command = "podman-compose"
            $baseArgs = @()
        } else {
            throw "Neither podman nor podman-compose was found in PATH."
        }
    }
}

$effectiveDownArgs = @()
if ($Volumes) {
    $effectiveDownArgs += "-v"
}
if ($RemoveOrphans) {
    $effectiveDownArgs += "--remove-orphans"
}
$effectiveDownArgs += $DownArgs

$auditDirectory = if ($env:AUDIT_DIR) { $env:AUDIT_DIR } else { './audit-logs' }
if ((Test-Path -LiteralPath $auditDirectory) -and
    ((Get-Item -LiteralPath $auditDirectory).Attributes -band [IO.FileAttributes]::ReparsePoint)) {
    throw 'Audit stop blocked: audit directory is a link.'
}
[void][IO.Directory]::CreateDirectory($auditDirectory)
$auditDirectory = [IO.Path]::GetFullPath($auditDirectory)
$day = (Get-Date).ToUniversalTime().ToString('yyyy-MM-dd')
$runId = [guid]::NewGuid().ToString()
$lockPath = Join-Path $auditDirectory '.audit-stop.lock'
$marker = Join-Path $auditDirectory ('.audit-mount.' + [guid]::NewGuid().ToString('N'))
$lockStream = $null
try {
    $lockStream = [IO.File]::Open($lockPath, [IO.FileMode]::CreateNew, [IO.FileAccess]::ReadWrite, [IO.FileShare]::None)
    $ownerBytes = [Text.Encoding]::UTF8.GetBytes($runId)
    $lockStream.Write($ownerBytes, 0, $ownerBytes.Length)
    $lockStream.Flush()
    [IO.File]::WriteAllText($marker, '')
    & $command @baseArgs exec -T ade /usr/bin/test -f ("/audit/" + [IO.Path]::GetFileName($marker))
    if ($LASTEXITCODE -ne 0) { throw 'Audit stop blocked at mount check: host audit directory is not visible at /audit. Check the Compose audit mount, then retry this wrapper; no down was started. See Get-Help.' }

    & $command @baseArgs exec -T -e "AUDIT_DATE=$day" -e "AUDIT_RUN_ID=$runId" ade /usr/local/bin/audit-export
    if ($LASTEXITCODE -ne 0) {
        $auditExitCode = $LASTEXITCODE
        Write-Warning "Audit stop blocked at export (exit $auditExitCode); no down was started. Check the exporter and retry this wrapper. See Get-Help."
        $script:AdeStopExitCode = $auditExitCode
        return
    }
    $dayFile = Join-Path $auditDirectory "$day.jsonl"
    if (-not [IO.File]::Exists($dayFile) -or (Get-Item -LiteralPath $dayFile).Length -eq 0 -or
        ((Get-Item -LiteralPath $dayFile).Attributes -band [IO.FileAttributes]::ReparsePoint)) {
        throw 'Audit stop blocked at verification: host day file is absent, empty or a link. Check the audit mount and retry this wrapper; no down was started. See Get-Help.'
    }
    & $command @baseArgs exec -T ade /usr/local/bin/audit-retention verify --audit-dir /audit --date $day --run-id $runId | Out-Null
    if ($LASTEXITCODE -ne 0) { throw 'Audit stop blocked at verification: current nonempty export run record missing. Check the exporter and retry this wrapper; no down was started. See Get-Help.' }
    $retentionOutput = & $command @baseArgs exec -T ade /usr/local/bin/audit-retention retain --audit-dir /audit --date $day 2>&1
    if ($LASTEXITCODE -ne 0) {
        $removed = 'unknown'
        $retentionText = ($retentionOutput | Out-String)
        if ($retentionText -match 'removed=(\d+)') { $removed = $Matches[1] }
        throw "Audit stop blocked at retention: removed=$removed old audit files before failure. Inspect the audit directory, then retry this wrapper for a new export; no down was started. See Get-Help."
    }
    $retentionOutput
    & $command @baseArgs down @effectiveDownArgs
    $script:AdeStopExitCode = $LASTEXITCODE
    return
} finally {
    if ([IO.File]::Exists($marker)) { [IO.File]::Delete($marker) }
    if ($lockStream) {
        $lockStream.Dispose()
        if ([IO.File]::Exists($lockPath) -and [IO.File]::ReadAllText($lockPath) -eq $runId) {
            [IO.File]::Delete($lockPath)
        }
    }
}
}

if ($MyInvocation.InvocationName -ne '.') {
    $script:AdeStopExitCode = 1
    Stop-AdeSandboxWithAudit @PSBoundParameters
    exit $script:AdeStopExitCode
}
