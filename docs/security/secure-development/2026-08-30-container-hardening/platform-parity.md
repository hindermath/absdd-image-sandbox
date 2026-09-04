# Plattformparitaet / Platform Parity

## Konsolidierter Status / Consolidated Status

Status: `Blocked` (30.08.2026). Owner: Repository Maintainer. Reviewer:
Security Review.

**DE:** Plattformparitaet bedeutet fuer Feature 003 getrennte Beobachtungen auf
macOS, dem Windows-Host und in Ubuntu unter WSL2. Nach der genehmigten
Entscheidung `DEC-XPLAT-WSL2-2026-09-04` duerfen Windows-Host und Ubuntu/WSL2
dieselbe physische Hardware nutzen. Sie muessen getrennte Podman-Laufzeiten,
Befehle, Zeitstempel, Image-IDs, Exitcodes und VS-Code-Beobachtungen besitzen.
Die Textbeschreibung ist vollstaendig; Statuswoerter und Exitcodes tragen die
Information ohne Farbe oder Symbol.

**EN:** For Feature 003, platform parity requires separate observations on
macOS, the Windows host, and Ubuntu under WSL2. Approved decision
`DEC-XPLAT-WSL2-2026-09-04` allows the Windows-host and Ubuntu/WSL2 paths to
share physical hardware. They must use separate Podman runtimes, commands,
timestamps, image IDs, exit codes, and VS Code observations. Text and exit
codes carry the complete information without relying on color or symbols.

## Ergebnisse / Results

| Plattform / Platform | Beobachtung / Observation | Status | Naechster Trigger / Next trigger |
|---|---|---|---|
| macOS | Bash-Dry-run und PowerShell-WhatIf waren gleichwertig. Native rootless Podman bestand Runtime, 6/6 Sprachen, 2/2 Skriptgrundlagen, sechs Agenten-CLIs, Dispatcher-Dry-run und Audit-Stopp. VS-Code-Attach wurde nicht beobachtet. / Paired plans and native runtime passed; VS Code attach was not observed. | `Pass` fuer den Hostpfad, VS Code `Open` / host path Pass, VS Code Open | Erneut mit VS Code Desktop und Dev Containers am echten macOS-Host anhaengen. / Retry attachment with VS Code Desktop and Dev Containers. |
| Ubuntu/WSL2 Linux path | Kein Ubuntu/WSL2-Runner mit normalem Benutzer, eigener rootless-Podman-Laufzeit, PowerShell 7 und VS Code war verfuegbar. Windows-Podman-Machine und macOS wurden nicht als Ersatz genutzt. / No matching Ubuntu/WSL2 runner was available; Windows Podman-machine and macOS evidence were not substituted. | `Open` / `Blocked` | `erneut bei verfuegbarem Ubuntu-WSL2-Bash-rootless-Podman-Runner` |
| Windows host | Kein Windows-Host mit PowerShell 7, Windows-Podman-Machine und VS Code Desktop war verfuegbar. Ubuntu/WSL2 und macOS wurden nicht als Ersatz genutzt. / No matching Windows host was available; Ubuntu/WSL2 and macOS evidence were not substituted. | `Open` / `Blocked` | `erneut bei verfuegbarem Windows-Host-PowerShell7-Podman-Runner` |

## Gemeinsamer Oberflaechenvertrag / Shared Surface Contract

**DE:** Die Python-Paritaetstests fuer Agentenoberflaechen und Hardening
bestanden mit 3/3 und 24/24 Tests. Nach der engen Resume-Korrektur waehlen die
Bash- und PowerShell-`check-only`-Aufrufe ausdruecklich das in diesem
Repository bereits installierte verwaltete Zwoelf-Preset-Profil. Beide
Varianten bestaetigten alle 12 IDs, Versionen, Prioritaeten und Aktivzustaende.
Das Standard-Acht-Profil bleibt fuer Repositories erhalten, die es bewusst
verwenden. `GATE-PARITY-01` steht damit auf `Pass`.

**EN:** Agent-surface and hardening parity tests passed 3/3 and 24/24. After
the narrow resume correction, both preset check-only paths explicitly select
this repository's already installed managed twelve-preset profile. Both
confirmed all 12 IDs, versions, priorities, and enabled states. The standard
eight profile remains available for repositories that intentionally use it.
GATE-PARITY-01 is now Pass.

## Merge-Blocker / Merge Blocker

**DE:** `GATE-XPLAT-01` bleibt `Blocked`, solange der Windows-Host- oder der
Ubuntu/WSL2-Pfad offen ist. Der positive `MergeAndSync`-Abschluss ist damit
nicht erlaubt. Der fehlende VS-Code-Attach und das separate Learner-Gate
verstaerken den Blocker, werden aber nicht als Plattform-Pass umgedeutet.

**EN:** GATE-XPLAT-01 remains Blocked while the Windows-host or Ubuntu/WSL2
path is open, so positive MergeAndSync completion is not allowed. Missing VS
Code attachment and the separate learner gate add blockers but are not
reclassified as a platform pass.

Neubewertungsausloeser / Re-evaluation trigger: Any paired interface,
help/man page/Cmdlet, exit-code, platform result, or platform availability
change.
