# Sandbox-Freigabe

Status: Owner-Freigabe für Secure-Trader-Wartungsupdates erteilt; gesonderte Rollenfreigabe nach P1-4 nicht nachgewiesen.

Dieses Dokument hält die ausdrückliche Owner-Entscheidung fest. Sie ist keine vom Agenten erteilte Freigabe und weist keine zusätzliche CISO-/ISB-/KIB-Rolle nach. Der gesonderte PR-Ablauf für diese Rollen ist in `docs/security/sandbox-freigabe-review.md` beschrieben.

## Deutsch

| Feld | Wert |
|---|---|
| Sandbox-Typ | Container (Podman) |
| Sandbox-Identifikator | `mcr.microsoft.com/dotnet/sdk:10.0@sha256:e1ffd2a92ae84c1291bc1b6887501f8af98e6331e7af6d4c8d37168c5e87a64c` |
| Verantwortliche Person | Thorsten Hindermann, Repository-/Workspace-Owner |
| Freigabestatus | Owner-Freigabe für die unten abgegrenzten Wartungsupdates erteilt |
| Freigabedatum | 2026-09-19; dokumentiert um 23:54 CEST |
| Ablaufdatum / Re-Review | 31.12.2026, ausdrücklich vom Owner ergänzt |
| Genehmigte Modelle | Siehe `docs/security/ai-tools-inventory.md` |
| Isolationsnachweis | Siehe `docs/security/sandbox-isolation.md` |
| Genehmigte Mount-Liste | Siehe `compose.yml` und optional `compose.home-baseline.yml`; Kurzliste unten |
| Genehmigte Tool-Versionen | Siehe `Dockerfile`; Kurzliste unten |
| Offener Freigabehinweis | Freigabe durch CISO/ISB oder KI-Beauftragte:n (KIB) ausstehend |
| Freigabe-Review | Siehe `docs/security/sandbox-freigabe-review.md` |

### Owner-Entscheidung vom 2026-09-19

Quelle: ausdrückliche Nachricht von Thorsten Hindermann in der laufenden
Wartungssitzung, nach Hinweis auf die ausstehende Sandbox-Freigabe:

> Ich erteile hiermit durch meine Autorität als Owner die Freigabe. Bitte dokumentieren!

Der Gesprächskontext begrenzt die Entscheidung auf Korrektur und Aktualisierung
der 21 Secure-Trader-Flottenziele (drei Level-1-Workspaces und 18
Level-2-Repositories) innerhalb der wiederhergestellten Sandbox. Bestehende
Mounts, Sicherheitsgrenzen und der Schutz lokaler Änderungen bleiben erhalten.
Keine pauschale Produktions-, Modell-, Provider-, Secret- oder Datenfreigabe;
keine zusätzliche Commit-/Push-/Merge-Autorität aus dieser Entscheidung.
Zulässige Datenklassifikation wurde nicht angegeben. Der Owner ergänzte
ausdrücklich das Ablaufdatum 31.12.2026 und beauftragte anschließend den
Rollout. Diese Freigabe gilt für den oben abgegrenzten Wartungsumfang.

Zum Dokumentationszeitpunkt geprüft: Container `bdbf765955a4`, laufend,
lokales Image `sha256:4c279f0c0f3a5abfc436deda18e87c9ca4ea966f502a7cae003fa03bd70ba84f`.
Der oben aufgeführte Basisimage-Digest bleibt eine getrennte deklarierte
Referenz und wird nicht mit der lokalen Image-ID gleichgesetzt.
Technische Evidence: Sitzungsnachweis
`agent-session-log/2026-09-19-2350-sandbox-container-recovery.md`.

P1-4 wird durch diese Dokumentation nicht als vollständig abgeschlossen
markiert: Der bestehende Rollen-/Review-Vertrag und die fehlenden Angaben
bleiben sichtbar. Die Owner-Entscheidung wird unverfälscht dokumentiert,
nicht stillschweigend in eine CISO-/ISB-/KIB-Freigabe umgedeutet.

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
| `${POWERSHELL_PROJECTS_DIR:-./powershell-projects}` | `/powershell-projects` | PowerShell-Skriptprojekte |
| `${SWIFT_PROJECTS_DIR:-./swift-projects}` | `/swift-projects` | Swift-Projekte |
| `${SECURE_CASE_TRACKER_PROJECTS_DIR:-./secure-case-tracker-projects}` | `/secure-case-tracker-projects` | Secure-CaseTracker-Lern- und Projektarbeiten |
| `${SECURE_SERVICE_HARVESTER_PROJECTS_DIR:-./secure-service-harvester-projects}` | `/secure-service-harvester-projects` | Secure-Service-Harvester-Lern- und Projektarbeiten |
| `${SECURE_ORDER_DESK_PROJECTS_DIR:-./secure-order-desk-projects}` | `/secure-order-desk-projects` | Secure-OrderDesk-Lern- und Projektarbeiten |
| `${HOME_BASELINE_DIR}` | `/opt/home-baseline` | Optionaler beschreibbarer persoenlicher `home-baseline-source`-Checkout; `~/home-baseline-source` ist kanonisch, `~/home-baseline-tmp` bleibt als veralteter Kompatibilitaetslink |
| `./dotnet/ContainerBuild.props` | `/dotnet-config/ContainerBuild.props` | Read-only .NET-Build-Konfiguration |
| `dotnet_build` | `/dotnet-build` | Persistente .NET-Build-Artefakte ausserhalb von Host-Bind-Mounts |
| `opencode_data` | `/home/adedev/.local/share/opencode` | Persistente OpenCode-Daten |
| `codex_data` | `/home/adedev/.codex` | Persistente Codex-Daten |
| `claude_data` | `/home/adedev/.claude` | Persistenter Claude-Code-Zustand |
| `gemini_data` | `/home/adedev/.gemini-home` | Persistenter Gemini-CLI-Zustand |
| `copilot_data` | `/home/adedev/.copilot` | Persistenter GitHub-Copilot-CLI-Zustand |

