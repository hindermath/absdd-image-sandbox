---
lang: en-GB
title: absdd-image-sandbox - Spec Kit Workshop
date: 2026-10-25
---

<!-- slide: W01 -->
# absdd-image-sandbox

Spec Kit workshop with AI agents
For first-year apprentices and non-specialist developers
English · Updated 25 October 2026

::: notes
AI means artificial intelligence. A container is a restricted working environment, not a complete security guarantee. This workshop assumes an environment prepared by an instructor. All four IT training occupations and all four IT-specialist tracks can use the same introduction. Practical tasks require the applicable project authority.
:::

---

<!-- slide: W02 -->
# Our workflow

- Understand the environment and your project folder
- Prepare Git, agent context and Spec Kit
- Review requirements, plans and tasks
- Implement within scope and review results

::: notes
Spec Kit divides a request into requirements, planning and tasks. A review is a deliberate assessment by another person or an explicitly assigned agent. Explaining a step does not authorize it automatically. The group may pause after any phase. See this repository's learner index and FAQ for details.
:::

---

<!-- slide: W03 -->
# Host, image and container

- Host: your physical computer
- Image: a prepared set of tools
- Container: a running environment from an image
- Mount: a connection to real host files

::: notes
A writable mount allows changes and deletion on the host too. A volume is persistent storage managed by Podman. Neither is a backup. A desktop IDE or agent app is not automatically connected to the container CLI. Diagram alternative: the host provides a selected project folder; the container accesses it through a mount; agent state lives in separate volumes.
:::

---

<!-- slide: W04 -->
# Choose the correct platform path

- Apple Silicon: native linux/arm64, no Rosetta fallback
- Intel/AMD Windows: PowerShell 7 and Podman machine
- Ubuntu/WSL2: its own rootless Linux Podman
- Shared hardware does not replace separate evidence

```text
podman info
podman-compose config
```

::: notes
Location: host, in the sandbox checkout, using Bash or PowerShell 7. Podman should respond; config validates Compose without building or starting. Rootless means operating without root privileges on that Linux system. Windows and Ubuntu/WSL2 use separate Podman runtimes. ARM64 success proves neither AMD64 acceptance nor native Linux hardware coverage. See installation and troubleshooting guides.
:::

---

<!-- slide: W05 -->
# Use your own repository

- Fork by default; template is a later option
- origin is your writable remote
- upstream needs a suitable reference relationship
- GitHub is one route, not a universal requirement

```text
git status --short --branch
git remote -v
```

::: notes
Location: host in the personal checkout. Forks preserve reference history and remain the default. Templates create independent history; this additional profile is prepared, not enabled. Naming a remote does not join histories: no blind upstream or unrelated-history merges. Copied approvals, statistics and run states are source context only. SysInfo/web still need empty product repos plus one learning package, not the whole sandbox. Keep Home Baseline separate. The commands are read-only but may show private URLs; sanitize output. Institutional GitLab, Codeberg, Forgejo and other Git systems remain valid. Commit/push require separate decisions. See docs/fuer-lernende/template-profil.md.
:::

---

<!-- slide: W06 -->
# Configure project mounts deliberately

- .env contains local Compose values
- Leave opencode.env unchanged without a provider
- Never overwrite existing files with examples
- Mount required folders, never your entire home

```text
if [ ! -e .env ]; then cp .env.example .env; fi
if [ ! -e opencode.env ]; then
  cp opencode.env.example opencode.env
fi
chmod 600 .env opencode.env
```

::: notes
Location: host sandbox checkout, Bash. PowerShell alternative: if (-not (Test-Path -LiteralPath .env)) { Copy-Item .env.example .env }; repeat for opencode.env. On Windows protect files using filesystem permissions, not a generic chmod instruction. Existing files must remain unchanged. Compose reads .env; the image does not embed it. New mounts require deliberate container recreation, not necessarily rebuilding. See installation and FAQ.
:::

---

<!-- slide: W07 -->
# A first test without an AI account

- The host opens a container shell
- Check user and working directory
- Run a small program in the project mount
- Matching output is not full platform acceptance

