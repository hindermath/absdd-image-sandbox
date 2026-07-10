# Sandbox-Isolationsnachweis

Stand: 2026-07-05

Dieses Dokument konsolidiert die technischen Isolationsmechanismen der
`absdd-image-sandbox`. Es beschreibt vorhandene Konfigurationen und aendert keine
Sandbox-Einstellung.

## Deutsch

### Sandbox-Typ

Die `absdd-image-sandbox` ist eine Container-Sandbox gemaess der lokalen
Secure-Development-Typologie fuer agentische KI in Sandbox-Umgebungen. Sie
wird ueber Podman Compose gebaut und gestartet.

### Isolationsmechanismen und Evidenz

| Mechanismus | Evidenzquelle | Bewertung |
|---|---|---|
| Nicht-privilegierte Laufzeit | `Dockerfile`: `useradd -m -s /bin/bash adedev`, `USER adedev`; `compose.yml`: Service `ade` startet das gebaute Image ohne `privileged: true` | Der Container laeuft nach dem Image-Build als Benutzer `adedev`, nicht als `root`. Root-Rechte werden nur waehrend des Image-Builds fuer Paketinstallation und Systempfade genutzt. |
| Dateisystem-Grenzen | `compose.yml`: Service `ade`, Abschnitt `volumes`; optional `compose.home-baseline.yml`; `docs/security/sandbox-freigabe.md`: "Genehmigte Mount-Liste" | Host-Dateien sind nur ueber explizit konfigurierte Bind-Mounts sichtbar: `/ade-dev-sandbox`, `/workspace`, `/rider-projects`, `/java-projects`, `/go-projects`, `/rust-projects`, `/python-projects`, `/swift-projects`, `/secure-case-tracker-projects`, `/secure-service-harvester-projects`, `/secure-order-desk-projects`, `/audit` und optional `/opt/home-baseline`. Die eingebaute Level-0-Referenz liegt root-eigen und ohne Schreibbits unter `/opt/home-baseline`; `~/home-baseline-tmp` ist ein Symlink. Der optionale persoenliche Mount ueberdeckt dieses Ziel. Die .NET-Konfiguration `./dotnet/ContainerBuild.props` ist mit `:ro` read-only gemountet. |
| Trennung von Build- und Agentendaten | `compose.yml`: benannte Volumes `dotnet_build`, `opencode_data`, `codex_data`; Mounts nach `/dotnet-build`, `/home/adedev/.local/share/opencode`, `/home/adedev/.codex` | Persistente Tool- und Build-Daten werden in benannten Volumes gehalten und nicht als Repository-Dateien committet. |
| Codex-Schreibgrenzen | `codex/config.toml`: `sandbox_mode = "workspace-write"`, `[sandbox_workspace_write].writable_roots`; `codex/requirements.toml`: `allowed_sandbox_modes`, `permissions.filesystem.deny_read` | Codex darf nur in definierten Arbeitsverzeichnissen schreiben, einschliesslich `/ade-dev-sandbox`, den Projekt-Mounts sowie `/opt/home-baseline` und dem Alias `/home/adedev/home-baseline-tmp`. Im Standardmodus verhindern root-Eigentum und fehlende Schreibbits Aenderungen an der eingebauten Referenz. Erst der bewusst aktivierte persoenliche Bind-Mount macht diesen Bereich beschreibbar. Sensitive Pfade bleiben als Leseverbote dokumentiert. |
| OpenCode-Schreib- und Leseregeln | `opencode.jsonc`: `permission.edit`, `permission.bash`, `permission.webfetch`, `permission.read` | OpenCode fragt fuer Shell-Kommandos und Webfetch nach Freigabe und blockiert das Lesen typischer Secret- und Tool-State-Pfade. |
| Netzwerkentscheidung | `docs/security/network-decision.md`: freier Egress bewusst dokumentiert; `codex/config.toml`: `[sandbox_workspace_write].network_access = false` | Die Containerumgebung nutzt weiterhin den normalen Compose-Netzwerkpfad mit freiem Egress, weil die Lernumgebung externe Quellen braucht. Innerhalb von Codex ist Netzwerkzugriff im Workspace-Write-Sandboxmodus deaktiviert. Die Egress-Entscheidung ist eine dokumentierte Risikoentscheidung, keine technische Netzwerkblockade. |
| Optionaler VS-Code-Zugang | `.devcontainer/devcontainer.json`, `README.md`, `compose.yml` | VS Code kann von aussen per Dev Containers an den laufenden `ade`-Container anhaengen. Dabei wird kein dauerhafter Browser-IDE- oder VS-Code-Server-Dienst im Image gestartet und kein zusaetzlicher IDE-Port veroeffentlicht; VS Code installiert seinen Remote-Server beim Verbinden selbst in den Container. |
| Geheimnis-Trennung | `.gitignore`: `opencode.env`; `compose.yml`: `env_file: opencode.env`; `codex/config.toml`: `shell_environment_policy.exclude`; `codex/requirements.toml` und `opencode.jsonc`: Leseverbote fuer Secret-Pfade | Secrets werden nicht im Repository gespeichert. Lokale Provider-Schluessel duerfen nur bei Bedarf ueber `opencode.env` eingebracht werden und duerfen nicht in Logs, Inventare oder Dokumentation uebernommen werden. |
| Audit-Metadaten | `scripts/audit-export.sh`; `scripts/compose-down-with-audit.sh`; `scripts/compose-down-with-audit.ps1`; `compose.yml`: Mount `./audit-logs:/audit`, `ADE_AUDIT_ON_STOP: "true"` | Der dokumentierte Standardweg exportiert Metadaten vor `compose down`. Der Stop-Hook im Image ist eine zusaetzliche Best-Effort-Absicherung bei graceful shutdown. |
| Supply-Chain-Kontrolle | `Dockerfile`; `home-baseline.lock.json`; MCR-.NET-SDK-Basisimage per `sha256`-Digest, verifizierte Release-Artefakte und gepinnte Tool-ARGs; `scripts/build-and-sbom.*` | Das Basisimage ist per Digest referenziert. Die eingebettete MIT-lizenzierte Level-0-Referenz wird als Shallow-Git-Checkout aus einem Release geladen; Build und Lock-Validator erzwingen Tag und exakten Commit. Keine Baseline-Skripte laufen automatisch. Fuer das finale Image kann eine CycloneDX-SBOM erzeugt werden. |
| Runtime-Haertung | `compose.yml`: kein `privileged: true`, `security_opt: no-new-privileges:true`, `cap_drop: ALL`; P3-4 im `COMPLIANCE-PLAN_RL-SE-001.md`; Testevidenz vom 2026-05-27: `NoNewPrivs: 1`, `CapEff: 0000000000000000` | Das aktuelle Schutzniveau kombiniert Podman-Standardisolation, non-root-Ausfuehrung, Agentenregeln und Compose-Haertung. Prozesse koennen keine neuen Privilegien ueber setuid/setgid oder File-Capabilities erlangen. Alle Linux-Capabilities werden zur Laufzeit entzogen; die validierten Toolchains benoetigen keine `cap_add`-Ausnahme. |

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

