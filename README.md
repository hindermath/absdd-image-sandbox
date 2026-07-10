# Agentische Podman-Sandbox / Agentic Podman Sandbox

Dieses Repository stellt eine Podman-basierte Container-Umgebung fuer
OpenCode, die vier Required-Agenten Codex, Claude Code, Gemini CLI und GitHub
Copilot CLI, sechs speichersichere Sprachen, Syft und Spec Kit bereit. Es ist
eine Sandbox- und Lernumgebung, keine Anwendung.

The repository provides a Podman-based container environment with OpenCode,
the four required agents Codex, Claude Code, Gemini CLI, and GitHub Copilot
CLI, six memory-safe languages, Syft, and Spec Kit. It is a sandbox and
training environment, not an application.

## Kurzueberblick

| Bereich | Standard |
|---|---|
| Container-Laufzeit | Podman |
| Compose-Lifecycle-Befehl | `podman compose` |
| Compose-Config-Validierung | `podman-compose config` |
| Lifecycle-Fallback | `podman-compose`, falls `podman compose` lokal nicht verfuegbar ist |
| Basisimage | Microsoft .NET SDK aus MCR, im `Dockerfile` per Digest gepinnt |
| OpenCode | Installiert, aber ohne vorkonfigurierten Modellanbieter |
| Codex | Systemweite Defaults aus `codex/config.toml` und `codex/requirements.toml` |
| Claude Code | Installiert; persistenter Zustand in `claude_data` |
| Gemini CLI | Installiert; persistenter Zustand in `gemini_data` |
| GitHub Copilot CLI | Installiert; persistenter Zustand in `copilot_data` |
| Software-Bill-of-Materials | Syft ist installiert; `scripts/build-and-sbom.*` erzeugt die Image-SBOM |
| Arbeitsverzeichnis im Container | `/rider-projects` |

## Public-Readiness-Status

Dieses Repository ist als oeffentlich nutzbare Ausbildungs-Sandbox vorbereitet.
Das bedeutet: Anleitungen sollen ohne private Infrastruktur, interne
Organisationstexte oder konkrete Providerkonten verstaendlich sein.

Public-Readiness ist keine formelle Freigabe. Offene Freigabe-, Provider-,
Rechts-, SBOM-, VEX-, SLSA- oder AI-SBOM-Punkte bleiben in
`docs/security/` und den aktiven Spec-Kit-Artefakten als `Open`, `N/A` oder
`_TODO_` sichtbar.

*This repository is prepared as a public-ready training sandbox. That means
the guidance should be understandable without private infrastructure,
organization-specific rules, or concrete provider accounts. Public readiness is
not a formal approval; open approval, provider, legal, SBOM, VEX, SLSA, or
AI-SBOM items remain explicit in `docs/security/` and the active Spec Kit
artifacts.*

## Repository-Struktur

- `Dockerfile`: baut das Image aus dem digest-gepinnten MCR-.NET-SDK-Image
  und installiert Java JDK 21, Maven, Go, Rust, Python, Node.js, OpenCode,
  Swift, die vier Required-Agenten, Syft, `uv`, Spec Kit und Hilfswerkzeuge.
- `compose.yml`: definiert den Service `ade`, getrennte persistente
  Podman-Volumes fuer die Agentenzustaende, die Host-Mounts und die
  Portfreigabe `127.0.0.1:5100-5199`.
- `home-baseline.lock.json`: pinnt Release, Commit, Quelle und Lizenz der
  read-only Level-0-Referenz unter `/opt/home-baseline`.
- `compose.home-baseline.yml`: optionale Compose-Erweiterung, die die
  eingebaute Referenz durch ein eigenes, beschreibbares `home-baseline`-Repo
  ersetzt.
- `.devcontainer/devcontainer.json`: VS-Code-Dev-Containers-Konfiguration,
  damit VS Code von aussen an den laufenden `ade`-Container anhaengen kann.