```text
podman compose exec ade bash
# Danach im Container / then inside the container:
id
pwd
python -c 'print("Hello from the sandbox")'
```

::: notes
Run the first command on the host and the remaining commands inside the opened container shell. Expect adedev, a nonzero UID and the Hello output. Use the relevant toolchain guide for C#, Java, Go, Rust or Swift. A host IDE may edit files; no additional host compiler is required. This does not prove perfect isolation or platform acceptance. See first steps.
:::

---

<!-- slide: W08 -->
# Agent context before the task

- Read the project README and existing agent rules
- AGENTS.md records durable project conventions
- Keep shared rules aligned across maintained agents
- Do not automate sign-in or permission escalation

::: notes
An agent CLI is a command-line program running an AI agent. Installation does not approve a provider, model or dataset. OpenCode 2 explicitly retains open control and audit follow-ups in this sandbox. Use only a project-approved agent for practical work. The prompt dispatcher supports individual requests without bypassing sign-in or approvals. See the agent and dispatcher guides.
:::

---

<!-- slide: W09 -->
# A bounded AGENTS.md request

- Read verifiable repository signals first
- Add durable, project-specific rules only
- Invent neither commands nor approvals
- Request the diff and open assumptions

```text
Read README, project files, scripts and agent rules.
Add only verifiable project conventions to AGENTS.md.
Preserve safety boundaries and existing guidance.
Show the diff and open assumptions. No commit or push.
```

::: notes
Location: an approved agent's chat in the application project, not the shell. /init is not a universal command. Read existing files before changing them; do not replace established rules wholesale. This sandbox maintains five shared agent-guidance surfaces. Each application project defines its own maintained surfaces.
:::

---

<!-- slide: W10 -->
# Initialize Spec Kit deliberately

- The image pins Spec Kit 1.2.3
- Inspect any existing .specify structure first
- Select one suitable agent integration
- No global installation or unreviewed --force

```text
specify --version
specify check
# Nur im vorbereiteten neuen Projekt / new project only:
specify init . --integration codex
```

::: notes
Location: container Bash in the prepared application project. Expect the CLI version and tool availability. Initialization writes project artifacts and therefore needs separate authority. For existing files, clarify purpose, backup and changes first. Linux scripts match the container; installed PowerShell is distinct from the Windows host. The Dockerfile is the version source. Reading the slide runs no command.
:::

---

<!-- slide: W11 -->
# Shell command or agent invocation?

- specify init belongs in the shell
- $speckit-analyze invokes a Codex skill
- Other integrations use different invocation styles
- Inspect installed skills instead of guessing syntax

::: notes
Agent-chat examples: Codex $speckit-analyze; OpenCode /speckit.analyze; Claude Code, Antigravity and Copilot may use /speckit-analyze through their installed skills. These examples approve no agent. The following prompts use Codex syntax. Adapt only the invocation for another integration, preserving scope and safety boundaries. Check installed integrations before a live demonstration.
:::

---

<!-- slide: W12 -->
# Understand governance presets first

- A preset adds workflow rules
- Lower priority numbers take precedence
- Installation does not fulfill controls
- Inspect installed versions and local changes

```text
specify preset list
git status --short
```

::: notes
Location: container Bash in the initialized application project. Expect installed presets and existing changes. Repository matrices provide reviewed versions, priorities and archive locations. Do not switch silently to latest. A new version may affect evidence and source bindings. The instructor decides which profiles and installation authority apply.
:::

---

<!-- slide: W13 -->
# Six foundational governance presets

- Security and Architecture
- iSAQB Architecture and A11Y
- Cross-Platform and Agent Parity
- The managed standard profile adds two run-governance presets

::: notes
These six areas form the conceptual foundation. The local standard profile contains eight packages, adding Autonomous Run and Parallel Autonomous Run. Installing them grants no autonomous authority. Prefer existing approved profiles for the workshop. The local pilot matrix contains fourteen packages, not a universal requirement for learner projects.
:::

---

<!-- slide: W14 -->
# Security and Architecture

