# Implementierungsplan: GSDB-Bestandspruefung / Implementation Plan: GSDB Baseline Assessment

**Branch / Branch**: `002-gsdb-baseline-assessment`
**Datum / Date**: 2026-08-30
**Spezifikation / Specification**: [spec.md](spec.md)
**Eingabe / Input**: Feature-Spezifikation aus
`specs/002-gsdb-baseline-assessment/spec.md`

**DE:** Dieser Plan beendet Phase 0 (Research) und Phase 1 (Design) von
`/speckit-plan`. Er plant ausschliesslich die spaetere Bestandspruefung. Er
erzeugt noch keine 157 Bewertungszeilen, behebt keine Luecke, startet keinen
Folge-Intake und erteilt keine Git-, Remote- oder Human-only-Autoritaet.

**EN:** This plan completes Phase 0 (research) and Phase 1 (design) of
`/speckit-plan`. It plans only the later baseline assessment. It does not yet
create the 157 assessment rows, remediate a gap, start a follow-up intake, or
grant Git, remote, or human-only authority.

## Zusammenfassung / Summary

**DE:** Die Implementierung erstellt eine vollstaendige, reine
GSDB-Bestandspruefung der Sandbox. Eine kanonische maschinenlesbare
Bewertungsdatei wird gegen die 157 stabilen IDs der zwoelf Checklisten
abgeglichen und in eine zweisprachige Evidenzmatrix, eine priorisierte
Lueckenliste und einen Inventarabgleich ueberfuehrt. Ein separates
Validierungsergebnis bindet Eingangs-Hashes, Zaehler, Statusregeln,
Gap-Zuordnungen, Human-only-Grenzen, A11Y-Pruefung und Scope-Nachweis. Die
Assessment-Artefakte erreichen agentisch hoechstens `ReviewPending`;
`AcceptedBaseline` bleibt eine dokumentierte Entscheidung von `Project Owner`
und `Security Review`.

**EN:** Implementation creates a complete assessment-only GSDB review of the
sandbox. A canonical machine-readable assessment file is reconciled with all
157 stable IDs across the twelve checklists and projected into a bilingual
evidence matrix, a prioritised gap list, and an inventory reconciliation. A
separate validation result binds input hashes, counts, status rules, gap
mappings, human-only boundaries, accessibility review, and scope proof. The
agent-produced assessment can reach `ReviewPending` at most;
`AcceptedBaseline` remains a documented decision by the `Project Owner` and
`Security Review`.

## Technischer Kontext / Technical Context

**Primaersprache und Version / Language and version**: `N/A` fuer eine neue
Laufzeitsprache. Die Umsetzung besteht aus Markdown- und JSON-Evidenz; fuer
vorhandene, portable Read-only-Pruefungen wird PowerShell 7 mit
`pwsh -NoProfile` verwendet. / `N/A` for a new runtime language. Delivery
consists of Markdown and JSON evidence; existing portable read-only checks use
PowerShell 7 through `pwsh -NoProfile`.

**Primaere Abhaengigkeiten / Primary dependencies**: Git, `rg`, PowerShell 7,
`podman-compose`, Spec Kit, die installierten Preset-Validatoren,
`docs/secure-development/baseline-manifest.json`, die zwoelf kanonischen
Checklisten sowie vorhandene Repository-Evidenz. Keine neue Abhaengigkeit. /
Git, `rg`, PowerShell 7, `podman-compose`, Spec Kit, installed preset
validators, the baseline manifest, twelve canonical checklists, and existing
repository evidence. No new dependency.

**Speicherung / Storage**: Git-getrackte Markdown- und JSON-Dateien unter
`specs/002-gsdb-baseline-assessment/` und
`docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/`;
temporaere Exact-Head-Evidenz unter `.specify/runtime/` oder einem temporaeren
Verzeichnis bleibt ungetrackt. / Git-tracked Markdown and JSON files in the
feature and assessment evidence directories; temporary exact-head evidence in
`.specify/runtime/` or a temporary directory remains untracked.

**Testen / Testing**: Bestehende Run-State-, Phase-Result-, Gate-Evidence-,
Delivery-Set-, Intake-Series-, Preset-, Documentation-Impact- und
Statistik-Validatoren; zusaetzliche scriptlose PowerShell-Pruefungen fuer beide
JSON-Vertraege, die vollstaendige manifestierte Quellenmenge, die exakte
157-ID-Menge, aufgeloeste Referenzen, wechselseitige Matrix-/Gap-Abbildung,
Inventarzaehler und eine protokollierte 12-Punkte-Rueckverfolgungsstichprobe. /
Existing validators for run state, phase results, gate evidence, delivery set,
intake series, presets, documentation impact, and statistics; additional
script-free PowerShell checks for both JSON contracts, the complete
manifest-controlled source set, the exact 157-ID set, resolved references,
reciprocal matrix-to-gap mapping, inventory counts, and a recorded twelve-item
traceability sample.

**Zielplattform / Target platform**: Repository-Pruefung auf macOS, Linux und
Windows/WSL2, soweit die jeweilige Evidenz verfuegbar ist. Der aktuelle lokale
Planungslauf findet auf macOS statt; nicht ausgefuehrte Plattformchecks bleiben
`Open`. / Repository review on macOS, Linux, and Windows/WSL2 where evidence is
available. The current planning run is on macOS; unexecuted platform checks
remain `Open`.

**Projekttyp / Project type**: Dokumentations-, Governance- und
Assessment-Feature fuer ein Podman-basiertes Sandbox-Image; keine Anwendung,
API oder Laufzeitkomponente. / Documentation, governance, and assessment
feature for a Podman-based sandbox image; no application, API, or runtime
component.

**Leistungsziele / Performance goals**: Die Validierung weist exakt 12 von 12
Checklisten, 157 von 157 eindeutige IDs, 0 fehlende IDs, 0 Duplikate und 0
ungueltige Pflichtfelder aus. Ein Review-Sample aus jeder Checkliste ist in
insgesamt hoechstens 30 Minuten ohne muendliche Erklaerung nachvollziehbar. /
Validation reports exactly 12 of 12 checklists, 157 of 157 unique IDs, zero
missing IDs, zero duplicates, and zero invalid mandatory fields. One sample
from each checklist is traceable within 30 minutes total without oral
explanation.

