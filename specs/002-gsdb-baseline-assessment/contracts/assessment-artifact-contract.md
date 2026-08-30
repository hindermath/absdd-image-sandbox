# Artefaktvertrag: GSDB-Bestandspruefung / Artefact Contract: GSDB Baseline Assessment

## Vertragszweck / Contract Purpose

**DE:** Dieser Vertrag beschreibt die dateibasierten Schnittstellen der
Bestandspruefung. Es handelt sich nicht um eine API oder Laufzeitschnittstelle.
Er bindet die kanonische JSON-Bewertung, ihre barrierearmen
Markdown-Projektionen, das Validierungsergebnis und die Human-only-Grenze.

**EN:** This contract describes the file-based interfaces of the baseline
assessment. It is not an API or runtime interface. It binds the canonical JSON
assessment, accessible Markdown projections, validation results, and the
human-only boundary.

## Feste Ausgabepfade / Fixed Output Paths

Alle Implementierungsausgaben liegen unter: / All implementation outputs are
stored below:

`docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/`

| Datei / File | Rolle / Role | Kanonisch / Canonical |
|---|---|---|
| `README.md` | Leserpfad, Begriffe, Scope, Zustand und Verifikationsweg. / Reader path, terms, scope, state, and verification route. | Nein / No |
| `assessment-results.json` | Vollstaendige strukturierte Bewertung mit 157 Rows, Evidenz, Gaps, Inventar und Summen. / Complete structured assessment. | Ja / Yes |
| `evidence-matrix.md` | Deutsch-first/Englisch-second Projektion aller 157 Rows. / Bilingual projection of all rows. | Nein / No |
| `prioritized-gap-list.md` | Projektion aller stabilen Gaps nach Prioritaet. / Projection of stable gaps by priority. | Nein / No |
| `inventory-reconciliation.md` | Projektion des Toolchain-, Agenten- und Preset-Abgleichs. / Inventory reconciliation projection. | Nein / No |
| `documentation-impact.json` | Strukturierte `UpdateRequired`-Entscheidung fuer die Dokumentfamilie. / Structured documentation-impact decision. | Eigener Validator / Own validator |
| `validation-results.json` | Tatsaechlich ausgefuehrte Befehle, Hashes, Zaehler, Grenzen, Rueckverfolgungsstichprobe und Gate-Ergebnisse. / Executed commands, hashes, counts, limits, traceability sample, and gate results. | `validation-results.schema.json` plus Semantikpruefung / schema plus semantic checks |

## Kanonische JSON-Bewertung / Canonical JSON Assessment

`assessment-results.json` MUSS gegen
`specs/002-gsdb-baseline-assessment/contracts/assessment-results.schema.json`
gueltig sein. Strukturpruefung allein genuegt nicht; die semantischen
Mengen-, Status- und Beziehungsregeln dieses Vertrags MUESSEN ebenfalls
bestehen. / The file MUST validate against the schema. Structural validation
alone is insufficient; semantic set, status, and relationship rules must also
pass.

### Top-Level-Pflichtobjekte / Required Top-Level Objects

- `schemaVersion`: `1.0`.
- `assessment`: genau ein `AssessmentSnapshot`. / Exactly one snapshot.
- `sources`: genau 37 `SourceSnapshot`-Objekte, eines fuer jeden eindeutigen
  manifestkontrollierten Pfad; genutzte Repository-Nachweise stehen getrennt
  unter `evidence`. / Exactly 37 source snapshots, one per unique
  manifest-controlled path; used repository evidence is recorded separately.
- `evidence`: nicht leere Liste von `EvidenceRecord`-Objekten.
- `matrixRows`: genau 157 `GSDBReviewItem`-Objekte.
- `gaps`: alle und nur die von Rows oder Inventory benoetigten Gaps. / All and
  only required gaps.
- `inventory`: `toolchains`, `agents`, `presets` und `additionalTools`.
- `summary`: exakte Zaehler und Fehlerzaehler.

`summary.checklistCounts` enthaelt genau einmal `CL-01` bis `CL-12` mit den
Soll-/Ist-Werten `12, 13, 15, 10, 13, 11, 12, 13, 17, 17, 12, 12`. Die
geschlossenen Namen der weiteren Zaehler sind die drei Anwendbarkeitswerte, die
vier Umsetzungswerte, die fuenf Assessment-Stati, `P0` bis `P3` sowie
`HumanOnly`/`NotHumanOnly`. Alle Werte werden aus den Detailobjekten neu
berechnet. / `summary.checklistCounts` contains each checklist exactly once
with the stated expected and actual values. All other count sets use the closed
status, priority, and human-only vocabularies and are recomputed from details.

