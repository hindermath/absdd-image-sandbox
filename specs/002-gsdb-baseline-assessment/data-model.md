# Datenmodell: GSDB-Bestandspruefung / Data Model: GSDB Baseline Assessment

## Zweck / Purpose

**DE:** Dieses Feature besitzt keine Laufzeitdatenbank. Das Modell definiert
die strukturierten Bewertungs-, Evidenz- und Validierungsobjekte fuer
`assessment-results.json` sowie ihre zweisprachigen Markdown-Projektionen.

**EN:** This feature has no runtime database. The model defines the structured
assessment, evidence, and validation objects for `assessment-results.json` and
their bilingual Markdown projections.

## AssessmentSnapshot

**Zweck / Purpose:** Bindet Identitaet, Scope, Eingaben, Zustand und
Authority-Grenze einer einzelnen Bestandspruefung. / Binds identity, scope,
inputs, state, and authority boundary for one assessment.

**Felder / Fields:**

- `assessmentId`: stabile Kennung / stable identifier.
- Die Vertragsversion steht einmal als Top-Level-`schemaVersion`, initial
  `1.0`; sie wird nicht im Snapshot dupliziert. / The contract version appears
  once as the top-level `schemaVersion`, initially `1.0`; it is not duplicated
  inside the snapshot.
- `scopePath`: Repository-Wurzel der bewerteten Sandbox. / Repository root of
  the assessed sandbox.
- `assessmentState`: `Draft`, `ReviewPending` oder `AcceptedBaseline`.
- `assessmentDate`: UTC-Zeitpunkt der gebundenen Bewertung. / UTC timestamp of
  the bound assessment.
- `reviewedRepositoryRevision`: voller Git-Commit-Hash oder bei noch
  uncommitteter Authoring-Phase `WORKTREE` mit spaeterer Exact-Head-Bindung. /
  Full Git commit hash, or `WORKTREE` during authoring with later exact-head
  binding.
- `ownerRole`: genau eine zulaessige generische Rolle. / Exactly one allowed
  generic role.
- `reviewerRole`: genau eine zulaessige generische Rolle. / Exactly one
  allowed generic role.
- `acceptedInputBindings`: genau die drei `{path, sha256}`-Objekte aus
  `spec.md`. / Exactly the three objects from the specification.
- `baselineVersionObserved`: beobachteter Stand; ein Konflikt ersetzt nicht
  den manifestierten Wert. / Observed version; a conflict does not replace the
  manifest value.
- `outputPaths`: Pfade der JSON- und Markdown-Projektionen. / Paths of JSON and
  Markdown projections.
- `scopeExclusions`: explizite Liste der verbotenen Aenderungsbereiche. /
  Explicit list of prohibited change areas.
- `nextIntakeDependency`: Pfad des Hardening-Intakes plus Bedingung
  `AcceptedBaseline` und separat autorisierter Serienfortschritt. / Hardening
  intake path plus AcceptedBaseline and separately authorized series
  advancement condition.
- `humanAcceptance`: `required`, beteiligte Rollen, Nachweispfad oder `N/A`
  solange nicht erfolgt. / Required flag, participating roles, and evidence
  path or N/A until completed.

**Validierungsregeln / Validation rules:**

- Es gibt genau drei Eingangsbindungen; Pfad und Hash muessen mit `spec.md`
  uebereinstimmen. / Exactly three bindings must match the specification.
- `AcceptedBaseline` ist nur mit dokumentierter Beteiligung von `Project
  Owner` und `Security Review` sowie einem existierenden Nachweispfad erlaubt.
  / AcceptedBaseline requires both human roles and an existing evidence path.
- Ein Agent darf hoechstens `ReviewPending` setzen. / An agent may set at most
  ReviewPending.
- Hash-, Baseline- oder Scope-Drift setzt den Snapshot zurueck auf `Draft` und
  verlangt Revalidierung. / Drift returns the snapshot to Draft and requires
  revalidation.

## SourceSnapshot

