# Tasks: GSDB-Bestandspruefung / GSDB Baseline Assessment

## Zweck und Nutzung / Purpose and Use

**DE:** Diese Datei ordnet die spaetere Assessment-Implementierung in exakte,
abhaengige Arbeitsschritte. Technische IDs, Befehle, kontrollierte Statuswerte
und Pfade bleiben unveraendert Englisch; Zweck, Phasen, Stories, Abhaengigkeiten,
Entscheidungen und Abnahme werden Deutsch zuerst und Englisch danach erklaert.
Spec-Kit-Erfahrung wird nicht vorausgesetzt; der Quickstart erklaert die
verwendeten Fachbegriffe und Befehle. / **EN:** This file orders the later
assessment implementation into exact dependent work steps. Technical IDs,
commands, controlled status values, and paths remain unchanged in English;
purpose, phases, stories, dependencies, decisions, and acceptance are explained
German first and English second. No Spec Kit experience is assumed; the
quickstart explains the terms and commands.

**Input**: Accepted and plan-reviewed artefacts in
`specs/002-gsdb-baseline-assessment/`
**Prerequisites**: `spec.md`, `plan.md`, `research.md`, `data-model.md`,
`quickstart.md`, `contracts/`, `autonomous-run-state.json`,
`autonomous-run-gate-requirements.json`, and both accepted checklists
**Tests**: Contract-first evidence is required. Temporary negative fixtures
MUST fail before the representative slice and complete assessment are accepted.
**Scope**: Assessment evidence only. No Dockerfile, Compose/runtime, provider,
secret, platform-rule, formal-approval, external-register, hardening,
statistics-file, or next-intake implementation change is permitted.

**Organization**: Tasks are dependency ordered and grouped by user story.
US1 is the representative MVP. Every task records `Applicable`, justified
`N/A`, or `Open` separately from implementation status where a governance
checkpoint is involved.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: May run in parallel because it writes a different file and does not
  depend on incomplete shared JSON.
- **[Story]**: Maps directly to one of the four user stories in `spec.md`.
- A command reference such as `Q05` means the complete, unchanged code block
  under the matching heading in `quickstart.md`; those blocks are the exact
  copy-ready verification commands and MUST be recorded verbatim in
  `validation-results.json` when executed.

## Exact Verification Command Index

