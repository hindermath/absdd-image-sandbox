# Public-Readiness Review Checkpoints

**Feature:** `001-public-readiness`
**Status:** implementation evidence
**Date:** 2026-07-02

## Governance Applicability

| Checkpoint | Status | Evidence | Rationale |
|---|---|---|---|
| Security-first | Applicable / pass | `README.md`, `COMPLIANCE-PLAN_RL-SE-001.md`, `docs/security/public-readiness-evidence.md` | Secrets and provider setup remain local/untracked; human-only decisions stay open |
| NIST SSDF | Applicable / pass | `COMPLIANCE-PLAN_RL-SE-001.md`, `docs/secure-development/`, this file | Secure-development intent is preserved through evidence classification |
| CWE Top 25 | Applicable as review lens / pass | `specs/001-public-readiness/plan.md`, this file | No code remediation is claimed; CWE remains a secure-development review lens |
| OWASP ASVS | N/A / pass | `specs/001-public-readiness/plan.md` | No web app, auth flow, API, or runtime service is introduced |
| SBOM | Applicable as evidence wording / pass | `README.md`, `docs/security/public-readiness-evidence.md` | SBOM generation is described as a release/build artifact, not claimed as newly produced |
| VEX | Applicable as evidence wording / pass | `README.md`, `docs/security/public-readiness-evidence.md` | VEX status is not claimed as complete |
| AI-SBOM | Applicable as wording/status check / pass | `docs/security/ai-tools-inventory.md`, `docs/security/public-readiness-evidence.md` | Development-tool AI is separated from product/runtime AI components |
| SLSA | Applicable as evidence wording / pass | `README.md`, `docs/security/public-readiness-evidence.md` | No new provenance or attestation is claimed |
| Architecture / iSAQB | Applicable as documentation trust-boundary review / pass | `docs/security/sandbox-isolation.md`, this file | No runtime architecture is changed |
| Accessibility | Applicable / pass | `README.md`, `Lastenheft_*.md`, this file | Markdown remains text-oriented; bilingual context is preserved where already present |
| Cross-platform scripts | N/A / pass | this file | No script-shaped tool or wrapper is added or changed |
| Agent parity | Applicable / pass | `specs/001-public-readiness/agent-parity-review.md` | Four maintained agent surfaces were updated atomically |

## Success Criteria Mapping

| Success criterion | Evidence paths | Result |
|---|---|---|
| SC-001 private setup assumptions | `README.md`, `opencode.env.example`, `compose.yml`, `compose.home-baseline.yml`, `public-readiness-surface-inventory.md` | Mandatory private paths, accounts, and provider requirements were removed or classified |
| SC-002 organization-specific audit references | `docs/security/public-readiness-evidence.md`, `docs/security/agent-session-log/README.md` | Historical references are classified as context or not-public-release-relevant evidence |
| SC-003 unresolved approval/provider/legal/platform decisions | `docs/security/public-readiness-evidence.md`, `docs/security/sandbox-freigabe.md`, `docs/security/ai-tools-inventory.md`, `docs/security/branch-protection.md` | Open and `_TODO_` items remain explicit with owner/follow-up/re-evaluation data |
| SC-004 clean-reader understanding | `README.md`, `Lastenheft_Sandbox-Public-Readiness.md`, this file | Public-readiness status, non-goals, optional `home-baseline`, and evidence status are visible from the README path |
| SC-005 agent guidance parity | `specs/001-public-readiness/agent-parity-review.md` | Shared public-readiness wording is aligned across maintained agent surfaces |
| SC-006 no overclaiming | `docs/security/public-readiness-evidence.md`, validation searches in this file | No public release, formal approval, rebuild, provider approval, SBOM, VEX, SLSA, or AI-SBOM completion is claimed by this feature |

## CEFR-B2, A11Y, And Bilingual Review

| Scope | Result |
|---|---|
| `README.md` | Public-Readiness section uses short paragraphs and direct wording; German and English context is preserved |
| `Lastenheft_*.md` | Existing Lastenhefte remain text-first Markdown; one private local path was generalized |
| Agent guidance | Shared wording remains direct, list-based, and screen-reader friendly |
| `docs/security/` | Evidence docs remain Markdown tables/lists; human-only statuses are explicit |

## Validation Results

| Check | Command | Result | Notes |
|---|---|---|---|
| Whitespace | `git diff --check` | PASS | No whitespace errors reported on 2026-07-02 |
| Private path / private URL scan | `rg -n "(/Users/|C:\\\\|/home/[^ ]+|gitlab-ce|localhost:[0-9]+|provider portal|DMS|QISMS)" ...` | REVIEWED | 15 hits; remaining hits are generic policy text, Spec-Kit search patterns, historical log placeholders, or classified context evidence |
| Status / overclaim scan | `rg -n "(private|internal|approval|Freigabe|provider|model|legal|license|data-residency|public release|SBOM|VEX|SLSA|AI-SBOM|_TODO_|Open|N/A)" ...` | REVIEWED | 650 hits; terms are expected evidence/status language and are classified in `docs/security/public-readiness-evidence.md` |
| Compose static parse | `podman-compose config` | PASS | Static Compose validation succeeded on 2026-07-02 |
| Optional home-baseline override | `HOME_BASELINE_DIR=/Users/thorstenhindermann/home-baseline-tmp podman-compose -f compose.yml -f compose.home-baseline.yml config` | PASS | Override validation succeeded because `compose.home-baseline.yml` comments changed and the local checkout exists |
| Scope boundary | manual review | PASS | No container build/start, public switch, secret rotation, provider/model setup, formal approval, branch-protection change, external register update, or RL-SE-/Checklist self-assessment was performed |

## Open Follow-Up

| Item | Status | Owner | Follow-up | Re-evaluation trigger |
|---|---|---|---|---|
| `Lastenheft_Sandbox-Public-Readiness.md` completion / rename helper reference | Open | Maintainer | Provide or identify `scripts/rename-lastenheft.sh` and `scripts/rename-lastenheft.ps1`, or document that no rename helper is required | Merge-readiness review for this feature |