**Einschraenkungen / Constraints**: Keine Aenderung an `Dockerfile`, Compose,
Laufzeitkonfiguration, Secrets, Provider-/Modellwahl, Plattform-Rulesets,
formalen Freigaben, externen Registern oder technischer Haertung. Kein
Folge-Intake vor `AcceptedBaseline`. Ein Content-Commit; ein separater
Statistik-Commit nur als spaeterer, erneut autorisierter Post-Feature-Ablauf
bei ausgeloestem Statistik-Trigger. / No change to the
Dockerfile, Compose, runtime configuration, secrets, provider/model selection,
platform rulesets, formal approvals, external registers, or technical
hardening. No follow-up intake before `AcceptedBaseline`. One content commit;
any triggered statistics commit is a separately authorized post-feature flow.

**Umfang / Scale and scope**: 157 Bewertungszeilen, 12 Checklisten, 6
MSL-Familien, 2 gesonderte Skript-/Werkzeugbasen, 4 Required-Agenten, 2
zusaetzliche Agentenoberflaechen, 12 installierte Presets, alle manifestierten
GSDB-Dokumente sowie die vorhandenen Security-, Architektur-, A11Y-, Build-,
Audit- und SBOM-Nachweise. / 157 assessment rows, 12 checklists, 6 MSL
families, 2 separate scripting/support foundations, 4 required agents, 2
additional agent surfaces, 12 installed presets, all manifest-controlled GSDB
documents, and existing security, architecture, accessibility, build, audit,
and SBOM evidence.

## Verfassungspruefung vor Research / Constitution Check Before Research

*GATE: vor Phase 0 bestanden; nach Phase 1 erneut geprueft. / GATE: passed
before Phase 0 and re-checked after Phase 1.*

| Pruefbereich / Checkpoint | Status | Planentscheidung und Evidenz / Planning decision and evidence |
|---|---|---|
| Level-2-Projektkontext / Level-2 context | `Applicable` / PASS | Der bindende Registry-Eintrag `container-images/absdd-image-sandbox` liefert Python/Bash/PowerShell als vorhandenen Automationskontext, die Podman-Pruefbasis, textorientierte Docs/A11Y, Statistikbasis `80` und die Repository-Agentensurfaces. Er wird bewertet, nicht geaendert. / The binding registry row supplies the existing automation, validation, A11Y, statistics, and agent context. It is assessed, not changed. |
| MSL / Memory-safe language | `N/A` fuer Implementierung / PASS | Keine neue Sprache oder Laufzeit. Die sechs installierten MSL-Familien bleiben Inventar-Pruefobjekte. Neubewertung bei Code- oder Skript-Scope. / No new language or runtime. The six installed MSL families remain inventory subjects. Re-evaluate for code or script scope. |
| Sichere Codeerzeugung / Secure code generation | `N/A` fuer Produktcode / PASS | Es entsteht kein Produktcode. JSON muss streng parsebar sein; Befehle bleiben read-only und quotiert. NIST SSDF und CWE Top 25 bleiben Assessment-Linsen. / No product code is created. JSON must parse strictly; commands remain read-only and quoted. NIST SSDF and CWE Top 25 remain assessment lenses. |
| Sichere Architektur und iSAQB / Secure architecture and iSAQB | `N/A` fuer Aenderung / PASS | Keine neue Struktur, Schnittstelle, Vertrauensgrenze, Datenfluss-, Runtime- oder Deployment-Aenderung. Vorhandene Architektur-, STRIDE-, CAPEC-, Zero-Trust-, SAMM-, ADR-/S-ADR- und arc42-Evidenz wird in der Matrix bewertet. / No new structure, interface, trust boundary, flow, runtime, or deployment change. Existing evidence is assessed. |
| Security-Dokumentation / Security documentation | `Applicable` / PASS | Die begruendete Evidenzablage ist `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/`. Separate neue ASVS-, SAMM-, Zero-Trust-, Cloud- oder Regulatory-Dateien sind fuer diese reine Bewertung `N/A`; fehlende Bestandsnachweise werden Gaps. / The justified evidence directory is the dated assessment path. Separate standard-specific files are N/A; missing existing evidence becomes gaps. |
| NIST SSDF und CWE Top 25 | `Applicable` / PASS | Vollstaendige Review-Linsen; keine Remediation-Behauptung. / Complete review lenses; no remediation claim. |
| OWASP ASVS | `N/A` fuer Feature-Implementierung / PASS | Kein Web-, API-, HTTP-, Authentisierungs- oder Autorisierungsdienst wird geaendert. Bestehende Anwendbarkeit bleibt Matrixgegenstand. Trigger: spaeterer passender Remediation-Scope. / No relevant service changes; existing applicability remains in the matrix. Trigger: later matching remediation scope. |
| SBOM, VEX und SLSA | `Applicable` als Assessment / PASS | Vorhandene Lieferkettenevidenz fuer das Image wird bewertet; dieses Feature erzeugt kein Image, keine SBOM, VEX oder Provenienz. / Existing image supply-chain evidence is assessed; this feature generates none of these artefacts. |
| AI-SBOM | `N/A` fuer neues Produktartefakt; `Applicable` als Bestandsfrage / PASS | KI ist Entwicklungswerkzeug, kein neuer Runtime-Bestandteil. CL-05-13 und CL-09-15 bewerten vorhandene Transparenz. Trigger: Betrieb oder Veroeffentlichung eines KI-Runtime-Bestandteils. / AI is development tooling, not a new runtime component. Existing transparency is assessed. |
| CAPEC, Zero Trust und SAMM | `Applicable` als Assessment / PASS | Vorhandene Nachweise und Luecken werden bewertet; keine neue Architektur- oder Reifegradentscheidung. / Existing evidence and gaps are assessed; no new architecture or maturity decision. |
| BSI C3A und BSI C5 | `N/A` fuer neue Artefakte / PASS | Keine Cloud-Auswahl, Providerabhaengigkeit oder Hosting-Aenderung. Vorhandene Aussagen werden bewertet; formale Assurance bleibt Human-only. / No cloud selection, provider dependency, or hosting change. Existing claims are assessed; formal assurance remains human-only. |
| NIS2, CRA, EU AI Act, DORA und Datenschutz / Regulatory screening | `Applicable` als Screening / PASS | Fakten und fehlende Evidenz werden dokumentiert; Rechtsentscheidung, Meldung und Risikoakzeptanz bleiben Human-only. / Facts and missing evidence are documented; legal decisions, notifications, and risk acceptance remain human-only. |
| Security-first | PASS | Keine Credentials, Prompt-/Antwortinhalte, Agenten-Sessions, Providerdaten oder SQLite-State werden getrackt. Evidence nennt nur Metadaten und repository-lokale Pfade. / No credentials or sensitive agent state are tracked. Evidence contains metadata and repository-local paths only. |
| A11Y / Accessibility | `Applicable` / PASS | Markdown und JSON-Statusparitaet, semantische Ueberschriften, beschreibende Links, Statuswoerter statt Farbe und vollstaendige Textalternativen werden geprueft. / Markdown and JSON status parity, semantic headings, descriptive links, text status words, and complete text alternatives are reviewed. |
| Zweisprachigkeit / Bilingual delivery | `Applicable` / PASS | Alle lesenden Artefakte sind Deutsch zuerst und Englisch danach; kontrollierte JSON-Feldnamen bleiben sprachneutral Englisch und werden im Vertrag zweisprachig erklaert. / All reader-facing artefacts are German-first and English-second; controlled JSON keys remain language-neutral English and are explained bilingually. |
| Lernendenbasis / Learner baseline | `Applicable` / PASS | CEFR B2, Erklaerung beim ersten Fachbegriff, keine vorausgesetzte Spec-Kit-Erfahrung und Verstaendlichkeit ab dem ersten Ausbildungsjahr fuer alle vier Zielberufe. / CEFR B2, first-use explanations, no assumed Spec Kit experience, and first-year comprehension for all four learner groups. |
| Cross-Platform Governance | `N/A` fuer neue Skripte / PASS | Es entsteht kein Bash-/PowerShell-Paar, Cmdlet oder Manpage. Portable `pwsh -NoProfile`-Einzeiler und vorhandene gepaarte Validatoren werden genutzt. Trigger: spaetere Skriptaenderung. / No script pair, cmdlet, or man page is created. Portable one-liners and existing paired validators are used. |
| Agentenparitaet / Agent parity | `N/A` fuer Aenderung; `Applicable` als Assessment / PASS | Agent-Guidance, Templates und Constitution werden nicht geaendert; ihre bestehende Paritaet wird inventarisiert. / Agent guidance, templates, and constitution are not changed; existing parity is inventoried. |
| Presets / Spec Kit presets | `Applicable` / PASS | Alle 12 installierten Presets werden mit Registry, zentralem Achterprofil, Version, Prioritaet, Aktivstatus und wirksamer Aufloesung abgeglichen. / All 12 installed presets are reconciled with the registry, binding eight-profile, versions, priority, enabled state, and effective resolution. |
| Statistik / Statistics | `Applicable` als Read-only-Assessment; Aenderung `N/A` / PASS | Planung und Assessment fuehren nur `render-project-statistics.* --check-only` aus und erfassen Drift als Gap. CR-004 verbietet Statistik-Aenderungen in diesem Feature. Falls der allgemeine Post-Feature-Trigger spaeter einen Statistik-Commit verlangt, ist dies ein separat autorisierter, statistik-only Ablauf nach Abschluss dieses Features. Referenzen: 80 Zeilen/Arbeitstag konservativ, 100 Thorsten-Solo fuer dieses Repository gemaess AGENTS-Profil 2. / Planning and assessment use check-only and record drift as a gap. CR-004 prohibits statistics edits in this feature. Any later triggered statistics commit is a separately authorized statistics-only post-feature workflow. |
| Dokumentationsauswirkung / Documentation impact | `UpdateRequired` / PASS | Source of truth: `spec.md`; Owner: `Project Owner` mit `Security Review`; Ziel: datierte Assessment-Evidenz; Sprachpartner inline; Distribution `RepositoryDocumentation`; Home-Sync `NoUpdateRequired`; Validierung ueber Matrix, Vertrag, A11Y-Review und Documentation-Impact-Evidenz. Trigger: Baseline-, Inventar-, Preset- oder Scope-Aenderung. / Source, owner, targets, language pairing, distribution, sync decision, validation, and trigger are explicit. |
| Autonomer Lauf / Autonomous run | `Applicable` / PASS | Run-State, Phase-Result, Gate-Requirements, Delivery-Set sowie temporaere Schema-2.0-`PreMerge`-/`PostMerge`-Evidenz werden fail-closed validiert. Mutable approval tokens sind `N/A`. / Run state, phase result, gate requirements, delivery set, and temporary exact-head evidence are validated fail-closed. Mutable approval tokens are N/A. |

