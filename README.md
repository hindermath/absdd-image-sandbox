# Opencode Podman-Umgebung / Opencode Podman Environment

Dieses Repository stellt eine Podman-basierte Container-Umgebung fuer
Opencode, .NET, C#, Java, Go, Rust, Python, Codex CLI und Spec Kit bereit.
Es ist eine Sandbox- und Lernumgebung, keine Anwendung.

The repository provides a Podman-based container environment for Opencode,
.NET, C#, Java, Go, Rust, Python, Codex CLI, and Spec Kit. It is a sandbox and
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
  und installiert Java JDK 21, Maven, Go, Rust, Python, Node.js, Opencode,
  Codex CLI, `uv`, Spec Kit und Hilfswerkzeuge.
- `compose.yml`: definiert den Service `ade`, die Podman-Volumes, die
  Host-Mounts und die Portfreigabe `127.0.0.1:5100-5199`.
- `compose.home-baseline.yml`: optionale Compose-Erweiterung fuer ein eigenes
  `home-baseline`-Template-Repo im Container.
- `opencode.jsonc`: setzt OpenCode-Sicherheitsregeln, aber keinen Provider.
- `opencode.env.example`: neutrale Vorlage fuer lokale Provider-Secrets,
  falls Nutzer eigene OpenCode-Provider konfigurieren.
- `codex/`: systemweite Codex-Defaults und Anforderungen.
- `dotnet/ContainerBuild.props`: read-only Build-Konfiguration, die .NET-
  Artefakte in das Podman-Volume `/dotnet-build` umleitet.
- `scripts/compose-down-with-audit.*`: exportiert Audit-Metadaten vor dem
  Stoppen der Umgebung.
- `scripts/build-and-sbom.*`: erzeugt eine CycloneDX-SBOM fuer das gebaute
  Image.
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

## Lokale Konfiguration

Kopiere die Beispielumgebungsdatei, damit `compose.yml` eine vorhandene
`opencode.env` findet:

```bash
cp opencode.env.example opencode.env
chmod 600 opencode.env
```

Dieses Image konfiguriert keinen OpenCode-Modellanbieter. Wenn eine lokale
OpenCode-Konfiguration eigene Provider nutzt, koennen die dafuer noetigen
Secret-Variablen in `opencode.env` eingetragen werden. Secrets nie committen
und nie in Logs ausgeben.

Optionale Host-Mounts werden ueber `.env` oder die Shell gesetzt:

```bash
RIDER_PROJECTS_DIR=/pfad/zu/RiderProjects
JAVA_PROJECTS_DIR=/pfad/zu/java-projects
GO_PROJECTS_DIR=/pfad/zu/go-projects
RUST_PROJECTS_DIR=/pfad/zu/rust-projects
PYTHON_PROJECTS_DIR=/pfad/zu/python-projects
AUDIT_DIR=./audit-logs
```

Nicht gesetzte Variablen fallen auf lokale Repository-Verzeichnisse zurueck.

## Optional: Home-Baseline einbinden

`home-baseline` wird nicht in das Public Image geklont. Nutzerinnen und
Nutzer erstellen zuerst ein eigenes Repository aus einem `home-baseline`-
Template ueber die Template-Funktion ihres Git-Hostings und klonen dieses Repo
lokal. Kurs- oder Projektunterlagen koennen eine konkrete Template-Quelle
nennen; die Sandbox selbst verlangt keinen bestimmten GitHub-Account.

Der lokale Checkout kann danach optional in die Sandbox gemountet werden:

```bash
HOME_BASELINE_DIR=/pfad/zu/home-baseline-tmp
podman-compose -f compose.yml -f compose.home-baseline.yml config
podman compose -f compose.yml -f compose.home-baseline.yml up -d
podman compose exec ade sh -lc 'cd ~/home-baseline-tmp && git status --short --branch'
```

Im Container liegt der Checkout unter `/home/adedev/home-baseline-tmp`.
Das entspricht der Arbeitsort-Guidance von `home-baseline`, ohne einen
privaten Hostpfad oder einen bestimmten GitHub-Account in das Image zu
verdrahten. `sync-home.sh` wird nicht automatisch ausgefuehrt; falls ein
Nutzer die Home-Baseline in seinem Container-Home synchronisieren will, muss
das bewusst manuell geschehen.

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
podman compose exec ade sh -lc 'opencode --version; codex --version'
podman compose exec ade sh -lc 'specify version; specify check'
```

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
verfuegbar ist, die ausgelassene Pruefung mit Grund im Merge Request oder im
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

OpenCode- und Codex-Zustand liegen in den Podman-Volumes `opencode_data` und
`codex_data`. `podman compose down -v` entfernt diese Daten.

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

4. Optionally mount your own repository created from a `home-baseline`
   template:

```bash
HOME_BASELINE_DIR=/path/to/home-baseline-tmp
podman compose -f compose.yml -f compose.home-baseline.yml up -d
podman compose exec ade sh -lc 'cd ~/home-baseline-tmp && git status --short --branch'
```

5. Stop with audit export:

```bash
bash scripts/compose-down-with-audit.sh --podman
```

OpenCode is installed without a preconfigured model provider. Add local
provider settings only in local, untracked configuration when needed.
