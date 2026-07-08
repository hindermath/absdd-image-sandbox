# Repository Guidelines

## Active Compliance Work Queue

This repository maintains open sandbox-governance findings against the generic Secure Development Guideline and checklist `CL_12` ("Agentic AI in Sandbox Environments") from `docs/secure-development`. The complete work list with concrete tasks, acceptance criteria, verification steps, and escalation rules is in `COMPLIANCE-PLAN_RL-SE-001.md`.

**Read `COMPLIANCE-PLAN_RL-SE-001.md` at the start of every GitHub Copilot session.** That file is the single source of truth for:

- the priority order of open work (P0 must run first, then P1, P2, P3);
- the per-task commit and pull request conventions used for these changes;
- the items that must NOT be handled by an agent and have to be escalated to a human (API key rotation, formal sandbox approval, platform-side branch protection rules, external management-system register entries).

At the end of every GitHub Copilot session, append a short session log under `docs/security/agent-session-log/<YYYY-MM-DD-HHMM>.md` as required by the plan. The log records which plan IDs were completed, partially completed, or escalated.

The plan and these guidelines work together: this `.github/copilot-instructions.md` file describes the repository conventions; `COMPLIANCE-PLAN_RL-SE-001.md` describes the generic secure-development and sandbox-governance work that brings those conventions into provable conformance.

## Secure-Development Neutralitaet / Secure Development Neutrality

Treat `docs/secure-development/` as the generic Secure-Development-Basis for
training, review, and hardening work. Do not describe it as a company policy,
internal guideline, or concrete management-system requirement.

Generic roles and placeholders such as organization, project owner, security
review, CISO/ISB/KIB, document repository, risk register, RoPA, provider, or
platform are allowed when they remain generic. Concrete organizations, private
URLs, local host paths, provider portals, account-specific defaults, external
document-management or security-management systems, or platform rules must be
removed, generalized, or marked as example, context, `N/A`, `Open`, or
project-specific evidence.

Spec-Kit runs against this baseline must create project-specific evidence.
Human-only items such as formal approval, external registers, secret rotation,
provider/model approvals, and platform branch protection must not be claimed as
completed by an agent.

## Project Structure & Module Organization

This repository contains a small Podman-based Opencode, .NET, and Spec Kit environment, not an application codebase.