### ID- und Kardinalitaetsregeln / ID and Cardinality Rules

1. Die kanonischen Heading-IDs aus den zwoelf Checklisten sind die erwartete
   Menge. / Canonical heading IDs from twelve checklists are the expected set.
2. `matrixRows[].clId` entspricht dieser Menge exakt: 157 Rows, 157 eindeutige
   IDs, 0 fehlend, 0 extra. / Rows match exactly: 157 rows and unique IDs, no
   missing or extra IDs.
3. Jede `evidenceId`, `sourceId`, `gapId`, `inventoryId` und `observationId` ist
   innerhalb ihres Typs eindeutig. / Every ID is unique within its type.
4. Jede Referenz zeigt auf ein vorhandenes Objekt. / Every reference resolves.
5. Jede gap-pflichtige Row verweist auf genau einen Gap; jede betroffene CL-ID
   des Gaps verweist auf denselben Gap zurueck. / Required row-to-gap mappings
   are exact and reciprocal.
6. `AlreadySatisfied` und begruendetes `N/A` verwenden `gapId: "N/A"`. /
   AlreadySatisfied and justified N/A use N/A.
7. Jede Inventarabweichung verweist auf genau einen Gap. / Every inventory
   mismatch references one gap.
8. Jeder im Baseline-Manifest genannte Pfad ist genau einmal als
   `SourceSnapshot` inventarisiert; jede nicht `Aligned` bewertete Quelle
   verweist auf genau einen offenen Gap und dieser verweist in seiner
   Nachweislage auf dieselbe Quelle. / Every manifest-controlled path appears
   exactly once; every non-Aligned source maps to one open gap with reciprocal
   source evidence.
   `Aligned` ist nur mit `verificationResult: Pass`, aktuellem Datei-Hash und
   existierendem Pfad erlaubt. / Aligned additionally requires a passing
   verification result, current file hash, and existing path.
9. Jede als `Pass` verwendete Evidenz besitzt `freshness: Current`, einen beim
   Review existierenden repository-lokalen Pfad und einen tatsaechlich
   ausgefuehrten Read-only-Schritt oder eine konkrete Dateiinspektion. / Every
   passing evidence record is current, has an existing repository-local path,
   and records an executed read-only check or concrete inspection.
10. Alle in dieser Assessment-Ausgabe erzeugten Gaps besitzen `state: Open`;
    spaetere Lifecycle-Zustaende duerfen nur in separat autorisierter
    Remediation-Evidenz erscheinen. / Every gap created here is Open; later
    lifecycle states belong only to separately authorised remediation.

### Statusregeln / Status Rules

Die Kombinationen aus `spec.md` FR-007 und `data-model.md` sind bindend. Die
Reihenfolge `N/A`, `Open`, `AlreadySatisfied`, `FollowUp`, `Applicable` wird
deterministisch angewendet. / The FR-007 combinations and their stated order
are binding.

- Fehlende, veraltete, widerspruechliche, uebersprungene oder nicht
  reproduzierbare Evidenz kann niemals `AlreadySatisfied` stuetzen. / Weak or
  skipped evidence can never support AlreadySatisfied.
- `N/A` ist nur sachliche Nichtanwendbarkeit, niemals fehlende Evidenz. / N/A
  means factual non-applicability, never missing evidence.
- `Unassessed`-Restrisiko ist nur bei `Open` erlaubt. / Unassessed residual risk
  is allowed only for Open.
- Rollen stammen ausschliesslich aus der kontrollierten Liste. / Roles come
  only from the controlled list.
- Human-only-Entscheidungen bleiben offen und nennen den menschlichen Owner und
  Stop-Grund. / Human-only decisions remain open and name the human owner and
  stop reason.

## Evidenzmatrix / Evidence Matrix

`evidence-matrix.md` MUSS alle 157 Rows genau einmal darstellen. Fuer
Screenreader und Textbrowser wird die Matrix in zwoelf Abschnitte mit
wiederholten Tabellenueberschriften geteilt; die Summe der Datenzeilen bleibt
157. / The matrix MUST show all 157 rows exactly once. It is split into twelve
sections with repeated headers for accessibility; the total remains 157.

Jede sichtbare Zeile enthaelt mindestens: / Every visible row includes at
least:

