# Repository Guidelines

## Active Compliance Work Queue

This repository has open audit findings against GWDG guideline `RL-SE-001` v2.1.0 ("Sichere Softwareentwicklung") and checklist `CL_12` v1.0 ("Agentische KI in Sandbox-Umgebungen"). The complete work list with concrete tasks, acceptance criteria, verification steps, and escalation rules is in `COMPLIANCE-PLAN_RL-SE-001.md`.

**Read `COMPLIANCE-PLAN_RL-SE-001.md` at the start of every Codex session.** That file is the single source of truth for:

- the priority order of open work (P0 must run first, then P1, P2, P3);
- the per-task commit and pull request conventions used for these changes;
- the items that must NOT be handled by an agent and have to be escalated to a human (API key rotation, formal sandbox approval, platform-side branch protection rules, QISMS register entries).

At the end of every Codex session, append a short session log under `docs/security/agent-session-log/<YYYY-MM-DD-HHMM>.md` as required by the plan. The log records which plan IDs were completed, partially completed, or escalated.

The plan and these guidelines work together: this `AGENTS.md` file describes the repository conventions; `COMPLIANCE-PLAN_RL-SE-001.md` describes the audit-driven work to bring those conventions into provable conformance.

## Project Structure & Module Organization

This repository contains a small Docker-based Opencode, .NET, and Spec Kit environment, not an application codebase.

- `Dockerfile`: builds from the shared `agent-sandbox` image pinned by digest and installs the current .NET SDK package, Java JDK 21, Maven, pinned Go and Rust toolchains, Python, pinned `opencode-ai` and `@openai/codex`, `uv`, `specify-cli`, and common CLI helper tools.
- `compose.yml`: defines the `ade` service, builds the local image, and mounts local state.
- The container runs commands as the Linux user `adedev`; keep home-directory paths under `/home/adedev`.
- `opencode.jsonc`: configures the `chat-ai` provider, models, and agents. Keep comments useful for first-year IT specialist apprentices.
- Codex CLI state is stored in the `codex_data` Docker volume mounted at `/home/adedev/.codex`; do not replace this with a bind mount to a committed directory.
- `opencode.env.example`: documents the required `GWDG_API_KEY` variable.
- `workspace/`: mounted into the container as `/workspace`; place working project files there.
- `ADE_DEV_SANDBOX_DIR`: host checkout of this repository mounted into the container as `/ade-dev-sandbox` for controlled repository maintenance tasks from inside the container.
- `RIDER_PROJECTS_DIR`: host directory mounted into the container as `/rider-projects` for Rider projects.
- `JAVA_PROJECTS_DIR`: host directory mounted into the container as `/java-projects` for Java, Maven, and Spring Boot projects.
- `java-projects/`: local fallback mount for `/java-projects` when `JAVA_PROJECTS_DIR` is not set.
- `dotnet/ContainerBuild.props`: mounted into `/dotnet-config` and loaded through `DirectoryBuildPropsPath` to redirect .NET build artifacts to `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: installed as `/usr/local/bin/dotnet` to filter one known workload verification noise line while preserving real output and exit codes.
- `spec-kit/patch-specify-cli.py`: patches Spec Kit copy behavior so initialization works better on Windows/WSL bind mounts.
- `README.md`: user-facing setup and operation guide.

There is currently no `src/`, `tests/`, or asset directory.

## Build, Test, and Development Commands

Run commands from the repository root:

```bash
docker compose config --no-interpolate
```

Validates the Compose file without printing values from `opencode.env`.

```bash
docker compose up -d
```

Builds the image if needed and starts the `ade` container.

```bash
docker compose exec ade bash
```

Opens a shell inside the running container.

On macOS or Windows with Podman, use the equivalent `podman compose ...` commands. Initialize and start the Podman machine before running Compose commands:

```bash
podman machine init
podman machine start
podman compose build --pull
podman compose up -d
podman compose exec ade bash
```

On macOS with Podman Desktop, do not assume Docker Desktop is required just because `podman info` or `podman build` fails from the terminal. If Podman Desktop is running but the CLI points at a stale `ssh://core@127.0.0.1:<port>` connection, check `/var/run/docker.sock`; Podman Desktop may expose a Docker-compatible socket there. In that case build with `docker --host unix:///var/run/docker.sock compose build --pull` and treat the resulting image as stored in the Podman machine, whose logical store is `/var/home/core/.local/share/containers/storage` and whose macOS disk is under `~/.local/share/containers/podman/machine/applehv/`.

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
docker compose down
docker compose down -v
```

Stops the environment. The `-v` variant also removes persistent Opencode data.

## Coding Style & Naming Conventions

Use two-space indentation for JSON and YAML. Keep shell commands simple and copyable. Use lowercase file names unless an ecosystem convention requires otherwise, such as `Dockerfile`, `README.md`, and `AGENTS.md`.

Prefer explicit configuration over hidden behavior. Keep secrets out of tracked files.

Every `ARG` in `Dockerfile` must have an immediately preceding Renovate metadata comment with a matching `argName`. Use the generic form `# renovate: datasource=<renovate-datasource> depName=<dependency-name> versioning=<versioning> argName=<ARG_NAME>` when the value is a simple version. Add or update a dedicated `renovate.json` custom manager when the value needs special parsing, and keep `docs/security/dependency-update-policy.md` in sync. The local pre-commit hook `dockerfile-arg-renovate-metadata` enforces this for current and future Dockerfile `ARG` lines.

## Testing Guidelines

