# Research: GSDB-Bestandspruefung / GSDB Baseline Assessment

## Zusammenfassung / Summary

**DE:** Die Research-Phase loest alle Planungsfragen fuer eine reine,
maschinenpruefbare und lernendenzugaengliche Bestandsbewertung. Sie behaelt
Quell- und Versionsdrift als sichtbaren Befund, trennt JSON-Quelle und
Markdown-Projektion, bindet Status und Gaps deterministisch und stoppt vor
Human-only-Abnahme, Serienfortschritt oder technischer Remediation.

**EN:** Research resolves every planning question for an assessment-only,
machine-checkable, learner-accessible review. It preserves source and version
drift as findings, separates the JSON source from Markdown projections, binds
statuses and gaps deterministically, and stops before human acceptance, series
advancement, or technical remediation.

## Entscheidung: Akzeptierte Eingaben bleiben unveraenderlich / Decision: Accepted Inputs Remain Immutable

**DE:** Die Bestandspruefung bindet sich an die drei in `spec.md` genannten
Pfade und SHA-256-Werte. Der Planlauf hat diese Werte erneut gelesen und exakt
bestaetigt. Aendert sich ein Pfad oder Hash, stoppt die Umsetzung und verlangt
eine ausdrueckliche Revalidierung des autonomen Laufs.

**EN:** The assessment binds to the three paths and SHA-256 values recorded in
`spec.md`. The planning run re-read and matched all values exactly. A changed
path or hash stops delivery and requires explicit autonomous-run revalidation.

**Begruendung / Rationale:** Intake, Serien-Review und Serienmanifest bilden
gemeinsam Scope, Reihenfolge und Authority-Grenze. / Intake, series review, and
manifest jointly define scope, order, and authority.

**Verworfene Alternativen / Alternatives considered:**

- Nur den Intake lesen: verworfen, weil Review- und Serienzustand verloren
  gingen. / Read only the intake: rejected because review and sequencing state
  would be lost.
- Geaenderte Quellen still neu hashen: verworfen, weil dies die akzeptierte
  Bindung ohne Authority ersetzen wuerde. / Silently re-hash changed inputs:
  rejected because it would replace accepted authority.

## Entscheidung: Kanonische GSDB-Quellen und jede Abweichung sichtbar halten / Decision: Preserve Canonical GSDB Sources and Expose Every Difference

**DE:** Das Manifest, die zwoelf Einzelchecklisten, Richtlinie, Sammelband und
alle manifestierten Begleitdokumente werden getrennt inventarisiert. Stabile
IDs werden ausschliesslich aus den kanonischen Checklisten-Headings gelesen.
Manifest- oder Versionskonflikte werden nicht waehrend der Bestandspruefung
korrigiert, sondern als `Open` oder `FollowUp` in Matrix und Gap-Register
festgehalten.

**EN:** The manifest, twelve individual checklists, guideline, compendium, and
all manifest-controlled companion documents are inventoried separately. Stable
IDs are read only from canonical checklist headings. Manifest or version
conflicts are not fixed during assessment; they are recorded as `Open` or
`FollowUp` in the matrix and gap register.

**Begruendung / Rationale:** Die reine Bewertung darf ihre eigene Quelle nicht
reparieren und danach den reparierten Zustand als urspruengliche Evidenz
ausgeben. / Assessment-only work must not repair its source and then present
the repaired state as original evidence.

**Beobachtete Research-Signale / Observed research signals:**

- `baseline-manifest.json` nennt Basis `3.1.0` und Sammelband `2.1.0`, waehrend
  Richtlinie und Sammelband neuere sichtbare Versionsangaben enthalten. / The
  manifest declares baseline `3.1.0` and compendium `2.1.0`, while the
  guideline and compendium visibly contain newer version claims.
- Der README-Stand und die manifestierten Versionen einzelner Checklisten
  muessen gegen die Dateien abgeglichen werden. / README and manifest version
  claims for individual checklists require reconciliation.
- Die in der GSDB-Dokumentation genannten gepaarten
  `build-secure-development-docs.*`-Skripte sind im aktuellen Repository nicht
  auffindbar. Das ist ein zu bewertender Nachweisbefund, kein Grund, einen
  erfundenen Generator-Pass zu melden. / The paired generator scripts named in
  GSDB documentation are not present in the current repository. This is an
  evidence finding, not permission to claim a fabricated generator pass.

**Verworfene Alternativen / Alternatives considered:**

