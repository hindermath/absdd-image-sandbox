# Dependency-Update-Policy

Stand: 2026-05-25

Dieses Dokument beschreibt die Repository-seitige Renovate-Konfiguration fuer
P3-3 aus `COMPLIANCE-PLAN_RL-SE-001.md`.

## Deutsch

### Ziel

`renovate.json` bereitet automatisierte Dependency-Merge-Requests fuer die im
`Dockerfile` gepinnten Build-Argumente vor. Renovate darf keine Aenderungen
direkt auf `main` schreiben und kein Auto-Merge ausfuehren. Jede Aenderung
bleibt ein normaler Merge Request mit Review, Build und Toolchecks.

### Dockerfile-ARG-Konvention

Alle `ARG`-Zeilen im `Dockerfile` muessen von Renovate erfasst werden. Dazu
steht direkt oberhalb des `ARG` eine Metadatenzeile:

```dockerfile
# renovate: datasource=<renovate-datasource> depName=<dependency-name> versioning=<versioning> argName=<ARG_NAME>
ARG <ARG_NAME>=<version>
```

Fuer Werte, die nicht nur eine reine Version enthalten, wird eine eigene
Regex-Regel verwendet. Das gilt aktuell fuer `DOTNET_SDK_PACKAGE`, weil der
Wert ein Debian-Paketname wie `dotnet-sdk-10.0` ist.

Wenn kuenftig ein weiteres `ARG` ergaenzt wird, muss es nach dieser Konvention
eine Renovate-Metadatenzeile bekommen. Wenn der Wert nicht als einfache Version
aktualisierbar ist, muss `renovate.json` um eine passende Sonderregel
erweitert werden. Der lokale Pre-commit-Hook
`dockerfile-arg-renovate-metadata` prueft, dass jedes `ARG` eine direkt
vorangestellte Metadatenzeile mit passendem `argName` hat.

### Aktuell erfasste ARGs

| ARG | Renovate datasource | Dependency |
|---|---|---|
| `DOTNET_SDK_PACKAGE` | `dotnet-version` | `dotnet-sdk` |
| `GO_VERSION` | `golang-version` | `go` |
| `GOPLS_VERSION` | `go` | `golang.org/x/tools/gopls` |
| `STATICCHECK_VERSION` | `go` | `honnef.co/go/tools` |
| `GOVULNCHECK_VERSION` | `go` | `golang.org/x/vuln` |
| `DELVE_VERSION` | `go` | `github.com/go-delve/delve` |
| `RUST_TOOLCHAIN` | `rust-version` | `rust` |
| `RUSTUP_VERSION` | `github-releases` | `rust-lang/rustup` |
| `NODE_MAJOR` | `node-version` | `node` |
| `UV_VERSION` | `github-releases` | `astral-sh/uv` |
| `OPENCODE_VERSION` | `npm` | `opencode-ai` |
| `CODEX_VERSION` | `npm` | `@openai/codex` |

### GitLab-CE-Betrieb

Dieses Repository enthaelt nur die Renovate-Konfiguration. Damit Renovate
tatsaechlich Merge Requests erstellt, muss ein Renovate-Bot, ein GitLab Runner
oder ein externer Renovate-Service fuer dieses GitLab-CE-Projekt aktiviert
werden. Bis dahin gilt P3-3 repo-seitig als vorbereitet; die serverseitige
Ausfuehrung ist ein Betriebs-/Admin-Schritt.

### Validierung vor Merge

Jeder Renovate-MR muss mindestens diese Pruefungen bestehen:

```bash
docker compose config --no-interpolate
docker compose build --pull
uvx pre-commit run --all-files
```

Bei Toolchain-Aenderungen sind zusaetzlich die Toolchecks aus `AGENTS.md`
auszufuehren.

## English

### Goal

`renovate.json` prepares automated dependency merge requests for pinned
Dockerfile build arguments. Renovate must not write directly to `main` and must
not automerge. Every change remains a normal merge request with review, build,
and tool checks.

### Dockerfile ARG Convention

All `ARG` lines in the `Dockerfile` must be visible to Renovate. A metadata
line must be placed directly above the `ARG`:

```dockerfile
# renovate: datasource=<renovate-datasource> depName=<dependency-name> versioning=<versioning> argName=<ARG_NAME>
ARG <ARG_NAME>=<version>
```

Values that are not simple versions need a dedicated regex rule. This currently
applies to `DOTNET_SDK_PACKAGE`, because the value is a Debian package name
such as `dotnet-sdk-10.0`.

When a new `ARG` is added later, it must follow this convention. If the value
cannot be updated as a simple version, `renovate.json` must receive a dedicated
rule for that argument. The local pre-commit hook
`dockerfile-arg-renovate-metadata` checks that every `ARG` has an immediately
preceding metadata line with a matching `argName`.

### Currently Covered ARGs

| ARG | Renovate datasource | Dependency |
|---|---|---|
| `DOTNET_SDK_PACKAGE` | `dotnet-version` | `dotnet-sdk` |
| `GO_VERSION` | `golang-version` | `go` |
| `GOPLS_VERSION` | `go` | `golang.org/x/tools/gopls` |
| `STATICCHECK_VERSION` | `go` | `honnef.co/go/tools` |
| `GOVULNCHECK_VERSION` | `go` | `golang.org/x/vuln` |
| `DELVE_VERSION` | `go` | `github.com/go-delve/delve` |
| `RUST_TOOLCHAIN` | `rust-version` | `rust` |
| `RUSTUP_VERSION` | `github-releases` | `rust-lang/rustup` |
| `NODE_MAJOR` | `node-version` | `node` |
| `UV_VERSION` | `github-releases` | `astral-sh/uv` |
| `OPENCODE_VERSION` | `npm` | `opencode-ai` |
| `CODEX_VERSION` | `npm` | `@openai/codex` |

### GitLab CE Operation

This repository only contains the Renovate configuration. For Renovate to
actually create merge requests, a Renovate bot, GitLab Runner, or external
Renovate service must be enabled for this GitLab CE project. Until then, P3-3
is prepared on the repository side; server-side execution is an operations or
admin step.

### Validation Before Merge

Every Renovate MR must pass at least these checks:

```bash
docker compose config --no-interpolate
docker compose build --pull
uvx pre-commit run --all-files
```

For toolchain changes, also run the tool checks from `AGENTS.md`.
