# Sandbox-Isolationsnachweis

Stand: 2026-05-22

Dieses Dokument konsolidiert die technischen Isolationsmechanismen der
`ade-dev-sandbox`. Es beschreibt vorhandene Konfigurationen und aendert keine
Sandbox-Einstellung.

## Deutsch

### Sandbox-Typ

Die `ade-dev-sandbox` ist eine Container-Sandbox gemaess der RL-SE-001-
Typologie fuer agentische KI in Sandbox-Umgebungen. Sie wird ueber Docker
Compose oder Podman Compose gebaut und gestartet.

### Isolationsmechanismen und Evidenz

| Mechanismus | Evidenzquelle | Bewertung |
|---|---|---|
| Nicht-privilegierte Laufzeit | `Dockerfile`: `useradd -m -s /bin/bash adedev`, `USER adedev`; `compose.yml`: Service `ade` startet das gebaute Image ohne `privileged: true` | Der Container laeuft nach dem Image-Build als Benutzer `adedev`, nicht als `root`. Root-Rechte werden nur waehrend des Image-Builds fuer Paketinstallation und Systempfade genutzt. |
| Dateisystem-Grenzen | `compose.yml`: Service `ade`, Abschnitt `volumes`; `docs/security/sandbox-freigabe.md`: "Genehmigte Mount-Liste" | Host-Dateien sind nur ueber explizit konfigurierte Bind-Mounts sichtbar: `/workspace`, `/rider-projects`, `/java-projects`, `/go-projects`, `/rust-projects`, `/python-projects` und `/audit`. Die .NET-Konfiguration `./dotnet/ContainerBuild.props` ist mit `:ro` read-only gemountet. |
| Trennung von Build- und Agentendaten | `compose.yml`: benannte Volumes `dotnet_build`, `opencode_data`, `codex_data`; Mounts nach `/dotnet-build`, `/home/adedev/.local/share/opencode`, `/home/adedev/.codex` | Persistente Tool- und Build-Daten werden in benannten Volumes gehalten und nicht als Repository-Dateien committet. |
| Codex-Schreibgrenzen | `codex/config.toml`: `sandbox_mode = "workspace-write"`, `[sandbox_workspace_write].writable_roots`; `codex/requirements.toml`: `allowed_sandbox_modes`, `permissions.filesystem.deny_read` | Codex darf nur in definierten Arbeitsverzeichnissen schreiben. Sensitive Pfade wie `.ssh`, `.gnupg`, `.docker`, `.codex`, OpenCode-Daten und Secret-Dateien sind als Leseverbote dokumentiert. |
| OpenCode-Schreib- und Leseregeln | `opencode.jsonc`: `permission.edit`, `permission.bash`, `permission.webfetch`, `permission.read` | OpenCode fragt fuer Shell-Kommandos nach Freigabe, verbietet Webfetch und blockiert das Lesen typischer Secret- und Tool-State-Pfade. |
| Netzwerkentscheidung | `docs/security/network-decision.md`: freier Egress bewusst dokumentiert; `codex/config.toml`: `[sandbox_workspace_write].network_access = false` | Die Containerumgebung nutzt weiterhin den normalen Compose-Netzwerkpfad mit freiem Egress, weil die Lernumgebung externe Quellen braucht. Innerhalb von Codex ist Netzwerkzugriff im Workspace-Write-Sandboxmodus deaktiviert. Die Egress-Entscheidung ist eine dokumentierte Risikoentscheidung, keine technische Netzwerkblockade. |
| Geheimnis-Trennung | `.gitignore`: `opencode.env`; `compose.yml`: `env_file: opencode.env`; `codex/config.toml`: `shell_environment_policy.exclude`; `codex/requirements.toml` und `opencode.jsonc`: Leseverbote fuer Secret-Pfade | Secrets werden nicht im Repository gespeichert. Der GWDG-API-Key wird zur Laufzeit ueber `opencode.env` eingebracht und darf nicht in Logs, Inventare oder Dokumentation uebernommen werden. |
| Audit-Metadaten | `scripts/audit-export.sh`; `scripts/compose-down-with-audit.sh`; `scripts/compose-down-with-audit.ps1`; `compose.yml`: Mount `./audit-logs:/audit`, `ADE_AUDIT_ON_STOP: "true"` | Der dokumentierte Standardweg exportiert Metadaten vor `compose down`. Der Stop-Hook im Image ist eine zusaetzliche Best-Effort-Absicherung bei graceful shutdown. |
| Supply-Chain-Kontrolle | `Dockerfile`: gepinntes Basisimage per `sha256`-Digest, signierte NodeSource-Apt-Quelle, uv-Release-Artefakt mit SHA256-Pruefung, gepinnte Tool-ARGs fuer OpenCode, Codex, Spec Kit, Go und Rust; `docs/security/ai-tools-inventory.md`; `docs/security/supply-chain-todo.md`; `scripts/build-and-sbom.*` | Das Basisimage ist reproduzierbar per Digest referenziert. Node.js wird ueber eine signierte Apt-Quelle statt ueber ein ausgefuehrtes Setup-Skript installiert. uv und uvx werden aus einem festen Release-Artefakt nach SHA256-Pruefung installiert. Fuer das finale Image kann eine CycloneDX-SBOM erzeugt werden. P3-1 bleibt fuer Rust offen, bis auch dieser Installerpfad durch ein verifizierteres Verfahren ersetzt ist. |
| Runtime-Haertung | `compose.yml`: kein `privileged: true`; P3-4 im `COMPLIANCE-PLAN_RL-SE-001.md` | Das aktuelle Schutzniveau beruht auf Docker-/Podman-Standardisolation, non-root-Ausfuehrung und Agentenregeln. Zusaetzliche Compose-Haertungen wie `no-new-privileges` und `cap_drop` sind als P3-4 noch offen. |

