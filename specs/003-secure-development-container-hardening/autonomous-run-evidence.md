# Autonome Lauf-Evidenz: Plan / Autonomous Run Evidence: Plan

## Status dieser Evidenz / Status of This Evidence

**DE:** Dieses Dokument belegt nur die abgeschlossene Planungsarbeit. Es ist
keine Implementierungs-, Gate-Ausfuehrungs-, Liefer- oder Risikoakzeptanz-
Evidenz. Alle spaeteren Implementation-Gates sind vor der ersten
Produkt-/Konfigurationsaenderung in
`autonomous-run-gate-requirements.json` deklariert.

**EN:** This document evidences planning only. It is not implementation,
executed-gate, delivery, or risk-acceptance evidence. Every later
implementation gate is declared before the first product/configuration edit.

## Run-Identitaet / Run Identity

| Feld / Field | Wert / Value |
|---|---|
| Run-ID | `8330f54b-97d1-424c-ad1a-842a3fad7be3` |
| Feature | `specs/003-secure-development-container-hardening` |
| Branch | `003-secure-development-container-hardening` |
| Stage | `Plan` |
| Status beim Start / Status at start | `Active`; routing phase `plan`: `Running` |
| Delivery Mode | `MergeAndSync` im orchestratorverwalteten State; keine Lieferaktion in dieser Phase. / In orchestrator-owned state; no delivery action in this phase. |
| State-Aenderung / State mutation | Keine / None |
| Commit/Remote | Keine / None |

## Akzeptierte Eingaben / Accepted Inputs

Die sechs Dateien wurden im Planlauf gelesen; ihre aktuellen Rohhashes stimmen
mit den normalisierten Bindungen ueberein: / The six files were read and their
current raw hashes match the normalized bindings:

| Pfad / Path | SHA-256 |
|---|---|
| `Lastenheft_Secure-Development-Container-Hardening.md` | `72c263db933ea5a10ca60f3a7cc41231b43e1aec5d0dd641129e1a523b3432dc` |
| `specs/intake-review-results/sandbox-development-lifecycle.json` | `0d08a1e90e25965c4b529d66be6996394b963abef4ddb3c3b75dd678f464004b` |
| `specs/intake-series/sandbox-development-lifecycle/manifest.json` | `8813d2135a092671ccb373cd9273f44fe8ec3ceabab3eaa35f44e617cf2d15c4` |
| `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json` | `81a7ab5c5d8c6de449289de1dbf143e14933a3678a1160a25ed8ba5d671c8b39` |
| `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/prioritized-gap-list.md` | `b7e631e9df5e37686ab1ff2c0a07552c5d59c23af28621c917e36d2a42f55542` |
| `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/acceptance-decision.md` | `12fbac3263f31646e83e4d9b841a73c41d96dcc8ca259be68b40f356bd0354c7` |

`AcceptedBaseline` schliesst weiterhin keinen Gap und akzeptiert kein
Restrisiko. / AcceptedBaseline still closes no gap and accepts no residual
risk.

## Repository- und Gap-Inspektion / Repository and Gap Inspection

Geprueft wurden: / Inspected:

- alle 157 Gap-Objekte und alle 157 priorisierten Markdown-Eintraege;
- Zaehler: `157 Open`, `157 Not Assessed`, `157 P1`, `108` agentisch,
  `49` Human-only, keine fehlende/duplizierte/extra ID;
- Human-only-Rollen: Privacy/Legal Review, Platform Owner/Admin,
  CISO/ISB/KIB und Project Owner exakt gemaess `spec.md`;
- `Dockerfile`, `compose.yml`, `compose.home-baseline.yml`, `.devcontainer/`,
  `codex/`, `opencode.jsonc`, Renovate, pre-commit und Workflows;
- vorhandene Skripte fuer Build/SBOM, Analyse/Scan, Audit, Shutdown,
  Agent-Prompt, Smoke, Homogeneity, Documentation Impact, Statistics und
  Secret-Scan sowie vorhandene Tests;
- Security-, Architektur-, Betriebs-, VS-Code-, Lernenden-, A11Y- und
  Statistikdokumentation;
- Constitution v1.16.0 und installierte Governance-Preset-Vertraege.

## Erzeugte Planungsartefakte / Generated Planning Artefacts