- `opencode.jsonc`: setzt OpenCode-Sicherheitsregeln, aber keinen API-Key
  und kein vorausgewaehltes Modell.
- `opencode.env.example`: neutrale Vorlage fuer lokale Provider-Secrets,
  falls Nutzer eigene OpenCode-Provider konfigurieren.
- `codex/`: systemweite Codex-Defaults und Anforderungen.
- `dotnet/ContainerBuild.props`: read-only Build-Konfiguration, die .NET-
  Artefakte in das Podman-Volume `/dotnet-build` umleitet.
- `scripts/compose-down-with-audit.*`: exportiert Audit-Metadaten vor dem
  Stoppen der Umgebung.
- `scripts/build-and-sbom.*`: erzeugt eine CycloneDX-SBOM mit dem im finalen
  Image gepinnten Syft, ohne das Image auf dem Host ein zweites Mal zu exportieren.
  Nur dieser kurzlebige Lesescan nutzt Root, damit alle Image-Pfade erfasst
  werden; der Sandbox-Service selbst bleibt der Non-Root-Benutzer `adedev`.
- `docs/security/`: Compliance-, Freigabe-, Inventar- und Evidenzdokumente.

## Voraussetzungen

Podman und Compose-Unterstuetzung muessen installiert sein.

Auf macOS mit Homebrew:

```bash
brew install podman podman-compose
podman machine init
podman machine start
podman info
podman compose version
```

Auf Ubuntu 24.04 LTS oder WSL2:

```bash
sudo apt update
sudo apt install -y podman podman-compose
podman --version
podman-compose --version
```

Auf Windows wird Podman Desktop empfohlen. Danach in PowerShell pruefen:

```powershell
podman --version
podman machine list
podman compose version
```

Fuer reine Compose-Config-Validierung ist `podman-compose config` der
Standard, weil dieser Check die Compose-Datei ohne laufende Podman-Machine
parsen kann. Fuer Build-, Start-, Exec- und Stop-Aktionen wird weiterhin
`podman compose` verwendet; wenn `podman compose` auf einem System nicht
verfuegbar ist, verwende `podman-compose` mit denselben Argumenten.

### Podman-Endpunkt-Auswahl

Dieses Repository nutzt Podman als Container-Laufzeit. Verwende fuer normale
Podman-Befehle zuerst die lokale Standardkonfiguration der Plattform. Setze
einen expliziten API-Endpunkt nur, wenn ein Podman-Machine-, Podman-Desktop-
oder Compose-Provider-Problem dies erfordert.

Auf macOS und Windows werden Podman-Machines typischerweise ueber
plattformlokale Endpunkte erreichbar gemacht. Ermittle den aktiven Endpunkt
aus Podman selbst, statt einen Hostpfad, eine Pipe oder einen SSH-Port fest zu
dokumentieren:

```bash
podman machine inspect podman-machine-default
```

Auf macOS kann der Unix-Socket bei Bedarf so fuer Podman und
Docker-kompatible API-Clients gesetzt werden:

```bash
PODMAN_SOCKET="$(podman machine inspect podman-machine-default --format '{{.ConnectionInfo.PodmanSocket.Path}}')"
test -S "$PODMAN_SOCKET"
CONTAINER_HOST="unix://${PODMAN_SOCKET}" DOCKER_HOST="unix://${PODMAN_SOCKET}" podman info
```

Auf Windows die von `podman machine inspect` gemeldete `PodmanPipe` oder den
gemeldeten Socket nutzen und nicht als projektspezifischen Default
festschreiben. Auf Linux ist fuer direkte `podman`-Befehle normalerweise kein
Endpoint-Override noetig. Wenn Docker-kompatible API-Werkzeuge einen Socket
brauchen, verwende den lokal aktivierten Podman-Socket, zum Beispiel
`unix://${XDG_RUNTIME_DIR}/podman/podman.sock` fuer rootless Podman.

`DOCKER_HOST` bezeichnet in diesem Kontext nur die Docker-kompatible
Podman-API fuer entsprechende Clients. Docker selbst ist fuer dieses Repository
weiterhin nicht die Ziel-Laufzeit.

