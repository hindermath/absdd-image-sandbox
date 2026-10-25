# DE: Historische Reproduzierbarkeit und aktuelle Statistik getrennt nachweisen.
# EN: Keep historical reproducibility separate from current statistics freshness.
function Assert-HistoricalStatisticsReplay {
    param($Decision, [int]$ExitCode, $Snapshot)
    Set-StrictMode -Version Latest
    foreach ($field in @('reproducible', 'current', 'changed')) {
        if ($Decision.$field -isnot [bool]) { throw 'Invalid historical boolean field.' }
    }
    $expectedExit = if ($Decision.current) { 0 } else { 1 }
    $expectedStatus = if ($Decision.current) { 'CURRENT' } else { 'DRIFT' }
    if ($ExitCode -ne $expectedExit -or $Decision.status -cne $expectedStatus -or
        -not $Decision.reproducible -or $Decision.changed -or
        [string]::IsNullOrWhiteSpace($Snapshot.measurement.sourceRevision) -or
        [string]::IsNullOrWhiteSpace($Snapshot.measurement.asOf) -or
        $Decision.sourceRevision -cne $Snapshot.measurement.sourceRevision -or
        $Decision.asOf -cne $Snapshot.measurement.asOf) {
        throw 'Historical measurement must reproduce exactly with consistent freshness classification.'
    }
}

function Assert-CurrentStatisticsProfile2 {
    param($Decision, [int]$ExitCode)
    Set-StrictMode -Version Latest
    if ($ExitCode -ne 0 -or $Decision.status -cne 'CURRENT' -or
        $Decision.changed -isnot [bool] -or $Decision.changed -or
        $Decision.methodologyVersion -ne 2 -or
        [string]::IsNullOrWhiteSpace($Decision.sourceRevision)) {
        throw 'Current Profile 2 statistics must be current and write-free.'
    }
}