**Gemeinsame Checkpoint-Evidenz / Shared checkpoint evidence:** Fuer jeden
Tabelleneintrag ist die Anwendbarkeit der erste Statuswert; `PASS` bewertet nur
die Vollstaendigkeit der Planentscheidung und behauptet keine Umsetzung der
spaeteren Kontrolle. Der getrennte Feature-Umsetzungsstatus ist in dieser
Planphase einheitlich `Not Assessed`. Evidenzpfade sind diese Tabelle,
[research.md](research.md), [data-model.md](data-model.md), die
[Vertraege](contracts/) und die jeweils im Eintrag genannten spaeteren
Assessment-Pfade. Owner ist `Repository Maintainer`, Reviewer ist `Security
Review`, und das Restrisiko bleibt bis zur 157-Zeilen-Bewertung `Unassessed`;
dies ist keine Risikoakzeptanz. Follow-up ist die Aufnahme in die spaetere
Matrix beziehungsweise bei `N/A` keine Implementierung. Gemeinsamer
Neubewertungs-Trigger ist eine Aenderung von Spezifikation, akzeptiertem
Eingangs-Hash, Constitution, Preset-Vertrag oder technischem Scope; engere
`N/A`-Trigger stehen zusaetzlich in der jeweiligen Zeile. / For every row, the
first status value is applicability; PASS means only that the planning
decision is complete and claims no implementation. Feature implementation is
uniformly Not Assessed during planning. The cited plan/design artefacts are the
evidence paths, Repository Maintainer is owner, Security Review is reviewer,
residual risk remains Unassessed without implying acceptance, and follow-up is
the later matrix or no implementation for N/A. Any specification, accepted
hash, constitution, preset-contract, or technical-scope change triggers
re-evaluation, with narrower N/A triggers retained in each row.

Es bestehen keine Verfassungsverstoesse und keine offenen Klaerungen.
No constitution violations or open clarifications remain.

## Projektstruktur / Project Structure

### Spec-Kit- und Planungsartefakte / Spec Kit and Planning Artefacts

```text
specs/002-gsdb-baseline-assessment/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── autonomous-run-state.json
├── autonomous-run-evidence.md
├── autonomous-run-gate-requirements.json
├── checklists/
│   ├── autonomous-readiness.md
│   └── requirements.md
├── contracts/
│   ├── assessment-artifact-contract.md
│   ├── assessment-results.schema.json
│   └── validation-results.schema.json
└── tasks.md                         # erst durch /speckit-tasks / by /speckit-tasks
```

### Spaetere Assessment-Evidenz / Later Assessment Evidence

