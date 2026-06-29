# Implementation Plan: Sandbox Public Readiness

**Branch**: `001-public-readiness` | **Date**: 2026-06-29 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/001-public-readiness/spec.md`

**Note**: This plan is the `/speckit-plan` output for a documentation and
governance feature. It plans the implementation work only; it does not start
the public-readiness edits.

## Summary

Plan the Public-Readiness implementation for `absdd-image-sandbox` as a
training sandbox. The implementation will convert user-facing and maintained
agent guidance to generic public wording, preserve security intent, and keep
security/audit evidence auditable through explicit `Open`, `N/A`, `_TODO_`,
context, example, or not-public-release-relevant classifications.

The technical approach is repository documentation review and evidence
classification. No runtime code, API, database, image build, provider setup,
secret rotation, formal approval, or repository visibility change is part of
this feature.

## Technical Context

**Language/Version**: N/A. This feature changes Markdown documentation and
Spec-Kit planning artefacts only; no implementation language is introduced.
**Primary Dependencies**: N/A for runtime. Planning uses existing repository
Markdown files, Spec Kit artefacts, `rg`, Git, and Podman Compose validation.
**Storage**: Git-tracked Markdown files in the repository.
**Testing**: `git diff --check`, targeted `rg` scans, `podman-compose config`,
and optional home-baseline Compose override validation.
**Target Platform**: Repository documentation consumed from macOS,
Windows/WSL2, and Linux; the sandbox runtime remains Podman-based.
**Project Type**: Documentation/governance feature for a container training
repository.
**Performance Goals**: A new reader can identify sandbox purpose, non-goals,
and public-readiness status from primary documentation in under 10 minutes.
**Constraints**: No container build, no repository visibility change, no
secret rotation, no provider/model configuration, no invented formal approval,
and no platform branch-protection configuration.
**Scale/Scope**: README, maintained agent guidance, compliance plan,
`docs/security/`, existing Lastenhefte, and current Spec-Kit artefacts.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Governance area | Status | Planning decision |
|---|---|---|
| Security-first | PASS | No secrets are added; local secret files stay gitignored; validation includes text scans for private paths, URLs, and overclaims. |
| Memory-safe language | N/A | No runtime code or primary implementation language is introduced. |
| NIST SSDF | Applicable | Plan explicit evidence classification and secure-development wording review. |
| CWE Top 25 | Applicable as review lens | No code defects are introduced, but the plan keeps CWE as an explicit secure-development checkpoint rather than silently omitting it. |
| OWASP ASVS | N/A | No web application, authentication flow, HTTP service, or API is introduced. |
| SBOM | Applicable as evidence wording | Public-readiness edits must not claim generated SBOM evidence unless an existing evidence path proves it. |
| VEX | Applicable as evidence wording | Vulnerability-status wording remains explicit as active evidence, `Open`, `N/A`, or `_TODO_`. |
| AI-SBOM | Applicable as tool-inventory wording; product AI-SBOM N/A unless runtime AI components are introduced | Development-tool AI usage alone does not create product AI-SBOM scope. |
| SLSA | Applicable as supply-chain evidence wording | Build-provenance language must not overclaim new attestations. |
| Architecture/iSAQB | PASS | No runtime, deployment, or interface structure changes; documentation trust boundary and overclaiming risk are planned explicitly. |
| Threat modeling / Zero Trust | Limited applicability | Documentation disclosure risk applies; no new system trust boundary or distributed access flow is introduced. |
| BSI C3A / C5 | N/A | No cloud service, provider-dependent deployment, or production operation is added. |
| Accessibility | Applicable | Learner-facing docs must remain text-oriented, CEFR-B2-friendly, and bilingual where the surrounding content is bilingual. |
| Cross-platform scripts | N/A | No new script-shaped tool is planned. |
| Agent parity | PASS | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` must be reviewed and updated atomically when shared wording changes. |

No constitution gate violations require complexity justification.

## Project Structure

### Documentation (this feature)

```text
specs/001-public-readiness/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── checklists/
│   └── requirements.md
└── spec.md
```

`contracts/` is intentionally not created. This feature has no API, CLI
interface, external service contract, data interchange protocol, or runtime
contract surface.

### Source Code (repository root)

```text
README.md
AGENTS.md
CLAUDE.md
GEMINI.md
.github/copilot-instructions.md
COMPLIANCE-PLAN_RL-SE-001.md
Lastenheft_*.md
docs/security/
specs/001-public-readiness/
```

**Structure Decision**: Documentation-only repository layout. No `src/`,
`tests/`, service, API, database, or generated application structure is added.

## Phase 0: Research

Research decisions are captured in [research.md](research.md). The decisions
resolve the relevant planning questions:

- How to separate generic public wording from audit-evidence origin.
- Which governance checkpoints apply to documentation-only public readiness.
- Why contracts are N/A.
- How to validate without building or publishing the repository.
- How to keep agent guidance surfaces in parity.

No `NEEDS CLARIFICATION` items remain.

## Phase 1: Design And Evidence Model

Design entities are captured in [data-model.md](data-model.md):

- Public-Readiness Surface
- Private Assumption
- Evidence Classification
- Maintained Agent Surface
- Public-Readiness Review Checkpoint

No API or external contract is defined. The implementation will operate on
repository files and review evidence, not on runtime interfaces.

## Implementation Guidance For Later Tasks

The later `/speckit-tasks` output should break implementation into these work
groups:

1. Inventory public-readiness surfaces and classify each as user-facing,
   agent-guidance, security/audit evidence, Lastenheft, or Spec-Kit artefact.
2. Replace or neutralize private paths, private URLs, private account defaults,
   organization-bound mandatory wording, and non-public provider assumptions
   in user-facing and agent-guidance surfaces.
3. Preserve security/audit evidence where needed by marking origin as context,
   example, or not-public-release-relevant evidence.
4. Keep unresolved approval, provider, model, legal, licensing, data-residency,
   and platform decisions as `Open`, `N/A`, or `_TODO_` with owner/follow-up.
5. Update maintained agent surfaces atomically and record intentional
   deviations, if any.
6. Run the validation commands from [quickstart.md](quickstart.md).

## Agent Context Update

No `<!-- SPECKIT START -->` / `<!-- SPECKIT END -->` marker block exists in
`AGENTS.md`, and this repository has no agent-context update script beyond the
generic Spec-Kit setup scripts. The plan therefore does not invent a marker
block. Agent context impact is handled as an explicit task requirement:
maintained agent surfaces must be reviewed and updated together during the
implementation phase.

## Post-Design Constitution Check

| Governance area | Status after design | Evidence path |
|---|---|---|
| Security-first | PASS | `plan.md`, `research.md`, `quickstart.md` validation commands |
| NIST SSDF / CWE | PASS | Planned evidence classification and text review checkpoints |
| OWASP ASVS | N/A | No web/API/authentication runtime |
| SBOM / VEX / SLSA / AI-SBOM | PASS | Planned wording/evidence-status review; no new build evidence claimed |
| Architecture/iSAQB | PASS | Documentation trust-boundary risk captured; no runtime ADR required |
| Accessibility | PASS | CEFR-B2, bilingual-context, text-oriented documentation checks planned |
| Cross-platform | N/A | No scripts added or changed by this plan |
| Agent parity | PASS | Four maintained agent surfaces identified as atomic implementation scope |

## Complexity Tracking

No constitution violations or exceptional complexity are introduced.
