# Repository Guidelines

## Project Structure & Module Organization

This repository contains a small Docker-based Opencode, .NET, and Spec Kit environment, not an application codebase.

- `Dockerfile`: builds from the official Microsoft .NET SDK `latest` image and installs `opencode-ai@latest`, `uv`, and `specify-cli`.
- `compose.yml`: defines the `opencode` service, pulls newer build base images, and mounts local state.
- `opencode.jsonc`: configures the `chat-ai` provider, models, and agents. Keep comments useful for first-year IT specialist apprentices.
- `opencode.env.example`: documents the required `GWDG_API_KEY` variable.
- `workspace/`: mounted into the container as `/workspace`; place working project files there.
- `RIDER_PROJECTS_DIR`: host directory mounted into the container as `/rider-projects` for Rider projects.
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

Builds the image if needed and starts the `opencode` container.

```bash
docker compose exec opencode bash
```

Opens a shell inside the running container.

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

## Testing Guidelines

There is no test framework in this repository. Before committing, run:

```bash
docker compose config --no-interpolate
```

For Dockerfile changes, also run:

```bash
docker compose build --pull
```

The `--pull` flag is important because the Dockerfile uses `mcr.microsoft.com/dotnet/sdk:latest`.

Do not require a real API key for validation unless the change explicitly affects live Opencode usage.

For .NET projects under `/rider-projects`, keep `bin`, `obj`, and AppHost output off the Windows bind mount. The mounted `ContainerBuild.props` sends build output to the `dotnet_build` volume at `/dotnet-build` and imports repository-specific `Directory.Build.props` files when present.

ASP.NET apps must bind to `0.0.0.0` inside the container to be reachable from Windows. Compose publishes `127.0.0.1:5100-5199:5100-5199`; keep sample web app ports in that range unless the Compose file is updated.

The Compose environment disables general .NET workload update notifications with `DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=true` and disables the MSBuild workload resolver with `MSBuildEnableWorkloadResolver=false`. The Dockerfile also sets `dotnet workload config --update-mode manifests` as root to reduce workload verification noise with .NET 10 SDK images. Do not run this command after switching to the `opencode` user because it needs elevated privileges. Install real workloads explicitly in the Dockerfile and re-enable the resolver if a project requires MAUI, WebAssembly, or another optional SDK workload.

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

## Security & Configuration Tips

Never commit `opencode.env`; it contains `GWDG_API_KEY` and is ignored by `.gitignore`. Keep local secret files restricted:

```bash
chmod 600 opencode.env
```

If copying credentials from `~/.local/share/opencode/auth.json`, only write the key into `opencode.env` and do not print it in logs or documentation.
