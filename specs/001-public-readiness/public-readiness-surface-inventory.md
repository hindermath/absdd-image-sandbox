# Public-Readiness Surface Inventory

**Feature:** `001-public-readiness`
**Status:** implementation evidence
**Date:** 2026-07-02

This inventory records the reviewed surfaces for the Public-Readiness
implementation. It separates reusable public guidance from security evidence,
historical context, examples, and open human-only decisions.

## Surface Inventory

| Surface | Type | Audience | Language mode | Status | Required action | Result |
|---|---|---|---|---|---|---|
| `README.md` | user-facing | apprentices, trainers, maintainers | bilingual | updated | genericize | Public-readiness status added; hard-coded `home-baseline` account reference generalized |
| `opencode.env.example` | configuration-guidance | public users, maintainers | English | updated | genericize | Empty public-training use and no-secret rule clarified |
| `compose.yml` | compose-guidance | public users, maintainers | English comments | updated | genericize | Self-mount and egress comments made public-reader friendly |
| `compose.home-baseline.yml` | compose-guidance | public users, maintainers | English comments | updated | genericize | Optional user-owned `home-baseline` mount clarified |
| `AGENTS.md` | agent-guidance | Codex-like agents | bilingual | updated | genericize | Hosting-platform guidance made generic while GitLab CE evidence remains classified |
| `CLAUDE.md` | agent-guidance | Claude agents | bilingual | updated | genericize | Kept in parity with `AGENTS.md` |
| `GEMINI.md` | agent-guidance | Gemini agents | bilingual | updated | genericize | Kept in parity with `AGENTS.md` |
| `.github/copilot-instructions.md` | agent-guidance | GitHub Copilot | bilingual | updated | genericize | Kept in parity with `AGENTS.md` |
| `COMPLIANCE-PLAN_RL-SE-001.md` | security-evidence | reviewers, maintainers | German | updated | classify-evidence | Fixed model/provider defaults so they are not claimed as repository requirements |
| `docs/security/` | security-evidence | reviewers, maintainers | mixed bilingual | updated | classify-evidence | Active evidence updated; historical provider/host/platform references classified in `docs/security/public-readiness-evidence.md` |
| `Lastenheft_Abarbeitungsreihenfolge.md` | lastenheft | maintainers, agents | bilingual | reviewed | preserve | Queue document remains a later-run order artifact and starts no run |
| `Lastenheft_Sandbox-Public-Readiness.md` | lastenheft | public-readiness maintainers | bilingual | reviewed | preserve | Intake remains accurate for this run |
| `Lastenheft_RL-SE-Checklist-Selbstpruefung.md` | lastenheft | maintainers, reviewers | bilingual | updated | genericize | Local `~/home-baseline-tmp` dependency generalized to `docs/secure-development/` |
| `Lastenheft_Secure-Development-Container-Hardening.md` | lastenheft | maintainers, reviewers | bilingual | reviewed | preserve | Separate hardening intake; not executed by this feature |
| `Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md` | lastenheft | maintainers, reviewers | bilingual | reviewed | preserve | Separate self-check intake; not executed by this feature |
| `Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md` | lastenheft | maintainers, reviewers | bilingual | reviewed | preserve | Separate GSDB review intake; not executed by this feature |
| `Lastenheft_Secure-Development-Hardening.md` | lastenheft | maintainers, reviewers | German | reviewed | preserve | Separate hardening intake; not executed by this feature |
| `specs/001-public-readiness/` | spec-kit-artifact | implementers, reviewers | English | updated | classify-evidence | Implementation evidence artifacts added and task status maintained |

## Private Assumptions And Resolutions

| ID | Source | Finding | Type | Risk | Resolution | Rationale | Owner | Re-evaluation trigger |
|---|---|---|---|---|---|---|---|---|
| PA-001 | `README.md` | Concrete `hindermath/home-baseline` template account in public setup text | account-default | public-confusion | genericize | Public users should create their own repository from a suitable `home-baseline` template; the sandbox must not require one account | Maintainer | Template source changes or public release review |
| PA-002 | `Lastenheft_RL-SE-Checklist-Selbstpruefung.md` | `~/home-baseline-tmp/docs/secure-development/` as source path | private-path | public-confusion | genericize | The repository contains `docs/secure-development/`; public readers should not depend on a maintainer home path | Maintainer | Next RL-SE-/Checklist Spec-Kit run |
| PA-003 | `docs/security/gsdb-self-assessment.md` | Local absolute host path in repository field | private-path | oversharing | genericize | Preflight report can identify the local checkout without exposing a maintainer-specific path | Maintainer | Next GSDB preflight refresh |
| PA-004 | `docs/security/sandbox-freigabe.md`, `docs/security/sandbox-freigabe-review.md`, `docs/security/sandbox-isolation.md` | Old `ade-dev-sandbox` object name in active evidence | release-status | public-confusion | genericize | Active evidence must refer to `absdd-image-sandbox` | Maintainer | Approval evidence refresh |
| PA-005 | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | GitLab CE phrasing could be read as required hosting platform | platform | public-confusion | genericize | Agent guidance now describes the active hosting platform generically and classifies GitLab CE as evidence context | Maintainer | Hosting platform change |
| PA-006 | `COMPLIANCE-PLAN_RL-SE-001.md` | Fixed model and Azure provider defaults in historical task text | provider-status | overclaiming | genericize | The current repository config has no provider default; concrete providers remain owner-managed local configuration | Maintainer | Codex provider configuration change |
| PA-007 | `docs/security/ai-tools-inventory.md`, `docs/security/network-decision.md` | Azure/OpenAI backend wording could imply configured provider status | provider-status | overclaiming | mark-open | Wording now keeps provider operation conditional on owner configuration | Owner | Provider/model approval or operating decision |
| PA-008 | Historical `docs/security/agent-session-log/*.md` | Old GitLab, Chat-AI, host-path, image, or MR references | context | audit-loss | mark-not-public-release-relevant | Historical logs are audit notes, not current public guidance; they remain classified in evidence instead of being rewritten wholesale | Maintainer | Session log curation policy change |

## Clean-Reader Notes

- `README.md` now exposes the Public-Readiness status before setup commands.
- Optional `home-baseline` use is described as a user-owned template checkout,
  not as a private path or mandatory account.
- Security evidence keeps human-only decisions visible and does not claim
  formal approval or public release.
- Agent guidance stays aligned across the four maintained agent surfaces.