**Zweck / Purpose:** Dokumentiert, welche GSDB- oder Repository-Quelle wann,
wie und mit welchem Ergebnis geprueft wurde. / Records which GSDB or repository
source was checked, when, how, and with what result.

**Felder / Fields:**

- `sourceId`: stabile ID. / Stable ID.
- `sourceRole`: `Manifest`, `Guideline`, `Checklist`, `Compendium`, `Related`,
  `Learning`, `Reference`, `ManagedBinary` oder `RepositoryEvidence`.
- `path`: repository-relativer Pfad. / Repository-relative path.
- `manifestDeclaredVersion` und `observedVersion`.
- `sha256`: beobachteter Datei-Hash. / Observed file hash.
- `generated`: Boolean fuer generierte Quellen. / Boolean for generated
  sources.
- `observedItemIds` und `observedItemCount` fuer Checklisten/Sammelband.
- `currencyStatus`: `Aligned`, `Missing`, `Conflicting`, `Stale` oder
  `NotReproducible`.
- `gapId`: bei `Aligned` der kontrollierte Wert `N/A`, sonst genau ein
  vorhandener offener Gap. / `N/A` for Aligned; otherwise exactly one existing
  open gap.
- `verificationCommand`, `expectedResult`, `observedResult`,
  `verificationResult`, `checkedAt`, `platform`, `limitations`.

**Validierungsregeln / Validation rules:**

- Jede Matrixzeile verweist auf genau einen kanonischen Checklist-Snapshot. /
  Every matrix row references exactly one canonical checklist snapshot.
- Ein Versionskonflikt bleibt als Beobachtung erhalten und wird nicht durch
  den manifestierten Wert ueberschrieben. / Version conflicts remain observed
  and are not overwritten by manifest claims.
- `Aligned` verlangt `verificationResult: Pass`; jeder andere Quellenstatus
  verbietet `Pass`. / Aligned requires a passing result; every other source
  status prohibits Pass.
- Jede manifestierte Quelle ist genau einmal als SourceSnapshot vorhanden;
  fehlende oder abweichende Quellen verweisen wechselseitig auf genau einen
  Gap. / Every manifest-controlled source appears exactly once; missing or
  divergent sources map reciprocally to exactly one gap.

## GSDBReviewItem

**Zweck / Purpose:** Eine der genau 157 Bewertungszeilen. / One of exactly 157
assessment rows.

**Pflichtfelder / Required fields:**

- `clId`: stabile ID im Format `CL-01-01` bis zum letzten manifestierten
  Pruefpunkt. / Stable CL ID.
- `titleDe`, `titleEn`.
- `sourceSnapshotId`, `sourcePath`, `sourceVersion`.
- `applicability`: `Applicable`, `N/A` oder `Open`.
- `implementationStatus`: `Fulfilled`, `Partly Fulfilled`, `Not Fulfilled`
  oder `Not Assessed`.
- `assessmentStatus`: `Applicable`, `AlreadySatisfied`, `N/A`, `Open` oder
  `FollowUp`.
- `learningStage`: `Year1`, `Year2`, `Year3` oder begruendete
  checklistenbezogene Kombination. / Checklist-based combination with
  rationale.
- `responsibleRole`, `reviewerRole`, bedingt `followUpOwner`.
- `rationaleDe`, `rationaleEn`.
- `evidenceIds`: mindestens eine Evidenzreferenz oder ein ausdruecklicher
  Missing-/External-Boundary-Eintrag. / At least one evidence reference or an
  explicit missing/external-boundary record.
- `verificationMethod`, `reviewDate`, `platformLimitation`.
- `residualRisk`: `None identified`, `Low`, `Medium`, `High`, `Critical` oder
  `Unassessed`; dazu `residualRiskRationale`. / Plus rationale.
- `nextAction`, `targetDate`, `reevaluationTrigger`.
- `humanOnly`: Boolean, plus `humanOnlyReason` bei `true`.
- `mappedStandards`, `mappedPresets`.
- `gapId`: genau eine ID, wenn der Status einen Gap verlangt, sonst `N/A`. /
  Exactly one ID when required, otherwise N/A.

