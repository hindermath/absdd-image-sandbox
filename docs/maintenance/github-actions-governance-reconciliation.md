# GitHub-Actions-Governance-Abgleich / GitHub Actions Governance Reconciliation

DE: Die anschliessende [Inhaltskorrektur](intake-content-repair-2026-10-06.md)
bearbeitet IR002 bis IR004; fuer den aktuellen Intake-Status ist ihr
Nachfolgereview massgeblich, nicht das unten beschriebene fruehere Ergebnis.
Keine Ausfuehrung oder Reihenfortschreibung wird dadurch autorisiert.

EN: The subsequent content repair addresses IR002 through IR004. Its successor
review governs current intake status, not the earlier outcome below. It does
not authorize execution or series advancement.

DE: Nachfolgereparatur vom 2026-10-06: `GOV-REV-001/RIG017` ist durch die
kanonische Archivbindung behoben; `GOV-CI-001` durch die datierte technische
[SandboxBaseline-Uebergabe](sandbox-baseline-handoff-2026-10-06.md) erfuellt.
Der [Reparaturbericht](sandbox-lifecycle-repair-2026-10-06.md) dokumentiert
neue Bindungen und das unabhaengige Review. Keine Abnahme oder Reihenfreigabe.

EN: The follow-up repair fixes RIG017 through canonical archive binding and
supplies the missing dated technical handoff. The repair report records new
bindings and independent review. Neither acceptance nor advancement is granted.

## Entscheidung / Decision

DE: Der Runnerwechsel in PR #90 aendert die CI-Umgebung, konkrete Checknamen
und operative Agent-Guidance, aber keine fachliche Intake-Anforderung oder
Akzeptanzbedingung. Die vier Intake-Texte bleiben unveraendert. Hash-Aktualitaet
ist kein semantisches Review geaenderter Quellen und keine Startberechtigung.
Ein gesonderter Agent prueft diesen Abgleich; das ist kein menschliches
Security-Review oder Vier-Augen-Testat.

EN: PR #90 changes the CI environment, concrete check names and operational
agent guidance, but no intake requirement or acceptance criterion. All four
intake texts remain unchanged. Current hashes do not establish semantic review
of changed sources or authority to start. A separate agent reviews this
reconciliation; this is not human security review or a four-eyes attestation.

## Quellen und technische Evidenz / Sources and Technical Evidence

