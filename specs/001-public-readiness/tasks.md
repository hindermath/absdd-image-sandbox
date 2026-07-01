# Tasks: Sandbox Public Readiness

**Input**: Design documents from `specs/001-public-readiness/`
**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `quickstart.md`
**Tests**: No code, runtime, container, or TDD test tasks are included. This
feature uses documentation review and validation tasks only.

**Organization**: Tasks are grouped by user story to enable independent
implementation and review. US1 is the MVP.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel because it touches different files and does not
  depend on incomplete tasks.
- **[Story]**: Maps to the user story from `spec.md`.
- Every task names concrete files or file groups.

## Phase 1: Setup

**Purpose**: Establish the review artefacts and scope boundaries for the
Public-Readiness implementation.

- [ ] T001 Review the current feature context in `specs/001-public-readiness/spec.md`, `specs/001-public-readiness/plan.md`, `specs/001-public-readiness/research.md`, `specs/001-public-readiness/data-model.md`, and `specs/001-public-readiness/quickstart.md`
- [ ] T002 Create the public-readiness surface inventory in `specs/001-public-readiness/public-readiness-surface-inventory.md`
- [ ] T003 [P] Create the public-readiness checkpoint mapping in `specs/001-public-readiness/public-readiness-checkpoints.md`
- [ ] T004 [P] Create the agent parity review artefact in `specs/001-public-readiness/agent-parity-review.md`
- [ ] T005 [P] Create the evidence classification artefact in `docs/security/public-readiness-evidence.md`

---

## Phase 2: Foundational

**Purpose**: Complete blocking discovery and applicability classification
before any user-story-specific edits begin.

**Checkpoint**: No user-story work starts until private assumptions,
evidence-status categories, and governance applicability have initial entries.

- [ ] T006 Populate `specs/001-public-readiness/public-readiness-surface-inventory.md` with `README.md`, `opencode.env.example`, `compose.yml`, `compose.home-baseline.yml`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `COMPLIANCE-PLAN_RL-SE-001.md`, `docs/security/`, `Lastenheft_*.md`, and `specs/001-public-readiness/`
- [ ] T007 Record initial private-assumption findings for user-facing and configuration guidance in `specs/001-public-readiness/public-readiness-surface-inventory.md`
- [ ] T008 [P] Record initial private-assumption findings for maintained agent guidance in `specs/001-public-readiness/agent-parity-review.md`
- [ ] T009 [P] Record initial security and audit evidence classifications in `docs/security/public-readiness-evidence.md`
- [ ] T010 Record governance applicability for Security, Architecture, iSAQB, A11Y, Cross-Platform, and Agent Parity checkpoints in `specs/001-public-readiness/public-readiness-checkpoints.md`
- [ ] T011 Add `Open`, `N/A`, `_TODO_`, context, example, and not-public-release-relevant evidence handling rules to `docs/security/public-readiness-evidence.md`

---

## Phase 3: User Story 1 - Public Training Reader Understands the Sandbox (Priority: P1) MVP

**Goal**: A public Fachinformatik apprentice or trainer can understand the
sandbox purpose, setup boundaries, non-goals, and evidence-status language
without private organizational context.

**Independent Review**: A clean reader can use `README.md` and linked setup,
security, Lastenheft, and agent-guidance entry points to identify purpose,
non-goals, optional home-baseline usage, and public-readiness status in under
10 minutes.

- [ ] T012 [US1] Update the public-facing sandbox purpose, audience, and non-production boundaries in `README.md`
- [ ] T013 [US1] Update the optional `home-baseline` setup explanation and public-template flow in `README.md`
- [ ] T014 [P] [US1] Update public provider and secret-handling wording in `opencode.env.example`
- [ ] T015 [P] [US1] Update reusable setup and comment wording in `compose.yml`
- [ ] T016 [P] [US1] Update optional home-baseline override wording in `compose.home-baseline.yml`
- [ ] T017 [US1] Review learner-facing `Lastenheft_*.md` wording for public-reader clarity and record required edits in `specs/001-public-readiness/public-readiness-surface-inventory.md`
- [ ] T018 [US1] Record the SC-004 clean-reader review result in `specs/001-public-readiness/public-readiness-checkpoints.md`

---

## Phase 4: User Story 2 - Maintainer Neutralizes Private Assumptions (Priority: P2)

**Goal**: Maintainers can replace private or organization-bound assumptions
with generic wording while preserving security intent and auditability.

**Independent Review**: Public-readiness surfaces contain no mandatory private
host path, private URL, private account, organization-only service, or
account-bound default unless the item is explicitly classified as context,
example, not-public-release-relevant evidence, `Open`, `N/A`, or `_TODO_`.

- [ ] T019 [US2] Neutralize private paths, private URLs, account-specific defaults, and non-public provider assumptions in `README.md`
- [ ] T020 [P] [US2] Neutralize private or account-specific defaults in `opencode.env.example`
- [ ] T021 [P] [US2] Neutralize private host-path and account-specific assumptions in `compose.yml` and `compose.home-baseline.yml`
- [ ] T022 [US2] Update shared public-readiness wording atomically across `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md`
- [ ] T023 [US2] Generalize user-facing organization-specific language in `Lastenheft_*.md`
- [ ] T024 [US2] Update `COMPLIANCE-PLAN_RL-SE-001.md` so reusable guidance is generic while security control objectives remain unchanged
- [ ] T025 [P] [US2] Update `docs/security/` evidence wording so organization-specific origin is classified instead of required from public readers
- [ ] T026 [US2] Update `specs/001-public-readiness/spec.md`, `specs/001-public-readiness/plan.md`, `specs/001-public-readiness/research.md`, `specs/001-public-readiness/data-model.md`, and `specs/001-public-readiness/quickstart.md` if public-readiness wording has drifted
- [ ] T027 [US2] Record each resolved private assumption and rationale in `specs/001-public-readiness/public-readiness-surface-inventory.md`

