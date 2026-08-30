# Quickstart: GSDB-Bestandspruefung pruefen / Validate the GSDB Baseline Assessment

## Zweck und sichere Verwendung / Purpose and Safe Use

**DE:** Dieser Quickstart ist die copy-ready Validierungsanleitung fuer die
spaetere Assessment-Implementierung. Die Befehle lesen Repository-Dateien,
validieren strukturierte Evidenz und erzeugen nur ausdruecklich genannte
temporaere Testdateien. Sie aendern keine Sandbox-Konfiguration, beheben keine
Luecke, akzeptieren kein Restrisiko und starten keinen Folge-Intake.

**EN:** This quickstart is the copy-ready validation guide for later assessment
implementation. Commands read repository files, validate structured evidence,
and create only explicitly named temporary test files. They do not change
sandbox configuration, remediate gaps, accept risk, or start a follow-up
intake.

Ausgangspunkt ist die Repository-Wurzel. PowerShell wird auf diesem macOS-Host
immer ohne Profil gestartet. / Run from the repository root. On this macOS
host, always start PowerShell without profiles.

```bash
uname -s
pwsh -NoLogo -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
git status --short --branch
```

Erwartet / Expected:

- Betriebssystem und PowerShell-Version sind sichtbar. / OS and PowerShell
  version are visible.
- Branch ist `002-gsdb-baseline-assessment`. / Branch matches.
- Alle vorhandenen fremden Aenderungen sind vor der Arbeit bekannt. / Existing
  unrelated changes are understood.

### Begriffe fuer diese Anleitung / Terms Used in This Guide

- **Read-only-Pruefung / Read-only check**: Ein Befehl liest Evidenz, ohne
  Repository-Inhalte zu aendern. Temporaere Fixtures sind kurzlebige
  Testdateien unter dem Betriebssystem-Temp-Verzeichnis. / A command reads
  evidence without changing repository content. Temporary fixtures are
  short-lived test files in the operating-system temporary directory.
- **Gate und Phasenergebnis / Gate and phase result**: Ein Gate ist eine
  Abnahmebedingung. Ein Phasenergebnis ist die kleine JSON-Datei, die Aufgabe,
  Gate-Status und Hash des gelieferten Payloads, also der Ergebnisdatei, bindet.
  / A gate is an acceptance condition. A phase result is the small JSON file
  binding task completion, gate state, and the hash of the delivered payload.
- **Rot-/Gruen-Test und vertikaler Slice / Red/green test and vertical slice**:
  Rot beweist, dass ein fehlerhaftes Minimalbeispiel abgelehnt wird. Gruen
  beweist den gueltigen Vertrag. Der Slice fuehrt einen einzigen CL-Punkt durch
  alle Schichten, bevor alle 157 Rows erstellt werden. / Red proves rejection
  of an invalid minimal example; green proves the valid contract. The slice
  carries one CL item through every layer before all 157 rows are authored.
- **Projektion / Projection**: Eine aus dem kanonischen JSON abgeleitete,
  besser lesbare Markdown-Darstellung. / A more readable Markdown view derived
  from the canonical JSON.
- **Delivery-Set, Staging und Content-Commit**: Das Delivery-Set ist die exakt
  erlaubte Dateimenge. Staging ist die Git-Vormerkliste fuer den naechsten
  Commit; der Content-Commit fasst die autorisierten Inhaltsdateien zusammen. /
  The delivery set is the exact allowed file set. Staging is Git's list for the
  next commit; the content commit groups the authorised content files.
- **Exact Head, PreMerge und PostMerge**: Exact Head ist der konkrete
  Commit-Hash der geprueften Version. PreMerge-Evidenz bindet diesen Stand vor,
  PostMerge-Evidenz den tatsaechlichen Merge danach. / Exact head is the exact
  reviewed commit hash. PreMerge evidence binds it before merge; PostMerge
  evidence binds the actual merge afterwards.
- **Drift und sanitierter Sitzungslog / Drift and sanitized session log**:
  Drift ist eine nachweisbare Abweichung vom erwarteten Stand. Ein sanitierter
  Log enthaelt nur Arbeitsmetadaten und keine Prompts, Antworten oder Secrets. /
  Drift is a measurable difference from the expected state. A sanitized log
  contains work metadata only, never prompts, responses, or secrets.

## 1. Run-State und akzeptierte Eingaben / Run State and Accepted Inputs

```bash
pwsh -NoLogo -NoProfile -File \
  .specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.ps1 \
  -State specs/002-gsdb-baseline-assessment/autonomous-run-state.json
```

```bash
pwsh -NoLogo -NoProfile -Command '
$expected = [ordered]@{
  "Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md" = "9b1963a5cc1e4f074e8fc918455f0285a0e1138334451523bd957ff21e72026a"
  "specs/intake-review-results/sandbox-development-lifecycle.json" = "0d08a1e90e25965c4b529d66be6996394b963abef4ddb3c3b75dd678f464004b"
  "specs/intake-series/sandbox-development-lifecycle/manifest.json" = "faa906c5acb7678265de75e28d80a337459d754ab53066f7a4f065ef24d1b3b2"
}
foreach ($entry in $expected.GetEnumerator()) {
  if (-not (Test-Path -LiteralPath $entry.Key -PathType Leaf)) {
    throw "Missing accepted input: $($entry.Key)"
  }
  $actual = (Get-FileHash -LiteralPath $entry.Key -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($actual -ne $entry.Value) {
    throw "Accepted-input hash mismatch: $($entry.Key): $actual"
  }
  "PASS $($entry.Key) $actual"
}
'
```

Erwartet / Expected: State-Validator meldet `PASS`; alle drei Hashes stimmen.
Jede Abweichung stoppt die Umsetzung und verlangt Resume/Revalidierung. / State
passes and all hashes match. Any mismatch stops delivery.

### Aktuelles Phasenergebnis und historische Verlaufsevidenz / Current Phase Result and Historical Lineage Evidence

Vor dem ersten Implementierungs-Edit wird genau das Ergebnis der letzten
abgeschlossenen gerouteten Phase gegen seinen aktuellen Payload geprueft. Eine
aeltere Phase kann denselben Payload vor einer spaeteren autorisierten
Fortschreibung gebunden haben; ihr altes Ergebnis bleibt Verlaufsevidenz und
wird nicht gegen den neuesten Dateiinhalt neu bewertet. / Before the first
implementation edit, validate exactly the last completed routed phase result
against its current payload. Older results remain lineage evidence and are not
re-evaluated against content changed by later authorised phases.

```bash
pwsh -NoLogo -NoProfile -Command '
$state = Get-Content -LiteralPath specs/002-gsdb-baseline-assessment/autonomous-run-state.json -Raw -Encoding UTF8 | ConvertFrom-Json
$completed = @($state.routing.phases | Where-Object status -eq "Completed")
if ($completed.Count -eq 0) { throw "No completed routed phase" }
$phase = $completed[-1]
if ($phase.resultPath -eq "N/A") { throw "Last completed phase has no result path" }
& .specify/presets/autonomous-run-governance/scripts/validate-autonomous-phase-result.ps1 `
  -Repo . -Result $phase.resultPath -PhaseId $phase.phaseId -ExitCode 0
if ($LASTEXITCODE -ne 0) { throw "Current phase-result validation failed" }
'
```

```bash
phase_id="$(jq -r '[.routing.phases[] | select(.status == "Completed")][-1].phaseId' \
  specs/002-gsdb-baseline-assessment/autonomous-run-state.json)"
result_path="$(jq -r '[.routing.phases[] | select(.status == "Completed")][-1].resultPath' \
  specs/002-gsdb-baseline-assessment/autonomous-run-state.json)"
if [ -z "$phase_id" ] || [ "$phase_id" = "null" ] ||
   [ -z "$result_path" ] || [ "$result_path" = "N/A" ] || [ "$result_path" = "null" ]; then
  printf '%s\n' 'Last completed routed phase is incomplete' >&2
  exit 1
fi
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-phase-result.sh \
  --repo . --result "$result_path" --phase-id "$phase_id" --exit-code 0