```text
docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/
├── README.md                        # Leserpfad, Scope und Zustandsdefinition
├── assessment-results.json          # kanonische maschinenlesbare Bewertung
├── evidence-matrix.md               # vollstaendige 157-Zeilen-Projektion
├── prioritized-gap-list.md          # priorisiertes Gap-Register
├── inventory-reconciliation.md      # Toolchains, Agenten und Presets
├── documentation-impact.json        # strukturierte Dokumentationsentscheidung
└── validation-results.json          # Befehle, Zaehler, Hashes und Gate-Ergebnis
```

**Strukturentscheidung / Structure decision**: Es wird kein `src/`, `tests/`,
API-, Service-, Datenbank-, Dockerfile-, Compose- oder Laufzeitbaum angelegt.
Die JSON-Datei ist die kanonische strukturierte Bewertung; die drei
Markdown-Dateien sind barrierearme, zweisprachige Projektionen fuer Menschen.
Der Vertrag verhindert Drift zwischen beiden Darstellungen. / No source,
test, API, service, database, Dockerfile, Compose, or runtime tree is added.
JSON is the canonical structured assessment; the Markdown files are accessible
bilingual projections. The contract prevents drift between representations.

## Phase 0: Research

Die abgeschlossenen Entscheidungen stehen in [research.md](research.md). Sie
klaeren insbesondere: / Completed decisions are recorded in
[research.md](research.md), including:

- kanonische Quellen- und Hashbindung, / canonical source and hash binding;
- zweiachsiges GSDB-Modell plus Intake-Bewertungsstatus, / two-axis GSDB model
  plus intake assessment status;
- JSON als maschinenlesbare Quelle mit Markdown-Projektionen, / JSON as the
  machine-readable source with Markdown projections;
- strikte Human-only- und `ReviewPending`-Grenze, / strict human-only and
  `ReviewPending` boundary;
- scriptlose semantische Pruefung mit vorhandenen Validatoren, zwei
  JSON-Schemas und PowerShell,
  / script-free semantic checks using existing validators and PowerShell;
- Umgang mit dem dokumentierten, aber im Repository fehlenden
  `build-secure-development-docs.*` als Assessment-Befund statt erfundenem
  Pass, / treating the documented but missing generator as a finding;
- ein Content-Commit sowie ein nur ausserhalb dieses Features separat
  autorisierbarer Statistikablauf nach Trigger. / one content commit and a
  separately authorized post-feature statistics workflow after a trigger.

## Phase 1: Design und Vertraege / Phase 1: Design and Contracts

Das [Datenmodell](data-model.md) definiert Bewertungszeile, Evidenznachweis,
Gap, Inventareintrag, Validierungsnachweis, Assessment-Snapshot und deren
Zustaende. Der [Artefaktvertrag](contracts/assessment-artifact-contract.md)
bindet Pfade, Pflichtfelder, Projektionen, Zaehler und Authority-Grenzen. Das
[JSON-Schema](contracts/assessment-results.schema.json) prueft die Struktur der
kanonischen Bewertung. Die
[Gate-Anforderungen](autonomous-run-gate-requirements.json) deklarieren die
Abnahme-Gates vor dem ersten Implementierungs-Edit. / The data model defines
rows, evidence, gaps, inventory, validation, snapshots, and states. The
artefact contract binds paths, fields, projections, counts, and authority. The
JSON Schema checks the canonical assessment structure. Gate requirements
declare acceptance gates before the first implementation edit.

## Geplante Implementierungsfolge / Planned Implementation Sequence

1. **Preflight und unveraenderliche Eingabe / Preflight and immutable input**:
   Run-State validieren, die drei akzeptierten SHA-256-Bindungen erneut
   pruefen und das Ergebnis der letzten abgeschlossenen gerouteten Phase gegen
   seinen aktuellen Payload validieren. Aeltere Phasenergebnisse bleiben
   historische Verlaufsevidenz; sie werden nicht gegen einen durch spaetere,
   autorisierte Phasen fortgeschriebenen Payload neu bewertet. Intended-Path-
   Liste erstellen und Scope-Verbote sichern. / Validate state, recheck the
   three accepted hashes, and validate the last completed routed phase result
   against its current payload. Older phase results remain historical lineage
   evidence and are not re-evaluated against payloads changed by later
   authorised phases. List intended paths and lock the prohibited scope.
2. **Roter Vertragstest / Red contract test**: Unter einem temporaeren Pfad
   eine absichtlich unvollstaendige Assessment-Fixture gegen das JSON-Schema
   und die 157-ID-Semantik laufen lassen. Nur der erwartete Fehler gilt als
   Pass des Negativtests; die Fixture wird nicht getrackt. / Run an
   intentionally incomplete temporary fixture against schema and semantic ID
   checks. Only the expected failure passes the negative test; do not track it.
3. **Vertikaler Slice / Vertical slice**: `CL-12-05` vollstaendig von Quelle
   ueber Evidenz, Tool-/Agent-Inventar, Status, moeglichen Gap, Human-only-
   Grenze, JSON, Markdown und Validierungszaehler fuehren. Danach muss derselbe
   Vertrag gruen sein. / Carry `CL-12-05` through source, evidence, inventory,
   status, gap, authority boundary, JSON, Markdown, and validation counts; then
   pass the same contract.
4. **157-Zeilen-Matrix / 157-row matrix**: Alle stabilen IDs in kanonischer
   Checklistenreihenfolge genau einmal bewerten. Positive Stati brauchen
   bestandene lokale Checks; fehlende, alte, widerspruechliche oder nur
   plattformbezogene Evidenz bleibt `Open` oder `FollowUp`. / Assess every ID
   exactly once in canonical order. Positive states need passing local checks;
   weak evidence remains open or follow-up.
5. **Gap-Register / Gap register**: Jede Zeile ausser `AlreadySatisfied` oder
   begruendetem `N/A` genau einem stabilen Gap zuordnen; Gruppierungen behalten
   alle CL-IDs. Prioritaet, Owner, Ziel, Restrisiko, Trigger und Human-only-
   Status ausfuellen. / Map every required row to exactly one stable gap while
   preserving all IDs and mandatory follow-up fields.
6. **Inventarabgleich / Inventory reconciliation**: Soll, Build-Deklaration,
   Compose-State, Versionscheck, Smoke-Test, Dispatcher, Registry und Doku fuer
   sechs MSL-Familien, PowerShell, Node/npm, Syft, `uv`, Spec Kit, sechs
   Agentenoberflaechen und zwoelf Presets vergleichen. / Reconcile declared,
   build, runtime, test, dispatcher, registry, and documentation evidence.