| Artefakt / Artefact | Zweck / Purpose |
|---|---|
| `plan.md` | Technischer Plan, Constitution Checks, 12 disjunkte Gap-Arbeitsgruppen, RED/GREEN, Vertical Slice und Closeout. |
| `research.md` | Vollstaendig entschiedene Forschungsfragen; keine `NEEDS CLARIFICATION`. |
| `data-model.md` | Entitaeten, Statusinvarianten, Beziehungen und Evidenzfrische. |
| `quickstart.md` | Kausal geordneter, spaeter ausfuehrbarer Validierungsweg. |
| `contracts/hardening-evidence-contract.md` | Pfade, Kardinalitaeten, Projektionen und Autoritaetsgrenzen. |
| `contracts/gap-dispositions.schema.json` | Struktur fuer exakt 157 Dispositionen. |
| `contracts/verification-evidence.schema.json` | Struktur fuer ausgefuehrte Gate-Evidenz ohne sensible Inhalte. |
| `autonomous-run-gate-requirements.json` | Vorab deklarierte Applicable-/N/A-Gates mit Command-/Runner-Tokens und Triggern. |

## Gate-Deklarationsnachweis / Gate Declaration Evidence

Applicable sind Input, Gap-Menge, Static, Compose Config, finaler Build,
Runtime/Isolation, Full Smoke, Supply Chain, Secret, Dokumentation, A11Y,
Paritaet, macOS, Linux, Windows/WSL2, Human-only-Grenze, Statistik und Delivery.
N/A sind ASVS, Produkt-AI-SBOM, verteilte Zero-Trust-Architektur, BSI C3A/C5
Cloud-Assurance sowie Registry-/Hosting-Distribution; jede N/A-Zeile nennt
Sachgrund und Ereignis-Trigger.

Die Gate-Datei ist in dieser Planphase Intended Evidence. Tatsaechliche
Primary Evidence entsteht erst durch die spaetere Ausfuehrung der exakten
Commands auf den deklarierten Runnern/Plattformen. Nicht verfuegbare Linux- oder
Windows/WSL2-Runner duerfen nicht als bestanden simuliert werden.

## Human-only- und Scope-Grenze / Human-Only and Scope Boundary

- Alle 49 Human-only-Gaps bleiben ohne datierten Rollenbeleg `Open`,
  `Not Assessed`, `Unassessed`.
- Erlaubt ist spaeter nur repository-lokale Fakten-/Vorlagenvorbereitung.
- Verboten bleiben formale Sandbox-/Provider-/Modell-/Rechts-/Datenschutz-/
  Telemetrie-/Netzwerk-/Plattformfreigabe, Risikoakzeptanz, Secret- oder
  Schluesselaktion, externe Register und Branch-/Plattformadministration.
- Registry-Verteilung, Hosting, unabhaengige Refactorings und jeder Bypass in
  der Modellphase sind ausserhalb des Features. Der bereits autorisierte
  Admin-Bypass bleibt auf die spaetere Provider-Merge-Operation begrenzt, wenn
  `REVIEW_REQUIRED` nach allen gruenen technischen Gates, gueltiger
  Schema-2.0-PreMerge-Evidenz und null handlungsrelevanten Review-Threads der
  einzige Policy-Blocker ist; er darf keine technische/Security-Pruefung oder
  Repository-Regel umgehen.

## Modell- und Orchestrator-Aufgabentrennung / Model and Orchestrator Separation

**Modellaufgaben:** lokale finding-conditioned Implementierung, RED/GREEN,
aktuelle Evidenz und ein validierter Arbeitsbaum innerhalb des genehmigten
Scopes. / Local implementation and evidence only.

**Orchestrator-only:** Autoritaetsrevalidierung, Staging, Content-Commit, PR,
Review-/Provider-Preflight, Provider-Merge einschliesslich des bereits
autorisierten eng begrenzten Admin-Bypass-Falls, Default-Branch-Sync,
Statistik-Render und separater Statistik-Commit. Keine weitere
Autoritaetsanfrage ist fuer diesen Run erforderlich; die Bypass-Voraussetzungen
werden unmittelbar vor der Merge-Operation fail-closed revalidiert. / Delivery
mechanics only after revalidation; the already authorized Admin-Bypass case is
limited to the provider merge operation and its fail-closed prerequisites.

**Causal PostMerge:** nur Checks oder Evidenzupdates, die durch den tatsaechlich
gemergten Head veraltet wurden; keine vorgezogene oder unabhaengige Arbeit.

## Plan-Phasenabschluss / Plan Phase Completion

Die Planphase darf `Completed` melden, wenn: / Plan may report Completed when:

1. alle Pflichtartefakte existieren und JSON parsebar ist;
2. Research keine offene Klaerung enthaelt;
3. Pre-/Post-Design Constitution Check bestanden ist;
4. 157/108/49 und Human-only-Liste im Plan deterministisch erhalten sind;
5. alle spaeteren Gates vorab deklariert sind;
6. keine Implementierungs-, State-, Commit- oder Remote-Aktion erfolgte;
7. der aktuelle normalisierte SHA-256 von `plan.md` in der Runner-
   Ergebnisdatei steht.

