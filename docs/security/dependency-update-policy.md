# Abhängigkeits-Update-Richtlinie / Dependency-Update-Policy

Stand: 2026-10-25

Aktueller Abgleich / Current audit:
[2026-10-25](../maintenance/toolchain-version-audit-2026-10-25.md).
Java und Node verwenden aktuelle LTS-Linien; .NET bleibt auf 10 LTS.
Python und Maven werden separat auf stabile Upstream-Versionen gepinnt.
Nur das System-Python und die weiteren APT-Pakete folgen Ubuntu 24.04.
Go- und Python-Downloads erhalten feste Architektur-Hashes; Maven erhaelt
eine feste SHA-512-Pruefsumme fuer das architekturunabhaengige Java-Archiv.

Der zusaetzliche Renovate-Dockerfile-Manager verfolgt auch den MCR-Basisdigest.
Die LTS-Grenzen bleiben bewusst bei .NET 10.0, Java 25 und Node 24; ein
kuenftiger LTS-Wechsel benoetigt die gemeinsame Anpassung der Paketregeln.
Java-/Node-Versionen werden fuer diese Major-ARGs auf ihre Hauptnummer
normalisiert, damit keine Paketnamen wie `openjdk-25.0.4-jdk-headless` oder
NodeSource-Pfade wie `node_24.22.1.x` entstehen.

*The Dockerfile manager also tracks the MCR base digest. Rules intentionally
retain .NET 10.0, Java 25 and Node 24; a future LTS switch must update these
package rules together. Java/Node release versions are normalized to their
major number so APT package names and NodeSource paths remain valid.*

*Java and Node use current LTS lines; .NET stays on 10 LTS. Python and Maven
use separately pinned stable upstream releases. System Python and remaining
APT packages follow Ubuntu 24.04. Go/Python downloads use architecture hashes;
Maven's architecture-independent Java archive has a committed SHA-512 hash.*

Dokumentationswerkzeuge / Documentation tools: Pandoc, Lychee, Typst und
Tinymist verwenden native AMD64-/ARM64-Releases mit fest hinterlegten
SHA-256-Pruefsummen. Versionsupdates muessen die jeweiligen Pruefsummen
gemeinsam aktualisieren und den Dokumentations-Smoke-Test bestehen.
Lychee-Tags tragen das Praefix `lychee-v`; Renovate entfernt dieses Praefix
vor dem Versionsvergleich.

Pandoc, Lychee, Typst, and Tinymist use native AMD64/ARM64 releases with
committed SHA-256 checksums. Version updates must update the matching
checksums and pass the documentation smoke test.

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
| `MAVEN_VERSION` | `maven` | `org.apache.maven:apache-maven` |
| `PYTHON_VERSION` | `python-version` | `python` |
| `PYTHON_BUILD_DATE` | `github-releases` | `astral-sh/python-build-standalone` |
| `POWERSHELL_VERSION` | `github-releases` | `PowerShell/PowerShell` |
| `GO_VERSION` | `golang-version` | `go` |
| `GOPLS_VERSION` | `go` | `golang.org/x/tools/gopls` |
| `STATICCHECK_VERSION` | `go` | `honnef.co/go/tools` |
| `GOVULNCHECK_VERSION` | `go` | `golang.org/x/vuln` |
| `DELVE_VERSION` | `go` | `github.com/go-delve/delve` |
| `RUST_TOOLCHAIN` | `rust-version` | `rust` |
| `RUSTUP_VERSION` | `github-releases` | `rust-lang/rustup` |
| `SWIFT_DOCKER_TAG` | `docker` | `swift` |
| `NODE_MAJOR` | `node-version` | `node` |
| `NPM_VERSION` | `npm` | `npm` |
| `UV_VERSION` | `github-releases` | `astral-sh/uv` |
| `OPENCODE_VERSION` | `npm` | `@opencode/cli` |
| `CODEX_VERSION` | `npm` | `@openai/codex` |
| `CLAUDE_CODE_VERSION` | `npm` | `@anthropic-ai/claude-code` |
| `GEMINI_CLI_VERSION` | `npm` | `@google/gemini-cli` |
| `ANTIGRAVITY_CLI_VERSION` | `github-releases` | `google-antigravity/antigravity-cli` |
| `COPILOT_CLI_VERSION` | `npm` | `@github/copilot` |
| `SYFT_VERSION` | `github-releases` | `anchore/syft` |
| `PANDOC_VERSION` | `github-releases` | `jgm/pandoc` |
| `LYCHEE_VERSION` | `github-releases` | `lycheeverse/lychee` |
| `TYPST_VERSION` | `github-releases` | `typst/typst` |
| `TINYMIST_VERSION` | `github-releases` | `Myriad-Dreamin/tinymist` |
| `ACTIONLINT_VERSION` | `github-releases` | `rhysd/actionlint` |
| `DOTNET_COMPAT_SDK_VERSION` | `dotnet-version` | `dotnet-sdk` |

`JAVA_VERSION` versioniert bewusst die Java-Major-Linie fuer das Ubuntu-APT-
Paket `openjdk-${JAVA_VERSION}-jdk-headless`. Die konkrete Ubuntu-Patchversion
wird nicht exakt gepinnt und muss bei Renovate-PRs im Build validiert werden.