- `Dockerfile`: builds from the Microsoft .NET SDK image in MCR pinned by digest and installs Java JDK 21, Maven, pinned Go and Rust toolchains, Python, pinned `opencode-ai` and `@openai/codex`, `uv`, `specify-cli`, and common CLI helper tools.
- `compose.yml`: defines the `ade` service, builds the local image, and mounts local state.
- `compose.home-baseline.yml`: optional Compose override that bind-mounts a user's own repository created from the `home-baseline` template into `/home/adedev/home-baseline-tmp`.
- The container runs commands as the Linux user `adedev`; keep home-directory paths under `/home/adedev`.
- `opencode.jsonc`: configures OpenCode safety defaults without an API key or preselected model. Keep comments useful for first-year IT specialist apprentices.
- Codex CLI state is stored in the `codex_data` Podman volume mounted at `/home/adedev/.codex`; do not replace this with a bind mount to a committed directory.
- `opencode.env.example`: documents that no OpenCode provider environment variable is required by this image.
- `workspace/`: mounted into the container as `/workspace`; place working project files there.
- `ADE_DEV_SANDBOX_DIR`: host checkout of this repository mounted into the container as `/ade-dev-sandbox` for controlled repository maintenance tasks from inside the container.
- `HOME_BASELINE_DIR`: optional host checkout of a user's own `home-baseline` template repository, used only with `compose.home-baseline.yml` and mounted into `/home/adedev/home-baseline-tmp`.
- `RIDER_PROJECTS_DIR`: host directory mounted into the container as `/rider-projects` for Rider projects.
- `JAVA_PROJECTS_DIR`: host directory mounted into the container as `/java-projects` for Java, Maven, and Spring Boot projects.
- `SECURE_CASE_TRACKER_PROJECTS_DIR`: host directory mounted into the container as `/secure-case-tracker-projects` for Secure CaseTracker learning and project work.
- `SECURE_SERVICE_HARVESTER_PROJECTS_DIR`: host directory mounted into the container as `/secure-service-harvester-projects` for Secure Service Harvester learning and project work.
- `SECURE_ORDER_DESK_PROJECTS_DIR`: host directory mounted into the container as `/secure-order-desk-projects` for Secure OrderDesk learning and project work.
- `java-projects/`: local fallback mount for `/java-projects` when `JAVA_PROJECTS_DIR` is not set.
- `secure-case-tracker-projects/`: local fallback mount for `/secure-case-tracker-projects` when `SECURE_CASE_TRACKER_PROJECTS_DIR` is not set.
- `secure-service-harvester-projects/`: local fallback mount for `/secure-service-harvester-projects` when `SECURE_SERVICE_HARVESTER_PROJECTS_DIR` is not set.
- `secure-order-desk-projects/`: local fallback mount for `/secure-order-desk-projects` when `SECURE_ORDER_DESK_PROJECTS_DIR` is not set.
- `dotnet/ContainerBuild.props`: mounted into `/dotnet-config` and loaded through `DirectoryBuildPropsPath` to redirect .NET build artifacts to `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: installed as `/usr/local/bin/dotnet` to filter one known workload verification noise line while preserving real output and exit codes.
- `spec-kit/patch-specify-cli.py`: patches Spec Kit copy behavior so initialization works better on Windows/WSL bind mounts.
- `README.md`: user-facing setup and operation guide.

There is currently no `src/`, `tests/`, or asset directory.

## Build, Test, and Development Commands

Run commands from the repository root:

```bash
podman-compose config
```

Validates the Compose file without printing values from `opencode.env` and
without requiring a running Podman machine.

```bash
podman compose up -d
```

Builds the image if needed and starts the `ade` container.

```bash
podman compose exec ade bash
```

Opens a shell inside the running container.

On macOS or Windows, initialize and start the Podman machine before running Compose commands:

```bash
podman machine init
podman machine start
podman compose build --pull
podman compose up -d
podman compose exec ade bash
```

Use `podman-compose config` for config-only validation. If `podman compose`
is not available for lifecycle actions on the local installation, use
`podman-compose` with the same arguments.

```bash
specify version
specify check
```

Verifies the Spec Kit CLI installation inside the container.

```bash
cd /rider-projects
```

Moves to the mounted Windows/Rider projects directory inside the container.

```bash
cd /home/adedev/home-baseline-tmp
```

Moves to the optional mounted `home-baseline` checkout when the container was
started with `compose.home-baseline.yml`. Do not clone `home-baseline` into the
image and do not hard-code a private host path; public users should create
their own repository via GitHub's "Use this template" flow and set
`HOME_BASELINE_DIR` locally.

```bash
podman compose down
podman compose down -v
```

Stops the environment. The `-v` variant also removes persistent Opencode data.

## Coding Style & Naming Conventions

Use two-space indentation for JSON and YAML. Keep shell commands simple and copyable. Use lowercase file names unless an ecosystem convention requires otherwise, such as `Dockerfile`, `README.md`, and `AGENTS.md`.

Prefer explicit configuration over hidden behavior. Keep secrets out of tracked files.

Every `ARG` in `Dockerfile` must have an immediately preceding Renovate metadata comment with a matching `argName`. Use the generic form `# renovate: datasource=<renovate-datasource> depName=<dependency-name> versioning=<versioning> argName=<ARG_NAME>` when the value is a simple version. Add or update a dedicated `renovate.json` custom manager when the value needs special parsing, and keep `docs/security/dependency-update-policy.md` in sync. The local pre-commit hook `dockerfile-arg-renovate-metadata` enforces this for current and future Dockerfile `ARG` lines.

## Agentische Skriptausfuehrung / Agentic Script Execution