| ID | Exact command or binding block |
|---|---|
| `Q01` | `uname -s`; `pwsh -NoLogo -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'`; `git status --short --branch` |
| `Q02` | `pwsh -NoLogo -NoProfile -File .specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.ps1 -State specs/002-gsdb-baseline-assessment/autonomous-run-state.json` |
| `Q03` | Complete accepted-input `Get-FileHash -Algorithm SHA256` block in `quickstart.md` section 1, with all three accepted paths and hashes unchanged |
| `Q04` | Complete both last-completed routed-phase blocks in `quickstart.md` section 1, invoking `validate-autonomous-phase-result.ps1` and `.sh` with the state-derived result path, phase ID and exit code 0 |
| `Q05` | Complete gate-requirements structural PowerShell block in `quickstart.md` section 2 |
| `Q06` | Complete temporary `{}` schema-rejection PowerShell block in `quickstart.md` section 3 |
| `Q07` | Complete assessment schema command in `quickstart.md` section 3 using `Test-Json -SchemaFile specs/002-gsdb-baseline-assessment/contracts/assessment-results.schema.json` |
| `Q08` | Complete 37-path, 12-checklist, exact per-checklist-count and 157-ID source-integrity PowerShell block in `quickstart.md` section 4 |
| `Q09` | Complete assessment semantic PowerShell block in `quickstart.md` section 5, including status, role, reference, source-integrity, reciprocal gap and recomputed checklist/status/gap/Human-only/inventory/error-counter checks |
| `Q10` | Complete validation-bundle schema, hash, gate-set, count and 12-sample PowerShell block in `quickstart.md` section 5 |
| `Q11` | Both projection-parity PowerShell blocks in `quickstart.md` section 6 |
| `Q12` | `python3 scripts/check-dockerfile-arg-renovate.py`; `python3 scripts/tests/test_agent_prompt_dispatchers.py`; `podman-compose config` |
| `Q13` | `bash scripts/install-spec-kit-governance-presets.sh --repo . --preset-config scripts/config/spec-kit-model-routing-governance-presets.json --check-only` |
| `Q14` | `pwsh -NoLogo -NoProfile -File scripts/install-spec-kit-governance-presets.ps1 -Repo . -PresetConfig scripts/config/spec-kit-model-routing-governance-presets.json -CheckOnly` |
| `Q15` | `specify preset list`; `specify preset info security-governance`; `specify preset resolve plan-template` |
| `Q16` | Complete `6/2/4/2/8/4` inventory and required-dimension PowerShell block in `quickstart.md` section 7 |
| `Q17` | `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh` only when the running service and intended endpoint are available; otherwise record `Open`, owner and retry trigger |
| `Q18` | Complete `hg_check_bilingual` plus `hg_check_a11y` warning-failing Bash wrapper in `quickstart.md` section 8 |
| `Q19` | `bash scripts/validate-documentation-impact.sh --evidence docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/documentation-impact.json` |
| `Q20` | `lychee --offline --include-fragments --no-progress --exclude-path docs/security/agent-session-log './**/*.md'` |
| `Q21` | Both read-only Statistics Profile 2 commands in `quickstart.md` section 9: `render-project-statistics.sh --repo . --check-only --json` and `render-project-statistics.ps1 -Repo . -CheckOnly -Json`, accepting only documented exit codes 0 or 1 |
| `Q22` | The three read-only intake review, series manifest and series receipt validator commands in `quickstart.md` section 10 |
| `Q23` | Complete dynamic feature-session-log plus `validate-autonomous-delivery-set.sh` allowlist command in `quickstart.md` section 11 |
| `Q24` | Complete staged-path PowerShell allowlist, sanitized-content and private-host-path block in `quickstart.md` section 11, followed by `git diff --cached --check` |
| `Q25` | `git diff --check`; `podman-compose config`; `uvx pre-commit run --all-files`; `git status --short` |
| `Q26` | `bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh --requirements specs/002-gsdb-baseline-assessment/autonomous-run-gate-requirements.json --evidence /tmp/002-gsdb-baseline-assessment.pre-merge.json --head "$(git rev-parse HEAD)"` |
| `Q27` | Complete causal PostMerge command in `quickstart.md` section 12 using `/tmp/002-gsdb-baseline-assessment.post-merge.json`, the accepted `reviewedHead`, and the actual `merge_commit` |
| `Q28` | `bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.sh --state specs/002-gsdb-baseline-assessment/autonomous-run-state.json` and Q02 for cross-shell final-state parity |

---

## Phase 1: Setup - Current Evidence and Gate Boundary

**Purpose**: Revalidate the accepted autonomous boundary before any assessment
implementation edit. A failure stops implementation and requires the governed
resume path; it is never converted to a positive result.

- [x] T001 Run Q01 and Q02, confirm branch `002-gsdb-baseline-assessment`, run ID `20befce1-05ca-45ea-b145-1e23afaa1e31`, `Active` status and a completed post-tasks Analyze phase before implementation, then record the exact outputs in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T002 Run Q03 and fail closed unless all three accepted paths and SHA-256 values match `specs/002-gsdb-baseline-assessment/spec.md`; record the bindings in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json` and `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T003 Run both Q04 validator variants for only the last completed routed phase, retain older phase results as historical lineage, and refresh the readable phase-boundary summary from the validated state in `specs/002-gsdb-baseline-assessment/autonomous-run-evidence.md`
- [x] T004 Run Q05 and reconcile all 13 declared gate IDs, applicability decisions, command tokens, runner tokens, rationales and triggers against `specs/002-gsdb-baseline-assessment/autonomous-run-gate-requirements.json`
- [x] T005 Reconcile the open boxes and implementation prerequisites without claiming implementation completion in `specs/002-gsdb-baseline-assessment/checklists/autonomous-readiness.md`
- [x] T006 Dynamically inventory every feature-related sanitized log matching `docs/security/agent-session-log/*.md` by the feature path or accepted-intake name at implementation start, including logs created by later planning phases; reject prompt/response/secret content and private host paths, then add every exact accepted path to the delivery evidence in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T007 Capture the pre-implementation changed/untracked path set with `git status --short` and `git diff --name-only`, prove that `Dockerfile`, `compose*.yml`, runtime/provider/secret/ruleset/approval/register/hardening/statistics paths are excluded, and record the baseline in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T008 Search for every executable validator that reads changed paths, markers, schemas, status values, assessment output or documentation-impact evidence with `rg -n 'assessment-results|validation-results|documentation-impact|autonomous-run|ReviewPending|AcceptedBaseline' scripts .specify/presets`, and record the triggered validator inventory in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`

**Checkpoint**: Accepted inputs, run state, last completed phase, gate contract,
scope baseline and validator inventory are current before Phase 2.

---

## Phase 2: Foundational - File Contracts and Draft State

**Purpose**: Establish the seven fixed outputs and their fail-closed Draft
state before any user-story rollout.

- [x] T009 Create the German-first/English-second reader path, glossary, state definitions, authority boundary, six linked outputs plus validation output, and verification route in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/README.md`
- [x] T010 Create a strict UTF-8 JSON Draft containing all top-level contract objects and exactly six non-self output paths in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T011 Create an initial strict UTF-8 Draft validation bundle with all 13 gate rows, exact accepted inputs, self path, `Blocked`/`Draft` state and no invented pass in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T012 Create the single structured `UpdateRequired` decision with reader, source, owner, navigation, document class, inline language partner, platform proof, `RepositoryDocumentation`, `NoUpdateRequired` Home-sync disposition and re-evaluation trigger in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/documentation-impact.json`
- [x] T013 Run Q06 against an untracked temporary `{}` fixture under `/tmp`, require the expected schema rejection, delete the fixture, and record the red-contract proof in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`