- P3-1: Verbleibenden Rust-Installerpfad weiter haerten und
  Curl-Pipe-Bash-Muster ersetzen.
- Weitere optionale Compose-Verstaerkungen wie `read_only: true`,
  `pids_limit` sowie Speicher- und CPU-Limits koennen spaeter separat
  geprueft werden. Sie sind nicht Teil der aktuell validierten P3-4-
  Mindesthaertung, weil ein schreibbares Root-Dateisystem und flexible
  Ressourcenlimits fuer Lern-, Build- und Tooling-Workflows relevant sein
  koennen.
- Plattformseitige Governance wie Repository Rulesets, Required Checks,
  Admin-Bypass und formelle Freigabe bleibt auf GitHub beziehungsweise bei
  Owner/CISO/ISB/KIB.

### Verweise

- `Dockerfile`
- `compose.yml`
- `compose.home-baseline.yml`
- `.devcontainer/devcontainer.json`
- `codex/config.toml`
- `codex/requirements.toml`
- `opencode.jsonc`
- `docs/security/sandbox-freigabe.md`
- `docs/security/network-decision.md`
- `docs/security/ai-tools-inventory.md`
- `docs/security/branch-protection.md`

## English

### Sandbox Type

The `absdd-image-sandbox` is a container sandbox according to the local
secure-development typology for agentic AI in sandbox environments. It is
built and started with Podman Compose.

### Isolation Mechanisms and Evidence