7. **Lernenden- und A11Y-Projektion / Learner and A11Y projection**: Matrix,
   Gap-Liste, Inventar und README Deutsch zuerst/Englisch danach bei CEFR B2
   erstellen; jeden Zustand, jede Abhaengigkeit und Entscheidung textlich
   erklaeren. / Create German-first/English-second CEFR-B2 projections with
   complete textual state, dependency, and decision explanations.
8. **Maschinenlesbare Validierung / Machine-readable validation**:
   `validation-results.json` aus den tatsaechlich ausgefuehrten Read-only-
   Befehlen, beobachteten Zaehlern, Hashes, Plattformgrenzen und Ergebnissen
   bilden und gegen `validation-results.schema.json` pruefen. Fuer jedes Gate
   wird `Applicable` oder begruendet `N/A` getrennt vom Ergebnis erfasst; kein
   uebersprungener anwendbarer Check wird als Pass gewertet. Die Stichprobe aus
   genau einem Punkt jeder Checkliste dokumentiert Start, Ende und insgesamt
   hoechstens 1.800 Sekunden. / Record actual commands, counts, hashes,
   platform limits, applicability, and results; validate them against the
   validation-results schema. No skipped applicable check is a pass. The sample
   of exactly one item per checklist records start, finish, and at most 1,800
   seconds total.
9. **Autonome Delivery-Evidenz / Autonomous delivery evidence**: Delivery-Set
   mit dem vorhandenen Validator und einer exakten Staging-Allowlist
   validieren, einen einzigen Content-Commit mit allen ausdruecklich
   aufgelisteten, sanitisierten Sitzungslogs dieses Feature-Laufs vorbereiten,
   `git diff --cached --check` und Intended-Path-Abgleich ausfuehren. Vor Merge
   temporaere Schema-2.0-`PreMerge`-Evidenz fuer den exakten Head validieren;
   nach Merge kausale `PostMerge`-Evidenz ohne Produktdelta erfassen. / Validate
   the delivery set, prepare one content commit, check staged paths, and use
   temporary exact-head pre/post-merge evidence.
   Der vorhandene Validator verwendet intern `git write-tree`; ein `AEI004`
   wegen gesperrter Git-Metadaten bleibt daher ein echter Delivery-Blocker und
   wird nicht durch die zusaetzliche read-only Allowlist ueberstimmt. / The
   existing validator internally uses `git write-tree`; an AEI004 metadata-lock
   failure remains a real delivery blocker and is not overridden by the
   supplemental read-only allowlist.
10. **Menschliche Abnahmegrenze / Human acceptance boundary**: Agentischer
    Abschluss ist `ReviewPending`. Erst dokumentierte Mitwirkung von `Project
    Owner` und `Security Review` darf `AcceptedBaseline` setzen. / Agentic
    completion is `ReviewPending`; only documented human participation may set
    `AcceptedBaseline`.
11. **Serienfortschritt / Series advancement**: In diesem Lauf nur Manifest,
    Receipt und Review read-only pruefen und Hardening als fachlichen
    Folgekandidaten nennen. Erst nach dokumentierter `AcceptedBaseline` und
    neuer Authority darf ausserhalb dieses Features
    `/speckit-intake-series-update` den aktuellen Root abschliessen; danach
    folgen `/speckit-intake-series-status` und erst dann das read-only
    `/speckit-intake-series-next`. Dieser Lauf fuehrt keinen dieser
    Fortschrittsschritte aus. / This run only validates series evidence and
    names hardening as the subject-matter candidate. After documented
    acceptance and fresh authority, a separate series update may complete the
    root, followed by status validation and only then read-only candidate
    listing. This run performs none of those advancement steps.
12. **Lastenheft-Archivierung / Requirements-document archival**: Die
    verfassungsseitige Umbenennung nach vollstaendig gemergter Implementierung
    bleibt in diesem Assessment-Lauf `N/A`, weil Eingangs-Hash und Serienwurzel
    den aktuellen Namen binden. Erst nach `AcceptedBaseline`, abgeschlossenem
    Serienupdate und separat autorisiertem Feature-Closeout darf der dann
    gueltige Root mit `rename-lastenheft.*` archiviert werden; zuvor ist jede
    Umbenennung ein Scope- und Provenienzverstoss. / The constitution-required
    post-merge rename is N/A in this assessment run because the accepted hash
    and series root bind the current name. Only after AcceptedBaseline, the
    separately authorized series update, and separate feature closeout may the
    then-current root be archived; an earlier rename violates scope and
    provenance.
13. **Statistik-Serialisierung / Statistics serialization**: Im Assessment
    `render-project-statistics.* --check-only` ausfuehren und Drift als Gap
    dokumentieren; keine Statistikdatei aendern und keinen Statistik-Commit
    erzeugen. Nur wenn nach Abschluss dieses Features ein allgemeiner
    Statistik-Trigger und separate Authority bestehen, darf ein nachgelagerter
    Ablauf ausschliesslich Statistikdateien in genau einem eigenen Commit
    rendern und validieren. / During assessment, run check-only and record
    drift as a gap; do not edit or commit statistics. Only a later post-feature
    trigger with separate authority may create one statistics-only commit.

## Verifikations- und Gate-Matrix / Verification and Gate Matrix