- Den Sammelband als alleinige Quelle verwenden: verworfen, weil das Manifest
  die Einzelchecklisten als kanonisch festlegt. / Use the compendium alone:
  rejected because the manifest makes individual checklists canonical.
- Versionsdrift im Plan reparieren: verworfen als technische bzw. normative
  Aenderung ausserhalb des Assessment-Scope. / Repair version drift in the
  plan: rejected as an out-of-scope normative change.

## Entscheidung: JSON ist die maschinenlesbare Quelle, Markdown die barrierearme Projektion / Decision: JSON Is the Machine-Readable Source and Markdown the Accessible Projection

**DE:** `assessment-results.json` enthaelt Assessment-Snapshot,
Quellen-Snapshots, genau 157 Bewertungszeilen, Evidenzrecords, Gaps,
Inventareintraege und exakte Summen. `evidence-matrix.md`,
`prioritized-gap-list.md` und `inventory-reconciliation.md` projizieren
dieselben IDs und Kernaussagen Deutsch zuerst/Englisch danach. Ein JSON-Schema
und semantische Mengenpruefungen verhindern leere Pflichtfelder, ungueltige
Statuskombinationen und Projektionsdrift.

**EN:** `assessment-results.json` contains the assessment snapshot, source
snapshots, exactly 157 review rows, evidence records, gaps, inventory entries,
and exact summaries. The three Markdown artefacts project the same IDs and core
statements in German-first/English-second form. A JSON Schema and semantic set
checks prevent missing fields, invalid status combinations, and projection
drift.

**Begruendung / Rationale:** Reine Markdown-Tabellen sind gut lesbar, aber
schwer streng zu validieren. Nur JSON waere fuer Lernende und Screenreader bei
157 umfangreichen Eintraegen unhandlich. / Markdown is readable but hard to
validate strictly; JSON alone is cumbersome for learners and assistive
technology across 157 detailed records.

**Verworfene Alternativen / Alternatives considered:**

- Nur Markdown: verworfen wegen schwacher maschineller Feld- und
  Mengenpruefung. / Markdown only: rejected because field and set validation is
  weak.
- Nur JSON: verworfen wegen Lernenden- und A11Y-Anforderungen. / JSON only:
  rejected because of learner and accessibility requirements.
- Neue Generator-Skripte: verworfen, weil CR-015 fuer dieses Feature neue
  Skriptwerkzeuge als `N/A` festlegt. / New generator scripts: rejected because
  CR-015 makes new script tooling N/A.

## Entscheidung: Dreifaches Statusmodell streng und deterministisch anwenden / Decision: Apply the Three-Layer Status Model Strictly and Deterministically

**DE:** Jede Zeile behaelt Anwendbarkeit, Umsetzungsstatus und genau einen
Intake-Bewertungsstatus. Die Entscheidungstabelle aus FR-007 wird in der dort
festgelegten Reihenfolge ausgewertet. `AlreadySatisfied` ist nur mit aktueller,
repository-lokaler, im Assessment bestandener Evidenz erlaubt. Unklare oder
nicht reproduzierbare Evidenz hat Vorrang und fuehrt zu `Open` oder
`FollowUp`.

**EN:** Every row preserves applicability, implementation status, and exactly
one intake assessment status. The FR-007 decision table is applied in its
stated order. `AlreadySatisfied` requires current repository-local evidence
that passed during assessment. Unclear or non-reproducible evidence takes
precedence and results in `Open` or `FollowUp`.

**Begruendung / Rationale:** Ein konsolidierter Status allein wuerde
Nichtanwendbarkeit, fehlende Bewertung und fehlende Umsetzung vermischen. /
A consolidated status alone would conflate non-applicability, missing
assessment, and missing implementation.

**Verworfene Alternativen / Alternatives considered:**

- Neue Statuswerte einfuehren: verworfen, weil sie Manifest und Spezifikation
  verletzen. / Add status values: rejected because they would violate the
  manifest and specification.
- Fehlende Evidenz als `N/A` behandeln: verworfen, weil fehlende Evidenz keine
  sachliche Nichtanwendbarkeit ist. / Treat missing evidence as N/A: rejected
  because missing evidence is not factual non-applicability.

## Entscheidung: Jeder offene oder teilweise erfuellte Punkt hat genau einen Gap / Decision: Every Open or Partly Fulfilled Item Has Exactly One Gap

**DE:** Jede Zeile mit `Open`, `FollowUp` oder dem besonderen Screeningstatus
`Applicable` verweist auf genau eine stabile Gap-ID. Ein Gap darf mehrere
CL-IDs mit gleicher Ursache gruppieren, muss aber jede ID nennen und die
Gruppierung begruenden. Inventarabweichungen verwenden denselben Gap-Vertrag.