**Checkpoint**: All fixed outputs have known ownership; only Draft/Blocked is
permitted until every applicable user-story and gate task passes.

---

## Phase 3: User Story 1 - Vollstaendige GSDB-Abdeckung / Complete GSDB Coverage (Priority: P1) MVP

**Goal**: A reviewer finds all 37 manifest-controlled sources, all twelve
checklists and every one of the 157 stable CL IDs exactly once.

**Independent Test**: Q07, Q08, Q09 and Q11 report 37 sources, 12 checklists,
157 rows, 157 unique IDs, no missing/extra/duplicate IDs and identical JSON and
Markdown row sets.

- [x] T014 [US1] Run Q08 before authoring, preserve manifest/guideline/checklist/compendium/generator drift as findings, and create exactly 37 unique `SourceSnapshot` objects with current hashes or explicit missing status in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T015 [US1] Extract the canonical checklist heading IDs with the Q08 regular expression `(?m)^#### (CL-[0-9]{2}-[0-9]{2}):`, preserve checklist order, and create exactly 157 unique draft rows in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T016 [US1] Give every draft row all FR-005 fields, deterministic FR-007 status axes, allowed roles, evidence reference, risk rationale, concrete trigger and a reciprocal open gap where required in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T017 [US1] Copy the Draft to `/tmp/002-gsdb-baseline-assessment.missing-cl-12-05.json`, remove `CL-12-05`, run the Q07 schema and Q09 semantic contracts against the temporary path, require rejection with one missing ID, and record the red result in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T018 [US1] Complete the representative `CL-12-05` vertical slice from canonical source through current repository evidence, tool/agent/preset observation, deterministic row status, gap or `N/A`, human-only boundary, summary counter and Markdown row in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json` and `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/evidence-matrix.md`
- [x] T019 [US1] Run Q07 and Q09 after T018, require the canonical Draft including the `CL-12-05` slice to pass the same structural and semantic contracts, and append the green vertical-slice proof to `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T020 [US1] Assess the remaining 156 canonical rows without silent source preference, using `Open` or `FollowUp` for stale, conflicting, missing, skipped, non-reproducible or platform-limited evidence in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T021 [P] [US1] Recompute each binding checklist count `12/13/15/10/13/11/12/13/17/17/12/12`, applicability, implementation, assessment-status, gap-priority, `HumanOnly`/`NotHumanOnly`, inventory and all error counters from detail objects rather than copying asserted totals in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T022 [P] [US1] Project all 157 rows into twelve checklist sections with repeated accessible headers, German first and English second, plus complete textual state and dependency explanations in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/evidence-matrix.md`
- [x] T023 [US1] Run Q07, Q08, Q09 and the matrix part of Q11, require all twelve binding checklist counts plus zero source, ID, status, role, reference, summary-counter and projection errors, and bind observed outputs in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T024 [US1] Record the independently reviewable 37/12/157 acceptance result and any honest `Open` source drift without modifying GSDB source files in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/README.md`

**Checkpoint**: US1 is independently reviewable and supplies the MVP vertical
slice plus complete canonical coverage.

---

## Phase 4: User Story 2 - Nachvollziehbare Evidenz und Grenzen / Traceable Evidence and Boundaries (Priority: P1)

