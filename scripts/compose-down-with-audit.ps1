[CmdletBinding()]
param(
    [ValidateSet("auto", "podman", "podman-compose")]
    [string]$Engine = "auto",

    [switch]$Volumes,

    [switch]$RemoveOrphans,

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$DownArgs = @()
)

$ErrorActionPreference = "Stop"

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

Write-Host "Running audit-export before compose down..."
& $command @baseArgs exec -T ade audit-export
if ($LASTEXITCODE -eq 0) {
    Write-Host "Audit metadata export completed before compose down."
} else {
    Write-Warning "Audit metadata export did not complete; continuing with compose down."
}

$effectiveDownArgs = @()
if ($Volumes) {
    $effectiveDownArgs += "-v"
}
if ($RemoveOrphans) {
    $effectiveDownArgs += "--remove-orphans"
}
$effectiveDownArgs += $DownArgs

& $command @baseArgs down @effectiveDownArgs
exit $LASTEXITCODE