**Zulaessige Rollen / Allowed roles:**

`Repository Maintainer`, `Project Owner`, `Security Review`, `Platform
Owner/Admin`, `Privacy/Legal Review`, `CISO/ISB/KIB` und `Learning/A11Y Review`.

**Deterministische Statusregeln / Deterministic status rules:**

| Assessment-Status | Anwendbarkeit + Umsetzung / Applicability + implementation | Gap | Zusatzregel / Additional rule |
|---|---|---|---|
| `N/A` | `N/A` + `Not Assessed` | nein / no | Begruendung und konkreter Scope-Trigger. / Rationale and concrete scope trigger. |
| `Open` | `Open` + `Not Assessed` oder `Applicable` + `Not Assessed` | ja / yes | Ungeklaerte oder nicht reproduzierbare Evidenz. / Unresolved or non-reproducible evidence. |
| `AlreadySatisfied` | `Applicable` + `Fulfilled` | nein / no | Aktuelle lokale Pass-Evidenz. / Current local passing evidence. |
| `FollowUp` | `Applicable` + `Partly Fulfilled` oder `Applicable` + `Not Fulfilled` | ja / yes | Bestaetigte Luecke und konkrete Aktion. / Confirmed gap and concrete action. |
| `Applicable` | `Applicable` + `Not Assessed` | ja / yes | Bewusstes Screening ohne Umsetzungsbewertung; keine verdeckte Evidenzluecke. / Deliberate screening without hidden evidence gap. |

**Weitere Regeln / Additional rules:**

- `AlreadySatisfied` braucht mindestens einen `EvidenceRecord` mit `Pass`,
  existierendem Repository-Pfad und aktuellem Check. / Requires at least one
  current passing repository-local evidence record.
- `Unassessed` ist nur mit `Open` erlaubt und erzeugt mindestens Gap-Prioritaet
  `P1`, ausser ein belegtes `P0` liegt vor. / Unassessed is allowed only with
  Open and creates at least P1 unless P0 evidence exists.
- `nextAction` und `targetDate` duerfen nur bei `AlreadySatisfied` oder
  begruendetem `N/A` den Wert `N/A` tragen. / May be N/A only for these states.
- Human-only-Zeilen bleiben offen und nennen die passende menschliche Rolle;
  ein Agent ist weder Owner noch Reviewer der formalen Entscheidung. /
  Human-only rows remain open and name the correct human role.
- Kein Pflichtfeld ist leer; `Unassigned`, Agenten- oder Modellnamen sind als
  Rollen verboten. / No required field is empty; unassigned, agent, and model
  role names are forbidden.

## EvidenceRecord

**Zweck / Purpose:** Reproduzierbarer Nachweis oder ausdruecklich fehlende bzw.
externe Evidenz. / Reproducible proof or explicitly missing/external evidence.

**Felder / Fields:**

- `evidenceId`.
- `kind`: `RepositoryPath`, `ReadOnlyCheck`, `MissingEvidence` oder
  `ExternalBoundary`.
- `path`: existierender repository-relativer Pfad oder `N/A` mit Begruendung. /
  Existing repository-relative path or justified N/A.
- `sourceVersionOrSha256`.
- `command`, `expectedResult`, `observedResult`.
- `result`: `Pass`, `Fail`, `Skipped` oder `Open`.
- `checkedAt`, `platform`, `limitations`, `freshness`.
- `containsSensitiveContent`: muss `false` sein. / Must be false.

**Validierungsregeln / Validation rules:**

- `Pass` verlangt einen tatsaechlich ausgefuehrten Befehl oder eine konkrete
  Dateiinspektion mit beobachtetem Ergebnis, `freshness: Current` und einen zum
  Pruefzeitpunkt existierenden repository-lokalen Pfad. / Pass requires an
  executed check or concrete inspection, Current freshness, and a repository
  path that exists at review time.
