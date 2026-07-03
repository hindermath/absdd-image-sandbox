# Agent Parity Review

**Feature:** `001-public-readiness`
**Status:** implementation evidence
**Date:** 2026-07-02

This review covers the maintained agent surfaces required by the feature:
`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and
`.github/copilot-instructions.md`.

## Shared Rule Areas

| Rule area | AGENTS.md | CLAUDE.md | GEMINI.md | Copilot instructions | Parity status |
|---|---|---|---|---|---|
| Active compliance work queue | aligned | aligned | aligned | aligned | aligned |
| Secure-development neutrality | aligned | aligned | aligned | aligned | aligned |
| Public-readiness wording | updated | updated | updated | updated | updated |
| Podman and Compose commands | aligned | aligned | aligned | aligned | aligned |
| Optional `home-baseline` mount | aligned | aligned | aligned | aligned | aligned |
| Security and secret handling | updated | updated | updated | updated | updated |
| Spec-Kit model routing guidance | aligned | aligned | aligned | aligned | aligned |

## Public-Readiness Change

The Commit & Pull Request and Security guidance sections were updated
atomically in all four files:

- hosting-platform enforcement is described generically;
- `.gitlab/` files remain repository-side evidence from the current evidence
  set, not a mandatory public-hosting assumption;
- the P1-3 audit text no longer states a concrete GitLab CE edition as a
  reusable public requirement;
- no agent surface claims provider approval, formal approval, public release,
  or branch-protection completion beyond the evidence path.

## Intentional Deviations

| Surface | Deviation | Reason |
|---|---|---|
| `AGENTS.md` | Mentions Codex session in the compliance queue | Agent-specific session wording |
| `CLAUDE.md` | Mentions Claude session in the compliance queue | Agent-specific session wording |
| `GEMINI.md` | Mentions Gemini session in the compliance queue | Agent-specific session wording |
| `.github/copilot-instructions.md` | Mentions GitHub Copilot session in the compliance queue | Agent-specific session wording |

No public-readiness rule deviation is open.