Diese Bedingungen behaupten keine spaetere Gate- oder Feature-Erfuellung. /
These conditions do not claim later feature or gate completion.

## Finale Analyze-Phase / Final Analyze Phase

**DE:** Die abschliessende artefaktuebergreifende Pruefung vor Implementierung
hat alle sechs akzeptierten Hashbindungen erneut bestaetigt. `tasks.md`
enthaelt exakt 85 eindeutige, lueckenlose Tasks T001–T085: 69 Modellaufgaben
bis zum sicheren Rand T069 und 16 Orchestrator-Aufgaben ab T070. Alle
Abhaengigkeiten zeigen rueckwaerts; alle 63 definierten Requirement-/Policy-
IDs, alle 26 Gate-IDs und `GAP-001`–`GAP-157` sind explizit abgebildet. Die
Human-only-Menge stimmt exakt mit den 49 akzeptierten IDs ueberein; 108 Gaps
bleiben agentisch bearbeitbar.

**EN:** The final pre-implementation cross-artifact analysis re-confirmed all
six accepted hash bindings. `tasks.md` contains exactly 85 unique contiguous
tasks T001–T085: 69 model tasks through safe boundary T069 and 16 orchestrator
tasks from T070. Every dependency points backwards; all 63 defined
requirement/policy IDs, all 26 gate IDs, and `GAP-001` through `GAP-157` are
explicitly mapped. The human-only set exactly matches the 49 accepted IDs,
leaving 108 agent-actionable gaps.

Remediiert wurden die widerspruechliche T077/T079-Bypass-Autoritaet, der
historische `Tasks`-State in T001, fehlende explizite N/A-Gate- und
SC-Traceability, eine nicht deterministische `Open`/`Applicable`-
Statusinvariante sowie zwei Datenmodell-/Schemaabweichungen. Admin-Bypass ist
fuer diesen Run bereits autorisiert, aber nur innerhalb der Provider-
Merge-Operation bei alleinigem `REVIEW_REQUIRED`-Policy-Blocker nach allen
gruenen technischen Gates, null handlungsrelevanten Review-Threads und
gueltiger Schema-2.0-PreMerge-Evidenz. Technische/Security-Gates und
Repository-Regeln bleiben unantastbar; keine weitere Autoritaetsanfrage ist
erforderlich. / Remediation aligned authority, traceability, deterministic
status invariants, and data/schema contracts under the stated fail-closed
provider-merge-only Admin-Bypass rule.

Es verbleibt kein Critical-/High-Befund und kein unverantworteter
Medium-Befund. Diese Phase hat keine Produktimplementierung, keinen Commit,
Push, PR, Merge, State-Edit, Registry-/Provider-/Secret-/Freigabe-/
Risiko-/Registeraktion und keine Fortschreibung der Intake-Serie ausgefuehrt.
/ No Critical or High finding and no unowned Medium finding remains. No
product, delivery, run-state, external-administration, approval, risk, or
series-advancement action occurred.

## Terminaler Validierungsrand / Terminal Validation Boundary

**DE:** Der Run endet nach T065 mit 65 von 85 abgeschlossenen Aufgaben im
Status `Blocked`. T066 wurde genau einmal ausgefuehrt und lehnte die damalige
Gate-Menge wegen vier fehlender Abschlusszeilen ab. Diese Zeilen wurden danach
nur als Fail-/Blocked-Evidenz ergaenzt; T066 wurde nicht wiederholt. T067 bis
T085 wurden nicht gestartet.

Das unveraenderte lokale Image
`sha256:5bec1910211e61f60d140907a75689f9f6e31c2ec5baceaac7ff10b99d846eaf`
bestand Build, Runtime, 6/6-MSL-, 2/2-Script- und sechs Agenten-CLI-Smokes.
Eine CycloneDX-SBOM mit 23.967 Komponenten und der digest-gepinnte Grype-Scan
wurden genau einmal ausgefuehrt. Alle 426 Advisory-IDs sind als
`in_triage` mit offenem Blocker erfasst; auf Match-Ebene bleiben 14 Critical
und 360 High offen. Es gibt keine Risikoakzeptanz und keine erfundene
Nichtbetroffenheit.

Zusaetzlich bleiben `GATE-PARITY-01` rot, echte Linux- und Windows/WSL2-
Hostevidenz sowie VS-Code-Attach offen und `GATE-LEARNER-01` ohne den
moderierten menschlichen Erstnutzungstest blockiert. `pre-commit` und der
Agent-State-Secret-Scan bestanden im redigierten Wiederholungslauf mit
Exitcode 0. Es erfolgten kein Commit, Push, PR, Statistikrendering, Merge,
Admin-Bypass, Default-Branch-Sync oder Serienfortschritt.