- CL-ID und zweisprachigen Kurztitel, / CL ID and bilingual short title;
- Quellenpfad/-version, / source path/version;
- alle drei Statusangaben, / all three status values;
- verantwortliche Rolle und Reviewer, / responsible role and reviewer;
- kurze zweisprachige Begruendung, / short bilingual rationale;
- Evidenz-ID/Pfad und Pruefmethode, / evidence ID/path and method;
- Restrisiko, Folgeaktion/Zieltermin und Trigger, / residual risk, action/date,
  and trigger;
- Human-only-Kennzeichen und Gap-ID. / human-only marker and gap ID.

Breite Details DUERFEN unmittelbar unter der Tabelle als eindeutig mit der
CL-ID ueberschriebene Abschnitte stehen, wenn dadurch die Tabelle besser mit
Screenreadern nutzbar wird. Pflichtinformationen duerfen nicht nur ueber
Farbe, Position oder Symbol vermittelt werden. / Wide details MAY appear in
CL-ID-labelled sections below the table for accessibility. No required
information may rely only on colour, position, or symbols.

## Priorisierte Lueckenliste / Prioritised Gap List

`prioritized-gap-list.md` MUSS jeden Gap aus JSON genau einmal darstellen und
nach `P0`, `P1`, `P2`, `P3`, dann `gapId` sortieren. / The gap list MUST show
every JSON gap exactly once, sorted by priority and ID.

Jeder Gap beginnt mit einer Ueberschrift der Form `### GAP-001`, damit die
Projektion ohne visuelle Interpretation maschinell abgeglichen werden kann. /
Every gap starts with a heading such as `### GAP-001`, enabling machine checks
without visual interpretation.

Jeder Eintrag nennt alle Felder aus FR-018. Gruppierte Gaps listen jede CL-ID
einzeln und begruenden die gemeinsame Ursache. Human-only ist kein Grund fuer
eine niedrigere Prioritaet. / Every entry includes all FR-018 fields. Grouped
gaps list every CL ID and justify the shared cause. Human-only status never
lowers priority.

Die Lueckenliste ist keine Autorisierung zur Behebung. / The gap list grants no
remediation authority.

## Inventarabgleich / Inventory Reconciliation

`inventory-reconciliation.md` MUSS Soll-Angabe und jede Beobachtung getrennt
zeigen. / The inventory projection MUST keep target claims and observations
separate.

Jeder Inventareintrag beginnt mit einer Ueberschrift der Form `### INV-*`. /
Every inventory item starts with a heading of the form `### INV-*`.

**Mindestabdeckung / Minimum coverage:**

- 6 MSL-Familien: .NET/C#, Java/JVM, Go, Rust, Python, Swift.
- 2 gesonderte Basen: PowerShell 7, Node.js/npm.
- weitere Werkzeuge: Syft, `uv`, Spec Kit.
- 4 Required-Agenten: Codex, Claude Code, Antigravity CLI, GitHub Copilot CLI.
- 2 Zusatzoberflaechen: OpenCode, Gemini CLI.
- 12 Presets: 8 verbindliches Profil plus 4 Routing-/Intake-Presets.

Fuer Agenten bleiben Installation, Pin, Versionscheck, State-Volume,
Dispatcher, Provider/Sign-in und dokumentierte Kategorie getrennte Spalten.
Fuer Presets bleiben ID, Version, Prioritaet, Aktivstatus, wirksame
Template-Aufloesung und CL-Abdeckung getrennte Spalten. / Agent and preset
properties remain separate fields.

## Validierungsergebnis / Validation Result

`validation-results.json` MUSS gegen
`specs/002-gsdb-baseline-assessment/contracts/validation-results.schema.json`
gueltig sein und zusaetzlich die folgenden semantischen Regeln bestehen. / It
MUST validate against the validation-results schema and pass these semantic
rules:

- `schemaVersion: "1.0"`;
- die drei akzeptierten Eingangsbindungen, sechs Hash-Bindungen fuer alle
  anderen Ausgaben und `validationResultsPath` fuer den eigenen Pfad; der
  eigene Hash wird in temporaerer Exact-Head-Evidenz gebunden, nicht
  selbstreferenziell in derselben Datei. / the three accepted input bindings,
  six hashes for every other output, and its own path; exact-head evidence
  binds the validation file hash externally;
- jeden Gate-Nachweis mit exaktem ausgefuehrtem Befehl, Plattform/Runner,
  Anwendbarkeit, Start/Ende, Exitcode, erwartetem und beobachtetem Ergebnis; /
  every gate record with applicability and exact execution facts;
