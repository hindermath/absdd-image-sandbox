#Requires -Version 7
<#
.SYNOPSIS
    Prueft die ADE-Sandbox. / Validates the ADE sandbox.

.DESCRIPTION
    Verwendet denselben Python-Standardbibliothek-Kern wie der Bash-Einstieg.
    Dadurch bleiben Modi, Pfadgrenzen und Exitcodes gleich. Der WhatIf-Modus
    zeigt externe Pruefschritte, ohne sie auszufuehren.
    Vorschau-Exit 0 ist kein bestandener Test. Feature 004 nutzt nur seine
    eigene Evidence; All mit offenen Pflicht-Gates ist nie GREEN.

    Uses the same Python standard-library core as the Bash entry point. This
    keeps modes, path boundaries, and exit codes equivalent. WhatIf reports
    external checks without executing them.
    Preview exit 0 is not a test pass. Feature 004 uses only its own evidence;
    All with mandatory Open gates is never GREEN.

.PARAMETER Mode
    Input, Static, Runtime, SupplyChain, Documentation, Accessibility oder All.
    Input, Static, Runtime, SupplyChain, Documentation, Accessibility, or All.

.PARAMETER EvidencePath
    Repository-relativer Pfad zur Verifikationsevidenz. / Repository-relative
    path to verification evidence.

.PARAMETER FeatureDirectory
    Explizites Feature-004-Verzeichnis. Ohne Angabe gilt der historische
    Feature-003-Vertrag. / Explicit Feature 004 directory; omission keeps the
    historical Feature 003 contract.

.EXAMPLE
    pwsh -NoProfile -File scripts/test-ade-sandbox-hardening.ps1 -Mode Input

.EXAMPLE
    pwsh -NoProfile -File scripts/test-ade-sandbox-hardening.ps1 -Mode Static -WhatIf

.NOTES
    Exitcodes: 0 belegt; 1 RED; 2 Bedien-/Vertragsfehler; 3 fehlende Plattform,
    Runner- oder Human-Evidenz. / Exit codes: 0 evidenced; 1 RED; 2 usage or
    contract error; 3 missing platform, runner, or human evidence.
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [ValidateSet('Input', 'Static', 'Runtime', 'SupplyChain', 'Documentation', 'Accessibility', 'All')]
    [string] $Mode,
    [string] $EvidencePath = '',
    [ValidateNotNullOrEmpty()] [string] $FeatureDirectory = ''
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Test-AdeSandboxHardening {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory)]
        [ValidateSet('Input', 'Static', 'Runtime', 'SupplyChain', 'Documentation', 'Accessibility', 'All')]
        [string] $Mode,
        [string] $EvidencePath = '',
        [ValidateNotNullOrEmpty()] [string] $FeatureDirectory = ''
    )

    $repositoryRoot = Split-Path -Parent $PSScriptRoot
    $core = Join-Path $PSScriptRoot 'lib/secure_development_hardening.py'
    $python = Get-Command python3 -ErrorAction SilentlyContinue
    if (-not $python) {
        Write-Error 'python3 fehlt / is unavailable.' -ErrorAction Continue
        $script:AdeHardeningExitCode = 3
        return
    }

    $arguments = @($core, 'run-mode', '--repo', $repositoryRoot, '--mode', $Mode)
    if ($EvidencePath) {
        $arguments += @('--evidence', $EvidencePath)
    }
    if ($FeatureDirectory) {
        $arguments += @('--feature-directory', $FeatureDirectory)
    }
    if ($WhatIfPreference) {
        $arguments += '--dry-run'
    }

    # The shared core receives an argument array, never an evaluated command
    # string. This preserves quoting and prevents PowerShell injection.
    & $python.Source @arguments
    if ($null -eq $LASTEXITCODE) {
        $script:AdeHardeningExitCode = 2
        return
    }
    $script:AdeHardeningExitCode = $LASTEXITCODE
}

$script:AdeHardeningExitCode = 2
$invocation = @{ Mode = $Mode; EvidencePath = $EvidencePath; WhatIf = $WhatIfPreference }
if ($PSBoundParameters.ContainsKey('FeatureDirectory')) {
    $invocation.FeatureDirectory = $FeatureDirectory
}
Test-AdeSandboxHardening @invocation
exit $script:AdeHardeningExitCode