Vor lokaler Automation zuerst das Betriebssystem erkennen. Wenn `pwsh`
verfuegbar ist, vorhandene PowerShell-7-Skripte oder Cmdlets bevorzugen und
auf diesem macOS-Host wegen Profil-Nebenwirkungen `pwsh -NoProfile` nutzen.
Fuer strukturierte lokale Automation ist C# ueber `.NET` oder `mono` ein
zulaessiger zweiter Weg, wenn Typisierung, Dateiformate oder
Wiederverwendbarkeit davon profitieren. Erst wenn PowerShell oder C# nicht
sinnvoll passen, die OS-nahe vorhandene Repo-Variante nutzen, in diesem
Repository typischerweise Bash, Podman-Compose-Befehle oder vorhandene
`scripts/`-Wrapper. Keine neue Sprache nur aus Bequemlichkeit einfuehren, wenn
ein bestehendes Repo-Skript denselben Zweck erfuellt.

*Before local automation, detect the operating system. If `pwsh` is available,
prefer existing PowerShell 7 scripts or Cmdlets and use `pwsh -NoProfile` on
this macOS host because the profile has side effects. For structured local
automation, C# via `.NET` or `mono` is an acceptable second option when typing,
file formats, or reuse benefit from it. Only use the OS-native existing
repository variant when PowerShell or C# does not fit, typically Bash, Podman
Compose commands, or existing `scripts/` wrappers in this repository. Do not
introduce a new language for convenience when an existing repository script
already solves the task.*

## Testing Guidelines

There is no test framework in this repository. Before committing, run:

```bash
podman-compose config
```

If `compose.home-baseline.yml` or the optional `HOME_BASELINE_DIR` workflow
changed, also run with a local checkout:

```bash
HOME_BASELINE_DIR=/path/to/home-baseline-tmp podman-compose -f compose.yml -f compose.home-baseline.yml config
```

For Dockerfile changes, also run:

```bash
podman compose build --pull
```

The `--pull` flag is still useful for registry access checks, but the Dockerfile pins the MCR-hosted .NET SDK base image by digest for reproducible builds. Update the digest deliberately in the Dockerfile when the base image should change.

Before distributing or handing over a rebuilt sandbox image, generate a
CycloneDX JSON SBOM from the final image:

```bash
scripts/build-and-sbom.sh --skip-build
```

On Windows, use the PowerShell variant:

```powershell
.\scripts\build-and-sbom.ps1 -SkipBuild
```

Generated `sboms/*.cdx.json` files are build artifacts. Keep `sboms/.gitkeep`
tracked, but do not commit generated SBOM files unless the release process
explicitly requires it.

After Dockerfile changes that affect language toolchains, also verify the container tools:

```bash
dotnet --info
java --version
javac --version
mvn --version
go version
gopls version
rustc --version
cargo --version
cargo clippy --version
python --version
```

Use `podman-compose config` for config-only validation. `podman compose config`
is only an additional local plausibility check when the Podman machine
or socket is healthy. If `podman compose` is not available for lifecycle
actions on the local installation, use `podman-compose` with the same
arguments.

When a local Podman machine or Compose provider does not use the intended
endpoint, do not treat a stored SSH connection such as `127.0.0.1:<port>` as
the repository default. First use the platform's native Podman setup. If an
explicit endpoint is needed, derive it from the local platform at runtime and
keep the concrete path or pipe out of committed files:

- macOS: read `.ConnectionInfo.PodmanSocket.Path` from
  `podman machine inspect podman-machine-default`, verify that it is a socket,
  and set `CONTAINER_HOST=unix://...` for Podman plus `DOCKER_HOST=unix://...`
  only for Docker-compatible API clients.
- Windows: use the `PodmanPipe` or socket reported by `podman machine inspect`
  or Podman Desktop; do not hard-code a named pipe or machine port in repo
  guidance.
- Linux: prefer direct local Podman without an endpoint override; when an API
  socket is needed for Docker-compatible tooling, use the active local Podman
  socket such as `unix://${XDG_RUNTIME_DIR}/podman/podman.sock`.

`DOCKER_HOST` in this repository means "Docker-compatible API endpoint for
Podman-backed tooling"; it does not reintroduce Docker as the target runtime.