| Mechanism | Evidence source | Assessment |
|---|---|---|
| Non-privileged runtime | `Dockerfile`: `useradd -m -s /bin/bash adedev`, `USER adedev`; `compose.yml`: service `ade` starts the built image without `privileged: true` | After the image build, the container runs as user `adedev`, not as `root`. Root privileges are used only during image build for package installation and system paths. |
| Filesystem boundaries | `compose.yml`: service `ade`, `volumes` section; optional `compose.home-baseline.yml`; `docs/security/sandbox-freigabe.md`: approved mount list | Host files are visible only through explicitly configured bind mounts, including optional `/opt/home-baseline`. The embedded Level-0 reference is root-owned without write bits at `/opt/home-baseline`; `~/home-baseline-tmp` is a symlink. The optional personal mount covers this target. The .NET configuration remains mounted read-only with `:ro`. |
| Separation of build and agent data | `compose.yml`: named volumes `dotnet_build`, `opencode_data`, `codex_data`; mounts to `/dotnet-build`, `/home/adedev/.local/share/opencode`, `/home/adedev/.codex` | Persistent tool and build data is kept in named volumes and is not committed as repository content. |
| Codex write boundaries | `codex/config.toml`: `sandbox_mode = "workspace-write"`, `[sandbox_workspace_write].writable_roots`; `codex/requirements.toml`: `allowed_sandbox_modes`, `permissions.filesystem.deny_read` | Codex is limited to declared work directories, including `/opt/home-baseline` and its user-facing alias. In default mode, root ownership and missing write bits prevent changes to the embedded reference. Only the deliberately enabled personal bind mount makes this area writable. Sensitive paths remain read-denied. |
| OpenCode write and read rules | `opencode.jsonc`: `permission.edit`, `permission.bash`, `permission.webfetch`, `permission.read` | OpenCode asks before shell commands and webfetch and blocks reads from typical secret and tool-state paths. |
| Network decision | `docs/security/network-decision.md`: free egress intentionally documented; `codex/config.toml`: `[sandbox_workspace_write].network_access = false` | The container environment still uses the normal Compose network path with free egress because the learning environment needs external sources. Within Codex, network access is disabled in workspace-write sandbox mode. The egress decision is a documented risk decision, not a technical network block. |
| Optional VS Code access | `.devcontainer/devcontainer.json`, `README.md`, `compose.yml` | VS Code can attach from the host to the running `ade` container through Dev Containers. No long-running browser IDE or VS Code Server service is started in the image and no additional IDE port is published; VS Code installs its remote server into the container when it connects. |
| Secret separation | `.gitignore`: `opencode.env`; `compose.yml`: `env_file: opencode.env`; `codex/config.toml`: `shell_environment_policy.exclude`; `codex/requirements.toml` and `opencode.jsonc`: read denies for secret paths | Secrets are not stored in the repository. Local provider keys may be provided through `opencode.env` when needed and must not be copied into logs, inventories, or documentation. |
| Audit metadata | `scripts/audit-export.sh`; `scripts/compose-down-with-audit.sh`; `scripts/compose-down-with-audit.ps1`; `compose.yml`: mount `./audit-logs:/audit`, `ADE_AUDIT_ON_STOP: "true"` | The documented standard path exports metadata before `compose down`. The image stop hook is an additional best-effort safeguard on graceful shutdown. |
| Supply-chain control | `Dockerfile`; `home-baseline.lock.json`; MCR .NET SDK base image pinned by digest, verified release artifacts, and pinned tool arguments; `scripts/build-and-sbom.*` | The embedded MIT-licensed Level-0 reference is a shallow Git checkout from a release; the build and lock validator enforce its tag and exact commit. No baseline script runs automatically. A CycloneDX SBOM can be generated for the final image. |
| Runtime hardening | `compose.yml`: no `privileged: true`, `security_opt: no-new-privileges:true`, `cap_drop: ALL`; P3-4 in `COMPLIANCE-PLAN_RL-SE-001.md`; test evidence from 2026-05-27: `NoNewPrivs: 1`, `CapEff: 0000000000000000` | The current protection level combines Podman default isolation, non-root execution, agent rules, and Compose hardening. Processes cannot gain new privileges through setuid/setgid binaries or file capabilities. All Linux capabilities are dropped at runtime; the validated toolchains need no `cap_add` exception. |

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

- P3-1: Further harden the remaining Rust installer path and replace
  curl-pipe-bash patterns.
- Additional optional Compose reinforcements such as `read_only: true`,
  `pids_limit`, and memory or CPU limits can be reviewed separately later.
  They are not part of the currently validated P3-4 minimum hardening because
  a writable root filesystem and flexible resource limits can be relevant for
  learning, build, and tooling workflows.
- Platform-side governance such as repository rulesets, required checks, admin
  bypass, and formal approval remains on GitHub or with owner/CISO/ISB/KIB.

### References

- `Dockerfile`
- `compose.yml`
- `compose.home-baseline.yml`
- `.devcontainer/devcontainer.json`
- `codex/config.toml`
- `codex/requirements.toml`
- `opencode.jsonc`
- `docs/security/sandbox-freigabe.md`
- `docs/security/network-decision.md`
- `docs/security/ai-tools-inventory.md`
- `docs/security/branch-protection.md`