- Security: protection needs, secrets and supply chains
- Architecture: boundaries, decisions and risks
- Separate assumptions from evidence
- Human approvals remain human decisions

::: notes
A secret is confidential access information. A supply chain includes sources, packages and build steps. An architectural decision explains a deliberate choice, alternatives and consequences. Example: mount the project folder, not the entire host home. An SBOM lists components; it does not prove vulnerability clearance or approval.
:::

---

<!-- slide: W15 -->
# iSAQB and accessibility

- iSAQB: traceable architecture and quality goals
- A11Y: understandable content and accessible interaction
- German first, equivalent English
- Automated checks do not replace human assessment

::: notes
iSAQB provides an architecture review baseline; beginners can start with understandable components and decisions. A11Y abbreviates accessibility. WCAG 2.2 AA is a target for applicable criteria, not an automatic property of these slides. Human checks cover keyboard use, screen readers, reading order and comprehension. CEFR B2 is the language target.
:::

---

<!-- slide: W16 -->
# Cross-Platform and Agent Parity

- Label each command's location and shell
- Check ARM64 and AMD64 separately
- Keep Windows and Ubuntu/WSL2 evidence separate
- Synchronize shared agent rules

::: notes
Parity means consistent meaning, not identical software on every platform. Testing Bash and PowerShell on one host does not establish native Windows acceptance. Missing checks stay Open with an owner, next step and re-evaluation trigger. The container remains Linux even when running PowerShell.
:::

---

<!-- slide: W17 -->
# Preview before installation

- Work in the prepared application project
- Select the managed matrix explicitly
- Start with --dry-run and human review
- Apply nothing without installation authority

```text
repo=/ade-dev-sandbox
matrix="$repo/scripts/config/spec-kit-governance-presets.json"
bash "$repo/scripts/install-spec-kit-governance-presets.sh" \
  --repo "$PWD" --preset-config "$matrix" --dry-run
```

::: notes
Location: container Bash in the application project; /ade-dev-sandbox is the existing repository mount. Expect a preview, not installation. Preserve local modifications and versions. Omitting --dry-run writes changes and needs a separate request. Do not mix this script's options with another sandbox's tools. Ask your instructor if the mount is missing; do not download a replacement installer.
:::

---

<!-- slide: W18 -->
# Choose additional profiles by need

- Intake: capture, review and order requirements
- Model Routing: map operational task roles
- Assurance: project-specific control evidence
- Statistics: optional pilot reporting

::: notes
Matrices live under scripts/config/. The fourteen-package profile is explicitly an optional statistics pilot. Do not pin models in feature specifications or infer provider/platform approval from preset installation. Review purpose, prerequisites and impact with the instructor. Assurance package and evidence-schema versions are different concepts.
:::

---

<!-- slide: W19 -->
# Record versions and priorities

- Compare the matrix with installed packages
- Trace sources and local modifications
- Do not broaden profiles accidentally
- Record unexplained differences as Open

```text
repo=/ade-dev-sandbox
bash "$repo/scripts/install-spec-kit-governance-presets.sh" \
  --repo "$PWD" --check-only
specify preset list
```

::: notes
Location: container Bash in the project. --check-only inspects the selected matrix without writing. This example uses the eight-package standard profile; supply --preset-config for another approved profile. Do not hide failures with --force. Validation, technical fulfillment and human approval are separate states.
:::

---

<!-- slide: W20 -->
# Intake: capture a request

- Name audience, problem and intended result
- State scope and non-goals explicitly
- Bind ordered, traceable sources
- Never guess unresolved decisions

::: notes
An intake is a requirements document preceding a feature run. A receipt records provenance and source bindings; a hash is a content checksum. Changing bound sources may require an update and review. Preserve intake identities and archive predecessors; do not replace sources merely to satisfy a validator. Use a separately authorized workshop example, never execute active sandbox intakes.
:::

---

<!-- slide: W21 -->
# Review and order before execution

- Review requirements fully and independently
- State dependencies and handoffs explicitly
- Ready and Eligible grant no execution authority
- Never bypass a blocked successor