### Schutzniveau-Begruendung

Die aktuelle Isolation ist geeignet fuer eine kurzlebige Lern- und
Entwicklungsumgebung mit Beispielcode, Schulungsprojekten und nicht-sensiblen
Arbeitsdaten. Sie ist nicht als dauerhafte VM, nicht als Produktionssystem und
nicht fuer produktive Geheimnisse, besondere Kategorien personenbezogener
Daten oder vertrauliche interne Daten freigegeben.

Die abschliessende Aussage "Schutzniveau ausreichend fuer
Datenklassifikation X" ist eine Entscheidung des Owners, der/des CISO/ISB oder
der/des KI-Beauftragten (KIB) und bleibt hier offen:

`_TODO_ (Owner/CISO/ISB/KIB: freigegebene Datenklassifikation und
Schutzniveau-Bewertung eintragen)`

### Offene Verstaerkungen

- P3-4: Compose-Haertung pruefen und gegebenenfalls `no-new-privileges`,
  `cap_drop`/`cap_add`, Read-only-Filesystem oder vergleichbare Direktiven
  konfigurieren.
- P3-1: Verbleibenden Rust-Installerpfad weiter haerten und
  Curl-Pipe-Bash-Muster ersetzen.
- Plattformseitige Governance wie Branch Protection, Push Rules und formelle
  Freigabe bleibt in GitLab beziehungsweise bei Owner/CISO/ISB/KIB.

### Verweise

- `Dockerfile`
- `compose.yml`
- `codex/config.toml`
- `codex/requirements.toml`
- `opencode.jsonc`
- `docs/security/sandbox-freigabe.md`
- `docs/security/network-decision.md`
- `docs/security/ai-tools-inventory.md`
- `docs/security/branch-protection.md`

## English

### Sandbox Type

The `ade-dev-sandbox` is a container sandbox according to the RL-SE-001
typology for agentic AI in sandbox environments. It is built and started with
Docker Compose or Podman Compose.

### Isolation Mechanisms and Evidence

