# Datenmodell: Container-Haertung / Data Model: Container Hardening

## Zweck / Purpose

**DE:** Das Modell beschreibt dateibasierte Evidenz. Es ist keine Laufzeit-API
und speichert keine Geheimnisse, Prompt-/Antworttexte oder Providerdaten.

**EN:** The model describes file-based evidence. It is not a runtime API and
stores no secrets, prompt/response text, or provider data.

## 1. AcceptedInputBinding

- `path`: repository-relativer Pfad, keine Traversierung.
- `sha256`: normalisierter SHA-256 mit 64 Kleinbuchstaben-/Ziffernzeichen.
- `role`: `FeatureIntake`, `IntakeReview`, `SeriesManifest`,
  `AssessmentResults`, `PrioritisedGapList` oder `AcceptanceDecision`.
- Regel: genau sechs, Pfad/Hash exakt aus `spec.md`; Drift blockiert.

## 2. GapDisposition

- `gapId`: exakt `GAP-001` bis `GAP-157`, aufsteigend und eindeutig.
- `affectedClIds`: nicht leere, wechselseitig belegte CL-ID-Liste.
- `priority`: fuer diese Baseline immer `P1`.
- `humanOnly`: unveraenderliches Boolean aus AcceptedBaseline.
- `humanOnlyRole`: `N/A`, `Privacy/Legal Review`, `Platform Owner/Admin`,
  `CISO/ISB/KIB` oder `Project Owner`; muss zur Spec-Liste passen.
- `applicability`: `Applicable`, `N/A` oder `Open`.
- `implementationStatus`: `Fulfilled`, `Partly Fulfilled`, `Not Fulfilled`
  oder `Not Assessed`.
- `consolidatedState`: `N/A`, `Open`, `AlreadySatisfied`, `FollowUp` oder
  `Applicable`.
- `rationaleDe`, `rationaleEn`: sachliche Begruendung, keine Leerwerte.
- `requirementIds`: mindestens eine `FR-*`, `GR-*`, `AR-*`, `CP-*`, `AP-*`
  oder zwingende Gate-ID.
- `evidenceIds`: aktuelle Evidenz oder leere Liste nur bei offenem Punkt mit
  `missingEvidence`.
- `owner`, `reviewer`: kontrollierte Rollen.
- `residualRisk`: `Unassessed`, `None identified`, `Low`, `Medium`, `High`
  oder `Critical`; Agenten setzen nie `Accepted`.
- `missingEvidence`, `followUp`, `reevaluationTrigger`: Pflichttexte; bei
  `N/A` ist `missingEvidence` `N/A`, Trigger bleibt Pflicht.
- `lastEvaluatedAt`: UTC-Zeitpunkt der letzten echten Bewertung.

### Statusinvarianten / Status Invariants

Die erste passende Regel gewinnt: / First matching rule wins:

1. `N/A` = `N/A` + `Not Assessed` + begruendeter Trigger.
2. `Open` = `Open` + `Not Assessed`.
3. `AlreadySatisfied` = `Applicable` + `Fulfilled` + aktuelle Evidenz.
4. `FollowUp` = `Applicable` + (`Partly Fulfilled` oder `Not Fulfilled`).
5. `Applicable` = `Applicable` + `Not Assessed` fuer bewusst noch nicht
   bewerteten Scope.

Human-only bleibt ohne datierten Rollenbeleg immer `Open`, `Not Assessed` und
`Unassessed`. Eine Vorlage oder technische Vorbereitung aendert dies nicht.

## 3. VerificationEvidence

Dokumentebene / Document envelope:

- `sourceRevision`: Git-HEAD oder `WORKTREE`.
- `imageIdentity`: finale lokale Image-ID beziehungsweise Digest; bis vor dem
  finalen Build ist `N/A` zulaessig. Der Wert gilt fuer die gesamte
  Evidenzdatei und wird nicht je Gate ueberschrieben.
- `overallResult`: `Pass`, `Fail` oder `Blocked`.

Je Gate-Eintrag / Per gate record:

- `evidenceId`: eindeutige stabile ID, z. B. `EVD-RUNTIME-001`.
- `gateId`: deklarierte Gate-ID.
- `applicability`: `Applicable` oder `N/A`, exakt wie vorab deklariert.
- `subjectPaths`: gepruefte Repository-Pfade oder lokaler Artefaktbezeichner.
- `command`: exakt ausgefuehrter Befehl; keine Secrets.
- `runnerOrPlatform`: z. B. `macOS-PowerShell7-PodmanMachine`,
  `Linux-Bash-rootless-Podman` oder `Windows-WSL2-PowerShell7-Podman`.
- `startedAt`, `finishedAt`, `exitCode`.
- `expectedResult`, `observedResult`, `result`: `Pass`, `Fail`, `Blocked` oder
  die unten eng begrenzte `N/A`-Form.
- `freshness`: `Current`, `Stale` oder die unten eng begrenzte `N/A`-Form.
- `limitations`: explizite Grenzen; nie still leer bei uebersprungenem Scope.
- `artifactSha256`: Hash des erzeugten Outputs oder `N/A`.
- `containsSensitiveContent`: muss `false` sein.
- `rationale`, `reevaluationTrigger`: Sachgrund und ereignisbezogener
  Ausloeser; bei N/A muessen beide mit der Gate-Deklaration uebereinstimmen.

`Current` ist nur erlaubt, wenn die Evidenz nach der letzten Aenderung ihres
Subjekts erzeugt und an Source-/Image-Identitaet gebunden wurde.

Fuer ein als `N/A` deklariertes Gate wird eine Bewertung, aber kein Lauf
erfasst: `command`, `runnerOrPlatform` und `artifactSha256` sind `N/A`,
`exitCode` ist `null`, `result` und `freshness` sind `N/A`, und Zeitpunkt,
Sachgrund sowie Ereignis-Trigger bleiben Pflicht. Die dokumentweite
`imageIdentity` bleibt die gemeinsame finale Image-Bindung und wird durch eine
N/A-Zeile nicht veraendert. Ein Applicable-Gate darf diese N/A-Form nie
verwenden. / An N/A gate records a decision, not an invented execution;
document-level image identity remains shared, and applicable gates always
require real execution data.

## 4. SandboxBoundary

- `boundaryId`, `kind`: `HostContainer`, `RepositoryAgentState`,
  `ProjectToolchain`, `ContainerPackageSource`, `AgentProvider`,
  `ImageSupplyChain` oder `LearnerMaintenance`.
- `source`, `target`, `assets`, `dataClass`: `public`, `internal`,
  `confidential`, `restricted`.
- `controlObjective`, `controls`, `allowedFlows`, `deniedFlows`.
- `verificationEvidenceIds`, `residualRisk`, `owner`, `reviewer`, `trigger`.

Reale Secretwerte werden nie modelliert; nur die Datenklasse und Grenze.

## 5. MountDisposition

- `mountId`, `hostSourceExpression`, `containerTarget`, `type`.
- `mode`: `read-only` oder `read-write`.
- `purposeDe`, `purposeEn`, `dataClass`, `requiredByWorkflow`.
- `agentAccess`, `allowedWriteProbe`, `deniedWriteProbe`.
- `status`, `evidenceIds`, `limitations`, `trigger`.

Jeder effektive Compose-Mount muss genau einen Eintrag besitzen. Ein Mount darf
nicht aufgrund einer Dokumentationsbehauptung als minimal gelten.

## 6. ToolInventoryEntry

- `toolId`, `category`: sechs `MSLToolchain`, zwei `ScriptFoundation`, vier
  `RequiredAgent`, zwei `AdditionalAgentSurface` oder `SupportingTool`.
- `expectedVersion`, `observedVersion`, `source`, `immutableIdentity`.
- `integrityMethod`, `updateMechanism`, `smokeCommand`, `evidenceIds`.
- `providerApproval`: fuer Agenten immer `NotGrantedByRepository`.
- `limitations`, `trigger`.

Sollwerte aus Dockerfile/Lock-Dateien und Laufzeitbeobachtungen bleiben
getrennte Felder.

## 7. VulnerabilityFinding und VexDecision

`VulnerabilityFinding`:

- `findingId`, `vulnerabilityId`, `componentPurl`, `componentVersion`.
- `scanner`, `scannerVersion`, `databaseUpdatedAt`, `severity`.
- `imageIdentity`, `sbomSha256`, `evidenceId`.

`VexDecision`:

- `findingId` als Referenz.
- `status`: `affected`, `not_affected`, `mitigated` oder
  `under_investigation` (CycloneDX-Ausgabe darf normkonforme Synonyme mappen).
- `rationaleDe`, `rationaleEn`, `action`, `owner`, `reviewer`, `trigger`.
- `humanApprovalRequired`: Boolean; keine agentische Risikoakzeptanz.

Jeder relevante Fund hat genau eine Entscheidung oder bleibt mit offenem
Blocker sichtbar.

## 8. BuildProvenance

- `sourceRevision`, `dirtyState`, `dockerfileSha256`, `composeSha256`.
- `baseImageReference`, `baseImageDigest`, `buildCommand`.
- `runnerOrPlatform`, `startedAt`, `finishedAt`, `exitCode`.
- `localImageName`, `localImageId`, `localRepoDigest` falls vorhanden.
- `sbomPath`, `sbomSha256`, `scannerEvidencePath`.
- `slsaClaim`: `NoPublishedLevel` fuer diesen lokalen Scope.
- `limitations`, `trigger`.

## 9. HumanOnlyHandoff

- `gapId`, `role`, `factsPrepared`, `missingDecision`.
- `repositoryEvidencePaths`, `followUp`, `targetOrEvent`, `trigger`.
- `state`: immer `Open` bis externer datierter Rollenbeleg in Scope kommt.
- `residualRisk`: `Unassessed`.
- `agentBoundary`: verbotene Aktion in Klartext.

## 10. LearnerFirstUseResult

- `reviewId`, `conductedAt`, `owner`: Owner muss `Learning/A11Y Review` sein.
- `participantCount`, `successfulParticipantCount`, `successRatePercent`.
- `audienceCoverage`: alle vier verbindlichen Ausbildungsberufe; fehlende
  Abdeckung bleibt offen.
- `priorSpecKitExperience`: fuer den Abnahmedatensatz `false`.
- `timeLimitMinutes`: `30`; `successRatePercent` muss mindestens `90` sein.
- `observedTasks`: sicherer Startpfad, aktueller Verifikationsstatus und
  naechster offener Human-only-Schritt.
- `methodDe`, `methodEn`, `limitations`, `followUp`, `trigger`.
- `containsSensitiveContent`: `false`; keine Namen, Kontaktdaten, Rohnotizen
  oder Leistungsprofile einzelner Teilnehmender.

Der Agent darf diesen Datensatz strukturell validieren, aber weder
Teilnehmende, Beobachtungen noch ein positives Ergebnis erzeugen. Fehlt die
menschliche Evidenz, bleibt `GATE-LEARNER-01` offen und blockiert einen
positiven Feature-Abschluss. / The agent may validate but never fabricate this
human evidence.

## 11. ValidationSummary

- `gapCount: 157`, `agentActionableCount: 108`, `humanOnlyCount: 49`.
- `missingGapIds`, `duplicateGapIds`, `extraGapIds`.
- Statuszaehler nach beiden Achsen und konsolidiertem Zustand.
- `changedPathMappings`: jeder geaenderte Pfad mit Gap-/Requirement-IDs.
- `gateResults`: alle deklarierten Gates.
- `learnerFirstUseResult`: vorhanden und bestanden oder explizit offen.
- `overallResult`: `Pass`, `Fail` oder `Blocked`.

`Pass` setzt leere Mengen fuer fehlende, doppelte, extra und ungemappte
Elemente voraus. Human-only-Offenheit ist kein Fehler, sondern eine
erwartete, separat gepruefte Grenze.

## Beziehungen / Relationships

```text
AcceptedInputBinding exactly 6 -> GapDisposition exactly 157
GapDisposition * <-> VerificationEvidence *
GapDisposition * -> HumanOnlyHandoff 0..1
SandboxBoundary 1..* -> VerificationEvidence 1..*
MountDisposition 1..* -> SandboxBoundary 1
ToolInventoryEntry 1..* -> VerificationEvidence 1..*
BuildProvenance 1 -> SBOM 1 -> VulnerabilityFinding * -> VexDecision 1
LearnerFirstUseResult 1 -> VerificationEvidence 1..*
ValidationSummary 1 -> all preceding records
```

Die Textdarstellung ergaenzt die Kardinalitaeten; das Diagramm ist nicht die
einzige Informationsquelle. / The prose fully explains the cardinalities; the
diagram is supplementary only.