- Baseline before PR #90: `1d5cb7f` (PR #89 merge).
- Migration commit: `4579fa8cdae8bccf18782f9b5a1b85cdc59bfdd5`.
- [PR #90](https://github.com/hindermath/absdd-image-sandbox/pull/90) checked head:
  `4521c9623a12b54ca984a0b7c47ad42bcc69148e`.
- Merge commit: `5deacc910227bb19684c335030c26ac5a075f9a0`.
- Read-only source comparison: `git diff 1d5cb7f..5deacc9 -- .github/workflows AGENTS.md`.
- Live ruleset `18493733`, inspected on 2026-10-06: active; strict checks for
  `Agent Secret Scan (ubuntu-22.04)`, `Agent Secret Scan (macos-15)` and
  `Agent Secret Scan (windows-2022)`, integration 15368.
- All nine PR checks succeeded: Markdown links and anchors; Sandbox static
  contracts; three Agent Secret Scan jobs; Maintenance TUI (Ubuntu);
  PSScriptAnalyzer (Ubuntu); Native proof (Ubuntu and Windows).

| Flaeche / Surface | Aenderung / Change | Grenze / Boundary |
|---|---|---|
| `homogeneity-check.yml` | `macos-14` -> `macos-15` | macOS job ran successfully; no sandbox runtime acceptance |
| `maintenance-tui.yml`, `powershell-analysis.yml` | Conditional reference-repository matrix uses `macos-15` | This repository still runs these jobs on Ubuntu only |
| Five maintained agent guidance files | Matching bilingual runner guidance and CI proof limits | Operational instruction, not a changed product requirement |
| `docs/security/branch-protection.md` | Current check names added beside July history | Read-only platform evidence, no rule mutation |

DE: Maintenance TUI und PowerShell Analysis aktivieren ihre macOS-/Windows-
Matrix nur in den benannten Referenz-Repositories. Die GitHub-Jobs pruefen
Vertraege und statische Regeln, nicht die native Podman-Sandbox oder das Image.
Historische Logs, Feature-003-Nachweise und abgeschlossene Runs bleiben erhalten.

EN: Maintenance TUI and PowerShell Analysis enable macOS/Windows only in
named reference repositories. GitHub jobs verify contracts and static rules,
not the native Podman sandbox or image. Historical logs, Feature 003 evidence
and completed runs remain unchanged.

## Intake-Auswirkungen / Intake Impact

| Intake | Zustand / State | Bewertung / Assessment |
|---|---|---|
| `Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md` | Completed | Historical assessment retained; no requirement update |
| `Lastenheft_Secure-Development-Container-Hardening.md` | Series Eligible; Feature 003 Completed | Separate advancement needed; completion is limited to the study |
| `Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md` | Blocked | Requires a current explicit SandboxBaseline handoff; CI cannot replace independent acceptance |
| `intakes/learner-fork-self-build-sandbox.md` | Blocked | Existing independent-acceptance completion gate remains binding |

DE: Fuer alle vier Texte sind Anforderungen, Akzeptanzkriterien und fachliche
Abhaengigkeiten durch den Runnerwechsel unveraendert. Die bestehenden
Intake-Reviews bleiben Nachweise fuer ihre damaligen Ziele; ihre Validatoren
pruefen heute passende Ziel-Hashes. Dieses Dokument erweitert ihre historische
Review-Aussage nicht. Das Series-Receipt und der Series-Review werden wegen
der Archivpfad-Aenderung nachvollziehbar ersetzt; die urspruenglichen Dateien
sind byte-identisch archiviert. Intake-Inhalte und Authoring-Receipts bleiben
unveraendert.

EN: The runner change leaves requirements, acceptance criteria and semantic
dependencies unchanged for all four texts. Existing intake reviews evidence
their original targets; their validators currently match target hashes. This
document does not expand the historical review claim. The series receipt and
review are explicitly superseded for the archive-path repair, with immutable
prior snapshots. Intake content and authoring receipts remain unchanged.

## Abschlussgrenze und offene Uebergabe / Completion Boundary and Open Handoff

DE: Feature 003 belegt 85 erledigte Aufgaben, terminalen Run-State und
[PR #53](https://github.com/hindermath/absdd-image-sandbox/pull/53), geliefert
auf Head `8b73d0a0e0b8680011876fcf906f3b08bcd36077` und gemergt als
`1c67b226d5a2c7c565c8b9630376710100798894`. Die ausdrueckliche Entscheidung
`DEC-FEASIBILITY-SINGLE-PERSON-2026-09-06` begrenzt den Abschluss auf eine
SourceRepositoryOnly-Machbarkeitsstudie bis 2026-12-31. Unabhaengige menschliche
Pruefung und moderierter Lernendentest waren `NotPerformed`; 49 Human-only-
Punkte bleiben offen. Der Run selbst wird nicht wieder geoeffnet.

EN: Feature 003 evidences 85 completed tasks, terminal run state and PR #53
delivery at the head and merge above. Decision
`DEC-FEASIBILITY-SINGLE-PERSON-2026-09-06` limits completion to a source-only
feasibility study through 2026-12-31. Independent human review and moderated
learner testing were NotPerformed; 49 human-only items remain open. The run
itself is not reopened.

- `Resolved GOV-CI-001` (technical documentation only): SBH-2026-10-06 binds
  the completed study, subsequent image changes and PR #90 to a dated baseline.
- Owner: Repository Maintainer; handoff scope to be checked by Security Review.
- Evidence: `specs/003-secure-development-container-hardening/autonomous-run-state.json`,
  `docs/security/secure-development/2026-08-30-container-hardening/human-only-handoffs.md`,
  `docs/security/secure-development/2026-08-30-container-hardening/feasibility-study-decision.json`.
- Evidence added: `docs/maintenance/sandbox-baseline-handoff-2026-10-06.md`.
- Follow-up: Security Review checks the supplied baseline before acceptance;
  any advancement requires the governed series-update process and authority.
- Re-evaluation trigger: before series advancement, acceptance-run start,
  learner rollout, distribution, production use, or study expiry.

DE: Manifest, Receipt und Abarbeitungsreihenfolge erhalten nur die korrigierte
Archivpfad-Bindung; ihre Lifecycle-Status bleiben unveraendert. `Completed` im historischen Run allein
setzt keinen Folgeschritt frei. Ein kuenftiger Series-Update muss die bisherigen
Artefakte byte-identisch archivieren und Review-/Evidenzbindungen erneut
pruefen; bei semantischer Intake-Aenderung ist zusaetzlich Intake-Update mit
nachfolgendem unabhaengigem Intake-Review erforderlich.

EN: The manifest, receipt and processing order receive only corrected archive
path bindings; lifecycle states remain unchanged. Completed in a historical run alone does not release a
successor. Any future series update must archive prior artifacts byte-for-byte
and check review/evidence bindings again. A semantic intake change additionally
requires intake update followed by independent intake review.

### Zusaetzlicher Lifecycle-Blocker / Additional Lifecycle Blocker

- `Resolved GOV-REV-001` (`RIG017`): the completed GSDB target is canonically
  bound inside the configured archive collection. The old root copy remains
  byte-identical only for historical feature/authoring input bindings.
- Evidence: `requirements/intake-governance-config.json` and
  `docs/maintenance/intake-lifecycle-fleet-rollout.json` already record the
  lifecycle finding. It predates PR #90 and is not caused by the runner change.
- Owner: Repository Maintainer.
- Repair operation: `9d9fce68-15cc-490c-afe0-16b98eda8a54`, explicitly authorized
  by the owner's request to correct both identified gaps on 2026-10-06.
- Follow-up: maintain archive paths, receipts, reviews and manifest references
  together. Do not move intake files ad hoc.
- Re-evaluation trigger: before any series advancement, collection migration
  or new acceptance run, and after the authorized repair.

DE: Der vorherige Exitcode 2 ist historisch dokumentiert. Nach der Reparatur
meldet die Gesamtkonfiguration `Aligned`. Dies bedeutet korrekte
Lifecycle-Bindungen, nicht Produkt-, Sandbox- oder Startfreigabe.

EN: The prior exit 2 remains historical evidence. The repaired configuration
reports Aligned, establishing lifecycle bindings rather than product,
sandbox or execution approval.

## Review und naechste Aktion / Review and Next Action

DE: Das separate Agent-Review wird im
[Reviewbericht](github-actions-governance-review.md) dokumentiert. Es ist ein
semantischer Zusatzabgleich, kein Ersatz der bestehenden Intake-Review-Results
und keine menschliche Abnahme. Das nachfolgende Reparatur-Review ist im
Reparaturbericht gebunden. Das damalige Vollreview meldete drei Inhaltsbefunde;
ihre anschliessend autorisierte Korrektur und das aktuelle Nachfolgereview
stehen im oben verlinkten Inhaltskorrekturbericht. Statuspruefungen bleiben
read-only; Reihenfortschreibung und neuer Abnahmelauf sind nicht freigegeben.
Kein Spec-Kit-Lauf startet hier.

EN: The separate agent review is recorded in the linked report. It is a
supplemental semantic reconciliation, not a replacement intake-review result
or human acceptance. The follow-up repair review is bound in the repair report.
That review identified three content findings; the authorized correction and
current successor review are recorded in the content-repair report above.
Status checks remain read-only. Advancement and a new acceptance run are not
authorized. No execution starts here.