| Gate-ID | Nachweis / Proof | Passbedingung / Pass condition | Fehlerbehandlung / Failure handling |
|---|---|---|---|
| `accepted-input-binding` | Hash-Pruefung der drei akzeptierten Artefakte und Run-State-Validator | Alle Pfade und Hashes stimmen; State ist strukturell gueltig. / All paths and hashes match; state is valid. | Sofort stoppen und Resume/Revalidierung verlangen. / Stop and require resume/revalidation. |
| `gsdb-source-integrity` | Manifest-, Quellen- und Checklisten-Pruefung | Alle manifestierten Pfade sind inventarisiert; 12 Checklisten mit den Einzelzahlen `12/13/15/10/13/11/12/13/17/17/12/12`, 157 eindeutige Heading-IDs und Manifestzahl 157; jeder Versions-, Sammelband- oder Generator-Drift verweist auf genau einen offenen Gap. / Every manifest path is inventoried; all twelve per-checklist counts and 157 unique IDs match; every source drift maps to one open gap. | Widerspruch als `Open`/Gap; kein positiver Matrixstatus. / Record open/gap; no positive claim. |
| `assessment-schema-contract` | Beide JSON-Schemas plus kontrollierte Enum-/Pflichtfeldpruefung | Assessment und Validierung sind schemagueltig; 157 Rows, aufgeloeste Referenzen, aktuelle Ausgabe-Hashes und keine leeren oder verbotenen Werte. / Both files validate; 157 rows, resolved references, current output hashes, and no missing or invalid values. | `Draft`; keine Delivery. / Remain Draft; no delivery. |
| `coverage-status-and-gap-traceability` | Exakter ID-Mengenvergleich, wechselseitige Status-/Gap-Zuordnung und protokollierte Stichprobe | Fehlend 0, doppelt 0, extra 0; jede erforderliche Row genau einem Gap zugeordnet; je Checkliste genau ein Sample, Gesamtzeit hoechstens 1.800 Sekunden. / Zero set errors, exact reciprocal gap mapping, and one sample per checklist within 1,800 seconds total. | `Draft`; Zaehler, IDs oder Zeitueberschreitung ausgeben. / Remain Draft and report counts, IDs, or time excess. |
| `inventory-reconciliation` | Inventarzaehler, Pflichtdimensionen und Quellenabgleich | 6 MSL, 2 Basen, 4 Required-Agenten, 2 Zusatzoberflaechen, 12 Presets; jede Abweichung ist Gap. / Required counts and dimensions pass; every mismatch becomes a gap. | Betroffene Eintraege `Open`/`FollowUp`. / Mark affected entries open/follow-up. |
| `bilingual-a11y-and-documentation-impact` | Heuristiken, dokumentierte redaktionelle Vollpruefung und Documentation-Impact-Validator | 0 fehlende EN-Partner, 0 nur visuelle Pflichtinfos, 0 unerklaerte Erstbegriffe/CEFR-Abweichungen; Reviewrecord und Impact-Evidenz gueltig. / Zero editorial defects; valid editorial and impact evidence. | `ReviewPending` gesperrt. / Block ReviewPending. |
| `assessment-scope-and-static-repository-validation` | Staging-Allowlist, Delivery-Set, Secret-/Privatpfad-Scan und statische Checks | Nur geplante Spec-Kit-/Assessment-Pfade und alle dynamisch ermittelten, einzeln aufgelisteten, sanitisierten Sitzungslogs dieses Laufs; keine fremden, privaten Host- oder verbotenen Werte/Pfade. / Only intended content and dynamically inventoried sanitized logs from this run; no unrelated, private-host, or prohibited values or paths. | Stop; Scope-Verstoss entfernen oder menschlich eskalieren. / Stop and remove violation or escalate. |
| `autonomous-delivery-integrity` | Gate-/Delivery-/aktueller Phase-Result-Validator und Exact-Head-Snapshots | Letzte abgeschlossene Phase und alle anwendbaren Gates fuer den exakten Head bestanden; keine Review-/Authority-Luecke. Historische Phasenergebnisse bleiben Verlaufsevidenz. / The last completed phase and all applicable exact-head gates pass; older phase results remain lineage evidence. | Kein Commit/Merge/Completed. / No commit, merge, or completion. |
| `statistics-assessment-only-boundary` | Statistik-Checkmodus und Pfadinventar | Check read-only; Drift als Gap; Content-Commit ohne Statistik. / Read-only check, drift gap, no statistics content. | Kein Statistik-Edit; spaeteren Trigger separat autorisieren. / No statistics edit; separate later authority. |
| `accepted-baseline-human-decision` | `N/A`: dokumentierte menschliche Doppelpruefung | Nicht agentisch erfuellbar; Trigger sind vollstaendige `ReviewPending`-Artefakte und Entscheidungen von `Project Owner` plus `Security Review`. / Human-only after complete ReviewPending artefacts. | Offen an beide Rollen uebergeben; keine Akzeptanz behaupten. / Hand off without claiming acceptance. |
| `intake-series-advancement` | `N/A`: Serienupdate ausserhalb dieses Laufs | Erst nach `AcceptedBaseline` und neuer Authority. / Only after acceptance and fresh authority. | Keinen Folge-Intake starten. / Do not start a follow-up intake. |
| `technical-hardening-and-runtime-change` | `N/A`: ausdrueckliche Scope-Grenze | Neubewertung nur in einem akzeptierten Remediation-Intake. / Re-evaluate only in an accepted remediation intake. | Keine technische Aenderung. / No technical change. |
| `parallel-autonomous-campaign` | `N/A`: einzelner begrenzter Lauf | Neubewertung nur nach ausdruecklichem Auftrag und eigener Kampagnen-Authority. / Re-evaluate only after an explicit campaign request and authority. | Keine Kampagne starten oder konsolidieren. / Do not start or consolidate a campaign. |

### Anforderungs-zu-Nachweis-Zuordnung / Requirement-to-Evidence Mapping

**DE:** Diese Zuordnung verhindert, dass eine Anforderung nur implizit in
einem Designtext vorkommt. Sie ersetzt weder die spaetere Task-Zuordnung noch
den normalen Analyze-Lauf nach `tasks.md`. / **EN:** This mapping prevents a
requirement from being covered only implicitly. It does not replace later task
traceability or the normal Analyze phase after `tasks.md`.