**Goal**: Every row explains what was checked, what local evidence supports
the status, and which decision remains human-only.

**Independent Test**: Q09 and Q10 resolve every object reference and exactly
one sample per checklist within 1,800 seconds; human-only rows remain `Open`
with an accountable human role.

- [x] T025 [US2] Catalogue candidate evidence under `docs/security/`, `docs/architecture/`, `docs/accessibility/`, Spec-Kit artefacts, build/test/audit/SBOM records and repository configuration without treating file existence as validity in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T026 [US2] Execute each read-only check needed for an `AlreadySatisfied` row, record exact command, expected/observed result, date, platform, limitations, current path/hash and `containsSensitiveContent: false`, and downgrade every skipped or stale check in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T027 [US2] Reconcile every formal approval, privacy/legal decision, secret action, platform rule, external register, risk acceptance, `AcceptedBaseline`, sign-in/provider decision and external publication against the Human-only table in `specs/002-gsdb-baseline-assessment/spec.md`, keeping each affected row open in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T028 [P] [US2] Add exact evidence IDs, repository paths, verification methods, limitations and reciprocal conditional gap IDs to every visible row in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/evidence-matrix.md`
- [x] T029 [P] [US2] Record exactly one traceability sample for each of `CL-01` through `CL-12`, including resolved row, evidence, conditional gap, start/end timestamps and duration, in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T030 [US2] Require the twelve T029 samples to be unique and total at most 1,800 seconds by running Q10, and record the independent reviewer outcome in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T031 [US2] Validate the FR-007 decision table, role allowlist, risk vocabulary, concrete triggers, human-only status and positive-evidence freshness with Q09 in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T032 [US2] Create a second temporary negative fixture at `/tmp/002-gsdb-baseline-assessment.invalid-gap.json` by breaking the `CL-12-05` reciprocal gap or evidence reference, require Q09 to reject it, delete it, and record the expected failure in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T033 [US2] Validate all current six non-self output hashes, accepted-input hashes, 13 gate rows, recomputed counts and traceability records with Q10 in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T034 [US2] Explain `Draft`, `ReviewPending`, Human-only `AcceptedBaseline`, drift reset, evidence limits and the no-overclaim rule in German first and English second in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/README.md`
- [x] T035 [US2] Record zero unsupported positive claims and 100-percent visible Human-only ownership as the independently reviewable US2 result in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/evidence-matrix.md`

**Checkpoint**: US2 is independently reviewable without oral explanation or
external assumptions.

---

## Phase 5: User Story 3 - Priorisierte Lueckenliste / Prioritised Gap List (Priority: P2)

**Goal**: Every row that is neither `AlreadySatisfied` nor justified `N/A`
maps to exactly one prioritised, actionable but non-authorizing gap.

**Independent Test**: Q09 and the gap part of Q11 report no missing, orphaned,
unreferenced or duplicate gap mapping.

- [x] T036 [US3] Derive stable `GAP-001`-style objects for all and only gap-requiring rows, non-aligned sources and inventory differences, preserving reciprocal CL/source/inventory references in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T037 [US3] Populate priority, every affected CL ID, bilingual summary, root cause, evidence state, impact, likelihood, dependencies, owner, action, acceptance criterion, expected evidence, target date, residual risk, concrete trigger and Human-only status for each gap in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T038 [US3] Project every JSON gap exactly once as a `### GAP-*` section sorted by P0, P1, P2, P3 and ID, retaining all grouped IDs and grouping rationales in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/prioritized-gap-list.md`
- [x] T039 [P] [US3] State that gaps grant no implementation, Git, remote, bypass or risk-acceptance authority and name `Lastenheft_Secure-Development-Container-Hardening.md` only as a conditional later candidate in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/README.md`
- [x] T040 [US3] Run Q09 and the gap projection portion of Q11, require zero unassigned/orphan/unreferenced gaps and exact JSON/Markdown parity, and record the result in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T041 [US3] Record exact counts by priority and Human-only category plus the independently reviewable no-hardening/no-next-intake disposition in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/README.md`

**Checkpoint**: US3 provides a complete prioritised handoff without starting
remediation or the next intake.

---

## Phase 6: User Story 4 - Installationsangaben abgleichen / Reconcile Installation Claims (Priority: P2)

**Goal**: Target claims and observations for toolchains, agents, supporting
tools and all twelve presets are separated and every mismatch is visible.