**EN:** Every `Open`, `FollowUp`, or screening-only `Applicable` row references
exactly one stable gap ID. A gap may group multiple CL IDs with one root cause,
but must list each ID and justify grouping. Inventory differences use the same
gap contract.

**Begruendung / Rationale:** So bleiben Matrix, Lueckenliste und spaeterer
Hardening-Intake vollstaendig rueckverfolgbar. / This keeps the matrix, gap
list, and later hardening intake completely traceable.

**Verworfene Alternativen / Alternatives considered:**

- Mehrere Gaps pro Zeile: verworfen wegen unklarer Ownership und doppelter
  Abnahme. / Multiple gaps per row: rejected because ownership and acceptance
  would be ambiguous.
- Gruppierte IDs nur als Bereich angeben: verworfen, weil einzelne CL-IDs
  verschwinden koennten. / Record grouped IDs only as a range: rejected because
  individual IDs could disappear.

## Entscheidung: Bestandsbeobachtungen getrennt von Soll-Angaben modellieren / Decision: Separate Inventory Observations from Target Claims

**DE:** Toolchain-, Agenten- und Preset-Inventar trennt jede Soll-Angabe von
Beobachtungen in `Dockerfile`, Compose, Registry, Versionscheck, Smoke-Test,
Dispatcher und Dokumentation. Widersprueche werden nicht durch Mehrheitslogik
aufgeloest, sondern als Gap dokumentiert.

**EN:** Toolchain, agent, and preset inventory separates each target claim
from observations in the Dockerfile, Compose, registries, version checks,
smoke tests, dispatchers, and documentation. Conflicts are not resolved by
majority vote; they become gaps.

**Begruendung / Rationale:** Installation, Pinning, Laufzeitpruefung,
Persistenz, Dispatcher-Support und dokumentierte Kategorie sind verschiedene
Eigenschaften. / Installation, pinning, runtime verification, persistence,
dispatcher support, and documented category are distinct properties.

**Beobachtete Research-Signale / Observed research signals:**

- Das zentrale Preset-Profil konfiguriert acht Governance-Presets; die lokale
  Installation zeigt zusaetzlich vier Intake-/Routing-Presets, insgesamt 12. /
  The central profile configures eight governance presets; local installation
  adds four intake/routing presets, totalling 12.
- Agentenkategorien und die gleichzeitige Gemini-/Antigravity-Sicht muessen
  zwischen CLI-Registry, Dockerfile, Compose, Smoke-Test, Dispatcher und Doku
  abgeglichen werden. / Agent categories and the concurrent Gemini/Antigravity
  surfaces require reconciliation across all named sources.

**Verworfene Alternativen / Alternatives considered:**

- Nur `Dockerfile` als Wahrheit: verworfen, weil Laufzeit, Mounts, Dispatcher
  und Doku nicht belegt waeren. / Use only the Dockerfile: rejected because
  runtime, mounts, dispatchers, and documentation would be unproved.
- Nur `specify preset list`: verworfen, weil zentrale Sollmatrix und wirksame
  Aufloesung fehlen. / Use only preset list: rejected because target matrix and
  effective resolution would be missing.

## Entscheidung: Vorhandene Validatoren plus zwei JSON-Vertraege und scriptlose PowerShell-Semantik / Decision: Existing Validators Plus Two JSON Contracts and Script-Free PowerShell Semantics

**DE:** Vorhandene gepaarte Validatoren pruefen autonomen State, Phase-Result,
Gate-Evidenz, Delivery-Set, Intake-Serie, Preset-Matrix, Documentation Impact
und Statistik. `assessment-results.schema.json` bindet die Bewertung;
`validation-results.schema.json` bindet die tatsaechlich ausgefuehrten Gates,
Ausgabe-Hashes und die 12-Punkte-Rueckverfolgungsstichprobe. Ein portabler
PowerShell-Block liest beide JSON-Dateien, die Schemas und
Checklisten-Headings fuer die feature-spezifischen Mengen-, Referenz- und
Beziehungsregeln. Er wird als exakter Befehl in `quickstart.md` dokumentiert,
aber nicht als neues Repository-Skript gespeichert.

**EN:** Existing paired validators cover autonomous state, phase result, gate
evidence, delivery set, intake series, preset matrix, documentation impact,
and statistics. Separate schemas bind the assessment and its executed
validation, output hashes, and twelve-item traceability sample. A portable
PowerShell block reads both JSON files, their schemas, and checklist headings
for feature-specific set, reference, and relationship rules. It is documented
as an exact quickstart command but is not stored as a new script.

