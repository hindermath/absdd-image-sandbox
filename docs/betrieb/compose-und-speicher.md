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

**DE:** Eingehend veröffentlicht Compose nur `127.0.0.1:5100-5199`.
Port `5199` gehört dem passwortgeschützten OpenCode-Server; eigene Web-Apps
verwenden `5100-5198` und binden im Container an `0.0.0.0`.

**EN:** For inbound access, Compose publishes only
`127.0.0.1:5100-5199`. Port `5199` is reserved for the password-protected
OpenCode server. Other web apps bind to `0.0.0.0` inside the container and use
`5100-5198`.

## Build-Profil / Build Profile

**DE:** `ADE_MSL_PROFILE` in der lokalen `.env` waehlt beim Build `dotnet`,
`java`, `go`, `rust`, `python`, `swift` oder `all`. `.NET` und gemeinsame
Infrastruktur sind immer enthalten; `all` behaelt alle sechs Toolchains.
Eine Aenderung ist kein Laufzeitschalter: im Host-Terminal mit Podman-Compose
und vorhandener `opencode.env` neu bauen, den bisherigen Service ueber
`scripts/compose-down-with-audit.sh --podman` mit Metadatenexport stoppen und
mit `podman compose up -d` neu erstellen. Die benannten Volumes bleiben
erhalten. Erwartet wird das Profil in `/usr/local/share/ade/msl-profile.json`
und im Image-Label. Bei einem unbekannten Profil bricht der Build ab; bei
Socketfehlern den lokalen Podman-Machine-Socket pruefen. Fuer `all` den Wert
entfernen oder `ADE_MSL_PROFILE=all` setzen.

**EN:** Set `ADE_MSL_PROFILE` in local `.env` to `dotnet`, `java`, `go`,
`rust`, `python`, `swift`, or `all` at build time. .NET and shared tools are
always present; `all` keeps all six toolchains. Changing this value requires
a rebuild and container recreation. In a host shell with Podman Compose and
`opencode.env`, build, stop through `scripts/compose-down-with-audit.sh
--podman`, then run `podman compose up -d`. Named volumes remain. Check the
manifest and image label for the selected profile. Unknown profiles fail the
build; check the local Podman machine socket if the engine is unreachable.
Remove the setting or use `ADE_MSL_PROFILE=all` to return to the full image.

**DE:** Ein direkter Host-Build ohne Zielangabe verwendet `all`. Fuer einen
gezielten direkten ARM64- oder AMD64-Build auf einem **nativen** Podman-Host
werden Ziel und ARG gemeinsam gesetzt, etwa in Bash fuer Java:

```bash
podman build --pull --format docker --target ade-java \
  --build-arg ADE_MSL_PROFILE=java -t localhost/ade-java:local .
```

Erwartet wird ein Image mit Profil-Label `java`. Wenn Podman den Machine-Socket
oder eine Downloadquelle nicht erreicht, diesen Zugang vor dem Wiederholen
pruefen. Der direkte Image-Tag ist von der Compose-Auswahl getrennt.

**EN:** A direct host build without a target uses `all`. For a focused direct
build on a **native** Podman host, set the target and ARG together as above.
The expected result is an image labelled `java`; if Podman cannot reach its
machine socket or a download source, fix that access before retrying. The
Compose selection above remains separate from direct build tags.

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

**DE:** `opencode.env` ist ungetrackt. Vor dem Webstart muss es ein privates
`OPENCODE_PASSWORD` mit mindestens 16 Zeichen enthalten; leere Werte und
bekannte Platzhalter werden abgewiesen. Oeffne danach am Host
`http://127.0.0.1:5199` und melde dich mit Benutzer `opencode` an. Fehlende
Passwoerter verursachen bei `restart: unless-stopped` wiederholte Startfehler;
Portkonflikte erfordern einen freien Host-Port oder das Stoppen des anderen
Stacks. Provider-Variablen bleiben optional.
Normale Agentenanmeldungen verwenden die offiziellen interaktiven Flows und
die benannten Volumes. Echte Secrets werden weder ausgegeben noch in
Dokumentation, Audit-JSONL oder Screenshots übernommen.

**EN:** `opencode.env` is untracked. Before starting the web service, set a
private `OPENCODE_PASSWORD` of at least 16 characters; empty and known
placeholder values fail. Open `http://127.0.0.1:5199` on the host and sign in
as `opencode`. A missing password can cause repeated starts under
`restart: unless-stopped`; resolve a port conflict by freeing the host port
or stopping the other stack. Provider variables remain optional. Agent sign-ins use
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

## Praktisch belegte Grenze / Practically Evidenced Boundary

**DE:** Das unveraenderte finale Image startete auf einem nativen
rootless-Podman-Host unter macOS als `adedev`. Der Lauf bestaetigte die
deklarierte Mountliste, getrennte Agenten-Volumes, `no-new-privileges`,
entfernte Capabilities, Loopback-Ports `5100-5199` und den Audit-Wrapper beim
Stoppen. Er belegt weder den Windows-Hostpfad noch Ubuntu/WSL2 mit eigener
rootless-Podman-Laufzeit und nicht den VS-Code-Attach. Freier ausgehender
Netzwerkzugriff bleibt eine offene Owner-Entscheidung und wird nicht als
akzeptiertes Risiko beschrieben.

**EN:** The unchanged final image ran as `adedev` on native macOS rootless
Podman and confirmed the declared mounts, separate agent volumes,
`no-new-privileges`, dropped capabilities, loopback ports `5100-5199`, and
audit-aware stop. It proves neither the Windows-host path nor Ubuntu/WSL2 with
its own rootless Podman runtime, and it does not prove VS Code attachment.
Unrestricted outbound networking remains an open owner decision, not accepted
risk.
