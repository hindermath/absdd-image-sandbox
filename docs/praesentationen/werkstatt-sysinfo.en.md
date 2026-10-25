---
title: "SysInfoTool: from request to verified program"
lang: en-GB
date: 2026-10-25
---

<!-- slide: S01 -->
# SysInfoTool

- Build a personal program from Hello World
- Use Spec Kit and agentic AI deliberately
- For first-year apprentices and non-specialist developers

::: notes
AI means artificial intelligence. An agent can operate tools and change files;
you remain responsible for requests, review and decisions. Read the introductory
workshop first. This workshop describes a product; practice starts only with
your explicit authority in your personal learning repository.
:::

<!-- slide: S02 -->
# What is system information?

- CPU, memory, disk, network, system and processes
- A snapshot with time and source
- Available, partially available or unavailable values

::: notes
CPU means processor. A snapshot stores information at one point in time.
Predict what a missing network address means: excluded or unavailable does
not simply mean an empty string. Explain value, status and reason in your own words.
:::

<!-- slide: S03 -->
# A container is not the physical host

- The program runs as adedev inside Linux
- Visible CPU and memory may reflect VM constraints
- A mount exposes real host files
- Request no privileges or additional mounts

::: notes
VM means virtual machine. Podman often uses one on macOS and Windows.
Container readings are not the physical computer's inventory. Do not escape
the sandbox to fill missing information. Systems integration and electronics
perspectives focus on these observation boundaries.
:::

<!-- slide: S04 -->
# Fictional first, real collection by choice

- Defaults and tests use labelled fictional data
- Real collection requires --collect container
- Network and processes need extra per-run opt-in
- No process command lines, users or credentials

::: notes
Opt-in is an explicit choice. `--include-sensitive network,processes` applies
only to that real collection run, never future runs. Read basis.md for the
exact contract. Show excluded categories and reasons. Never copy real exports
into agent prompts without review.
:::

<!-- slide: S05 -->
# Choose one language

- C#, Java, Python, Rust, Go or Swift
- Same product functions and acceptance criteria
- Select idiomatic libraries in the technical plan
- Do not generate six solutions at once

::: notes
Acceptance describes observable results. The agent must not silently select
your language. Record it before Specify. PowerShell supports environment
scripting, but is not a seventh product language for this workshop. A later
language change is a separate decision.
:::

<!-- slide: S06 -->
# Six stages with explicit handovers

- SYS-00 CLI and JSON/CSV/XML → SYS-01 YAML
- SYS-02 SQLite → SYS-03 REST API
- SYS-04 documentation → SYS-05 evidence review
- Accept one stage before starting the next

::: notes
CLI means command-line interface. JSON, CSV, XML and YAML are data formats.
SQLite stores data in a file. S12 explains REST. Each transition requires human
acceptance and current evidence. The shipped series is Draft; every stage is
Pending, not already learned or authorized. The package contains the full order view.
:::

<!-- slide: S07 -->
# Separate request and specification

- Intake: goal, limits and measurable acceptance
- Specify the product, not the workshop
- Clarify only material ambiguity
- One question at a time, no endless loops

::: notes
Read SYS-00 and basis.md. Predict which requirement prevents collection on
--help, then find AC-02. The example is a Codex skill prompt, not a shell
command. Other integrations may use different installed command names.
:::

```text
$speckit-specify Use intakes/00-cli.md and basis.md.
Specify only SYS-00 in the recorded language.
No implementation, commit or push.
```

<!-- slide: S08 -->
# Plan, Checklist, Tasks and Analyze

- Plan fixes components, libraries and data contracts
- Checklist evaluates requirement quality
- Tasks divide work into verifiable steps
- Analyze compares artifacts without changing them

::: notes
Specification, plan and tasks are different work products, called artifacts.
A green requirements checklist does not prove an exporter works. Authorize
specific remediation separately and recheck affected evidence. Never repeat
checks merely to obtain a preferred approval.
:::

<!-- slide: S09 -->
# SYS-00: actually verify an export

- Use the same fixture for JSON, CSV and XML
- Read the file with the correct parser
- Compare values, category, state and source
- Preserve existing files on failure

::: notes
A parser reads structured data. A .json filename proves no valid JSON.
Basic task: predict one CPU value and status. Extension: explain how multiple
category values map to CSV rows. Decide this in the plan before generating code.
:::

<!-- slide: S10 -->
# SYS-01: YAML extends the contract

- Another format, not new system data
- Full and category exports preserve meaning
- Unicode and multiline text remain data
- No executable type tags or import feature

::: notes
YAML supports varied type notation. This task needs safe data, not object
construction. Use fictional strings that resemble syntax and compare the
parsed result. Keep regression tests for all previous formats.
:::

<!-- slide: S11 -->
# SYS-02: persistence is a promise

- Save ID, time and source with the snapshot
- Read the same values after restart
- Transactions prevent partial snapshots
- A database is neither build output nor a Git backup

::: notes
A transaction groups changes: all or nothing. Before a simulated write failure,
predict the allowed snapshot count afterwards. Use personal temporary test
databases only. Protect backups outside Git. Data/process analysis traces
how a snapshot moves through the system.
:::

<!-- slide: S12 -->
# SYS-03: REST works on stored data

- API means Application Programming Interface
- HTTP operations read or change snapshots
- No request may trigger fresh system collection
- Local HTTPS, limits and errors are contractual

::: notes
REST here means an HTTP resource contract. GET reads, POST creates, PUT replaces,
DELETE removes: CRUD, Create Read Update Delete. Replace the collector with
a test double that fails if called. HTTP CRUD must still pass. This proves
separation better than a comment. Port 5113 remains local to the learning setup.
:::

<!-- slide: S13 -->
# SYS-04: documentation is product work

- Code reference from language-native comments
- CLI help with options and exit codes
- API reference from current OpenAPI
- Generating documents starts no service

::: notes
OpenAPI is a machine-readable HTTP contract. A public code API can instead be
a method; distinguish them. Predict what happens if generator inputs are
missing: report failure rather than present stale output as current. Use
fictional examples only.
:::

<!-- slide: S14 -->
# SYS-05: evidence, not invented approval

- Map requirements and controls to evidence
- Explain Applicable, N/A and Open
- Open needs owner, follow-up and trigger
- Source adoption does not accept risk

::: notes
Evidence is inspectable proof. Applicable means relevant, N/A not applicable,
Open unresolved. Installing a guideline fulfils no control by itself. Separate
technical tests, human acceptance and formal approval. Controls applied since
SYS-00; this stage reviews their evidence.
:::

<!-- slide: S15 -->
# Shared review, different perspectives

- Basic: explain one success and one failure
- Development: connect code and test
- Operations/networking: describe boundaries and rights
- Management: justify value, effort and acceptance

::: notes
Choose an occupational task from the workshop index. No perspective gets fewer
protections. At least 80 % scoped own-code coverage supplies evidence, not
a quality certificate. Human learner/accessibility review remains separate.
:::

<!-- slide: S16 -->
# Prepare the first personal request

- Copy the SysInfo package into an empty personal repo
- Record language and working directory
- Review the complete series and decide on start
- Begin SYS-00 only, without skipping ahead

::: notes
An optional template copy is the personal sandbox, not the SysInfo product;
it inherits no acceptance and the profile is not enabled. Use the
[SysInfo package](../lernwerkstaetten/sysinfo/README.md) and
[transfer/workflow guide](../lernwerkstaetten/README.md). Answer SYS-00's
learning question before starting a prompt. Instructor answers are separate.
These slides execute nothing themselves.
:::
