# Plattformparitaet / Platform Parity

## Konsolidierter Status / Consolidated Status

Status: `Pass` (06.09.2026). Owner: Repository Maintainer. Reviewer:
Security Review. Technischer Quell-Head / technical source head:
`ad5cd8bc9a9a2c541416390aa4256bc1ffe1eee7`.

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
| macOS | Auf Repository-Head `7901cc71...` wurde das technisch unveraenderte Image neu gebaut. Runtime, vollstaendiger Toolchain-Smoke, Agent-Prompt-Dry-run und beide Static-Plaene bestanden. VS Code Desktop haengte real an Container `49adefa...` an; UI, `code --status` und `podman top` bestaetigten `/rider-projects`, Remoteindikator, Terminal-Backend, `adedev` und aktiven JSON-LSP. Die lokale Podman-Machine meldet `Rootful=true`; sie wird nicht als rootless Beleg ausgegeben. / The technically unchanged image was rebuilt at repository head `7901cc71...`. Runtime, full toolchain smoke, dispatcher dry run, and both static plans passed. VS Code Desktop attached to container `49adefa...`; UI, status, and process evidence confirmed workspace, remote indicator, terminal backend, `adedev`, and active JSON LSP. The local Podman machine reports rootful and is not presented as rootless evidence. | `Pass`, Frische `Current` / freshness Current | Bei Aenderung von macOS, Podman-Machine-Modus, Image, Mounts oder VS Code erneut pruefen. / Recheck after macOS, Podman machine mode, image, mount, or VS Code changes. |
| Ubuntu/WSL2 Linux path | Eigener Linux-Checkout, rootless Podman, Build, freier publizierter Portbereich `5600-5699`, Isolation, vollstaendiger Runtime-Modus, Audit-Shutdown, Static/pre-commit/Secret/Diff, SBOM, aktueller Grype-Scan, VEX/Provenienz und Remote WSL wurden getrennt belegt. Nach Auswahl von Podman als Dev-Containers-Engine gelang auch der manuelle Anhang. Menschliche Terminalausgaben und der technische Status-/Prozessnachweis bestaetigten `adedev`, `/rider-projects`, Remote-Indikator, integriertes Terminal und den aktiven `rust-analyzer`. / The separate Linux checkout proved the build, free published port range, isolation, complete Runtime mode, audit shutdown, static/pre-commit/secret/diff, SBOM, current Grype scan, VEX/provenance, Remote WSL, and the manual Dev Containers attachment. Human terminal output and the technical status/process probe confirmed the remote user, workspace, indicator, terminal, and active LSP. | `Pass` (aktueller vollstaendiger Plattformnachweis / current complete platform evidence) | Bei Aenderung von WSL, Podman, Image, Mounts oder VS Code erneut pruefen. / Recheck after WSL, Podman, image, mount, or VS Code changes. |
| Windows host | Eigene Podman-Machine, PowerShell-Plaene, Build, isolierte no-port Runtime, kompletter Toolchain-Smoke, Agent-Prompt-Dry-Run und aktuelle SBOM wurden belegt. Der reale VS-Code-Desktop-Anhang bestaetigte `adedev`, `/rider-projects`, Remote-Indikator, integriertes Terminal und aktiven JSON-LSP. Der Repository-Mount ist lesbar; allein Git im Container kann den Windows-absoluten `.git`-Verweis des Linked Worktrees nicht aufloesen. / Separate Podman machine, plans, build, isolated runtime, smoke, agent dry run, current SBOM, and real VS Code attachment passed. The repository mount is readable; only in-container Git cannot resolve the linked worktree's Windows-absolute `.git` pointer. | `Pass` (aktueller vollstaendiger Plattformnachweis mit dokumentierter Linked-Worktree-Grenze / current complete platform evidence with a documented linked-worktree limitation) | Bei Aenderung von Windows, Podman, Image, Mounts, Linked Worktree oder VS Code erneut pruefen. / Recheck after Windows, Podman, image, mount, linked-worktree, or VS Code changes. |

## Image-Bindung / Image Binding

**DE:** Das dokumentweite Feld `imageIdentity` in
`verification-evidence.json` bindet das aktuelle, kanonisch mit rootless
Podman nachgepruefte Ubuntu/WSL2-Image `sha256:bcdd1c8d...`. Der getrennte
Windows-Plattformdatensatz nennt seine eigene lokale Image-ID `57736551...`,
wie es die Scope-Entscheidung verlangt. Der aktuelle macOS-Plattformdatensatz
nennt das separat erzeugte arm64-Image `978cb724...`. Die drei lokal erzeugten
IDs werden nicht als identische Artefakte ausgegeben. Nur das WSL2-Image bleibt
die kanonische Bindung fuer SBOM, Scan, VEX und Provenienz.