`POWERSHELL_VERSION` pinnt die stabile PowerShell-Version. Wenn MCR noch eine
alte Patchversion enthaelt, aktualisiert der Build dessen vorhandenes globales
Tool aus dem offiziellen Microsoft-Paket mit festen AMD64-/ARM64-SHA-256-Hashes.
Es entsteht keine zweite Tool-Installation. Paket-Hashes, Versions-ARG und
Basisimage-Digest gemeinsam pruefen; der Build vergleicht das Ergebnis mit `pwsh`.

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

### Native npm-Installationsschritte / Native npm Install Hooks

DE: npm blockiert nicht ausdruecklich erlaubte Installationsskripte. Der Build
schliesst deshalb nur die benannten Hooks von `@opencode/cli`,
`@anthropic-ai/claude-code`, `@github/keytar` und `node-pty` explizit ab. Es gibt
keine globale Freigabe aller Skripte und keine persistierte npm-Freigabe.
`libsecret-1-0` liefert die Laufzeitbibliothek fuer das vorhandene Keytar-Addon;
das konfiguriert weder Schluesselbund, Konto noch Zugangsdaten. Versions- und
Modul-Ladechecks muessen danach erfolgreich sein.

EN: npm blocks unapproved install scripts. The build explicitly finalizes only
the named hooks for OpenCode, Claude Code, keytar and node-pty. No blanket or
persistent npm script approval is configured. libsecret supplies the existing
keytar addon's runtime library, without configuring a keyring, account or
credentials. Version and native module load checks must pass afterwards.

### Spec-Kit-Commitbindung

Spec Kit 1.2.3 ist im Dockerfile direkt auf seinen Release-Commit gepinnt.
Dieser Pin wird bewusst geprueft und nicht vom ARG-Manager automatisch
aktualisiert. Der Image-Build prueft die installierte Paketversion; der lokale
Hook `specify-container-patch` prueft den Bind-Mount-Patch fuer die alte und
neue Modulstruktur, Idempotenz und die Blockierung unbekannter Strukturen.
Ein Versionswechsel benoetigt Image-Build und CLI-/Installations-Smokes.

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
| `MAVEN_VERSION` | `maven` | `org.apache.maven:apache-maven` |
| `PYTHON_VERSION` | `python-version` | `python` |
| `PYTHON_BUILD_DATE` | `github-releases` | `astral-sh/python-build-standalone` |
| `POWERSHELL_VERSION` | `github-releases` | `PowerShell/PowerShell` |
| `GO_VERSION` | `golang-version` | `go` |
| `GOPLS_VERSION` | `go` | `golang.org/x/tools/gopls` |
| `STATICCHECK_VERSION` | `go` | `honnef.co/go/tools` |
| `GOVULNCHECK_VERSION` | `go` | `golang.org/x/vuln` |
| `DELVE_VERSION` | `go` | `github.com/go-delve/delve` |
| `RUST_TOOLCHAIN` | `rust-version` | `rust` |
| `RUSTUP_VERSION` | `github-releases` | `rust-lang/rustup` |
| `SWIFT_DOCKER_TAG` | `docker` | `swift` |
| `NODE_MAJOR` | `node-version` | `node` |
| `NPM_VERSION` | `npm` | `npm` |
| `UV_VERSION` | `github-releases` | `astral-sh/uv` |
| `OPENCODE_VERSION` | `npm` | `@opencode/cli` |
| `CODEX_VERSION` | `npm` | `@openai/codex` |
| `CLAUDE_CODE_VERSION` | `npm` | `@anthropic-ai/claude-code` |
| `GEMINI_CLI_VERSION` | `npm` | `@google/gemini-cli` |
| `ANTIGRAVITY_CLI_VERSION` | `github-releases` | `google-antigravity/antigravity-cli` |
| `COPILOT_CLI_VERSION` | `npm` | `@github/copilot` |
| `SYFT_VERSION` | `github-releases` | `anchore/syft` |
| `PANDOC_VERSION` | `github-releases` | `jgm/pandoc` |
| `LYCHEE_VERSION` | `github-releases` | `lycheeverse/lychee` |
| `TYPST_VERSION` | `github-releases` | `typst/typst` |
| `TINYMIST_VERSION` | `github-releases` | `Myriad-Dreamin/tinymist` |
| `ACTIONLINT_VERSION` | `github-releases` | `rhysd/actionlint` |
| `DOTNET_COMPAT_SDK_VERSION` | `dotnet-version` | `dotnet-sdk` |

`JAVA_VERSION` deliberately versions the Java major line for the Ubuntu APT
package `openjdk-${JAVA_VERSION}-jdk-headless`. The concrete Ubuntu patch
package version is not pinned exactly and must be validated in Renovate PR
builds.

`POWERSHELL_VERSION` pins stable PowerShell. If MCR still contains an older
patch, the build updates its existing global tool using the official Microsoft
package and committed AMD64/ARM64 SHA-256 hashes, not a second installation.
Review package hashes, version ARG and base-image digest together. The build
checks the resulting `pwsh` version.

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

### Spec Kit Commit Binding

The Dockerfile pins Spec Kit 1.2.3 directly to its release commit. Review this
pin deliberately; the ARG manager does not update it automatically. The image
build checks installed package metadata. The `specify-container-patch` local
hook tests old and new module layouts, idempotency and unknown-layout blocking.
A version change requires an image build plus CLI and installation smoke tests.

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
