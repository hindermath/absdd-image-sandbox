# Sandbox-Freigabe

Status: Entwurf, Freigabe ausstehend

Dieses Dokument bereitet die formelle Freigabe der `ade-dev-sandbox` vor.  Verantwortliche Personen, Freigabestatus, Freigabedatum und rechtliche Bewertungen muessen durch die verantwortliche Stelle ergaenzt werden.

## Deutsch

| Feld | Wert |
|---|---|
| Sandbox-Typ | Container (Docker / Podman) |
| Sandbox-Identifikator | `docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox@sha256:a21e15872aed8b0e4b9e18e0ff1e678318968efb4b8367ddf9fa4a63fc1d294c` |
| Verantwortliche Person | `_TODO_ (vom Owner einzutragen)` |
| Freigabestatus | `_Entwurf, Freigabe ausstehend_` |
| Freigabedatum | `_TODO_ (vom Owner einzutragen)` |
| Ablaufdatum / Re-Review | `_TODO_ (Empfehlung: 12 Monate nach Freigabe)` |
| Genehmigte Modelle | Siehe `docs/security/ai-tools-inventory.md` |
| Genehmigte Mount-Liste | Siehe `compose.yml`; Kurzliste unten |
| Genehmigte Tool-Versionen | Siehe `Dockerfile`; Kurzliste unten |
| Offener Freigabehinweis | Freigabe durch CISO/ISB ausstehend |

### Genehmigte Mount-Liste

| Quelle | Ziel | Zweck |
|---|---|---|
| `./workspace` | `/workspace` | Allgemeiner Arbeitsbereich |
| `${RIDER_PROJECTS_DIR:-./workspace}` | `/rider-projects` | Rider- und .NET-Projekte |
| `${JAVA_PROJECTS_DIR:-./java-projects}` | `/java-projects` | Java-, Maven- und Spring-Boot-Projekte |
| `${GO_PROJECTS_DIR:-./go-projects}` | `/go-projects` | Go-Projekte |
| `${RUST_PROJECTS_DIR:-./rust-projects}` | `/rust-projects` | Rust-Projekte |
| `${PYTHON_PROJECTS_DIR:-./python-projects}` | `/python-projects` | Python-Projekte |
| `./dotnet/ContainerBuild.props` | `/dotnet-config/ContainerBuild.props` | Read-only .NET-Build-Konfiguration |
| `dotnet_build` | `/dotnet-build` | Persistente .NET-Build-Artefakte ausserhalb von Host-Bind-Mounts |
| `opencode_data` | `/home/adedev/.local/share/opencode` | Persistente OpenCode-Daten |
| `codex_data` | `/home/adedev/.codex` | Persistente Codex-Daten |

### Genehmigte Tool-Versionen

| Tool | Version / Quelle |
|---|---|
| .NET SDK | `dotnet-sdk-10.0` |
| Java | OpenJDK 21 aus Debian-Paketquellen |
| Maven | Debian-Paketquelle |
| Python | Debian-Paketquelle (`python3`, `python3-venv`, `python-is-python3`) |
| Go | `1.26.3` |
| gopls | `v0.21.1` |
| staticcheck | `v0.7.0` |
| govulncheck | `v1.3.0` |
| Delve | `v1.26.3` |
| Rust | `1.95.0` |
| OpenCode | `opencode-ai` `1.14.50` |
| Codex CLI | `@openai/codex` `0.130.0` |
| Spec Kit | `specify-cli` `v0.8.3` aus `github.com/github/spec-kit.git` |
| uv / uvx | Installiert aus `https://astral.sh/uv/install.sh` beim Image-Build |

### Unterschriftsblock

| Rolle | Name | Datum | Unterschrift |
|---|---|---|---|
| Verantwortliche Person | `_TODO_` | `_TODO_` | `_TODO_` |
| CISO / ISB | `_TODO_` | `_TODO_` | `_TODO_` |
| Betrieb / Plattform | `_TODO_` | `_TODO_` | `_TODO_` |

## English

| Field | Value |
|---|---|
| Sandbox type | Container (Docker / Podman) |
| Sandbox identifier | `docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox@sha256:a21e15872aed8b0e4b9e18e0ff1e678318968efb4b8367ddf9fa4a63fc1d294c` |
| Responsible person | `_TODO_ (to be entered by owner)` |
| Approval status | `_Draft, approval pending_` |
| Approval date | `_TODO_ (to be entered by owner)` |
| Expiration date / re-review | `_TODO_ (recommendation: 12 months after approval)` |
| Approved models | See `docs/security/ai-tools-inventory.md` |
| Approved mount list | See `compose.yml`; short list above |
| Approved tool versions | See `Dockerfile`; short list above |
| Open approval note | Approval by CISO/ISB pending |

This file is a draft for review and signature by the responsible people.