| Anforderungen / Requirements | Bindendes Design und Gate / Binding design and gate |
|---|---|
| `FR-001`, `FR-002`, `FR-003`, `FR-011` | Akzeptierte Eingabebindungen, 37 `SourceSnapshot`-Objekte und `accepted-input-binding`/`gsdb-source-integrity`. / Accepted bindings, 37 source snapshots, and both source gates. |
| `FR-004`, `FR-005`, `FR-006`, `FR-007`, `FR-008`, `FR-009` | `ReviewItem`, `EvidenceRecord`, Entscheidungstabelle, JSON-Schema und `assessment-schema-contract`/`coverage-status-and-gap-traceability`. |
| `FR-010`, `FR-010a`, `FR-010b`, `FR-012` | Rollen-, Risiko-, Trigger- und Evidenzregeln im Datenmodell, Vertrag und semantischen Quickstart-Check. / Role, risk, trigger, and evidence rules in model, contract, and semantic check. |
| `FR-013`, `FR-014`, `FR-015`, `FR-016`, `FR-017` | Inventarmodell mit 6/2/4/2/8/4 Sollgruppen, mindestens drei Zusatzwerkzeugen und Gate `inventory-reconciliation`. / Inventory model with the declared groups, at least three additional tools, and its gate. |
| `FR-018`, `FR-019`, `FR-020` | `Gap`, Prioritaetsregeln, wechselseitige Row-/Quellen-/Inventarzuordnung und Coverage-Gate. / Gap model, priority rules, reciprocal mappings, and coverage gate. |
| `FR-021`, `FR-022`, `FR-025` | Kanonisches JSON, sechs Projektionen, textorientierte Summary und Zustandsautomat `Draft` → `ReviewPending` → Human-only `AcceptedBaseline`. / Canonical JSON, six projections, text-first summary, and state machine. |
| `FR-023`, `FR-024` | Delivery-Set-Grenze sowie `N/A`-Gates fuer Hardening, menschliche Abnahme und Serienfortschritt. / Delivery boundary and N/A gates for remediation, acceptance, and series advancement. |
| `CR-001`, `CR-004`, `CR-005`, `CR-006`, `CR-007`, `CR-008`, `CR-009`, `CR-010`, `CR-011`, `CR-013`, `CR-015`, `CR-016`, `CR-017` | Applicability-Matrix, Inventar, Statistik-Read-only-Pruefung, Plattformgrenzen und autonome Integritaetsgates. / Applicability matrix, inventory, read-only statistics review, platform boundaries, and autonomy gates. |
| `CR-002`, `CR-003`, `CR-012`, `CR-014`, `CR-018` | DE-first/EN-second-Vertrag, A11Y-/CEFR-Vollpruefung, Nachweispfade und `documentation-impact.json`. / Bilingual contract, full A11Y/CEFR review, evidence paths, and documentation impact. |
| `SC-001`, `SC-002`, `SC-003`, `SC-004`, `SC-006`, `SC-007` | Neu berechnete Zaehler und Nullfehlerbedingungen in beiden Schemas, Semantikcheck und `validation-results.json`. / Recomputed counts and zero-error conditions in schemas, semantic check, and validation results. |
| `SC-005` | Exakte Inventarzaehler und Pflichtdimensionen im Schema und Inventar-Gate. / Exact inventory counts and required dimensions in schema and inventory gate. |
| `SC-008` | Genau zwoelf protokollierte Traceability-Samples mit insgesamt hoechstens 1.800 Sekunden. / Exactly twelve recorded samples totalling no more than 1,800 seconds. |
| `SC-009` | Bilinguale/A11Y-Heuristiken plus protokollierte redaktionelle Vollpruefung mit vier Nullzaehlern. / Automated heuristics plus recorded full editorial review with four zero counters. |
| `SC-010` | Scope- und Delivery-Set-Gate, verbotene Pfade sowie `N/A`-Folgegates. / Scope and delivery-set gate, prohibited paths, and N/A follow-up gates. |

Die copy-ready Befehle und erwarteten Ergebnisse stehen in
[quickstart.md](quickstart.md). / Copy-ready commands and expected results are
in [quickstart.md](quickstart.md).

## Commit-, Review- und Closeout-Vertrag / Commit, Review, and Closeout Contract

- **Content-Commit / Content commit**: genau ein Commit fuer Spec-Kit-
  Artefakte, Assessment-Evidenz, Vertragsdateien und alle ausdruecklich
  inventarisierten, sanitisierten Sitzungslogs dieses Feature-Laufs. Fremde
  Aenderungen und fremde Logs bleiben unberuehrt. / Exactly one commit for
  feature, assessment, contract, and all explicitly inventoried sanitized
  session logs from this feature run. Preserve unrelated changes and logs.
- **Statistik-Commit / Statistics commit**: in diesem Feature verboten. Nur ein
  separat autorisierter Post-Feature-Ablauf darf nach ausgeloestem Trigger und
  nachgewiesenem Drift ausschliesslich die vom Profil-2-Renderer vorgesehenen
  Statistikpfade in genau einem eigenen Commit liefern. / Prohibited in this
  feature. Only a separately authorized post-feature workflow may deliver one
  statistics-only commit after a trigger and proven drift.
- **PreMerge**: temporaer, Schema 2.0, exakter Content- bzw. Statistik-Head,
  keine Merge-Behauptung. / Temporary schema-2.0 evidence for the exact head,
  with no merge claim.
- **PostMerge**: kausal an akzeptierten PreMerge-Hash und tatsaechlichen
  Merge-Commit gebunden, `changedPaths` leer, kein Produktdelta. / Causally
  bound to accepted pre-merge evidence and actual merge commit, with no
  product delta.
- **Completed**: erst wenn Run-State, Tasks, Gate-Evidenz, Delivery-Modus,
  Default-Branch-Sync, Post-Merge-Aktionen und finale Validierung terminal
  sind. `ReviewPending` der fachlichen Matrix ersetzt nicht den terminalen
  technischen Laufzustand; `AcceptedBaseline` bleibt trotzdem Human-only. /
  Only when all technical closeout fields are terminal. The assessment's
  ReviewPending state is separate, while AcceptedBaseline stays human-only.

## Plan-Review-Konvergenz / Plan Review Convergence

**DE:** Der vorgezogene `plan-review` ist absichtlich die einzige
`speckit.analyze`-Ausnahme vor `tasks.md`. Der normale Analyze-Lauf nach
`/speckit-tasks` bleibt als eigene Phase bestehen. Die folgende Tabelle bindet
alle im Plan-Review gefundenen mittleren oder hoeheren Befunde an ihre
Korrektur oder an benannte spaetere Evidenz. Es verbleibt kein ungeklaerter
Critical-, High- oder Medium-Befund. / **EN:** This early plan review is the
only intentional Analyze exception before tasks.md. The normal post-tasks
Analyze phase remains required. Every medium-or-higher finding is closed below
or routed to named later evidence; none remains unresolved.