- `observedCounts` mit exakten Summen aus `AssessmentSummary` und den
  tatsaechlichen Detailobjekten; / observed counts matching both the summary
  and detailed objects;
- `overallResult`: `Pass`, `Fail` oder `Blocked`;
- `assessmentStateResult`: hoechstens `ReviewPending`, solange Human-Akzeptanz
  fehlt. / at most ReviewPending without human acceptance;
- alle uebersprungenen oder blockierten Checks mit Grund. / all skipped or
  blocked checks with reason.
- genau zwoelf Rueckverfolgungssamples, je eines fuer `CL-01` bis `CL-12`, mit
  aufgeloester Row, Evidenz und bedingtem Gap sowie einer Gesamtdauer von
  hoechstens 1.800 Sekunden. / exactly one resolved traceability sample per
  checklist, totalling at most 1,800 seconds.

Ein anwendbares `Skipped` oder `Blocked` verhindert `overallResult: "Pass"`.
Ein Validatorname oder gruener Aggregatstatus ersetzt nicht den tatsaechlich
ausgefuehrten Befehl. / Applicable skipped/blocked checks prevent Pass. A
validator name or aggregate green status does not replace the executed command.
Ein `N/A`-Gate ist `Skipped`, nennt Begruendung und konkreten
Neubewertungs-Trigger und darf kein `Pass` behaupten. Alle selbst berichteten
Zaehler und Hashes werden gegen die Detailobjekte beziehungsweise aktuellen
Dateien neu berechnet. / An N/A gate is Skipped with rationale and trigger; it
cannot claim Pass. Recompute every reported count and hash from details and
current files.

## Dokumentations-, Lernenden- und A11Y-Vertrag / Documentation, Learner, and A11Y Contract

- Deutsch steht in lesenden Artefakten zuerst, Englisch folgt direkt. /
  German comes first and English follows directly.
- Ueberschriften verwenden `DE / EN`, ausser bei Eigennamen. / Headings use
  DE / EN except proper nouns.
- Sprache ist ungefaehr CEFR B2; Fachbegriffe werden beim ersten Auftreten
  kurz erklaert. / Language targets CEFR B2 and explains first-use terms.
- Spec-Kit-Erfahrung wird nicht vorausgesetzt. / No Spec Kit experience is
  assumed.
- Zustaende, Abhaengigkeiten, Entscheidungen, Diagramme und Zaehler erhalten
  vollstaendige Textalternativen. / States, dependencies, decisions, diagrams,
  and counts have complete text alternatives.
- Kontrollierte JSON-Werte bleiben sprachneutral Englisch; README und Vertrag
  erklaeren sie zweisprachig. / Controlled JSON values remain English and are
  explained bilingually.
- Die redaktionelle Vollpruefung meldet 0 fehlende Sprachpartner, 0
  unerlaeuterte Erstbegriffe, 0 visuell-only Pflichtinformationen und 0
  unerklaerte CEFR-Abweichungen. / Editorial review reports zero defects in
  these categories.

## Scope- und Sicherheitsvertrag / Scope and Security Contract

Zulaessige Content-Pfade sind die Feature-Artefakte, der datierte
Assessment-Ordner und alle einzeln inventarisierten, sanitisierten
Agent-Session-Logs dieses Feature-Laufs. Die Repository-Pflicht erzeugt pro
Sitzung einen Log; daher ist die Anzahl nicht pauschal auf eins begrenzt. /
Allowed content paths are feature artefacts, the dated assessment directory,
and every explicitly inventoried sanitized agent-session log from this feature
run. Repository governance creates one log per session, so the total is not
artificially limited to one.

Verboten sind Aenderungen an: / Changes are prohibited to:

- `Dockerfile`, `compose*.yml`, Laufzeit- oder Agentenkonfiguration, / runtime
  or agent configuration;
- Secrets, Provider-/Modellwahl, Anmeldung oder Telemetrie-Freigabe, /
  secrets, provider/model choice, sign-in, or telemetry approval;
- Plattform-Rulesets, formalen Freigaben oder externen Registern; / platform
  rulesets, formal approvals, or external registers;
- technischen Hardening-Dateien; / technical hardening files;
- Statistikdateien innerhalb des Assessment-Content-Commits; / statistics
  files in the assessment content commit;
- `.specify/runtime/**/*.log.txt` oder anderen Prompt-/Antwort-/Sessionlogs. /
  prompt, response, or session logs.

