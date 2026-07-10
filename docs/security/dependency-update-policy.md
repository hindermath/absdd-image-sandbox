# Abhängigkeits-Update-Richtlinie / Dependency-Update-Policy

Stand: 2026-07-10

## Deutsch

Dieses Dokument beschreibt die Repository-seitige Renovate-Konfiguration fuer
P3-3 aus `COMPLIANCE-PLAN_RL-SE-001.md`.

### Ziel

`renovate.json` bereitet automatisierte Dependency-Pull-Requests fuer die im
`Dockerfile` gepinnten Build-Argumente vor. Renovate darf keine Aenderungen
direkt auf `main` schreiben und kein Auto-Merge ausfuehren. Jede Aenderung
bleibt ein normaler Pull Request mit Review, Build und Toolchecks.

### Dockerfile-ARG-Konvention

Alle `ARG`-Zeilen im `Dockerfile` muessen von Renovate erfasst werden. Dazu
steht direkt oberhalb des `ARG` eine Metadatenzeile:

```dockerfile
# renovate: datasource=<renovate-datasource> depName=<dependency-name> versioning=<versioning> argName=<ARG_NAME>
ARG <ARG_NAME>=<version>
```

Wenn kuenftig ein weiteres `ARG` ergaenzt wird, muss es nach dieser Konvention
eine Renovate-Metadatenzeile bekommen. Wenn der Wert nicht als einfache Version
aktualisierbar ist, muss `renovate.json` um eine passende Sonderregel
erweitert werden. Der lokale Pre-commit-Hook
`dockerfile-arg-renovate-metadata` prueft, dass jedes `ARG` eine direkt
vorangestellte Metadatenzeile mit passendem `argName` hat.

### Aktuell erfasste ARGs

| ARG | Renovate datasource | Dependency |
|---|---|---|
| `JAVA_VERSION` | `java-version` | `java` |
| `GO_VERSION` | `golang-version` | `go` |
| `GOPLS_VERSION` | `go` | `golang.org/x/tools/gopls` |
| `STATICCHECK_VERSION` | `go` | `honnef.co/go/tools` |
| `GOVULNCHECK_VERSION` | `go` | `golang.org/x/vuln` |
| `DELVE_VERSION` | `go` | `github.com/go-delve/delve` |
| `RUST_TOOLCHAIN` | `rust-version` | `rust` |
| `RUSTUP_VERSION` | `github-releases` | `rust-lang/rustup` |
| `SWIFT_DOCKER_TAG` | `docker` | `swift` |
| `NODE_MAJOR` | `node-version` | `node` |
| `UV_VERSION` | `github-releases` | `astral-sh/uv` |
| `OPENCODE_VERSION` | `npm` | `opencode-ai` |
| `CODEX_VERSION` | `npm` | `@openai/codex` |
| `CLAUDE_CODE_VERSION` | `npm` | `@anthropic-ai/claude-code` |
| `GEMINI_CLI_VERSION` | `npm` | `@google/gemini-cli` |
| `COPILOT_CLI_VERSION` | `npm` | `@github/copilot` |
| `SYFT_VERSION` | `github-releases` | `anchore/syft` |

`JAVA_VERSION` versioniert bewusst die Java-Major-Linie fuer das Ubuntu-APT-
Paket `openjdk-${JAVA_VERSION}-jdk-headless`. Die konkrete Ubuntu-Patchversion
wird nicht exakt gepinnt und muss bei Renovate-PRs im Build validiert werden.

### Eingebettete Home-Baseline-Referenz

`home-baseline.lock.json` behandelt die Level-0-Referenz als eingebettete
Inhaltsabhaengigkeit. Die Lock-Datei enthaelt ausschliesslich die oeffentliche
HTTPS-Quelle, einen stabilen Release-Tag, den exakten 40-stelligen Commit und
die MIT-Lizenz. Ein eigener Renovate-Regex-Manager erfasst Tag und Commit-Digest
gemeinsam; Auto-Merge bleibt deaktiviert.

Ein Update ist nur zulaessig, wenn der Release veroeffentlicht ist, der Tag auf
den eingetragenen Commit aufloest und der Build die erwartete Lizenz sowie die
zentrale Lernenden-Anleitung findet. `scripts/check-home-baseline-lock.py`
prueft die statische Lock-Struktur. Der Image-Build prueft den Tag gegen den
Commit vor dem Checkout. Die lokale Arbeitskopie eines Maintainers ist keine
zulaessige Build-Quelle.

