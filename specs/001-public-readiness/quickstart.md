# Quickstart: Sandbox Public Readiness Planning

This quickstart is for the later implementation phase. It does not make the
repository public, does not build the image, and does not configure secrets,
providers, models, or formal approvals.

## 1. Confirm Feature Context

```bash
git status --short --branch
sed -n '1,220p' specs/001-public-readiness/spec.md
sed -n '1,220p' specs/001-public-readiness/plan.md
sed -n '1,220p' specs/001-public-readiness/research.md
```

Expected:

- Branch is `001-public-readiness`.
- Working tree changes are understood before implementation starts.
- `spec.md`, `plan.md`, and `research.md` describe documentation/governance
  work only.

## 2. Review The Planned Surface Set

```bash
printf '%s\n' \
  README.md \
  opencode.env.example \
  compose.yml \
  compose.home-baseline.yml \
  AGENTS.md \
  CLAUDE.md \
  GEMINI.md \
  .github/copilot-instructions.md \
  COMPLIANCE-PLAN_RL-SE-001.md \
  docs/security/ \
  Lastenheft_*.md \
  specs/001-public-readiness/
```

Expected:

- User-facing and agent-guidance surfaces are treated as generic public
  guidance.
- Security and audit evidence may retain origin context only when classified.

## 3. Run Public-Readiness Discovery Searches

Use these searches as review aids. They are intentionally broad and require
human interpretation.

```bash
rg -n "(/Users/|C:\\\\|/home/[^ ]+|gitlab-ce|localhost:[0-9]+|provider portal|DMS|QISMS)" README.md opencode.env.example compose.yml compose.home-baseline.yml AGENTS.md CLAUDE.md GEMINI.md .github/copilot-instructions.md COMPLIANCE-PLAN_RL-SE-001.md docs/security Lastenheft*.md specs/001-public-readiness
rg -n "(private|internal|approval|Freigabe|provider|model|legal|license|data-residency|public release|SBOM|VEX|SLSA|AI-SBOM|_TODO_|Open|N/A)" README.md opencode.env.example compose.yml compose.home-baseline.yml AGENTS.md CLAUDE.md GEMINI.md .github/copilot-instructions.md COMPLIANCE-PLAN_RL-SE-001.md docs/security Lastenheft*.md specs/001-public-readiness
```

Expected:

- Findings in user-facing and agent-guidance files are removed or generalized.
- Findings in security/audit evidence are classified as context, example,
  not-public-release-relevant, `Open`, `N/A`, or `_TODO_`.
- No finding is silently ignored.
- Findings must not start or imply RL-SE-/Checklist self-assessment work.

## 4. Validate Documentation Edits

```bash
git diff --check
podman-compose config
```

Optional home-baseline override validation, when a local checkout exists:

```bash
HOME_BASELINE_DIR=/path/to/home-baseline-tmp podman-compose -f compose.yml -f compose.home-baseline.yml config
```

Expected:

- Markdown and command snippets have no whitespace errors.
- Static Compose parsing succeeds without requiring a running Podman machine.
- `podman compose config` is optional only; a local Podman socket or machine
  failure is not a repository content failure when `podman-compose config`
  succeeds.

## 5. Checks That Must Not Run For This Feature

Do not run these as part of Public-Readiness planning or implementation unless
a later approved feature explicitly changes scope:

```bash
podman compose build --pull
podman compose up -d
podman compose down -v
```

Do not:

- switch the repository to public,
- rotate API keys or other secrets,
- configure provider/model access,
- invent formal sandbox approval,
- configure platform branch protection.

## 6. Completion Signal For Later Implementation

Implementation is ready for `/speckit-implement` handoff when:

- all public-readiness surfaces have been reviewed,
- private assumptions are removed, generalized, or classified,
- shared agent guidance surfaces are aligned or deviations are documented,
- unresolved evidence remains explicit with owner/follow-up where applicable,
- `git diff --check` and `podman-compose config` pass,
- no container build or public-release action was performed.