**EN:** The run ends after T065 with 65 of 85 tasks complete and status
`Blocked`. T066 ran exactly once and failed; T067 through T085 did not start.
Build, runtime, language, scripting, and six agent CLI smoke evidence passed
for the unchanged image. All 426 scanner advisory IDs remain explicitly open
and in triage, including 14 Critical and 360 High match-level results. Preset
parity, Linux, Windows/WSL2, VS Code attachment, and human learner evidence
also remain unresolved. No delivery, bypass, statistics, merge, sync, risk
acceptance, or series action occurred.

## Explizite Wiederaufnahme / Explicit Resume

**DE:** Am 2026-08-30T15:00:16Z wurde ausschliesslich Run
`8330f54b-97d1-424c-ad1a-842a3fad7be3` auf ausdruecklichen Auftrag zur
Fortsetzung revalidiert. Branch, Worktree, Input- und Review-Hashes sind
unveraendert; `main` und `origin/main` stehen bei `0/0`. Intake Review
`6403c657-e508-4029-bfe8-319436f3fa7a` bleibt `Ready`. Alle sieben
abgeschlossenen Routing-Ergebnisse behalten ihre gebundenen Ergebnis-Hashes;
der blockierte Implementierungsstand wird aus den 65 Task-Checkboxen und der
aktuellen Evidenz rekonstruiert. Das lokale Codex-Routing ist `Aligned`, der
Vertrag validiert und der Preflight antwortete exakt `MODEL_READY`.

Der einzige materielle Artefaktwiderspruch war die Standard-Acht-Matrix in
Plan und T063 trotz des installierten verwalteten Zwoelf-Preset-Profils. Plan
und Task werden eng auf die bereits vorhandene
`spec-kit-model-routing-governance-presets.json` korrigiert und danach erneut
analysiert. Die aktuelle Autoritaet gilt fuer die restlichen Aufgaben dieses
unveraenderten Runs im gespeicherten Modus `MergeAndSync`; der frueher
autorisierte Admin-Bypass bleibt ausschliesslich auf eine spaetere
Provider-Merge-Operation begrenzt, wenn `REVIEW_REQUIRED` nach allen gruenen
Gates der einzige Blocker ist. Es wird kein neuer Spec-Kit-Lauf angelegt.

**EN:** Only the existing run was explicitly resumed. Identity, accepted
inputs, review, branch and routing remain current. The narrow amendment aligns
Plan and T063 with the already installed managed twelve-preset profile, after
which Analyze is rerun in the same run. Current authority covers the remaining
tasks in `MergeAndSync`; the previously granted bypass remains limited to the
provider merge operation under its fail-closed prerequisites. No new Spec Kit
run is created.

Die erneute Analyze-Phase bestand nach einer rein semantischen
Resultatformat-Korrektur mit 85/85 analysierten Tasks, 63/63 Requirement-/
Policy-IDs, 26/26 Gates und exakt 49 Human-only-IDs. Die erste Ergebnisdatei
wurde mit `AEI105` abgelehnt, weil sie Implementierungsfortschritt 65/85 statt
den vollstaendig analysierten Taskbestand 85/85 meldete; sie autorisierte
keinen Folgeschritt. Das korrigierte Ergebnis ist unter SHA-256
`a2149f710127898d396b6f5f5031fcf8bcaac932e5d54e0c8e97f0db24811d57`
gebunden. Danach bestanden beide expliziten Zwoelf-Preset-Checks sowie die
Python-Paritaetssuiten mit 3/3 und 24/24; `GATE-PARITY-01` ist `Pass`.

The rerun Analyze phase passed after correcting only the structured-result
cardinality from implementation progress to the complete analyzed inventory.
The rejected result authorized no follow-up. Both explicit twelve-preset
checks and the 3/3 plus 24/24 Python parity suites then passed; parity is now
green.

## Gepushter Uebergabecheckpoint / Pushed Handoff Checkpoint