For README or `AGENTS.md` changes that add or change documented copy-and-paste
commands, always run `git diff --check` as the minimum repository-side
plausibility check. If Podman or `podman-compose` is
available, also run the documented commands practically inside the container.
Use temporary directories under `/tmp` for these checks unless the documentation
explicitly describes a host-mounted project directory; this keeps sample
projects out of `/workspace`, `/rider-projects`, and the repository.

Treat platform coverage explicitly. A successful run on only one host platform
is a local plausibility check, not full cross-platform acceptance. When a change
claims or affects macOS, Windows/WSL2, and Linux/Ubuntu behavior, verify the
commands on each affected platform when those systems are available. For
config-only validation, prefer `podman-compose config`; for lifecycle commands,
use the platform's actual Podman Compose command (`podman compose` or
`podman-compose`) rather than assuming one spelling. If a platform, engine,
Podman socket, or network access for package downloads is unavailable, record
the skipped check and the reason in the pull request text or in the agent
session log.

For documented web-app examples, bind the app to `0.0.0.0` inside the container
and use a port from the published `5100-5199` range. During practical checks,
verify that the app responds over HTTP and stop any background test process
before ending the session.

Do not require a real API key for validation unless the change explicitly affects live Opencode usage.

For .NET projects under `/rider-projects`, keep `bin`, `obj`, and AppHost output off the Windows bind mount. The mounted `ContainerBuild.props` sends build output to the `dotnet_build` volume at `/dotnet-build` and imports repository-specific `Directory.Build.props` files when present.

For Java projects, use `/java-projects` and prefer project-local Maven or Gradle wrappers when a repository provides them. The container includes JDK 21 and Maven for baseline Java and Spring Boot development. Gradle and Spring Boot CLI are not installed globally unless this repository is intentionally extended.

For Go projects, use `/workspace` unless a project-specific mount is configured. Keep dependencies in `go.mod`, run `gofmt`/`go test ./...`, and add web frameworks such as `gin`, `fiber`, or `chi` per project instead of installing them globally.

For Rust projects, use `/workspace` unless a project-specific mount is configured. Keep dependencies in `Cargo.toml`, run `cargo fmt`, `cargo clippy -- -D warnings`, and `cargo test`. Add frameworks such as `tokio`, `axum`, `actix-web`, or `serde` per project instead of installing them globally.

ASP.NET apps must bind to `0.0.0.0` inside the container to be reachable from Windows. Compose publishes `127.0.0.1:5100-5199:5100-5199`; keep sample web app ports in that range unless the Compose file is updated.

The Compose environment disables general .NET workload update notifications with `DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=true` and disables the MSBuild workload resolver with `MSBuildEnableWorkloadResolver=false`. Install real workloads explicitly in the Dockerfile and re-enable the resolver if a project requires MAUI, WebAssembly, or another optional SDK workload.

The `dotnet` wrapper must only filter the exact workload verification message. Do not broaden the filter, because normal warnings and build errors must stay visible.

Spec Kit is installed with `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.3`. Keep the version pinned unless intentionally upgrading and updating documentation.

For Spec Kit initialization under `/rider-projects`, prefer `specify init . --integration opencode --force`. If prompted for script type, choose `sh` in this Linux container. For each application repository, decide whether `.opencode/` or sensitive parts of it belong in that repository's `.gitignore`.

Spec Kit is patched after installation to avoid Python metadata-preserving copy operations on host bind mounts. Keep this patch narrow; it should only affect copying behavior, not Spec Kit command semantics.

## Commit & Pull Request Guidelines

The current history uses short, imperative commit messages, for example `Update opencode podman setup` and `Add README table of contents`.

For pull requests, include:

- a short summary of the change
- any Podman Compose commands used for validation
- notes about configuration or secret handling
- screenshots only if documentation rendering or UI output is relevant

Repository governance lives partly in this repository and partly in the active
GitHub hosting platform. `.github/CODEOWNERS` and
`.github/pull_request_template.md` are repository-side guidance for reviews.
Platform-side enforcement such as repository rulesets, required checks, Code
Owner review, signed-commit policy, and admin bypass must be configured
separately by an Owner or Admin on GitHub. For the target public-readiness
ruleset and signed-commit notes, see `docs/security/branch-protection.md`.