::: notes
An intake series orders requests through dependencies. Its machine-readable manifest governs; text and diagrams explain the same state. Independent review checks meaning, not just hashes. Successful requirements review grants no technical, legal, privacy, provider or release approval. This workshop does not alter the active sandbox series.
:::

---

<!-- slide: W22 -->
# Autonomy requires explicit boundaries

- Define goal, files and permitted actions
- State stop rules and human-only decisions
- Authorize commit, push and merge separately
- Model choice remains operational agent guidance

::: notes
Autonomous Run governs an explicitly requested run; Parallel Autonomous Run coordinates separated runs. Neither grants blanket authority. Secrets, formal approvals and platform rules remain human responsibilities. Report stopping conditions clearly. Model names do not belong in reproducible spec.md, plan.md or tasks.md artifacts.
:::

---

<!-- slide: W23 -->
# Evidence instead of green claims

- Record date, version, platform and result
- Open needs owner, follow-up and trigger
- N/A needs a reasoned explanation
- Statistics do not measure individual performance

::: notes
A follow-up is the next planned action; a trigger is a reason to reassess. Successful PDF creation does not prove PDF accessibility; an SBOM does not prove vulnerability clearance. Project statistics describe recorded delivery activity, not working hours or personal productivity. Do not install the optional pilot profile without a project decision.
:::

---

<!-- slide: W24 -->
# Do not overwrite existing projects

- Read git status before setup
- Preserve local rules and presets
- Keep changes small and reviewable
- Never repair by applying blanket --force

```text
git status --short
git diff
specify preset list
```

::: notes
Location: container Bash in the application project. Git diff omits untracked files, so inspect status and new files too. Clarify backup and impact before updates. The embedded Home Baseline is read-only, not a workshop edit target. No home sync runs automatically. Installers and host permissions differ outside this sandbox; there is no silent fallback.
:::

---

<!-- slide: W25 -->
# Our example: SysInfoTool

- A small console program using fictional data
- Choose one of the six language toolchains
- Collect no real user, host or network data
- Do not start implementation yet

::: notes
Possible request: a console program displays three predefined example values with German and English labels. Describe failure cases and success criteria before implementation. C#/.NET, Java, Go, Rust, Python and Swift are alternative toolchains, not simultaneous requirements. Python and PowerShell provide scripting foundations. This example needs no real API keys or provider calls.
:::

---

<!-- slide: W26 -->
# Constitution: project principles

- Durable rules for the application project
- State security, quality and responsibilities
- Distinguish MUST, SHOULD and MAY deliberately
- Read an existing constitution first

```text
$speckit-constitution
Review existing project principles for SysInfoTool.
Use fictional data only; no secrets or providers.
Show impacts on dependent artifacts.
No implementation, commit or push.
```

::: notes
Location: agent chat in the separately authorized application project. MUST is mandatory, SHOULD a recommendation with reasoned exceptions, MAY a permitted option. Constitution changes may affect dependent artifacts; make impacts visible. This example does not change the sandbox repository's constitution. Read and decide on each concrete change.
:::

---

<!-- slide: W27 -->
# Specify: describe requirements

- Describe audience, value and boundaries
- Require verifiability, not design details
- State non-goals explicitly
- Read and understand the resulting spec.md

```text
$speckit-specify
Specify SysInfoTool with three fictional example values.
Define DE/EN output, failure cases and success criteria.
No real system-data collection or network connection.
No implementation or Git delivery.
```

::: notes
A functional requirement describes desired behavior; an acceptance criterion makes fulfillment checkable. A user story explains a person's need. Introduce these terms using a small example. Name an existing requirements document as binding input rather than inventing replacement requirements. Active sandbox specifications remain untouched.
:::

---

<!-- slide: W28 -->
# Clarify: resolve important decisions

- Ask only questions with material consequences
- Ask one question at a time
- At most five questions per pass
- Record decisions and reasoning traceably

```text
$speckit-clarify
Inspect the active SysInfoTool spec for material ambiguity.
At most five questions, one at a time, with a recommendation.
No implementation; preserve recorded decisions.
```

