# Opencode Docker-Umgebung

## Inhaltsverzeichnis

- [Deutsch](#deutsch)
  - [Zweck](#zweck)
  - [Wichtige Dateien](#wichtige-dateien)
  - [Voraussetzungen](#voraussetzungen)
  - [API-Key einrichten](#api-key-einrichten)
  - [Container bauen und starten](#container-bauen-und-starten)
  - [Opencode verwenden](#opencode-verwenden)
  - [Konfiguration](#konfiguration)
  - [Opencode-Version](#opencode-version)
  - [Aufraeumen](#aufraeumen)
- [English](#english)
  - [Purpose](#purpose)
  - [Important files](#important-files)
  - [Requirements](#requirements)
  - [Set up the API key](#set-up-the-api-key)
  - [Build and start the container](#build-and-start-the-container)
  - [Use Opencode](#use-opencode)
  - [Configuration](#configuration)
  - [Opencode version](#opencode-version-1)
  - [Clean up](#clean-up)

## Deutsch

### Zweck

Dieses Repository stellt eine kleine Docker-Umgebung fuer Opencode bereit. Der Container startet nicht direkt Opencode, sondern bleibt laufen. Danach kann eine Shell im Container geoeffnet und Opencode manuell gestartet werden.

Der lokale Ordner `workspace` wird im Container als `/workspace` eingebunden. Dort kann mit Projektdaten gearbeitet werden.

### Wichtige Dateien

- `Dockerfile`: baut das Container-Image auf Basis des offiziellen Microsoft-.NET-SDK-Images `mcr.microsoft.com/dotnet/sdk:latest`.
- `compose.yml`: definiert den Docker-Compose-Service `opencode`.
- `opencode.json`: enthaelt die Opencode-Konfiguration fuer den Provider `chat-ai`.
- `opencode.env.example`: Beispiel fuer die benoetigte Umgebungsvariable `GWDG_API_KEY`.
- `workspace`: Arbeitsverzeichnis, das in den Container eingebunden wird.

### Voraussetzungen

Docker muss installiert sein. Docker Compose muss als modernes Docker-Plugin verfuegbar sein.

Pruefen:

```bash
docker --version
docker compose version
docker info
```

Die Compose-Datei kann ohne Secret-Ausgabe so geprueft werden:

```bash
docker compose config --no-interpolate
```

Wenn `docker compose` fehlt, kann auf Ubuntu 24.04 dieses Paket installiert werden:

```bash
sudo apt install docker-compose-v2
```

Wenn `docker info` wegen fehlender Rechte scheitert, gibt es zwei Wege:

```bash
sudo docker compose up -d
```

Oder den aktuellen Benutzer dauerhaft fuer Docker freigeben:

```bash
sudo usermod -aG docker "$USER"
```

Danach ist ein neues Login noetig. Erst danach sollte `docker info` ohne `sudo` funktionieren.

### API-Key einrichten

Vor dem Start muss eine lokale Datei `opencode.env` angelegt werden:

```bash
cp opencode.env.example opencode.env
```

Danach in `opencode.env` den echten API-Key setzen:

```text
GWDG_API_KEY=dein_echter_key
```

Alternativ kann der vorhandene Key aus der lokalen Opencode-Datei `~/.local/share/opencode/auth.json` uebernommen werden. In diesem Setup wird der Wert aus `chat-ai.key` als `GWDG_API_KEY` in `opencode.env` gespeichert.

Die Datei `opencode.env` wird nicht versioniert. Sie ist in `.gitignore` ausdruecklich ausgeschlossen und darf nicht ins GitLab-Repository gepusht werden. Da sie einen Secret-Wert enthaelt, sollte sie nur fuer den aktuellen Benutzer lesbar sein:

```bash
chmod 600 opencode.env
```

### Container bauen und starten

Aus dem Repository-Verzeichnis starten:

```bash
docker compose up -d
```

Beim ersten Start wird das Image gebaut. Das kann etwas dauern, weil Debian-Pakete installiert werden und Opencode ueber npm geladen wird.

Compose ist so konfiguriert, dass beim Build auch nach einem neueren Basisimage gesucht wird. Explizit kann das so ausgefuehrt werden:

```bash
docker compose build --pull
docker compose up -d
```

### Opencode verwenden

Shell im Container oeffnen:

```bash
docker compose exec opencode bash
```

Opencode starten:

```bash
opencode
```

### Konfiguration

Die Datei `opencode.json` nutzt den Provider `chat-ai` mit der Basis-URL:

```text
https://chat-ai.academiccloud.de/v1
```

Der API-Key wird aus der Umgebungsvariable `GWDG_API_KEY` gelesen. Das Standardmodell ist:

```text
chat-ai/glm-4.7
```

Zusaetzlich sind Agenten fuer Coding, Qwen-Coding und Brainstorming eingerichtet.

### Opencode-Version

Im `Dockerfile` wird Opencode mit diesem Befehl installiert:

```dockerfile
RUN npm i -g opencode-ai@latest
```

Dadurch wird beim Neubau des Images die aktuellste Version von `opencode-ai` aus npm installiert.

### Aufraeumen

Container stoppen, Daten aber behalten:

```bash
docker compose down
```

Container stoppen und persistente Opencode-Daten loeschen:

```bash
docker compose down -v
```

## English

### Purpose

This repository provides a small Docker environment for Opencode. The container does not start Opencode directly. It keeps running, so you can open a shell inside the container and start Opencode manually.

The local `workspace` folder is mounted into the container as `/workspace`. This is where project files can be used.

### Important files

- `Dockerfile`: builds the container image from the official Microsoft .NET SDK image `mcr.microsoft.com/dotnet/sdk:latest`.
- `compose.yml`: defines the Docker Compose service `opencode`.
- `opencode.json`: contains the Opencode configuration for the `chat-ai` provider.
- `opencode.env.example`: example file for the required `GWDG_API_KEY` environment variable.
- `workspace`: working directory mounted into the container.

### Requirements

Docker must be installed. Docker Compose must be available as the modern Docker plugin.

Check this with:

```bash
docker --version
docker compose version
docker info
```

The Compose file can be checked without printing secret values:

```bash
docker compose config --no-interpolate
```

If `docker compose` is missing, this package can be installed on Ubuntu 24.04:

```bash
sudo apt install docker-compose-v2
```

If `docker info` fails because of missing permissions, there are two options:

```bash
sudo docker compose up -d
```

Or allow the current user to use Docker permanently:

```bash
sudo usermod -aG docker "$USER"
```

After that, a new login is required. Only then should `docker info` work without `sudo`.

### Set up the API key

Before starting the container, create a local `opencode.env` file:

```bash
cp opencode.env.example opencode.env
```

Then set the real API key in `opencode.env`:

```text
GWDG_API_KEY=your_real_key
```

Alternatively, the existing key can be copied from the local Opencode file `~/.local/share/opencode/auth.json`. In this setup, the value from `chat-ai.key` is stored as `GWDG_API_KEY` in `opencode.env`.

The `opencode.env` file is not versioned. It is explicitly excluded in `.gitignore` and must not be pushed to the GitLab repository. Because it contains a secret value, only the current user should be able to read it:

```bash
chmod 600 opencode.env
```

### Build and start the container

Run this from the repository directory:

```bash
docker compose up -d
```

On the first start, Docker builds the image. This can take some time because Debian packages are installed and Opencode is downloaded through npm.

Compose is configured to check for a newer base image during builds. This can also be run explicitly:

```bash
docker compose build --pull
docker compose up -d
```

### Use Opencode

Open a shell inside the container:

```bash
docker compose exec opencode bash
```

Start Opencode:

```bash
opencode
```

### Configuration

The `opencode.json` file uses the `chat-ai` provider with this base URL:

```text
https://chat-ai.academiccloud.de/v1
```

The API key is read from the `GWDG_API_KEY` environment variable. The default model is:

```text
chat-ai/glm-4.7
```

Additional agents are configured for coding, Qwen coding, and brainstorming.

### Opencode version

The `Dockerfile` installs Opencode with this command:

```dockerfile
RUN npm i -g opencode-ai@latest
```

This means that each new image build installs the latest `opencode-ai` version from npm.

### Clean up

Stop the container but keep data:

```bash
docker compose down
```

Stop the container and delete persistent Opencode data:

```bash
docker compose down -v
```