**EN:** The document-level `imageIdentity` in `verification-evidence.json`
binds the current Ubuntu/WSL2 image canonically rechecked with rootless Podman,
`sha256:bcdd1c8d...`. The separate Windows platform record states its own local
image ID `57736551...`; the current macOS record states its separately built
arm64 image `978cb724...`. The three local IDs are not presented as identical
artifacts. Only the WSL2 image remains canonical for SBOM, scan, VEX, and
provenance.

## Gemeinsamer Oberflaechenvertrag / Shared Surface Contract

**DE:** Die Python-Paritaetstests fuer Agentenoberflaechen und Hardening
bestanden auf dem neuen Head mit 3/3 und 24/24 Tests. Die Bash- und
PowerShell-`check-only`-Aufrufe waehlen ausdruecklich das in diesem Repository
installierte verwaltete Zwoelf-Preset-Profil. Beide Varianten bestaetigten alle
12 IDs, Versionen, Prioritaeten und Aktivzustaende. Das Standard-Acht-Profil
bleibt fuer Repositories erhalten, die es bewusst verwenden.
`GATE-PARITY-01` bleibt damit `Pass`.

**EN:** Agent-surface and hardening parity tests passed 3/3 and 24/24 on the
new head. Both preset check-only paths explicitly select this repository's
installed managed twelve-preset profile. Both confirmed all 12 IDs, versions,
priorities, and enabled states. The standard eight profile remains available
for repositories that intentionally use it. GATE-PARITY-01 remains Pass.

## Verbleibende Abschlussgrenzen / Remaining Closeout Boundaries

**DE:** `GATE-XPLAT-01` ist nach dem getrennten aktuellen macOS-Nachlauf nun
`Pass`. Alle 390 Advisories bleiben sichtbar `Open`/`in_triage` und werden
nicht als akzeptiert oder behoben ausgegeben. Fuer die befristete source-only
Machbarkeitsstudie ist `GATE-SUPPLY-01` deshalb ein Transparenzgate und keine
Distributions- oder Produktionsfreigabe. Der moderierte First-Use-Test und eine
unabhaengige Learning-/A11Y-Pruefung sind `NotPerformed`; nur
`GATE-LEARNER-01` ist gemaess der befristeten Owner-Entscheidung fuer diesen
Studienabschluss `N/A`. Die vorherigen Gap-/Diff-Fehler bleiben historische
Kandidatenbefunde und muessen durch genau einen neu revalidierten T066-
Kandidaten ersetzt werden.

**EN:** GATE-XPLAT-01 is now Pass after the separate current macOS rerun. The
390 advisories remain visibly Open/in_triage and are not presented as accepted
or remediated. For this time-bounded source-only feasibility study,
GATE-SUPPLY-01 is a transparency gate, not distribution or production
approval. Moderated first use and independent Learning/A11Y review are
NotPerformed; only GATE-LEARNER-01 is N/A for this study closeout under the
time-bounded owner decision. The prior gap/diff failures remain historical
candidate results and must be replaced by exactly one newly revalidated T066
candidate.

## Dokumentierte menschliche Abweichungen / Documented Human Deviations

**DE:** Der Repository Owner hat am 06.09.2026 entschieden, dieses Feature als
bis 31.12.2026 befristete, allein durchgefuehrte und source-only
Machbarkeitsstudie abzuschliessen. Ein echtes Vier-Augen-Review und der
moderierte Erstnutzungstest sind in diesem Scope `NotPerformed`.
`GATE-A11Y-01` prueft weiterhin die tatsaechlich ausgefuehrte
artefaktbezogene, text-first WCAG-2.2-AA-Pruefung. `GATE-LEARNER-01` ist nur
fuer diesen Studienabschluss `N/A`. Es werden keine Teilnehmenden,
Beobachtungen, Zeitwerte, Erfolgsquoten oder unabhaengigen Testate erfunden.

**EN:** On 2026-09-06, the Repository Owner limited completion to a
single-person, source-only feasibility study through 2026-12-31. Four-eyes
review and moderated first use are NotPerformed. GATE-A11Y-01 still validates
the actual artefact-level text-first WCAG review; GATE-LEARNER-01 is N/A only
for this study closeout. No participants, observations, timings, success
rates, or independent attestations are invented.

Neubewertungsausloeser / Re-evaluation trigger: Any paired interface,
help/man page/Cmdlet, exit-code, platform result, source/image identity, or
platform availability change, learner rollout, prebuilt image distribution,
production use, or arrival of 2026-12-31.