::: notes
Material decisions include which data may be shown and what happens for an unknown language. Do not ask merely about preferred wording. Technical details may belong in planning. Repeat only when new material questions arise, not until an arbitrary green claim appears.
:::

---

<!-- slide: W29 -->
# Clarify or defer deliberately?

- Decide requirements and safety boundaries now
- Put implementation details in the later plan
- Record deferred items with owner and trigger
- Stop on blockers instead of inventing approval

::: notes
Deferred means deliberately postponed, not completed. Example: plan internal file layout later, but decide permitted data before planning. Open items need owner, follow-up and re-evaluation trigger. A non-specialist must understand which actions remain prohibited until a decision.
:::

---

<!-- slide: W30 -->
# Plan: prepare the technical approach

- Translate requirements into a suitable technical approach
- Preserve security and architecture boundaries
- Plan relevant evidence and tests
- Do not implement yet

```text
$speckit-plan
Plan only the active SysInfoTool specification.
Use existing project conventions and test tools.
Explain N/A and document missing evidence.
Do not generate tasks or start implementation.
```

::: notes
A plan describes how: components, interfaces, data flow, failure cases and evidence. Invent no database or API if the example needs neither. N/A means not applicable and needs a reason. Planned tests have not passed yet. Assess the applicability of all six foundational governance areas.
:::

---

<!-- slide: W31 -->
# Checklist: requirements quality

- Are statements clear and complete?
- Are criteria measurable and consistent?
- Does each item explain how to review it?
- This is not an implementation or functional test

```text
$speckit-checklist
Assess the quality of the active requirements.
Each item needs a reference and review instruction.
No builds, runtime tests or implementation checks.
```

::: notes
Example: is the language for an unknown selection specified unambiguously? Review instructions name the text and sufficient quality criteria. Do not ask whether language switching works; that belongs to a later functional test. Name gaps and obtain explicit correction authority instead of hiding automatic remediation.
:::

---

<!-- slide: W32 -->
# Tasks: small actionable steps

- Cover every requirement with tasks
- Name dependencies and concrete files
- Use [P] only for truly independent work
- Mark [X] only after completion

```text
$speckit-tasks
Generate tasks.md from the active spec.md and plan.md.
Name dependencies, files and validation.
No implementation, commit or push.
```

::: notes
An MVP is the smallest useful, independently checkable increment. User-story tasks use agreed story IDs. [P] does not authorize spawning agents without permission. Plan TDD tasks only where product logic and a real test route exist; do not inflate documentation work with invented runtime tests.
:::

---

<!-- slide: W33 -->
# Analyze: compare artifacts read-only

- Check consistency across spec, plan and tasks
- Map requirements and success criteria to tasks
- Report stable finding IDs and severity
- Change no files during Analyze

```text
$speckit-analyze
Review the active spec, plan and tasks strictly read-only.
Report gaps, conflicts and missing task coverage.
No remediation, builds, commits or pushes.
```

::: notes
Traceability maps requirements to tasks and later evidence. Analysis must invent no approval or silently drop findings. Current analysis is not platform acceptance. Reuse review goals for a new revision and claim historical improvement only with an actual previous analysis.
:::

---

<!-- slide: W34 -->
# Fix findings with a bounded request

- Name findings and affected files first
- Authorize corrections separately
- Recheck the relevant changed revision
- Stop when decisions remain unresolved

```text
Fix only the confirmed findings C1 and C2.
Preserve safety boundaries and the agreed scope.
No feature implementation, commit or push.
Report changes; perform a read-only analysis afterwards.
```

::: notes
There is no fixed repeat count and no instruction to review indefinitely. A focused pass, concrete fix and targeted recheck suffice when no relevant blockers remain. Do not bypass constitution MUST violations or confirmed severe findings by changing status labels. Do not replace human risk decisions.
:::

---

<!-- slide: W35 -->
# Implement: only with current authority

- Reread the current spec, plan and tasks
- Check prerequisites and checklists
- Implement in dependency order
- Record actual tests and stopping conditions

