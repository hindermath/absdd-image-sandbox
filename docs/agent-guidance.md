# Agentenregeln im Detail / Detailed agent guidance

Beginne mit [AGENTS.md](../AGENTS.md). Die Abschnitte gelten für die genannten Einstiege. Pfade in Beispielen beziehen sich auf den Repository-Stamm.

Start with [AGENTS.md](../AGENTS.md). The following sections apply to the named entry files. Paths in examples are relative to the repository root.

## Project Structure & Module Organization

Geltung / Applies to: `AGENTS.md`

This repository contains a Podman-based agentic learning sandbox with OpenCode, four required agent CLIs, and six required memory-safe language toolchains (.NET/C#, Java, Go, Rust, Python, and Swift) in the default `all` image. The five focused profiles install only their selected language toolchain plus .NET/C#. PowerShell 7 as a second scripting foundation, Node.js/npm as supporting tooling, Syft, and Spec Kit are shared; this is not an application codebase.

- `Dockerfile`: builds from the Microsoft .NET SDK image in MCR pinned by digest; `ADE_MSL_PROFILE` selects `dotnet`, `java`, `go`, `rust`, `python`, `swift`, or the full default `all`. It also provides version-checked PowerShell 7, Node.js/npm, pinned agent CLIs, Syft, `uv`, Spec Kit, and common tools.
- `compose.yml`: defines the `ade` service, builds the local image, and mounts separate persistent state volumes for OpenCode and all four required agents.
- `home-baseline.lock.json`: pins the public `home-baseline` release and exact commit embedded as a read-only shallow Git reference under `/opt/home-baseline`.
- `scripts/sync-home-baseline-runtime.sh`: installs the explicit three-mode wrapper that previews, checks, or applies manifest-defined Home Runtime content without Git side effects.
- `compose.home-baseline.yml`: optional Compose override that replaces the embedded reference with the learner's writable personal `home-baseline-source` checkout. The canonical user path is `/home/adedev/home-baseline-source`; `/home/adedev/home-baseline-tmp` remains a deprecated compatibility symlink.
- The container runs commands as the Linux user `adedev`; keep home-directory paths under `/home/adedev`.
- `opencode.jsonc`: configures OpenCode safety defaults without an API key or preselected model. Keep comments useful for first-year IT specialist apprentices.
- Agent state is isolated in `codex_data`, `claude_data`, `gemini_data`, and `copilot_data`; do not replace these with bind mounts to committed directories.
- `opencode.env.example`: documents the local web password; no OpenCode provider variable is required by the image.
- `workspace/`: mounted into the container as `/workspace`; place working project files there.
- `ADE_DEV_SANDBOX_DIR`: host checkout of this repository mounted into the container as `/ade-dev-sandbox` for controlled repository maintenance tasks from inside the container.
- `HOME_BASELINE_DIR`: optional persistent host checkout of the learner's personal `home-baseline-source` fork, used only with `compose.home-baseline.yml` and mounted over `/opt/home-baseline`; `/home/adedev/home-baseline-source` is canonical and `/home/adedev/home-baseline-tmp` is transitional.
- `RIDER_PROJECTS_DIR`: host directory mounted into the container as `/rider-projects` for Rider projects.
- `JAVA_PROJECTS_DIR`: host directory mounted into the container as `/java-projects` for Java, Maven, and Spring Boot projects.
- `POWERSHELL_PROJECTS_DIR`: host directory mounted into the container as `/powershell-projects` for PowerShell learning and project work.
- `GO_PROJECTS_DIR`: host directory mounted into the container as `/go-projects` for Go projects.
- `RUST_PROJECTS_DIR`: host directory mounted into the container as `/rust-projects` for Rust projects.
- `PYTHON_PROJECTS_DIR`: host directory mounted into the container as `/python-projects` for Python projects.
- `SWIFT_PROJECTS_DIR`: host directory mounted into the container as `/swift-projects` for Swift projects.
- `SECURE_CASE_TRACKER_PROJECTS_DIR`: host directory mounted into the container as `/secure-case-tracker-projects` for Secure CaseTracker learning and project work.
- `SECURE_SERVICE_HARVESTER_PROJECTS_DIR`: host directory mounted into the container as `/secure-service-harvester-projects` for Secure Service Harvester learning and project work.
- `SECURE_ORDER_DESK_PROJECTS_DIR`: host directory mounted into the container as `/secure-order-desk-projects` for Secure OrderDesk learning and project work.
- `java-projects/`: local fallback mount for `/java-projects` when `JAVA_PROJECTS_DIR` is not set.
- `powershell-projects/`: local fallback mount for `/powershell-projects` when `POWERSHELL_PROJECTS_DIR` is not set.
- `go-projects/`: local fallback mount for `/go-projects` when `GO_PROJECTS_DIR` is not set.
- `rust-projects/`: local fallback mount for `/rust-projects` when `RUST_PROJECTS_DIR` is not set.
- `python-projects/`: local fallback mount for `/python-projects` when `PYTHON_PROJECTS_DIR` is not set.
- `swift-projects/`: local fallback mount for `/swift-projects` when `SWIFT_PROJECTS_DIR` is not set.
- `secure-case-tracker-projects/`: local fallback mount for `/secure-case-tracker-projects` when `SECURE_CASE_TRACKER_PROJECTS_DIR` is not set.
- `secure-service-harvester-projects/`: local fallback mount for `/secure-service-harvester-projects` when `SECURE_SERVICE_HARVESTER_PROJECTS_DIR` is not set.
- `secure-order-desk-projects/`: local fallback mount for `/secure-order-desk-projects` when `SECURE_ORDER_DESK_PROJECTS_DIR` is not set.
- `dotnet/ContainerBuild.props`: mounted into `/dotnet-config` and loaded through `DirectoryBuildPropsPath` to redirect .NET build artifacts to `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: installed as `/usr/local/bin/dotnet` to filter one known workload verification noise line while preserving real output and exit codes.
- `spec-kit/patch-specify-cli.py`: patches Spec Kit copy behavior so initialization works better on Windows/WSL bind mounts.
- `README.md`: user-facing setup and operation guide.

There is currently no `src/`, `tests/`, or asset directory.

## Coding Style & Naming Conventions

Geltung / Applies to: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.github/agents/copilot-instructions.md`

Use two-space indentation for JSON and YAML. Keep shell commands simple and copyable. Use lowercase file names unless an ecosystem convention requires otherwise, such as `Dockerfile`, `README.md`, and `AGENTS.md`.

Prefer explicit configuration over hidden behavior. Keep secrets out of tracked files.

DE: Jedes `ARG` im `Dockerfile` braucht unmittelbar davor `# toolchain-pin: argName=<ARG_NAME>` und genau einen Eintrag in `scripts/config/toolchain-pins.json`. Dependabot pflegt den Basisimage-Digest im freigegebenen 10.0-Kanal; `toolchain-pins.yml` pflegt ARG-Versionen und ihre Architektur-Pruefsummen gemeinsam. Podman bleibt die Build-Engine. Keine automatischen Merges; bei fehlender Hersteller-Evidence bleibt das Update gesperrt. Neue Pins brauchen Provider-, Negativ- und Payload-Tests. Halte `docs/security/dependency-update-policy.md` synchron; der Hook `toolchain-pin-coverage` prueft die Abdeckung.

EN: Every Dockerfile ARG needs an immediately preceding `# toolchain-pin: argName=<ARG_NAME>` and exactly one record in `scripts/config/toolchain-pins.json`. Dependabot maintains the base-image digest within the approved 10.0 channel; `toolchain-pins.yml` updates ARG versions together with architecture checksums. Podman remains the build engine. No automatic merges; missing upstream evidence blocks an update. New pins need provider, negative and payload tests. Keep the dependency update policy synchronized; the `toolchain-pin-coverage` hook enforces coverage.

## Testing Guidelines

Geltung / Applies to: `AGENTS.md`

There is no test framework in this repository. Before committing, run:

```bash
podman-compose config
```

If `compose.home-baseline.yml` or the optional `HOME_BASELINE_DIR` workflow
changed, also run with a local checkout:

```bash
HOME_BASELINE_DIR=/path/to/home-baseline-source podman-compose -f compose.yml -f compose.home-baseline.yml config
```

For Dockerfile changes, also run:

```bash
podman compose build --pull
```

The `--pull` flag is still useful for registry access checks, but the Dockerfile pins the MCR-hosted .NET SDK base image by digest for reproducible builds. Update the digest deliberately in the Dockerfile when the base image should change.

Before distributing or handing over a rebuilt sandbox image, generate a
CycloneDX JSON SBOM from the final image:

```bash
bash scripts/build-and-sbom.sh --skip-build
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
pwsh --version
node --version
npm --version
swift --version
swiftc --version
command -v sourcekit-lsp
codex --version
claude --version
agy --version
copilot --version
syft version
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
and use a port from the published `5100-5198` app range; `5199` belongs to OpenCode. During practical checks,
verify that the app responds over HTTP and stop any background test process
before ending the session.

Do not require a real API key for validation unless the change explicitly affects live Opencode usage.

For .NET projects under `/rider-projects`, keep `bin`, `obj`, and AppHost output off the Windows bind mount. The mounted `ContainerBuild.props` sends build output to the `dotnet_build` volume at `/dotnet-build` and imports repository-specific `Directory.Build.props` files when present.

For Java projects, use `/java-projects` and prefer project-local Maven or Gradle wrappers when a repository provides them. The container includes JDK 25 LTS and Maven for baseline Java and Spring Boot development. Gradle and Spring Boot CLI are not installed globally unless this repository is intentionally extended.

For Go projects, use `/go-projects` unless a project-specific mount is configured. Keep dependencies in `go.mod`, run `gofmt`/`go test ./...`, and add web frameworks such as `gin`, `fiber`, or `chi` per project instead of installing them globally.

For Rust projects, use `/rust-projects` unless a project-specific mount is configured. Keep dependencies in `Cargo.toml`, run `cargo fmt`, `cargo clippy -- -D warnings`, and `cargo test`. Add frameworks such as `tokio`, `axum`, `actix-web`, or `serde` per project instead of installing them globally.

For Python projects, use `/python-projects` unless a project-specific mount is configured. The default `python` and `python3` use pinned CPython under `/opt/cpython`; `/usr/bin/python3` remains Ubuntu-managed for system tools. Keep virtual environments project-local or under an explicitly chosen cache path, and do not rely on globally installed application dependencies.

For PowerShell projects, use `/powershell-projects` unless a project-specific mount is configured. Run scripts with `pwsh -NoLogo -NoProfile`, keep modules project-local or explicitly versioned, and validate repository-owned scripts with PSScriptAnalyzer when that module is available.

For Swift projects, use `/swift-projects` unless a project-specific mount is configured. Keep dependencies in `Package.swift`, run `swift build`, `swift test`, and `swift run` for executable smoke checks. The image includes SourceKit-LSP for editors that attach through VS Code Dev Containers or another LSP-capable client.

ASP.NET apps must bind to `0.0.0.0` inside the container to be reachable from Windows. Compose publishes app ports `127.0.0.1:5100-5198:5100-5198` and reserves `127.0.0.1:5199:5199` for OpenCode.

The Compose environment disables general .NET workload update notifications with `DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=true` and disables the MSBuild workload resolver with `MSBuildEnableWorkloadResolver=false`. Install real workloads explicitly in the Dockerfile and re-enable the resolver if a project requires MAUI, WebAssembly, or another optional SDK workload.

The `dotnet` wrapper must only filter the exact workload verification message. Do not broaden the filter, because normal warnings and build errors must stay visible.

Spec Kit is installed from the exact release commit pinned in `Dockerfile`; the build verifies its package version. Keep the commit and version check synchronized when upgrading. See `docs/maintenance/toolchain-version-audit-2026-11-06.md` for the latest version audit.

For Spec Kit initialization under `/rider-projects`, prefer `specify init . --integration opencode --force`. If prompted for script type, choose `sh` in this Linux container. For each application repository, decide whether `.opencode/` or sensitive parts of it belong in that repository's `.gitignore`.

Spec Kit is patched after installation to avoid Python metadata-preserving copy operations on host bind mounts. Keep this patch narrow; it should only affect copying behavior, not Spec Kit command semantics.

## Project Structure & Module Organization

Geltung / Applies to: `CLAUDE.md`, `GEMINI.md`

This repository contains a Podman-based agentic learning sandbox with OpenCode, four required agent CLIs, six required memory-safe language toolchains (.NET/C#, Java, Go, Rust, Python, and Swift), PowerShell 7 as a second scripting foundation, Node.js/npm as supporting tooling, Syft, and Spec Kit; it is not an application codebase.

- `Dockerfile`: builds from the Microsoft .NET SDK image in MCR pinned by digest and provides the six required language toolchains (.NET/C#, Java, Go, Rust, Python, and Swift), a version-checked PowerShell 7 from the base image as a second scripting foundation, Node.js/npm as supporting tooling, pinned OpenCode, Codex, Claude Code, Antigravity CLI, GitHub Copilot CLI, Syft, `uv`, Spec Kit, and common CLI helper tools.
- `compose.yml`: defines the `ade` service, builds the local image, and mounts separate persistent state volumes for OpenCode and all four required agents.
- `home-baseline.lock.json`: pins the public `home-baseline` release and exact commit embedded as a read-only shallow Git reference under `/opt/home-baseline`.
- `scripts/sync-home-baseline-runtime.sh`: installs the explicit three-mode wrapper that previews, checks, or applies manifest-defined Home Runtime content without Git side effects.
- `compose.home-baseline.yml`: optional Compose override that replaces the embedded reference with the learner's writable personal `home-baseline-source` checkout. The canonical user path is `/home/adedev/home-baseline-source`; `/home/adedev/home-baseline-tmp` remains a deprecated compatibility symlink.
- The container runs commands as the Linux user `adedev`; keep home-directory paths under `/home/adedev`.
- `opencode.jsonc`: configures OpenCode safety defaults without an API key or preselected model. Keep comments useful for first-year IT specialist apprentices.
- Agent state is isolated in `codex_data`, `claude_data`, `gemini_data`, and `copilot_data`; do not replace these with bind mounts to committed directories.
- `opencode.env.example`: documents that no OpenCode provider environment variable is required by this image.
- `workspace/`: mounted into the container as `/workspace`; place working project files there.
- `ADE_DEV_SANDBOX_DIR`: host checkout of this repository mounted into the container as `/ade-dev-sandbox` for controlled repository maintenance tasks from inside the container.
- `HOME_BASELINE_DIR`: optional persistent host checkout of the learner's personal `home-baseline-source` fork, used only with `compose.home-baseline.yml` and mounted over `/opt/home-baseline`; `/home/adedev/home-baseline-source` is canonical and `/home/adedev/home-baseline-tmp` is transitional.
- `RIDER_PROJECTS_DIR`: host directory mounted into the container as `/rider-projects` for Rider projects.
- `JAVA_PROJECTS_DIR`: host directory mounted into the container as `/java-projects` for Java, Maven, and Spring Boot projects.
- `POWERSHELL_PROJECTS_DIR`: host directory mounted into the container as `/powershell-projects` for PowerShell learning and project work.
- `GO_PROJECTS_DIR`: host directory mounted into the container as `/go-projects` for Go projects.
- `RUST_PROJECTS_DIR`: host directory mounted into the container as `/rust-projects` for Rust projects.
- `PYTHON_PROJECTS_DIR`: host directory mounted into the container as `/python-projects` for Python projects.
- `SWIFT_PROJECTS_DIR`: host directory mounted into the container as `/swift-projects` for Swift projects.
- `SECURE_CASE_TRACKER_PROJECTS_DIR`: host directory mounted into the container as `/secure-case-tracker-projects` for Secure CaseTracker learning and project work.
- `SECURE_SERVICE_HARVESTER_PROJECTS_DIR`: host directory mounted into the container as `/secure-service-harvester-projects` for Secure Service Harvester learning and project work.
- `SECURE_ORDER_DESK_PROJECTS_DIR`: host directory mounted into the container as `/secure-order-desk-projects` for Secure OrderDesk learning and project work.
- `java-projects/`: local fallback mount for `/java-projects` when `JAVA_PROJECTS_DIR` is not set.
- `powershell-projects/`: local fallback mount for `/powershell-projects` when `POWERSHELL_PROJECTS_DIR` is not set.
- `go-projects/`: local fallback mount for `/go-projects` when `GO_PROJECTS_DIR` is not set.
- `rust-projects/`: local fallback mount for `/rust-projects` when `RUST_PROJECTS_DIR` is not set.
- `python-projects/`: local fallback mount for `/python-projects` when `PYTHON_PROJECTS_DIR` is not set.
- `swift-projects/`: local fallback mount for `/swift-projects` when `SWIFT_PROJECTS_DIR` is not set.
- `secure-case-tracker-projects/`: local fallback mount for `/secure-case-tracker-projects` when `SECURE_CASE_TRACKER_PROJECTS_DIR` is not set.
- `secure-service-harvester-projects/`: local fallback mount for `/secure-service-harvester-projects` when `SECURE_SERVICE_HARVESTER_PROJECTS_DIR` is not set.
- `secure-order-desk-projects/`: local fallback mount for `/secure-order-desk-projects` when `SECURE_ORDER_DESK_PROJECTS_DIR` is not set.
- `dotnet/ContainerBuild.props`: mounted into `/dotnet-config` and loaded through `DirectoryBuildPropsPath` to redirect .NET build artifacts to `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: installed as `/usr/local/bin/dotnet` to filter one known workload verification noise line while preserving real output and exit codes.
- `spec-kit/patch-specify-cli.py`: patches Spec Kit copy behavior so initialization works better on Windows/WSL bind mounts.
- `README.md`: user-facing setup and operation guide.

There is currently no `src/`, `tests/`, or asset directory.

## Testing Guidelines

Geltung / Applies to: `CLAUDE.md`, `GEMINI.md`

There is no test framework in this repository. Before committing, run:

```bash
podman-compose config
```

If `compose.home-baseline.yml` or the optional `HOME_BASELINE_DIR` workflow
changed, also run with a local checkout:

```bash
HOME_BASELINE_DIR=/path/to/home-baseline-source podman-compose -f compose.yml -f compose.home-baseline.yml config
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
pwsh --version
node --version
npm --version
swift --version
swiftc --version
command -v sourcekit-lsp
codex --version
claude --version
agy --version
copilot --version
syft version
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
and use a port from the published app range `5100-5198`. During practical checks,
verify that the app responds over HTTP and stop any background test process
before ending the session.

Do not require a real API key for validation unless the change explicitly affects live Opencode usage.

For .NET projects under `/rider-projects`, keep `bin`, `obj`, and AppHost output off the Windows bind mount. The mounted `ContainerBuild.props` sends build output to the `dotnet_build` volume at `/dotnet-build` and imports repository-specific `Directory.Build.props` files when present.

For Java projects, use `/java-projects` and prefer project-local Maven or Gradle wrappers when a repository provides them. The container includes JDK 25 LTS and Maven for baseline Java and Spring Boot development. Gradle and Spring Boot CLI are not installed globally unless this repository is intentionally extended.

For Go projects, use `/go-projects` unless a project-specific mount is configured. Keep dependencies in `go.mod`, run `gofmt`/`go test ./...`, and add web frameworks such as `gin`, `fiber`, or `chi` per project instead of installing them globally.

For Rust projects, use `/rust-projects` unless a project-specific mount is configured. Keep dependencies in `Cargo.toml`, run `cargo fmt`, `cargo clippy -- -D warnings`, and `cargo test`. Add frameworks such as `tokio`, `axum`, `actix-web`, or `serde` per project instead of installing them globally.

For Python projects, use `/python-projects` unless a project-specific mount is configured. The default `python` and `python3` use pinned CPython under `/opt/cpython`; `/usr/bin/python3` remains Ubuntu-managed for system tools. Keep virtual environments project-local or under an explicitly chosen cache path, and do not rely on globally installed application dependencies.

For PowerShell projects, use `/powershell-projects` unless a project-specific mount is configured. Run scripts with `pwsh -NoLogo -NoProfile`, keep modules project-local or explicitly versioned, and validate repository-owned scripts with PSScriptAnalyzer when that module is available.

For Swift projects, use `/swift-projects` unless a project-specific mount is configured. Keep dependencies in `Package.swift`, run `swift build`, `swift test`, and `swift run` for executable smoke checks. The image includes SourceKit-LSP for editors that attach through VS Code Dev Containers or another LSP-capable client.

ASP.NET apps must bind to `0.0.0.0` inside the container to be reachable from Windows. Compose publishes `127.0.0.1:5100-5198:5100-5198` for apps; port 5199 is reserved for OpenCode.

The Compose environment disables general .NET workload update notifications with `DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=true` and disables the MSBuild workload resolver with `MSBuildEnableWorkloadResolver=false`. Install real workloads explicitly in the Dockerfile and re-enable the resolver if a project requires MAUI, WebAssembly, or another optional SDK workload.

The `dotnet` wrapper must only filter the exact workload verification message. Do not broaden the filter, because normal warnings and build errors must stay visible.

Spec Kit is installed from the exact release commit pinned in `Dockerfile`; the build verifies its package version. Keep the commit and version check synchronized when upgrading. See `docs/maintenance/toolchain-version-audit-2026-10-25.md` for the latest version audit.

For Spec Kit initialization under `/rider-projects`, prefer `specify init . --integration opencode --force`. If prompted for script type, choose `sh` in this Linux container. For each application repository, decide whether `.opencode/` or sensitive parts of it belong in that repository's `.gitignore`.

Spec Kit is patched after installation to avoid Python metadata-preserving copy operations on host bind mounts. Keep this patch narrow; it should only affect copying behavior, not Spec Kit command semantics.

## Project Structure & Module Organization

Geltung / Applies to: `.github/copilot-instructions.md`, `.github/agents/copilot-instructions.md`

This repository contains a Podman-based agentic learning sandbox with OpenCode, four required agent CLIs, six required memory-safe language toolchains (.NET/C#, Java, Go, Rust, Python, and Swift), PowerShell 7 as a second scripting foundation, Node.js/npm as supporting tooling, Syft, and Spec Kit; it is not an application codebase.

- `Dockerfile`: builds from the Microsoft .NET SDK image in MCR pinned by digest and provides the six required language toolchains (.NET/C#, Java, Go, Rust, Python, and Swift), a version-checked PowerShell 7 from the base image as a second scripting foundation, Node.js/npm as supporting tooling, pinned OpenCode, Codex, Claude Code, Antigravity CLI, GitHub Copilot CLI, Syft, `uv`, Spec Kit, and common CLI helper tools.
- `compose.yml`: defines the `ade` service, builds the local image, and mounts separate persistent state volumes for OpenCode and all four required agents.
- `home-baseline.lock.json`: pins the public `home-baseline` release and exact commit embedded as a read-only shallow Git reference under `/opt/home-baseline`.
- `scripts/sync-home-baseline-runtime.sh`: installs the explicit three-mode wrapper that previews, checks, or applies manifest-defined Home Runtime content without Git side effects.
- `compose.home-baseline.yml`: optional Compose override that replaces the embedded reference with the learner's writable personal `home-baseline-source` checkout. The canonical user path is `/home/adedev/home-baseline-source`; `/home/adedev/home-baseline-tmp` remains a deprecated compatibility symlink.
- The container runs commands as the Linux user `adedev`; keep home-directory paths under `/home/adedev`.
- `opencode.jsonc`: configures OpenCode safety defaults without an API key or preselected model. Keep comments useful for first-year IT specialist apprentices.
- Agent state is isolated in `codex_data`, `claude_data`, `gemini_data`, and `copilot_data`; do not replace these with bind mounts to committed directories.
- `opencode.env.example`: documents that no OpenCode provider environment variable is required by this image.
- `workspace/`: mounted into the container as `/workspace`; place working project files there.
- `ADE_DEV_SANDBOX_DIR`: host checkout of this repository mounted into the container as `/ade-dev-sandbox` for controlled repository maintenance tasks from inside the container.
- `HOME_BASELINE_DIR`: optional persistent host checkout of the learner's personal `home-baseline-source` fork, used only with `compose.home-baseline.yml` and mounted over `/opt/home-baseline`; `/home/adedev/home-baseline-source` is canonical and `/home/adedev/home-baseline-tmp` is transitional.
- `RIDER_PROJECTS_DIR`: host directory mounted into the container as `/rider-projects` for Rider projects.
- `JAVA_PROJECTS_DIR`: host directory mounted into the container as `/java-projects` for Java, Maven, and Spring Boot projects.
- `POWERSHELL_PROJECTS_DIR`: host directory mounted into the container as `/powershell-projects` for PowerShell learning and project work.
- `SECURE_CASE_TRACKER_PROJECTS_DIR`: host directory mounted into the container as `/secure-case-tracker-projects` for Secure CaseTracker learning and project work.
- `SECURE_SERVICE_HARVESTER_PROJECTS_DIR`: host directory mounted into the container as `/secure-service-harvester-projects` for Secure Service Harvester learning and project work.
- `SECURE_ORDER_DESK_PROJECTS_DIR`: host directory mounted into the container as `/secure-order-desk-projects` for Secure OrderDesk learning and project work.
- `java-projects/`: local fallback mount for `/java-projects` when `JAVA_PROJECTS_DIR` is not set.
- `powershell-projects/`: local fallback mount for `/powershell-projects` when `POWERSHELL_PROJECTS_DIR` is not set.
- `secure-case-tracker-projects/`: local fallback mount for `/secure-case-tracker-projects` when `SECURE_CASE_TRACKER_PROJECTS_DIR` is not set.
- `secure-service-harvester-projects/`: local fallback mount for `/secure-service-harvester-projects` when `SECURE_SERVICE_HARVESTER_PROJECTS_DIR` is not set.
- `secure-order-desk-projects/`: local fallback mount for `/secure-order-desk-projects` when `SECURE_ORDER_DESK_PROJECTS_DIR` is not set.
- `dotnet/ContainerBuild.props`: mounted into `/dotnet-config` and loaded through `DirectoryBuildPropsPath` to redirect .NET build artifacts to `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: installed as `/usr/local/bin/dotnet` to filter one known workload verification noise line while preserving real output and exit codes.
- `spec-kit/patch-specify-cli.py`: patches Spec Kit copy behavior so initialization works better on Windows/WSL bind mounts.
- `README.md`: user-facing setup and operation guide.

There is currently no `src/`, `tests/`, or asset directory.

## Testing Guidelines

Geltung / Applies to: `.github/copilot-instructions.md`, `.github/agents/copilot-instructions.md`

There is no test framework in this repository. Before committing, run:

```bash
podman-compose config
```

If `compose.home-baseline.yml` or the optional `HOME_BASELINE_DIR` workflow
changed, also run with a local checkout:

```bash
HOME_BASELINE_DIR=/path/to/home-baseline-source podman-compose -f compose.yml -f compose.home-baseline.yml config
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
pwsh --version
node --version
npm --version
swift --version
swiftc --version
command -v sourcekit-lsp
codex --version
claude --version
agy --version
copilot --version
syft version
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
and use a port from the published app range `5100-5198`. During practical checks,
verify that the app responds over HTTP and stop any background test process
before ending the session.

Do not require a real API key for validation unless the change explicitly affects live Opencode usage.

For .NET projects under `/rider-projects`, keep `bin`, `obj`, and AppHost output off the Windows bind mount. The mounted `ContainerBuild.props` sends build output to the `dotnet_build` volume at `/dotnet-build` and imports repository-specific `Directory.Build.props` files when present.

For Java projects, use `/java-projects` and prefer project-local Maven or Gradle wrappers when a repository provides them. The container includes JDK 25 LTS and Maven for baseline Java and Spring Boot development. Gradle and Spring Boot CLI are not installed globally unless this repository is intentionally extended.

For Go projects, use `/workspace` unless a project-specific mount is configured. Keep dependencies in `go.mod`, run `gofmt`/`go test ./...`, and add web frameworks such as `gin`, `fiber`, or `chi` per project instead of installing them globally.

For Rust projects, use `/workspace` unless a project-specific mount is configured. Keep dependencies in `Cargo.toml`, run `cargo fmt`, `cargo clippy -- -D warnings`, and `cargo test`. Add frameworks such as `tokio`, `axum`, `actix-web`, or `serde` per project instead of installing them globally.

For Python projects, use `/python-projects` unless a project-specific mount is configured. The default `python` and `python3` use pinned CPython under `/opt/cpython`; `/usr/bin/python3` remains Ubuntu-managed for system tools. Keep virtual environments project-local or under an explicitly chosen cache path, and do not rely on globally installed application dependencies.

For PowerShell projects, use `/powershell-projects` unless a project-specific mount is configured. Run scripts with `pwsh -NoLogo -NoProfile`, keep modules project-local or explicitly versioned, and validate repository-owned scripts with PSScriptAnalyzer when that module is available.

ASP.NET apps must bind to `0.0.0.0` inside the container to be reachable from Windows. Compose publishes `127.0.0.1:5100-5198:5100-5198` for apps; port 5199 is reserved for OpenCode.

The Compose environment disables general .NET workload update notifications with `DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=true` and disables the MSBuild workload resolver with `MSBuildEnableWorkloadResolver=false`. Install real workloads explicitly in the Dockerfile and re-enable the resolver if a project requires MAUI, WebAssembly, or another optional SDK workload.

The `dotnet` wrapper must only filter the exact workload verification message. Do not broaden the filter, because normal warnings and build errors must stay visible.

Spec Kit is installed from the exact release commit pinned in `Dockerfile`; the build verifies its package version. Keep the commit and version check synchronized when upgrading. See `docs/maintenance/toolchain-version-audit-2026-10-25.md` for the latest version audit.

For Spec Kit initialization under `/rider-projects`, prefer `specify init . --integration opencode --force`. If prompted for script type, choose `sh` in this Linux container. For each application repository, decide whether `.opencode/` or sensitive parts of it belong in that repository's `.gitignore`.

Spec Kit is patched after installation to avoid Python metadata-preserving copy operations on host bind mounts. Keep this patch narrow; it should only affect copying behavior, not Spec Kit command semantics.
