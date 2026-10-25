param([string]$Repo = (Join-Path $PSScriptRoot '../..'))
$ErrorActionPreference = 'Stop'
. (Join-Path $Repo 'scripts/lib/statistics-ci-evidence.ps1')
$snapshot = @{measurement = @{sourceRevision = 'a' * 40; asOf = '2026-10-09'}}
$history = @{status = 'DRIFT'; reproducible = $true; current = $false; changed = $false;
    sourceRevision = 'a' * 40; asOf = '2026-10-09'}
$current = @{status = 'CURRENT'; changed = $false; methodologyVersion = 2; sourceRevision = 'b' * 40}
Assert-HistoricalStatisticsReplay -Decision $history -ExitCode 1 -Snapshot $snapshot
$freshHistory = $history.Clone()
$freshHistory.current = $true
$freshHistory.status = 'CURRENT'
Assert-HistoricalStatisticsReplay -Decision $freshHistory -ExitCode 0 -Snapshot $snapshot
Assert-CurrentStatisticsProfile2 -Decision $current -ExitCode 0
$blocked = 0
foreach ($change in @(@{reproducible = $false}, @{reproducible = 'true'}, @{current = $true},
    @{changed = $true}, @{status = 'CURRENT'}, @{sourceRevision = 'c' * 40}, @{asOf = '2026-10-10'})) {
    $candidate = $history.Clone()
    foreach ($key in $change.Keys) { $candidate[$key] = $change[$key] }
    $rejected = $false
    try { Assert-HistoricalStatisticsReplay -Decision $candidate -ExitCode 1 -Snapshot $snapshot } catch { $rejected = $true }
    if (-not $rejected) { throw 'Invalid historical evidence accepted.' }
    $blocked++
}
foreach ($change in @(@{status = 'DRIFT'}, @{changed = $true}, @{changed = 'false'},
    @{methodologyVersion = 1}, @{sourceRevision = ''})) {
    $candidate = $current.Clone()
    foreach ($key in $change.Keys) { $candidate[$key] = $change[$key] }
    $rejected = $false
    try { Assert-CurrentStatisticsProfile2 -Decision $candidate -ExitCode 0 } catch { $rejected = $true }
    if (-not $rejected) { throw 'Invalid current evidence accepted.' }
    $blocked++
}
foreach ($mode in @('historical', 'current')) {
    $rejected = $false
    try {
        if ($mode -eq 'historical') { Assert-HistoricalStatisticsReplay -Decision $history -ExitCode 0 -Snapshot $snapshot }
        else { Assert-CurrentStatisticsProfile2 -Decision $current -ExitCode 1 }
    } catch { $rejected = $true }
    if (-not $rejected) { throw 'Wrong exit code accepted.' }
    $blocked++
}
Write-Output "PASS: 3 valid decisions and $blocked invalid decisions rejected"