| ID | Befund / Finding | Disposition und Nachweis / Disposition and evidence |
|---|---|---|
| `PR-001` | Der Standard-Analyze-Precheck verlangt `tasks.md`, diese Routingphase liegt jedoch absichtlich davor. / Standard Analyze expects tasks, but this routed phase intentionally precedes them. | `N/A` nur fuer `plan-review`; `tasks` und der normale spaetere `analyze` bleiben im Run-State abhaengigkeitsgeordnet. / N/A only for plan-review; tasks and normal Analyze remain ordered in run state. |
| `PR-002` | `validation-results.json` hatte keinen unabhaengigen Strukturvertrag. / Validation results had no independent structural contract. | Behoben durch `contracts/validation-results.schema.json`, Vertragsabschnitt und Quickstart-Schema-/Hashpruefung. / Resolved by the new schema, contract, and quickstart checks. |
| `PR-003` | Manifestierte Quellen, Versionsdrift und Quellen-Gap-Zuordnung waren nicht vollstaendig testbar. / Manifest sources and source-drift gap mapping were not fully testable. | 37-Pfad-Inventar, `SourceSnapshot.gapId`, wechselseitige Semantik und Gate `gsdb-source-integrity`. / 37-path inventory, source gap ID, reciprocal semantics, and source-integrity gate. |
| `PR-004` | Existenz positiver Evidenz, Objekt-Referenzen, eindeutige IDs sowie wechselseitige Gap-Zuordnung konnten trotz gueltigem Schema unbemerkt driften. / Positive evidence, references, unique IDs, and reciprocal gaps could drift despite schema validity. | Schema-Bedingungen und neu berechnete Quickstart-Semantik; Zaehler duerfen nicht nur selbst berichtet werden. / Schema conditions and recomputed semantic checks. |
| `PR-005` | SC-008 besass keinen ausgefuehrten 30-Minuten-Abnahmenachweis. / SC-008 lacked an executed 30-minute acceptance proof. | Genau zwoelf Samples und maximal 1.800 Sekunden in `validation-results.json`; Gate `coverage-status-and-gap-traceability`. |
| `PR-006` | Aeltere `specify`-/`clarify`-Resultate wurden faelschlich gegen spaeter fortgeschriebene Payloads geprueft; die lesbare Lauf-Evidenz kann waehrend einer laufenden Phase hinter dem JSON-State liegen. / Older phase results were incorrectly checked against later payloads; readable run evidence may lag the JSON state while a phase is running. | Nur das letzte abgeschlossene geroutete Ergebnis ist aktueller Payload-Gate; aeltere Dateien bleiben Verlaufsevidenz. `autonomous-run-evidence.md` ist orchestration-owned und MUSS am Phasenrand vor Implementierung aus dem validierten State aktualisiert werden. / Only the last completed routed result is the current-payload gate. Readable run evidence must be refreshed from validated state at the orchestration boundary before implementation. |
| `PR-007` | „Genau ein“ Sitzungslog widersprach der Pflicht zu einem Log je Agentensitzung. / Exactly one session log conflicted with the per-session rule. | Alle einzeln inventarisierten, feature-bezogenen und sanitisierten Logs sind erlaubt; fremde Logs bleiben verboten. / All explicitly inventoried sanitized feature logs are allowed; unrelated logs remain forbidden. |
| `PR-008` | Der Delivery-Set-Validator wurde stellenweise als read-only bezeichnet, obwohl er `git write-tree` nutzt. / The delivery validator was called read-only although it uses git write-tree. | Vertrag und Quickstart benennen den Metadaten-Write und behandeln `AEI004` weiter als Blocker. / Contract and quickstart disclose the metadata write and retain AEI004 as a blocker. |
| `PR-009` | Quickstart-Fachbegriffe waren fuer Lernende nicht beim ersten Auftreten erklaert. / Quickstart terms were not explained on first use. | Bilinguale Begriffseinfuehrung vor dem ersten Validierungsschritt. / Bilingual terms section before validation. |
| `PR-010` | Tatsaechlicher GSDB-, Plattform-, Statistik-, Delivery- oder Human-only-Drift darf im Plan nicht behoben werden. / Actual source, platform, statistics, delivery, or human-only drift cannot be remediated by the plan. | Benannte Folgeevidenz: `assessment-results.json`, `prioritized-gap-list.md`, `validation-results.json` und die `N/A`-Gates in `autonomous-run-gate-requirements.json`; keine technische Aenderung. / Routed to the named assessment, gap, validation, and N/A-gate evidence; no technical change. |
| `PR-011` | Die vorhandenen Bilingual-/A11Y-Hilfsfunktionen besitzen keinen verlaesslichen Pass-/Fail-Exitcode. / Existing bilingual/A11Y helpers do not expose a reliable pass/fail exit code. | Der Quickstart-Wrapper sammelt ihre Ausgabe und scheitert bei jedem `WARN|`; die Hilfsskripte selbst bleiben im Assessment-only-Scope unveraendert. / The wrapper fails on warning output while leaving the helper scripts unchanged. |

## Post-Design-Verfassungspruefung / Post-Design Constitution Check

| Ergebnis / Result | Nachweis / Evidence |
|---|---|
| Security-first PASS | Vertrag verbietet Secrets und Agenteninhalt; Scope-Gate und Delivery-Set sind geplant. / Contract prohibits secrets and session content; scope and delivery gates are planned. |
| Architektur N/A/PASS | Keine technische Grenze oder Deployment-Aenderung; nur Bestandsbewertung. / No technical boundary or deployment change; assessment only. |
| Supply Chain PASS | SBOM/VEX/SLSA/AI-SBOM werden bewertet, nicht erzeugt oder erfunden. / Evidence is assessed, not generated or invented. |
| A11Y und Lernendenbasis PASS | Bilinguale Markdown-Projektionen, JSON-Statusparitaet und redaktionelle Vollpruefung sind verbindlich. / Bilingual projections, JSON status parity, and full editorial review are binding. |
| Cross-Platform N/A/PASS | Keine neuen Skripte; vorhandene gepaarte Validatoren und portables PowerShell werden verwendet. / No new scripts; existing paired validators and portable PowerShell are used. |
| Agentenparitaet N/A/PASS | Keine Guidance-Aenderung; bestehende Paritaet bleibt Assessment-Gegenstand. / No guidance change; existing parity remains an assessment subject. |
| Autonomie PASS | Gate-Requirements existieren vor Implementierung; Exact-Head, Delivery-Set, Phase-Result und Stop/Resume sind fail-closed geplant. / Requirements exist before implementation; evidence is fail-closed. |
| Dokumentationsauswirkung PASS | `UpdateRequired` ist mit Zielpfad, Owner, Publikum, Sprache, Distribution, Validation und Trigger vollstaendig. / Documentation impact is fully specified. |
| Statistik PASS | Assessment-Content bleibt statistikfrei; ein spaeterer getriggerter Statistik-Commit ist separat autorisiert und serialisiert. / Assessment content remains statistics-free; any later triggered statistics commit is separately authorized and serialized. |
| Lastenheft-Archivierung N/A/PASS | Der akzeptierte Pfad/Hash bleibt in diesem Lauf unveraendert; die verfassungsseitige Umbenennung ist erst nach menschlicher Akzeptanz, Serienupdate und separatem Closeout neu zu bewerten. / The accepted path/hash remains unchanged; archival is re-evaluated only after acceptance, series update, and separate closeout. |

Die gemeinsame Checkpoint-Evidenz aus der Vorpruefung gilt unveraendert auch
fuer diese Post-Design-Pruefung; nach Phase 1 bestehen weiterhin keine `Open`-
Dispositionen. / The shared checkpoint evidence from the pre-design check also
applies here; no Open disposition remains after Phase 1.

Keine Complexity-Tracking-Ausnahme ist erforderlich. / No complexity-tracking
exception is required.

## Komplexitaetspruefung / Complexity Tracking

Keine Verfassungsverletzung und keine begruendungspflichtige Zusatzkomplexitaet.
No constitution violation or exceptional complexity requires justification.
