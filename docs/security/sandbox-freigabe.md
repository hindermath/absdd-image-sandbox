# Sandbox-Freigabe

Status: Entwurf, Freigabe ausstehend

Dieses Dokument bereitet die formelle Freigabe von `absdd-image-sandbox` vor. Verantwortliche Personen, Freigabestatus, Freigabedatum und rechtliche Bewertungen muessen durch die verantwortliche Stelle ergaenzt werden. Der PR-Ablauf fuer CISO/ISB oder KI-Beauftragte:n (KIB) ist in `docs/security/sandbox-freigabe-review.md` beschrieben.

## Deutsch

| Feld | Wert |
|---|---|
| Sandbox-Typ | Container (Podman) |
| Sandbox-Identifikator | `mcr.microsoft.com/dotnet/sdk:10.0@sha256:1f48db91b4f27fdb4409b7b4253ce1fd4f78f69d34efd9edb788c03a337f5ab8` |
| Verantwortliche Person | `_TODO_ (vom Owner einzutragen)` |
| Freigabestatus | `_Entwurf, Freigabe ausstehend_` |
| Freigabedatum | `_TODO_ (vom Owner einzutragen)` |
| Ablaufdatum / Re-Review | `_TODO_ (Empfehlung: 12 Monate nach Freigabe)` |
| Genehmigte Modelle | Siehe `docs/security/ai-tools-inventory.md` |
| Isolationsnachweis | Siehe `docs/security/sandbox-isolation.md` |
| Genehmigte Mount-Liste | Siehe `compose.yml` und optional `compose.home-baseline.yml`; Kurzliste unten |
| Genehmigte Tool-Versionen | Siehe `Dockerfile`; Kurzliste unten |
| Offener Freigabehinweis | Freigabe durch CISO/ISB oder KI-Beauftragte:n (KIB) ausstehend |
| Freigabe-Review | Siehe `docs/security/sandbox-freigabe-review.md` |

### Genehmigte Mount-Liste

| Quelle | Ziel | Zweck |
|---|---|---|
| `./workspace` | `/workspace` | Allgemeiner Arbeitsbereich |
| `${ADE_DEV_SANDBOX_DIR:-.}` | `/ade-dev-sandbox` | Checkout dieses Setup-Repositories fuer kontrollierte Wartungsaufgaben aus dem Container |
| `${RIDER_PROJECTS_DIR:-./workspace}` | `/rider-projects` | Rider- und .NET-Projekte |
| `${JAVA_PROJECTS_DIR:-./java-projects}` | `/java-projects` | Java-, Maven- und Spring-Boot-Projekte |
| `${GO_PROJECTS_DIR:-./go-projects}` | `/go-projects` | Go-Projekte |
| `${RUST_PROJECTS_DIR:-./rust-projects}` | `/rust-projects` | Rust-Projekte |
| `${PYTHON_PROJECTS_DIR:-./python-projects}` | `/python-projects` | Python-Projekte |
| `${SWIFT_PROJECTS_DIR:-./swift-projects}` | `/swift-projects` | Swift-Projekte |
| `${HOME_BASELINE_DIR}` | `/home/adedev/home-baseline-tmp` | Optionaler Checkout eines eigenen aus `home-baseline` erzeugten Template-Repositories; nur mit `compose.home-baseline.yml` |
| `./dotnet/ContainerBuild.props` | `/dotnet-config/ContainerBuild.props` | Read-only .NET-Build-Konfiguration |
| `dotnet_build` | `/dotnet-build` | Persistente .NET-Build-Artefakte ausserhalb von Host-Bind-Mounts |
| `opencode_data` | `/home/adedev/.local/share/opencode` | Persistente OpenCode-Daten |
| `codex_data` | `/home/adedev/.codex` | Persistente Codex-Daten |

### Genehmigte Tool-Versionen

| Tool | Version / Quelle |
|---|---|
| .NET SDK | Microsoft .NET SDK aus MCR-Basisimage `mcr.microsoft.com/dotnet/sdk:10.0` |
| Java | OpenJDK 21 aus Ubuntu-Paketquellen |
| Maven | Ubuntu-Paketquelle |
| Python | Ubuntu-Paketquelle (`python3`, `python3-venv`, `python-is-python3`) |
| Node.js / npm | NodeSource-Apt-Quelle, `NODE_MAJOR=22`, signiert ueber `/usr/share/keyrings/nodesource.gpg` |
| Go | `1.26.3` |
| gopls | `v0.21.1` |
| staticcheck | `v0.7.0` |
| govulncheck | `v1.3.0` |
| Delve | `v1.26.3` |
| Rust | `1.95.0` |
| Swift | `6.3.3-noble` aus `download.swift.org`, PGP-Signaturpruefung im Image-Build |
| OpenCode | `opencode-ai` `1.14.50` |
| Codex CLI | `@openai/codex` `0.130.0` |
| Spec Kit | `specify-cli` `v0.8.3` aus `github.com/github/spec-kit.git` |
| uv / uvx | `0.11.16` aus GitHub-Release-Artefakt, SHA256-Pruefung im Image-Build |

### Optionaler lokaler IDE-Zugang

VS Code kann vom Host per Dev Containers an den laufenden `ade`-Container
anhaengen. Diese Option startet keinen dauerhaften Browser-IDE- oder
VS-Code-Server-Dienst im Image und veroeffentlicht keinen zusaetzlichen
IDE-Port. VS Code installiert den benoetigten Remote-Server beim Verbinden
selbst in den Container; die Anleitung steht in `README.md`.

### Unterschriftsblock

| Rolle | Name | Datum | Unterschrift |
|---|---|---|---|
| Verantwortliche Person | `_TODO_` | `_TODO_` | `_TODO_` |
| CISO / ISB | `_TODO_` | `_TODO_` | `_TODO_` |
| KI-Beauftragte:r (KIB) | `_TODO_` | `_TODO_` | `_TODO_` |
| Betrieb / Plattform | `_TODO_` | `_TODO_` | `_TODO_` |

## English

| Field | Value |
|---|---|
| Sandbox type | Container (Podman) |
| Sandbox identifier | `mcr.microsoft.com/dotnet/sdk:10.0@sha256:1f48db91b4f27fdb4409b7b4253ce1fd4f78f69d34efd9edb788c03a337f5ab8` |
| Responsible person | `_TODO_ (to be entered by owner)` |
| Approval status | `_Draft, approval pending_` |
| Approval date | `_TODO_ (to be entered by owner)` |
| Expiration date / re-review | `_TODO_ (recommendation: 12 months after approval)` |
| Approved models | See `docs/security/ai-tools-inventory.md` |
| Isolation evidence | See `docs/security/sandbox-isolation.md` |
| Approved mount list | See `compose.yml` and optional `compose.home-baseline.yml`; short list above |
| Approved tool versions | See `Dockerfile`; short list above |
| Open approval note | Approval by CISO/ISB or AI officer (KIB) pending |
| Approval review | See `docs/security/sandbox-freigabe-review.md` |

This file is a draft for review and signature by the responsible people. The PR review flow is described in `docs/security/sandbox-freigabe-review.md`.

Optional local IDE access: VS Code can attach from the host to the running
`ade` container through Dev Containers. This option does not start a
long-running browser IDE or VS Code Server service in the image and does not
publish an additional IDE port. VS Code installs the required remote server
into the container when it connects; the workflow is documented in `README.md`.