**Begruendung / Rationale:** Dies nutzt vorhandene Muster, vermeidet neue
Cross-Platform-Skriptpflichten und liefert trotzdem reproduzierbare
maschinenlesbare Validierung. / This uses existing patterns, avoids new
cross-platform script obligations, and still provides reproducible
machine-readable validation.

**Verworfene Alternativen / Alternatives considered:**

- Fehlen des dokumentierten GSDB-Generators ignorieren: verworfen; der Befund
  muss sichtbar bleiben. / Ignore the missing documented GSDB generator:
  rejected; the finding must remain visible.
- Einen Bash-only-Validator hinzufuegen: verworfen wegen Paritaets- und
  Scope-Verstoss. / Add a Bash-only validator: rejected because of parity and
  scope.

## Entscheidung: Autonome Cross-File-Evidenz vor Implementierung revalidieren / Decision: Revalidate Autonomous Cross-File Evidence Before Implementation

**DE:** Der JSON-Run-State ist strukturell gueltig und markiert die im Runner
gestartete `plan-review`-Phase als `Running`; die letzte abgeschlossene
geroutete Phase `plan` besitzt ein gueltiges, an den aktuellen `plan.md`-Payload
gebundenes Ergebnis. Die aelteren `specify`- und `clarify`-Ergebnisse binden
ihren damaligen Payload und bleiben historische Verlaufsevidenz. Sie werden
nicht gegen eine Spezifikation neu validiert, die durch spaetere autorisierte
Phasen fortgeschrieben wurde. Vor dem ersten Implementierungs-Edit und vor
jeder Delivery werden der aktuelle State, die lesbare Evidence und genau das
Ergebnis der letzten abgeschlossenen gerouteten Phase fail-closed geprueft.
Runtime-`*.log.txt`-Dateien bleiben ausgeschlossen.

**EN:** The JSON run state is structurally valid and marks `plan-review` as
Running; the last completed routed phase, `plan`, has a valid result bound to
the current plan payload. Older specify and clarify results bind their former
payloads and remain historical lineage evidence. They are not revalidated
against a specification changed by later authorised phases. Before the first
implementation edit and every delivery, validate current state, readable
evidence, and exactly the last completed routed phase result fail-closed.
Runtime log files remain excluded.

**Begruendung / Rationale:** Ein strukturell gueltiges Einzelartefakt beweist
nicht die Aktualitaet der gesamten Evidenzkette. / One structurally valid
artefact does not prove freshness of the complete evidence chain.

**Verworfene Alternativen / Alternatives considered:**

- Alle historischen Resultate gegen den neuesten Payload pruefen: verworfen,
  weil spaetere autorisierte Phasen denselben Payload fortschreiben duerfen;
  aktuellkeitsbindend ist das Ergebnis der letzten abgeschlossenen Phase. /
  Revalidate every historical result against the latest payload: rejected
  because later authorised phases may evolve that payload; the last completed
  phase result supplies the current freshness binding.
- Prompt-/Antwortlogs als Ersatznachweis committen: verworfen wegen
  Security-first, Datenschutz und Delivery-Scope. / Commit prompt/response logs
  as substitute evidence: rejected by security, privacy, and delivery scope.

## Entscheidung: Human-only-Abnahme endet agentisch bei ReviewPending / Decision: Agentic Assessment Stops at ReviewPending

**DE:** `Draft -> ReviewPending` ist bei vollstaendigen Artefakten und
bestandenen technischen Gates erlaubt. `ReviewPending -> AcceptedBaseline`
verlangt dokumentierte Mitwirkung von `Project Owner` und `Security Review`.
Kein Agenten-, Modell-, Exitcode- oder Merge-Ergebnis ersetzt diese
Entscheidung.

**EN:** `Draft -> ReviewPending` is permitted after complete artefacts and
passing technical gates. `ReviewPending -> AcceptedBaseline` requires
documented participation by the `Project Owner` and `Security Review`. No
agent, model, exit code, or merge result substitutes for this decision.

**Begruendung / Rationale:** Technische Vollstaendigkeit ist keine formale
Risiko- oder Baseline-Akzeptanz. / Technical completeness is not formal risk or
baseline acceptance.

**Verworfene Alternativen / Alternatives considered:**

- Bei gruenen Gates automatisch akzeptieren: verworfen als Human-only-
  Verletzung. / Auto-accept on green gates: rejected as a human-only violation.
