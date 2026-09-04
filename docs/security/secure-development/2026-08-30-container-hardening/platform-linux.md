# Ubuntu/WSL2-Linux-Plattformbeleg / Ubuntu/WSL2 Linux Platform Evidence

Status: `Open`. Owner: Repository Maintainer. Reviewer: Security Review.
Runner-Token: `Ubuntu-WSL2-Bash-rootless-Podman`.

## Scope

**DE:** Nach der genehmigten Entscheidung
`DEC-XPLAT-WSL2-2026-09-04` ist Ubuntu unter WSL2 die verbindliche
Linux-Akzeptanzumgebung fuer Feature 003. Windows-Host und Ubuntu/WSL2 duerfen
dieselbe physische Hardware nutzen. Dieser Nachweis verwendet jedoch eine
eigene rootless-Podman-Laufzeit innerhalb von Ubuntu und darf keine
Windows-Podman-Machine-Evidenz wiederverwenden. Native Linux-Hardware ist kein
Akzeptanzziel dieses Features.

**EN:** Under approved decision `DEC-XPLAT-WSL2-2026-09-04`, Ubuntu under WSL2
is the binding Linux acceptance environment for Feature 003. The Windows host
and Ubuntu/WSL2 may share physical hardware, but this evidence uses its own
rootless Podman runtime inside Ubuntu and must not reuse Windows Podman-machine
evidence. Native Linux hardware is not an acceptance target for this feature.

## Aktuelle Beobachtung / Current Observation

**DE:** In dieser macOS-Sitzung war kein Ubuntu/WSL2-Runner verfuegbar. Daher
wurden weder Benutzeridentitaet noch rootless Podman, Bash-/PowerShell-Paritaet,
Build, Runtime oder VS-Code-Attach beobachtet. Es wird kein `N/A` oder `Pass`
abgeleitet.

**EN:** No Ubuntu/WSL2 runner was available in this macOS session. User
identity, rootless Podman, Bash/PowerShell parity, build, runtime, and VS Code
attachment were therefore not observed. No `N/A` or `Pass` is inferred.

## Fuer Pass erforderliche Evidenz / Evidence Required for Pass

- WSL-Version, Ubuntu-Version, exakter Git-Head und Checkout im
  Linux-Dateisystem. / WSL version, Ubuntu version, exact Git head, and a
  checkout in the Linux file system.
- `id -u` fuer einen normalen Benutzer sowie `podman info` mit rootless-Status
  aus der Ubuntu-Laufzeit. / A non-root `id -u` and rootless status from
  `podman info` executed in Ubuntu.
- Getrennte Bash-Dry-run- und PowerShell-`-WhatIf`-Ergebnisse. / Separate Bash
  dry-run and PowerShell `-WhatIf` results.
- Eigener Compose-Build, Runtime-Smoke und Image-ID in Ubuntu/WSL2. / A
  dedicated Compose build, runtime smoke, and image ID in Ubuntu/WSL2.
- Beobachteter VS-Code-Attach ueber Remote WSL und Dev Containers mit
  `remoteUser=adedev`, Workspace und LSP. / Observed VS Code attachment through
  Remote WSL and Dev Containers with `remoteUser=adedev`, workspace, and LSP.

Retry-Trigger: erneut bei verfuegbarem
`Ubuntu-WSL2-Bash-rootless-Podman`-Runner. / Retry when that runner is
available.