- `Skipped` ist niemals positive Evidenz. / Skipped is never positive evidence.
- Prompt-, Antwort-, Secret- oder Sessioninhalte sind verboten. / Prompt,
  response, secret, and session content is prohibited.
- Pfadfelder sind repository-relativ. Befehle, Ergebnisse, Grenzen und
  Projektionen duerfen keine privaten Hostpfade wie `/Users/<name>`,
  nicht-kanonische `/home/<name>`-Pfade oder `C:\Users\<name>` enthalten. Der
  kanonische Containerpfad `/home/adedev` bleibt als generische Laufzeitangabe
  zulaessig. / Path fields are repository-relative. Commands, results,
  limitations, and projections must not expose private host paths such as the
  examples above; the generic container path `/home/adedev` remains allowed.
- Ein EvidenceRecord kann von mehreren Rows genutzt werden; jede Row behaelt
  ihre eigene Begruendung. / Evidence may be reused, while every row keeps its
  own rationale.

## Gap

**Zweck / Purpose:** Eine bestaetigte oder offene Abweichung fuer spaetere,
separat autorisierte Bearbeitung. / A confirmed or open difference for later,
separately authorized work.

**Felder / Fields:**

- `gapId`: stabil und eindeutig, Format `GAP-001`. / Stable and unique.
- `state`: in dieser kanonischen Assessment-Ausgabe ausschliesslich `Open`.
  `Planned`, `EvidenceReady`, `HumanReviewPending` und `Closed` gehoeren zu
  spaeterer, separat autorisierter Remediation-Evidenz. / Only `Open` is valid
  in this canonical assessment output; later lifecycle states belong to
  separately authorised remediation evidence.
- `priority`: `P0`, `P1`, `P2` oder `P3` nach FR-019.
- `affectedClIds`: nicht leere, eindeutige Liste. / Non-empty unique list.
- `summaryDe`, `summaryEn`.
- `rootCause`, `evidenceState`, `impact`, `likelihood`, `dependencies`.
- `owner`, `followUpAction`, `acceptanceCriterion`, `expectedEvidence`.
- `targetDate`, `residualRisk`, `reevaluationTrigger`.
- `humanOnly`, `humanOnlyRole` bedingt.
- `groupingRationale`: erforderlich bei mehr als einer CL-ID. / Required for
  more than one CL ID.

**Validierungsregeln / Validation rules:**

- Jede gap-pflichtige Matrixzeile verweist auf genau einen Gap. / Every
  gap-requiring row references exactly one gap.
- Jede `affectedClId` existiert genau einmal in der Matrix und verweist zurueck
  auf denselben Gap. / Every affected ID exists once and points back.
- Human-only senkt die Prioritaet nicht. / Human-only status does not lower
  priority.
- Ein Gap ist keine Implementierungs- oder Risikoakzeptanz-Autoritaet. / A gap
  grants no implementation or risk-acceptance authority.

## InventoryItem und InventoryObservation

**Zweck / Purpose:** Trennt Soll-Angabe von jeder technischen oder
dokumentarischen Beobachtung. / Separates target claims from every technical or
documentary observation.

**InventoryItem-Felder / InventoryItem fields:**

- `inventoryId`, `category`, `displayNameDe`, `displayNameEn`.
- `expectedClassification`, `expectedVersionOrPin`, `requiredCountGroup`.
- `reconciliationStatus`: `Aligned`, `Mismatch`, `Missing`, `Open`.
- `observations`: mindestens eine eingebettete `InventoryObservation`; dadurch
  bleibt jede Beobachtung ohne zweite Referenzliste eindeutig ihrem Eintrag
  zugeordnet. / At least one embedded observation, keeping ownership explicit
  without a second reference list.
- bedingt `gapId`. / Conditional gap ID.

**InventoryObservation-Felder / InventoryObservation fields:**