There is no test framework in this repository. Before committing, run:

```bash
docker compose config --no-interpolate
```

For Dockerfile changes, also run:

```bash
docker compose build --pull
```

The `--pull` flag is still useful for registry access checks, but the Dockerfile pins the registry-hosted `agent-sandbox` base image by digest for reproducible builds. Update the digest deliberately in the Dockerfile when the base image should change.

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

On macOS or Windows with Podman, the equivalent validation path is:

```bash
podman compose config --no-interpolate
podman compose build --pull
```

If `podman compose` is not available on the local installation, use `podman-compose` with the same arguments.

Do not require a real API key for validation unless the change explicitly affects live Opencode usage.

For .NET projects under `/rider-projects`, keep `bin`, `obj`, and AppHost output off the Windows bind mount. The mounted `ContainerBuild.props` sends build output to the `dotnet_build` volume at `/dotnet-build` and imports repository-specific `Directory.Build.props` files when present.

For Java projects, use `/java-projects` and prefer project-local Maven or Gradle wrappers when a repository provides them. The container includes JDK 21 and Maven for baseline Java and Spring Boot development. Gradle and Spring Boot CLI are not installed globally unless this repository is intentionally extended.

For Go projects, use `/workspace` unless a project-specific mount is configured. Keep dependencies in `go.mod`, run `gofmt`/`go test ./...`, and add web frameworks such as `gin`, `fiber`, or `chi` per project instead of installing them globally.

For Rust projects, use `/workspace` unless a project-specific mount is configured. Keep dependencies in `Cargo.toml`, run `cargo fmt`, `cargo clippy -- -D warnings`, and `cargo test`. Add frameworks such as `tokio`, `axum`, `actix-web`, or `serde` per project instead of installing them globally.

ASP.NET apps must bind to `0.0.0.0` inside the container to be reachable from Windows. Compose publishes `127.0.0.1:5100-5199:5100-5199`; keep sample web app ports in that range unless the Compose file is updated.

The Compose environment disables general .NET workload update notifications with `DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=true` and disables the MSBuild workload resolver with `MSBuildEnableWorkloadResolver=false`. The Dockerfile also sets `dotnet workload config --update-mode manifests` as root to reduce workload verification noise with .NET 10 SDK images. Do not run this command after switching to the `adedev` user because it needs elevated privileges. Install real workloads explicitly in the Dockerfile and re-enable the resolver if a project requires MAUI, WebAssembly, or another optional SDK workload.

The `dotnet` wrapper must only filter the exact workload verification message. Do not broaden the filter, because normal warnings and build errors must stay visible.

Spec Kit is installed with `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.3`. Keep the version pinned unless intentionally upgrading and updating documentation.

For Spec Kit initialization under `/rider-projects`, prefer `specify init . --integration opencode --force`. If prompted for script type, choose `sh` in this Linux container. For each application repository, decide whether `.opencode/` or sensitive parts of it belong in that repository's `.gitignore`.

Spec Kit is patched after installation to avoid Python metadata-preserving copy operations on host bind mounts. Keep this patch narrow; it should only affect copying behavior, not Spec Kit command semantics.

## Commit & Pull Request Guidelines

The current history uses short, imperative commit messages, for example `Update opencode docker setup` and `Add README table of contents`.

For pull requests, include:

- a short summary of the change
- any Docker or Compose commands used for validation
- notes about configuration or secret handling
- screenshots only if documentation rendering or UI output is relevant

GitLab repository governance lives in this repository and in the GitLab project
settings. `.gitlab/CODEOWNERS` and
`.gitlab/merge_request_templates/Default.md` are repository-side guidance.
Platform-side enforcement such as protected-branch rules, Code Owner approval,
and push rules must be configured separately in GitLab by an Owner or Admin.
For the current GitLab CE status and signed-commit limitations, see
`docs/security/branch-protection.md`.

## Security & Configuration Tips

Never commit `opencode.env`; it contains `GWDG_API_KEY` and is ignored by `.gitignore`. Keep local secret files restricted:

```bash
chmod 600 opencode.env
```

If copying credentials from `~/.local/share/opencode/auth.json`, only write the key into `opencode.env` and do not print it in logs or documentation.

Run the repository secret scan before committing:

```bash
pre-commit install
pre-commit run --all-files
```

If `pre-commit` is not installed in the current environment, install it first with `uv tool install pre-commit` or run it via `uvx pre-commit run --all-files`.

Audit text for P1-3: "Client-side Control, in GitLab CE nicht vollständig serverseitig erzwingbar; zentrale Push-Blockade nur mit GitLab Ultimate Secret Push Protection oder Admin-Server-Hook."

Run the agent-session audit export at least once per workday and always before removing Compose volumes. The standard stop path is the wrapper, because it exports metadata before running `compose down`:

```bash
bash scripts/compose-down-with-audit.sh --podman -v
```

On Windows PowerShell with Podman:

```powershell
.\scripts\compose-down-with-audit.ps1 -Engine podman -Volumes
```

If the wrapper cannot be used, run `audit-export` inside the container before `docker compose down -v` or `podman compose down -v`. The image entrypoint also runs `audit-export` as a best-effort hook on graceful container shutdown when `ADE_AUDIT_ON_STOP=true` is set, but hard kills or host aborts can still skip it.

The export writes metadata only to `/audit/YYYY-MM-DD.jsonl`. Do not extend it to include prompt text, response text, raw session payloads, or secrets. The default host directory is `audit-logs/`; generated JSONL files stay untracked.
