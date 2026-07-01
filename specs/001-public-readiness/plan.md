# Implementation Plan: Sandbox Public Readiness

**Branch**: `001-public-readiness` | **Date**: 2026-06-30 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/001-public-readiness/spec.md`

**Note**: This plan is the `/speckit-plan` output for the Public-Readiness
feature only. It plans documentation and governance implementation work; it
does not start edits, generate tasks, run a container build, or start the
RL-SE-/Checklist self-assessment feature.

## Summary

Plan the Public-Readiness implementation for `absdd-image-sandbox` as a
public-ready training sandbox. The implementation will convert user-facing and
maintained agent guidance to generic public wording, preserve security intent,
and keep security/audit evidence auditable through explicit `Open`, `N/A`,
`_TODO_`, context, example, or not-public-release-relevant classifications.

The technical approach is repository documentation review and evidence
classification across the Public-Readiness surfaces only. No runtime code, API,
database, image build, container start, provider setup, secret rotation, formal
approval, external register entry, platform branch-protection configuration, or
repository visibility change is part of this feature.

## Technical Context

**Language/Version**: N/A. This feature changes Markdown documentation and
Spec-Kit planning artefacts only; no implementation language is introduced.
**Primary Dependencies**: N/A for runtime. Planning uses existing repository
Markdown files, Spec Kit artefacts, `rg`, Git, and Podman Compose validation.
**Storage**: Git-tracked Markdown and text configuration files in the
repository.
**Testing**: `git diff --check`, targeted `rg` scans, `podman-compose config`,
and optional home-baseline Compose override validation when the override is
affected.
**Target Platform**: Repository documentation consumed from macOS,
Windows/WSL2, and Linux; the sandbox runtime remains Podman-based.
**Project Type**: Documentation/governance feature for a container training
repository.
**Performance Goals**: A new public Fachinformatik apprentice or trainer can
identify sandbox purpose, non-goals, and public-readiness status from
`README.md` and linked setup, security, Lastenheft, and agent-guidance entry
points in under 10 minutes.
**Constraints**: No RL-SE-/Checklist self-assessment planning, no tasks
generation, no implementation start, no container build or start, no repository
visibility change, no secret rotation, no provider/model configuration, no
invented formal approval, no platform branch-protection configuration, and no
external register completion claim.
**Scale/Scope**: `README.md`, `opencode.env.example`, `compose.yml`,
`compose.home-baseline.yml`, maintained agent guidance, `COMPLIANCE-PLAN_RL-SE-
001.md`, `docs/security/`, `Lastenheft_*.md`, and
`specs/001-public-readiness/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Governance area | Status | Planning decision |
|---|---|---|
| Security-first | PASS | No secrets are added; validation plans text scans for private paths, private URLs, account defaults, provider portals, and overclaims. |
| Memory-safe language | N/A | No runtime code or primary implementation language is introduced; MSL remains a later training/evidence topic only where referenced by existing docs. |
| NIST SSDF | Applicable | Public-readiness work must preserve secure-development intent and explicit evidence status. |
| CWE Top 25 | Applicable as review lens | No code defects or vulnerability remediation are implemented; tasks must record CWE applicability without creating a remediation or acceptance claim. |
| OWASP ASVS | N/A | No web application, authentication flow, HTTP service, API, or runtime interface is introduced. |
| SBOM | Applicable as evidence wording | Public-readiness edits must not claim generated SBOM evidence unless an existing evidence path proves it. |
| VEX | Applicable as evidence wording | Vulnerability-status wording remains explicit as active evidence, `Open`, `N/A`, or `_TODO_`. |
| AI-SBOM | Applicable as wording/status check only | Development-tool AI usage may be documented, but product AI-SBOM scope remains conditional unless runtime AI components are introduced. |
| SLSA | Applicable as supply-chain evidence wording | Build-provenance language must not overclaim new attestations. |
| Architecture/iSAQB | PASS | No runtime, deployment, interface, or structural architecture work is introduced; documentation trust boundary and overclaim risk are planned explicitly. |
| Threat modeling / Zero Trust | Limited applicability | Applies only to disclosure and documentation trust-boundary risk; no new system trust boundary or distributed access flow is introduced. |
| BSI C3A / C5 | N/A | No cloud service, provider-dependent deployment, production operation, or provider assurance status is added. |
| Accessibility | Applicable | Learner-facing docs must remain text-oriented, CEFR-B2-friendly, and bilingual where surrounding content is bilingual. |
| Cross-platform scripts | N/A | No script-shaped tool, wrapper, or platform command parity claim is added or changed by this plan. |
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
│   ├── requirements.md
│   └── requirements-quality.md
└── spec.md
```

`contracts/` is intentionally not created. This feature has no API, CLI command
schema, external service contract, data interchange protocol, parser grammar,
UI flow contract, or runtime contract surface.

### Source Code (repository root)

```text
README.md
opencode.env.example
compose.yml
compose.home-baseline.yml
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
`tests/`, service, API, database, generated application structure, or contracts
directory is added.

## Phase 0: Research

Research decisions are captured in [research.md](research.md). They resolve the
relevant planning questions:

- How to separate generic public wording from audit-evidence origin.
- Which Public-Readiness surfaces are in scope.
- Why RL-SE-/Checklist self-assessment is out of scope for this feature.
- Which governance checkpoints apply to documentation-only public readiness.
- Why contracts are N/A.
- How to validate without building, starting, publishing, or changing provider
  configuration.
- How to keep maintained agent guidance surfaces in parity.

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

The later `/speckit-tasks` output should break Public-Readiness implementation
into these work groups only:

1. Inventory the listed Public-Readiness surfaces and classify each as
   user-facing, agent-guidance, security/audit evidence, Lastenheft,
   configuration guidance, Compose guidance, or Spec-Kit artefact.
2. Replace or neutralize private paths, private URLs, private account defaults,
   organization-bound mandatory wording, provider portals, and non-public
   provider assumptions in user-facing and agent-guidance surfaces.
3. Preserve security/audit evidence where needed by marking origin as context,
   example, or not-public-release-relevant evidence.
4. Keep unresolved approval, provider, model, legal, licensing, data-residency,
   public-release, SBOM, VEX, SLSA, AI-SBOM, and platform decisions as `Open`,
   `N/A`, or `_TODO_` with rationale, owner, follow-up, and re-evaluation
   trigger where applicable.
5. Update maintained agent surfaces atomically and record intentional
   deviations, if any.
6. Run the validation commands from [quickstart.md](quickstart.md), including
   `podman-compose config` as the standard static Compose validation.

Tasks must not plan or perform RL-SE-/Checklist self-assessment, container
builds, container starts, repository visibility changes, secret rotation,
provider/model configuration, formal approval, platform branch-protection
configuration, or external register updates.

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
| NIST SSDF | PASS | Planned secure-development wording and evidence-status review |
| CWE Top 25 | PASS | Applicable as a secure-development review lens; no code remediation or vulnerability-fix claim is introduced |
| OWASP ASVS | N/A/PASS | No web, API, authentication, or runtime service implementation |
| SBOM / VEX / SLSA / AI-SBOM | PASS | Planned wording/evidence-status review; no new build evidence claimed |
| Architecture/iSAQB | PASS | Documentation trust-boundary risk captured; no runtime ADR required |
| Accessibility | PASS | CEFR-B2, bilingual-context, text-oriented documentation checks planned |
| Cross-platform | N/A | No scripts, wrappers, or platform parity claims added or changed |
| Agent parity | PASS | Four maintained agent surfaces identified as atomic implementation scope |

## Complexity Tracking

No constitution violations or exceptional complexity are introduced.