- `observationId`.
- `dimension`: kontrollierte Pruefdimension. Agenten benoetigen getrennte
  Beobachtungen fuer Installation, Pin, Versionscheck, State, Dispatcher,
  Provider/Anmeldung und Dokumentationskategorie; Presets fuer ID, Version,
  Prioritaet, Aktivstatus, Aufloesung und CL-Abdeckung. / Controlled review
  dimension. Agents and presets require the separately listed observations.
- `sourceKind`: `TargetClaim`, `Dockerfile`, `ComposeMount`, `StateVolume`,
  `Registry`, `VersionCheck`, `SmokeTest`, `Dispatcher`, `Documentation` oder
  `InstalledPreset`.
- `sourcePath`, `sourceReference`, `observedCategory`, `observedVersionOrValue`.
- `command`, `result`, `checkedAt`, `platform`, `limitations`.

**Kategorieregeln / Category rules:**

- Toolchains: genau 6 MSL-Familien (.NET/C#, Java/JVM, Go, Rust, Python,
  Swift), 2 getrennte Basen (PowerShell 7, Node.js/npm) sowie Syft, `uv` und
  Spec Kit als weitere Werkzeuge. / Exactly six MSL families, two separate
  foundations, and additional tools.
- Agenten: 4 Required-Agenten (Codex, Claude Code, Antigravity CLI, GitHub
  Copilot CLI) und 2 Zusatzoberflaechen (OpenCode, Gemini CLI). Installation,
  Pin, Versionscheck, State, Dispatcher, Provider/Sign-in und Doku-Kategorie
  bleiben getrennt. / Four required and two additional agent surfaces with
  separate observations.
- Presets: genau 12 installierte Presets; 8 im verbindlichen Governance-Profil
  und 4 zusaetzliche Routing-/Intake-Presets. ID, Version, Prioritaet,
  Aktivstatus, effektive Aufloesung und CL-Abdeckung sind Pflicht. / Exactly 12
  installed presets split into binding eight and additional four.
- Jede Abweichung besitzt genau einen Gap. / Every mismatch has exactly one gap.

## AssessmentSummary

**Zweck / Purpose:** Liefert exakte, maschinenlesbare Zaehler fuer Abnahme und
textorientierte Zusammenfassung. / Provides exact machine-readable counts for
acceptance and text-first summary.

**Felder / Fields:**

- `checklistCounts`: genau eine Soll-/Ist-Zeile je `CL-01` bis `CL-12` mit den
  bindenden Sollzahlen `12, 13, 15, 10, 13, 11, 12, 13, 17, 17, 12, 12`. /
  Exactly one expected/actual row per checklist with the stated binding counts.
- `applicabilityCounts`: genau `Applicable`, `N/A`, `Open`;
  `implementationCounts`: genau `Fulfilled`, `Partly Fulfilled`,
  `Not Fulfilled`, `Not Assessed`; `assessmentStatusCounts`: genau
  `Applicable`, `AlreadySatisfied`, `N/A`, `Open`, `FollowUp`. / Each count set
  uses exactly the closed vocabulary listed here.
- `gapPriorityCounts`: genau `P0`, `P1`, `P2`, `P3`; `humanOnlyCounts`: genau
  `HumanOnly` und `NotHumanOnly`. / Gap and human-only counts use exactly these
  closed names.
- `inventoryCounts`: MSL, Basen, Required-Agenten, Zusatzagenten, Presets.
- Fehlerzaehler: `missingIds`, `duplicateIds`, `extraIds`,
  `invalidStatusCombinations`, `missingMandatoryFields`,
  `unsupportedPositiveAssessments`, `unassignedGapRows`,
  `orphanGapMappings`, `unassignedOwners`, `indefiniteTriggers`,
  `scopeViolations`, `missingEnglishPartners`, `unexplainedTerms`,
  `visualOnlyInformation`, `unexplainedCefrDeviations`.

**Validierungsregeln / Validation rules:**