## Security & Configuration Tips

Never commit `opencode.env`; it is ignored by `.gitignore` and may contain local provider secrets when a user adds their own OpenCode configuration. Keep local secret files restricted:

```bash
chmod 600 opencode.env
```

If copying credentials for a local OpenCode provider, only write the key into `opencode.env` and do not print it in logs or documentation.

Run the repository secret scan before committing:

```bash
pre-commit install
pre-commit run --all-files
```

If `pre-commit` is not installed in the current environment, install it first with `uv tool install pre-commit` or run it via `uvx pre-commit run --all-files`.

Audit text for P1-3: "Client-side Control; central secret push blocking
depends on the active hosting platform, edition, and admin-operated hooks."

Run the agent-session audit export at least once per workday and always before removing Compose volumes. The standard stop path is the wrapper, because it exports metadata before running `compose down`:

```bash
bash scripts/compose-down-with-audit.sh --podman -v
```

On Windows PowerShell with Podman:

```powershell
.\scripts\compose-down-with-audit.ps1 -Engine podman -Volumes
```

If the wrapper cannot be used, run `audit-export` inside the container before `podman compose down -v`. The image entrypoint also runs `audit-export` as a best-effort hook on graceful container shutdown when `ADE_AUDIT_ON_STOP=true` is set, but hard kills or host aborts can still skip it.

The export writes metadata only to `/audit/YYYY-MM-DD.jsonl`. Do not extend it to include prompt text, response text, raw session payloads, or secrets. The default host directory is `audit-logs/`; generated JSONL files stay untracked.

## Spec-Kit-Modell-Routing / Spec Kit Model Routing

- Modellwahl ist operative Agenten-Routing-Guidance, keine Feature-Anforderung. Modellnamen nicht in `spec.md`, `plan.md`, `tasks.md` oder einzelne Feature-Specs schreiben; diese Artefakte muessen reproduzierbar bleiben, auch wenn Modellnamen wechseln oder ein anderer KI-Agent verwendet wird.
- Der jeweilige Agent soll diese Empfehlungen auf seine aktuell verfuegbaren Modelle abbilden; keine feste Anbieter- oder Modellbindung ableiten.
- Fuer Spec-Kit-Spezifikation, Klaerung, Planung, Tasks und Analyse (`/speckit-specify`, `/speckit-clarify`, `/speckit-plan`, `/speckit-tasks`, `/speckit-analyze`; je nach Agent auch `/speckit.specify` usw.) das staerkste verfuegbare Frontier-Reasoning-/Coding-Modell bevorzugen.
- Fuer vollstaendige, lang laufende `/speckit-implement`-Laeufe das staerkste verfuegbare Long-Running-Agent-Modell bevorzugen; das Frontier-Modell nutzen, wenn maximale Urteilsguete wichtiger ist als Laufzeitstabilitaet.
- Fuer fokussierte Reviews oder CI-Fixes ein coding-optimiertes Modell bevorzugen.
- Fuer triviale Bereinigung, Formatierung oder risikoarme mechanische Edits ist ein schnelles kleines Coding-Modell akzeptabel.

*Model choice is operational agent-routing guidance, not a feature requirement. Do not pin model names in `spec.md`, `plan.md`, `tasks.md`, or individual feature specs; those artifacts must stay reproducible even when model names change or another AI agent is used. Each agent should map these recommendations to its currently available models; do not derive a fixed vendor or model requirement. For Spec-Kit specification, clarification, planning, task generation, and analysis (`/speckit-specify`, `/speckit-clarify`, `/speckit-plan`, `/speckit-tasks`, `/speckit-analyze`; or `/speckit.specify` etc. depending on the agent surface), prefer the strongest available frontier reasoning/coding model. For complete long-running `/speckit-implement` runs, prefer the strongest available long-running agent model; use the frontier model when maximum judgment quality is more important than runtime stability. For focused review or CI fixes, prefer a coding-optimized model. For trivial cleanup, formatting, or low-risk mechanical edits, a fast small coding model is acceptable.*

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
<!-- SPECKIT END -->
