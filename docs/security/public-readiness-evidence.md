# Public-Readiness Evidence

**Status:** implementation evidence for `specs/001-public-readiness`
**Date:** 2026-07-05

This file classifies security, governance, release, provider, and audit
evidence for the Public-Readiness run. The repository was switched to public
visibility on 2026-07-03 after validation. This file does not grant approval,
generate SBOM/VEX/SLSA evidence, configure providers, or close human-only
decisions.

## Evidence Classification Rules

| Classification | Meaning | Required data |
|---|---|---|
| `active-evidence` | Current repository evidence for a statement | Evidence path |
| `context-evidence` | Origin or background that explains why a control exists | Rationale |
| `example-evidence` | Illustrative example, not a mandatory public requirement | Rationale |
| `not-public-release-relevant` | Useful for audit history but not a public-release claim | Rationale |
| `Open` | Applicable but unresolved | Owner, follow-up, re-evaluation trigger |
| `N/A` | Not applicable to this documentation-only feature | Rationale |
| `_TODO_` | Placeholder for a human or future run | Owner, follow-up, re-evaluation trigger |

## Classified Evidence

| Evidence item | Classification | Evidence path | Rationale | Owner | Follow-up | Re-evaluation trigger |
|---|---|---|---|---|---|---|
| Public sandbox purpose and boundaries | active-evidence | `README.md` | README now states training purpose, non-production scope, and Public-Readiness status | Maintainer | Keep current during README changes | Public release review |
| Optional `home-baseline` workflow | active-evidence | `README.md`, `compose.home-baseline.yml` | Described as user-owned optional template checkout, not as image content or mandatory private path | Maintainer | Keep template source generic unless a course-specific source is documented separately | Template workflow change |
| OpenCode provider status | active-evidence | `README.md`, `opencode.env.example`, `opencode.jsonc` | No provider is configured by the image; local provider secrets are untracked | Owner | Configure locally only if needed | Provider setup decision |
| Codex provider/model status | `Open` | `codex/config.toml`, `docs/security/ai-tools-inventory.md` | No repository provider default is configured; local backend status is owner-controlled | Owner | Enter local provider/backend details only in approved local or operational evidence | Provider/model approval |
| Formal sandbox approval | `Open` | `docs/security/sandbox-freigabe.md`, `docs/security/sandbox-freigabe-review.md` | Approval is explicitly pending and cannot be granted by an agent | Owner / CISO / ISB / KIB | Complete approval review and signature fields | Formal approval decision |
| Branch protection / hosting enforcement | active-evidence | `docs/security/branch-protection.md`, `.github/CODEOWNERS`, `.github/pull_request_template.md`, `.github/workflows/homogeneity-check.yml` | Repository is public and GitHub Ruleset `18493733` actively protects `main` with PR review, Code Owner review, required Agent Secret Scan checks, deletion/non-fast-forward protection, and documented admin bypass | Owner / platform admin | Keep ruleset evidence current when required checks or hosting settings change | GitHub ruleset, workflow, repository visibility, or platform-rule change |
| Secret scanning | active-evidence | `docs/security/secret-scanning.md`, `.pre-commit-config.yaml`, `.gitleaks.toml` | Repository-side controls are documented; central push blocking depends on platform capability | Maintainer / platform admin | Keep tool versions and platform limits current | Secret-scanning tool or host change |
| Network egress decision | active-evidence | `docs/security/network-decision.md`, `compose.yml` | Free egress is a documented learning-environment risk decision, not a hidden default | Owner | Reassess egress allow-list feasibility | Network/proxy availability change |
| Sandbox isolation | active-evidence | `docs/security/sandbox-isolation.md`, `compose.yml`, `codex/`, `opencode.jsonc` | Current isolation mechanisms are documented without claiming production approval | Maintainer | Keep evidence aligned with Compose/Dockerfile changes | Runtime or mount change |
| Swift project mount and toolchain | active-evidence | `Dockerfile`, `compose.yml`, `.env.example`, `scripts/smoke-test-toolchains.sh`, `README.md` | Swift projects are mountable at `/swift-projects`; the image installs Swift `6.3.3-noble` from a signed Swift.org release artifact and validates it in the smoke test | Maintainer | Keep version, mount, and smoke test aligned with Swift updates | Swift version, mount, or toolchain change |
| Optional VS Code Dev Containers access | active-evidence | `README.md`, `.devcontainer/devcontainer.json`, `docs/security/sandbox-isolation.md` | VS Code can attach from the host to the running `ade` container without adding a long-running browser IDE service or publishing an additional IDE port | Maintainer | Keep aligned with Dev Containers and Compose changes | IDE access, runtime, or mount change |
| Image SBOM generation | `Open` | `README.md`, `scripts/build-and-sbom.*`, `sboms/.gitkeep` | The process exists; generated SBOM JSON files are per-image build artifacts and are not standing repository evidence unless a release workflow explicitly requires them | Maintainer | Generate SBOM only in a release/build workflow | Image handover or release build |
| VEX status | `Open` | `README.md`, `docs/security/public-readiness-evidence.md` | No VEX evidence is produced by this documentation run | Maintainer | Decide VEX workflow in a later hardening/release run | Vulnerability or release review |
| SLSA / provenance status | `Open` | `README.md`, `docs/security/public-readiness-evidence.md` | No provenance or attestation is produced by this documentation run | Maintainer | Decide provenance workflow in a later hardening/release run | Release pipeline design |
| AI-SBOM supplier transparency | `_TODO_` | `docs/security/ai-tools-inventory.md` | Development-tool entries exist; owner/provider fields remain intentionally open | Owner / KIB | Fill provider/model supplier data when provider usage is approved | Provider/model approval |
| Historical agent-session logs | not-public-release-relevant | `docs/security/agent-session-log/` | Logs may contain old provider, image, hosting, or host-context references; they are audit notes, not current public setup instructions | Maintainer | Neutralize a log only if it is reused as current guidance | Session-log curation review |
| GSDB preflight report | context-evidence | `docs/security/gsdb-self-assessment.md` | Preflight prepares a later GSDB run and is not a formal approval | Maintainer | Refresh when the GSDB intensive review starts | GSDB Spec-Kit run |
| RL-SE-/Checklist self-assessment | `Open` | `Lastenheft_RL-SE-Checklist-Selbstpruefung.md` | Separate Spec-Kit run; intentionally not executed here | Maintainer | Start separate run manually if requested | Explicit user request |
| Container hardening | `Open` | `Lastenheft_Secure-Development-Container-Hardening.md`, `Lastenheft_Secure-Development-Hardening.md` | Separate hardening runs; intentionally not executed here | Maintainer | Start separate run manually if requested | Explicit user request |

## No-Overclaim Statement

This Public-Readiness implementation does not claim that:

- the container image has been formally released;
- formal sandbox approval has been granted;
- provider, model, legal, data-residency, or platform decisions are complete;
- SBOM, VEX, SLSA, or AI-SBOM evidence has been generated by this run;
- external registers have been updated.