- Jede der zwoelf Checklistensummen stimmt einzeln mit der bindenden Sollzahl
  und den Detailzeilen ueberein; zusammen ergeben sie exakt 157. Fehlerzaehler
  sind fuer `ReviewPending` alle 0. / Every checklist count individually matches
  its binding expected value and detailed rows; together they total 157. All
  error counters are zero for ReviewPending.
- Status-, Gap-, Human-only- und Inventarsummen werden aus den Detailobjekten
  neu berechnet und stimmen exakt ueberein. / Status, gap, human-only, and
  inventory counts are recomputed from detail objects and match exactly.

## ValidationBundle und ValidationRecord

**Zweck / Purpose:** `validation-results.json` bindet die ausgefuehrte
Abnahme unabhaengig von der kanonischen Bewertung. / `validation-results.json`
binds executed acceptance independently from the canonical assessment.

**ValidationBundle-Felder / ValidationBundle fields:**

- `schemaVersion`: `1.0`.
- `assessmentResultsSha256`: aktueller Hash von `assessment-results.json`. /
  Current hash of the canonical assessment.
- `acceptedInputBindings`: genau die drei akzeptierten Eingaben. / Exactly the
  three accepted inputs.
- `outputBindings`: genau die sechs anderen vertraglichen Ausgabepfade mit
  aktuellem SHA-256; `validationResultsPath` erfasst den siebten, eigenen Pfad.
  Dessen Hash wird im Exact-Head-Gate ausserhalb der Datei gebunden. / Exactly
  the six other contractual outputs with current hashes;
  `validationResultsPath` records the self path, whose hash is bound by
  exact-head evidence outside the file.
- `gateResults`: genau eine Zeile je Gate-ID aus
  `autonomous-run-gate-requirements.json`.
- `traceabilitySample`: genau zwoelf Eintraege, je einer fuer `CL-01` bis
  `CL-12`, mit CL-ID, Status-, Evidenz- und bedingter Gap-Aufloesung, Start,
  Ende und Dauer. / Exactly one sample per checklist with resolved status,
  evidence, conditional gap, timestamps, and duration.
- `observedCounts`: beobachtete Assessment- und Fehlerzaehler; daneben
  `traceabilityTotalSeconds`. / Observed assessment and error counts, plus the
  separate traceability total.
- `overallResult`: `Pass`, `Fail` oder `Blocked`.
- `assessmentStateResult`: `Draft` oder `ReviewPending`; Human-only-
  `AcceptedBaseline` wird hier nicht gesetzt. / Draft or ReviewPending only.

**Zweck / Purpose:** Ein tatsaechlich ausgefuehrter Gate-Nachweis in
`validation-results.json`. / An actually executed gate proof.

**Felder / Fields:**

- `gateId`, `applicability`: `Applicable` oder `N/A`, `executedCommand`,
  `runnerOrPlatform`, `startedAt`, `finishedAt`.
- `exitCode`, `result`: `Pass`, `Fail`, `Skipped`, `Blocked`.
- `expectedResult`, `observedResult`, `evidencePath`, `limitations`.
- `inputSha256` und `outputSha256`, soweit anwendbar. / Where applicable.
- `rationale` und `reevaluationTrigger`; bei `N/A` beide konkret, bei
  `Applicable` darf `rationale` den kontrollierten Wert `N/A` tragen. /
  Concrete rationale and trigger for N/A; Applicable may use N/A rationale.

**Validierungsregeln / Validation rules:**

- Nur `Pass` mit Exitcode 0 und passendem beobachtetem Ergebnis erfuellt ein
  anwendbares Gate. / Only matching exit-zero Pass fulfils an applicable gate.
- `Skipped` und `Blocked` bleiben sichtbar und verhindern `ReviewPending`, wenn
  das Gate anwendbar ist. / Skipped and Blocked remain visible and block
  ReviewPending for applicable gates.
- Ein `N/A`-Gate verwendet `Skipped`, Exitcode `N/A`, eine konkrete Begruendung
  und einen konkreten Trigger; es darf kein `Pass` behaupten. / An N/A gate is
  Skipped with N/A exit code, a concrete rationale and trigger; it cannot claim
  Pass.