```text
$speckit-implement
Implement only the authorized SysInfoTool tasks.
Mark tasks complete only after verifiable completion.
Stop on secrets or missing human decisions.
No commit, push, container rebuild or hosting changes.
```

::: notes
Adapt the example to the actual project. Project tests and rebuilding the sandbox image are different actions. A fresh agent session may help but must reread repository rules, current artifacts and recorded decisions. Do not demand an empty context that discards safeguards. Define progress and stop rules for long runs; do not leave sensitive work unattended.
:::

---

<!-- slide: W36 -->
# Review, tests and safe data

- Review changed and new files with a human
- Distinguish planned tests from executed tests
- Save project files in the intended mount
- Decide on commit and push separately

```text
git status --short
git diff
# Im Anwendungsprojekt / in the application project:
# dokumentierte Projekttests / documented project tests
```

::: notes
Location: container shell in the application project. Expect a reviewable diff and visible new files. A smoke test is a small functional check, not full security or accessibility acceptance. Persistent agent state may contain credentials; never copy it into the repository. Follow the defined process for SBOMs and audit evidence.
:::

---

<!-- slide: W37 -->
# End the session cleanly

- Save work in the project mount
- Leave the container shell
- Run the audit wrapper on the host
- Do not remove volumes during routine shutdown

```text
# Host, Bash:
bash scripts/compose-down-with-audit.sh --podman
# Host, PowerShell 7 (Alternative):
.\scripts\compose-down-with-audit.ps1 -Engine podman
```

::: notes
Prerequisite: back in the host terminal at the sandbox checkout. Expect successful metadata export before compose down, retaining volumes. Stop on export failure instead of bypassing the wrapper. Never add -v or -Volumes to routine shutdown; these can delete agent data and sign-in state. OpenCode 2 file metadata is not full session coverage. Stopping the Podman machine is a separate host action. See daily workflow.
:::

---

<!-- slide: W38 -->
# Key terms to remember

- Spec: checkable requirements; plan: technical approach
- Tasks: small steps; evidence: actual proof
- Open: unresolved; N/A: justified non-applicability
- Ready grants no execution, product or release approval

::: notes
Additional terms: MSL names the six language paths here, not guaranteed code safety. STRIDE supports threat modeling. CIA means confidentiality, integrity and availability. SBOM lists components; VEX records reasoned vulnerability statements; SLSA concerns supply-chain evidence. Applicability depends on the project. See the learner glossary for details.
:::

---

<!-- slide: W39 -->
# Next step and materials

- Choose a learning path and suitable toolchain
- Start one small, explicitly authorized project
- Discuss questions and missing evidence with the instructor
- Keep the Markdown, speaker notes and profile matrix

::: notes
Materials: the learner index, learning paths, installation, agent/Spec Kit and daily workflow guides; current safety boundaries are in the dated follow-up register. The profile matrix in this Markdown source and the speaker notes comes from existing local configuration. It records a revision, not an instruction to install every package. No institutional access or external presentation template is needed.

Local pilot revision, not installation authority:

| Preset | Version | Priority |
|---|---|---|
| security-governance | v0.7.4 | 10 |
| secure-development-assurance-governance | v0.1.8 | 15 |
| architecture-governance | v0.6.5 | 20 |
| isaqb-architecture-governance | v0.2.5 | 30 |
| a11y-governance | v0.4.6 | 40 |
| cross-platform-governance | v0.2.5 | 50 |
| agent-parity-governance | v0.4.5 | 60 |
| model-routing-governance | v0.1.7 | 61 |
| intake-authoring-governance | v0.3.10 | 64 |
| intake-review-governance | v0.2.7 | 65 |
| intake-sequencing-governance | v0.2.11 | 66 |
| autonomous-run-governance | v0.4.7 | 70 |
| parallel-autonomous-run-governance | v0.2.9 | 80 |
| project-statistics-governance | v0.1.3 | 90 |

https://github.com/hindermath/absdd-image-sandbox
https://github.com/github/spec-kit/tree/v1.2.3

:::

---
