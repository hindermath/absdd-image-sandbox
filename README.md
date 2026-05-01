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
- `opencode.json`: enthaelt Provider, Modelle und Agenten fuer Opencode.
- `opencode.env.example`: Vorlage fuer die lokale Datei `opencode.env`.
- `workspace/`: lokales Arbeitsverzeichnis, im Container unter `/workspace`.
- `/mnt/c/Users/thinder/RiderProjects`: Windows-Projekte, im Container unter `/rider-projects`.
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

### Opencode verwenden

Opencode im Container starten:

```bash
opencode
```

Der Container startet Opencode nicht automatisch. Das ist Absicht. So kann zuerst entschieden werden, in welchem Projektverzeichnis gearbeitet wird.

### Konfiguration

`opencode.json` nutzt den Provider `chat-ai` mit dieser Basis-URL:

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

### Kompakter Testablauf

Dieser Ablauf prueft das Setup in einer sinnvollen Reihenfolge. Er eignet sich gut nach einer Neuinstallation oder nach Aenderungen an `Dockerfile`, `compose.yml` oder `opencode.json`.

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
- `opencode.json`: contains provider, model, and agent settings for Opencode.
- `opencode.env.example`: template for the local `opencode.env` file.
- `workspace/`: local working directory, mounted as `/workspace`.
- `/mnt/c/Users/thinder/RiderProjects`: Windows projects, mounted as `/rider-projects`.
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

### Use Opencode

Start Opencode inside the container:

```bash
opencode
```

The container does not start Opencode automatically. This is intentional. It lets you choose the project directory first.

### Configuration

`opencode.json` uses the `chat-ai` provider with this base URL:

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

### Compact test procedure

This procedure checks the setup in a useful order. It is a good choice after a fresh installation or after changes to `Dockerfile`, `compose.yml`, or `opencode.json`.

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
ls /workspace
ls /rider-projects
```
