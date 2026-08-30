# Plattformparitaet / Platform Parity

## Konsolidierter Status / Consolidated Status

Status: `Blocked` (30.08.2026). Owner: Repository Maintainer. Reviewer:
Security Review.

**DE:** Plattformparitaet bedeutet, dass die betroffenen Hostablaeufe auf der
jeweiligen echten Plattform beobachtet wurden. Ein macOS-Lauf oder ein
Linux-Container auf macOS ersetzt weder einen Linux-Host noch Windows/WSL2.
Die Textbeschreibung ist vollstaendig; Statuswoerter und Exitcodes tragen die
Information ohne Farbe oder Symbol.

**EN:** Platform parity requires observing affected host workflows on each
real platform. A macOS run or Linux container on macOS cannot replace a Linux
host or Windows/WSL2. Text and exit codes carry the complete information
without relying on color or symbols.

## Ergebnisse / Results

| Plattform / Platform | Beobachtung / Observation | Status | Naechster Trigger / Next trigger |
|---|---|---|---|
| macOS | Bash-Dry-run und PowerShell-WhatIf waren gleichwertig. Native rootless Podman bestand Runtime, 6/6 Sprachen, 2/2 Skriptgrundlagen, sechs Agenten-CLIs, Dispatcher-Dry-run und Audit-Stopp. VS-Code-Attach wurde nicht beobachtet. / Paired plans and native runtime passed; VS Code attach was not observed. | `Pass` fuer den Hostpfad, VS Code `Open` / host path Pass, VS Code Open | Erneut mit VS Code Desktop und Dev Containers am echten macOS-Host anhaengen. / Retry attachment with VS Code Desktop and Dev Containers. |
| Linux | Kein echter Linux-Host mit rootless Podman, PowerShell 7 und VS Code Dev Containers war verfuegbar. Ein Linux-Container auf macOS wurde nicht als Ersatz genutzt. / No real matching Linux host was available; no substitute was used. | `Open` / `Blocked` | `erneut bei verfuegbarem Linux-rootless-Podman-Runner` |
| Windows/WSL2 | Kein echter Windows/WSL2-Host mit PowerShell 7, Podman und VS Code Dev Containers war verfuegbar. macOS wurde nicht als Ersatz genutzt. / No real matching Windows/WSL2 host was available; macOS was not substituted. | `Open` / `Blocked` | `erneut bei verfuegbarem Windows/WSL2-PowerShell7-Podman-Runner` |

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

**DE:** `GATE-XPLAT-01` bleibt `Blocked`, solange Linux und Windows/WSL2 offen
sind. Der positive `MergeAndSync`-Abschluss ist damit nicht erlaubt. Der
fehlende VS-Code-Attach und das separate Learner-Gate verstaerken den Blocker,
werden aber nicht als Plattform-Pass umgedeutet.

**EN:** GATE-XPLAT-01 remains Blocked while Linux and Windows/WSL2 are open,
so positive MergeAndSync completion is not allowed. Missing VS Code attachment
and the separate learner gate add blockers but are not reclassified as a
platform pass.

Neubewertungsausloeser / Re-evaluation trigger: Any paired interface,
help/man page/Cmdlet, exit-code, platform result, or platform availability
change.