**Independent Test**: Q12 through Q17 and Q16 report exactly 6 MSL, 2 separate
foundations, 4 required agents, 2 additional agent surfaces, 8 binding presets,
4 additional presets and at least 3 supporting tools, or an honest Open result
for an unavailable runtime/platform check.

- [x] T042 [US4] Reconcile .NET/C#, Java/JVM, Go, Rust, Python and Swift separately across target claim, `Dockerfile`, version evidence and smoke-test evidence in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T043 [US4] Reconcile PowerShell 7 and Node.js/npm as the two separate scripting/support foundations and Syft, `uv` and Spec Kit as additional tools without inflating the six-MSL count in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T044 [US4] Reconcile Codex, Claude Code, Antigravity CLI and GitHub Copilot CLI as four required agents plus OpenCode and Gemini CLI as two additional surfaces across installation, pin, version check, state, dispatcher, provider/sign-in and documentation category in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T045 [P] [US4] Run `python3 scripts/tests/test_agent_prompt_dispatchers.py`, capture the observed six-surface dispatcher result, and map every mismatch to one gap in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T046 [P] [US4] Run Q13, Q14 and Q15, then reconcile all twelve installed presets by ID, version, priority, enabled state, effective resolution and CL coverage as eight binding plus four additional presets in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json`
- [x] T047 [US4] Run Q17 only when the Compose service and intended endpoint are available; otherwise record the exact environment blocker, owner and retry trigger as `Open` rather than Pass or Fail in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T048 [US4] Project every inventory item exactly once as a `### INV-*` section with target claim, every separate observation, reconciliation status and gap in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/inventory-reconciliation.md`
- [x] T049 [US4] Run Q12, Q16 and the inventory part of Q11, require exact 6/2/4/2/8/4 counts, at least three supporting tools, complete dimensions and reciprocal gap mappings, and record the outcome in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T050 [US4] Record macOS evidence and mark every unavailable Linux, Windows/WSL2, Podman, network or provider observation `Open` with owner and retry trigger in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/inventory-reconciliation.md`

**Checkpoint**: All four user stories are independently reviewable and the
canonical JSON remains the source of every Markdown projection.

---

## Final Phase: Cross-Cutting Validation, Delivery and Closeout

**Purpose**: Prove learner accessibility, governance dispositions, exact
scope, technical ReviewPending completion and the authorized MergeAndSync
closeout without crossing Human-only or next-intake boundaries.