---

## Phase 5: User Story 3 - Reviewer Verifies Evidence and Boundaries (Priority: P3)

**Goal**: Reviewers can verify that the repository does not overclaim security,
legal, provider, release, SBOM, VEX, SLSA, AI-SBOM, or public-readiness status.

**Independent Review**: Every unresolved approval, provider, model, legal,
licensing, data-residency, platform, release, SBOM, VEX, SLSA, or AI-SBOM item
is marked as `Open`, `N/A`, or `_TODO_` with rationale and follow-up data where
applicable.

- [ ] T028 [US3] Classify active evidence, context evidence, example evidence, not-public-release-relevant evidence, `Open`, `N/A`, and `_TODO_` entries in `docs/security/public-readiness-evidence.md`
- [ ] T029 [US3] Add owner, follow-up, and re-evaluation trigger fields for each `Open` or `_TODO_` item in `docs/security/public-readiness-evidence.md`
- [ ] T030 [US3] Add short rationales for each `N/A` and not-public-release-relevant item in `docs/security/public-readiness-evidence.md`
- [ ] T031 [US3] Record no-overclaim review results for `COMPLIANCE-PLAN_RL-SE-001.md` and `docs/security/` in `specs/001-public-readiness/public-readiness-checkpoints.md`
- [ ] T032 [US3] Record agent guidance parity results and any intentional deviations in `specs/001-public-readiness/agent-parity-review.md`
- [ ] T033 [US3] Map SC-001 through SC-006 to concrete evidence paths in `specs/001-public-readiness/public-readiness-checkpoints.md`

---

## Final Phase: Validation And Handover

**Purpose**: Validate documentation quality, Compose syntax, scope boundaries,
and later implementation-session evidence.

- [ ] T034 Run `git diff --check` and record the result in `specs/001-public-readiness/public-readiness-checkpoints.md`
- [ ] T035 Run the private-path and private-URL `rg` searches from `specs/001-public-readiness/quickstart.md` and record findings or clean result in `specs/001-public-readiness/public-readiness-checkpoints.md`
- [ ] T036 Run the status-overclaim `rg` searches from `specs/001-public-readiness/quickstart.md` and record findings or clean result in `specs/001-public-readiness/public-readiness-checkpoints.md`
- [ ] T037 Run `podman-compose config` and record the result in `specs/001-public-readiness/public-readiness-checkpoints.md`
- [ ] T038 Run `HOME_BASELINE_DIR=/path/to/home-baseline-tmp podman-compose -f compose.yml -f compose.home-baseline.yml config` only if `compose.home-baseline.yml` or the home-baseline workflow changed, then record pass, skip, or failure reason in `specs/001-public-readiness/public-readiness-checkpoints.md`
- [ ] T039 Confirm that no container build, container start, repository visibility change, secret rotation, provider/model configuration, formal approval, platform branch-protection configuration, external register entry, or RL-SE-/Checklist self-assessment was performed, and record the result in `specs/001-public-readiness/public-readiness-checkpoints.md`
- [ ] T040 Add the implementation-session summary for completed, partial, skipped, and escalated Public-Readiness tasks in `docs/security/agent-session-log/<YYYY-MM-DD-HHMM>.md`

---

## Dependencies And Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Phase 1 and blocks all user stories.
- **US1 (Phase 3)**: Starts after Foundational and is the MVP.
- **US2 (Phase 4)**: Starts after Foundational; can run after or alongside US1 when file conflicts are coordinated.
- **US3 (Phase 5)**: Starts after Foundational; final evidence mapping depends on US1 and US2 edits.
- **Validation And Handover**: Runs after selected user stories are complete.

### User Story Dependencies

- **US1 (P1)**: No dependency on US2 or US3 after Foundational.
- **US2 (P2)**: No functional dependency on US1, but shared files such as `README.md` and agent guidance require sequencing to avoid edit conflicts.
- **US3 (P3)**: Depends on the evidence and wording results from US1 and US2 for final checkpoint mapping.

### Parallel Opportunities

- T003, T004, and T005 can run in parallel after T001.
- T008 and T009 can run in parallel with T007 after T006.
- T014, T015, and T016 can run in parallel in US1.
- T020, T021, and T025 can run in parallel in US2 because they touch different surfaces.

## Implementation Strategy

### MVP First

1. Complete Phase 1 and Phase 2.
2. Complete US1 tasks T012 through T018.
3. Run the relevant validation tasks T034 through T037.
4. Stop before broader neutralization if the MVP needs review.

### Incremental Delivery

1. Complete setup and foundational review artefacts.
2. Deliver US1 for public-reader clarity.
3. Deliver US2 for private-assumption neutralization.
4. Deliver US3 for evidence and overclaim verification.
5. Complete validation and handover tasks.

## Non-Goals For This Task List

- No RL-SE-/Checklist self-assessment is planned.
- No new feature specification is generated.
- No implementation starts during task generation.
- No container is built or started.
- Repository visibility is not changed.
- No secrets are rotated.
- No provider or model access is configured.
- No formal approval is invented.
- No platform branch protection is configured.
- No external register entry is marked complete.
- No commit or push is performed by task generation.