## Lokale Konfiguration

Kopiere die Beispielumgebungsdatei, damit `compose.yml` eine vorhandene
`opencode.env` findet:

```bash
cp opencode.env.example opencode.env
chmod 600 opencode.env
```

Dieses Image konfiguriert keinen OpenCode-API-Key und kein vorausgewaehltes
Modell. Die eingebaute OpenCode-Provider-Auswahl bleibt verfuegbar; wenn eine
lokale OpenCode-Konfiguration eigene Provider nutzt, koennen die dafuer
noetigen Secret-Variablen in `opencode.env` eingetragen werden. Secrets nie
committen und nie in Logs ausgeben.

Optionale Host-Mounts werden ueber `.env` oder die Shell gesetzt:

```bash
RIDER_PROJECTS_DIR=/pfad/zu/RiderProjects
JAVA_PROJECTS_DIR=/pfad/zu/java-projects
GO_PROJECTS_DIR=/pfad/zu/go-projects
RUST_PROJECTS_DIR=/pfad/zu/rust-projects
PYTHON_PROJECTS_DIR=/pfad/zu/python-projects
SWIFT_PROJECTS_DIR=/pfad/zu/swift-projects
SECURE_CASE_TRACKER_PROJECTS_DIR=/pfad/zu/SecureCaseTrackerProjects
SECURE_SERVICE_HARVESTER_PROJECTS_DIR=/pfad/zu/SecureServiceHarvesterProjects
SECURE_ORDER_DESK_PROJECTS_DIR=/pfad/zu/SecureOrderDeskProjects
AUDIT_DIR=./audit-logs
```

Nicht gesetzte Variablen fallen auf lokale Repository-Verzeichnisse zurueck.

## Required-Agenten pruefen

Nach dem Build muessen alle vier Required-Agenten und Syft eine Versionsausgabe
liefern. Anmeldung und Providerfreigabe sind davon getrennte, menschlich
verantwortete Schritte.

```bash
podman compose exec ade sh -lc 'codex --version && claude --version && gemini --version && copilot --version && syft version'
```

Die vollstaendige Toolchain prueft:

```bash
podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh
```

## Home-Baseline-Referenz und persoenlicher Override

Das Image enthaelt `home-baseline` als read-only Shallow-Git-Referenz. Release,
Commit, Quelle und MIT-Lizenz sind in `home-baseline.lock.json` festgehalten.
Im Container liegt die Referenz technisch unter `/opt/home-baseline`; der
gewohnte Pfad `~/home-baseline-tmp` zeigt darauf. Dadurch sind die Lernreihen
direkt und nach dem Build auch offline lesbar. Es wird kein Baseline-Skript
automatisch ausgefuehrt und es werden keine Zugangsdaten eingebaut.

```bash
podman compose exec ade sh -lc 'cd ~/home-baseline-tmp && git status --short --branch && git log -1 --oneline'
```

Fuer Aenderungen, Commits und Pushes forken Lernende weiterhin die von ihrer
Institution bereitgestellte Referenz in den persoenlichen Namensraum ihres
Git-Systems und klonen dieses Repository dauerhaft auf dem Host. Nur im
direkten GitHub-Profil ist die Referenz
<https://github.com/hindermath/home-baseline>. Der persoenliche Checkout hat
`origin`; die institutionelle Referenz wird als `upstream` gefuehrt. Die
vollstaendige Reihenfolge steht in der von der Institution mitgelieferten
`START-HERE-FUER-LERNENDE.md`; die oeffentliche Provenienz liegt unter
<https://github.com/hindermath/home-baseline/blob/main/docs/learning-units/START-HERE-FUER-LERNENDE.md>.

Fuer die Verbindung zwischen diesem Sandbox-Image und den Lernreihen siehe
auch [docs/fuer-lernende/README.md](docs/fuer-lernende/README.md).

