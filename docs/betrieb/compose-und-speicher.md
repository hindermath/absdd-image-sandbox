# Compose und Speicher / Compose and Storage

## Service und Netz / Service and Network

**DE:** `compose.yml` definiert einen Service `ade`. Er baut das lokale Image,
arbeitet in `/rider-projects` und läuft mit `restart: unless-stopped`. Die
Lernumgebung verwendet bewusst das Compose-Default-Bridge-Netz mit freiem
ausgehendem Netzwerkzugriff. Das ist eine dokumentierte Risikoentscheidung,
keine technische Allow-List.

**EN:** `compose.yml` defines one service named `ade`. It builds the local
image, works in `/rider-projects`, and uses `restart: unless-stopped`. The
learning environment deliberately uses the Compose default bridge with free
outbound network access. This is a documented risk decision, not a technical
allow-list.

**DE:** Eingehend veröffentlicht Compose nur `127.0.0.1:5100-5199`. Eine
Webanwendung bindet im Container an `0.0.0.0` und verwendet einen Port aus
diesem Bereich. Andere Ports sind nicht Teil des öffentlichen Vertrags.

**EN:** For inbound access, Compose publishes only
`127.0.0.1:5100-5199`. A web application binds to `0.0.0.0` inside the
container and uses a port from that range. Other ports are not part of the
public contract.

## Bind-Mounts / Bind Mounts

| Variable oder Quelle / Variable or source | Containerziel / Container target | Zweck / Purpose |
|---|---|---|
| `./workspace` | `/workspace` | allgemeine Arbeit / general work |
| `ADE_DEV_SANDBOX_DIR` | `/ade-dev-sandbox` | kontrollierte Wartung dieses Repos / controlled maintenance of this repo |
| `RIDER_PROJECTS_DIR` | `/rider-projects` | .NET-/Rider-Projekte / .NET and Rider projects |
| `JAVA_PROJECTS_DIR` | `/java-projects` | Java und Maven / Java and Maven |
| `GO_PROJECTS_DIR` | `/go-projects` | Go |
| `RUST_PROJECTS_DIR` | `/rust-projects` | Rust |
| `PYTHON_PROJECTS_DIR` | `/python-projects` | Python |
| `POWERSHELL_PROJECTS_DIR` | `/powershell-projects` | PowerShell |
| `SWIFT_PROJECTS_DIR` | `/swift-projects` | Swift |
| drei `SECURE_*_PROJECTS_DIR` | gleichnamige `/secure-*-projects`-Pfade / matching paths | Secure-Trader-Lernprojekte / Secure Trader training projects |
| `AUDIT_DIR` | `/audit` | ausschließlich Audit-Metadaten / audit metadata only |
| `./dotnet/ContainerBuild.props` | `/dotnet-config/ContainerBuild.props` | read-only .NET-Buildvertrag / read-only .NET build contract |

**DE:** Die Standardwerte stehen in `.env.example` und zeigen auf lokale
Fallback-Verzeichnisse. Ein produktiver oder persönlicher Hostpfad bleibt in
der ungetrackten `.env` beziehungsweise in der lokalen Umgebung. Konkrete
absolute Hostpfade werden nicht in `compose.yml` committet.

**EN:** Defaults are documented in `.env.example` and point to local fallback
directories. A production or personal host path remains in untracked `.env`
or the local environment. Concrete absolute host paths are not committed to
`compose.yml`.

## Benannte Volumes / Named Volumes

| Volume | Ziel / Target | Lebensdauer und Risiko / Lifetime and risk |
|---|---|---|
| `dotnet_build` | `/dotnet-build` | Build-Ausgaben bleiben außerhalb der Bind-Mounts / build output remains outside bind mounts |
| `opencode_data` | `/home/adedev/.local/share/opencode` | OpenCode-Zustand / OpenCode state |
| `codex_data` | `/home/adedev/.codex` | Codex-Konfiguration und Anmeldung / Codex configuration and sign-in |
| `claude_data` | `/home/adedev/.claude` | Claude-Zustand / Claude state |
| `gemini_data` | `/home/adedev/.gemini-home` | Gemini und Antigravity / Gemini and Antigravity |
| `copilot_data` | `/home/adedev/.copilot` | Copilot-Zustand / Copilot state |

**DE:** `podman compose down` erhält Volumes. `podman compose down -v` löscht
sie einschließlich lokaler Anmeldungen und Einstellungen. Vor einer
Volumenlöschung ist der Audit-Wrapper Pflicht; die Löschabsicht muss explizit
sein.