### Genehmigte Tool-Versionen

| Tool | Version / Quelle |
|---|---|
| .NET SDK | Microsoft .NET SDK aus MCR-Basisimage `mcr.microsoft.com/dotnet/sdk:10.0` plus hashgeprueftes Kompatibilitaets-SDK `10.0.301` |
| actionlint | `1.7.12`, architekturspezifisches GitHub-Release mit SHA-256-Pruefung |
| GitHub CLI | Nicht im Agentencontainer; `gh` und Provider-Credentials bleiben auf der getrennten Control Plane |
| Java | OpenJDK 21 aus Ubuntu-Paketquellen |
| Maven | Ubuntu-Paketquelle |
| Python | Ubuntu-Paketquelle (`python3`, `python3-venv`, `python-is-python3`) |

Codex bindet die Schreibberechtigung an den je Aufruf gewaehlten internen
Transaktionspfad `/home/adedev/codex-workspace`. Zusaetzliche Mounts benoetigen
ein ausdrueckliches `--add-dir`; eine pauschale Schreibfreigabe aller
Projektmounts ist nicht Teil des Sandboxprofils. Die Linux-Aufloesung von
Secret-Globmustern ist auf vier Verzeichnisebenen begrenzt, damit Bubblewrap
keine unbeschraenkte Argumentliste erhaelt. Im rootless Podman-Container bindet
ein enger Adapter das bereits von Podman isolierte Minimal-`/dev` und
Container-`/proc` ein. Nicht unterstuetzte synthetische Remounts werden nur fuer
die vorab root-eigenen, nicht beschreibbaren Metadaten-Platzhalter `.git`,
`.agents` und `.codex` durch Read-only-Binds ersetzt. Das im Profil
ausgeschlossene `/tmp` bleibt read-only; unnoetige synthetische Metadaten-Mounts
darunter werden verworfen. Direkte Host-Projektmounts sind fuer agentenlose
Installation und Tests vorgesehen; Agentenaenderungen werden ueber den internen
Transaktionspfad kontrolliert ein- und ausgefuehrt. Der Adapter benoetigt weder
Capabilities noch einen privilegierten Containerstart.

Interaktive Codex-Sitzungen verwenden weiterhin `untrusted` oder `on-request`.
Der nicht-interaktive `codex exec`-Modus setzt technisch `never`; dieser Modus
ist nur zusammen mit den erzwungenen `read-only`- oder `workspace-write`-
Profilen zugelassen und kann die Dateisystem- oder Netzwerkgrenzen nicht
erweitern.
| PowerShell | `7.6.4`, vom digest-gepinnten Microsoft-.NET-SDK-Basisimage geliefert und im Build geprueft |
| Node.js / npm | NodeSource-Apt-Quelle, `NODE_MAJOR=22`, signiert ueber `/usr/share/keyrings/nodesource.gpg` |
| Go | `1.26.3` |
| gopls | `v0.21.1` |
| staticcheck | `v0.7.0` |
| govulncheck | `v1.3.0` |
| Delve | `v1.26.3` |
| Rust | `1.95.0` |
| Swift | `6.3.3-noble` aus `download.swift.org`, PGP-Signaturpruefung im Image-Build |
| OpenCode | `opencode-ai` `1.14.50` |
| Codex CLI | `@openai/codex` `0.144.1` |
| Claude Code | `@anthropic-ai/claude-code` `2.1.206` |
| Antigravity CLI | `google-antigravity/antigravity-cli` `1.1.1` |
| GitHub Copilot CLI | `@github/copilot` `1.0.70` |
| Spec Kit | `specify-cli` `v0.8.3` aus `github.com/github/spec-kit.git` |
| Syft | `anchore/syft` `1.46.0`, SHA256-Pruefung im Image-Build |
| uv / uvx | `0.11.16` aus GitHub-Release-Artefakt, SHA256-Pruefung im Image-Build |
| home-baseline Level-0-Quelle | Commit-Pin (kein Release-Tag) `5b3096c244a6b08266916d2cb4ba5981ebafbd67`, MIT; Schema 2 in `home-baseline.lock.json` |

