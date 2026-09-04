# Windows-Host-Plattformbeleg / Windows Host Platform Evidence

Status: `Open`. Owner: Repository Maintainer. Reviewer: Security Review.
Runner-Token: `Windows-Host-PowerShell7-Podman`.

## Scope

**DE:** Diese Datei dokumentiert ausschliesslich den Windows-Hostpfad mit
Windows PowerShell 7, Windows-Podman-Machine und VS Code Desktop. Nach
`DEC-XPLAT-WSL2-2026-09-04` darf derselbe Rechner auch den getrennten
Ubuntu/WSL2-Nachweis ausfuehren. Ergebnisse des rootless Podman innerhalb von
Ubuntu/WSL2 werden hier nicht als Windows-Nachweis wiederverwendet.

**EN:** This file documents only the Windows host path with Windows PowerShell
7, the Windows Podman machine, and VS Code Desktop. Under
`DEC-XPLAT-WSL2-2026-09-04`, the same computer may also run the separate
Ubuntu/WSL2 evidence path. Results from rootless Podman inside Ubuntu/WSL2 are
not reused here as Windows evidence.

## Aktuelle Beobachtung / Current Observation

**DE:** In dieser macOS-Sitzung war kein Windows-Host mit PowerShell 7, Podman
und VS Code Dev Containers verfuegbar. macOS- oder Ubuntu/WSL2-Ergebnisse
ersetzen diesen Pfad nicht; es wird kein `N/A` oder `Pass` abgeleitet.

**EN:** No Windows host with PowerShell 7, Podman, and VS Code Dev Containers
was available in this macOS session. macOS or Ubuntu/WSL2 results do not
replace this path; no `N/A` or `Pass` is inferred.

## Fuer Pass erforderliche Evidenz / Evidence Required for Pass

- Windows-, PowerShell-, Podman-, VS-Code- und Dev-Containers-Version sowie
  exakter Git-Head. / Windows, PowerShell, Podman, VS Code, and Dev Containers
  versions plus the exact Git head.
- PowerShell-`-WhatIf`, Windows-Podman-Machine, Compose Build/Runtime und eigene
  Image-ID. / PowerShell `-WhatIf`, Windows Podman machine, Compose
  build/runtime, and a distinct image ID.
- Beobachteter VS-Code-Desktop-Attach mit `remoteUser=adedev`, Workspace und
  LSP. / Observed VS Code Desktop attachment with `remoteUser=adedev`,
  workspace, and LSP.
- Eigene Befehle, Start-/Endzeiten und Exitcodes; keine Wiederverwendung der
  Ubuntu/WSL2-Evidenz. / Distinct commands, start/end times, and exit codes; no
  reuse of Ubuntu/WSL2 evidence.

Retry-Trigger: erneut bei verfuegbarem
`Windows-Host-PowerShell7-Podman`-Runner. / Retry when that runner is
available.