Alle gelieferten Text- und JSON-Inhalte MUESSEN Secret-Werte, Prompt-/Antwort-
Inhalte und private Hostpfade ausschliessen. Strukturierte Pfadfelder sind
repository-relativ; zusaetzlich prueft die Staging-Abnahme Freitextfelder und
sanitisierte Sitzungslogs gegen `/Users/<name>`, nicht-kanonische
`/home/<name>`-Pfade und `C:\Users\<name>`. Der generische Containerpfad
`/home/adedev` ist erlaubt. / Delivered text and JSON content MUST exclude
secret values, prompt/response content, and private host paths. Structured path
fields are repository-relative, and staged free text plus sanitized session
logs are checked for private macOS, Linux, and Windows user paths; the generic
container path `/home/adedev` is allowed.

Ausserhalb des Scope gefundene Sachverhalte werden nur als Gap mit Owner,
Folgeaktion und Trigger dokumentiert. / Out-of-scope findings are recorded only
as gaps with owner, action, and trigger.

## Assessment-Lebenszyklus und Authority / Assessment Lifecycle and Authority

| Zustand / State | Bedeutung / Meaning | Wer darf setzen? / Who may set? |
|---|---|---|
| `Draft` | Bewertung oder Gates unvollstaendig. / Assessment or gates incomplete. | Repository Maintainer oder Agent innerhalb Scope. / Maintainer or in-scope agent. |
| `ReviewPending` | 157 Rows, Gaps, Inventar und technische Gates vollstaendig; keine menschliche Baseline-Akzeptanz. / Complete technical assessment without human acceptance. | In-scope Implementierung nach bestandenen Gates. / In-scope delivery after gates pass. |
| `AcceptedBaseline` | Menschlich gepruefte und formell akzeptierte Eingangsbaseline fuer moeglichen Folge-Intake. / Human-reviewed accepted baseline. | Nur dokumentiert gemeinsam durch `Project Owner` und `Security Review`. / Only both human roles. |

Der aktuelle Lauf startet oder avanciert keinen Folge-Intake. Die spaetere
Kette ist: dokumentierte `AcceptedBaseline` -> separat autorisiertes
`/speckit-intake-series-update` -> `/speckit-intake-series-status` -> read-only
`/speckit-intake-series-next`. Jeder Schritt besitzt eigene Authority und
Evidenz. / The current run neither starts nor advances a follow-up intake. The
later chain is accepted baseline, separately authorized series update, status
validation, then read-only next-candidate listing. Each step has separate
authority and evidence.

## Commit- und Exact-Head-Vertrag / Commit and Exact-Head Contract

- Ein Assessment-Content-Commit enthaelt alle geplanten Content-Pfade, alle
  ausdruecklich aufgelisteten sanitisierten Sitzungslogs dieses Laufs und keine
  Statistik. / One assessment content commit contains all planned content,
  every explicitly listed sanitized session log from this run, and no
  statistics.
- Der Content-Commit erfordert den vorhandenen Delivery-Set-Validator,
  Staging-Inventar, `git diff --cached --check`, statische
  Repository-Validierung und Secret-Scan. Der Validator verwendet intern
  `git write-tree` und ist deshalb nicht read-only; ein `AEI004`-Lockfehler
  bleibt ein echter Blocker. / The content commit requires the existing
  delivery-set validator and declared checks. Because that validator uses
  `git write-tree`, it is not read-only; an AEI004 metadata-lock failure remains
  a blocker.
- Schema-2.0-`PreMerge`-Evidenz ist temporaer und bindet den exakten
  reviewten Head. / PreMerge evidence is temporary and exact-head bound.
- `PostMerge` bindet den akzeptierten PreMerge-Hash und tatsaechlichen
  Merge-Commit, hat leere `changedPaths` und erzeugt kein Produktdelta. /
  PostMerge binds accepted evidence and has no product delta.
- Statistik wird im Assessment nur read-only bewertet. Ein spaeterer
  Statistik-Commit ist ein separater, erneut autorisierter Post-Feature-Ablauf
  nach Trigger und Drift. / Statistics is assessment-only and read-only. Any
  later statistics commit is a separately authorized post-feature workflow.

## Abnahme / Acceptance

Der Vertrag ist technisch erfuellt, wenn JSON-Schema, Semantikpruefung,
Projektionsparitaet, A11Y-/Dokumentationspruefung, Scope-Gate und autonome
Exact-Head-Evidenz bestanden sind und `validation-results.json` dies mit
aktuellen Hashes dokumentiert. Dies erlaubt `ReviewPending`, aber nicht
`AcceptedBaseline`. / Technical contract completion permits ReviewPending, not
AcceptedBaseline.