- Human-only-Zeilen aus der Matrix entfernen: verworfen, weil dies Luecken
  verbergen wuerde. / Remove human-only rows: rejected because it would hide
  gaps.

## Entscheidung: Der Folge-Intake bleibt bis Akzeptanz und separat autorisiertem Serienupdate blockiert / Decision: Follow-Up Intake Remains Blocked Until Acceptance and a Separately Authorized Series Update

**DE:** Der aktuelle Lauf darf den Serienzustand read-only validieren. Erst
nach `AcceptedBaseline` und neuer Authority darf ein separater
`/speckit-intake-series-update`-Aufruf den aktuellen GSDB-Root abschliessen.
Danach validiert `/speckit-intake-series-status` den Zustand; erst dann kann
`/speckit-intake-series-next` den naechsten Kandidaten read-only anzeigen.
Keiner dieser Fortschrittsschritte gehoert zu diesem Lauf.

**EN:** The current run may validate series state read-only. Only after
`AcceptedBaseline` and fresh authority may a separate series-update command
complete the current GSDB root. Series-status validation follows, and only then
may the read-only next command list the next candidate. None of these
advancement steps belongs to this run.

**Begruendung / Rationale:** Reihenfolge-Evidenz erteilt keine
Implementierungs- oder Delivery-Autoritaet. / Sequencing evidence grants no
implementation or delivery authority.

**Verworfene Alternativen / Alternatives considered:**

- Hardening automatisch starten: verworfen durch FR-024/025 und die
  Serien-Governance. / Start hardening automatically: rejected by the spec and
  sequencing governance.

## Entscheidung: Ein Content-Commit; Statistik im Feature nur read-only / Decision: One Content Commit; Statistics Are Read-Only in This Feature

**DE:** Alle Feature- und Assessment-Inhalte sowie alle ausdruecklich
inventarisierten, sanitisierten Sitzungslogs dieses Feature-Laufs werden in
genau einem Content-Commit zusammengefasst. Im Assessment prueft Profil 2 nur read-only auf
Statistikdrift; vorhandene Drift wird ein Gap, weil CR-004 Statistik-Aenderungen
in diesem Feature verbietet. Falls nach Feature-Abschluss ein allgemeiner
Trigger und neue Authority bestehen, darf ein separater Post-Feature-Ablauf
genau einen statistik-only Commit erzeugen. PreMerge-/PostMerge-Snapshots
bleiben temporaere Exact-Head-Evidenz und erzeugen keinen Produktdelta-Commit.

**EN:** All feature and assessment content plus every explicitly inventoried,
sanitized session log from this feature run is grouped into exactly one content
commit. During assessment, Profile 2 checks drift read-only; drift becomes a
gap because CR-004 prohibits statistics edits in this feature. A separately
authorized post-feature workflow may create exactly one statistics-only commit
only after a later trigger. Exact-head snapshots create no product delta.

**Begruendung / Rationale:** Statistik beschreibt einen abgeschlossenen
Meilenstein und darf den geprueften Content-Head nicht waehrend der
Reviewentscheidung veraendern. / Statistics describes a completed milestone
and must not change the reviewed content head during review.

**Beobachteter Read-only-Stand / Observed read-only state:** Beide vorhandenen
Renderer-Varianten melden am 2026-08-30 denselben Status `DRIFT` fuer
Source-Revision `db0f7c92984a`, 132838 getrackte Textzeilen und 63 aktive Tage.
Dieser Befund wird in der spaeteren Matrix beziehungsweise im Gap-Register
erfasst; die Planphase hat keine Statistikdatei geaendert. / Both existing
renderer variants report the same DRIFT state for source revision
`db0f7c92984a`, 132838 tracked text lines, and 63 active days. The later
assessment records this finding; planning changed no statistics file.

**Verworfene Alternativen / Alternatives considered:**

- Statistik im Assessment oder Content-Commit: verworfen durch CR-004 und die
  Serialisierungsanforderung. / Put statistics in the assessment or content
  commit: rejected by CR-004 and serialization requirements.
- Den spaeteren Trigger im Assessment still ausfuehren: verworfen; Post-Feature-
  Statistik braucht eigene Authority. / Silently execute the later trigger:
  rejected because post-feature statistics needs separate authority.

## Offene Klaerungen / Remaining Clarifications

Keine. Alle fachlichen Unbekannten sind als Entscheidung, nachgelagerter
Assessment-Befund oder Human-only-Grenze aufgeloest. / None. Every material
unknown is resolved as a decision, later assessment finding, or human-only
boundary.