Der lokale Checkout kann danach die eingebaute read-only Referenz ersetzen:

```bash
HOME_BASELINE_DIR=/pfad/zu/home-baseline-tmp
podman-compose -f compose.yml -f compose.home-baseline.yml config
podman compose -f compose.yml -f compose.home-baseline.yml up -d
podman compose exec ade sh -lc 'cd ~/home-baseline-tmp && git status --short --branch'
```

Der Benutzerpfad bleibt `/home/adedev/home-baseline-tmp`; der Override mountet
den Host-Checkout ueber das reale Ziel `/opt/home-baseline`. Damit bleiben
private Hostpfade und Hosting-Accounts ausserhalb des Images. `sync-home.sh`
wird in beiden Modi nur bewusst manuell ausgefuehrt.

## Bauen und Starten

```bash
podman-compose config
podman compose build --pull
podman compose up -d
podman compose ps
podman compose exec ade bash
```

Der Container startet im Arbeitsverzeichnis `/rider-projects`. Das Image
laeuft nach dem Build als Linux-Benutzer `adedev`.

## VS Code von aussen verbinden

Die empfohlene VS-Code-Nutzung ist der offizielle Dev-Containers-Workflow:
VS Code laeuft auf dem Host und verbindet sich in den laufenden Container.
Es wird kein dauerhafter Browser-IDE- oder VS-Code-Server-Dienst im Image
gestartet und kein zusaetzlicher IDE-Port veroeffentlicht. VS Code installiert
den passenden Remote-Server beim Verbinden selbst in den Container.

Voraussetzungen auf dem Host:

- VS Code Desktop
- VS Code Extension "Dev Containers"
- Podman oder Podman Desktop mit einer Docker-kompatiblen Container-Sicht

Container starten:

```bash
podman compose up -d ade
```

Danach in VS Code:

1. Command Palette oeffnen: `F1`
2. `Dev Containers: Attach to Running Container...` auswaehlen
3. Den Container `ade` beziehungsweise `absdd-image-sandbox-ade-1`
   auswaehlen
4. Im verbundenen Fenster den Ordner `/rider-projects`, `/workspace` oder
   `/swift-projects` oeffnen. Fuer Wartungsarbeiten an diesem Setup-Repo
   `/ade-dev-sandbox` oeffnen.

Zur Kontrolle im VS-Code-Terminal:

```bash
whoami
pwd
```

`whoami` muss `adedev` ausgeben. Wenn ein Projekt Web-Ports braucht, weiter
Ports aus dem bereits veroeffentlichten Bereich `5100-5199` verwenden oder
temporaer ueber VS Code weiterleiten.

Wenn `specify check` im Container `Visual Studio Code (not found)` meldet, ist
das bei diesem Setup erwartbar: VS Code ist ein Host-Werkzeug und nicht als
dauerhaft laufende IDE im Container installiert.

Stoppen ohne Volume-Loeschung:

```bash
bash scripts/compose-down-with-audit.sh --podman
```

Stoppen mit Volume-Loeschung:

```bash
bash scripts/compose-down-with-audit.sh --podman -v
```

PowerShell:

```powershell
.\scripts\compose-down-with-audit.ps1 -Engine podman
.\scripts\compose-down-with-audit.ps1 -Engine podman -Volumes
```

## Toolchecks

Nach Dockerfile-Aenderungen, die Toolchains betreffen, im laufenden Container
pruefen:

```bash
podman compose exec ade sh -lc 'dotnet --info'
podman compose exec ade sh -lc 'java --version; javac --version; mvn --version'
podman compose exec ade sh -lc 'go version; gopls version'
podman compose exec ade sh -lc 'rustc --version; cargo --version; cargo clippy --version'
podman compose exec ade sh -lc 'python --version'
podman compose exec ade sh -lc 'node --version; npm --version'
podman compose exec ade sh -lc 'swift --version; swiftc --version; command -v sourcekit-lsp'
podman compose exec ade sh -lc 'opencode --version; codex --version'
podman compose exec ade sh -lc 'specify version; specify check'
```

