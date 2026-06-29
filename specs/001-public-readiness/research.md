# Research: Sandbox Public Readiness

## Decision: Documentation/governance feature only

**Rationale**: The feature specification explicitly limits the work to public
readiness wording, evidence classification, and reader guidance. It forbids
container builds, repository visibility changes, secret rotation, provider
configuration, and model access changes.

**Alternatives considered**:

- Build or rebuild the sandbox image: rejected because this would exceed the
  planning scope and create release evidence the feature is not allowed to
  claim.
- Change runtime configuration: rejected because public readiness is a
  documentation and governance concern here.

## Decision: Split public wording from audit-evidence origin

**Rationale**: The accepted clarification from 2026-06-28 requires
user-facing and agent-guidance surfaces to use generic wording, while
security/audit evidence may retain organization-specific origin when it is
explicitly marked as context, example, or not-public-release-relevant evidence.
This preserves auditability without forcing public readers to depend on private
context.

**Alternatives considered**:

- Remove all organization-specific wording everywhere: rejected because it
  could weaken audit traceability.
- Keep organization-specific wording everywhere with explanations: rejected
  because it would keep public-facing guidance tied to non-public context.

## Decision: Use explicit evidence classifications

**Rationale**: The specification requires unresolved approval, provider, model,
data-residency, licensing, legal, and platform decisions to remain visible as
`Open`, `N/A`, or `_TODO_` with rationale. Security evidence also needs clear
classification as active evidence, example evidence, unresolved follow-up, or
non-applicable control.

**Alternatives considered**:

- Omit uncertain evidence fields: rejected because omission hides risk and
  weakens reviewability.
- Infer missing approval or provider status: rejected because it would
  overclaim readiness.

## Decision: Treat governance standards by applicability, not by omission

**Rationale**: The constitution requires applicability decisions for security,
architecture, accessibility, cross-platform, and agent-parity checkpoints.
For this documentation-only feature, NIST SSDF and CWE remain applicable as
secure-development review lenses; OWASP ASVS, BSI C3A/C5, cross-platform
script work, and runtime architecture changes are N/A with rationale.

**Alternatives considered**:

- Mark all code-oriented standards as N/A: rejected because the constitution
  keeps NIST SSDF and CWE in scope for Level-2 work even when no code changes.
- Generate full runtime security artefacts: rejected because no runtime
  boundary or deployment changes are planned.

## Decision: No contracts artefact

**Rationale**: The feature has no API, CLI command schema, service endpoint,
file exchange protocol, parser grammar, UI flow contract, or public runtime
interface. Creating `contracts/` would imply a non-existent integration
surface.

**Alternatives considered**:

- Create a Markdown review contract: rejected because the data model and
  quickstart already define the review entities and validation flow.
- Create placeholder contracts: rejected because placeholders reduce Spec-Kit
  artefact quality.

## Decision: Data model covers review and evidence entities

**Rationale**: Although there is no application data model, implementation
tasks need consistent terms for files, private assumptions, evidence status,
agent surfaces, and review checkpoints. These entities make task generation
and acceptance checks concrete without inventing runtime storage.

**Alternatives considered**:

- Omit `data-model.md`: rejected because Spec Kit planning expects design
  entities where the spec defines review objects.
- Model repository files as code modules: rejected because this is a
  documentation workflow, not a software architecture change.

## Decision: `podman-compose config` is the blocking Compose validation

**Rationale**: Repository guidance now treats `podman-compose config` as the
standard static Compose parse. It validates `compose.yml` without requiring a
running Podman machine and avoids treating local socket failures as repository
content failures.

**Alternatives considered**:

- Use `podman compose config` as the blocking check: rejected because this
  host currently fails against a local Podman socket even for config-only
  validation.
- Skip Compose validation: rejected because documentation changes may affect
  copy-and-paste setup commands.

## Decision: Validate with text scans and Markdown checks

**Rationale**: The feature's risk is wording drift, hidden private assumptions,
and overclaiming. `rg` scans, `git diff --check`, and review against the data
model directly target those risks.

**Alternatives considered**:

- Add a new scanner script: rejected because the feature explicitly avoids
  implementing new tooling and cross-platform script obligations.
- Use only manual review: rejected because targeted text searches provide
  repeatable evidence for common public-readiness failures.

## Decision: Agent parity is an implementation work group

**Rationale**: The maintained agent surfaces are `AGENTS.md`, `CLAUDE.md`,
`GEMINI.md`, and `.github/copilot-instructions.md`. Shared wording must be
updated atomically or deviations must be recorded. No Spec-Kit marker block
currently exists in `AGENTS.md`, so the plan does not invent one.

**Alternatives considered**:

- Update only `AGENTS.md`: rejected because it violates agent parity.
- Add new Spec-Kit marker blocks: rejected because the repository does not
  currently use that mechanism.
