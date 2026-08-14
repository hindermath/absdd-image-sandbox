# PowerShell 7

## Einordnung / Context

**DE:** PowerShell-Projekte liegen standardmäßig unter
`/powershell-projects`. Das Image verwendet die PowerShell-7-Version des
gepinnten .NET-SDK-Basisimages und prüft sie beim Build. Führe Skripte auf
diesem macOS-Host und im Container ohne Benutzerprofil aus, damit lokale
Profile das Ergebnis nicht verändern.

**EN:** PowerShell projects normally live under `/powershell-projects`. The
image uses the PowerShell 7 version supplied by the pinned .NET SDK base image
and verifies it during the build. Run scripts on this macOS host and inside the
container without a user profile so local profiles cannot change the result.

## Skript anlegen und ausführen / Create and Run a Script

Datei `Get-SandboxGreeting.ps1` / File `Get-SandboxGreeting.ps1`:

```powershell
[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$Name
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

"Hallo, $Name!"
```

```bash
cd /powershell-projects
pwsh -NoLogo -NoProfile -File ./Get-SandboxGreeting.ps1 -Name Sandbox
```

## Module und Analyse / Modules and Analysis

**DE:** Module gehören projektlokal oder in eine ausdrücklich versionierte
Abhängigkeit. Prüfe ein Repository-Skript mit PSScriptAnalyzer, wenn das Modul
verfügbar ist:

**EN:** Modules belong in the project or in an explicitly versioned
dependency. Check a repository script with PSScriptAnalyzer when the module is
available:

```powershell
$analyzer = Get-Module -ListAvailable PSScriptAnalyzer
if ($analyzer) {
    Invoke-ScriptAnalyzer -Path . -Recurse
} else {
    Write-Warning "PSScriptAnalyzer ist nicht installiert / is not installed"
}
```

**DE:** Für strukturierte Repository-Automation stehen vorhandene PowerShell-
Skripte an erster Stelle. Führe vor Änderungen `Get-Help` oder die jeweilige
Manpage unter `docs/man/` aus beziehungsweise lies sie.

**EN:** Existing PowerShell scripts are the first choice for structured
repository automation. Before changing anything, use `Get-Help` or read the
corresponding page under `docs/man/`.

## Grenzen / Limits

- **DE:** Verwende keine Windows-PowerShell-5.1-Syntax als stillschweigende
  Voraussetzung. Ziel ist PowerShell 7. **EN:** Do not silently require Windows
  PowerShell 5.1 syntax. The target is PowerShell 7.
- **DE:** Prüfe Hostpfade und Containerpfade getrennt. **EN:** Treat host paths
  and container paths separately.
- **DE:** Geheimnisse gehören weder in `.ps1`-Dateien noch in die
  Befehlszeile. **EN:** Secrets belong neither in `.ps1` files nor on the
  command line.

Zurück zum [Toolchain-Index](README.md). / Return to the
[toolchain index](README.md).