```

Erwartet / Expected: Beide vorhandenen Validatorvarianten bestehen fuer dasselbe
letzte abgeschlossene Ergebnis. Ein
`AEI107`-Hashfehler dort oder eine materielle Abweichung zwischen aktuellem
`autonomous-run-state.json` und `autonomous-run-evidence.md` ist ein
fail-closed Revalidierungsblocker. Aeltere Resultate duerfen im State als
historische Phasenbelege verbleiben. Die grossen
`.specify/runtime/**/*.log.txt`-Dateien duerfen niemals in den Delivery-Set
aufgenommen werden. / The last completed result passes. Current hash or
state/evidence drift blocks delivery; older results may remain as historical
phase evidence. Both existing validator variants pass for the same last
completed result. Runtime prompt/response logs never enter the delivery set.

## 2. Gate-Anforderungen strukturell pruefen / Check Gate Requirements Structurally

```bash
pwsh -NoLogo -NoProfile -Command '
$path = "specs/002-gsdb-baseline-assessment/autonomous-run-gate-requirements.json"
$data = Get-Content -LiteralPath $path -Raw -Encoding UTF8 | ConvertFrom-Json
if ($data.schemaVersion -ne "1.0") { throw "Wrong requirements schema" }
if (@($data.gates).Count -eq 0) { throw "No gates declared" }
$ids = @($data.gates.gateId)
if (@($ids | Sort-Object -Unique).Count -ne $ids.Count) { throw "Duplicate gate ID" }
foreach ($gate in $data.gates) {
  if ($gate.applicability -notin @("Applicable", "N/A")) {
    throw "Invalid applicability: $($gate.gateId)"
  }
  if ($gate.applicability -eq "N/A" -and
      ([string]::IsNullOrWhiteSpace($gate.rationale) -or
       [string]::IsNullOrWhiteSpace($gate.reevaluationTrigger))) {
    throw "Incomplete N/A gate: $($gate.gateId)"
  }
}
"PASS: $($ids.Count) declared gates"
'
```

Erwartet / Expected: `PASS` mit eindeutigen Gates und vollstaendigen
`N/A`-Dispositionen. / PASS with unique gates and complete N/A dispositions.

## 3. Rot-/Gruen-Vertragstest / Red/Green Contract Test

**DE:** Der rote Test beweist, dass eine unvollstaendige Bewertung wirklich
abgelehnt wird. Er schreibt nur nach `/tmp`. Ein unerwarteter Pass ist ein
Fehler. / The red test proves that an incomplete assessment is rejected. It
writes only to `/tmp`; an unexpected pass is a failure.

```bash
pwsh -NoLogo -NoProfile -Command '
$fixture = Join-Path ([IO.Path]::GetTempPath()) "gsdb-invalid-assessment.json"
"{}" | Set-Content -LiteralPath $fixture -Encoding utf8NoBOM
$valid = Get-Content -LiteralPath $fixture -Raw -Encoding UTF8 |
  Test-Json -SchemaFile specs/002-gsdb-baseline-assessment/contracts/assessment-results.schema.json -ErrorAction SilentlyContinue