**DE:** Der vollstaendige lokale Feature-Inhalt wurde als Commit
`91ad1f06fc93c75c98e3c6c7c2a8cf54777b1964` auf Branch
`003-secure-development-container-hardening` gepusht. GitHub-Issue
[#52](https://github.com/hindermath/absdd-image-sandbox/issues/52) beschreibt
die fehlenden Windows/WSL2-, unabhaengigen Linux/Ubuntu-, VS-Code-Attach- und
Learning/A11Y-Nachweise mit Befehlen, Evidenzfeldern, Sicherheitsgrenzen und
der exakten Fortsetzung ab T066.

Der Commit ist ein Zwischenstand fuer die plattformuebergreifende Fortsetzung,
kein positiver Gate-, Statistik-, PR- oder Merge-Abschluss. Der Run bleibt
`Blocked`; T066 wurde fuer diese Uebergabe nicht erneut ausgefuehrt und ein
neuer autonomer Lauf wurde nicht erzeugt.

**EN:** Content checkpoint
`91ad1f06fc93c75c98e3c6c7c2a8cf54777b1964` is pushed on the feature branch.
Issue #52 is the exact external-evidence handoff. This is not a positive gate,
statistics, pull-request, or merge completion. The existing run remains
Blocked, T066 was not rerun for this handoff, and no new autonomous run was
created.

## Genehmigtes Plattform-Scope-Amendment / Approved Platform Scope Amendment

**DE:** Am 2026-09-04 genehmigte `@hindermath` in den Rollen `Repository
Owner` und `Security Review` die Entscheidung
`DEC-XPLAT-WSL2-2026-09-04`. Fuer Feature 003 ersetzt Ubuntu unter WSL2 mit
eigener rootless-Podman-Laufzeit den zuvor geforderten separaten nativen
Linux-Rechner. `GATE-XPLAT-WIN-01` bleibt der Windows-Hostpfad;
`GATE-XPLAT-LINUX-01` bleibt als Gate-ID erhalten und bezeichnet jetzt den
getrennten Ubuntu/WSL2-Linux-Ausfuehrungspfad. Beide duerfen dieselbe physische
Windows-Hardware nutzen, aber keine Laufzeit, Befehls-, Zeit-, Image- oder
VS-Code-Evidenz wiederverwenden. Native Linux-Kompatibilitaet wurde nicht
geprueft und wird nicht behauptet.

Die Aenderung erteilt keinen Plattform-Pass und schliesst kein anderes Gate.
Der bestehende Run bleibt nach T065 bei `65/85` und `Blocked`; T066 wurde nicht
ausgefuehrt und es wurde kein neuer Lauf angelegt. Der erste neue
Analyze-Kandidat wurde mit `AEI002` abgelehnt, weil die letzte Ausgabe kein
striktes JSON war; er autorisierte keinen Folgeschritt. Der korrigierte
Cross-Artefakt-Lauf analysierte `85/85` Tasks, band den neuen Tasks-Hash
`0a3fdc078e83835a6dc7457c507998890b8c7ce4d959b01aff013fab3e16d9bf` und
bestand mit Ergebnis-Hash
`814c6e1d3e1cef93548dfe6b3104497cb854dded32613a48de564dbf8c34dbbd`.
Der Run darf erst nach realer Windows-Host-, Ubuntu/WSL2-, VS-Code-,
Learning/A11Y- und sonstiger offener Evidenz explizit fortgesetzt werden.

**EN:** On 2026-09-04, `@hindermath`, acting as `Repository Owner` and
`Security Review`, approved decision `DEC-XPLAT-WSL2-2026-09-04`. For Feature
003, Ubuntu under WSL2 with its own rootless Podman runtime replaces the former
separate native Linux machine requirement. The Windows-host and Ubuntu/WSL2
paths retain separate gate IDs and must not reuse runtime or evidence. This
does not claim native Linux compatibility, close a gate, execute T066, or
create a new run. The first Analyze candidate was rejected as non-JSON. The
corrected 85/85 result is bound at
`814c6e1d3e1cef93548dfe6b3104497cb854dded32613a48de564dbf8c34dbbd`; the run
remains blocked on real external evidence.

Bei der anschliessenden Pflichtvalidierung wurde im Bash-Dispatcher eine
bereits vorhandene Bash-4-Abhaengigkeit (`${MODE,,}`) sichtbar. Die eng
begrenzte, semantisch gleiche Normalisierung mit `tr` stellt die Ausfuehrung
unter dem macOS-System-Bash 3.2 wieder her. Danach bestanden die
Hardening-Suite mit 24/24, die Agent-Surface-Paritaet mit 3/3 sowie die
gleichwertigen Bash- und PowerShell-Dry-Runs. Diese lokale technische
Korrektur ersetzt keinen der weiterhin fehlenden Windows-Host-,
Ubuntu/WSL2-, VS-Code- oder Lernenden-Nachweise.

The required validation exposed a pre-existing Bash-4-only lowercase
expansion in the Bash dispatcher. Replacing it with equivalent `tr`-based
normalization restores macOS Bash 3.2 compatibility. The 24/24 hardening
suite, 3/3 agent-surface parity suite, and paired Bash/PowerShell dry runs then
passed. This local correction does not substitute for any open external gate.

## Wiederaufnahme nach Plattformuebergabe / Resume After Platform Handoff

**DE:** Am 06.09.2026 wurde ausschliesslich der bestehende Run
`8330f54b-97d1-424c-ad1a-842a3fad7be3` erneut auditiert. Branch, Checkpoint,
Tasks-Hash, sechs akzeptierte Artefakthashes und Intake-Review
`6403c657-e508-4029-bfe8-319436f3fa7a` blieben gueltig. Das Codex-Routing
wurde auf `Aligned` aktualisiert. Die erneut ausgefuehrte Analyze-Phase
bestand mit 85/85 analysierten Tasks, 63/63 Requirement-/Policy-IDs, 26/26
Gates, 157/157 Gaps, exakter 108/49-Aufteilung und rueckwaerts gerichteten
Abhaengigkeiten. Das strukturierte Ergebnis ist unter SHA-256
`a7282c684fb27ee7e3d2fdc7c0a5eb121a2e3a89d40fecbb759e3932ac70d4ac`
gebunden.

Auf macOS 26.6.2/arm64 wurde `podman compose build --pull` erfolgreich
ausgefuehrt. Das neue lokale Image
`sha256:978cb724a3cf33be6891ad99c261a0bfe441a813d90a6be9eb029b10ce4e2a72`
und Container `49adefa68ec670a563c1b8c92255a3368a9e9595506012e3ef5c79f4aaa09afe`
bestanden Runtime, den vollstaendigen Toolchain-/Agenten-Smoke, den
providerfreien Dispatcher-Dry-run und die Bash-/PowerShell-Static-Plaene. VS
Code 1.135.0 mit Dev Containers 0.466.0 haengte real an den Container an;
UI-, Status- und Prozessnachweise bestaetigten `/rider-projects`,
Remoteindikator, Terminal-Backend, `adedev` und aktiven JSON-LSP. Die lokale
Podman-Machine meldet `Rootful=true` und wird nicht als rootless Evidenz
ausgegeben; der kanonische rootless Nachweis bleibt Ubuntu/WSL2.

`GATE-XPLAT-MAC-01` und `GATE-XPLAT-01` sind damit `Pass` und `Current`. Danach
begrenzte der Repository Owner den Abschluss ausdruecklich auf eine bis
31.12.2026 befristete, allein durchgefuehrte und source-only
Machbarkeitsstudie. Die nicht verfuegbaren unabhaengigen Learning-/A11Y- und
moderierten Lernendennachweise sind ehrlich `NotPerformed`; es werden keine
Ersatzdaten erzeugt. `GATE-LEARNER-01` ist nur fuer diesen Studienabschluss
`N/A`, waehrend `GATE-A11Y-01` ausschliesslich die tatsaechlich ausgefuehrte
artefaktbezogene Pruefung belegt. Alle 390 Advisories bleiben `Open`/`in_triage`;
das Supply-Chain-Pass-Ergebnis belegt Transparenz, nicht Risikoakzeptanz,
Distribution oder Produktion.

**EN:** Only the existing run was re-audited. Branch, checkpoint, task hash,
all six accepted artifact hashes, intake review, and refreshed model routing
validated. Analyze completed for all 85 tasks and is bound at
`a7282c684fb27ee7e3d2fdc7c0a5eb121a2e3a89d40fecbb759e3932ac70d4ac`.
The current macOS arm64 image built successfully and passed runtime, full
toolchain and agent smoke, dispatcher dry run, paired static plans, and a real
VS Code Dev Containers attachment. Both macOS and consolidated platform gates
are now current Pass results. The owner then limited closeout to a
single-person, source-only feasibility study through 2026-12-31. Independent
Learning/A11Y review and moderated learner evidence are honestly NotPerformed;
no substitute data is created. GATE-LEARNER-01 is N/A only for this study,
while GATE-A11Y-01 proves only the executed artefact-level review. All 390
advisories remain Open/in_triage; the supply-chain Pass proves transparency,
not risk acceptance, distribution, or production approval. No new autonomous
run was created.

## T066-Kandidaten und erneuter Resume-Audit / T066 Candidates and New Resume Audit

**DE:** Der erste Kandidat nach der Machbarkeitsentscheidung fuehrte T066 am
06.09.2026 genau einmal aus. Seine statischen Teilpruefungen bestanden; der
Runtime-Teil konnte im untergeordneten `codex exec --sandbox workspace-write`-
Prozess den Podman-Socket nicht erreichen und endete mit Exitcode 125. Der
Gesamtbefehl endete mit Exitcode 1. T067 bis T069 wurden nicht gestartet und
der Kandidat bleibt als fehlgeschlagen belegt.

Der aktuelle Auftrag autorisiert die ausdrueckliche Wiederaufnahme desselben
Runs. Der neue Audit bestaetigte Branch und Remote-Ahead/Behind `0/0`, den
Checkpoint, alle sechs akzeptierten Artefakthashes, den Tasks-Hash, das
strukturierte Analyze-Ergebnis, unveraendertes Modell-Routing, fehlende
repositorybezogene Locks sowie den vom Host erreichbaren laufenden Podman-
Container. Ein anderer autonomer Lauf in einem anderen Repository wurde nur
beobachtet und nicht veraendert. Der neue T066-Kandidat wird deshalb direkt
durch den Orchestrator auf dem Host ausgefuehrt; dies korrigiert ausschliesslich
die nachgewiesene Socket-Grenze des untergeordneten Prozesses.

**EN:** The first candidate after the feasibility decision executed T066
exactly once on 2026-09-06. Its static subchecks passed, but the nested
`codex exec --sandbox workspace-write` process could not access the Podman
socket; the runtime check exited 125 and the overall command exited 1. T067
through T069 did not start, and this candidate remains recorded as failed.

The current request explicitly resumes the same run. The new audit confirmed
branch and remote ahead/behind 0/0, checkpoint, all six accepted-artifact
hashes, task hash, structured Analyze result, unchanged model routing, no
repository-specific locks, and a running Podman container reachable from the
host. Another autonomous run in another repository was only observed and was
not changed. The new T066 candidate is therefore executed directly by the host
orchestrator, correcting only the proven nested-process socket boundary.

## Sicherer Implementierungsrand T069 / Safe Implementation Boundary T069

**DE:** Der neu revalidierte Host-Kandidat fuehrte T066 genau einmal aus und
bestand mit Exitcode 0. Alle sechs Hardening-Modi meldeten `GREEN`; der
T066-Befund bindet 157/108/49, exakt sechs begruendete N/A-Gates, 27
Hardening-Tests, vier Dispatcher-Tests, drei Oberflaechen-Paritaetstests und den
laufenden Podman-Container. T067 bestand anschliessend mit `git diff --check`,
16 geaenderten getrackten Pfaden, vier beabsichtigten neuen Evidenzpfaden,
null fremden ungetrackten Pfaden und unveraendertem Index. Es gibt null
unabhaengige Refactorings. T068 ist durch die nicht sensiblen Sitzungsprotokolle
belegt. T066 bis T069 sind damit am sicheren Modellrand abgeschlossen; Commit,
Push, PR, Review, Merge, Bypass, Branchwechsel und Remote-Synchronisierung
wurden bis zu diesem Rand nicht ausgefuehrt.

Offen bleiben als ehrliche Grenzen 49 Human-only-Gaps, sechs begruendete
N/A-Gates und 390 Advisories mit Status `Open`/`in_triage`. Die
Machbarkeitsentscheidung ist keine formale Sandbox-, Risiko-, Distributions-
oder Produktionsfreigabe. Ab T070 besitzt ausschliesslich der Orchestrator die
aktuell bestaetigte `MergeAndSync`- und eng begrenzte Admin-Bypass-Autoritaet.

**EN:** The newly revalidated host candidate executed T066 exactly once and
passed with exit code 0. All six hardening modes reported GREEN, binding the
157/108/49 partition, exactly six reasoned N/A gates, 27 hardening tests, four
dispatcher tests, three surface-parity tests, and the running Podman
container. T067 then passed git diff hygiene and the read-only delivery-set
check with 16 changed tracked paths, four intended new evidence paths, zero
unrelated untracked paths, and an unchanged index. No independent refactoring
is present. T068 is covered by non-sensitive session logs. T066 through T069
are complete at the safe model boundary; no commit, push, PR, review, merge,
bypass, branch switch, or remote synchronization occurred before that point.

The honest residual boundaries are 49 Human-only gaps, six reasoned N/A gates,
and 390 Open/in_triage advisories. The feasibility decision is not formal
sandbox, risk, distribution, or production approval. From T070 onward, only
the orchestrator holds the currently confirmed MergeAndSync and narrowly
scoped admin-bypass authority.

## Delivery-Abschluss / Delivery Closeout

**DE:** Der validierte Content-Satz wurde als Commit
`3fb1b6d27396abbcec27e6e324ada1e60fdc188c` erstellt. Danach wurde
Statistikprofil 2 aus genau diesem Inhaltsstand gerendert, mit `-CheckOnly`
validiert und ausschliesslich als separater Commit
`8b73d0a0e0b8680011876fcf906f3b08bcd36077` geliefert. PR #53 band diesen
Head. Alle 14 beobachteten GitHub-Checks bestanden; Reviews, Kommentare und
handlungsrelevante Review-Threads waren leer. `REVIEW_REQUIRED` war der einzige
Policy-Blocker. Der bereits genehmigte Admin-Bypass wurde deshalb nur fuer die
Provider-Merge-Operation eingesetzt. GitHub erzeugte Merge-Commit
`1c67b226d5a2c7c565c8b9630376710100798894`.

Die temporaere Schema-2.0-PreMerge-Evidenz bestand unter normalisiertem Hash
`fa40edf8a2ee721a5aba64f1e3b9ebbe61e8aa4ce14f496ca99505acb102a78d`.
Die kausale PostMerge-Evidenz band diesen Hash, den reviewten Head und den
tatsaechlichen Merge-Commit bei leerem `changedPaths`; sie bestand unter
`a1b07e58497b0b05b23fc73c5f7c79d8808e7bbe2d5f14010818b6a5f7e227df`.
Der lokale `main` wurde ausschliesslich per Fast-forward synchronisiert. Vor
dem Cleanup standen `main`/`origin/main` und lokaler/remoter Feature-Branch
jeweils bei Ahead/Behind `0/0`. Danach wurden nur die bereits gemergten lokalen
und remoten Feature-Refs entfernt; beide sind jetzt abwesend.

**EN:** The validated content set was committed as `3fb1b6d...`. Statistics
Profile 2 was then rendered from that exact content state, checked, and
delivered only in separate commit `8b73d0a...`. PR #53 bound that head. All 14
observed GitHub checks passed, with no review, comment, or actionable review
thread. REVIEW_REQUIRED was the sole policy blocker, so the approved admin
bypass was used only for the provider merge operation. GitHub produced merge
commit `1c67b226...`. PreMerge `fa40edf8...` and causal PostMerge `a1b07e58...`
both validated. Local main was fast-forwarded and was 0/0 with origin/main.
The local and remote feature refs were also 0/0 before only those merged refs
were removed; both are now absent.

## Retrospektive / Retrospective

| Entscheidung / Decision | Beobachtung und Grenze / Observation and boundary | Reproduzierbarer Test / Reproducible test |
|---|---|---|
| `ObserveAgain` | Ein verschachtelter `codex exec --sandbox workspace-write`-Prozess konnte den Host-Podman-Socket nicht erreichen, waehrend derselbe T066-Befehl im Host-Orchestrator bestand. Quelle: `docs/security/agent-session-log/2026-09-06-1419.md` und der erfolgreiche Kandidat in `2026-09-06-1427.md`. Portable Zielregel: Host-Runtime-Gates direkt orchestrieren oder Socket-Zugriff als explizite Runner-Voraussetzung pruefen. Die Beobachtung bleibt einmalig und aendert deshalb noch kein gemeinsames Preset. / A nested model runner could not reach the host Podman socket while the host orchestrator passed the same T066 command. Portable target rule: orchestrate host-runtime gates directly or preflight socket access explicitly. One occurrence does not yet alter a shared preset. | In einem temporaeren Repository denselben read-only `podman compose ps`-Preflight einmal im Runnerprofil und einmal im Host-Orchestrator ausfuehren; unterschiedliche Erreichbarkeit muss fail-closed vor dem einmaligen Abnahmekandidaten erkannt werden. / Run the same read-only Podman preflight in runner and host contexts; detect differing access before the one-shot candidate. |
| `RejectProjectSpecific` | Die befristete Ein-Personen-Machbarkeitsentscheidung ist eine ausdrueckliche Feature-003-Scope-Grenze. Sie darf nicht als allgemeines Muster zum Herabsetzen von Learning-/A11Y-Gates in andere Repositories uebernommen werden. / The time-bounded single-person feasibility decision is specific to Feature 003 and must not become a generic learner-gate reduction. | Einen Fixture-Test mit fehlender Decision-ID, Ablauf oder verbotenem Pass-Claim ausfuehren; der Validator muss ablehnen. / Validate fixtures with missing identity, expiry, or a prohibited Pass claim and require failure. |
| `ObserveAgain` | Push- und Pull-Request-Ereignis erzeugten zwei gleichwertige Check-Saetze. Beide wurden terminal abgewartet; ohne expliziten sicheren Concurrency-Vertrag wurde keiner abgebrochen. / Push and pull-request events created duplicate equivalent check sets; both were allowed to complete because no safe cancellation contract exists. | In einem temporaeren Workflow beide Trigger ausloesen und erst nach nachgewiesener Concurrency-/Cancellation-Semantik eine Optimierung vorschlagen. / Trigger both events in a temporary workflow and propose optimization only after proving safe cancellation semantics. |

Es wurden keine Provider-/Accountdetails, Secrets, formalen Freigaben oder
projektspezifischen Risikoakzeptanzen in gemeinsame Guidance uebernommen. Es
wird kein weiterer Spec-Kit-Lauf oder Intake gestartet. / No provider/account
details, secrets, formal approvals, or project-specific risk acceptance were
promoted into shared guidance. No additional Spec Kit run or intake is started.