Fuer eine praktische Pruefung der MSL-Toolchain-Familien
(.NET/C#, Java/JVM, Go, Rust, Python und JavaScript/TypeScript ueber
Node.js/npm sowie Swift) kann der wiederholbare Smoke-Test im Container
ausgefuehrt werden:

```bash
podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh
```

Der Test legt temporaere Projekte unter `/home/adedev/smoke-tests` an und
raeumt sie nach dem Lauf wieder auf. Der Swift-Teil erzeugt ein temporaeres
SwiftPM-Projekt, baut es mit `swift build` und fuehrt es mit `swift run` aus.
TypeScript- und Kotlin-Compiler werden nicht als global installierte Werkzeuge
behauptet; sie gehoeren bei Bedarf als projektlokale Abhaengigkeiten in das
jeweilige Projekt.

Fuer dokumentierte Web-App-Beispiele im Container an `0.0.0.0` binden und
Ports aus `5100-5199` verwenden. Praktische Checks sollen HTTP-Antworten
pruefen und Hintergrundprozesse am Ende stoppen.

## .NET-Projekte

`dotnet/ContainerBuild.props` wird in den Container als
`/dotnet-config/ContainerBuild.props` gemountet. Dadurch landen `bin`, `obj`
und AppHost-Ausgaben nicht auf Windows-/Host-Bind-Mounts, sondern im
Podman-Volume `/dotnet-build`.

ASP.NET-Anwendungen muessen im Container an `0.0.0.0` binden, damit sie vom
Host erreichbar sind. Verwende Ports aus `5100-5199`, solange `compose.yml`
nicht angepasst wird.

## Swift-Projekte

Swift-Projekte koennen ueber `SWIFT_PROJECTS_DIR` nach `/swift-projects`
gemountet werden. Das Image enthaelt die native Swift-Toolchain fuer Ubuntu
24.04, einschliesslich SwiftPM und SourceKit-LSP. Fuer VS Code wird die
Extension `swiftlang.swift-vscode` empfohlen; sie arbeitet besonders gut mit
SwiftPM-Projekten, die eine `Package.swift` im Projektwurzelverzeichnis
enthalten.

## Spec Kit

Spec Kit ist per `uv tool install specify-cli --from
git+https://github.com/github/spec-kit.git@v0.8.3` installiert und danach
schmal gepatcht, damit Initialisierung auf Host-Bind-Mounts stabiler laeuft.

Unter `/rider-projects` bevorzugt:

```bash
specify init . --integration opencode --force
```

Falls nach dem Skripttyp gefragt wird, im Linux-Container `sh` auswaehlen.

## Secure-Development-Container-Hardening-Intake

Dieses Repository ist der passende Level-2-Ort fuer einen spaeteren
Spec-Kit-Lauf zum sicheren Softwareentwicklungscontainer. Der Intake
`Lastenheft_Secure-Development-Container-Hardening.md` beschreibt die
Pruefpunkte fuer Podman/Docker-Runtime, digest-gepinnte Basisimages,
SBOM/VEX/SLSA, Container-Scanning, Signatur- oder Attestation-Entscheidung,
Secrets, Host-Mounts, Agenten-Daten, Modell-/Tool-Inventar und
C3A/C5-/Regulatory-`N/A`-Begruendungen.

Das Lastenheft ist nur Vorbereitung. Es baut kein Image, startet keinen
Container und migriert keine Projekte. Die aktive Reihenfolge fuer spaetere
Spec-Kit-Laeufe steht in `Lastenheft_Abarbeitungsreihenfolge.md`.

*This repository is the right Level-2 place for a later Spec Kit run about a
secure software development container. The intake
`Lastenheft_Secure-Development-Container-Hardening.md` covers Podman/Docker
runtime, digest-pinned base images, SBOM/VEX/SLSA, container scanning,
signature or attestation decisions, secrets, host mounts, agent data,
model/tool inventory, and C3A/C5/regulatory `N/A` rationales. It is preparation
only; it does not build an image, start a container, or migrate projects.*