if ($valid) { throw "RED TEST FAILED: invalid fixture was accepted" }
"PASS: expected schema rejection"
Remove-Item -LiteralPath $fixture -Force
'
```

Der gruene Test wird nach dem vertikalen Slice und erneut nach allen 157 Rows
mit dem realen Artefakt ausgefuehrt: / Run the green test after the vertical
slice and again after all 157 rows:

```bash
pwsh -NoLogo -NoProfile -Command '
$json = "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json"
$schema = "specs/002-gsdb-baseline-assessment/contracts/assessment-results.schema.json"
if (-not (Get-Content -LiteralPath $json -Raw -Encoding UTF8 | Test-Json -SchemaFile $schema)) {
  throw "Assessment JSON does not satisfy the schema"
}
"PASS: assessment JSON schema"
'
```

Beim Slice darf eine temporaere, separate Fixture mit genau einer Row genutzt
werden; das Produktionsschema verlangt absichtlich 157 Rows und wird erst beim
vollstaendigen Artefakt gruen. Der Slice muss seine eigenen Feld-, Status-,
Evidenz- und Gap-Pruefungen bestehen. / A separate one-row fixture may be used
for the slice; the production schema intentionally passes only with 157 rows.

## 4. GSDB-Quellen und 157 IDs pruefen / Validate GSDB Sources and 157 IDs

```bash
pwsh -NoLogo -NoProfile -Command '
$root = "docs/secure-development"
$manifest = Get-Content -Raw -Encoding UTF8 "$root/baseline-manifest.json" | ConvertFrom-Json
$manifestPaths = @(
  "$root/baseline-manifest.json"
  (Join-Path $root $manifest.guideline.path)
  (Join-Path $root $manifest.compendium.path)
  @($manifest.checklists | ForEach-Object { Join-Path $root $_.path })
  @($manifest.relatedDocuments | ForEach-Object { Join-Path $root $_.path })
  @($manifest.learningDocuments | ForEach-Object { Join-Path $root $_.path })
  @($manifest.managedBinaryFiles | ForEach-Object { Join-Path $root $_ })
  @($manifest.managedReferenceFiles | ForEach-Object { Join-Path $root $_ })
)
$manifestPaths = @($manifestPaths | ForEach-Object { $_.ToString().Replace("\\", "/") })
$missingManifestFiles = @($manifestPaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
$expectedChecklistCounts = [ordered]@{
  "CL-01" = 12; "CL-02" = 13; "CL-03" = 15; "CL-04" = 10
  "CL-05" = 13; "CL-06" = 11; "CL-07" = 12; "CL-08" = 13
  "CL-09" = 17; "CL-10" = 17; "CL-11" = 12; "CL-12" = 12
}
$checklistCounts = [ordered]@{}
$sourceIds = foreach ($entry in $manifest.checklists) {
  $path = Join-Path $root $entry.path
  if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Missing checklist: $path" }
  $ids = [regex]::Matches(
    (Get-Content -LiteralPath $path -Raw -Encoding UTF8),
    "(?m)^#### (CL-[0-9]{2}-[0-9]{2}):"
  ) | ForEach-Object { $_.Groups[1].Value }
  [void]($checklistCounts[$entry.id] = @($ids).Count)
  $ids
}
$checklistCountMismatches = @($expectedChecklistCounts.Keys | Where-Object {
  -not $checklistCounts.Contains($_) -or
  [int]$checklistCounts[$_] -ne [int]$expectedChecklistCounts[$_]
})
$compendiumPath = Join-Path $root $manifest.compendium.path
$compendiumIds = [regex]::Matches(
  (Get-Content -LiteralPath $compendiumPath -Raw -Encoding UTF8),
  "(?m)^#### (CL-[0-9]{2}-[0-9]{2}):"
) | ForEach-Object { $_.Groups[1].Value }
$sourceUnique = @($sourceIds | Sort-Object -Unique)
$compendiumUnique = @($compendiumIds | Sort-Object -Unique)
$result = [ordered]@{
  expected = $manifest.checklistItemCount
  manifestControlledPaths = $manifestPaths.Count
  missingManifestFiles = $missingManifestFiles
  checklistFiles = @($manifest.checklists).Count
  checklistCounts = $checklistCounts
  checklistCountMismatches = $checklistCountMismatches
  sourceCount = @($sourceIds).Count
  sourceUnique = $sourceUnique.Count
  sourceDuplicates = @($sourceIds | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
  compendiumCount = @($compendiumIds).Count
  compendiumUnique = $compendiumUnique.Count
  missingInCompendium = @($sourceUnique | Where-Object { $_ -notin $compendiumUnique })
  extraInCompendium = @($compendiumUnique | Where-Object { $_ -notin $sourceUnique })
}
$result | ConvertTo-Json -Depth 4
if ($result.expected -ne 157 -or $result.manifestControlledPaths -ne 37 -or
    $result.missingManifestFiles.Count -ne 0 -or $result.checklistFiles -ne 12 -or
    $result.checklistCountMismatches.Count -ne 0 -or
    $result.sourceCount -ne 157 -or $result.sourceUnique -ne 157 -or
    $result.sourceDuplicates.Count -ne 0 -or
    $result.missingInCompendium.Count -ne 0 -or
    $result.extraInCompendium.Count -ne 0) {
  throw "GSDB ID integrity failed"
}
'
```

Erwartet / Expected: 37 manifestierte Pfade, 12 Checklisten mit den Einzelzahlen
`12/13/15/10/13/11/12/13/17/17/12/12`, 157 Source-IDs, 157 eindeutige IDs,
keine Duplikate und Sammelband-ID-Paritaet. Versions- oder Generator-Drift
bleibt trotzdem ein eigener `Open`-/Gap-Befund. Der im README
genannte Befehl `scripts/build-secure-development-docs.* --check` darf nicht
als bestanden gemeldet werden, solange die Skripte fehlen. / All 37
manifest-controlled paths exist, all 157 IDs are unique, and compendium parity
passes; version or generator drift remains a separate open gap.

## 5. Semantik, Coverage und Gap-Zuordnung pruefen / Validate Semantics, Coverage, and Gap Mapping

```bash
pwsh -NoLogo -NoProfile -Command '
$assessmentPath = "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json"
$assessment = Get-Content -LiteralPath $assessmentPath -Raw -Encoding UTF8 | ConvertFrom-Json
$manifest = Get-Content -LiteralPath docs/secure-development/baseline-manifest.json -Raw -Encoding UTF8 | ConvertFrom-Json
$expectedIds = foreach ($entry in $manifest.checklists) {
  [regex]::Matches(
    (Get-Content -LiteralPath (Join-Path "docs/secure-development" $entry.path) -Raw -Encoding UTF8),
    "(?m)^#### (CL-[0-9]{2}-[0-9]{2}):"
  ) | ForEach-Object { $_.Groups[1].Value }
}
$rows = @($assessment.matrixRows)
$rowIds = @($rows.clId)
$uniqueRows = @($rowIds | Sort-Object -Unique)
$missing = @($expectedIds | Where-Object { $_ -notin $uniqueRows })
$extra = @($uniqueRows | Where-Object { $_ -notin $expectedIds })
$duplicates = @($rowIds | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
$gapsById = @{}
foreach ($gap in $assessment.gaps) { $gapsById[$gap.gapId] = $gap }
$evidenceById = @{}
foreach ($evidence in $assessment.evidence) { $evidenceById[$evidence.evidenceId] = $evidence }
$sourcesById = @{}
foreach ($source in $assessment.sources) { $sourcesById[$source.sourceId] = $source }
$inventoryItems = @(
  $assessment.inventory.toolchains
  $assessment.inventory.agents
  $assessment.inventory.presets
  $assessment.inventory.additionalTools
)
$manifestPaths = @(
  "docs/secure-development/baseline-manifest.json"
  (Join-Path "docs/secure-development" $manifest.guideline.path)
  (Join-Path "docs/secure-development" $manifest.compendium.path)
  @($manifest.checklists | ForEach-Object { Join-Path "docs/secure-development" $_.path })
  @($manifest.relatedDocuments | ForEach-Object { Join-Path "docs/secure-development" $_.path })
  @($manifest.learningDocuments | ForEach-Object { Join-Path "docs/secure-development" $_.path })
  @($manifest.managedBinaryFiles | ForEach-Object { Join-Path "docs/secure-development" $_ })
  @($manifest.managedReferenceFiles | ForEach-Object { Join-Path "docs/secure-development" $_ })
) | ForEach-Object { $_.ToString().Replace("\\", "/") }
$invalidStatus = [Collections.Generic.List[string]]::new()
$unassignedGap = [Collections.Generic.List[string]]::new()
$orphanGap = [Collections.Generic.List[string]]::new()
$unsupportedPositive = [Collections.Generic.List[string]]::new()
$invalidOwner = [Collections.Generic.List[string]]::new()
$unresolvedReference = [Collections.Generic.List[string]]::new()
$indefiniteTrigger = [Collections.Generic.List[string]]::new()
$allowedRoles = @(
  "Repository Maintainer", "Project Owner", "Security Review",
  "Platform Owner/Admin", "Privacy/Legal Review", "CISO/ISB/KIB",
  "Learning/A11Y Review"
)
foreach ($row in $rows) {
  $valid = switch ($row.assessmentStatus) {
    "N/A" { $row.applicability -eq "N/A" -and $row.implementationStatus -eq "Not Assessed" -and $row.gapId -eq "N/A" }
    "Open" { $row.applicability -in @("Open", "Applicable") -and $row.implementationStatus -eq "Not Assessed" -and $row.gapId -match "^GAP-" }
    "AlreadySatisfied" { $row.applicability -eq "Applicable" -and $row.implementationStatus -eq "Fulfilled" -and $row.gapId -eq "N/A" }
    "FollowUp" { $row.applicability -eq "Applicable" -and $row.implementationStatus -in @("Partly Fulfilled", "Not Fulfilled") -and $row.gapId -match "^GAP-" }
    "Applicable" { $row.applicability -eq "Applicable" -and $row.implementationStatus -eq "Not Assessed" -and $row.gapId -match "^GAP-" }
    default { $false }
  }
  if (-not $valid) { $invalidStatus.Add($row.clId) }
  if ($row.responsibleRole -notin $allowedRoles -or $row.reviewerRole -notin $allowedRoles) {
    $invalidOwner.Add($row.clId)
  }
  if ($row.followUpOwner -ne "N/A" -and $row.followUpOwner -notin $allowedRoles) {
    $invalidOwner.Add($row.clId)
  }
  if (-not $sourcesById.ContainsKey($row.sourceSnapshotId)) {
    $unresolvedReference.Add("$($row.clId):source:$($row.sourceSnapshotId)")
  } else {
    $source = $sourcesById[$row.sourceSnapshotId]
    if ($source.sourceRole -ne "Checklist" -or $source.path -ne $row.sourcePath -or
        $source.observedVersion -ne $row.sourceVersion -or
        $row.clId -notin @($source.observedItemIds)) {
      $unresolvedReference.Add("$($row.clId):source-content:$($row.sourceSnapshotId)")
    }
  }
  foreach ($evidenceId in $row.evidenceIds) {
    if (-not $evidenceById.ContainsKey($evidenceId)) {
      $unresolvedReference.Add("$($row.clId):evidence:$evidenceId")
    }
  }
  if ($row.reevaluationTrigger -match "(?i)^(N/A|TODO|TBD|bei Bedarf|as needed)$") {
    $indefiniteTrigger.Add($row.clId)
  }
  if ($row.gapId -ne "N/A") {
    if (-not $gapsById.ContainsKey($row.gapId)) {
      $unassignedGap.Add($row.clId)
    } elseif ($row.clId -notin @($gapsById[$row.gapId].affectedClIds)) {
      $orphanGap.Add($row.clId)
    }
  }
  if ($row.assessmentStatus -eq "AlreadySatisfied") {
    $passing = @($row.evidenceIds | Where-Object {
      $evidenceById.ContainsKey($_) -and
      $evidenceById[$_].result -eq "Pass" -and
      $evidenceById[$_].kind -in @("RepositoryPath", "ReadOnlyCheck") -and
      $evidenceById[$_].freshness -eq "Current" -and
      $evidenceById[$_].path -ne "N/A" -and
      (Test-Path -LiteralPath $evidenceById[$_].path)
    })
    if ($passing.Count -eq 0) { $unsupportedPositive.Add($row.clId) }
  }
  if ($row.humanOnly -and $row.assessmentStatus -ne "Open") {
    $invalidStatus.Add($row.clId)
  }
}
$duplicateObjectIds = @(
  @($assessment.sources.sourceId | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
  @($assessment.evidence.evidenceId | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
  @($assessment.gaps.gapId | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
  @($inventoryItems.inventoryId | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
  @($inventoryItems.observations.observationId | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
)
$missingManifestSources = @($manifestPaths | Where-Object { $_ -notin @($assessment.sources.path) })
$extraManifestSources = @($assessment.sources.path | Where-Object { $_ -notin $manifestPaths })
$duplicateSourcePaths = @($assessment.sources.path | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
$invalidSourceIntegrity = [Collections.Generic.List[string]]::new()
foreach ($source in $assessment.sources) {
  if ($source.observedItemCount -ne @($source.observedItemIds).Count) {
    $invalidSourceIntegrity.Add("$($source.sourceId):item-count")
  }
  if (Test-Path -LiteralPath $source.path -PathType Leaf) {
    $actualSourceHash = (Get-FileHash -LiteralPath $source.path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($source.sha256 -ne $actualSourceHash) {
      $invalidSourceIntegrity.Add("$($source.sourceId):hash")
    }
  } elseif ($source.currencyStatus -ne "Missing" -or $source.sha256 -ne "N/A") {
    $invalidSourceIntegrity.Add("$($source.sourceId):missing-path")
  }
}
$invalidSourceGap = @($assessment.sources | Where-Object {
  ($_.currencyStatus -eq "Aligned" -and $_.gapId -ne "N/A") -or
  ($_.currencyStatus -ne "Aligned" -and
    ($_.gapId -eq "N/A" -or -not $gapsById.ContainsKey($_.gapId) -or
     $gapsById[$_.gapId].state -ne "Open" -or
     $gapsById[$_.gapId].evidenceState -notmatch ([regex]::Escape($_.path))))
} | ForEach-Object sourceId)
foreach ($gap in $assessment.gaps) {
  foreach ($clId in $gap.affectedClIds) {
    $row = @($rows | Where-Object clId -eq $clId)
    if ($row.Count -ne 1 -or $row[0].gapId -ne $gap.gapId) {
      $orphanGap.Add("$($gap.gapId):$clId")
    }
  }
}
$allGapReferences = @(
  @($rows.gapId | Where-Object { $_ -ne "N/A" })
  @($assessment.sources.gapId | Where-Object { $_ -ne "N/A" })
  @($inventoryItems.gapId | Where-Object { $_ -ne "N/A" })
)
$unreferencedGaps = @($assessment.gaps.gapId | Where-Object { $_ -notin $allGapReferences })
$summaryCounterDrift = [Collections.Generic.List[string]]::new()
$expectedChecklistCounts = [ordered]@{
  "CL-01" = 12; "CL-02" = 13; "CL-03" = 15; "CL-04" = 10
  "CL-05" = 13; "CL-06" = 11; "CL-07" = 12; "CL-08" = 13
  "CL-09" = 17; "CL-10" = 17; "CL-11" = 12; "CL-12" = 12
}
$reportedChecklistCounts = @($assessment.summary.checklistCounts)
if ($reportedChecklistCounts.Count -ne 12 -or
    @($reportedChecklistCounts.checklistId | Sort-Object -Unique).Count -ne 12) {
  $summaryCounterDrift.Add("checklistCounts:set")
}
foreach ($checklistId in $expectedChecklistCounts.Keys) {
  $reportedCount = @($reportedChecklistCounts | Where-Object checklistId -eq $checklistId)
  $actualCount = @($rows | Where-Object { $_.clId.StartsWith("$checklistId-") }).Count
  if ($reportedCount.Count -ne 1 -or
      [int]$reportedCount[0].expected -ne [int]$expectedChecklistCounts[$checklistId] -or
      [int]$reportedCount[0].actual -ne $actualCount -or
      $actualCount -ne [int]$expectedChecklistCounts[$checklistId]) {
    $summaryCounterDrift.Add("checklistCounts:$checklistId")
  }
}
function Compare-NamedCountSet {
  param($Label, $Reported, [System.Collections.IDictionary]$Expected, $Drift)
  $items = @($Reported)
  if ($items.Count -ne $Expected.Count -or
      @($items.name | Sort-Object -Unique).Count -ne $Expected.Count) {
    $Drift.Add("$Label:set")
  }
  foreach ($name in $Expected.Keys) {
    $match = @($items | Where-Object name -eq $name)
    if ($match.Count -ne 1 -or [int]$match[0].count -ne [int]$Expected[$name]) {
      $Drift.Add("${Label}:$name")
    }
  }
}
$applicabilityCounts = [ordered]@{}
foreach ($name in @("Applicable", "N/A", "Open")) {
  $applicabilityCounts[$name] = @($rows | Where-Object applicability -eq $name).Count
}
$implementationCounts = [ordered]@{}
foreach ($name in @("Fulfilled", "Partly Fulfilled", "Not Fulfilled", "Not Assessed")) {
  $implementationCounts[$name] = @($rows | Where-Object implementationStatus -eq $name).Count
}
$assessmentStatusCounts = [ordered]@{}
foreach ($name in @("Applicable", "AlreadySatisfied", "N/A", "Open", "FollowUp")) {
  $assessmentStatusCounts[$name] = @($rows | Where-Object assessmentStatus -eq $name).Count
}
$gapPriorityCounts = [ordered]@{}
foreach ($name in @("P0", "P1", "P2", "P3")) {
  $gapPriorityCounts[$name] = @($assessment.gaps | Where-Object priority -eq $name).Count
}
$humanOnlyCounts = [ordered]@{
  HumanOnly = @($rows | Where-Object humanOnly -eq $true).Count
  NotHumanOnly = @($rows | Where-Object humanOnly -eq $false).Count
}
Compare-NamedCountSet "applicabilityCounts" $assessment.summary.applicabilityCounts $applicabilityCounts $summaryCounterDrift
Compare-NamedCountSet "implementationCounts" $assessment.summary.implementationCounts $implementationCounts $summaryCounterDrift
Compare-NamedCountSet "assessmentStatusCounts" $assessment.summary.assessmentStatusCounts $assessmentStatusCounts $summaryCounterDrift
Compare-NamedCountSet "gapPriorityCounts" $assessment.summary.gapPriorityCounts $gapPriorityCounts $summaryCounterDrift
Compare-NamedCountSet "humanOnlyCounts" $assessment.summary.humanOnlyCounts $humanOnlyCounts $summaryCounterDrift
$actualInventoryCounts = [ordered]@{
  mslFamilies = @($assessment.inventory.toolchains | Where-Object category -eq "MSLToolchain").Count
  separateFoundations = @($assessment.inventory.toolchains | Where-Object category -eq "ScriptingFoundation").Count
  requiredAgents = @($assessment.inventory.agents | Where-Object category -eq "RequiredAgent").Count
  additionalAgentSurfaces = @($assessment.inventory.agents | Where-Object category -eq "AdditionalAgentSurface").Count
  installedPresets = @($assessment.inventory.presets).Count
}
foreach ($name in $actualInventoryCounts.Keys) {
  if ([int]$assessment.summary.inventoryCounts.$name -ne [int]$actualInventoryCounts[$name]) {
    $summaryCounterDrift.Add("inventoryCounts:$name")
  }
}
$summary = [ordered]@{
  expected = 157
  rows = $rows.Count
  uniqueIds = $uniqueRows.Count
  missingIds = $missing
  extraIds = $extra
  duplicateIds = $duplicates
  invalidStatusCombinations = @($invalidStatus | Sort-Object -Unique)
  unassignedGapRows = @($unassignedGap)
  orphanGapMappings = @($orphanGap)
  unsupportedPositiveAssessments = @($unsupportedPositive)
  invalidOwners = @($invalidOwner)
  unresolvedReferences = @($unresolvedReference)
  indefiniteTriggers = @($indefiniteTrigger)
  duplicateObjectIds = @($duplicateObjectIds)
  missingManifestSources = @($missingManifestSources)
  extraManifestSources = @($extraManifestSources)
  duplicateSourcePaths = @($duplicateSourcePaths)
  invalidSourceIntegrity = @($invalidSourceIntegrity)
  invalidSourceGapMappings = @($invalidSourceGap)
  unreferencedGaps = @($unreferencedGaps)
  summaryCounterDrift = @($summaryCounterDrift)
}
$reported = $assessment.summary.errorCounts
$computedCounters = [ordered]@{
  missingIds = $summary.missingIds.Count
  duplicateIds = $summary.duplicateIds.Count
  extraIds = $summary.extraIds.Count
  invalidStatusCombinations = $summary.invalidStatusCombinations.Count
  unsupportedPositiveAssessments = $summary.unsupportedPositiveAssessments.Count
  unassignedGapRows = $summary.unassignedGapRows.Count
  orphanGapMappings = $summary.orphanGapMappings.Count + $summary.unreferencedGaps.Count
  unassignedOwners = $summary.invalidOwners.Count
  indefiniteTriggers = $summary.indefiniteTriggers.Count
}
foreach ($counter in $computedCounters.GetEnumerator()) {
  if ([int] $reported.($counter.Key) -ne [int] $counter.Value) {
    throw "Reported counter drift $($counter.Key): $($reported.($counter.Key))/$($counter.Value)"
  }
}
$manualZeroCounters = @(
  "missingMandatoryFields", "scopeViolations", "missingEnglishPartners",
  "unexplainedTerms", "visualOnlyInformation", "unexplainedCefrDeviations"
)
foreach ($name in $manualZeroCounters) {
  if ([int] $reported.$name -ne 0) { throw "Manual acceptance counter is not zero: $name" }
}
$summary | ConvertTo-Json -Depth 6
if ($summary.rows -ne 157 -or $summary.uniqueIds -ne 157 -or
    $summary.missingIds.Count -ne 0 -or $summary.extraIds.Count -ne 0 -or
    $summary.duplicateIds.Count -ne 0 -or
    $summary.invalidStatusCombinations.Count -ne 0 -or
    $summary.unassignedGapRows.Count -ne 0 -or
    $summary.orphanGapMappings.Count -ne 0 -or
    $summary.unsupportedPositiveAssessments.Count -ne 0 -or
    $summary.invalidOwners.Count -ne 0 -or
    $summary.unresolvedReferences.Count -ne 0 -or
    $summary.indefiniteTriggers.Count -ne 0 -or
    $summary.duplicateObjectIds.Count -ne 0 -or
    $summary.missingManifestSources.Count -ne 0 -or
    $summary.extraManifestSources.Count -ne 0 -or
    $summary.duplicateSourcePaths.Count -ne 0 -or
    $summary.invalidSourceIntegrity.Count -ne 0 -or
    $summary.invalidSourceGapMappings.Count -ne 0 -or
    $summary.unreferencedGaps.Count -ne 0 -or
    $summary.summaryCounterDrift.Count -ne 0) {
  throw "Assessment semantic validation failed"
}
'
```

Erwartet / Expected: 157 Rows und alle Fehlerlisten leer. Die Umsetzung MUSS
die tatsaechlichen Zaehler auch nach `validation-results.json` schreiben. /
Exactly 157 rows and empty error lists; record observed counts in validation
results.

### Ausgefuehrte Gates und 30-Minuten-Stichprobe / Executed Gates and 30-Minute Sample

**DE:** Die Stichprobe waehlt genau eine Row jeder Checkliste. Eine pruefende
Person verfolgt CL-ID, Status, Begruendung, Evidenz und den bedingten Gap ohne
muendliche Zusatzinformation. Die zwoelf gemessenen Dauern duerfen zusammen
1.800 Sekunden nicht ueberschreiten. / **EN:** Select exactly one row from each
checklist. A reviewer traces ID, status, rationale, evidence, and the conditional
gap without oral help; all twelve durations total no more than 1,800 seconds.

```bash
pwsh -NoLogo -NoProfile -Command '
$base = "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment"
$validationPath = "$base/validation-results.json"
$schemaPath = "specs/002-gsdb-baseline-assessment/contracts/validation-results.schema.json"
if (-not (Get-Content -LiteralPath $validationPath -Raw -Encoding UTF8 | Test-Json -SchemaFile $schemaPath)) {
  throw "Validation results do not satisfy the schema"
}
$validation = Get-Content -LiteralPath $validationPath -Raw -Encoding UTF8 | ConvertFrom-Json
$assessment = Get-Content -LiteralPath "$base/assessment-results.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$requirements = Get-Content -LiteralPath specs/002-gsdb-baseline-assessment/autonomous-run-gate-requirements.json -Raw -Encoding UTF8 | ConvertFrom-Json
$acceptedInputs = @($assessment.assessment.acceptedInputBindings)
$validationInputs = @($validation.acceptedInputBindings)
$expectedInputPaths = @(
  "Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md",
  "specs/intake-review-results/sandbox-development-lifecycle.json",
  "specs/intake-series/sandbox-development-lifecycle/manifest.json"
)
if ($acceptedInputs.Count -ne 3 -or $validationInputs.Count -ne 3 -or
    @($acceptedInputs.path | Sort-Object -Unique).Count -ne 3 -or
    @($validationInputs.path | Sort-Object -Unique).Count -ne 3 -or
    @($expectedInputPaths | Where-Object { $_ -notin @($acceptedInputs.path) }).Count -ne 0) {
  throw "Expected exactly three accepted input bindings"
}
foreach ($input in $acceptedInputs) {
  $binding = @($validationInputs | Where-Object path -eq $input.path)
  if ($binding.Count -ne 1 -or $binding[0].sha256 -ne $input.sha256 -or
      -not (Test-Path -LiteralPath $input.path -PathType Leaf)) {
    throw "Accepted input binding mismatch: $($input.path)"
  }
  $actualHash = (Get-FileHash -LiteralPath $input.path -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($input.sha256 -ne $actualHash) { throw "Accepted input hash drift: $($input.path)" }
}
$requiredGateIds = @($requirements.gates.gateId)
$actualGateIds = @($validation.gateResults.gateId)
if (@($actualGateIds | Sort-Object -Unique).Count -ne $requiredGateIds.Count -or
    @($requiredGateIds | Where-Object { $_ -notin $actualGateIds }).Count -ne 0 -or
    @($actualGateIds | Where-Object { $_ -notin $requiredGateIds }).Count -ne 0) {
  throw "Gate-result set does not match requirements"
}
foreach ($gate in $validation.gateResults) {
  if ($gate.applicability -eq "Applicable" -and
      ($gate.result -ne "Pass" -or $gate.exitCode -ne 0)) {
    throw "Applicable gate did not pass: $($gate.gateId)"
  }
  if ($gate.applicability -eq "N/A" -and
      ($gate.result -ne "Skipped" -or $gate.exitCode -ne "N/A" -or
       $gate.rationale -eq "N/A" -or $gate.reevaluationTrigger -eq "N/A")) {
    throw "Invalid N/A gate result: $($gate.gateId)"
  }
}
$expectedOutputs = @(
  "$base/README.md",
  "$base/assessment-results.json",
  "$base/evidence-matrix.md",
  "$base/prioritized-gap-list.md",
  "$base/inventory-reconciliation.md",
  "$base/documentation-impact.json"
)
$assessmentOutputPaths = @($assessment.assessment.outputPaths)
if ($assessmentOutputPaths.Count -ne 6 -or
    @($expectedOutputs | Where-Object { $_ -notin $assessmentOutputPaths }).Count -ne 0) {
  throw "Assessment output-path set does not match the six contractual outputs"
}
foreach ($path in $expectedOutputs) {
  $binding = @($validation.outputBindings | Where-Object path -eq $path)
  if ($binding.Count -ne 1 -or -not (Test-Path -LiteralPath $path -PathType Leaf)) {
    throw "Missing unique output binding: $path"
  }
  $actualHash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($binding[0].sha256 -ne $actualHash) { throw "Output hash drift: $path" }
}
if ($validation.assessmentResultsSha256 -ne
    (Get-FileHash -LiteralPath "$base/assessment-results.json" -Algorithm SHA256).Hash.ToLowerInvariant()) {
  throw "Assessment hash drift in validation results"
}
$inventoryItems = @(
  $assessment.inventory.toolchains
  $assessment.inventory.agents
  $assessment.inventory.presets
  $assessment.inventory.additionalTools
)
$observed = $validation.observedCounts
if ($observed.checklists -ne 12 -or $observed.matrixRows -ne @($assessment.matrixRows).Count -or
    $observed.uniqueClIds -ne @($assessment.matrixRows.clId | Sort-Object -Unique).Count -or
    $observed.gaps -ne @($assessment.gaps).Count -or
    $observed.inventoryItems -ne $inventoryItems.Count) {
  throw "Observed validation counts do not match assessment content"
}
foreach ($property in $assessment.summary.errorCounts.PSObject.Properties) {
  if ([int] $observed.errorCounts.($property.Name) -ne [int] $property.Value) {
    throw "Validation error-count drift: $($property.Name)"
  }
}
$samples = @($validation.traceabilitySample)
$sampleChecklistIds = @($samples.checklistId)
$expectedChecklistIds = 1..12 | ForEach-Object { "CL-{0:D2}" -f $_ }
if ($samples.Count -ne 12 -or
    @($sampleChecklistIds | Sort-Object -Unique).Count -ne 12 -or
    @($expectedChecklistIds | Where-Object { $_ -notin $sampleChecklistIds }).Count -ne 0) {
  throw "Traceability sample must contain one row per checklist"
}
foreach ($sample in $samples) {
  $row = @($assessment.matrixRows | Where-Object clId -eq $sample.clId)
  if ($row.Count -ne 1 -or -not $sample.clId.StartsWith("$($sample.checklistId)-") -or
      $sample.assessmentStatus -ne $row[0].assessmentStatus -or
      $sample.gapId -ne $row[0].gapId -or
      @($sample.evidenceIds | Where-Object { $_ -notin @($row[0].evidenceIds) }).Count -ne 0) {
    throw "Unresolved traceability sample: $($sample.clId)"
  }
}
$duration = [int] (($samples | Measure-Object durationSeconds -Sum).Sum)
if ($duration -gt 1800 -or $validation.traceabilityTotalSeconds -ne $duration) {
  throw "Traceability sample exceeds or misreports 1800 seconds: $duration"
}
"PASS: accepted inputs, observed counts, gate set, six output hashes, and 12-checklist traceability in $duration seconds"
'
```

## 6. JSON-/Markdown-Projektionsparitaet / JSON-to-Markdown Projection Parity

Der erste Tabellenwert jeder Matrix-Datenzeile ist die CL-ID. / The first
table value in every matrix data row is the CL ID.

```bash
pwsh -NoLogo -NoProfile -Command '
$base = "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment"
$assessment = Get-Content -LiteralPath "$base/assessment-results.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$markdown = Get-Content -LiteralPath "$base/evidence-matrix.md" -Raw -Encoding UTF8
$markdownIds = [regex]::Matches($markdown, "(?m)^\| (CL-[0-9]{2}-[0-9]{2}) \|") |
  ForEach-Object { $_.Groups[1].Value }
$jsonIds = @($assessment.matrixRows.clId)
$missing = @($jsonIds | Where-Object { $_ -notin $markdownIds })
$extra = @($markdownIds | Where-Object { $_ -notin $jsonIds })
$duplicates = @($markdownIds | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
[ordered]@{
  jsonRows = $jsonIds.Count
  markdownRows = @($markdownIds).Count
  missing = $missing
  extra = $extra
  duplicates = $duplicates
} | ConvertTo-Json -Depth 4
if ($jsonIds.Count -ne 157 -or @($markdownIds).Count -ne 157 -or
    $missing.Count -ne 0 -or $extra.Count -ne 0 -or $duplicates.Count -ne 0) {
  throw "JSON/Markdown matrix projection drift"
}
'
```

Gap- und Inventarprojektionen werden mit ihren vertraglich festgelegten
Ueberschriften exakt verglichen: / Compare gap and inventory projections
exactly through their contract-defined headings:

```bash
pwsh -NoLogo -NoProfile -Command '
$base = "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment"
$assessment = Get-Content -LiteralPath "$base/assessment-results.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$checks = @(
  [ordered]@{
    name = "gaps"
    expected = @($assessment.gaps.gapId)
    markdown = "$base/prioritized-gap-list.md"
    pattern = "(?m)^### (GAP-[0-9]{3,})\s*$"
  },
  [ordered]@{
    name = "inventory"
    expected = @(
      $assessment.inventory.toolchains.inventoryId
      $assessment.inventory.agents.inventoryId
      $assessment.inventory.presets.inventoryId
      $assessment.inventory.additionalTools.inventoryId
    )
    markdown = "$base/inventory-reconciliation.md"
    pattern = "(?m)^### (INV-[A-Z0-9-]+)\s*$"
  }
)
foreach ($check in $checks) {
  $actual = [regex]::Matches(
    (Get-Content -LiteralPath $check.markdown -Raw -Encoding UTF8),
    $check.pattern
  ) | ForEach-Object { $_.Groups[1].Value }
  $missing = @($check.expected | Where-Object { $_ -notin $actual })
  $extra = @($actual | Where-Object { $_ -notin $check.expected })
  $duplicates = @($actual | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
  if (@($actual).Count -ne @($check.expected).Count -or
      $missing.Count -ne 0 -or $extra.Count -ne 0 -or
      $duplicates.Count -ne 0) {
    throw "$($check.name) projection drift: missing=$missing extra=$extra duplicates=$duplicates"
  }
  "PASS: $($check.name) projection $(@($actual).Count)/$(@($check.expected).Count)"
}
'
```

## 7. Inventarabgleich / Inventory Reconciliation

Statische vorhandene Pruefungen: / Existing static checks:

```bash
python3 scripts/check-dockerfile-arg-renovate.py
python3 scripts/tests/test_agent_prompt_dispatchers.py
podman-compose config
```

Exaktes installiertes Zwölferprofil in beiden vorhandenen Varianten: / Exact
installed twelve-preset profile in both existing variants:

```bash
bash scripts/install-spec-kit-governance-presets.sh \
  --repo . \
  --preset-config scripts/config/spec-kit-model-routing-governance-presets.json \
  --check-only
```

```bash
pwsh -NoLogo -NoProfile \
  -File scripts/install-spec-kit-governance-presets.ps1 \
  -Repo . \
  -PresetConfig scripts/config/spec-kit-model-routing-governance-presets.json \
  -CheckOnly
```

```bash
specify preset list
specify preset info security-governance
specify preset resolve plan-template
```

Die kanonische Assessment-Datei erzwingt danach auch die Sollzahlen,
Pruefdimensionen und Gap-Zuordnungen des Inventars: / The canonical assessment
then enforces inventory counts, review dimensions, and gap mappings:

```bash
pwsh -NoLogo -NoProfile -Command '
$path = "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json"
$data = Get-Content -LiteralPath $path -Raw -Encoding UTF8 | ConvertFrom-Json
$items = @(
  $data.inventory.toolchains
  $data.inventory.agents
  $data.inventory.presets
  $data.inventory.additionalTools
)
$gaps = @($data.gaps.gapId)
$expected = [ordered]@{
  MSLToolchain = 6
  ScriptingFoundation = 2
  RequiredAgent = 4
  AdditionalAgentSurface = 2
  BindingPreset = 8
  AdditionalPreset = 4
}
foreach ($entry in $expected.GetEnumerator()) {
  $actual = @($items | Where-Object category -eq $entry.Key).Count
  if ($actual -ne $entry.Value) { throw "Inventory count $($entry.Key): $actual/$($entry.Value)" }
}
$agentDimensions = @("Installation", "VersionPin", "VersionCheck", "State", "Dispatcher", "ProviderSignIn", "DocumentationCategory")
$presetDimensions = @("PresetIdentity", "PresetVersion", "PresetPriority", "PresetEnabled", "PresetResolution", "PresetCoverage")
foreach ($item in $items) {
  $requiredDimensions = if ($item.category -in @("RequiredAgent", "AdditionalAgentSurface")) {
    $agentDimensions
  } elseif ($item.category -in @("BindingPreset", "AdditionalPreset")) {
    $presetDimensions
  } else {
    @("TargetClaim")
  }
  $observedDimensions = @($item.observations.dimension | Sort-Object -Unique)
  $missingDimensions = @($requiredDimensions | Where-Object { $_ -notin $observedDimensions })
  if ($missingDimensions.Count -ne 0) { throw "$($item.inventoryId) missing dimensions: $missingDimensions" }
  if ($item.reconciliationStatus -eq "Aligned" -and $item.gapId -ne "N/A") {
    throw "$($item.inventoryId) aligned but has gap $($item.gapId)"
  }
  if ($item.reconciliationStatus -in @("Mismatch", "Missing", "Open") -and
      ($item.gapId -eq "N/A" -or $item.gapId -notin $gaps)) {
    throw "$($item.inventoryId) has no valid gap"
  }
}
"PASS: inventory 6/2/4/2/8/4 plus at least 3 additional tools with required dimensions and gap mappings"
'
```

Praktischer Containercheck nur bei erreichbarer lokaler Podman-Umgebung: /
Practical container check only when the local Podman environment is available:

```bash
podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh
```

Erwartet / Expected:

- Statische Checks und das 12-Preset-Profil bestehen. / Static checks and the
  12-preset profile pass.
- Der Smoke-Test prueft die sechs MSL-Familien, PowerShell, Node/npm,
  Werkzeuge und Agent-CLIs. / Smoke test covers declared tools and agents.
- Ist Podman nicht erreichbar, lautet das Ergebnis `Open`, niemals `Pass`. /
  Unavailable Podman is Open, never Pass.
- Jede Abweichung zwischen Dockerfile, Compose, Registry, Smoke-Test,
  Dispatcher und Doku wird genau einem Gap zugeordnet. / Every discrepancy
  maps to exactly one gap.

## 8. Bilingualitaet, A11Y und Documentation Impact / Bilingual, A11Y, and Documentation Impact

```bash
heuristic_output=$(bash -c '
source scripts/lib/hg-bilingual.sh
source scripts/lib/hg-a11y.sh
for file in "$@"; do
  hg_check_bilingual "$file" || true
  hg_check_a11y "$file" || true
done
' _ docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/*.md
)
printf '%s\n' "$heuristic_output"
if printf '%s\n' "$heuristic_output" | rg -q '^WARN\|'; then
  exit 1
fi
```

Die vorhandenen Hilfsfunktionen melden Befunde ueber `WARN|...`; ihre
Funktions-Exitcodes sind kein stabiler Pass-/Fail-Vertrag. Deshalb wertet der
Wrapper die Ausgabe aus. / The existing helpers report findings as `WARN|...`;
their function exit codes are not a stable pass/fail contract, so the wrapper
evaluates their output.

```bash
bash scripts/validate-documentation-impact.sh \
  --evidence docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/documentation-impact.json
```

Wenn `lychee` vorhanden ist: / If `lychee` is available:

```bash
lychee --offline --include-fragments --no-progress \
  --exclude-path docs/security/agent-session-log \
  './**/*.md'
```

Automatische Heuristiken ersetzen nicht die redaktionelle Vollpruefung. Diese
muss 0 fehlende englische Partner, 0 unerklaerte erste Fachbegriffe, 0 nur
visuell transportierte Pflichtinformationen und 0 unerklaerte CEFR-B2-
Abweichungen protokollieren. / Automated heuristics do not replace the full
editorial review, which must record zero defects in the four categories.

## 9. Statistik nur read-only bewerten / Assess Statistics Read-Only

```bash
stats_json=$(bash scripts/render-project-statistics.sh --repo . --check-only --json)
stats_exit=$?
printf '%s\n' "$stats_json"
if [ "$stats_exit" -ne 0 ] && [ "$stats_exit" -ne 1 ]; then
  exit "$stats_exit"
fi
```

```bash
pwsh -NoLogo -NoProfile -Command '
& scripts/render-project-statistics.ps1 -Repo . -CheckOnly -Json
$statsExit = $LASTEXITCODE
if ($statsExit -notin @(0, 1)) { exit $statsExit }
'
```

Erwartet / Expected: Beide Varianten liefern denselben Status. `DRIFT` wird als
Assessment-Gap dokumentiert und fuehrt in diesem Feature weder zu einem Render
noch zu einem Statistik-Commit. Ein spaeterer Statistik-Commit braucht einen
Post-Feature-Trigger und separate Authority und darf nur Statistikpfade
enthalten. / Both variants agree. Drift becomes an assessment gap and causes no
statistics edit or commit in this feature.

## 10. Serienzustand pruefen, nicht fortschreiben / Validate, Do Not Advance, the Series

```bash
bash .specify/presets/intake-review-governance/scripts/validate-intake-review-result.sh \
  --result specs/intake-review-results/sandbox-development-lifecycle.json \
  --repo .
```

```bash
bash .specify/presets/intake-sequencing-governance/scripts/validate-intake-series-manifest.sh \
  --file specs/intake-series/sandbox-development-lifecycle/manifest.json \
  --repo . \
  --json
```

```bash
bash .specify/presets/intake-sequencing-governance/scripts/validate-intake-series-receipt.sh \
  --file specs/intake-series/sandbox-development-lifecycle/receipt.json \
  --repo . \
  --json
```

Erwartet / Expected: Der aktuelle GSDB-Root ist der einzige `Eligible`-Eintrag;
Hardening bleibt `Blocked`. Dieser Lauf fuehrt weder Series Update noch
`series-next` aus. / The GSDB root remains the only eligible entry and hardening
remains blocked. This run performs no advancement.

Erst ausserhalb dieses Features, nach dokumentiertem `AcceptedBaseline` und
neuer Authority, ist die Reihenfolge: / Only outside this feature, after
documented acceptance and fresh authority, the sequence is:

1. `/speckit-intake-series-update` separat autorisieren und ausfuehren. /
   Separately authorize and execute series update.
2. `/speckit-intake-series-status` read-only validieren. / Validate status
   read-only.
3. `/speckit-intake-series-next` read-only Kandidaten anzeigen lassen. / List
   candidates read-only.

Keiner dieser Befehle erteilt Implementierungs- oder Remote-Authority. / None
of these commands grants implementation or remote authority.

## 11. Intended Delivery Set und Content-Commit / Intended Delivery Set and Content Commit

Vor einem autorisierten Commit jeden unversionierten Zielpfad explizit nennen.
Die Liste muss nach Erzeugung der Implementierungsartefakte vervollstaendigt
werden. / Explicitly name every untracked intended path before an authorized
commit; complete the list after artefact creation.

```bash
session_args=()
while IFS= read -r session_log; do
  session_args+=(--intended "$session_log")
done < <(rg -l '002-gsdb-baseline-assessment|Lastenheft_GSDB-Spec-Kit-Intensivpruefung' \
  docs/security/agent-session-log/*.md)
if [ "${#session_args[@]}" -eq 0 ]; then
  printf '%s\n' 'No feature-related sanitized session log found' >&2
  exit 1
fi
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-delivery-set.sh \
  --repo . \
  --intended .specify/feature.json \
  --intended specs/002-gsdb-baseline-assessment/spec.md \
  --intended specs/002-gsdb-baseline-assessment/plan.md \
  --intended specs/002-gsdb-baseline-assessment/research.md \
  --intended specs/002-gsdb-baseline-assessment/data-model.md \
  --intended specs/002-gsdb-baseline-assessment/quickstart.md \
  --intended specs/002-gsdb-baseline-assessment/contracts/assessment-artifact-contract.md \
  --intended specs/002-gsdb-baseline-assessment/contracts/assessment-results.schema.json \
  --intended specs/002-gsdb-baseline-assessment/contracts/validation-results.schema.json \
  --intended specs/002-gsdb-baseline-assessment/autonomous-run-state.json \
  --intended specs/002-gsdb-baseline-assessment/autonomous-run-evidence.md \
  --intended specs/002-gsdb-baseline-assessment/autonomous-run-gate-requirements.json \
  --intended specs/002-gsdb-baseline-assessment/checklists/autonomous-readiness.md \
  --intended specs/002-gsdb-baseline-assessment/checklists/requirements.md \
  --intended specs/002-gsdb-baseline-assessment/tasks.md \
  --intended docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/README.md \
  --intended docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json \
  --intended docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/evidence-matrix.md \
  --intended docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/prioritized-gap-list.md \
  --intended docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/inventory-reconciliation.md \
  --intended docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/documentation-impact.json \
  --intended docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json \
  "${session_args[@]}"
```

Der Validator prueft die benannten unversionierten Pfade. Zusaetzlich wird das
tatsaechliche Staging-Inventar gegen die zwei erlaubten Inhaltswurzeln und alle
einzeln erkannten, feature-bezogenen, sanitisierten Sitzungslogs abgeglichen: /
The validator checks named untracked paths. Additionally, compare the actual
staged inventory with the two allowed content roots and every individually
identified sanitized session log from this feature run:

```bash
pwsh -NoLogo -NoProfile -Command '
$staged = @(git diff --cached --name-only --diff-filter=ACMR)
if ($LASTEXITCODE -ne 0) { throw "Cannot read staged delivery set" }
$expected = @(
  ".specify/feature.json",
  "specs/002-gsdb-baseline-assessment/spec.md",
  "specs/002-gsdb-baseline-assessment/plan.md",
  "specs/002-gsdb-baseline-assessment/research.md",
  "specs/002-gsdb-baseline-assessment/data-model.md",
  "specs/002-gsdb-baseline-assessment/quickstart.md",
  "specs/002-gsdb-baseline-assessment/tasks.md",
  "specs/002-gsdb-baseline-assessment/autonomous-run-state.json",
  "specs/002-gsdb-baseline-assessment/autonomous-run-evidence.md",
  "specs/002-gsdb-baseline-assessment/autonomous-run-gate-requirements.json",
  "specs/002-gsdb-baseline-assessment/checklists/autonomous-readiness.md",
  "specs/002-gsdb-baseline-assessment/checklists/requirements.md",
  "specs/002-gsdb-baseline-assessment/contracts/assessment-artifact-contract.md",
  "specs/002-gsdb-baseline-assessment/contracts/assessment-results.schema.json",
  "specs/002-gsdb-baseline-assessment/contracts/validation-results.schema.json",
  "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/README.md",
  "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json",
  "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/evidence-matrix.md",
  "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/prioritized-gap-list.md",
  "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/inventory-reconciliation.md",
  "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/documentation-impact.json",
  "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json"
)
$sessionLogs = @($staged | Where-Object { $_ -match "^docs/security/agent-session-log/[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{4}\\.md$" })
$unrelatedSessionLogs = @($sessionLogs | Where-Object {
  (Get-Content -LiteralPath $_ -Raw -Encoding UTF8) -notmatch
    "002-gsdb-baseline-assessment|Lastenheft_GSDB-Spec-Kit-Intensivpruefung"
})
$sensitiveSessionLogs = @($sessionLogs | Where-Object {
  (Get-Content -LiteralPath $_ -Raw -Encoding UTF8) -match
    "(?im)^\\s*(prompt|response|antwort)\\s*:"
})
$textPaths = @($staged | Where-Object { $_ -match "\\.(?:md|json)$" })
$privatePathPatterns = @(
  ("(?i)/" + "Users/[^/<\\s]+"),
  "(?i)[A-Z]:[\\\\/]+Users[\\\\/]+[^<\\\\/\\s]+",
  ("(?i)/" + "home/(?!adedev\\b)[^/<\\s]+")
)
$privatePathLeaks = @($textPaths | Where-Object {
  $content = Get-Content -LiteralPath $_ -Raw -Encoding UTF8
  @($privatePathPatterns | Where-Object { $content -match $_ }).Count -gt 0
})
$missing = @($expected | Where-Object { $_ -notin $staged })
$forbidden = @($staged | Where-Object { $_ -notin $expected -and $_ -notin $sessionLogs })
if ($staged.Count -eq 0) { throw "Empty staged delivery set" }
if ($sessionLogs.Count -lt 1) { throw "Expected at least one related sanitized session log" }
if ($unrelatedSessionLogs.Count -ne 0) { throw "Unrelated staged session logs: $unrelatedSessionLogs" }
if ($sensitiveSessionLogs.Count -ne 0) { throw "Unsanitized staged session logs: $sensitiveSessionLogs" }
if ($privatePathLeaks.Count -ne 0) { throw "Private host paths in staged content: $privatePathLeaks" }
if ($missing.Count -ne 0) { throw "Missing intended staged paths: $missing" }
if ($forbidden.Count -ne 0) { throw "Out-of-scope staged paths: $forbidden" }
if ($staged -match "^\\.specify/runtime/" -or
    $staged -match "^(Dockerfile|compose.*\\.yml)$" -or
    $staged -match "^docs/project-statistics(?:\\.config)?\\.(?:md|json)$") {
  throw "Prohibited staged path"
}
"PASS: exact staged scope with $($staged.Count) paths"
'
```

Der vorhandene Delivery-Set-Validator ruft intern `git write-tree` auf und ist
deshalb nicht rein read-only. Wenn die aktuelle Sandbox das erforderliche
Git-Metadaten-Lock nicht erlaubt, bleibt der Nachweis mit `AEI004` `Blocked`;
der exakte Staging-Abgleich ersetzt diesen Pflichtvalidator nicht und darf den
Blocker nicht ueberstimmen. / The existing delivery-set validator internally
calls `git write-tree` and is therefore not strictly read-only. If the sandbox
cannot create the Git metadata lock, evidence remains Blocked with `AEI004`;
the exact staged comparison is supplemental and cannot override that blocker.

Danach / Then:

```bash
git diff --check
podman-compose config
uvx pre-commit run --all-files
git status --short
```

Unbedingt ausschliessen / Always exclude:

- `.specify/runtime/**/*.log.txt`,
- fremde Session-Logs und fremde unversionierte Dateien, / unrelated session
  logs and untracked files;
- `Dockerfile`, `compose*.yml`, Laufzeit-, Secret-, Provider-, Plattform- und
  Hardening-Dateien, / prohibited technical files;
- `docs/project-statistics.md` und
  `docs/project-statistics.config.json` aus dem Assessment-Content-Commit. /
  statistics files from the assessment content commit.

Der Content-Commit darf erst nach expliziter Delivery-Authority entstehen und
enthaelt genau die beabsichtigten Feature-/Assessment-/sanitierten Session-
Evidenzpfade. / Create the single content commit only under explicit delivery
authority and with intended paths only.

## 12. Exact-Head Gate Evidence und Abschluss / Exact-Head Gate Evidence and Closeout

Vor Merge eine temporaere Schema-2.0-`PreMerge`-Datei fuer den exakten
reviewten Head erzeugen. Sie enthaelt fuer jedes deklarierte Gate genau eine
`Primary`-Zeile. / Before merge, create temporary schema-2.0 PreMerge evidence
for the exact reviewed head with one Primary row per declared gate.

```bash
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh \
  --requirements specs/002-gsdb-baseline-assessment/autonomous-run-gate-requirements.json \
  --evidence /tmp/002-gsdb-baseline-assessment.pre-merge.json \
  --head "$(git rev-parse HEAD)"
```

Nach einem autorisierten Merge wird eine separate kausale Schema-2.0-
`PostMerge`-Evidenz mit akzeptiertem PreMerge-Hash, echtem Merge-Commit und
leeren `changedPaths` validiert. Sie erzeugt kein Produktdelta. / After an
authorized merge, validate separate causal PostMerge evidence with no product
delta.

```bash
reviewed_head=$(pwsh -NoLogo -NoProfile -Command '
$evidence = Get-Content -LiteralPath /tmp/002-gsdb-baseline-assessment.pre-merge.json -Raw -Encoding UTF8 | ConvertFrom-Json
$evidence.reviewedHead
')
merge_commit="$(git rev-parse HEAD)"
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh \
  --requirements specs/002-gsdb-baseline-assessment/autonomous-run-gate-requirements.json \
  --evidence /tmp/002-gsdb-baseline-assessment.post-merge.json \
  --head "$reviewed_head" \
  --merge-commit "$merge_commit"
```

`Completed` ist nur erlaubt, wenn Tasks, anwendbare Gates, Reviews,
Delivery-Modus, Default-Branch-Sync, Post-Merge-Aktionen und finale Validierung
terminal sind. Die fachliche Bewertung bleibt trotzdem `ReviewPending`, bis
die beiden menschlichen Rollen `AcceptedBaseline` dokumentieren. / Completed
requires terminal technical closeout, while the assessment remains
ReviewPending until human acceptance.

## 13. Verbotene Schritte / Prohibited Steps

In diesem Feature nicht ausfuehren: / Do not perform in this feature:

```bash
podman compose build --pull
podman compose down -v
```

Ebenfalls verboten sind: Dockerfile-/Compose-/Runtime-Haertung,
Secret-Rotation, Provider-/Modellwahl, Anmeldung, Plattform-Rulesets, formale
Freigabe, externe Registerpflege, Statistik-Rendering und der Start des
Hardening-Intakes. / Also prohibited are technical hardening, secret or
provider actions, platform rulesets, formal approval, external registers,
statistics rendering, and starting hardening.