- [x] T051 Run Q18 on all four assessment Markdown files and Q20 on repository Markdown, resolve only assessment-owned findings, and record warnings, commands and results in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T052 Perform and record the complete manual GSDB-neutrality, DE-first/EN-second, CEFR-B2, first-use-term, semantic-heading, descriptive-link and text-first review with no company-policy/internal-management-system wording and all four editorial error counters at zero in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/evidence-matrix.md`
- [x] T053 Run Q19 and bind the valid `UpdateRequired` Documentation Impact decision to its current hash in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T054 Record NIST SSDF and CWE Top 25 as applicable assessment lenses; OWASP ASVS, new threat model/ADR/S-ADR/arc42, BSI C3A/C5, new Zero Trust/SAMM and separate regulatory files as justified feature-implementation `N/A`; and existing architecture/security/regulatory evidence as assessed inventory in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/evidence-matrix.md`
- [x] T055 Record SBOM, VEX and SLSA as applicable existing-image assessment areas, new AI-SBOM as `N/A` because AI is development tooling only, existing CL-05-13/CL-09-15 AI transparency as applicable, and every trigger-aware missing artefact as a gap in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/prioritized-gap-list.md`
- [x] T056 Record cross-platform script-pair/manpage/Cmdlet work and shared agent-guidance/template/constitution edits as implementation `N/A`, while assessing existing parity and naming the exact re-evaluation triggers in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/inventory-reconciliation.md`
- [x] T057 Run Q21 read-only, capture Profile-2 drift as an assessment observation or gap, and prove that `docs/project-statistics.md` and `docs/project-statistics.config.json` remain unchanged in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T058 Run Q22, prove the current GSDB series root remains the only eligible/active target, and record that `AcceptedBaseline -> separately authorized intake-series update -> series status -> read-only next-candidate listing` is a future chain not executed by this feature in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/README.md`
- [x] T059 Run Q12 and Q25, using `podman-compose config` only as the documentation/static validator required by the reviewed gate; do not build, start, stop or change the Compose runtime, and record platform skips honestly in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T060 Re-run Q03, Q07 through Q20, Q21, Q22 and every triggered validator from T008, require every applicable gate to Pass, all twelve binding checklist counts and every recomputed summary set to match detail, every `N/A` gate to be `Skipped` with rationale/trigger, set only `ReviewPending`, and finalize current hashes and zero error counters in `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/validation-results.json`
- [x] T061 Create the current implementation-session record with completed, partial, skipped and escalated Compliance-Plan/task IDs, no prompt/response/secret content, and the next exact action in a concrete timestamped file under `docs/security/agent-session-log/`
- [x] T062 Update technical implementation boxes only after their cited proof passes, while leaving Human-only acceptance and next-intake advancement visibly incomplete in `specs/002-gsdb-baseline-assessment/checklists/autonomous-readiness.md`
- [x] T063 Run Q23 with the exact feature paths from `quickstart.md` plus every dynamically discovered and individually inventoried sanitized feature-session-log path, reject unrelated/runtime logs and `AEI004`, and record the passing intended delivery set in `specs/002-gsdb-baseline-assessment/autonomous-run-evidence.md`
- [x] T064 Stage only the Q24 allowlist, verify all intended paths and no prohibited/statistics/runtime/private-host path or unsanitized content with Q24, run `git diff --cached --check`, preserve unrelated changes, and create exactly one assessment content commit containing `specs/002-gsdb-baseline-assessment/`, `.specify/feature.json`, the seven dated assessment outputs and explicitly inventoried sanitized session logs
- [ ] T065 Push only branch `002-gsdb-baseline-assessment`, create or update its pull request, and record PR URL, exact head and delivery authority in `specs/002-gsdb-baseline-assessment/autonomous-run-evidence.md`; no statistics commit is part of this feature, and any later Profile-2 render requires a separate post-feature trigger and authority
- [ ] T066 Converge required current-head checks, Code Owner/security review and actionable threads, map each required gate to actual workflow/job/runner/command evidence, create temporary schema-2.0 `/tmp/002-gsdb-baseline-assessment.pre-merge.json`, and require Q26 to pass for the exact content head before any merge
- [ ] T067 Reconfirm current MergeAndSync authority and use the narrowly authorized admin bypass only for the concrete PR and nontechnical policy after T066 passes; never bypass a failed technical gate, missing review, conflict, wrong head or secret finding, and record authorizer/scope/reason/residual risk in `specs/002-gsdb-baseline-assessment/autonomous-run-evidence.md`
- [ ] T068 Verify the actual remote merge commit, fetch `origin`, fast-forward local `main` with `git switch main && git merge --ff-only origin/main`, create temporary causal `/tmp/002-gsdb-baseline-assessment.post-merge.json` with empty `changedPaths`, run Q27 and Q28, mark schema-1.1 MergeAndSync closeout fields terminal, and leave `AcceptedBaseline`, series transition, Lastenheft rename and next-intake start unperformed in `specs/002-gsdb-baseline-assessment/autonomous-run-state.json` and `specs/002-gsdb-baseline-assessment/autonomous-run-evidence.md`

---

## Dependencies and Execution Order

### Phase Dependencies

- Phase 1 has no task dependency but requires the routed post-tasks Analyze
  phase to be completed by orchestration before implementation begins.
- Phase 2 depends on T001-T008 and blocks all user stories.
- US1 depends on T009-T013 and is the MVP.
- US2 depends on the US1 canonical source/row set.
- US3 depends on final US1/US2 statuses and evidence.
- US4 depends on the canonical JSON shape but is independently reviewable from
  US3 until final gap reconciliation.
- Final validation depends on T014-T050. Remote delivery is strictly serialized
  as T063 -> T064 -> T065 -> T066 -> T067 -> T068.

### User Story Dependencies

- **US1 (P1)**: No dependency on another story after Foundation; establishes
  the source and row identity contract used by all later stories.
- **US2 (P1)**: Depends on US1 IDs and sources; independently proves evidence,
  Human-only boundaries and twelve-item traceability.
- **US3 (P2)**: Depends on final row statuses from US1/US2; independently proves
  exact reciprocal gap coverage.
- **US4 (P2)**: Depends on the shared JSON contract; its source collection can
  proceed after US1, but final mismatch gaps depend on US3 reconciliation.

### Parallel Opportunities

- After T016, evidence discovery for T025 and inventory source collection for
  T042-T046 may run in parallel as read-only work; writes to
  `assessment-results.json` remain serialized.
- T051, T053 and the read-only part of T057 may run in parallel after all
  Markdown/JSON projections are stable, but their results are serialized into
  `validation-results.json` by T060.
- No Git, gate-evidence, statistics, run-state, session-log, shared JSON or
  remote task is parallelized.

### Parallel Execution Examples per Story

- **US1**: After T020, run T021 and T022 concurrently; one writes canonical
  summary counters and the other writes the Markdown matrix projection. Join
  both before T023.
- **US2**: After T027, run T028 and T029 concurrently against the same stable
  canonical row set; join both before T030.
- **US3**: After T036, T039 may document the non-authorizing handoff in the
  README while T037-T038 serialize canonical gap and projection work; join
  before T040.
- **US4**: After T044, run T045 and T046 concurrently because dispatcher proof
  and preset reconciliation write different outputs; join before T047-T049.

## Implementation Strategy

### MVP First

1. Complete T001-T013 and stop on any binding or gate drift.
2. Complete T014-T019 to prove the red/green `CL-12-05` vertical slice.
3. Complete T020-T024 for exact 37/12/157 coverage.
4. Run the US1 independent test before continuing.

### Incremental Delivery

1. Add traceable evidence and Human-only boundaries through US2.
2. Derive the exact prioritised gap handoff through US3.
3. Reconcile toolchains, agents, supporting tools, presets and platforms
   through US4.
4. Complete all local gates and `ReviewPending` evidence.
5. Deliver one content commit, converge current-head review, and perform the
   authorized MergeAndSync closeout.

## Post-Tasks Analyze Convergence

**DE:** Der finale Analyze-Lauf hat alle 68 eindeutigen, fortlaufenden Tasks
gegen 27 funktionale Anforderungseintraege (einschliesslich `FR-010a` und
`FR-010b`), zehn Erfolgskriterien, vier User Stories, 18 Governance-
Anforderungen und 13 Gates geprueft. Die Zuordnung ist vollstaendig: Setup und
Foundation `T001-T013`, US1 `T014-T024`, US2 `T025-T035`, US3 `T036-T041`, US4
`T042-T050` sowie Gate-/Delivery-Closeout `T051-T068`. / **EN:** Final Analyze
reviewed all 68 unique sequential tasks against 27 functional requirement
entries, ten success criteria, four user stories, 18 governance requirements,
and 13 gates. Coverage is complete across the stated task ranges.

| Coverage surface | Task evidence |
|---|---|
| `FR-001`-`FR-003`, `FR-011`, `FR-012` | `T002`, `T014`, `T024-T026`, `T052`, `T058` bind accepted inputs, all 37 sources, GSDB-neutral wording, source versions and evidence catalogues. |
| `FR-004`-`FR-010b`, `FR-021`, `FR-022`, `FR-025` | `T009-T023`, `T026-T035`, `T041`, `T052`, `T060` cover 157 rows, all closed status/role/risk/trigger vocabularies, projections, text summaries and lifecycle states. |
| `FR-013`-`FR-017` | `T042-T050` cover source-version, runtime, registry, dispatcher, 6/2/4/2/8/4 inventory and mismatch reconciliation. |
| `FR-018`-`FR-020` | `T036-T041` cover stable priorities, complete gap fields and reciprocal row/source/inventory mappings. |
| `FR-023`, `FR-024` | `T006-T008`, `T039`, `T057-T068` enforce the assessment-only firewall, accepted-baseline/series boundary and no next-intake implementation. |
| `SC-001`-`SC-004`, `SC-006`, `SC-007` | `T015-T035`, `T040` supply exact checklist/ID counts, field/status/evidence rules, gap coverage and Human-only openness. |
| `SC-005`, `SC-008`, `SC-009`, `SC-010` | `T042-T052`, `T057-T068` supply exact inventory, twelve timed samples, bilingual/A11Y proof and zero scope violations. |
| User Stories 1-4 | `T014-T024`, `T025-T035`, `T036-T041`, `T042-T050`; each story retains its own independent test and checkpoint. |
| `CR-001`-`CR-018` | `T001-T008`, `T012`, `T042-T058`, `T060-T068` cover project context, standards, A11Y, bilingual delivery, inventory, statistics read-only, documentation impact and autonomous integrity. |
| 13 gates and 68 tasks | `T004`, `T011`, `T060` require one result for every unique gate; `T001-T068` are unique, sequential and dependency ordered, with remote closeout serialized as `T063 -> T068`. |

| ID | Schwere / Severity | Befund / Finding | Vollstaendige Disposition / Complete disposition |
|---|---|---|---|
| `AN-001` | High | Gesamt-157 und Schemagueltigkeit prueften die zwoelf bindenden Einzelzahlen sowie alle Summary-Sets nicht vollstaendig gegen Detailobjekte. / Total 157 and schema validity did not fully prove all twelve binding counts and summary sets against details. | Behoben in Schema, Datenmodell, Vertrag, Q08/Q09 und `T021`/`T023`/`T060`; die Einzelzahlen und geschlossenen Count-Namen werden strukturell und semantisch neu berechnet. / Resolved through structural and semantic recomputation. |
| `AN-002` | Medium | Die statische Sitzungslogliste war phasenbedingt veraltet; private Hostpfade in Freitext waren nicht explizit Teil der Lieferpruefung. / The static session-log list had become stale, and private host paths in free text were not explicitly delivery-checked. | Behoben durch dynamische Inventarisierung in `T006`/Q23 und `privatePathPatterns` in Vertrag, Q24, Gate-Anforderung sowie `T063-T064`; Secret-Scan bleibt zusaetzlich Pflicht. / Resolved by dynamic inventory, explicit private-path checks, and the existing secret scan. |
| `AN-003` | Medium | Die bindende Lastenheft-Archivierung darf weder die aktuelle Eingangsbindung noch die gesperrte Serie vor `AcceptedBaseline` brechen. / Mandatory requirements-document archival must not break the current accepted input or blocked series before AcceptedBaseline. | Vollstaendig zeitlich disponiert: aktueller Assessment- und Merge-Lauf endet fachlich `ReviewPending`; Owner `Repository Maintainer`; Trigger sind dokumentierte `AcceptedBaseline`, separat autorisiertes Serienupdate und eigener Closeout. Erst dann darf `rename-lastenheft.*` laufen; der naechste Intake wird dadurch nicht implementiert. / Fully time-disposed to the explicit human acceptance, series-update, and separate-closeout trigger without implementing the next intake. |
| `AN-004` | High | `autonomous-delivery-integrity` verlangte `validate-autonomous-phase-result.sh`, waehrend Q04 nur die PowerShell-Variante ausführte. / The gate required the Bash phase-result validator while Q04 executed only PowerShell. | Behoben ohne neuen Task: Q04 und `T003` fuehren beide vorhandenen Varianten gegen dieselbe letzte abgeschlossene Phase aus; spaetere Gate-Evidenz kann den geforderten Bash-Token und Cross-Shell-Paritaet belegen. / Resolved by executing both variants against the same phase. |
| `AN-005` | Medium | Die vorhandene Bilingualitaetsheuristik erkannte in `tasks.md` und beiden Checklisten keinen passenden DE-/EN-Zweckabschnitt. / The existing bilingual heuristic found no matching German/English purpose section in tasks and both checklists. | Behoben durch explizite `Zweck / Purpose`-Abschnitte; die Anforderungen-Checkliste bleibt itemweise bilingual, und die Readiness-Checkliste wurde vollstaendig DE-first/EN-second formuliert. / Resolved with explicit purpose sections and a fully bilingual readiness checklist. |

Es verbleibt kein Critical- oder High-Befund und kein Medium ohne Owner, Trigger
und vollstaendige Disposition. / No Critical or High finding remains, and no
Medium lacks an owner, trigger, and complete disposition.

## Explicit Deferred and Prohibited Work

- `AcceptedBaseline` is a later documented human decision by `Project Owner`
  and `Security Review`; technical completion and merge do not grant it.
- Series advancement is not a task in this feature. Only after
  `AcceptedBaseline` and fresh authority may a separate workflow run
  `/speckit-intake-series-update`, validate series status, and list the next
  candidate read-only. This feature does not make the next intake Eligible.
- A statistics render commit is not a task in this feature. T057 is read-only;
  any later triggered Profile-2 commit requires separate post-feature authority
  and must contain only renderer-approved statistics paths.
- The Lastenheft rename is `N/A` here because the accepted input hash and series
  root bind its current path. Re-evaluate only after human acceptance, series
  update and separately authorized closeout; `Repository Maintainer` owns that
  mandatory final archival action via `rename-lastenheft.*`.
- No Dockerfile, Compose/runtime, provider/secret, platform-rule, formal
  approval, external-register or hardening change is permitted.
