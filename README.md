# Opencode Docker-Umgebung

## Inhaltsverzeichnis

- [Deutsch](#deutsch)
  - [Zielgruppe und Zweck](#zielgruppe-und-zweck)
  - [Grundidee](#grundidee)
  - [Projektstruktur](#projektstruktur)
  - [Docker unter Ubuntu oder WSL2 installieren](#docker-unter-ubuntu-oder-wsl2-installieren)
  - [Docker-Berechtigungen pruefen](#docker-berechtigungen-pruefen)
  - [API-Key einrichten](#api-key-einrichten)
  - [Container bauen und starten](#container-bauen-und-starten)
  - [Rider-Projekte aus Windows einbinden](#rider-projekte-aus-windows-einbinden)
  - [.NET und C# im Container nutzen](#net-und-c-im-container-nutzen)
  - [Spec Kit verwenden](#spec-kit-verwenden)
  - [Beispiel: ConsoleApp2 mit Opencode und Spec Kit](#beispiel-consoleapp2-mit-opencode-und-spec-kit)
  - [Pflichtablauf fuer ein SDD-Feature](#pflichtablauf-fuer-ein-sdd-feature)
  - [Opencode verwenden](#opencode-verwenden)
  - [Konfiguration](#konfiguration)
  - [Aufraeumen](#aufraeumen)
  - [Haeufige Probleme](#haeufige-probleme)
  - [Kompakter Testablauf](#kompakter-testablauf)
- [English](#english)
  - [Target group and purpose](#target-group-and-purpose)
  - [Basic idea](#basic-idea)
  - [Project structure](#project-structure)
  - [Install Docker on Ubuntu or WSL2](#install-docker-on-ubuntu-or-wsl2)
  - [Check Docker permissions](#check-docker-permissions)
  - [Set up the API key](#set-up-the-api-key)
  - [Build and start the container](#build-and-start-the-container)
  - [Mount Rider projects from Windows](#mount-rider-projects-from-windows)
  - [Use .NET and C# inside the container](#use-net-and-c-inside-the-container)
  - [Use Spec Kit](#use-spec-kit)
  - [Example: ConsoleApp2 with Opencode and Spec Kit](#example-consoleapp2-with-opencode-and-spec-kit)
  - [Required flow for an SDD feature](#required-flow-for-an-sdd-feature)
  - [Use Opencode](#use-opencode)
  - [Configuration](#configuration)
  - [Clean up](#clean-up)
  - [Common problems](#common-problems)
  - [Compact test procedure](#compact-test-procedure)

## Deutsch

### Zielgruppe und Zweck

Diese Anleitung richtet sich an Auszubildende der Fachinformatik ab dem 1. Lehrjahr. Sie erklaert nicht nur die Befehle, sondern auch kurz, warum sie gebraucht werden.

Dieses Repository stellt eine Docker-Umgebung fuer Opencode, .NET und C# bereit. Die Umgebung ist fuer Entwicklung unter WSL2 gedacht. Projekte koennen weiter unter Windows mit JetBrains Rider bearbeitet werden.

### Grundidee

Docker erstellt aus dem `Dockerfile` ein Image. Aus diesem Image startet Docker Compose einen Container. Der Container enthaelt das aktuelle Microsoft .NET SDK, Node.js, npm und Opencode.

Der Container bleibt im Hintergrund aktiv. Danach kann eine Shell im Container geoeffnet werden. Dort koennen Befehle wie `dotnet`, `opencode` oder `ls` ausgefuehrt werden.

### Projektstruktur

- `Dockerfile`: beschreibt das Container-Image. Es nutzt `mcr.microsoft.com/dotnet/sdk:latest`.
- `compose.yml`: beschreibt den Service `opencode`, Volumes und Build-Regeln.
- `opencode.jsonc`: enthaelt Provider, Modelle und Agenten fuer Opencode. JSONC erlaubt Kommentare und ist deshalb fuer Lernzwecke besser lesbar.
- `opencode.env.example`: Vorlage fuer die lokale Datei `opencode.env`.
- `workspace/`: lokales Arbeitsverzeichnis, im Container unter `/workspace`.
- `/mnt/c/Users/thinder/RiderProjects`: Windows-Projekte, im Container unter `/rider-projects`.
- `dotnet/ContainerBuild.props`: leitet .NET-Build-Artefakte fuer Rider-Projekte in das Container-Volume `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: filtert eine bekannte .NET-Workload-Verifikationsmeldung aus der Ausgabe.
- `spec-kit/patch-specify-cli.py`: passt Spec Kit fuer Windows-/WSL-Bind-Mounts an.
- `AGENTS.md`: Regeln fuer KI-Agenten wie Opencode oder Codex.

### Docker unter Ubuntu oder WSL2 installieren

Zuerst die Paketlisten aktualisieren:

```bash
sudo apt update
```

Docker Engine und Docker Compose installieren:

```bash
sudo apt install -y docker.io docker-compose-v2
```

Docker-Dienst starten:

```bash
sudo systemctl enable --now docker
```

Unter WSL2 funktioniert `systemctl` nur, wenn systemd aktiv ist. Falls der Befehl scheitert, kann Docker auch ueber Docker Desktop fuer Windows bereitgestellt werden. In diesem Fall muss die WSL-Integration fuer die verwendete Distribution aktiviert sein.

Installation pruefen:

```bash
docker --version
docker compose version
docker info
```

Die Compose-Datei kann ohne Secret-Ausgabe geprueft werden:

```bash
docker compose config --no-interpolate
```

### Docker-Berechtigungen pruefen

Wenn `docker info` mit `permission denied` scheitert, darf der aktuelle Benutzer noch nicht auf Docker zugreifen.

Schneller Test mit `sudo`:

```bash
sudo docker info
```

Dauerhafte Freigabe fuer den aktuellen Benutzer:

```bash
sudo usermod -aG docker "$USER"
```

Danach komplett neu anmelden. Erst danach wird die neue Gruppenzugehoerigkeit aktiv. Pruefen:

```bash
id
docker info
```

### API-Key einrichten

Vor dem Start muss eine lokale Datei `opencode.env` angelegt werden:

```bash
cp opencode.env.example opencode.env
```

Danach den echten Key eintragen:

```text
GWDG_API_KEY=dein_echter_key
```

Alternativ kann der vorhandene Key aus `~/.local/share/opencode/auth.json` uebernommen werden. In diesem Setup wird `chat-ai.key` als `GWDG_API_KEY` gespeichert.

Wichtig: `opencode.env` enthaelt ein Secret. Die Datei ist in `.gitignore` ausgeschlossen und darf nicht nach GitLab gepusht werden.

```bash
chmod 600 opencode.env
```

### Container bauen und starten

In das Repository wechseln:

```bash
cd /home/thinder/ade-dev-sandbox
```

Image bauen und dabei nach dem neuesten .NET-Basisimage suchen:

```bash
docker compose build --pull
```

Container starten:

```bash
docker compose up -d
```

Status anzeigen:

```bash
docker compose ps
```

Beim ersten Build werden das .NET-SDK-Basisimage und npm-Pakete geladen. Das kann einige Minuten dauern.

### Rider-Projekte aus Windows einbinden

Die Windows-Projekte liegen unter:

```text
/mnt/c/Users/thinder/RiderProjects
```

Sie werden im Container hier eingebunden:

```text
/rider-projects
```

Im Container kann dorthin gewechselt werden:

```bash
cd /rider-projects
ls
```

Aenderungen im Container wirken direkt auf die Windows-Dateien. Rider unter Windows sieht dieselben Dateien. Builds auf `/mnt/c` koennen langsamer sein als Builds im Linux-Dateisystem.

Damit .NET auf Windows-Dateien keine Probleme mit `bin`, `obj`, AppHost-Dateien oder Dateizeitstempeln bekommt, wird eine MSBuild-Konfiguration in den Container eingebunden:

```text
dotnet/ContainerBuild.props -> /dotnet-config/ContainerBuild.props
```

Compose setzt dazu die Umgebungsvariable `DirectoryBuildPropsPath`. Dadurch wird die Konfiguration sehr frueh im MSBuild-Ablauf geladen. Repo-eigene `Directory.Build.props`-Dateien werden von `ContainerBuild.props` weiter importiert, damit projektspezifische Einstellungen erhalten bleiben.

Die Build-Artefakte liegen nicht unter `/rider-projects`, sondern im Linux-Volume `/dotnet-build`. Das verhindert typische Fehler wie `Access to the path ... obj ... is denied` oder Fehler beim Erstellen von `apphost`.

### .NET und C# im Container nutzen

Shell im Container oeffnen:

```bash
docker compose exec opencode bash
```

.NET-Version pruefen:

```bash
dotnet --info
```

Beispiel fuer ein neues Konsolenprojekt:

```bash
cd /rider-projects
dotnet new console -n DemoApp
cd DemoApp
dotnet run
```

Wenn ein Projekt bereits fehlerhafte `bin`- oder `obj`-Ordner auf dem Windows-Mount hat, koennen diese in Rider oder im Terminal geloescht werden. Danach erneut im Container bauen.

### Spec Kit verwenden

Spec Kit ist im Container als `specify` installiert. Die Installation erfolgt im Dockerfile mit der offiziellen GitHub-Quelle und ist auf Version `v0.8.3` gepinnt:

```dockerfile
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.3
```

Version und Umgebung pruefen:

```bash
specify version
specify check
```

Ein vorhandenes Projekt kann vorbereitet werden, nachdem in sein Verzeichnis gewechselt wurde:

```bash
cd /rider-projects/TinyPl0
specify init . --integration opencode --force
```

Falls eine Integration nicht verfuegbar ist, zuerst die unterstuetzten Optionen pruefen:

```bash
specify init --help
```

Wenn Spec Kit nach dem Script-Typ fragt, fuer diesen Linux-Container `sh` auswaehlen.

Spec Kit weist darauf hin, dass Agentenordner private Daten enthalten koennen. Fuer Projekte unter `/rider-projects` sollte deshalb im jeweiligen Anwendungsrepo geprueft werden, ob `.opencode/` oder sensible Teile davon in die Projekt-`.gitignore` gehoeren.

Spec Kit erzeugt Projektdateien fuer spec-driven development. Diese Dateien gehoeren normalerweise in das jeweilige Anwendungsrepo unter `/rider-projects`, nicht in dieses Docker-Setup-Repo.

### Beispiel: ConsoleApp2 mit Opencode und Spec Kit

Dieses Beispiel zeigt den kompletten Einstieg fuer eine neue Konsolenanwendung. Es wird im Container ausgefuehrt.

```bash
cd /rider-projects
dotnet new console -n ConsoleApp2
cd ConsoleApp2
dotnet run
```

Danach Opencode einmal im Projekt initialisieren. Dadurch kann Opencode projektspezifische Regeln erkennen oder anlegen:

```bash
opencode /init
```

Danach Spec Kit fuer Opencode einrichten:

```bash
specify init . --integration opencode --force
```

Wenn Spec Kit nach dem Script-Typ fragt, `sh` auswaehlen. Nach erfolgreicher Initialisierung stehen in Opencode die Slash-Commands `/speckit.*` zur Verfuegung.

Wenn das Projekt mit Git verwaltet wird, pruefen:

```bash
git status --short
```

Danach entscheiden, ob `.opencode/` vollstaendig versioniert werden soll oder ob sensible Teile in die Projekt-`.gitignore` gehoeren.

### Pflichtablauf fuer ein SDD-Feature

SDD bedeutet spec-driven development. Ein Feature wird zuerst beschrieben, dann geplant, dann in Aufgaben zerlegt und erst danach implementiert. Fuer die Ausbildung werden auch die Qualitaetsschritte immer ausgefuehrt.

Empfohlene Reihenfolge in Opencode:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.checklist
/speckit.tasks
/speckit.analyze
/speckit.implement
```

Die Schritte haben diese Aufgabe:

- `/speckit.constitution`: Projektprinzipien und technische Leitplanken festlegen.
- `/speckit.specify`: Feature fachlich beschreiben, ohne direkt Code zu planen.
- `/speckit.clarify`: offene Fragen klaeren, bevor technische Planung beginnt.
- `/speckit.plan`: technische Umsetzung planen.
- `/speckit.checklist`: Anforderungen auf Vollstaendigkeit und Klarheit pruefen.
- `/speckit.tasks`: konkrete umsetzbare Aufgaben erzeugen.
- `/speckit.analyze`: Konsistenz zwischen Spezifikation, Plan und Aufgaben pruefen.
- `/speckit.implement`: Aufgaben umsetzen.

Nach der Implementierung immer ausfuehren:

```bash
dotnet test
dotnet run
```

Wenn das Projekt keine Tests enthaelt, mindestens `dotnet build` ausfuehren und in der Dokumentation notieren, warum keine Tests vorhanden sind.

### Opencode verwenden

Opencode im Container starten:

```bash
opencode
```

Der Container startet Opencode nicht automatisch. Das ist Absicht. So kann zuerst entschieden werden, in welchem Projektverzeichnis gearbeitet wird.

### Konfiguration

`opencode.jsonc` nutzt den Provider `chat-ai` mit dieser Basis-URL:

```text
https://chat-ai.academiccloud.de/v1
```

Der API-Key wird aus `GWDG_API_KEY` gelesen. Das Standardmodell ist:

```text
chat-ai/glm-4.7
```

Opencode wird beim Image-Build mit der neuesten npm-Version installiert:

```dockerfile
RUN npm i -g opencode-ai@latest
```

Spec Kit wird beim Image-Build mit `uv` installiert. Dafuer enthaelt das Image auch `git`, `curl` und `ca-certificates`.

Nach der Installation wird Spec Kit im Container gepatcht. Der Patch verhindert, dass Python-Kopiervorgaenge Dateirechte oder Zeitstempel auf dem Windows-Mount uebernehmen wollen. Das ist wichtig, weil `/mnt/c` solche Metadatenoperationen mit `Operation not permitted` ablehnen kann.

Die .NET-Workload-Hinweismeldung wird im Container deaktiviert:

```text
DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=true
MSBuildEnableWorkloadResolver=false
```

Die erste Variable betrifft allgemeine Update-Benachrichtigungen. Die zweite Variable deaktiviert den MSBuild-Workload-Resolver. Das ist fuer normale Konsolen-, Library-, Test- und Web-Projekte sinnvoll, weil dort keine optionalen SDK-Workloads wie MAUI gebraucht werden.

Gegen die Meldung `An issue was encountered verifying workloads` wird beim Image-Build zusaetzlich der Manifest-Modus gesetzt:

```dockerfile
RUN dotnet workload config --update-mode manifests \
    && dotnet workload update
```

Dieser Befehl laeuft beim Image-Build als `root`, weil `dotnet workload config` erhoehte Rechte braucht. Normale .NET-Projekte koennen weiter gebaut und gestartet werden. Wenn ein Projekt echte Workloads wie MAUI oder spezielle WebAssembly-Tools braucht, muessen diese gezielt im Dockerfile ergaenzt und `MSBuildEnableWorkloadResolver` wieder aktiviert werden.

Zusaetzlich wird im Image ein schmaler Wrapper unter `/usr/local/bin/dotnet` installiert. Er ruft intern `/usr/bin/dotnet` auf und filtert nur diese bekannte Zeile aus der Fehlerausgabe:

```text
An issue was encountered verifying workloads. For more information, run "dotnet workload update".
```

Andere Warnungen, Fehler und der Exit-Code von `dotnet` bleiben erhalten.

### Aufraeumen

Container stoppen, Daten behalten:

```bash
docker compose down
```

Container stoppen und persistente Opencode-Daten loeschen:

```bash
docker compose down -v
```

### Haeufige Probleme

Wenn `docker compose` nicht gefunden wird, fehlt meist `docker-compose-v2`:

```bash
sudo apt install -y docker-compose-v2
```

Wenn Docker keine Berechtigung hat, entweder `sudo docker ...` verwenden oder den Benutzer zur Gruppe `docker` hinzufuegen.

Wenn der API-Key nicht funktioniert, `opencode.env` pruefen. Den Key nicht im Terminalverlauf, in Screenshots oder in Git-Ausgaben zeigen.

Wenn .NET unter `/rider-projects` einen Fehler zu `obj`, `bin`, `apphost` oder `Access denied` meldet, den Container neu bauen und starten:

```bash
docker compose build --pull
docker compose up -d
```

Danach im Container pruefen, ob die allgemeine MSBuild-Konfiguration und das Build-Volume vorhanden sind:

```bash
test "$DirectoryBuildPropsPath" = "/dotnet-config/ContainerBuild.props"
ls /dotnet-config/ContainerBuild.props
ls /dotnet-build
```

Wenn eine Warnung `MSB3539` zu `BaseIntermediateOutputPath` erscheint, laeuft wahrscheinlich noch ein alter Container. Dann den Container neu erstellen:

```bash
docker compose up -d --force-recreate
```

Wenn danach ein Fehler wie `Duplicate TargetFrameworkAttribute` erscheint, liegen meist alte `obj`-Dateien im Windows-Projektordner. Diese Ordner einmal loeschen und danach erneut bauen:

```bash
find /rider-projects/ConsoleApp1 -type d \( -name bin -o -name obj \) -prune -print
```

Wenn die Ausgabe nur erwartete Build-Ordner zeigt, koennen sie geloescht werden:

```bash
find /rider-projects/ConsoleApp1 -type d \( -name bin -o -name obj \) -prune -exec rm -rf {} +
```

Wenn ein Fehler wie `Root element is missing` fuer `/rider-projects/Directory.Build.props` erscheint, liegt im Windows-Projektroot eine alte oder leere MSBuild-Datei. Diese Datei darf dort nicht mehr liegen. Pruefen:

```bash
ls -l /rider-projects/Directory.Build.props
```

Wenn die Datei leer oder unerwuenscht ist, loeschen:

```bash
rm /rider-projects/Directory.Build.props
```

### Kompakter Testablauf

Dieser Ablauf prueft das Setup in einer sinnvollen Reihenfolge. Er eignet sich gut nach einer Neuinstallation oder nach Aenderungen an `Dockerfile`, `compose.yml` oder `opencode.jsonc`.

Auf dem Host ausfuehren:

```bash
cd /home/thinder/ade-dev-sandbox
docker compose config --no-interpolate
docker compose build --pull
docker compose up -d
docker compose ps
docker compose exec opencode bash
```

Danach im Container pruefen:

```bash
dotnet --info
node --version
npm --version
opencode --version
specify version
ls /workspace
ls /rider-projects
```

## English

### Target group and purpose

This guide is written for first-year IT specialist apprentices and later. It explains the commands and also why they are needed.

This repository provides a Docker environment for Opencode, .NET, and C#. It is designed for development with WSL2. Projects can still be edited on Windows with JetBrains Rider.

### Basic idea

Docker builds an image from the `Dockerfile`. Docker Compose starts a container from that image. The container includes the current Microsoft .NET SDK, Node.js, npm, and Opencode.

The container stays active in the background. You can then open a shell inside it and run commands such as `dotnet`, `opencode`, or `ls`.

### Project structure

- `Dockerfile`: describes the container image. It uses `mcr.microsoft.com/dotnet/sdk:latest`.
- `compose.yml`: describes the `opencode` service, volumes, and build rules.
- `opencode.jsonc`: contains provider, model, and agent settings for Opencode. JSONC allows comments and is easier to read for learning.
- `opencode.env.example`: template for the local `opencode.env` file.
- `workspace/`: local working directory, mounted as `/workspace`.
- `/mnt/c/Users/thinder/RiderProjects`: Windows projects, mounted as `/rider-projects`.
- `dotnet/ContainerBuild.props`: redirects .NET build artifacts for Rider projects to the container volume `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: filters a known .NET workload verification message from command output.
- `spec-kit/patch-specify-cli.py`: adapts Spec Kit for Windows/WSL bind mounts.
- `AGENTS.md`: rules for AI agents such as Opencode or Codex.

### Install Docker on Ubuntu or WSL2

First update the package lists:

```bash
sudo apt update
```

Install Docker Engine and Docker Compose:

```bash
sudo apt install -y docker.io docker-compose-v2
```

Start the Docker service:

```bash
sudo systemctl enable --now docker
```

On WSL2, `systemctl` only works if systemd is enabled. If the command fails, Docker can also be provided by Docker Desktop for Windows. In that case, enable WSL integration for the used distribution.

Check the installation:

```bash
docker --version
docker compose version
docker info
```

Check the Compose file without printing secret values:

```bash
docker compose config --no-interpolate
```

### Check Docker permissions

If `docker info` fails with `permission denied`, the current user is not allowed to access Docker yet.

Quick test with `sudo`:

```bash
sudo docker info
```

Permanent access for the current user:

```bash
sudo usermod -aG docker "$USER"
```

Log out completely and log in again. Only then is the new group membership active. Check it:

```bash
id
docker info
```

### Set up the API key

Before starting the container, create a local `opencode.env` file:

```bash
cp opencode.env.example opencode.env
```

Then enter the real key:

```text
GWDG_API_KEY=your_real_key
```

Alternatively, copy the existing key from `~/.local/share/opencode/auth.json`. In this setup, `chat-ai.key` is stored as `GWDG_API_KEY`.

Important: `opencode.env` contains a secret. The file is excluded in `.gitignore` and must not be pushed to GitLab.

```bash
chmod 600 opencode.env
```

### Build and start the container

Change into the repository:

```bash
cd /home/thinder/ade-dev-sandbox
```

Build the image and check for the newest .NET base image:

```bash
docker compose build --pull
```

Start the container:

```bash
docker compose up -d
```

Show the status:

```bash
docker compose ps
```

The first build downloads the .NET SDK base image and npm packages. This can take several minutes.

### Mount Rider projects from Windows

The Windows projects are stored here:

```text
/mnt/c/Users/thinder/RiderProjects
```

They are mounted inside the container here:

```text
/rider-projects
```

Inside the container, change to that directory:

```bash
cd /rider-projects
ls
```

Changes inside the container are written directly to the Windows files. Rider on Windows sees the same files. Builds on `/mnt/c` can be slower than builds inside the Linux file system.

To avoid .NET problems with `bin`, `obj`, AppHost files, or file timestamps on Windows files, an MSBuild configuration file is mounted into the container:

```text
dotnet/ContainerBuild.props -> /dotnet-config/ContainerBuild.props
```

Compose sets the `DirectoryBuildPropsPath` environment variable for this. The configuration is loaded very early in the MSBuild process. Repository-specific `Directory.Build.props` files are still imported by `ContainerBuild.props`, so project settings remain active.

Build artifacts are written to the Linux volume `/dotnet-build` instead of `/rider-projects`. This prevents common errors such as `Access to the path ... obj ... is denied` or errors while creating `apphost`.

### Use .NET and C# inside the container

Open a shell inside the container:

```bash
docker compose exec opencode bash
```

Check the .NET version:

```bash
dotnet --info
```

Example for a new console project:

```bash
cd /rider-projects
dotnet new console -n DemoApp
cd DemoApp
dotnet run
```

If a project already has broken `bin` or `obj` folders on the Windows mount, delete them in Rider or in the terminal. Then build again inside the container.

### Use Spec Kit

Spec Kit is installed in the container as `specify`. The Dockerfile installs it from the official GitHub source and pins version `v0.8.3`:

```dockerfile
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.3
```

Check the version and environment:

```bash
specify version
specify check
```

An existing project can be prepared after changing into its directory:

```bash
cd /rider-projects/TinyPl0
specify init . --integration opencode --force
```

If an integration is not available, check the supported options first:

```bash
specify init --help
```

If Spec Kit asks for the script type, choose `sh` for this Linux container.

Spec Kit warns that agent folders can contain private data. For projects under `/rider-projects`, check whether `.opencode/` or sensitive parts of it should be added to that application repository's `.gitignore`.

Spec Kit creates project files for spec-driven development. These files normally belong in the application repository under `/rider-projects`, not in this Docker setup repository.

### Example: ConsoleApp2 with Opencode and Spec Kit

This example shows the complete start for a new console application. Run it inside the container.

```bash
cd /rider-projects
dotnet new console -n ConsoleApp2
cd ConsoleApp2
dotnet run
```

Then initialize Opencode once in the project. This lets Opencode detect or create project-specific rules:

```bash
opencode /init
```

Then set up Spec Kit for Opencode:

```bash
specify init . --integration opencode --force
```

If Spec Kit asks for the script type, choose `sh`. After successful initialization, the `/speckit.*` slash commands are available in Opencode.

If the project is managed with Git, check:

```bash
git status --short
```

Then decide whether `.opencode/` should be fully versioned or whether sensitive parts belong in the project `.gitignore`.

### Required flow for an SDD feature

SDD means spec-driven development. A feature is described first, then planned, then split into tasks, and only then implemented. For training, the quality steps are always required.

Recommended order in Opencode:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.checklist
/speckit.tasks
/speckit.analyze
/speckit.implement
```

The steps have these roles:

- `/speckit.constitution`: define project principles and technical guardrails.
- `/speckit.specify`: describe the feature from a user and domain view, without planning code yet.
- `/speckit.clarify`: answer open questions before technical planning starts.
- `/speckit.plan`: plan the technical implementation.
- `/speckit.checklist`: check requirements for completeness and clarity.
- `/speckit.tasks`: create concrete actionable tasks.
- `/speckit.analyze`: check consistency between specification, plan, and tasks.
- `/speckit.implement`: implement the tasks.

After implementation, always run:

```bash
dotnet test
dotnet run
```

If the project has no tests, run at least `dotnet build` and document why no tests exist.

### Use Opencode

Start Opencode inside the container:

```bash
opencode
```

The container does not start Opencode automatically. This is intentional. It lets you choose the project directory first.

### Configuration

`opencode.jsonc` uses the `chat-ai` provider with this base URL:

```text
https://chat-ai.academiccloud.de/v1
```

The API key is read from `GWDG_API_KEY`. The default model is:

```text
chat-ai/glm-4.7
```

Opencode is installed during the image build with the newest npm version:

```dockerfile
RUN npm i -g opencode-ai@latest
```

Spec Kit is installed during the image build with `uv`. For that reason, the image also includes `git`, `curl`, and `ca-certificates`.

After installation, Spec Kit is patched inside the container. The patch prevents Python copy operations from preserving file permissions or timestamps on the Windows mount. This is important because `/mnt/c` can reject these metadata operations with `Operation not permitted`.

The .NET workload notification is disabled inside the container:

```text
DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=true
MSBuildEnableWorkloadResolver=false
```

The first variable affects general update notifications. The second variable disables the MSBuild workload resolver. This is useful for normal console, library, test, and web projects because they do not need optional SDK workloads such as MAUI.

To address the message `An issue was encountered verifying workloads`, the image build also sets manifest mode:

```dockerfile
RUN dotnet workload config --update-mode manifests \
    && dotnet workload update
```

This command runs as `root` during the image build because `dotnet workload config` needs elevated privileges. Normal .NET projects can still be built and started. If a project needs real workloads such as MAUI or special WebAssembly tools, add them explicitly in the Dockerfile and enable `MSBuildEnableWorkloadResolver` again.

The image also installs a small wrapper at `/usr/local/bin/dotnet`. It calls `/usr/bin/dotnet` internally and filters only this known line from error output:

```text
An issue was encountered verifying workloads. For more information, run "dotnet workload update".
```

Other warnings, errors, and the `dotnet` exit code are preserved.

### Clean up

Stop the container but keep data:

```bash
docker compose down
```

Stop the container and delete persistent Opencode data:

```bash
docker compose down -v
```

### Common problems

If `docker compose` is not found, `docker-compose-v2` is usually missing:

```bash
sudo apt install -y docker-compose-v2
```

If Docker has no permission, use `sudo docker ...` or add the user to the `docker` group.

If the API key does not work, check `opencode.env`. Do not show the key in terminal history, screenshots, or Git output.

If .NET reports an `obj`, `bin`, `apphost`, or `Access denied` error under `/rider-projects`, rebuild and start the container:

```bash
docker compose build --pull
docker compose up -d
```

Then check inside the container that the general MSBuild configuration and build volume exist:

```bash
test "$DirectoryBuildPropsPath" = "/dotnet-config/ContainerBuild.props"
ls /dotnet-config/ContainerBuild.props
ls /dotnet-build
```

If a warning `MSB3539` about `BaseIntermediateOutputPath` appears, an old container is probably still running. Recreate the container:

```bash
docker compose up -d --force-recreate
```

If an error like `Duplicate TargetFrameworkAttribute` appears after that, old `obj` files are usually still present in the Windows project folder. Delete these folders once and build again:

```bash
find /rider-projects/ConsoleApp1 -type d \( -name bin -o -name obj \) -prune -print
```

If the output only shows expected build folders, they can be deleted:

```bash
find /rider-projects/ConsoleApp1 -type d \( -name bin -o -name obj \) -prune -exec rm -rf {} +
```

If an error like `Root element is missing` appears for `/rider-projects/Directory.Build.props`, an old or empty MSBuild file exists in the Windows project root. This file must not stay there. Check it:

```bash
ls -l /rider-projects/Directory.Build.props
```

If the file is empty or unwanted, delete it:

```bash
rm /rider-projects/Directory.Build.props
```

### Compact test procedure

This procedure checks the setup in a useful order. It is a good choice after a fresh installation or after changes to `Dockerfile`, `compose.yml`, or `opencode.jsonc`.

Run this on the host:

```bash
cd /home/thinder/ade-dev-sandbox
docker compose config --no-interpolate
docker compose build --pull
docker compose up -d
docker compose ps
docker compose exec opencode bash
```

Then check this inside the container:

```bash
dotnet --info
node --version
npm --version
opencode --version
specify version
ls /workspace
ls /rider-projects
```