## SBOM

Vor Weitergabe eines neu gebauten Images eine CycloneDX-SBOM erzeugen:

```bash
scripts/build-and-sbom.sh --skip-build
```

PowerShell:

```powershell
.\scripts\build-and-sbom.ps1 -SkipBuild
```

Die Skripte nutzen eine lokal installierte `syft`, wenn vorhanden. Andernfalls
wird das Syft-Containerimage mit Podman ausgefuehrt. Generierte
`sboms/*.cdx.json` sind Build-Artefakte und werden nicht committet.

## Validierung vor Commit

Mindestens:

```bash
podman-compose config
git diff --check
```

`podman compose config` kann als zusaetzliche lokale Plausibilitaetspruefung
laufen, wenn die Podman-Machine beziehungsweise der Podman-Socket funktioniert.
Ein lokaler Socket- oder Machine-Fehler ist kein Repo-Fehler, solange
`podman-compose config` erfolgreich ist.

Bei Dockerfile-Aenderungen:

```bash
podman compose build --pull
```

Bei Toolchain-Aenderungen zusaetzlich die Toolchecks aus diesem Dokument
ausfuehren. Wenn eine Plattform, Podman-Machine oder Netzwerkzugriff nicht
verfuegbar ist, die ausgelassene Pruefung mit Grund im Pull Request oder im
Session-Log dokumentieren.

## Troubleshooting

Podman-Machine auf macOS oder Windows pruefen:

```bash
podman machine list
podman machine start
podman info
```

Container neu starten:

```bash
podman compose up -d --force-recreate
podman compose exec ade bash
```

Build-Volume fuer .NET zuruecksetzen, wenn Besitzrechte im Volume defekt sind:

```bash
bash scripts/compose-down-with-audit.sh --podman
podman volume rm absdd-image-sandbox_dotnet_build
podman compose up -d
```

OpenCode sowie die vier Required-Agenten verwenden getrennte Podman-Volumes:
`opencode_data`, `codex_data`, `claude_data`, `gemini_data` und
`copilot_data`. `podman compose down -v` entfernt diese Daten einschliesslich
lokaler Anmeldezustaende. Vorher immer den Audit-Wrapper verwenden.

## English Quick Start

1. Install Podman and Compose support.
2. Create the local env file:

```bash
cp opencode.env.example opencode.env
chmod 600 opencode.env
```

3. Build and start:

```bash
podman-compose config
podman compose build --pull
podman compose up -d
podman compose exec ade bash
```

4. The image includes a pinned, read-only shallow Git reference at
   `~/home-baseline-tmp`. Its release, commit, source, and MIT license are
   recorded in `home-baseline.lock.json`; no baseline script runs
   automatically. To make changes, optionally replace it with your personal
   `home-baseline` repository. First fork the reference provided by your
   institution into your personal namespace, then clone it persistently on the
   host. Only the direct GitHub profile uses
   <https://github.com/hindermath/home-baseline>. Follow the
   `START-HERE-FUER-LERNENDE.md` supplied by your institution; the public
   provenance is available
   [on GitHub](https://github.com/hindermath/home-baseline/blob/main/docs/learning-units/START-HERE-FUER-LERNENDE.md).

```bash
HOME_BASELINE_DIR=/path/to/home-baseline-tmp
podman compose -f compose.yml -f compose.home-baseline.yml up -d
podman compose exec ade sh -lc 'cd ~/home-baseline-tmp && git status --short --branch'
```

5. Stop with audit export:

```bash
bash scripts/compose-down-with-audit.sh --podman
```

OpenCode is installed without a preconfigured API key or preselected model.
The built-in provider picker remains available; add local provider settings
only in local, untracked configuration when needed.

Codex, Claude Code, Gemini CLI, and GitHub Copilot CLI are installed as the
four required agents. Their presence does not imply account, provider, legal,
or organizational approval.
