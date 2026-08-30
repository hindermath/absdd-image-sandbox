#Requires -Version 7
<#
.SYNOPSIS
    Prueft die ADE-Sandbox. / Validates the ADE sandbox.

.DESCRIPTION
    Verwendet denselben Python-Standardbibliothek-Kern wie der Bash-Einstieg.
    Dadurch bleiben Modi, Pfadgrenzen und Exitcodes gleich. Der WhatIf-Modus
    zeigt externe Pruefschritte, ohne sie auszufuehren.

    Uses the same Python standard-library core as the Bash entry point. This
    keeps modes, path boundaries, and exit codes equivalent. WhatIf reports
    external checks without executing them.

.PARAMETER Mode
    Input, Static, Runtime, SupplyChain, Documentation, Accessibility oder All.
    Input, Static, Runtime, SupplyChain, Documentation, Accessibility, or All.

.PARAMETER EvidencePath
    Repository-relativer Pfad zur Verifikationsevidenz. / Repository-relative
    path to verification evidence.

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
    [string] $EvidencePath = ''
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Test-AdeSandboxHardening {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory)]
        [ValidateSet('Input', 'Static', 'Runtime', 'SupplyChain', 'Documentation', 'Accessibility', 'All')]
        [string] $Mode,
        [string] $EvidencePath = ''
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
Test-AdeSandboxHardening -Mode $Mode -EvidencePath $EvidencePath -WhatIf:$WhatIfPreference
exit $script:AdeHardeningExitCode
