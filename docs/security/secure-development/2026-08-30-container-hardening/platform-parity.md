# Plattformparitaet / Platform Parity

## Konsolidierter Status / Consolidated Status

Status: `Blocked` (06.09.2026). Owner: Repository Maintainer. Reviewer:
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
| macOS | Der fruehere native Build-/Runtime-Nachweis gehoert zum vorherigen Image `sha256:5bec191...` und ist fuer den neuen Head/Image-Stand `Stale`. Ein VS-Code-Attach wurde auch dort nicht beobachtet. / The earlier native build/runtime evidence belongs to the previous image and is stale for the new source/image state; VS Code attachment was not observed. | Ergebnis `Blocked`, Frische `Stale`; VS Code offen / result Blocked, freshness Stale; VS Code open | Auf einem macOS-Runner gegen den neuen Head erneut bauen, pruefen und mit VS Code anhaengen. / Rebuild, verify, and attach with VS Code on macOS against the new head. |
| Ubuntu/WSL2 Linux path | Eigener Linux-Checkout, rootless Podman, Build, freier publizierter Portbereich `5600-5699`, Isolation, vollstaendiger Runtime-Modus, Audit-Shutdown, Static/pre-commit/Secret/Diff, SBOM, aktueller Grype-Scan, VEX/Provenienz und Remote WSL wurden getrennt belegt. Nach Auswahl von Podman als Dev-Containers-Engine gelang auch der manuelle Anhang. Menschliche Terminalausgaben und der technische Status-/Prozessnachweis bestaetigten `adedev`, `/rider-projects`, Remote-Indikator, integriertes Terminal und den aktiven `rust-analyzer`. / The separate Linux checkout proved the build, free published port range, isolation, complete Runtime mode, audit shutdown, static/pre-commit/secret/diff, SBOM, current Grype scan, VEX/provenance, Remote WSL, and the manual Dev Containers attachment. Human terminal output and the technical status/process probe confirmed the remote user, workspace, indicator, terminal, and active LSP. | `Pass` (aktueller vollstaendiger Plattformnachweis / current complete platform evidence) | Bei Aenderung von WSL, Podman, Image, Mounts oder VS Code erneut pruefen. / Recheck after WSL, Podman, image, mount, or VS Code changes. |
| Windows host | Eigene Podman-Machine, PowerShell-Plaene, Build, isolierte no-port Runtime, kompletter Toolchain-Smoke, Agent-Prompt-Dry-Run und aktuelle SBOM wurden belegt. Der reale VS-Code-Desktop-Anhang bestaetigte `adedev`, `/rider-projects`, Remote-Indikator, integriertes Terminal und aktiven JSON-LSP. Der Repository-Mount ist lesbar; allein Git im Container kann den Windows-absoluten `.git`-Verweis des Linked Worktrees nicht aufloesen. / Separate Podman machine, plans, build, isolated runtime, smoke, agent dry run, current SBOM, and real VS Code attachment passed. The repository mount is readable; only in-container Git cannot resolve the linked worktree's Windows-absolute `.git` pointer. | `Pass` (aktueller vollstaendiger Plattformnachweis mit dokumentierter Linked-Worktree-Grenze / current complete platform evidence with a documented linked-worktree limitation) | Bei Aenderung von Windows, Podman, Image, Mounts, Linked Worktree oder VS Code erneut pruefen. / Recheck after Windows, Podman, image, mount, linked-worktree, or VS Code changes. |

## Image-Bindung / Image Binding

**DE:** Das dokumentweite Feld `imageIdentity` in
`verification-evidence.json` bindet das aktuelle, kanonisch mit rootless
Podman nachgepruefte Ubuntu/WSL2-Image `sha256:bcdd1c8d...`. Der getrennte
Windows-Plattformdatensatz nennt seine eigene lokale Image-ID `57736551...`,
wie es die Scope-Entscheidung verlangt. Die beiden lokal erzeugten IDs werden
nicht als identische Artefakte ausgegeben. Der alte macOS-Build bleibt
historisch sichtbar, aber `Stale` und damit `Blocked`.

**EN:** The document-level `imageIdentity` in `verification-evidence.json`
binds the current Ubuntu/WSL2 image canonically rechecked with rootless Podman,
`sha256:bcdd1c8d...`. The separate Windows platform record states its own local
image ID `57736551...`, as required by the scope decision. The two locally
produced IDs are not presented as identical artifacts. The old macOS build
remains visible historically but is marked `Stale` and therefore `Blocked`.

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

## Merge-Blocker / Merge Blocker

**DE:** `GATE-XPLAT-01` bleibt `Blocked`. Ubuntu/WSL2 besitzt nun einen
aktuellen vollstaendigen Runtime-, Static-, Supply-Chain- und
Dev-Containers-Plattformnachweis. Auch der getrennte Windows-Pfad ist mit
Build, Runtime, Toolchain, SBOM und VS-Code-Anhang aktuell vollstaendig. Der
macOS-Lauf ist fuer den neuen Head/Image-Stand veraltet. Learning/A11Y, der
moderierte First-Use-Test und T066 bleiben unveraendert offen. Ein positiver
`MergeAndSync`-Abschluss ist nicht erlaubt.

**EN:** GATE-XPLAT-01 remains Blocked. Ubuntu/WSL2 now has current complete
Runtime, Static, supply-chain, and Dev Containers platform evidence. The
separate Windows path is also complete with current build, runtime, toolchain,
SBOM, and VS Code attachment evidence. The macOS run is stale for the new
source/image state. Learning/A11Y, the moderated first-use test, and T066
remain open. Positive MergeAndSync completion is not allowed.

## Dokumentierte menschliche Abweichungen / Documented Human Deviations

**DE:** Der Repository Owner hat am 04.09.2026 bestaetigt, dass dieses Feature
in einem Ein-Personen-Setup erstellt, ausgefuehrt und geprueft wird. Deshalb
sind weder ein echtes Vier-Augen-Review noch ein realer moderierter
Erstnutzungstest mit allen vier Ausbildungsberufen und assistiven Technologien
durchfuehrbar. Die ausdrueckliche Selbstpruefung des Patches ersetzt keine
personell unabhaengige Pruefung. Beide Punkte bleiben begruendete offene
Abweichungen; `GATE-A11Y-01` und `GATE-LEARNER-01` bleiben `Blocked`. Es werden
keine Teilnehmenden, Beobachtungen, Zeitwerte, Erfolgsquoten, Testate oder
Risikoakzeptanzen erfunden.

**EN:** On 2026-09-04, the Repository Owner confirmed that this feature is
created, operated, and reviewed in a one-person setup. Therefore neither a
genuine four-eyes review nor a real moderated first-use test covering all four
occupations and assistive technologies is feasible. Explicit self-review of
the patch does not replace person-independent review. Both items remain
justified open deviations; GATE-A11Y-01 and GATE-LEARNER-01 remain Blocked. No
participants, observations, timings, success rates, attestations, or risk
acceptances are invented.

Neubewertungsausloeser / Re-evaluation trigger: Any paired interface,
help/man page/Cmdlet, exit-code, platform result, source/image identity, or
platform availability change, or availability of an independent reviewer,
representative learners, or assistive technologies.