### GitHub-Betriebskontext

Dieses Repository enthaelt nur die Renovate-Konfiguration. Damit Renovate
tatsaechlich Pull Requests erstellt, muss ein Renovate-Bot, eine passende
CI-Ausfuehrung oder ein externer Renovate-Service fuer GitHub aktiviert
werden. Bis zur Plattform-Einrichtung gilt P3-3 repo-seitig als vorbereitet;
die serverseitige Ausfuehrung ist ein Betriebs-/Admin-Schritt.

### Validierung vor Merge

Jeder Renovate-PR muss mindestens diese Pruefungen bestehen:

```bash
podman-compose config
podman compose build --pull
uvx pre-commit run --all-files
```

Bei Toolchain-Aenderungen sind zusaetzlich die Toolchecks aus `AGENTS.md`
auszufuehren.

## English

### Goal

`renovate.json` prepares automated dependency pull requests for pinned
Dockerfile build arguments. Renovate must not write directly to `main` and must
not automerge. Every change remains a normal pull request with review, build,
and tool checks.

### Dockerfile ARG Convention

All `ARG` lines in the `Dockerfile` must be visible to Renovate. A metadata
line must be placed directly above the `ARG`:

```dockerfile
# renovate: datasource=<renovate-datasource> depName=<dependency-name> versioning=<versioning> argName=<ARG_NAME>
ARG <ARG_NAME>=<version>
```

When a new `ARG` is added later, it must follow this convention. If the value
cannot be updated as a simple version, `renovate.json` must receive a dedicated
rule for that argument. The local pre-commit hook
`dockerfile-arg-renovate-metadata` checks that every `ARG` has an immediately
preceding metadata line with a matching `argName`.

### Currently Covered ARGs

| ARG | Renovate datasource | Dependency |
|---|---|---|
| `JAVA_VERSION` | `java-version` | `java` |
| `GO_VERSION` | `golang-version` | `go` |
| `GOPLS_VERSION` | `go` | `golang.org/x/tools/gopls` |
| `STATICCHECK_VERSION` | `go` | `honnef.co/go/tools` |
| `GOVULNCHECK_VERSION` | `go` | `golang.org/x/vuln` |
| `DELVE_VERSION` | `go` | `github.com/go-delve/delve` |
| `RUST_TOOLCHAIN` | `rust-version` | `rust` |
| `RUSTUP_VERSION` | `github-releases` | `rust-lang/rustup` |
| `SWIFT_DOCKER_TAG` | `docker` | `swift` |
| `NODE_MAJOR` | `node-version` | `node` |
| `UV_VERSION` | `github-releases` | `astral-sh/uv` |
| `OPENCODE_VERSION` | `npm` | `opencode-ai` |
| `CODEX_VERSION` | `npm` | `@openai/codex` |
| `CLAUDE_CODE_VERSION` | `npm` | `@anthropic-ai/claude-code` |
| `GEMINI_CLI_VERSION` | `npm` | `@google/gemini-cli` |
| `COPILOT_CLI_VERSION` | `npm` | `@github/copilot` |
| `SYFT_VERSION` | `github-releases` | `anchore/syft` |

`JAVA_VERSION` deliberately versions the Java major line for the Ubuntu APT
package `openjdk-${JAVA_VERSION}-jdk-headless`. The concrete Ubuntu patch
package version is not pinned exactly and must be validated in Renovate PR
builds.

### Embedded Home-Baseline Reference

`home-baseline.lock.json` treats the Level-0 reference as an embedded content
dependency. It records only the public HTTPS source, a stable release tag, the
exact 40-character commit, and the MIT license. A dedicated Renovate regex
manager captures the tag and commit digest together; automerge stays disabled.

An update is allowed only after the release is published, the tag resolves to
the recorded commit, and the build finds the expected license and canonical
learner guide. `scripts/check-home-baseline-lock.py` validates the static lock
shape. The image build verifies tag against commit before checkout. A
maintainer's local working tree is not an allowed build source.

### GitHub Operation Context

This repository only contains the Renovate configuration. For Renovate to
actually create pull requests, a Renovate bot, suitable CI execution, or an
external Renovate service must be enabled for GitHub. Until platform setup is
complete, P3-3 is prepared on the repository side; server-side execution is an
operations or admin step.

### Validation Before Merge

Every Renovate PR must pass at least these checks:

```bash
podman-compose config
podman compose build --pull
uvx pre-commit run --all-files
```

For toolchain changes, also run the tool checks from `AGENTS.md`.