| Mechanism | Evidence source | Assessment |
|---|---|---|
| Non-privileged runtime | `Dockerfile`: `useradd -m -s /bin/bash adedev`, `USER adedev`; `compose.yml`: service `ade` starts the built image without `privileged: true` | After the image build, the container runs as user `adedev`, not as `root`. Root privileges are used only during image build for package installation and system paths. |
| Filesystem boundaries | `compose.yml`: service `ade`, `volumes` section; `docs/security/sandbox-freigabe.md`: approved mount list | Host files are visible only through explicitly configured bind mounts: `/workspace`, `/rider-projects`, `/java-projects`, `/go-projects`, `/rust-projects`, `/python-projects`, and `/audit`. The .NET configuration `./dotnet/ContainerBuild.props` is mounted read-only with `:ro`. |
| Separation of build and agent data | `compose.yml`: named volumes `dotnet_build`, `opencode_data`, `codex_data`; mounts to `/dotnet-build`, `/home/adedev/.local/share/opencode`, `/home/adedev/.codex` | Persistent tool and build data is kept in named volumes and is not committed as repository content. |
| Codex write boundaries | `codex/config.toml`: `sandbox_mode = "workspace-write"`, `[sandbox_workspace_write].writable_roots`; `codex/requirements.toml`: `allowed_sandbox_modes`, `permissions.filesystem.deny_read` | Codex may write only to defined work directories. Sensitive paths such as `.ssh`, `.gnupg`, `.docker`, `.codex`, OpenCode data, and secret files are documented as read-denied paths. |
| OpenCode write and read rules | `opencode.jsonc`: `permission.edit`, `permission.bash`, `permission.webfetch`, `permission.read` | OpenCode asks before shell commands, denies webfetch, and blocks reads from typical secret and tool-state paths. |
| Network decision | `docs/security/network-decision.md`: free egress intentionally documented; `codex/config.toml`: `[sandbox_workspace_write].network_access = false` | The container environment still uses the normal Compose network path with free egress because the learning environment needs external sources. Within Codex, network access is disabled in workspace-write sandbox mode. The egress decision is a documented risk decision, not a technical network block. |
| Secret separation | `.gitignore`: `opencode.env`; `compose.yml`: `env_file: opencode.env`; `codex/config.toml`: `shell_environment_policy.exclude`; `codex/requirements.toml` and `opencode.jsonc`: read denies for secret paths | Secrets are not stored in the repository. The GWDG API key is provided at runtime through `opencode.env` and must not be copied into logs, inventories, or documentation. |
| Audit metadata | `scripts/audit-export.sh`; `scripts/compose-down-with-audit.sh`; `scripts/compose-down-with-audit.ps1`; `compose.yml`: mount `./audit-logs:/audit`, `ADE_AUDIT_ON_STOP: "true"` | The documented standard path exports metadata before `compose down`. The image stop hook is an additional best-effort safeguard on graceful shutdown. |
| Supply-chain control | `Dockerfile`: base image pinned by `sha256` digest, signed NodeSource Apt source, uv release artifact with SHA256 verification, pinned tool ARGs for OpenCode, Codex, Spec Kit, Go, and Rust; `docs/security/ai-tools-inventory.md`; `docs/security/supply-chain-todo.md`; `scripts/build-and-sbom.*` | The base image is referenced reproducibly by digest. Node.js is installed through a signed Apt source instead of an executed setup script. uv and uvx are installed from a fixed release artifact after SHA256 verification. A CycloneDX SBOM can be generated for the final image. P3-1 remains open for Rust until that installer path is replaced by a more verified method as well. |
| Runtime hardening | `compose.yml`: no `privileged: true`; P3-4 in `COMPLIANCE-PLAN_RL-SE-001.md` | The current protection level relies on Docker/Podman default isolation, non-root execution, and agent rules. Additional Compose hardening such as `no-new-privileges` and `cap_drop` remains open as P3-4. |

### Protection-Level Rationale

The current isolation is suitable for a short-lived learning and development
environment with sample code, training projects, and non-sensitive work data.
It is not approved as a long-lived VM, not a production system, and not for
production secrets, special categories of personal data, or confidential
internal data.

The final statement "protection level sufficient for data classification X" is
a decision by the owner, CISO/ISB, or AI officer (KIB) and remains open here:

`_TODO_ (owner/CISO/ISB/KIB: enter approved data classification and
protection-level assessment)`

### Open Reinforcements

- P3-4: Review Compose hardening and, where feasible, configure
  `no-new-privileges`, `cap_drop`/`cap_add`, a read-only filesystem, or
  comparable directives.
- P3-1: Further harden the remaining Rust installer path and replace
  curl-pipe-bash patterns.
- Platform-side governance such as branch protection, push rules, and formal
  approval remains in GitLab or with owner/CISO/ISB/KIB.

### References

- `Dockerfile`
- `compose.yml`
- `codex/config.toml`
- `codex/requirements.toml`
- `opencode.jsonc`
- `docs/security/sandbox-freigabe.md`
- `docs/security/network-decision.md`
- `docs/security/ai-tools-inventory.md`
- `docs/security/branch-protection.md`