- `ReviewPending` verlangt alle anwendbaren Gates `Pass`, alle Fehlerzaehler 0,
  aktuelle Output-Bindungen und zwoelf eindeutige Samples mit zusammen
  hoechstens 1.800 Sekunden. / ReviewPending requires passing applicable gates,
  zero error counts, current outputs, and twelve unique samples totalling at
  most 1,800 seconds.

## Beziehungen / Relationships

- Ein `AssessmentSnapshot` besitzt viele `SourceSnapshot`, genau 157
  `GSDBReviewItem`, viele `EvidenceRecord`, `Gap`, `InventoryItem` und genau
  eine `AssessmentSummary`. / One snapshot owns these collections and exactly
  157 rows.
- Jede Row verweist auf genau eine kanonische Quelle und mindestens einen
  Evidenzrecord. / Every row references one canonical source and at least one
  evidence record.
- Evidence ist many-to-many; Gap-Zuordnung ist fuer gap-pflichtige Rows
  many-to-one. / Evidence is many-to-many; required gap mapping is many-to-one.
- Ein InventoryItem besitzt eine oder mehrere Beobachtungen; `Mismatch`,
  `Missing` oder `Open` verweist auf genau einen Gap. / An inventory item owns
  observations and unresolved states map to one gap.
- `validation-results.json` bindet per Hash an
  `assessment-results.json` und alle von ihm verschiedenen vertraglichen
  Ausgaben. Sein eigener Hash wird durch temporaere Exact-Head-Gate-Evidenz
  gebunden, damit keine unmoegliche selbstreferenzielle Hashforderung entsteht.
  / Validation results hash-bind the canonical assessment and every other
  contractual output. Exact-head evidence binds the validation file itself,
  avoiding an impossible self-referential hash.

## Zustandsuebergaenge / State Transitions

```text
AssessmentSnapshot:
Draft -> ReviewPending
ReviewPending -> AcceptedBaseline   [nur Project Owner + Security Review]
Draft|ReviewPending|AcceptedBaseline -> Draft [Input-, Baseline-, Scope- oder Evidenzdrift]

GSDBReviewItem:
unbewertete Row -> Open|Applicable [Implementation bleibt Not Assessed]
Open -> AlreadySatisfied|FollowUp|N/A [nach neuer Evidenz oder Scope-Klaerung]
FollowUp -> AlreadySatisfied [nur in spaeterer Remediation]
AlreadySatisfied|N/A -> Open [Trigger oder Evidenzdrift]

Gap:
Open -> Planned -> EvidenceReady -> HumanReviewPending -> Closed
Jeder Zustandswechsel nach Open liegt ausserhalb dieser reinen Bestandspruefung.
Every transition after Open is outside this assessment-only feature.

Intake series:
Current GSDB intake Eligible/Active -> Completed only after AcceptedBaseline
-> separately authorized intake-series update -> series status validation
-> next-candidate listing. No transition occurs in this assessment run.
```

**Textalternative DE:** Die Bewertung beginnt als `Draft`. Vollstaendige und
validierte Artefakte duerfen `ReviewPending` erreichen. Nur die beiden
menschlichen Rollen duerfen `AcceptedBaseline` bestaetigen. Jede relevante
Aenderung setzt die Bewertung auf `Draft` zurueck. Gaps werden in diesem
Feature nur dokumentiert; ihre Planung oder Schliessung gehoert zu einem
spaeteren, separat autorisierten Intake. Der Serienfortschritt erfolgt erst
nach menschlicher Akzeptanz und einem gesonderten Update-Befehl.

**Text alternative EN:** The assessment starts as Draft. Complete, validated
artefacts may reach ReviewPending. Only the two human roles may confirm
AcceptedBaseline. Relevant drift returns the assessment to Draft. This feature
only records gaps; planning or closing them belongs to a later separately
authorized intake. Series advancement happens only after human acceptance and
a separate update command.