Am 20.09.2026 genehmigte der Owner ausdruecklich das Sandbox-Image-Update
als Erweiterung des Wartungsauftrags. Es aktualisiert die eingebettete
Home-Baseline-Referenz, nicht Modelle, Provider, Mounts oder Rollenfreigaben.
Alle bestehenden Volumes bleiben erhalten; die Wartungsfreigabe endet weiterhin
am 31.12.2026. Build- und Wiederanlaufnachweise werden getrennt dokumentiert.

*On 2026-09-20 the owner explicitly approved the sandbox image update as an
extension of the maintenance task. It updates the embedded Home Baseline
reference, not models, providers, mounts or role approvals. Existing volumes
are retained and the maintenance approval still expires on 2026-12-31.
Build and restart evidence is recorded separately.*

Die Home Runtime wird nie automatisch angewendet. Der ausdrueckliche Wrapper
`sync-home-baseline-runtime` kennt nur `--dry-run`, `--check-only` und
`--apply`. Er synchronisiert ausschliesslich manifestdefinierte `homeRuntime`-
Inhalte und laesst Zugangsdaten, Providerzustand und lokale Einstellungen
unangetastet.

*The Home Runtime is never applied automatically. The explicit
`sync-home-baseline-runtime` wrapper accepts only `--dry-run`, `--check-only`,
and `--apply`. It synchronizes manifest-defined `homeRuntime` content only and
leaves credentials, provider state, and local settings untouched.*

### Optionaler lokaler IDE-Zugang

VS Code kann vom Host per Dev Containers an den laufenden `ade`-Container
anhaengen. Diese Option startet keinen dauerhaften Browser-IDE- oder
VS-Code-Server-Dienst im Image und veroeffentlicht keinen zusaetzlichen
IDE-Port. VS Code installiert den benoetigten Remote-Server beim Verbinden
selbst in den Container; die Anleitung steht in `README.md`.

### Unterschriftsblock

| Rolle | Name | Datum | Unterschrift |
|---|---|---|---|
| Verantwortliche Person / Owner | Thorsten Hindermann | 2026-09-19 | Explizite Chat-Entscheidung oben; keine Unterschrift simuliert |
| CISO / ISB | `_TODO_` | `_TODO_` | `_TODO_` |
| KI-Beauftragte:r (KIB) | `_TODO_` | `_TODO_` | `_TODO_` |
| Betrieb / Plattform | `_TODO_` | `_TODO_` | `_TODO_` |

## English

| Field | Value |
|---|---|
| Sandbox type | Container (Podman) |
| Sandbox identifier | `mcr.microsoft.com/dotnet/sdk:10.0@sha256:e1ffd2a92ae84c1291bc1b6887501f8af98e6331e7af6d4c8d37168c5e87a64c` |
| Responsible person | Thorsten Hindermann, repository/workspace owner |
| Approval status | Owner approval granted for the bounded maintenance updates below |
| Approval date | 2026-09-19; recorded at 23:54 CEST |
| Expiration date / re-review | 2026-12-31, explicitly supplied by the owner |
| Approved models | See `docs/security/ai-tools-inventory.md` |
| Isolation evidence | See `docs/security/sandbox-isolation.md` |
| Approved mount list | See `compose.yml` and optional `compose.home-baseline.yml`; short list above |
| Approved tool versions | See `Dockerfile`; short list above |
| Open approval note | Approval by CISO/ISB or AI officer (KIB) pending |
| Approval review | See `docs/security/sandbox-freigabe-review.md` |

### Owner decision of 2026-09-19

Thorsten Hindermann explicitly granted approval in his capacity as owner in
the maintenance conversation and requested documentation. The conversation
limits its scope to maintenance corrections and updates of 21 Secure Trader
fleet targets (three Level-1 workspaces and 18 Level-2 repositories) inside
the restored sandbox. Existing mounts, security boundaries and local changes
remain protected. This is not a blanket production, model, provider, secret or
data approval and grants no additional commit, push or merge authority.
Data classification was not supplied. The owner subsequently specified
2026-12-31 as the expiration date and explicitly requested starting the rollout
within the bounded maintenance scope above.

Verified when recorded: running container `bdbf765955a4`, local image
`sha256:4c279f0c0f3a5abfc436deda18e87c9ca4ea966f502a7cae003fa03bd70ba84f`.
This image ID is distinct from the declared base-image digest above.
Technical evidence: `agent-session-log/2026-09-19-2350-sandbox-container-recovery.md`.
The decision is human-provided, not granted by the agent. No CISO/ISB/KIB role
or signature is inferred. P1-4 is not marked fully complete; its separate
role/review requirements and missing fields remain open. The review workflow
is documented in `docs/security/sandbox-freigabe-review.md`.

Optional local IDE access: VS Code can attach from the host to the running
`ade` container through Dev Containers. This option does not start a
long-running browser IDE or VS Code Server service in the image and does not
publish an additional IDE port. VS Code installs the required remote server
into the container when it connects; the workflow is documented in `README.md`.