**EN:** `podman compose down` preserves volumes. `podman compose down -v`
deletes them, including local sign-ins and settings. The audit wrapper is
mandatory before volume removal, and deletion must be intentional.

## Home-Baseline-Override / Home Baseline Override

**DE:** Im Standardimage ist `/opt/home-baseline` read-only. Der optionale
Compose-Override ersetzt genau dieses Ziel durch den unter
`HOME_BASELINE_DIR` gewählten persönlichen oder institutionellen Checkout:

**EN:** In the standard image, `/opt/home-baseline` is read-only. The optional
Compose override replaces exactly this target with the personal or
institutional checkout selected through `HOME_BASELINE_DIR`:

```bash
HOME_BASELINE_DIR=/path/to/home-baseline-source \
  podman-compose -f compose.yml -f compose.home-baseline.yml config
```

**DE:** Ein vorhandener Checkout wird nicht automatisch gepullt, committet
oder gepusht. Der Override ändert nur den Mount. Beide Home-Links zeigen danach
weiterhin auf `/opt/home-baseline`.

**EN:** An existing checkout is not automatically pulled, committed, or
pushed. The override changes only the mount. Both home links continue to point
to `/opt/home-baseline`.

## Umgebungsvariablen und Secrets / Environment Variables and Secrets

**DE:** `opencode.env` ist ungetrackt und darf leer bleiben. Es ist nur für
eine bewusst lokal konfigurierte OpenCode-Provider-Variable vorgesehen.
Normale Agentenanmeldungen verwenden die offiziellen interaktiven Flows und
die benannten Volumes. Echte Secrets werden weder ausgegeben noch in
Dokumentation, Audit-JSONL oder Screenshots übernommen.

**EN:** `opencode.env` is untracked and may remain empty. It is intended only
for a deliberately local OpenCode provider variable. Normal agent sign-ins use
official interactive flows and named volumes. Real secrets are never printed
or copied into documentation, audit JSONL, or screenshots.

**DE:** Weitere Umgebungswerte deaktivieren automatische Agentenupdates,
halten .NET-Workload-Benachrichtigungen ruhig und teilen den Dispatcher mit,
dass er im Container lokale CLIs ausführt. Diese Werte sind Laufzeitverträge
und werden nicht in einer Shellprofil-Datei versteckt.

**EN:** Additional environment values disable automatic agent updates, silence
.NET workload notifications, and tell the dispatcher to invoke local CLIs
inside the container. These values are runtime contracts and are not hidden in
a shell profile.

## Laufzeithärtung / Runtime Hardening

| Kontrolle / Control | Einstellung / Setting | Wirkung / Effect |
|---|---|---|
| non-root | finaler Benutzer `adedev` / final user `adedev` | keine Root-Rechte im normalen Lauf / no root privileges in normal operation |
| keine neuen Privilegien / no new privileges | `no-new-privileges:true` | blockiert Rechteerhöhung über setuid/setgid / blocks privilege gain through setuid/setgid |
| Capability-Minimum | `cap_drop: ALL` | entzieht Linux-Capabilities / drops Linux capabilities |
| kein privilegierter Modus / no privileged mode | kein `privileged: true` / no `privileged: true` | keine Host-Kernel-Kontrolle / no host-kernel control |
| begrenztes Ingress | Loopback-Ports `5100-5199` | keine öffentliche Bindung / no public binding |

**DE:** Das Root-Dateisystem bleibt beschreibbar und es gibt keine festen CPU-
oder Speicherlimits. Diese offenen Härtungsoptionen sind dokumentierte
Abwägungen für Build- und Lernworkflows, keine versehentlich behaupteten
Kontrollen.

**EN:** The root filesystem remains writable and there are no fixed CPU or
memory limits. These open hardening options are documented tradeoffs for build
and learning workflows, not controls claimed by accident.

## Konfiguration prüfen / Validate Configuration

```bash
podman-compose config
```

**DE:** Für Lifecycle-Befehle darf je nach Plattform `podman compose` oder
`podman-compose` verwendet werden. Ein gespeicherter SSH-Port ist kein
Repository-Standard. Wenn auf macOS ein expliziter Endpoint nötig ist, wird
der Unix-Socket zur Laufzeit aus `podman machine inspect` ermittelt und nie
committet.

**EN:** Depending on the platform, lifecycle commands may use `podman compose`
or `podman-compose`. A stored SSH port is not a repository default. If macOS
needs an explicit endpoint, derive the Unix socket at runtime from
`podman machine inspect` and never commit it.

Weiter zu [Validierung und Wartung](validierung-und-wartung.md). / Continue
with [Validation and maintenance](validierung-und-wartung.md).
