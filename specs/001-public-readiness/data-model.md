# Data Model: Sandbox Public Readiness

This feature has no runtime database. The model below defines the review and
evidence entities used to plan documentation changes and acceptance checks.

## Public-Readiness Surface

**Purpose**: A repository file or document group that a public reader, trainer,
maintainer, or reviewer may use to understand setup, security, governance, or
training workflow.

**Fields**:

- `path`: Repository-relative path or document group.
- `surface_type`: One of `user-facing`, `agent-guidance`, `security-evidence`,
  `lastenheft`, `spec-kit-artifact`, or `operational-policy`.
- `audience`: Public reader, apprentice, trainer, maintainer, reviewer, or
  operator.
- `language_mode`: German only, English only, bilingual, or surrounding-context
  dependent.
- `public_readiness_status`: `candidate`, `reviewed`, `updated`, `verified`,
  or `deferred`.
- `required_action`: `genericize`, `classify-evidence`, `preserve`, `defer`,
  or `document-deviation`.

**Validation rules**:

- User-facing and agent-guidance surfaces must not require private host paths,
  private URLs, private accounts, organization-only services, or account-bound
  defaults.
- Bilingual surrounding context must remain bilingual unless a deviation is
  documented.
- Security intent must not be weakened when wording is generalized.

## Private Assumption

**Purpose**: A context-bound statement that cannot be required of public
readers without explanation or replacement.

**Fields**:

- `source_path`: Repository-relative file path.
- `source_reference`: Heading, line reference, or search term used by review.
- `assumption_type`: `private-path`, `private-url`, `organization-role`,
  `non-public-service`, `account-default`, `provider-status`, `legal-status`,
  or `approval-status`.
- `visibility_risk`: `public-confusion`, `oversharing`, `overclaiming`,
  `audit-loss`, or `none`.
- `resolution`: `remove`, `genericize`, `mark-context`, `mark-example`,
  `mark-not-public-release-relevant`, `mark-open`, `mark-na`, or `mark-todo`.
- `rationale`: Short reason for the selected resolution.
- `owner`: Responsible role when follow-up is needed.
- `re_evaluation_trigger`: Event that causes the item to be reviewed again.

**Validation rules**:

- User-facing and agent-guidance instances must resolve to `remove` or
  `genericize` unless an intentional deviation is recorded.
- Security/audit evidence may use context/example/not-public-release-relevant
  markings when auditability would otherwise be lost.
- Missing approval, provider, model, legal, licensing, or platform decisions
  must not be inferred.

## Evidence Classification

**Purpose**: The status assigned to a security, compliance, release, provider,
or governance statement.

**Fields**:

- `statement`: Short description of the evidence item.
- `classification`: `active-evidence`, `context-evidence`,
  `example-evidence`, `open`, `na`, `todo`, or
  `not-public-release-relevant`.
- `rationale`: Why this classification is correct.
- `evidence_path`: Existing or planned Markdown evidence path.
- `owner`: Required for `open` and `todo`.
- `follow_up`: Required next action for `open` and `todo`.
- `re_evaluation_trigger`: Date, release event, provider decision, legal
  review, platform change, or public-release decision.

**Validation rules**:

- `open` and `todo` require owner, follow-up, and re-evaluation trigger.
- `na` requires a short rationale.
- `context-evidence` and `not-public-release-relevant` require a rationale
  explaining why the statement remains useful for audit or history without
  becoming a reusable public release claim.
- `active-evidence` must point to an existing evidence path or a task that will
  create one.

## Maintained Agent Surface

**Purpose**: A shared AI-agent guidance file that must remain aligned when
public-readiness wording changes.

**Fields**:

- `path`: One of `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or
  `.github/copilot-instructions.md`.
- `agent_surface`: Codex/Codex-like, Claude, Gemini, or GitHub Copilot.
- `shared_rule_area`: Setup commands, testing guidance, security guidance,
  model-routing guidance, or public-readiness wording.
- `parity_status`: `aligned`, `updated`, `intentional-deviation`, or
  `not-affected`.
- `deviation_reason`: Required when `parity_status` is
  `intentional-deviation`.

**Validation rules**:

- Shared operational rules must be updated atomically across all maintained
  agent surfaces.
- Any intentional deviation must be explicit in the same change.

## Public-Readiness Review Checkpoint

**Purpose**: A repeatable review step that proves the implementation meets the
feature success criteria.

**Fields**:

- `checkpoint_name`: Human-readable review name.
- `scope`: Files or document group covered.
- `method`: Manual review, `rg` search, Markdown check, Compose config parse,
  or evidence review.
- `command`: Optional command when the method is automated.
- `expected_result`: Observable pass condition.
- `residual_risk`: Remaining risk after the checkpoint.

**Validation rules**:

- Every success criterion must map to at least one checkpoint.
- Checks that depend on a local platform, Podman machine, network, or owner
  decision must record skipped status and reason when unavailable.

## State Transitions

```text
Public-Readiness Surface:
candidate -> reviewed -> updated -> verified
candidate -> reviewed -> deferred

Private Assumption:
found -> classified -> resolved -> verified
found -> classified -> open-follow-up

Evidence Classification:
unclassified -> active-evidence
unclassified -> context-evidence
unclassified -> example-evidence
unclassified -> open
unclassified -> na
unclassified -> todo
unclassified -> not-public-release-relevant

Maintained Agent Surface:
not-affected -> aligned
aligned -> updated -> verified
aligned -> intentional-deviation
```

## Relationships

- A Public-Readiness Surface may contain zero or more Private Assumptions.
- A Private Assumption resolves to exactly one Evidence Classification or a
  wording change.
- A Maintained Agent Surface is a specialized Public-Readiness Surface.
- A Public-Readiness Review Checkpoint verifies one or more Success Criteria
  from `spec.md`.
