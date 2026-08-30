#Requires -Version 7
<#
.SYNOPSIS
    Exportiert nur erlaubte Agenten-Metadaten. / Exports allow-listed agent metadata only.
.DESCRIPTION
    Liest Dateiname, Zeitstempel und Typ aus eng erlaubten Sitzungsverzeichnissen
    sowie installierte Werkzeugversionen. Prompt-, Antwort-, Token- und
    Credential-Inhalte werden weder gelesen noch ausgegeben.

    Reads filename, timestamp, and type from narrowly allow-listed session
    directories plus installed tool versions. Prompt, response, token, and
    credential content is neither read nor exported.
.PARAMETER AuditDirectory
    Zielverzeichnis / target directory.
.PARAMETER ProjectPath
    Nicht sensibler Projektpfad / non-sensitive project path.
.PARAMETER WhatIf
    Zeigt den Zielpfad ohne Schreibzugriff / shows the target without writing.
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [string] $AuditDirectory = $(if ($env:AUDIT_DIR) { $env:AUDIT_DIR } else { '/audit' }),
    [string] $ProjectPath = $(if ($env:AUDIT_PROJECT_PATH) { $env:AUDIT_PROJECT_PATH } else { $PWD.Path })
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Export-AdeAgentAuditMetadata {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory)] [string] $TargetDirectory,
        [Parameter(Mandatory)] [string] $RepositoryPath
    )

    $target = Join-Path $TargetDirectory "$(Get-Date -AsUTC -Format 'yyyy-MM-dd').jsonl"
    if (-not $PSCmdlet.ShouldProcess($target, 'Write allow-listed audit metadata')) {
        return
    }

    New-Item -ItemType Directory -Force -Path $TargetDirectory | Out-Null
    $exportedAt = Get-Date -AsUTC -Format 'yyyy-MM-ddTHH:mm:ssZ'
    $actor = [Environment]::UserName
    $records = [System.Collections.Generic.List[object]]::new()

    $tools = @(
        @{ Name = 'opencode'; Command = 'opencode'; State = $(if ($env:OPENCODE_DATA_DIR) { $env:OPENCODE_DATA_DIR } else { '/home/adedev/.local/share/opencode' }) },
        @{ Name = 'codex'; Command = 'codex'; State = $(if ($env:CODEX_DATA_DIR) { $env:CODEX_DATA_DIR } else { '/home/adedev/.codex' }) },
        @{ Name = 'claude'; Command = 'claude'; State = $(if ($env:CLAUDE_DATA_DIR) { $env:CLAUDE_DATA_DIR } else { '/home/adedev/.claude' }) },
        @{ Name = 'antigravity'; Command = 'agy'; State = '/home/adedev/.gemini-home/.gemini/antigravity-cli' },
        @{ Name = 'copilot'; Command = 'copilot'; State = $(if ($env:COPILOT_HOME) { $env:COPILOT_HOME } else { '/home/adedev/.copilot' }) }
    )
    foreach ($tool in $tools) {
        $command = Get-Command $tool.Command -ErrorAction SilentlyContinue
        if ($command) {
            $version = (& $command.Source --version 2>&1 | Select-Object -First 1).ToString()
            $records.Add([ordered]@{ record_type = 'tool-version'; tool = $tool.Name; version = $version; state_dir = $tool.State; project_path = $RepositoryPath; actor = $actor; exported_at = $exportedAt })
        }
    }

    $allowLists = @(
        @{ Tool = 'opencode'; Root = "$($tools[0].State)/storage/session_diff"; Filter = 'ses_*'; Recurse = $false },
        @{ Tool = 'codex'; Root = "$($tools[1].State)/sessions"; Filter = '*'; Recurse = $true },
        @{ Tool = 'claude'; Root = "$($tools[2].State)/projects"; Filter = '*.jsonl'; Recurse = $true }
    )
    foreach ($allow in $allowLists) {
        if (-not (Test-Path -LiteralPath $allow.Root)) { continue }
        foreach ($item in Get-ChildItem -LiteralPath $allow.Root -File -Filter $allow.Filter -Recurse:$allow.Recurse | Sort-Object FullName) {
            $records.Add([ordered]@{
                tool = $allow.Tool; session_id = $item.BaseName
                started_at = $item.LastWriteTimeUtc.ToString('yyyy-MM-ddTHH:mm:ssZ')
                ended_at = $item.LastWriteTimeUtc.ToString('yyyy-MM-ddTHH:mm:ssZ')
                project_path = $RepositoryPath; actor = $actor; source_type = 'file'
                source_path = $item.FullName; exported_at = $exportedAt
            })
        }
    }

    $lines = @($records | ForEach-Object { $_ | ConvertTo-Json -Compress -Depth 5 })
    [IO.File]::WriteAllLines($target, $lines, [Text.UTF8Encoding]::new($false))
    Write-Output "Wrote $($lines.Count) audit metadata line(s) to $target"
}

Export-AdeAgentAuditMetadata -TargetDirectory $AuditDirectory -RepositoryPath $ProjectPath -WhatIf:$WhatIfPreference
