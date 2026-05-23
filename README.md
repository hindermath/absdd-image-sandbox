# Opencode Docker-Umgebung / Opencode Docker Environment

Eine vorbereitete Container-Lern- und Entwicklungsumgebung für Fachinformatiker:innen.
Sprachen und Werkzeuge: .NET, C#, Java, Go, Rust, Python, Maven, Node.js, Opencode, Codex CLI, Spec Kit.

*A ready-to-use container learning and development environment for IT-specialist apprentices.
Languages and tools: .NET, C#, Java, Go, Rust, Python, Maven, Node.js, Opencode CLI/TUI, Codex CLI/TUI, Spec Kit*

---

> **Dokumentationsstandard:** Diese Dokumentation ist so aufbereitet, dass sie für Auszubildende der Fachinformatik ab mindestens dem 1. Lehrjahr geeignet ist. Sie verwendet ein Sprachniveau nach CEFR B2, berücksichtigt Barrierefreiheit nach WCAG 2.2 Level AA und führt Inhalte zuerst auf Deutsch und danach auf Englisch auf.
>
> **Documentation standard:** This documentation is prepared for IT-specialist apprentices from at least the first year of training. It uses CEFR B2 language level, considers accessibility according to WCAG 2.2 Level AA, and presents content first in German and then in English.

## Kurzlebige Aufgabenumgebung / Short-Lived Task Environment

Dieses Image ist für agentische KI-Aufgaben gedacht, die bewusst kurzlebig bearbeitet werden: Image bauen, Container starten, Aufgabe erledigen, relevante Ergebnisse sichern und die laufende Umgebung danach wieder stoppen oder löschen. Es ist keine dauerhaft gepflegte VM und sollte nicht als langlebiger Arbeitsplatz mit dauerhaftem Zustand verstanden werden.

Persistente Daten liegen nur dort, wo sie bewusst gemountet oder in Volumes abgelegt werden, zum Beispiel in Projektverzeichnissen, `/workspace`, `opencode_data`, `codex_data` oder `dotnet_build`. Vor dem Löschen von Volumes prüfen, ob dort noch benötigte Daten liegen.

This image is intended for short-lived agentic AI tasks: build the image, start the container, complete the task, save the relevant results, then stop or remove the running environment. It is not a long-lived VM and should not be treated as a permanent workstation with permanent state.

Persistent data exists only where it is intentionally mounted or stored in volumes, for example in project directories, `/workspace`, `opencode_data`, `codex_data`, or `dotnet_build`. Check volumes before deleting them.

---

## Hinweis für Auszubildende und Kolleg:innen / Note for Apprentices and Colleagues

Dieses Repository ist die zentrale Vorlage für die ADE-Entwicklungsumgebung. Bitte arbeitet für eigene Übungen, Anpassungen und Experimente nicht direkt im Ursprungsrepo, sondern erstellt zuerst einen persönlichen Fork in GitLab.

Empfohlener Ablauf:

1. In GitLab über **Fork** eine eigene Kopie des Repositories erstellen.
2. Den eigenen Fork lokal klonen.
3. Wenn etwas auffällt oder nicht so funktioniert wie beschrieben, bitte zuerst im eigenen Fork prüfen, ob es dort auch passiert. Wenn ja, dann gerne eine Verbesserung per Issue im Ursprungsrepo vorschlagen.
4. Bei Änderungen diese in eigenen Branches vornehmen.
5. Relevante Verbesserungen per Merge Request zurück an das Ursprungsrepo vorschlagen.

Lokale Secret-Dateien wie `opencode.env` und `.env` werden nicht mitgeforkt und dürfen nicht committed werden.

This repository is the central template for the ADE development environment. For your own exercises, changes, and experiments, do not work directly in the upstream repository. Create a personal fork in GitLab first.

Recommended flow:

1. Use **Fork** in GitLab to create your own copy of the repository.
2. Clone your own fork locally.
3. If you notice any issues or something doesn't work as described, first check if it also happens in your own fork. If it does, feel free to propose an improvement via an issue in the upstream repository.
4. Make changes in your own branches.
5. Propose useful improvements back to the upstream repository through a merge request.

Local secret files such as `opencode.env` and `.env` are not included in forks and must not be committed.

---

## Inhaltsverzeichnis / Table of Contents

### Deutsch

- [Auf einen Blick](#auf-einen-blick)
- [Schnellstart in 10 Minuten](#schnellstart-in-10-minuten)
- [Voraussetzungen](#voraussetzungen)
- [Zielgruppe und Zweck](#zielgruppe-und-zweck)
- [Lernpfad für Azubis](#lernpfad-für-azubis)
- [Grundidee](#grundidee)
- [Begriffe und Ausführungsort](#begriffe-und-ausführungsort)
- [Projektstruktur](#projektstruktur)
- [Docker und Podman: gleiche Befehle](#docker-und-podman-gleiche-befehle)
- [Docker unter Ubuntu oder WSL2 installieren](#docker-unter-ubuntu-oder-wsl2-installieren)
- [Docker-Desktop-Profile für macOS und Windows](#docker-desktop-profile-für-macos-und-windows)
- [Podman unter Ubuntu 24.04 LTS verwenden](#podman-unter-ubuntu-2404-lts-verwenden)
- [Podman unter macOS mit Homebrew verwenden](#podman-unter-macos-mit-homebrew-verwenden)
- [Podman unter Windows mit Podman Desktop verwenden](#podman-unter-windows-mit-podman-desktop-verwenden)
- [Docker-Berechtigungen prüfen](#docker-berechtigungen-prüfen)
- [API-Key einrichten](#api-key-einrichten)
- [Container bauen und starten](#container-bauen-und-starten)
- [Rider-Projekte aus Windows einbinden](#rider-projekte-aus-windows-einbinden)
- [.NET und C# im Container nutzen](#net-und-c-im-container-nutzen)
- [Java-Projekte einbinden](#java-projekte-einbinden)
- [Java und Maven im Container nutzen](#java-und-maven-im-container-nutzen)
- [Go im Container nutzen](#go-im-container-nutzen)
- [Rust im Container nutzen](#rust-im-container-nutzen)
- [Python im Container nutzen](#python-im-container-nutzen)
- [Skripte mit Bash und PowerShell](#skripte-mit-bash-und-powershell)
- [ASP.NET-Web-App vom Host erreichen](#aspnet-web-app-vom-host-erreichen)
- [Spec Kit verwenden](#spec-kit-verwenden)
- [Opencode verwenden](#opencode-verwenden)
- [Codex CLI verwenden](#codex-cli-verwenden)
- [Spec-Kit-Governance-Presets installieren](#spec-kit-governance-presets-installieren)
- [Beispiel: ConsoleApp2 mit Opencode und Spec Kit](#beispiel-consoleapp2-mit-opencode-und-spec-kit)
- [Pilot: ASP.NET-Web-App mit Opencode und Spec Kit](#pilot-aspnet-web-app-mit-opencode-und-spec-kit)
- [Pflichtablauf für ein SDD-Feature](#pflichtablauf-für-ein-sdd-feature)
- [Konfiguration](#konfiguration)
- [Image-SBOM erzeugen](#image-sbom-erzeugen)
- [Image-SBOM auswerten](#image-sbom-auswerten)
- [Aufräumen](#aufräumen)
- [Häufige Probleme](#häufige-probleme)
- [Kompakter Testablauf](#kompakter-testablauf)
- [Merksätze](#merksätze)
- [Glossar](#glossar)
- [Barrierefreiheit](#barrierefreiheit)

### English

- [At a glance](#at-a-glance)
- [Quick start in 10 minutes](#quick-start-in-10-minutes)
- [Prerequisites](#prerequisites)
- [Target group and purpose](#target-group-and-purpose)
- [Learning path for apprentices](#learning-path-for-apprentices)
- [Basic idea](#basic-idea)
- [Terms and command location](#terms-and-command-location)
- [Project structure](#project-structure)
- [Docker and Podman: the same commands](#docker-and-podman-the-same-commands)
- [Install Docker on Ubuntu or WSL2](#install-docker-on-ubuntu-or-wsl2)
- [Docker Desktop profiles for macOS and Windows](#docker-desktop-profiles-for-macos-and-windows)
- [Use Podman on Ubuntu 24.04 LTS](#use-podman-on-ubuntu-2404-lts)
- [Use Podman on macOS with Homebrew](#use-podman-on-macos-with-homebrew)
- [Use Podman on Windows with Podman Desktop](#use-podman-on-windows-with-podman-desktop)
- [Check Docker permissions](#check-docker-permissions)
- [Set up the API key](#set-up-the-api-key)
- [Build and start the container](#build-and-start-the-container)
- [Mount Rider projects from Windows](#mount-rider-projects-from-windows)
- [Use .NET and C# inside the container](#use-net-and-c-inside-the-container)
- [Mount Java projects](#mount-java-projects)
- [Use Java and Maven inside the container](#use-java-and-maven-inside-the-container)
- [Use Go inside the container](#use-go-inside-the-container)
- [Use Rust inside the container](#use-rust-inside-the-container)
- [Use Python inside the container](#use-python-inside-the-container)
- [Scripting with Bash and PowerShell](#scripting-with-bash-and-powershell)
- [Reach an ASP.NET web app from the host](#reach-an-aspnet-web-app-from-the-host)
- [Use Spec Kit](#use-spec-kit)
- [Use Opencode](#use-opencode)
- [Use Codex CLI](#use-codex-cli)
- [Install Spec Kit governance presets](#install-spec-kit-governance-presets)
- [Example: ConsoleApp2 with Opencode and Spec Kit](#example-consoleapp2-with-opencode-and-spec-kit)
- [Pilot: ASP.NET web app with Opencode and Spec Kit](#pilot-aspnet-web-app-with-opencode-and-spec-kit)
- [Required flow for an SDD feature](#required-flow-for-an-sdd-feature)
- [Configuration](#configuration)
- [Generate an image SBOM](#generate-an-image-sbom)
- [Analyze an image SBOM](#analyze-an-image-sbom)
- [Clean up](#clean-up)
- [Common problems](#common-problems)
- [Compact test procedure](#compact-test-procedure)
- [Quick rules](#quick-rules)
- [Glossary](#glossary)
- [Accessibility](#accessibility)

---

## Deutsch

### Auf einen Blick

| Punkt | Information |
|---|---|
| Zielgruppe | Fachinformatiker:innen ab dem 1. Lehrjahr |
| Lernziel | Reproduzierbare Entwicklungsumgebung im Container nutzen |
| Sprachen | C# / .NET, Java, Go, Rust, Python, Bash, PowerShell |
| Container | Docker oder Podman, auf Linux, macOS oder Windows |
| Zeitbedarf für den Schnellstart | etwa 10 Minuten Lesen, 15 bis 30 Minuten erster Build |
| Zeitbedarf für volle Erkundung | mehrere Übungseinheiten über mehrere Wochen |
| Vorwissen | Grundlagen Shell, grobes Verständnis von Git |
| Barrierefreiheit | WCAG 2.2 Level AA, siehe Abschnitt [Barrierefreiheit](#barrierefreiheit) |

### Schnellstart in 10 Minuten

Dieser Schnellstart richtet sich an alle, die das Setup zuerst nur ausprobieren wollen. Die Details folgen in den späteren Abschnitten.

> **Docker oder Podman:** Dieser Schnellstart nutzt Docker. Mit Podman die Befehle sinngemäß ersetzen (`podman compose` oder `podman-compose`) und für die Erstanmeldung an der GitLab-Registry den passenden Podman-Abschnitt nutzen: [Ubuntu](#podman-unter-ubuntu-2404-lts-verwenden), [macOS](#podman-unter-macos-mit-homebrew-verwenden), [Windows](#podman-unter-windows-mit-podman-desktop-verwenden).

Schritt 1: Voraussetzungen prüfen.

- Docker Engine oder Docker Desktop ist installiert.
- Eine Shell ist offen (Bash unter Linux/macOS, PowerShell unter Windows).
- Du kennst den Pfad zu diesem Repository auf deinem Rechner.

Schritt 2: In das Repository wechseln. Ersetze `<benutzer>` durch deinen Anmeldenamen.

```bash
cd /home/<benutzer>/ade-dev-sandbox     # Linux / WSL2
cd /Users/<benutzer>/ade-dev-sandbox    # macOS
```

```powershell
cd C:\Users\<benutzer>\ade-dev-sandbox  # Windows
```

Schritt 3: Lokale Konfigurationsdateien anlegen. `.env` enthält nur Pfade, `opencode.env` enthält den geheimen API-Key.

```bash
cp .env.example .env
cp opencode.env.example opencode.env
chmod 600 opencode.env
```

Schritt 4: In `opencode.env` den echten `GWDG_API_KEY` eintragen. Den Key nicht in das Terminal ausgeben und nicht committen.

Schritt 5: Container bauen und starten.

```bash
docker compose build --pull
docker compose up -d
docker compose ps
```

Schritt 6: Eine Shell im Container öffnen.

```bash
docker compose exec ade bash
```

Schritt 7: Im Container prüfen, ob alles bereit ist.

```bash
dotnet --info
opencode --version
specify version
```

Wenn diese drei Befehle Versionsinformationen ausgeben, ist der Schnellstart erfolgreich abgeschlossen. Für die ersten echten Übungen geht es weiter im Abschnitt [Lernpfad für Azubis](#lernpfad-für-azubis).

### Voraussetzungen

Diese Anleitung geht von folgenden Mindestvoraussetzungen aus. Die Werte sind großzügig gewählt, damit der Container auch beim Bauen größerer Projekte stabil läuft.

| Anforderung | Mindestwert | Empfohlen | Hinweis |
|---|---|---|---|
| Betriebssystem | Ubuntu 22.04, macOS 13, Windows 11 | aktuelle LTS oder Folgeversion | Für Windows wird WSL2 empfohlen. |
| Arbeitsspeicher (RAM) | 8 GiB | 16 GiB oder mehr | .NET, Java und Container brauchen Speicher. |
| Freier Plattenspeicher | 20 GiB | 50 GiB oder mehr | Images, Volumes und Build-Cache wachsen. |
| Internet | 10 Mbit/s | 50 Mbit/s | Erste Builds laden viele Pakete. |
| Berechtigungen | lokales Benutzerkonto | sudo oder Admin für die Installation | Für die Container-Nutzung selbst reicht der normale Benutzer. |
| Vorkenntnisse | Shell-Grundlagen, Git-Grundlagen | dazu Editor-Erfahrung | Editor: Visual Studio Code oder JetBrains Rider. |

Wenn ein Punkt nicht erfüllt ist, geht der Schnellstart trotzdem oft. Das Setup wird aber langsamer oder weniger stabil.

### Zielgruppe und Zweck

Diese Anleitung richtet sich an angehende Fachinformatiker:innen ab dem 1. Lehrjahr. Sie erklärt nicht nur die Befehle, sondern auch kurz, warum sie gebraucht werden.

Dieses Repository stellt eine Docker-Umgebung für Opencode, .NET, C#, Java, Go, Rust und Python bereit. Die Umgebung läuft mit Docker Engine unter Linux oder WSL2 und mit Docker Desktop unter macOS oder Windows. Projekte können weiter mit JetBrains Rider auf dem Host bearbeitet werden.

### Lernpfad für Azubis

Die README ist lang. Sie ist aber kein Buch, das du in einem Stück lesen musst. Dieser Lernpfad zeigt eine sinnvolle Reihenfolge.

| Phase | Abschnitte | Lernziel |
|---|---|---|
| Phase 1: Verstehen | [Grundidee](#grundidee), [Begriffe und Ausführungsort](#begriffe-und-ausführungsort), [Projektstruktur](#projektstruktur) | Was ist ein Container? Was ist ein Image? Wo läuft welcher Befehl? |
| Phase 2: Aufsetzen | [Voraussetzungen](#voraussetzungen), eine der Installationssektionen (Docker oder Podman), [API-Key einrichten](#api-key-einrichten), [Container bauen und starten](#container-bauen-und-starten) | Container läuft auf dem eigenen Rechner. |
| Phase 3: Erste Übungen | [.NET und C# im Container nutzen](#net-und-c-im-container-nutzen), [Java und Maven im Container nutzen](#java-und-maven-im-container-nutzen), [Go im Container nutzen](#go-im-container-nutzen), [Rust im Container nutzen](#rust-im-container-nutzen), [Python im Container nutzen](#python-im-container-nutzen), [Skripte mit Bash und PowerShell](#skripte-mit-bash-und-powershell) | Ein eigenes Konsolen- oder Skriptprojekt anlegen, bauen und starten. |
| Phase 4: Werkzeuge der Praxis | [Spec Kit verwenden](#spec-kit-verwenden), [Opencode verwenden](#opencode-verwenden), [Codex CLI verwenden](#codex-cli-verwenden) | KI-Werkzeuge für Spezifikation und Code richtig einsetzen. |
| Phase 5: Qualität und Sicherheit | [Spec-Kit-Governance-Presets installieren](#spec-kit-governance-presets-installieren), [Pflichtablauf für ein SDD-Feature](#pflichtablauf-für-ein-sdd-feature), [Konfiguration](#konfiguration) | Regelwerk, sichere Entwicklung, Qualitätsprozess. |
| Phase 6: Betrieb und Fehlerbehebung | [Aufräumen](#aufräumen), [Häufige Probleme](#häufige-probleme), [Kompakter Testablauf](#kompakter-testablauf) | Eigene Umgebung pflegen und Fehler verstehen. |

Empfehlung für das erste Lehrjahr: Phasen 1 bis 3. Phasen 4 bis 6 sind danach an der Reihe und auch passend für höhere Lehrjahre oder Umschulungen.

### Grundidee

Docker erstellt aus dem `Dockerfile` ein Image. Aus diesem Image startet Docker Compose einen Container. Der Container enthält das Microsoft .NET SDK, Java JDK 21, Maven, Go, Rust, Python, Node.js, npm, Opencode, Codex CLI und gängige Agenten-Hilfswerkzeuge.

Der Container bleibt im Hintergrund aktiv. Danach kann eine Shell im Container geöffnet werden. Dort können Befehle wie `dotnet`, `opencode`, `codex` oder `ls` ausgeführt werden.

Die Shell läuft im Container als Linux-Benutzer `adedev`. Deshalb beginnt die Promptzeile nach dem Einstieg zum Beispiel mit `adedev@...`. Der Compose-Service heißt `ade`; das OpenCode-Programm heißt weiterhin `opencode`.

### Begriffe und Ausführungsort

Viele Fehler entstehen, wenn ein Befehl am falschen Ort ausgeführt wird. Diese Anleitung trennt deshalb zwischen Host und Container.

- Host: der eigene Rechner oder die WSL2-Umgebung. Dort werden `docker compose ...`-Befehle ausgeführt.
- Container: die Linux-Umgebung, die Docker aus dem Image startet. Dort werden Werkzeuge wie `dotnet`, `java`, `mvn`, `go`, `cargo`, `python`, `opencode`, `codex` und `specify` ausgeführt.
- Image: die Vorlage für den Container. Nach Änderungen am `Dockerfile` muss das Image neu gebaut werden.
- Bind-Mount: ein Host-Verzeichnis wird direkt in den Container eingebunden, zum Beispiel `/rider-projects` oder `/java-projects`.
- Volume: ein von Docker verwalteter Speicherbereich, zum Beispiel für `/dotnet-build` oder lokale Agenten-Daten.
- Service: der Name in `compose.yml`. In diesem Repository heißt der Service `ade`.

Wenn der Prompt mit `adedev@...` beginnt, befindet sich die Shell im Container. Wenn der Prompt den normalen Rechnernamen oder die WSL2-Shell zeigt, befindet sie sich auf dem Host.

Ein vollständigeres Begriffsregister steht im Abschnitt [Glossar](#glossar).

### Projektstruktur

- `Dockerfile`: beschreibt das Container-Image. Es erbt vom gemeinsamen `agent-sandbox`-Image und installiert darauf .NET SDK, Java JDK 21, Maven, Go, Rust, Python, Opencode, Codex CLI, `uv`, Spec Kit und gängige CLI-Hilfswerkzeuge.
- `compose.yml`: beschreibt den Service `ade`, Volumes und Build-Regeln.
- `.dockerignore` und `.containerignore`: schließen lokale Secrets, Git-Daten und Arbeitsverzeichnisse aus dem Build-Kontext aus.
- `.env.example`: Vorlage für die plattformabhängigen Projekt-Mounts `RIDER_PROJECTS_DIR`, `JAVA_PROJECTS_DIR`, `GO_PROJECTS_DIR`, `RUST_PROJECTS_DIR` und `PYTHON_PROJECTS_DIR`.
- `opencode.jsonc`: enthält Provider, Modelle und Agenten für Opencode. JSONC erlaubt Kommentare und ist deshalb für Lernzwecke besser lesbar.
- `opencode.env.example`: Vorlage für die lokale Datei `opencode.env`.
- `codex/config.toml`: systemweite Codex-Standardkonfiguration für den Container. Sie wird nach `/etc/codex/config.toml` und `/etc/codex/managed_config.toml` kopiert.
- `codex/requirements.toml`: admin-erzwingende Codex-Sicherheitsanforderungen. Sie wird nach `/etc/codex/requirements.toml` kopiert.
- `workspace/`: lokales Arbeitsverzeichnis, im Container unter `/workspace`.
- `RIDER_PROJECTS_DIR`: Host-Verzeichnis für Rider-Projekte, im Container unter `/rider-projects`.
- `JAVA_PROJECTS_DIR`: Host-Verzeichnis für Java-Projekte, im Container unter `/java-projects`.
- `java-projects/`: lokales Fallback-Verzeichnis für Java-Projekte, wenn `JAVA_PROJECTS_DIR` nicht gesetzt ist.
- `GO_PROJECTS_DIR`: Host-Verzeichnis für Go-Projekte, im Container unter `/go-projects`.
- `go-projects/`: lokales Fallback-Verzeichnis für Go-Projekte, wenn `GO_PROJECTS_DIR` nicht gesetzt ist.
- `RUST_PROJECTS_DIR`: Host-Verzeichnis für Rust-Projekte, im Container unter `/rust-projects`.
- `rust-projects/`: lokales Fallback-Verzeichnis für Rust-Projekte, wenn `RUST_PROJECTS_DIR` nicht gesetzt ist.
- `PYTHON_PROJECTS_DIR`: Host-Verzeichnis für Python-Projekte, im Container unter `/python-projects`.
- `python-projects/`: lokales Fallback-Verzeichnis für Python-Projekte, wenn `PYTHON_PROJECTS_DIR` nicht gesetzt ist.
- `dotnet/ContainerBuild.props`: leitet .NET-Build-Artefakte für Rider-Projekte in das Container-Volume `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: filtert eine bekannte .NET-Workload-Verifikationsmeldung aus der Ausgabe.
- `spec-kit/patch-specify-cli.py`: passt Spec Kit für Windows- und WSL-Bind-Mounts an.
- `codex_data`: Docker-Volume für Codex-CLI-Daten unter `/home/adedev/.codex`.
- `AGENTS.md`: Regeln für KI-Agenten wie Opencode oder Codex.

### Docker und Podman: gleiche Befehle

Diese Anleitung zeigt die meisten Beispiele mit `docker`. Podman ist weitgehend befehlskompatibel. Die allgemeinen Abschnitte wie [Container bauen und starten](#container-bauen-und-starten), [.NET und C# im Container nutzen](#net-und-c-im-container-nutzen), [ASP.NET-Web-App vom Host erreichen](#aspnet-web-app-vom-host-erreichen) und [Kompakter Testablauf](#kompakter-testablauf) gelten deshalb für beide Werkzeuge. Ersetze die Befehle sinngemäß:

| Docker | Podman |
|---|---|
| `docker compose build --pull` | `podman compose build --pull` oder `podman-compose build --pull` |
| `docker compose up -d` | `podman compose up -d` oder `podman-compose up -d` |
| `docker compose ps` | `podman compose ps` oder `podman-compose ps` |
| `docker compose exec ade bash` | `podman compose exec ade bash` oder `podman-compose exec ade bash` |
| `docker compose down` | `podman compose down` oder `podman-compose down` |
| `docker compose down -v` | `podman compose down -v` oder `podman-compose down -v` |
| `docker info` | `podman info` |

Hinweis zur Schreibweise: Auf vielen Linux-Installationen heißt der Compose-Befehl `podman-compose` (mit Bindestrich). Auf macOS und Windows mit Podman Desktop funktioniert oft `podman compose` (mit Leerzeichen). Wenn eine Variante nicht vorhanden ist, die jeweils andere verwenden.

Für eine vollständige Schritt-für-Schritt-Anleitung mit Podman gibt es eigene Abschnitte für [Ubuntu](#podman-unter-ubuntu-2404-lts-verwenden), [macOS](#podman-unter-macos-mit-homebrew-verwenden) und [Windows](#podman-unter-windows-mit-podman-desktop-verwenden). Ein wichtiger Unterschied bleibt: Beim Bauen des privaten GitLab-Basisimages verwenden externe Compose-Provider unter macOS und Windows manchmal andere Registry-Anmeldedaten. Deshalb bauen die Podman-Abschnitte das Image dort bewusst direkt mit `podman build`. Für den normalen Betrieb mit `up`, `ps`, `exec` und `down` sind die Befehle aber austauschbar.

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

Unter WSL2 funktioniert `systemctl` nur, wenn systemd aktiv ist. Falls der Befehl scheitert, kann Docker auch über Docker Desktop für Windows bereitgestellt werden. In diesem Fall muss die WSL-Integration für die verwendete Distribution aktiviert sein.

Installation prüfen:

```bash
docker --version
docker compose version
docker info
```

Die Compose-Datei kann ohne Secret-Ausgabe geprüft werden:

```bash
docker compose config --no-interpolate
```

### Docker-Desktop-Profile für macOS und Windows

Wenn Docker Desktop verwendet wird, bleibt der Container ein Linux-Container. Der Unterschied liegt nur in den Host-Pfaden, die nach `/rider-projects` und `/java-projects` eingebunden werden.

Docker Desktop kann für private Nutzung, Ausbildung, Lernen, kleine Unternehmen und nicht-kommerzielle Open-Source-Projekte kostenlos genutzt werden. Kommerzielle Nutzung in größeren Unternehmen mit mehr als 250 Mitarbeitenden oder mehr als 10 Mio. USD Jahresumsatz benötigt ein bezahltes Docker-Abo. Im Zweifel gelten die aktuellen Bedingungen des Docker Subscription Service Agreement.

macOS mit Homebrew:

```bash
brew install --cask docker
open -a Docker
```

Danach im Terminal prüfen:

```bash
docker --version
docker compose version
docker info
```

Windows mit Winget:

```powershell
winget install --id Docker.DockerDesktop -e
```

Danach Docker Desktop aus dem Startmenü starten, die Lizenzbedingungen akzeptieren und sicherstellen, dass das WSL2-Backend aktiviert ist. Alternativ kann der Installer von der offiziellen Docker-Webseite verwendet werden.

Zuerst die Compose-Umgebungsdatei anlegen:

```bash
cp .env.example .env
```

Danach `RIDER_PROJECTS_DIR` und `JAVA_PROJECTS_DIR` passend zur Plattform setzen.

macOS:

```text
RIDER_PROJECTS_DIR=/Users/<benutzer>/RiderProjects
JAVA_PROJECTS_DIR=/Users/<benutzer>/JavaProjects
```

Windows mit Docker Desktop aus PowerShell:

```text
RIDER_PROJECTS_DIR=C:\Users\<benutzer>\RiderProjects
JAVA_PROJECTS_DIR=C:\Users\<benutzer>\JavaProjects
```

Windows mit Docker Desktop aus Ubuntu/WSL2:

```text
RIDER_PROJECTS_DIR=/mnt/c/Users/<benutzer>/RiderProjects
JAVA_PROJECTS_DIR=/mnt/c/Users/<benutzer>/JavaProjects
```

Wenn kein separates Rider- oder Java-Projektverzeichnis gebraucht wird, kann der Standard aus `.env.example` bleiben. Dann zeigt `/rider-projects` auf `workspace/` und `/java-projects` auf `java-projects/`.

Die Datei `.env` enthält keine Secrets, ist aber lokal und plattformabhängig. Sie wird nicht committed. Der API-Key bleibt getrennt in `opencode.env`.

Hinweis für Auszubildende: In `.env` stehen nur Pfade. In `opencode.env` steht ein Secret. Diese Trennung ist wichtig, damit ein API-Key nicht versehentlich in Git landet.

Konfiguration prüfen:

```bash
docker compose config --no-interpolate
```

### Podman unter Ubuntu 24.04 LTS verwenden

Podman ist eine Alternative zu Docker. Unter Ubuntu läuft Podman direkt auf dem Linux-Host. Eine Podman-Machine wie unter macOS wird nicht gebraucht.

Podman, Podman Compose und Flatpak installieren:

```bash
sudo apt update
sudo apt install -y podman podman-compose flatpak
```

Installation prüfen:

```bash
podman --version
podman-compose --version
podman run --rm quay.io/podman/hello
```

Podman Desktop optional über Flathub installieren:

```bash
flatpak remote-add --if-not-exists --user flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install --user flathub io.podman_desktop.PodmanDesktop
```

Podman Desktop starten:

```bash
flatpak run io.podman_desktop.PodmanDesktop
```

Vor dem Start die lokalen Umgebungsdateien anlegen. `.env` enthält lokale Pfade, `opencode.env` enthält den geheimen API-Key:

```bash
cp .env.example .env
cp opencode.env.example opencode.env
chmod 600 opencode.env
```

Danach in `opencode.env` den echten `GWDG_API_KEY` eintragen. Den Key nicht im Terminal ausgeben und nicht committen.

In das Repository wechseln:

```bash
cd /home/<benutzer>/ade-dev-sandbox
```

Vor dem ersten Build bei der GitLab Container Registry anmelden. Als Passwort einen GitLab-Token mit mindestens `read_registry` verwenden:

```bash
podman login docker.gitlab-ce.gwdg.de
```

Compose-Datei prüfen, ohne Variablenwerte und Secrets auszubreiten:

```bash
podman-compose config --no-interpolate
```

Image über die Compose-Konfiguration bauen:

```bash
podman-compose build --pull
```

Nur das Image direkt aus diesem Verzeichnis bauen, ohne den Compose-Service zu starten:

```bash
podman build --pull -t ade-dev-sandbox .
```

Container im Hintergrund starten:

```bash
podman-compose up -d
```

Status anzeigen:

```bash
podman-compose ps
```

Bash im laufenden `ade`-Container öffnen:

```bash
podman-compose exec ade bash
```

Die Container-Shell wieder verlassen:

```bash
exit
```

Container stoppen, Daten behalten:

```bash
podman-compose down
```

Container stoppen und persistente Container- und Volume-Daten aus diesem Compose-Projekt löschen:

```bash
podman-compose down -v
```

Hinweis: Auf manchen Installationen funktioniert auch `podman compose ...`. Wenn dieser Befehl aber Docker Compose als Provider startet oder den Docker-Daemon sucht, für dieses Repository `podman-compose ...` verwenden.

WSL2- und Windows-Hinweis: Wenn dieselbe Umgebung einmal mit Podman Desktop unter Windows und einmal mit Podman in WSL2 gestartet wird, dürfen nicht beide Container gleichzeitig laufen. Beide Varianten veröffentlichen dieselbe Port-Range `127.0.0.1:5100-5199`. Vor dem Start in WSL2 den Windows-Container in Podman Desktop oder PowerShell stoppen:

```powershell
podman compose down
```

Vor dem Start unter Windows den WSL2-Container stoppen:

```bash
podman-compose down
```

### Podman unter macOS mit Homebrew verwenden

Podman ist eine Alternative zu Docker Desktop. Unter macOS läuft der eigentliche Linux-Container ebenfalls in einer kleinen virtuellen Maschine. Diese virtuelle Maschine heißt bei Podman `machine`.

Podman und Podman Compose mit Homebrew installieren:

```bash
brew install podman podman-compose
```

Installation prüfen:

```bash
podman --version
podman compose version
```

Die Podman-Machine einmalig anlegen:

```bash
podman machine init
```

Die Podman-Machine starten:

```bash
podman machine start
```

Danach prüfen, ob Podman läuft:

```bash
podman info
```

Vor dem Start auch bei Podman die lokalen Umgebungsdateien anlegen. `.env` enthält lokale Pfade, `opencode.env` enthält den geheimen API-Key:

```bash
cp .env.example .env
cp opencode.env.example opencode.env
chmod 600 opencode.env
```

Danach in `opencode.env` den echten `GWDG_API_KEY` eintragen. Den Key nicht im Terminal ausgeben und nicht committen.

In das Repository wechseln:

```bash
cd /Users/<benutzer>/ade-dev-sandbox
```

Vor dem ersten Build bei der GitLab Container Registry anmelden. Als Passwort einen GitLab-Token mit mindestens `read_registry` verwenden:

```bash
podman login docker.gitlab-ce.gwdg.de
```

Compose-Datei prüfen, ohne Variablenwerte und Secrets auszubreiten:

```bash
podman compose config --no-interpolate
```

Image bauen und dabei das gepinnte Sandbox-Basisimage nachziehen:

```bash
podman compose build --pull
```

Wenn `podman compose build --pull` meldet, dass ein externer Compose-Provider wie `/usr/local/bin/docker-compose` verwendet wird, ist das unter macOS nicht automatisch ein Fehler. Bricht der Build aber beim privaten GitLab-Basisimage mit `Requesting bearer token` und `403 Forbidden` ab, verwendet der externe Provider wahrscheinlich andere Registry-Anmeldedaten als `podman login`. Dann das Basisimage und das Projektimage direkt mit Podman bauen und Compose nur für den Start verwenden:

```bash
podman pull docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox@sha256:a21e15872aed8b0e4b9e18e0ff1e678318968efb4b8367ddf9fa4a63fc1d294c
podman build --pull -t ade-dev-sandbox-ade .
podman compose up -d --no-build --force-recreate
```

Wenn Podman Desktop sichtbar läuft, die Terminal-CLI aber trotzdem mit einer Meldung wie `unable to connect to Podman socket`, `connection refused` oder einem veralteten `ssh://core@127.0.0.1:<port>` abbricht, zuerst die aktive Verbindung prüfen:

```bash
podman machine list
podman system connection list
ls -l /var/run/docker.sock
docker --host unix:///var/run/docker.sock version
```

Unter macOS legt Podman Desktop häufig einen Docker-kompatiblen Socket an. Dann zeigt `/var/run/docker.sock` auf einen Podman-Socket unter `~/.local/share/containers/podman/machine/podman.sock`. In diesem Fall kann das Image mit der Docker-CLI gegen Podman gebaut werden, ohne Docker Desktop zu starten:

```bash
docker --host unix:///var/run/docker.sock compose build --pull
docker --host unix:///var/run/docker.sock image inspect ade-dev-sandbox-ade --format '{{.Id}} {{.Architecture}} {{.Os}} {{.Size}}'
```

Der Image- und Container-Store liegt dabei logisch in der Podman-Machine unter `/var/home/core/.local/share/containers/storage` und verwendet in der Regel den Treiber `overlay`. Physisch liegt dieser Store auf macOS in der virtuellen Disk der Podman-Machine, zum Beispiel unter `~/.local/share/containers/podman/machine/applehv/podman-machine-default-arm64.raw`. Diese Datei ist keine einzelne Image-Datei, sondern die virtuelle Linux-Disk der Podman-Machine.

Danach direkt mit der Statusprüfung fortfahren.

Container im Hintergrund starten:

```bash
podman compose up -d
```

Status anzeigen:

```bash
podman compose ps
```

Bash im laufenden `ade`-Container öffnen:

```bash
podman compose exec ade bash
```

Die Container-Shell wieder verlassen:

```bash
exit
```

Container stoppen, Daten behalten:

```bash
podman compose down
```

Container stoppen und persistente Container- und Volume-Daten aus diesem Compose-Projekt löschen:

```bash
podman compose down -v
```

Wenn Podman danach nicht mehr gebraucht wird, kann auch die Podman-Machine gestoppt werden:

```bash
podman machine stop
```

Falls `podman compose ...` auf einer Installation nicht verfügbar ist, kann derselbe Ablauf mit `podman-compose ...` ausgeführt werden, zum Beispiel:

```bash
podman-compose build --pull
podman-compose up -d
podman-compose exec ade bash
podman-compose down
```

### Podman unter Windows mit Podman Desktop verwenden

Podman ist eine Alternative zu Docker Desktop. Unter Windows laufen Linux-Container in einer kleinen virtuellen Maschine. Podman nennt diese virtuelle Maschine `machine`. Podman Desktop kann Podman, die Machine und die Compose-Unterstützung einrichten.

Podman Desktop mit Winget installieren:

```powershell
winget install --id RedHat.Podman-Desktop -e
```

Danach Podman Desktop aus dem Startmenü starten. Beim ersten Start die Einrichtung durchlaufen:

- WSL2 als Provider verwenden, wenn keine Hyper-V-Anforderung besteht.
- Podman installieren lassen, wenn Podman noch fehlt.
- Eine Podman-Machine erstellen lassen.
- Die Compose-Unterstützung installieren lassen.

Falls WSL2 noch nicht bereit ist, PowerShell als Administrator öffnen und WSL aktualisieren beziehungsweise aktivieren:

```powershell
wsl --update
wsl --install --no-distribution
```

Wenn Windows einen Neustart verlangt, den Rechner neu starten. Danach prüfen:

```powershell
wsl --status
podman --version
podman machine list
podman info
podman compose version
```

Wenn noch keine Machine existiert oder sie gestoppt ist:

```powershell
podman machine init
podman machine start
```

Vor dem Start die lokalen Umgebungsdateien im Repository anlegen. Diese Befehle laufen in PowerShell auf dem Windows-Host:

```powershell
Copy-Item .env.example .env
Copy-Item opencode.env.example opencode.env
```

Danach in `opencode.env` den echten `GWDG_API_KEY` eintragen. Den Key nicht im Terminal ausgeben und nicht committen.

In `.env` Windows-Pfade setzen, wenn Rider- oder Java-Projekte außerhalb dieses Repositorys liegen:

```text
RIDER_PROJECTS_DIR=C:\Users\<benutzer>\RiderProjects
JAVA_PROJECTS_DIR=C:\Users\<benutzer>\JavaProjects
```

Wenn kein separates Rider- oder Java-Projektverzeichnis gebraucht wird, kann der Standard aus `.env.example` bleiben. Dann zeigt `/rider-projects` auf `workspace/` und `/java-projects` auf `java-projects/`.

In das Repository wechseln:

```powershell
cd C:\Users\<benutzer>\ade-dev-sandbox
```

Vor dem ersten Build bei der GitLab Container Registry anmelden. Als Passwort einen GitLab-Token mit mindestens `read_registry` verwenden:

```powershell
podman login docker.gitlab-ce.gwdg.de
```

Windows-spezifisch: `podman compose` nutzt auf vielen Installationen einen externen Compose-Provider, oft `docker-compose.exe`. Dieser Provider liest nicht zwingend dieselbe Podman-Auth-Datei wie `podman pull`. Deshalb zusätzlich ein Docker-kompatibles Authfile anlegen und dort ebenfalls anmelden:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.docker" | Out-Null
podman login --compat-auth-file "$env:USERPROFILE\.docker\config.json" docker.gitlab-ce.gwdg.de
podman login --get-login --compat-auth-file "$env:USERPROFILE\.docker\config.json" docker.gitlab-ce.gwdg.de
```

Der letzte Befehl muss den GitLab-Benutzernamen ausgeben. Wenn nur `podman login` funktioniert, aber das Docker-kompatible Authfile fehlt, kann `podman pull` erfolgreich sein und `podman compose build --pull` trotzdem beim gepinnten GitLab-Basisimage mit `Requesting bearer token` und `403 Forbidden` scheitern.

Compose-Datei prüfen, ohne Variablenwerte und Secrets auszubreiten:

```powershell
podman compose config --no-interpolate
```

Auf Windows zuerst das gepinnte Basisimage mit Podman ziehen. Dieser Schritt prüft, ob der Registry-Login für Podman funktioniert:

```powershell
podman pull docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox@sha256:a21e15872aed8b0e4b9e18e0ff1e678318968efb4b8367ddf9fa4a63fc1d294c
```

Danach das Projektimage regulär über Compose bauen. Durch das Docker-kompatible Authfile kann auch der externe `docker-compose.exe`-Provider das private GitLab-Basisimage ziehen:

```powershell
podman compose build --pull
```

Container im Hintergrund starten:

```powershell
podman compose up -d --force-recreate
```

Fallback: Wenn `podman compose build --pull` trotz gesetztem Docker-kompatiblem Authfile weiter mit `403 Forbidden` scheitert, zuerst den Login und den direkten Pull erneut prüfen. Als kurzfristige Umgehung kann das Projektimage direkt mit Podman gebaut und Compose nur zum Starten verwendet werden:

```powershell
podman pull docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox@sha256:a21e15872aed8b0e4b9e18e0ff1e678318968efb4b8367ddf9fa4a63fc1d294c
podman build --pull -t ade-dev-sandbox-ade .
podman compose up -d --no-build --force-recreate
```

Status anzeigen:

```powershell
podman compose ps
```

Bash im laufenden `ade`-Container öffnen:

```powershell
podman compose exec ade bash
```

Die Container-Shell wieder verlassen:

```bash
exit
```

Container stoppen, Daten behalten:

```powershell
podman compose down
```

Container stoppen und persistente Container- und Volume-Daten aus diesem Compose-Projekt löschen:

```powershell
podman compose down -v
```

Wenn `podman compose ...` meldet, dass ein externer Compose-Provider wie `docker-compose.exe` verwendet wird, ist das nicht automatisch ein Fehler. Wichtig ist der Auth-Kontext: `docker-compose.exe` braucht auf Windows ein Docker-kompatibles Authfile. Ohne `podman login --compat-auth-file "$env:USERPROFILE\.docker\config.json" docker.gitlab-ce.gwdg.de` kann `podman pull` funktionieren, während `podman compose build --pull` mit `403 Forbidden` am privaten GitLab-Basisimage scheitert.

WSL2- und Windows-Hinweis: Wenn dieselbe Umgebung einmal mit Podman Desktop unter Windows und einmal mit Podman in WSL2 gestartet wird, dürfen nicht beide Container gleichzeitig laufen. Beide Varianten veröffentlichen dieselbe Port-Range `127.0.0.1:5100-5199`. Vor dem Start unter Windows den WSL2-Container stoppen:

```bash
podman-compose down
```

Vor dem Start in WSL2 den Windows-Container in Podman Desktop oder PowerShell stoppen:

```powershell
podman compose down
```

### Docker-Berechtigungen prüfen

Wenn `docker info` mit `permission denied` scheitert, darf der aktuelle Benutzer noch nicht auf Docker zugreifen.

Hinweis für Podman: Podman läuft standardmäßig rootless. Eine Docker-Gruppe wird dann meist nicht gebraucht. Dieser Abschnitt gilt vor allem für Docker.

Schneller Test mit `sudo`:

```bash
sudo docker info
```

Dauerhafte Freigabe für den aktuellen Benutzer:

```bash
sudo usermod -aG docker "$USER"
```

Danach komplett neu anmelden. Erst danach wird die neue Gruppenzugehörigkeit aktiv. Prüfen:

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

Alternativ kann der vorhandene Key aus `~/.local/share/opencode/auth.json` übernommen werden. In diesem Setup wird `chat-ai.key` als `GWDG_API_KEY` gespeichert.

Wichtig: `opencode.env` enthält ein Secret. Die Datei ist in `.gitignore` ausgeschlossen und darf nicht nach GitLab gepusht werden.

```bash
chmod 600 opencode.env
```

### Container bauen und starten

> **Docker oder Podman:** Diese Befehle nutzen Docker. Mit Podman gelten sie sinngemäß — ersetze `docker compose` durch `podman compose` oder `podman-compose` (siehe [Docker und Podman: gleiche Befehle](#docker-und-podman-gleiche-befehle)). Eine vollständige Podman-Anleitung steht in den Abschnitten [Podman unter Ubuntu](#podman-unter-ubuntu-2404-lts-verwenden), [Podman unter macOS](#podman-unter-macos-mit-homebrew-verwenden) und [Podman unter Windows](#podman-unter-windows-mit-podman-desktop-verwenden).

In das Repository wechseln:

```bash
cd /home/<benutzer>/ade-dev-sandbox
```

Vor dem ersten Build bei der GitLab Container Registry anmelden. Als Passwort einen GitLab-Token mit mindestens `read_registry` verwenden:

```bash
docker login docker.gitlab-ce.gwdg.de
```

Image bauen und dabei das gepinnte Sandbox-Basisimage nachziehen:

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

Beim ersten Build werden das gepinnte Sandbox-Basisimage, das .NET-SDK-Paket und npm-Pakete geladen. Das kann einige Minuten dauern.

### Rider-Projekte aus Windows einbinden

Das Host-Verzeichnis für Rider-Projekte wird über `RIDER_PROJECTS_DIR` gesetzt. Typische Werte sind:

```text
RIDER_PROJECTS_DIR=/mnt/c/Users/<benutzer>/RiderProjects
RIDER_PROJECTS_DIR=C:\Users\<benutzer>\RiderProjects
RIDER_PROJECTS_DIR=/Users/<benutzer>/RiderProjects
```

Das Verzeichnis wird im Container hier eingebunden:

```text
/rider-projects
```

Im Container kann dorthin gewechselt werden:

```bash
cd /rider-projects
ls
```

Änderungen im Container wirken direkt auf die Host-Dateien. Rider auf dem Host sieht dieselben Dateien. Builds auf Windows- oder macOS-Bind-Mounts können langsamer sein als Builds im Linux-Dateisystem.

Damit .NET auf Host-Dateien keine Probleme mit `bin`, `obj`, AppHost-Dateien oder Dateizeitstempeln bekommt, wird eine MSBuild-Konfiguration in den Container eingebunden:

```text
dotnet/ContainerBuild.props -> /dotnet-config/ContainerBuild.props
```

Compose setzt dazu die Umgebungsvariable `DirectoryBuildPropsPath`. Dadurch wird die Konfiguration sehr früh im MSBuild-Ablauf geladen. Repo-eigene `Directory.Build.props`-Dateien werden von `ContainerBuild.props` weiter importiert, damit projektspezifische Einstellungen erhalten bleiben.

Die Build-Artefakte liegen nicht unter `/rider-projects`, sondern im Linux-Volume `/dotnet-build`. Das verhindert typische Fehler wie `Access to the path ... obj ... is denied` oder Fehler beim Erstellen von `apphost`.

### .NET und C# im Container nutzen

Shell im Container öffnen:

```bash
docker compose exec ade bash
```

Mit Podman: `podman compose exec ade bash` oder `podman-compose exec ade bash`.

.NET-Version prüfen:

```bash
dotnet --info
```

Beispiel für ein neues Konsolenprojekt:

```bash
cd /rider-projects
dotnet new console -n DemoApp
cd DemoApp
dotnet run
```

`dotnet new console` erstellt eine einfache Konsolenanwendung. `dotnet run` baut und startet das Projekt. Die Dateien liegen auf dem Host im `RIDER_PROJECTS_DIR`-Verzeichnis und können dort mit Rider geöffnet werden.

Wenn ein Projekt bereits fehlerhafte `bin`- oder `obj`-Ordner auf dem Windows-Mount hat, können diese in Rider oder im Terminal gelöscht werden. Danach erneut im Container bauen.

### Java-Projekte einbinden

Das Host-Verzeichnis für Java-Projekte wird über `JAVA_PROJECTS_DIR` gesetzt. In einer WSL2-Umgebung ist ein typischer Wert:

```text
JAVA_PROJECTS_DIR=/mnt/c/Users/<benutzer>/JavaProjects
```

Das Verzeichnis wird im Container hier eingebunden:

```text
/java-projects
```

So bleiben .NET-/Rider-Projekte und Java-Projekte getrennt:

- `/rider-projects`: .NET-, C#- und Rider-Projekte.
- `/java-projects`: Java-, Maven- und Spring-Boot-Projekte.
- `/workspace`: allgemeine Übungen, zum Beispiel für Go-, Rust- oder Python-Projekte.

### Java und Maven im Container nutzen

Java-Version prüfen:

```bash
java --version
javac --version
mvn --version
```

Beispiel für ein neues Maven-Projekt:

```bash
cd /java-projects
mvn archetype:generate -DgroupId=de.example -DartifactId=demo-java -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
cd demo-java
mvn test
```

Spring-Boot-Projekte werden normalerweise über Maven oder einen Projekt-Wrapper gestartet, zum Beispiel:

```bash
mvn spring-boot:run
```

Gradle und Spring Boot CLI sind absichtlich nicht global installiert. Viele Unternehmensprojekte bringen ihren eigenen Maven- oder Gradle-Wrapper mit. Das ist reproduzierbarer als globale Werkzeugversionen.

### Go im Container nutzen

Go-Version und Go-Werkzeuge prüfen:

```bash
go version
gopls version
staticcheck -version
govulncheck -version
dlv version
```

Beispiel für ein kleines Go-Projekt:

```bash
cd /workspace
mkdir -p demo-go
cd demo-go
go mod init example.com/demo-go
cat > main.go <<'EOF'
package main

import "fmt"

func main() {
    fmt.Println("Hello from Go")
}
EOF
gofmt -w main.go
go test ./...
go run .
```

Go-Webframeworks werden nicht global installiert. Für erste Webübungen reicht die Standardbibliothek `net/http`. Frameworks wie `gin`, `fiber` oder `chi` gehören projektlokal in `go.mod`.

Für eigene Host-Projekte gibt es zusätzlich den konfigurierbaren Mount `/go-projects` (Variable `GO_PROJECTS_DIR`), analog zu `/java-projects`. `/workspace` ist der einfache Standard für schnelle Übungen.

### Rust im Container nutzen

Rust-Version und Rust-Werkzeuge prüfen:

```bash
rustc --version
cargo --version
rustfmt --version
cargo clippy --version
rust-analyzer --version
```

Beispiel für ein kleines Rust-Projekt:

```bash
cd /workspace
cargo new demo-rust
cd demo-rust
cargo fmt
cargo clippy -- -D warnings
cargo run
```

Rust-Webframeworks werden nicht global installiert. Frameworks und Laufzeiten wie `tokio`, `axum`, `actix-web` oder `serde` gehören projektlokal in `Cargo.toml`.

Für eigene Host-Projekte gibt es zusätzlich den konfigurierbaren Mount `/rust-projects` (Variable `RUST_PROJECTS_DIR`), analog zu `/java-projects`. `/workspace` ist der einfache Standard für schnelle Übungen.

### Python im Container nutzen

Python-Version und Werkzeuge prüfen:

```bash
python --version
python3 --version
uv --version
```

Im Container sind `python` und `python3` dasselbe Python 3. Zusätzlich ist `uv` installiert, ein schnelles Werkzeug für virtuelle Umgebungen und Pakete.

Beispiel für ein kleines Python-Programm mit Test:

```bash
cd /workspace
mkdir -p demo-python
cd demo-python
cat > main.py <<'EOF'
def greet(name: str) -> str:
    return f"Hallo aus Python, {name}"


if __name__ == "__main__":
    print(greet("ADE"))
EOF
cat > test_main.py <<'EOF'
import unittest

from main import greet


class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("ADE"), "Hallo aus Python, ADE")


if __name__ == "__main__":
    unittest.main()
EOF
python main.py
python -m unittest
```

`unittest` ist Teil der Standardbibliothek und braucht keine Installation. Für zusätzliche Pakete sollte eine virtuelle Umgebung genutzt werden, damit nichts global installiert wird. Das Paket `python3-venv` ist im Image vorhanden:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install pytest
pytest
deactivate
```

`pip install` lädt aus dem Netz und funktioniert nur mit Internetzugang. Alternativ und moderner verwaltet `uv` Umgebung und Pakete in einem Schritt, zum Beispiel mit `uv init` und `uv run`.

Python-Webframeworks werden nicht global installiert. Frameworks wie `flask`, `django` oder `fastapi` gehören projektlokal in die virtuelle Umgebung oder in `pyproject.toml`.

Für eigene Host-Projekte gibt es zusätzlich den konfigurierbaren Mount `/python-projects` (Variable `PYTHON_PROJECTS_DIR`), analog zu `/java-projects`. `/workspace` ist der einfache Standard für schnelle Übungen.

### Skripte mit Bash und PowerShell

Bash ist die Standard-Shell **im Container**. PowerShell ist hier die Shell **auf dem Windows-Host**, mit der die Container-Befehle (`docker`/`podman`) ausgeführt werden. `pwsh` ist im Linux-Container standardmäßig nicht installiert. Deshalb laufen Bash-Skripte im Container und PowerShell-Skripte auf dem Host.

Für Bash-Skripte sind `shellcheck` (Prüfung) und `shfmt` (Formatierung) installiert.

Bash-Version und Werkzeuge prüfen:

```bash
bash --version
shellcheck --version
shfmt --version
```

Beispiel für ein kleines Bash-Skript im Container:

```bash
cd /workspace
mkdir -p demo-bash
cd demo-bash
cat > hello.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

greet() {
  local name="$1"
  echo "Hallo aus Bash, ${name}"
}

greet "ADE"
EOF
shfmt -w hello.sh
shellcheck hello.sh
chmod +x hello.sh
./hello.sh
```

`shfmt -w` formatiert das Skript, `shellcheck` prüft es auf typische Fehler, danach wird es ausführbar gemacht und gestartet.

PowerShell-Version auf dem Windows-Host prüfen:

```powershell
$PSVersionTable.PSVersion
```

Beispiel für ein kleines PowerShell-Skript auf dem Host:

```powershell
Set-Location $HOME
New-Item -ItemType Directory -Force demo-powershell | Out-Null
Set-Location demo-powershell
@'
function Get-Greeting {
    param([string]$Name)
    "Hallo aus PowerShell, $Name"
}

Get-Greeting -Name "ADE"
'@ | Set-Content hello.ps1
.\hello.ps1
```

Wenn das Ausführen blockiert wird, die Ausführungsrichtlinie prüfen: `Get-ExecutionPolicy` und bei Bedarf `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`. Im Container selbst werden Skripte mit Bash geschrieben.

### ASP.NET-Web-App vom Host erreichen

Der Container gibt die lokale Port-Range `5100-5199` an den Host frei:

```yaml
ports:
  - "127.0.0.1:5100-5199:5100-5199"
```

Nach einer Änderung an `compose.yml` muss der Container neu erstellt werden:

```bash
cd /Users/<benutzer>/ade-dev-sandbox
docker compose up -d --force-recreate
docker compose exec ade bash
```

Mit Podman: `podman compose up -d --force-recreate` und `podman compose exec ade bash` (oder jeweils `podman-compose ...`).

Eine ASP.NET-App muss im Container auf `0.0.0.0` lauschen. `localhost` reicht nicht, weil `localhost` im Container nur den Container selbst meint.

Beispiel für eine Razor-Pages-Web-App:

```bash
cd /rider-projects
dotnet new webapp -n WebApp1
cd WebApp1
dotnet run --urls http://0.0.0.0:5102
```

Danach auf dem Host im Browser öffnen:

```text
http://localhost:5102
```

Beispiel für eine minimale ASP.NET-App:

```bash
cd /rider-projects
dotnet new web -n MinimalWebApp1
cd MinimalWebApp1
dotnet run --urls http://0.0.0.0:5103
```

Danach auf dem Host im Browser öffnen:

```text
http://localhost:5103
```

Der Unterschied: `dotnet new webapp` erstellt eine Web-App mit Razor Pages und mehr Projektstruktur. `dotnet new web` erstellt eine sehr kleine ASP.NET-App, die gut zum Verstehen des Grundprinzips ist.

Wenn eine App einen anderen Port nutzt, muss dieser in der freigegebenen Range `5100-5199` liegen oder in `compose.yml` zusätzlich eingetragen werden.

### Spec Kit verwenden

Spec Kit ist im Container als `specify` installiert. Die Installation erfolgt im Dockerfile mit der offiziellen GitHub-Quelle und ist auf Version `v0.8.3` gepinnt:

```dockerfile
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.3
```

Version und Umgebung prüfen:

```bash
specify version
specify check
```

Ein vorhandenes Projekt kann vorbereitet werden, nachdem in sein Verzeichnis gewechselt wurde:

```bash
cd /rider-projects/TinyPl0
specify init . --integration opencode --force
```

Falls eine Integration nicht verfügbar ist, zuerst die unterstützten Optionen prüfen:

```bash
specify init --help
```

Wenn Spec Kit nach dem Script-Typ fragt, für diesen Linux-Container `sh` auswählen.

Spec Kit weist darauf hin, dass Agentenordner private Daten enthalten können. Für Projekte unter `/rider-projects` sollte deshalb im jeweiligen Anwendungsrepo geprüft werden, ob `.opencode/` oder sensible Teile davon in die Projekt-`.gitignore` gehören.

Spec Kit erzeugt Projektdateien für spec-driven development. Diese Dateien gehören normalerweise in das jeweilige Anwendungsrepo unter `/rider-projects`, nicht in dieses Docker-Setup-Repo.

### Opencode verwenden

Opencode im Container starten:

```bash
opencode
```

Der Container startet Opencode nicht automatisch. Das ist Absicht. So kann zuerst entschieden werden, in welchem Projektverzeichnis gearbeitet wird.

Für Sicherheits- und Architekturprüfungen gibt es den read-only-Agenten `security-review`. Er ist für Reviews gedacht und darf keine Dateien ändern.

Interaktiv im Projekt starten:

```bash
cd /rider-projects/MeinProjekt
opencode --agent security-review
```

Dann im Prompt eine konkrete Prüffrage stellen, zum Beispiel:

```text
Prüfe dieses Projekt auf Sicherheitsrisiken, unsichere Konfiguration, Secret-Leaks und Architekturprobleme. Ändere keine Dateien, sondern liefere Findings mit Datei- und Zeilenhinweisen.
```

Als einmaligen nicht-interaktiven Review-Lauf:

```bash
cd /rider-projects/MeinProjekt
opencode run --agent security-review "Prüfe dieses Projekt auf Sicherheitsrisiken, unsichere Konfiguration, Secret-Leaks und Architekturprobleme. Ändere keine Dateien, sondern liefere Findings mit Datei- und Zeilenhinweisen."
```

Wenn aus einem Finding eine Änderung entstehen soll, danach bewusst mit dem normalen `coding`-Agenten oder manuell umsetzen. `security-review` ist absichtlich auf Analyse begrenzt.

### Codex CLI verwenden

Codex CLI ist ebenfalls im Container installiert:

```bash
codex --version
```

Codex startet nicht automatisch. Für ein Projekt zuerst in das Projektverzeichnis wechseln und dann Codex starten:

```bash
cd /rider-projects/MeinProjekt
codex
```

Lokale Codex-Daten liegen im Docker-Volume `codex_data` unter `/home/adedev/.codex`. Dieses Volume ist nicht Teil des Git-Repositories. Zugangsdaten und private Sitzungsdaten dürfen nicht in Projektordner kopiert oder committed werden.

### Spec-Kit-Governance-Presets installieren

Nach `specify init` können die sechs Governance-Presets in einem Projekt installiert werden. Die Presets erweitern Spec Kit um verbindliche Regeln für sichere Entwicklung, Softwarearchitektur, iSAQB/arc42, Barrierefreiheit, Plattform-Parität und KI-Agenten-Parität.

Für C#/.NET-Level-2-Projekte ist in der home-baseline-Umgebung die Standardentscheidung: alle sechs Presets installieren, sofern das Projekt keine begründete Ausnahme dokumentiert.

Die Befehle werden im jeweiligen Projektverzeichnis im Container ausgeführt, also zum Beispiel unter `/rider-projects/TinyPl0`:

```bash
cd /rider-projects/TinyPl0

specify preset add --from https://github.com/hindermath/spec-kit-preset-security-governance/archive/refs/tags/v0.2.0.zip --priority 10
specify preset add --from https://github.com/hindermath/spec-kit-preset-architecture-governance/archive/refs/tags/v0.2.0.zip --priority 20
specify preset add --from https://github.com/hindermath/spec-kit-preset-isaqb-architecture-governance/archive/refs/tags/v0.1.0.zip --priority 30
specify preset add --from https://github.com/hindermath/spec-kit-preset-a11y-governance/archive/refs/tags/v0.2.0.zip --priority 40
specify preset add --from https://github.com/hindermath/spec-kit-preset-cross-platform-governance/archive/refs/tags/v0.1.0.zip --priority 50
specify preset add --from https://github.com/hindermath/spec-kit-preset-agent-parity-governance/archive/refs/tags/v0.1.0.zip --priority 60
```

Die Priorität steuert, welches Preset bei gleichen Template-Bausteinen zuerst wirkt. Kleinere Zahl bedeutet höhere Priorität. Deshalb steht `security-governance` auf `10`.

Installation prüfen:

```bash
specify preset list
specify preset info security-governance
specify preset resolve constitution-template.md
specify preset resolve agent-guidance-addendum-template.md
git status --short
```

Wenn das Projekt die Presets dauerhaft nutzen soll, werden die Preset-Dateien und die erzeugten Agenten-/Command-Dateien im Anwendungsrepo committed und gepusht:

```bash
git add .specify/presets .agents .claude .gemini .github .opencode
git commit -m "chore: configure spec-kit governance presets"
git push
```

Wichtig: `.specify/presets/` gehört dann zur Projekt-Policy. Lokale Caches wie `.specify/presets/.cache/` sollten nicht committed werden.

### Beispiel: ConsoleApp2 mit Opencode und Spec Kit

Dieses Beispiel zeigt den kompletten Einstieg für eine neue Konsolenanwendung. Es wird im Container ausgeführt.

```bash
cd /rider-projects
dotnet new console -n ConsoleApp2
cd ConsoleApp2
dotnet run
```

Danach Opencode einmal im Projekt initialisieren. Dadurch kann Opencode projektspezifische Regeln erkennen oder anlegen:

```bash
opencode --prompt "/init"
```

Danach Spec Kit für Opencode einrichten:

```bash
specify init . --integration opencode --force
```

Wenn Spec Kit nach dem Script-Typ fragt, `sh` auswählen. Nach erfolgreicher Initialisierung stehen in Opencode die Slash-Commands `/speckit.*` zur Verfügung.

Wenn das Projekt mit Git verwaltet wird, prüfen:

```bash
git status --short
```

Danach entscheiden, ob `.opencode/` vollständig versioniert werden soll oder ob sensible Teile in die Projekt-`.gitignore` gehören.

### Pilot: ASP.NET-Web-App mit Opencode und Spec Kit

Für C#/.NET-Projekte unter `/rider-projects` ist dieser Pilotablauf ein gutes erstes End-to-End-Beispiel. Er erzeugt eine kleine Razor-Pages-Web-App, initialisiert Opencode, initialisiert Spec Kit und führt danach die Projekt-Constitution aus.

```bash
cd /rider-projects
mkdir -p specify-pilot
cd specify-pilot

dotnet new webapp -n SpecifyPilot -o . --force
dotnet restore
dotnet build --no-restore
```

Danach Opencode im Projekt starten und das Init-Kommando ausführen:

```bash
opencode
```

Im Opencode-Prompt:

```text
/init
```

Wenn Opencode fragt, ob es `AGENTS.md` anlegen oder ändern darf, nur Dateien im aktuellen Pilotprojekt freigeben. Danach Spec Kit für Opencode initialisieren:

```bash
specify init . --integration opencode --script sh --force
```

Dann die sechs Governance-Presets aus dem Abschnitt [Spec-Kit-Governance-Presets installieren](#spec-kit-governance-presets-installieren) installieren und prüfen:

```bash
specify preset list
```

Zum Abschluss Opencode erneut starten und die Spec-Kit-Constitution erzeugen:

```bash
opencode
```

Im Opencode-Prompt:

```text
/speckit.constitution
```

Eine sinnvolle kurze Eingabe ist:

```text
Projektname: SpecifyPilot. Projekttyp: ASP.NET Core Razor Pages Web App in der ADE-Lernumgebung. Ziel: minimale, auditierbare Pilot-Constitution für Auszubildende und Kolleg:innen.
```

Danach sollten mindestens diese Dateien vorhanden sein:

```bash
test -f AGENTS.md
test -f .specify/memory/constitution.md
test -d .opencode/command
test -d .specify/presets
dotnet build --no-restore
```

Die Pilot-Evidenz für dieses Repository ist in `docs/security/spec-kit-pilot.md` dokumentiert. Das Pilotprojekt selbst bleibt im Anwendungsbereich unter `/rider-projects/specify-pilot` und wird nicht in dieses Docker-Setup-Repository übernommen.

### Pflichtablauf für ein SDD-Feature

SDD bedeutet spec-driven development. Ein Feature wird zuerst beschrieben, dann geplant, dann in Aufgaben zerlegt und erst danach implementiert. Für die Ausbildung werden auch die Qualitätsschritte immer ausgeführt.

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
- `/speckit.clarify`: offene Fragen klären, bevor technische Planung beginnt.
- `/speckit.plan`: technische Umsetzung planen.
- `/speckit.checklist`: Anforderungen auf Vollständigkeit und Klarheit prüfen.
- `/speckit.tasks`: konkrete umsetzbare Aufgaben erzeugen.
- `/speckit.analyze`: Konsistenz zwischen Spezifikation, Plan und Aufgaben prüfen.
- `/speckit.implement`: Aufgaben umsetzen.

Nach der Implementierung immer ausführen:

```bash
dotnet test
dotnet run
```

Wenn das Projekt keine Tests enthält, mindestens `dotnet build` ausführen und in der Dokumentation notieren, warum keine Tests vorhanden sind.

### Konfiguration

`opencode.jsonc` nutzt den Provider `chat-ai` mit dieser Basis-URL:

```text
https://chat-ai.academiccloud.de/v1
```

Der API-Key wird aus `GWDG_API_KEY` gelesen. Das Standardmodell für normale Coding-Aufgaben ist:

```text
chat-ai/qwen3-coder-30b-a3b-instruct
```

Der Standard-Agent `coding` nutzt dieses Modell mit fokussierten Coding-Parametern. `glm-4.7` bleibt als kleineres Modell für Nebenaufgaben und als Alternative für Analyse und Brainstorming konfiguriert.

#### OpenCode-Härtung

Die Datei `opencode.jsonc` enthält Sicherheitsregeln für OpenCode. Das ist wichtig, weil OpenCode ohne eigene `permission`-Regeln viele Aktionen standardmäßig erlaubt. In einer Umgebung mit ISO-9001- und ISO-27001-Anforderungen sollen riskante Aktionen deshalb nicht ohne bewusste Freigabe laufen.

Die wichtigsten Einstellungen:

- `share` steht auf `disabled`. OpenCode darf keine Sitzungen als öffentliche Links teilen.
- `autoupdate` steht auf `false`. Updates erfolgen kontrolliert über Dockerfile, Git-Commit und Image-Build.
- `enabled_providers` enthält nur `chat-ai`. Andere automatisch erkannte Provider werden nicht verwendet.
- `permission` setzt als Grundregel `ask`. OpenCode fragt also nach, wenn keine engere Regel greift.
- Lesen, Suchen und Listen im Projekt sind erlaubt. Das ist für Code-Analyse nötig.
- Echte Secret-Dateien und lokale Tool-Daten sind für Lesen und Schreiben gesperrt, zum Beispiel `.env`, `opencode.env`, `codex.env`, `~/.ssh`, GitHub-/GitLab-CLI-Konfiguration, Docker-/Podman-Konfiguration, Codex-Daten und OpenCode-Daten.
- Datei-Änderungen stehen auf `ask`. OpenCode darf also nicht still Dateien schreiben.
- Shell-Kommandos stehen grundsätzlich auf `ask`. Einfache Statusbefehle wie `pwd`, `ls`, `git status`, `git diff`, `git log` und `git show` sind erlaubt.
- Destruktive Kommandos wie `rm`, `sudo`, `su`, `dd`, `mkfs`, `mount` und `umount` sind gesperrt.
- Netzwerkzugriffe über OpenCode-Werkzeuge wie `webfetch`, `websearch` und `codesearch` fragen nach.
- Der Agent `security-review` ist für Sicherheits- und Architekturprüfungen gedacht. Er ist read-only und darf keine Dateien ändern.

Wenn `opencode.jsonc` geändert wird, gibt es zwei Wege:

```bash
CONTAINER_NAME=$(podman ps --filter name=ade-dev-sandbox --format '{{.Names}}' | head -n 1)
podman cp opencode.jsonc "${CONTAINER_NAME}:/home/adedev/.config/opencode/opencode.jsonc"
podman exec --user root "$CONTAINER_NAME" chown adedev:adedev /home/adedev/.config/opencode/opencode.jsonc
```

Mit Docker statt Podman gelten dieselben Schritte mit `docker compose cp` und `docker compose exec --user root ade ...`.

Dieser Weg aktualisiert den laufenden Container sofort. Er ändert aber nicht das bereits gebaute Image. Für neue Container muss das Image neu gebaut werden:

```bash
podman compose build --pull
podman compose up -d --force-recreate
```

Nach einer Änderung kann die geladene Konfiguration geprüft werden:

```bash
opencode debug config
opencode debug agent coding
opencode debug agent security-review
```

#### Codex-Härtung

Codex CLI wird ebenfalls gehärtet. Die Konfiguration liegt im Repository unter `codex/config.toml` und `codex/requirements.toml`. Beim Image-Build werden diese Dateien systemweit nach `/etc/codex` kopiert.

Die wichtigsten Einstellungen in `codex/config.toml`:

- `approval_policy = "untrusted"`: Codex darf nur einen kleinen Satz vertrauenswürdiger Basisbefehle ohne Rückfrage ausführen.
- `sandbox_mode = "workspace-write"`: Codex darf innerhalb der vorgesehenen Arbeitsbereiche schreiben, aber nicht mit Vollzugriff laufen.
- `web_search = "disabled"`: Websuche ist standardmäßig deaktiviert.
- `check_for_update_on_startup = false`: Updates erfolgen kontrolliert über Dockerfile und Image-Build.
- `history.persistence = "none"`: Session-Transkripte werden nicht dauerhaft gespeichert.
- `otel.exporter = "none"` und `log_user_prompt = false`: Es wird keine Telemetrie exportiert und Prompts werden nicht geloggt.
- `sandbox_workspace_write.network_access = false`: Shell-Kommandos in der Sandbox haben keinen direkten Netzwerkzugriff.
- `sandbox_workspace_write.exclude_slash_tmp = true`: `/tmp` wird nicht automatisch beschreibbar.
- `sandbox_workspace_write.writable_roots`: Schreibrechte sind auf `/workspace`, `/rider-projects`, `/java-projects`, `/go-projects`, `/rust-projects` und `/python-projects` begrenzt.
- `shell_environment_policy.inherit = "core"`: Subprozesse erben nur eine reduzierte Umgebung.
- Secret-Variablen mit Namen wie `*KEY*`, `*SECRET*`, `*TOKEN*`, `*PASSWORD*` und `*CREDENTIAL*` werden aus Subprozessen entfernt.
- App-, Browser- und Computer-Use-Flächen sind deaktiviert.

Die Datei `codex/requirements.toml` setzt Schranken, die normale Benutzer- oder Projektkonfiguration nicht abschwächen darf:

- `allowed_approval_policies = ["untrusted", "on-request"]`: Der Modus `never` ist nicht erlaubt.
- `allowed_sandbox_modes = ["read-only", "workspace-write"]`: `danger-full-access` ist nicht erlaubt.
- `allowed_web_search_modes = []`: Nur deaktivierte Websuche ist erlaubt.
- Secret-Dateien und lokale Tool-Daten sind für Codex gesperrt, zum Beispiel `.env`, `opencode.env`, `codex.env`, `~/.ssh`, Docker-/Podman-Konfiguration, Codex-Daten und OpenCode-Daten.
- Gefährliche Shell-Prefixe wie `rm`, `sudo`, `su`, `dd`, `mkfs`, `mount` und `umount` sind verboten.
- Git-Schreibaktionen, Container-Befehle, Netzwerkabrufe und Build-/Paketmanager-Befehle verlangen eine Rückfrage.

`codex/config.toml` wird absichtlich nicht nach `/home/adedev/.codex/config.toml` kopiert. Dieses Verzeichnis wird durch das persistente Docker-/Podman-Volume `codex_data` überlagert. Eine Datei im Image wäre dort bei laufendem Compose-Setup nicht sichtbar.

Für eine dauerhafte Änderung muss das Image neu gebaut und der Container neu erzeugt werden:

```bash
podman compose build --pull
podman compose up -d --force-recreate
```

Für einen laufenden Container können die Konfigurationsdateien testweise kopiert werden. Das ersetzt keinen Image-Build und installiert auch kein neues Paket wie `bubblewrap`:

```bash
CONTAINER_NAME=$(podman ps --filter name=ade-dev-sandbox --format '{{.Names}}' | head -n 1)
podman exec --user root "$CONTAINER_NAME" mkdir -p /etc/codex
podman cp codex/config.toml "${CONTAINER_NAME}:/etc/codex/config.toml"
podman cp codex/config.toml "${CONTAINER_NAME}:/etc/codex/managed_config.toml"
podman cp codex/requirements.toml "${CONTAINER_NAME}:/etc/codex/requirements.toml"
podman exec --user root "$CONTAINER_NAME" chmod 0644 /etc/codex/config.toml /etc/codex/managed_config.toml /etc/codex/requirements.toml
```

Mit Docker statt Podman gelten dieselben Schritte mit `docker compose cp` und `docker compose exec --user root ade ...`.

Nach einer Änderung kann die wirksame Sandbox grob geprüft werden:

```bash
codex debug prompt-input "Test"
```

In der Ausgabe sollten `sandbox_mode` als `workspace-write`, Netzwerkzugriff als eingeschränkt und die Writable-Roots `/workspace`, `/rider-projects`, `/java-projects`, `/go-projects`, `/rust-projects` und `/python-projects` sichtbar sein.

Java JDK 21 und Maven werden beim Image-Build aus den Debian-Paketquellen installiert. Sie sind für Java-Grundlagen, Maven-Projekte und Spring-Boot-Projekte vorbereitet.

Go wird beim Image-Build als offizielles Go-Tarball nach `/usr/local/go` installiert. Die Version ist im Dockerfile über `GO_VERSION` gepinnt, damit Updates bewusst über eine Dockerfile-Änderung, einen Git-Commit und einen neuen Image-Build erfolgen. Zusätzlich werden `gopls`, `staticcheck`, `govulncheck` und `dlv` in `/home/adedev/go/bin` installiert; auch diese Werkzeugversionen sind über Dockerfile-Build-Argumente gepinnt.

Rust wird beim Image-Build mit `rustup` für den Linux-Benutzer `adedev` installiert. Die Toolchain ist im Dockerfile über `RUST_TOOLCHAIN` gepinnt. Installiert werden außerdem die Komponenten `rustfmt`, `clippy`, `rust-analyzer` und `rust-src`.

OpenCode und Codex CLI werden beim Image-Build als konkret gepinnte npm-Pakete installiert. Die Versionen stehen im Dockerfile in `OPENCODE_VERSION` und `CODEX_VERSION`; Updates erfolgen bewusst über Dockerfile-Änderung, Git-Commit und neuen Image-Build:

```dockerfile
ARG OPENCODE_VERSION=1.14.50
ARG CODEX_VERSION=0.130.0
RUN npm i -g "opencode-ai@${OPENCODE_VERSION}" "@openai/codex@${CODEX_VERSION}"
```

Zusätzlich installiert das Image häufig genutzte CLI-Werkzeuge für Agenten-Workflows: `git`, `python`, `python3`, `jq`, `yq`, `rg`, `fd`, `fdfind`, `direnv`, `shellcheck`, `shfmt`, `delta`, `tree`, `just`, `wget`, `curl` und `bubblewrap`. Das Debian-Paket für `fd` heißt `fd-find` und liefert den Befehl `fdfind`; das Image legt zusätzlich den erwarteten Befehl `fd` als Symlink an. `bubblewrap` wird für die Linux-Sandbox von Codex installiert. `mas` ist ein macOS-App-Store-Werkzeug und wird im Linux-Container nicht installiert.

Der `PATH` enthält zusätzlich `/usr/local/go/bin`, `/home/adedev/go/bin` und `/home/adedev/.cargo/bin`. Dadurch sind Go, Go-Zusatzwerkzeuge und Rust-Werkzeuge nach dem Öffnen einer Container-Shell direkt verfügbar.

Codex CLI speichert lokale Daten im Docker-Volume `codex_data`. Dieses Volume wird im Container nach `/home/adedev/.codex` eingebunden. Dadurch bleiben Codex-Daten zwischen Container-Neustarts erhalten, ohne dass sie in das Git-Repository geschrieben werden.

Spec Kit wird beim Image-Build mit `uv` installiert. Dafür enthält das Image auch `git`, `curl` und `ca-certificates`.

Nach der Installation wird Spec Kit im Container gepatcht. Der Patch verhindert, dass Python-Kopiervorgänge Datei- oder Verzeichnis-Metadaten wie Rechte oder Zeitstempel auf Host-Bind-Mounts übernehmen wollen. Das ist wichtig, weil Windows- und WSL-Mounts solche Metadatenoperationen mit `Operation not permitted` ablehnen können.

Die .NET-Workload-Hinweismeldung wird im Container deaktiviert:

```text
DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=true
MSBuildEnableWorkloadResolver=false
```

Die erste Variable betrifft allgemeine Update-Benachrichtigungen. Die zweite Variable deaktiviert den MSBuild-Workload-Resolver. Das ist für normale Konsolen-, Library-, Test- und Web-Projekte sinnvoll, weil dort keine optionalen SDK-Workloads wie MAUI gebraucht werden.

Das Image erbt vom gemeinsamen `agent-sandbox`-Image auf Debian 13. Das Basisimage ist im Dockerfile per `sha256`-Digest gepinnt; der lesbare `latest`-Tag bleibt nur als Kommentar mit Beobachtungsdatum erhalten. Ein Update des Basisimages erfolgt bewusst über Digest-Änderung im Dockerfile, Review, Git-Commit und neuen Image-Build. .NET wird über die Microsoft-Paketquelle für Debian 13 installiert. Der Build-Parameter `DOTNET_SDK_PACKAGE` steht standardmäßig auf `dotnet-sdk-10.0`.

Die Sicherheitsfreigabe wird in `docs/security/sandbox-freigabe.md` als Entwurf dokumentiert. Die MR/PR-Anleitung fuer CISO/ISB oder KI-Beauftragte:n (KIB) liegt in `docs/security/sandbox-freigabe-review.md`. Der Isolationsnachweis liegt in `docs/security/sandbox-isolation.md`. Das zugehörige KI-Werkzeug-Inventar liegt in `docs/security/ai-tools-inventory.md`. Offene `_TODO_`-Felder müssen durch Owner, Betrieb, CISO/ISB oder KIB gepflegt werden und werden nicht durch Annahmen ersetzt.

#### Secret-Scanning

Dieses Repository nutzt `pre-commit` mit `gitleaks` `v8.30.1`, um Klartext-Geheimnisse vor Commits zu finden. Vor der Arbeit einmalig den Hook installieren:

```bash
uv tool install pre-commit
pre-commit install
```

Vor einem Commit oder als Vollscan:

```bash
pre-commit run --all-files
```

Wenn `pre-commit` nicht installiert ist, kann der Vollscan auch ohne dauerhafte Installation laufen:

```bash
uvx pre-commit run --all-files
```

Die Gitleaks-Konfiguration liegt in `.gitleaks.toml`. Sie erweitert die Standardregeln und erlaubt nur dokumentierte Platzhalterwerte in Beispiel-Dateien wie `opencode.env.example`. Echte Secrets dürfen nicht allowlisted werden. Die Audit-Notiz steht zusätzlich in `docs/security/secret-scanning.md`.

GitLab CE kann diesen lokalen Hook nicht vollständig serverseitig erzwingen. Audit-Text: "Client-side Control, in GitLab CE nicht vollständig serverseitig erzwingbar; zentrale Push-Blockade nur mit GitLab Ultimate Secret Push Protection oder Admin-Server-Hook." Als zusätzliche Kontrolle enthält `.gitlab-ci.yml` einen `secret_scan`-Job mit demselben gepinnten Gitleaks-Release. Dieser CI-Job erkennt Secrets nach dem Push bzw. im Merge Request, ersetzt aber keine zentrale Pre-Receive-Blockade.

#### Audit-Export

Agentennutzung muss als Metadaten-Audit nachvollziehbar sein. Das Image installiert deshalb `audit-export` aus `scripts/audit-export.sh`. Der Compose-Service bindet `${AUDIT_DIR:-./audit-logs}` nach `/audit` ein.

Der Export liest nur Dateinamen und Dateizeitstempel aus den OpenCode- und Codex-Datenverzeichnissen. Er liest keine Prompt-Texte, Antwort-Texte, Roh-Sitzungsinhalte oder API-Keys.

Mindestens einmal pro Arbeitstag und zwingend vor dem Entfernen der Container-Volumes ausführen. Der dokumentierte Standardweg zum Beenden ist der Wrapper, weil er zuerst `audit-export` im laufenden Container startet und danach `compose down` ausführt.

Windows PowerShell mit Podman:

```powershell
.\scripts\compose-down-with-audit.ps1 -Engine podman
.\scripts\compose-down-with-audit.ps1 -Engine podman -Volumes
```

macOS/Linux mit Podman oder Docker:

```bash
bash scripts/compose-down-with-audit.sh --podman
bash scripts/compose-down-with-audit.sh --podman -v
bash scripts/compose-down-with-audit.sh --docker -v
```

Falls der Wrapper nicht genutzt werden kann, den Export manuell im Container ausführen und danach erst `docker compose down -v` oder `podman compose down -v` starten:

```bash
audit-export
```

Zusätzlich installiert das Image einen Best-Effort-Stop-Hook über `/usr/local/bin/ade-entrypoint`. Bei einem normalen `docker compose down`, `podman compose down` oder `SIGTERM` ruft der Entrypoint einmalig `audit-export` auf, sofern `ADE_AUDIT_ON_STOP=true` gesetzt ist. Dieser Hook ist eine zusätzliche Absicherung, ersetzt aber nicht den Wrapper: harte Kills, Host-Abbrüche oder sehr kurze Stop-Timeouts können den Export verhindern.

Der Standardpfad ist:

```text
/audit/YYYY-MM-DD.jsonl
```

Auf dem Host landet diese Datei standardmäßig unter `audit-logs/`. Echte Audit-JSONL-Dateien bleiben untracked; nur `audit-logs/README.md` und `audit-logs/.gitkeep` gehören ins Repository. Das README in `audit-logs/` beschreibt Inhalt, Zugriff, Aufbewahrung und Löschung.

Gegen die Meldung `An issue was encountered verifying workloads` wird beim Image-Build zusätzlich der Manifest-Modus gesetzt:

```dockerfile
RUN dotnet workload config --update-mode manifests \
    && dotnet workload update
```

Dieser Befehl läuft beim Image-Build als `root`, weil `dotnet workload config` erhöhte Rechte braucht. Normale .NET-Projekte können weiter gebaut und gestartet werden. Wenn ein Projekt echte Workloads wie MAUI oder spezielle WebAssembly-Tools braucht, müssen diese gezielt im Dockerfile ergänzt und `MSBuildEnableWorkloadResolver` wieder aktiviert werden.

Zusätzlich wird im Image ein schmaler Wrapper unter `/usr/local/bin/dotnet` installiert. Er ruft intern `/usr/bin/dotnet` auf und filtert nur diese bekannte Zeile aus der Fehlerausgabe:

```text
An issue was encountered verifying workloads. For more information, run "dotnet workload update".
```

Andere Warnungen, Fehler und der Exit-Code von `dotnet` bleiben erhalten.

### Image-SBOM erzeugen

Eine SBOM ist eine *Software Bill of Materials*, also eine maschinenlesbare Stückliste für Software. Für dieses Container-Image listet sie Betriebssystempakete, Bibliotheken, installierte Werkzeuge und Versionen auf. Das hilft bei Lieferkettentransparenz: Wenn später eine Schwachstelle in einer bestimmten Komponente bekannt wird, kann geprüft werden, ob das Image betroffen ist.

Für dieses Repository wird eine CycloneDX-JSON-SBOM erzeugt. Vor der Verteilung oder Übergabe eines neu gebauten Sandbox-Images ist dieser Schritt Pflicht.

Linux, macOS oder WSL2:

```bash
./scripts/build-and-sbom.sh
```

Windows PowerShell, zum Beispiel mit Podman:

```powershell
.\scripts\build-and-sbom.ps1 -Runtime podman
```

Wenn das Image bereits gebaut ist und nur die SBOM neu erzeugt werden soll:

```bash
./scripts/build-and-sbom.sh --skip-build
```

```powershell
.\scripts\build-and-sbom.ps1 -Runtime podman -SkipBuild
```

Die Skripte verwenden lokal installiertes `syft`, wenn es vorhanden ist. Wenn `syft` nicht im `PATH` liegt, nutzen sie als Fallback das Container-Image `docker.io/anchore/syft:latest`. Dafür muss Docker oder Podman öffentliche Images ziehen können.

Die erzeugten Dateien liegen unter `sboms/`, zum Beispiel `sboms/2026-05-17-localhost-ade-dev-sandbox-ade-latest.cdx.json`. Diese Dateien sind Build-Artefakte und werden durch `.gitignore` nicht committed. Für Releases können sie separat als Release-Artefakt abgelegt werden.

### Image-SBOM auswerten

Die SBOM kann mit den mitgelieferten Skripten lokal zusammengefasst und durchsucht werden. Ohne weitere Parameter wird die neueste Datei aus `sboms/*.cdx.json` verwendet.

Windows PowerShell:

```powershell
.\scripts\analyze-sbom.ps1
```

macOS, Linux oder WSL2:

```bash
./scripts/analyze-sbom.sh
```

Die Ausgabe zeigt Format, CycloneDX-Version, Erzeugungszeit, Anzahl der Komponenten, Komponententypen, Paket-Ökosysteme aus `purl` und erkannte Lizenzen.

Nach Komponenten suchen:

```powershell
.\scripts\analyze-sbom.ps1 -Search "openssl|dotnet|node|python|rust|go"
.\scripts\analyze-sbom.ps1 -ComponentType library -Search "openssl|dotnet|node|python|rust|go"
```

```bash
./scripts/analyze-sbom.sh --search 'openssl|dotnet|node|python|rust|go'
./scripts/analyze-sbom.sh --type library --search 'openssl|dotnet|node|python|rust|go'
```

Der Typfilter `library` blendet reine Datei-Einträge aus und ist meist die sinnvollste Sicht für Paket- und CVE-Fragen.

Eine bestimmte SBOM-Datei auswerten:

```powershell
.\scripts\analyze-sbom.ps1 -SbomPath .\sboms\2026-05-17-localhost-ade-dev-sandbox-ade-latest.cdx.json
```

```bash
./scripts/analyze-sbom.sh --file sboms/2026-05-17-localhost-ade-dev-sandbox-ade-latest.cdx.json
```

Optional kann ein Schwachstellenscan gegen die SBOM laufen, wenn `grype` oder `trivy` installiert ist:

```powershell
.\scripts\analyze-sbom.ps1 -Scan
.\scripts\analyze-sbom.ps1 -Scan -Scanner trivy
```

```bash
./scripts/analyze-sbom.sh --scan
./scripts/analyze-sbom.sh --scan --scanner trivy
```

Das Bash-Skript nutzt für die lokale Zusammenfassung `jq`, wenn verfügbar, und fällt sonst auf `python3` oder `python` zurück. Das PowerShell-Skript nutzt `ConvertFrom-Json` und benötigt für die Basis-Auswertung keine Zusatzwerkzeuge. Für CVE-Auswertungen ist eines der Scanner-Werkzeuge `grype` oder `trivy` erforderlich.

### Aufräumen

Container stoppen, Daten behalten:

```bash
docker compose down
```

Container stoppen und persistente Container- und Volume-Daten dieses Compose-Projekts löschen:

```bash
docker compose down -v
```

Diese Befehle gelten sinngemäß auf Linux, macOS und Windows. Entscheidend ist, ob die Umgebung mit Docker oder Podman gestartet wurde. Unter Windows können die Befehle in PowerShell, im Windows Terminal oder in WSL2 laufen. Wichtig ist nur, dass derselbe Container-Provider angesprochen wird, der die Container auch gestartet hat.

Vor dem Aufräumen zuerst anzeigen, wie viel Speicher Container, Images, Volumes und Build-Cache belegen:

```bash
docker system df
podman system df
```

Eine vorsichtige Bereinigung entfernt nur ungenutzte Daten, zum Beispiel gestoppte Container, ungenutzte Networks und nicht mehr verwendete Images oder Caches. Laufende Container und die von ihnen verwendeten Images und Volumes bleiben erhalten:

```bash
docker system prune
podman system prune
```

Mit `-a` werden zusätzlich alle ungenutzten Images entfernt, nicht nur unbenannte Zwischen-Images. Auch hier bleiben Images erhalten, die von laufenden Containern verwendet werden:

```bash
docker system prune -a
podman system prune -a
```

Gezieltes Aufräumen ist ebenfalls möglich:

```bash
docker container prune
docker image prune
docker builder prune

podman container prune
podman image prune
podman image prune --build-cache
```

Volumes sind der riskante Teil, weil dort persistente Daten liegen können, zum Beispiel `opencode_data`, `codex_data` und `dotnet_build`. Volumes nur löschen, wenn diese Daten bewusst entfernt werden sollen:

```bash
docker volume prune
podman volume prune
```

Die härteste Variante löscht ungenutzte Images, Container, Networks, Build-Cache und ungenutzte Volumes. Das ist nicht der normale Standardbefehl für dieses Projekt:

```bash
docker system prune -a --volumes
podman system prune -a --volumes
```

### Häufige Probleme

Wenn `docker compose` nicht gefunden wird, fehlt meist `docker-compose-v2`:

```bash
sudo apt install -y docker-compose-v2
```

Wenn Docker keine Berechtigung hat, entweder `sudo docker ...` verwenden oder den Benutzer zur Gruppe `docker` hinzufügen.

Wenn der API-Key nicht funktioniert, `opencode.env` prüfen. Den Key nicht im Terminalverlauf, in Screenshots oder in Git-Ausgaben zeigen.

Wenn `codex` oder `opencode` im Container mit `Permission denied` oder `EACCES` unter `/home/adedev/.codex` oder `/home/adedev/.local/share/opencode` abbrechen, gehören wahrscheinlich alte persistente Volumes noch einem früheren Container-Benutzer. Das kann nach einem Image- oder Basisimage-Wechsel passieren. Die Verzeichnisse im Image sind bereits für `adedev` angelegt; vorhandene Volumes überdecken diese Verzeichnisse aber und müssen einmalig korrigiert werden.

Für Podman auf macOS, Windows oder WSL2 zuerst den tatsächlichen Container-Namen ermitteln. Je nach Compose-Provider kann er zum Beispiel `ade-dev-sandbox-ade-1` oder `ade-dev-sandbox_ade_1` heißen:

```bash
CONTAINER_NAME=$(podman ps --filter name=ade-dev-sandbox --format '{{.Names}}' | head -n 1)
podman exec --user root "$CONTAINER_NAME" bash -lc 'chown -R adedev:adedev /home/adedev/.codex /home/adedev/.local/share/opencode'
```

Für Docker Compose:

```bash
docker compose exec --user root ade bash -lc 'chown -R adedev:adedev /home/adedev/.codex /home/adedev/.local/share/opencode'
```

Wenn Podman mit Meldungen wie `container name "ade-dev-sandbox-ade-1" is already in use`, `container name "ade-dev-sandbox_ade_1" is already in use`, `can only create exec sessions on running containers` oder `rootlessport listen tcp 127.0.0.1:5100: bind: address already in use` abbricht, läuft meist dieselbe Umgebung noch in einer anderen Podman-Machine oder ein alter Container belegt die Port-Range. Es darf nur eine Variante gleichzeitig laufen.

In WSL2 prüfen und stoppen:

```bash
podman-compose ps
podman-compose down
```

Unter Windows in PowerShell prüfen und stoppen:

```powershell
podman compose ps
podman compose down
```

Danach die gewünschte Seite neu starten. Beispiel für WSL2:

```bash
podman-compose up -d
```

Wenn .NET unter `/rider-projects` einen Fehler zu `obj`, `bin`, `apphost` oder `Access denied` meldet, den Container neu bauen und starten:

```bash
docker compose build --pull
docker compose up -d
```

Wenn der Fehler auf `/dotnet-build/...` zeigt, gehört wahrscheinlich das persistente Build-Volume noch einem früheren Container-Benutzer. Das kann nach einem Image- oder Basisimage-Wechsel passieren. Dann das Volume einmalig korrigieren:

```bash
CONTAINER_NAME=$(podman ps --filter name=ade-dev-sandbox --format '{{.Names}}' | head -n 1)
podman exec --user root "$CONTAINER_NAME" bash -lc 'chown -R adedev:adedev /dotnet-build'
```

Mit Docker Compose:

```bash
docker compose exec --user root ade bash -lc 'chown -R adedev:adedev /dotnet-build'
```

Danach im Container prüfen, ob die allgemeine MSBuild-Konfiguration und das Build-Volume vorhanden sind:

```bash
test "$DirectoryBuildPropsPath" = "/dotnet-config/ContainerBuild.props"
ls /dotnet-config/ContainerBuild.props
ls /dotnet-build
```

Wenn eine Warnung `MSB3539` zu `BaseIntermediateOutputPath` erscheint, läuft wahrscheinlich noch ein alter Container. Dann den Container neu erstellen:

```bash
docker compose up -d --force-recreate
```

Wenn danach ein Fehler wie `Duplicate TargetFrameworkAttribute` erscheint, liegen meist alte `obj`-Dateien im Windows-Projektordner. Diese Ordner einmal löschen und danach erneut bauen:

```bash
find /rider-projects/ConsoleApp1 -type d \( -name bin -o -name obj \) -prune -print
```

Wenn die Ausgabe nur erwartete Build-Ordner zeigt, können sie gelöscht werden:

```bash
find /rider-projects/ConsoleApp1 -type d \( -name bin -o -name obj \) -prune -exec rm -rf {} +
```

Wenn ein Fehler wie `Root element is missing` für `/rider-projects/Directory.Build.props` erscheint, liegt im Windows-Projektroot eine alte oder leere MSBuild-Datei. Diese Datei darf dort nicht mehr liegen. Prüfen:

```bash
ls -l /rider-projects/Directory.Build.props
```

Wenn die Datei leer oder unerwünscht ist, löschen:

```bash
rm /rider-projects/Directory.Build.props
```

### Kompakter Testablauf

Dieser Ablauf prüft das Setup in einer sinnvollen Reihenfolge. Er eignet sich gut nach einer Neuinstallation, nach Änderungen an `Dockerfile`, `compose.yml` oder `opencode.jsonc` und als erster Test auf macOS mit Docker Desktop.

> **Docker oder Podman:** Die Beispiele nutzen Docker. Mit Podman dieselben Schritte ausführen und `docker compose` durch `podman compose` oder `podman-compose` ersetzen (siehe [Docker und Podman: gleiche Befehle](#docker-und-podman-gleiche-befehle)).

Der Test besteht aus zwei Teilen:

1. Auf dem Host wird Docker Compose geprüft, das Image gebaut und der Container gestartet.
2. Im Container wird geprüft, ob .NET, Java, Go, Rust, Python, OpenCode, Spec Kit und die gemounteten Verzeichnisse funktionieren.

Auf dem Host ausführen. Der erste Befehl wechselt in dieses Repository; den Pfad bei Bedarf anpassen:

```bash
cd /home/<benutzer>/ade-dev-sandbox
docker compose config --no-interpolate
docker compose build --pull
docker compose up -d
docker compose ps
docker compose exec ade bash
```

Danach im Container prüfen:

```bash
dotnet --info
java --version
javac --version
mvn --version
go version
gopls version
rustc --version
cargo --version
cargo clippy --version
python --version
node --version
npm --version
opencode --version
codex --version
specify version
ls /workspace
ls /rider-projects
ls /java-projects
ls /go-projects
ls /rust-projects
ls /python-projects
```

Was die Befehle bedeuten:

- `docker compose config --no-interpolate` prüft die Compose-Datei, ohne Variablenwerte und Secrets in der Ausgabe auszubreiten.
- `docker compose build --pull` baut das Image und prüft bzw. lädt vorher nach Möglichkeit die gepinnten Basisimages.
- `docker compose up -d` startet den Container im Hintergrund.
- `docker compose ps` zeigt, ob der Service `ade` läuft.
- `docker compose exec ade bash` öffnet eine Shell im laufenden Container.
- `dotnet --info` zeigt, ob das .NET SDK im Container installiert und nutzbar ist.
- `java --version`, `javac --version` und `mvn --version` prüfen JDK und Maven.
- `go version` und `gopls version` prüfen Go und den Go Language Server.
- `rustc --version`, `cargo --version` und `cargo clippy --version` prüfen die Rust-Toolchain und Clippy.
- `python --version` prüft die installierte Python-Version.
- `node --version` und `npm --version` prüfen die Node.js-Werkzeuge, die OpenCode und Codex CLI brauchen.
- `opencode --version` prüft die installierte OpenCode CLI.
- `codex --version` prüft die installierte Codex CLI.
- `specify version` prüft die installierte Spec Kit CLI.
- `ls /workspace` prüft das lokale Projekt-Workspace-Mount.
- `ls /rider-projects` prüft den über `RIDER_PROJECTS_DIR` konfigurierten Host-Mount.
- `ls /java-projects` prüft den über `JAVA_PROJECTS_DIR` konfigurierten Host-Mount.
- `ls /go-projects`, `ls /rust-projects` und `ls /python-projects` prüfen die sprachspezifischen Host-Mounts.

Erwartetes Ergebnis:

- `docker compose ps` zeigt den Service `ade` als laufend.
- `dotnet --info` gibt SDK-Informationen aus und endet ohne Fehler.
- `java --version` und `mvn --version` geben Versionsinformationen aus.
- `go version`, `gopls version`, `rustc --version`, `cargo --version`, `cargo clippy --version` und `python --version` geben Versionsinformationen aus.
- `opencode --version`, `codex --version` und `specify version` geben Versionsinformationen aus.
- `ls /rider-projects` zeigt die Projekte aus dem Host-Verzeichnis oder bleibt leer, wenn das Verzeichnis noch keine Projekte enthält.
- `ls /java-projects` zeigt Java-Projekte aus dem Host-Verzeichnis oder bleibt leer, wenn das Verzeichnis noch keine Projekte enthält.
- `ls /go-projects`, `ls /rust-projects` und `ls /python-projects` zeigen sprachspezifische Projekte oder bleiben leer.

macOS-Hinweis: Wenn Docker Desktop gerade erst installiert wurde, Docker Desktop zuerst einmal starten und warten, bis die Engine läuft. Danach funktionieren `docker --version`, `docker compose version` und `docker info` im Terminal.

Windows-Hinweis: Wenn Docker Desktop aus PowerShell verwendet wird, muss `RIDER_PROJECTS_DIR` in `.env` als Windows-Pfad gesetzt werden, zum Beispiel `C:\Users\<benutzer>\RiderProjects`. Wenn die Befehle aus Ubuntu/WSL2 laufen, wird der WSL-Pfad verwendet, zum Beispiel `/mnt/c/Users/<benutzer>/RiderProjects`.

Sicherheits-Hinweis: `opencode.env` enthält den API-Key. Diese Datei nie committen, nie in Screenshots zeigen und nicht in Chat- oder Ticket-Systeme kopieren. Für Tests reicht es, zu prüfen, dass OpenCode startet; der Key muss nicht sichtbar gemacht werden.

Wenn der Build bewusst komplett frisch laufen soll:

```bash
docker compose build --pull --no-cache
docker compose up -d --force-recreate
```

### Merksätze

> **Docker oder Podman:** Die folgenden `docker`-Befehle gelten mit Podman sinngemäß (`podman compose` oder `podman-compose`), siehe [Docker und Podman: gleiche Befehle](#docker-und-podman-gleiche-befehle).

- Nach Änderungen am `Dockerfile` immer neu bauen:

```bash
docker compose build --pull --no-cache
docker compose up -d --force-recreate
```

- Nach reinen Änderungen an `compose.yml` reicht meistens:

```bash
docker compose up -d --force-recreate
```

- ASP.NET-Apps müssen im Container auf `0.0.0.0` lauschen:

```bash
dotnet run --urls http://0.0.0.0:5102
```

- Windows erreicht Web-Apps dann über `http://localhost:<port>`.
- Freigegeben ist lokal die Port-Range `5100-5199`.
- `opencode.env` enthält ein Secret und darf nicht committed werden.
- `opencode.jsonc` ist die kommentierte OpenCode-Konfiguration für den Container.
- `specify-cli` ist bewusst auf eine Version gepinnt. Updates werden manuell im Dockerfile gemacht.
- Für neue Projekte unter `/rider-projects` zuerst projektlokal initialisieren:

```bash
opencode --prompt "/init"
specify init . --integration opencode --force
```

- Wenn Spec Kit nach dem Script-Typ fragt, `sh` wählen.
- Projektregeln für OpenCode gehören in die jeweilige Projektdatei `AGENTS.md`.
- `.opencode/` kann sensible Daten enthalten. Pro Projekt entscheiden, ob der Ordner ganz oder teilweise in `.gitignore` gehört.
- Bei `bin`-, `obj`- oder `apphost`-Fehlern prüfen:

```bash
echo "$DirectoryBuildPropsPath"
ls /dotnet-config/ContainerBuild.props
ls /dotnet-build
```

### Glossar

Dieses Glossar erklärt die wichtigsten Begriffe in einfacher Form. Wer den Begriff nicht kennt, sollte zuerst hier nachsehen, bevor er weiterliest.

| Begriff | Bedeutung |
|---|---|
| Agent | Ein KI-Programm wie OpenCode oder Codex, das im Container Aufgaben ausführen kann. |
| API-Key | Ein geheimer Schlüssel, mit dem ein Programm einen Online-Dienst nutzen darf. Wie ein Passwort, aber für Maschinen. |
| ASP.NET | Web-Framework von Microsoft für serverseitige Webanwendungen in C#. |
| Bind-Mount | Ein Verzeichnis vom Host, das direkt in den Container eingebunden wird. Änderungen wirken in beide Richtungen. |
| Build | Der Bauschritt, der aus Quellcode ein ausführbares Programm macht. |
| Cargo | Build- und Paketwerkzeug für Rust-Projekte. |
| Compose | Werkzeug, das Container über eine Datei `compose.yml` startet und stoppt. |
| Container | Ein gekapselter Linux-Prozess, der aus einem Image gestartet wird. Wie eine kleine virtuelle Umgebung, aber leichter als eine virtuelle Maschine. |
| Dockerfile | Eine Textdatei, die beschreibt, wie ein Image gebaut wird. |
| Engine | Der laufende Hintergrunddienst von Docker oder Podman. Ohne Engine kein Container. |
| Host | Dein eigener Rechner. Im Gegensatz dazu der Container. |
| Image | Die Vorlage für Container. Aus einem Image können viele Container gestartet werden. |
| JDK | Java Development Kit. Enthält Compiler `javac` und Laufzeit `java`. |
| JSONC | JSON mit erlaubten Kommentaren. Wird in `opencode.jsonc` verwendet. |
| Maven | Werkzeug für Java-Projekte. Baut Projekte und verwaltet Abhängigkeiten. |
| MSBuild | Bauwerkzeug von Microsoft für .NET-Projekte. |
| Mount | Allgemein: ein Verzeichnis irgendwo einhängen. Hier meist Bind-Mount oder Volume. |
| .NET SDK | Software Development Kit für die Programmiersprachen C#, F# und VB.NET. |
| Podman | Alternative zu Docker. Läuft ohne Daemon und braucht meistens keine Root-Rechte. |
| Port | Eine nummerierte Tür auf einem Rechner, über die Netzwerkdienste erreicht werden. |
| Provider | Hier: der Anbieter eines KI-Modells, zum Beispiel `chat-ai`. |
| Registry | Speicherort für Container-Images im Netz, zum Beispiel die GitLab Container Registry. |
| Rider | Eine integrierte Entwicklungsumgebung (IDE) von JetBrains für .NET. |
| Rootless | Ohne Administrator- oder Root-Rechte. Podman läuft standardmäßig rootless. |
| Rustup | Werkzeug, das Rust-Toolchains und Komponenten wie `rustfmt` oder `clippy` installiert. |
| Sandbox | Eine geschützte Umgebung, in der ein Programm nicht überall hin schreiben darf. |
| SDD | Spec-Driven Development. Erst beschreiben, dann planen, dann umsetzen. |
| Secret | Eine geheime Information wie ein API-Key oder ein Passwort. |
| Service | Ein benannter Container in `compose.yml`. In diesem Repository: `ade`. |
| Shell | Ein Programm wie Bash, mit dem Befehle eingegeben werden. |
| Spec Kit | Eine CLI, die einen festen Ablauf für die Erstellung von Software-Spezifikationen anbietet. |
| Volume | Ein von Docker oder Podman verwalteter Speicherbereich, getrennt vom Host-Dateisystem. |
| WSL2 | Windows Subsystem for Linux Version 2. Eine echte Linux-Umgebung in Windows. |

### Barrierefreiheit

Diese README erfüllt WCAG 2.2 Level AA so weit wie es Markdown auf GitHub erlaubt.

| WCAG-Kriterium | Umsetzung |
|---|---|
| 1.3.1 Info und Beziehungen | Konsistente Heading-Hierarchie H1 → H2 → H3 → H4. Tabellen mit Kopfzeile. Listen statt freien Text, wo es passt. |
| 1.4.1 Verwendung von Farbe | Keine Information allein durch Farbe. Status wird durch Text wie *erlaubt*, *gesperrt*, *fragt nach* ausgedrückt. |
| 2.4.4 Linkzweck | Sprechende Linktexte im Inhaltsverzeichnis. Keine "hier klicken"-Formulierungen. |
| 2.4.6 Überschriften und Beschriftungen | Bilinguale Überschriften am Anfang. Klare, eigenständige Sektionsüberschriften. |
| 3.1.1 Sprache der Seite | Hauptsprache Deutsch im DE-Block, Englisch im EN-Block. (Plattform-Einschränkung: GitHub-Markdown unterstützt kein `lang`-Attribut.) |
| 3.1.5 Lesbarkeit | Zielsprachniveau CEFR B2. Kurze Sätze. Fachbegriffe werden eingeführt und im Glossar erklärt. |
| 4.1.1 Syntaxanalyse | Alle Code-Blöcke haben eine Sprachangabe (`bash`, `powershell`, `yaml`, `dockerfile`, `text` …). |
| 4.1.2 Name, Rolle, Wert | Markdown-Standardelemente. Keine eingebetteten HTML-Komponenten mit eigener Logik. |

Bekannte Einschränkungen der Plattform:

- WCAG 3.1.2 (Sprache von Teilen): GitHub entfernt HTML-`lang`-Attribute. Sprachwechsel zwischen DE und EN sind nur über Sektionsüberschriften signalisiert.
- Lange Codeblöcke können auf kleinen Bildschirmen horizontales Scrollen verursachen. Das ist ein Markdown-Limit.

Tipps für Lernende mit Screenreader oder Braille-Display:

- Das Inhaltsverzeichnis nutzen, um schnell in die richtige Sektion zu springen.
- Innerhalb einer Sektion sind die Schritte als nummerierte oder ungeordnete Listen aufgebaut.
- Code-Blöcke werden im Fließtext immer mit einem erklärenden Satz vorbereitet.

---

## English

### At a glance

| Item | Information |
|---|---|
| Target group | IT-specialist apprentices, first year and later |
| Learning goal | Use a reproducible container development environment |
| Languages | C# / .NET, Java, Go, Rust, Python, Bash, PowerShell |
| Container | Docker or Podman, on Linux, macOS, or Windows |
| Time for the quick start | About 10 minutes of reading, 15 to 30 minutes for the first build |
| Time for full exploration | Several training units across several weeks |
| Prerequisite knowledge | Shell basics, rough understanding of Git |
| Accessibility | WCAG 2.2 Level AA, see section [Accessibility](#accessibility) |

### Quick start in 10 minutes

This quick start is for anyone who wants to try the setup first. Details follow in the later sections.

> **Docker or Podman:** This quick start uses Docker. With Podman, substitute the commands accordingly (`podman compose` or `podman-compose`) and use the matching Podman section for the first GitLab registry login: [Ubuntu](#use-podman-on-ubuntu-2404-lts), [macOS](#use-podman-on-macos-with-homebrew), [Windows](#use-podman-on-windows-with-podman-desktop).

Step 1: Check prerequisites.

- Docker Engine or Docker Desktop is installed.
- A shell is open (Bash on Linux/macOS, PowerShell on Windows).
- You know the path to this repository on your machine.

Step 2: Change into the repository. Replace `<user>` with your login name.

```bash
cd /home/<user>/ade-dev-sandbox     # Linux / WSL2
cd /Users/<user>/ade-dev-sandbox    # macOS
```

```powershell
cd C:\Users\<user>\ade-dev-sandbox  # Windows
```

Step 3: Create local configuration files. `.env` only contains paths; `opencode.env` contains the secret API key.

```bash
cp .env.example .env
cp opencode.env.example opencode.env
chmod 600 opencode.env
```

Step 4: Enter the real `GWDG_API_KEY` in `opencode.env`. Do not print the key in the terminal and do not commit it.

Step 5: Build and start the container.

```bash
docker compose build --pull
docker compose up -d
docker compose ps
```

Step 6: Open a shell inside the container.

```bash
docker compose exec ade bash
```

Step 7: Inside the container, check that everything is ready.

```bash
dotnet --info
opencode --version
specify version
```

If these three commands print version information, the quick start is complete. For your first real exercises, continue with the section [Learning path for apprentices](#learning-path-for-apprentices).

### Prerequisites

This guide assumes the following minimum requirements. The values are generous so the container stays stable when building larger projects.

| Requirement | Minimum | Recommended | Note |
|---|---|---|---|
| Operating system | Ubuntu 22.04, macOS 13, Windows 11 | Current LTS or follow-up version | WSL2 is recommended on Windows. |
| RAM | 8 GiB | 16 GiB or more | .NET, Java, and containers need memory. |
| Free disk space | 20 GiB | 50 GiB or more | Images, volumes, and build cache grow. |
| Internet | 10 Mbit/s | 50 Mbit/s | First builds download many packages. |
| Permissions | Local user account | sudo or admin for installation | The container itself runs as a normal user. |
| Prior knowledge | Shell basics, Git basics | Plus editor experience | Editor: Visual Studio Code or JetBrains Rider. |

If one item is missing, the quick start usually still works. The setup will be slower or less stable, though.

### Target group and purpose

This guide is written for first-year IT specialist apprentices and later. It explains the commands and also why they are needed.

This repository provides a Docker environment for Opencode, .NET, C#, Java, Go, Rust, and Python. It runs with Docker Engine on Linux or WSL2 and with Docker Desktop on macOS or Windows. Projects can still be edited with JetBrains Rider on the host.

### Learning path for apprentices

The README is long. But it is not a book you must read in one sitting. This learning path shows a sensible order.

| Phase | Sections | Learning goal |
|---|---|---|
| Phase 1: Understand | [Basic idea](#basic-idea), [Terms and command location](#terms-and-command-location), [Project structure](#project-structure) | What is a container? What is an image? Where does which command run? |
| Phase 2: Set up | [Prerequisites](#prerequisites), one installation section (Docker or Podman), [Set up the API key](#set-up-the-api-key), [Build and start the container](#build-and-start-the-container) | The container runs on your own machine. |
| Phase 3: First exercises | [Use .NET and C# inside the container](#use-net-and-c-inside-the-container), [Use Java and Maven inside the container](#use-java-and-maven-inside-the-container), [Use Go inside the container](#use-go-inside-the-container), [Use Rust inside the container](#use-rust-inside-the-container), [Use Python inside the container](#use-python-inside-the-container), [Scripting with Bash and PowerShell](#scripting-with-bash-and-powershell) | Create, build, and run your own console or script project. |
| Phase 4: Practice tools | [Use Spec Kit](#use-spec-kit), [Use Opencode](#use-opencode), [Use Codex CLI](#use-codex-cli) | Use AI tools for specification and code correctly. |
| Phase 5: Quality and security | [Install Spec Kit governance presets](#install-spec-kit-governance-presets), [Required flow for an SDD feature](#required-flow-for-an-sdd-feature), [Configuration](#configuration) | Rules, secure development, quality process. |
| Phase 6: Operation and troubleshooting | [Clean up](#clean-up), [Common problems](#common-problems), [Compact test procedure](#compact-test-procedure) | Keep your environment healthy and understand errors. |

Recommendation for the first year: phases 1 to 3. Phases 4 to 6 come next and suit later years or retraining.

### Basic idea

Docker builds an image from the `Dockerfile`. Docker Compose starts a container from that image. The container includes the Microsoft .NET SDK, Java JDK 21, Maven, Go, Rust, Python, Node.js, npm, Opencode, Codex CLI, and common agent helper tools.

The container stays active in the background. You can then open a shell inside it and run commands such as `dotnet`, `opencode`, `codex`, or `ls`.

The shell runs as the Linux user `adedev` inside the container. That is why the prompt starts with something like `adedev@...` after entering the container. The Compose service is named `ade`; the OpenCode command is still named `opencode`.

### Terms and command location

Many errors happen when a command is run in the wrong place. This guide therefore separates host and container.

- Host: your computer or the WSL2 environment. Run `docker compose ...` commands there.
- Container: the Linux environment started by Docker from the image. Run tools such as `dotnet`, `java`, `mvn`, `go`, `cargo`, `python`, `opencode`, `codex`, and `specify` there.
- Image: the template for the container. After changes to the `Dockerfile`, rebuild the image.
- Bind mount: a host directory is mounted directly into the container, for example `/rider-projects` or `/java-projects`.
- Volume: storage managed by Docker, for example for `/dotnet-build` or local agent data.
- Service: the name in `compose.yml`. In this repository, the service is named `ade`.

If the prompt starts with `adedev@...`, the shell is inside the container. If the prompt shows the normal computer name or the WSL2 shell, the shell is on the host.

A more complete term reference is in the section [Glossary](#glossary).

### Project structure

- `Dockerfile`: describes the container image. It inherits from the shared `agent-sandbox` image and installs .NET SDK, Java JDK 21, Maven, Go, Rust, Python, Opencode, Codex CLI, `uv`, Spec Kit, and common CLI helper tools on top.
- `compose.yml`: describes the `ade` service, volumes, and build rules.
- `.dockerignore` and `.containerignore`: exclude local secrets, Git data, and working directories from the build context.
- `.env.example`: template for the platform-specific project mounts `RIDER_PROJECTS_DIR`, `JAVA_PROJECTS_DIR`, `GO_PROJECTS_DIR`, `RUST_PROJECTS_DIR`, and `PYTHON_PROJECTS_DIR`.
- `opencode.jsonc`: contains provider, model, and agent settings for Opencode. JSONC allows comments and is easier to read for learning.
- `opencode.env.example`: template for the local `opencode.env` file.
- `codex/config.toml`: system-wide Codex default configuration for the container. It is copied to `/etc/codex/config.toml` and `/etc/codex/managed_config.toml`.
- `codex/requirements.toml`: admin-enforced Codex security requirements. It is copied to `/etc/codex/requirements.toml`.
- `workspace/`: local working directory, mounted as `/workspace`.
- `RIDER_PROJECTS_DIR`: host directory for Rider projects, mounted as `/rider-projects`.
- `JAVA_PROJECTS_DIR`: host directory for Java projects, mounted as `/java-projects`.
- `java-projects/`: local fallback directory for Java projects when `JAVA_PROJECTS_DIR` is not set.
- `GO_PROJECTS_DIR`: host directory for Go projects, mounted as `/go-projects`.
- `go-projects/`: local fallback directory for Go projects when `GO_PROJECTS_DIR` is not set.
- `RUST_PROJECTS_DIR`: host directory for Rust projects, mounted as `/rust-projects`.
- `rust-projects/`: local fallback directory for Rust projects when `RUST_PROJECTS_DIR` is not set.
- `PYTHON_PROJECTS_DIR`: host directory for Python projects, mounted as `/python-projects`.
- `python-projects/`: local fallback directory for Python projects when `PYTHON_PROJECTS_DIR` is not set.
- `dotnet/ContainerBuild.props`: redirects .NET build artifacts for Rider projects to the container volume `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: filters a known .NET workload verification message from command output.
- `spec-kit/patch-specify-cli.py`: adapts Spec Kit for Windows and WSL bind mounts.
- `codex_data`: Docker volume for Codex CLI data under `/home/adedev/.codex`.
- `AGENTS.md`: rules for AI agents such as Opencode or Codex.

### Docker and Podman: the same commands

This guide shows most examples with `docker`. Podman is largely command-compatible. The general sections such as [Build and start the container](#build-and-start-the-container), [Use .NET and C# inside the container](#use-net-and-c-inside-the-container), [Reach an ASP.NET web app from the host](#reach-an-aspnet-web-app-from-the-host), and [Compact test procedure](#compact-test-procedure) therefore apply to both tools. Substitute the commands accordingly:

| Docker | Podman |
|---|---|
| `docker compose build --pull` | `podman compose build --pull` or `podman-compose build --pull` |
| `docker compose up -d` | `podman compose up -d` or `podman-compose up -d` |
| `docker compose ps` | `podman compose ps` or `podman-compose ps` |
| `docker compose exec ade bash` | `podman compose exec ade bash` or `podman-compose exec ade bash` |
| `docker compose down` | `podman compose down` or `podman-compose down` |
| `docker compose down -v` | `podman compose down -v` or `podman-compose down -v` |
| `docker info` | `podman info` |

Note on spelling: On many Linux installations, the Compose command is `podman-compose` (with a hyphen). On macOS and Windows with Podman Desktop, `podman compose` (with a space) often works. If one variant is missing, use the other.

For a full step-by-step guide with Podman, there are dedicated sections for [Ubuntu](#use-podman-on-ubuntu-2404-lts), [macOS](#use-podman-on-macos-with-homebrew), and [Windows](#use-podman-on-windows-with-podman-desktop). One important difference remains: when building the private GitLab base image, external Compose providers on macOS and Windows sometimes use different registry credentials. That is why the Podman sections build the image directly with `podman build` there. For normal operation with `up`, `ps`, `exec`, and `down`, the commands are interchangeable.

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

### Docker Desktop profiles for macOS and Windows

When Docker Desktop is used, the container is still a Linux container. Only the host paths mounted into `/rider-projects` and `/java-projects` change.

Docker Desktop can be used free of charge for personal use, education, learning, small businesses, and non-commercial open source projects. Commercial use in larger companies with more than 250 employees or more than USD 10 million in annual revenue requires a paid Docker subscription. When in doubt, the current Docker Subscription Service Agreement terms apply.

macOS with Homebrew:

```bash
brew install --cask docker
open -a Docker
```

Then check in the terminal:

```bash
docker --version
docker compose version
docker info
```

Windows with Winget:

```powershell
winget install --id Docker.DockerDesktop -e
```

Then start Docker Desktop from the Start menu, accept the license terms, and make sure the WSL2 backend is enabled. Alternatively, use the installer from the official Docker website.

First create the Compose environment file:

```bash
cp .env.example .env
```

Then set `RIDER_PROJECTS_DIR` and `JAVA_PROJECTS_DIR` for the current platform.

macOS:

```text
RIDER_PROJECTS_DIR=/Users/<user>/RiderProjects
JAVA_PROJECTS_DIR=/Users/<user>/JavaProjects
```

Windows with Docker Desktop from PowerShell:

```text
RIDER_PROJECTS_DIR=C:\Users\<user>\RiderProjects
JAVA_PROJECTS_DIR=C:\Users\<user>\JavaProjects
```

Windows with Docker Desktop from Ubuntu/WSL2:

```text
RIDER_PROJECTS_DIR=/mnt/c/Users/<user>/RiderProjects
JAVA_PROJECTS_DIR=/mnt/c/Users/<user>/JavaProjects
```

If no separate Rider or Java project directory is needed, keep the default from `.env.example`. Then `/rider-projects` points to `workspace/` and `/java-projects` points to `java-projects/`.

The `.env` file contains no secrets, but it is local and platform-specific. It is not committed. The API key stays separate in `opencode.env`.

Note for apprentices: `.env` only contains paths. `opencode.env` contains a secret. This separation is important so an API key is not accidentally committed to Git.

Check the configuration:

```bash
docker compose config --no-interpolate
```

### Use Podman on Ubuntu 24.04 LTS

Podman is an alternative to Docker. On Ubuntu, Podman runs directly on the Linux host. A Podman machine like on macOS is not needed.

Install Podman, Podman Compose, and Flatpak:

```bash
sudo apt update
sudo apt install -y podman podman-compose flatpak
```

Check the installation:

```bash
podman --version
podman-compose --version
podman run --rm quay.io/podman/hello
```

Optionally install Podman Desktop through Flathub:

```bash
flatpak remote-add --if-not-exists --user flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install --user flathub io.podman_desktop.PodmanDesktop
```

Start Podman Desktop:

```bash
flatpak run io.podman_desktop.PodmanDesktop
```

Before starting the container, create the local environment files. `.env` contains local paths, and `opencode.env` contains the secret API key:

```bash
cp .env.example .env
cp opencode.env.example opencode.env
chmod 600 opencode.env
```

Then enter the real `GWDG_API_KEY` in `opencode.env`. Do not print the key in the terminal and do not commit it.

Change into the repository:

```bash
cd /home/<user>/ade-dev-sandbox
```

Before the first build, log in to the GitLab container registry. Use a GitLab token with at least `read_registry` as the password:

```bash
podman login docker.gitlab-ce.gwdg.de
```

Check the Compose file without expanding variable values and secrets:

```bash
podman-compose config --no-interpolate
```

Build the image through the Compose configuration:

```bash
podman-compose build --pull
```

Build only the image directly from this directory, without starting the Compose service:

```bash
podman build --pull -t ade-dev-sandbox .
```

Start the container in the background:

```bash
podman-compose up -d
```

Show the status:

```bash
podman-compose ps
```

Open Bash inside the running `ade` container:

```bash
podman-compose exec ade bash
```

Leave the container shell again:

```bash
exit
```

Stop the container but keep data:

```bash
podman-compose down
```

Stop the container and delete persistent container and volume data from this Compose project:

```bash
podman-compose down -v
```

Note: On some installations, `podman compose ...` also works. If that command starts Docker Compose as a provider or searches for the Docker daemon, use `podman-compose ...` for this repository.

WSL2 and Windows note: If the same environment is started once with Podman Desktop on Windows and once with Podman in WSL2, both containers must not run at the same time. Both variants publish the same port range `127.0.0.1:5100-5199`. Before starting in WSL2, stop the Windows container in Podman Desktop or PowerShell:

```powershell
podman compose down
```

Before starting on Windows, stop the WSL2 container:

```bash
podman-compose down
```

### Use Podman on macOS with Homebrew

Podman is an alternative to Docker Desktop. On macOS, the actual Linux container also runs inside a small virtual machine. In Podman, this virtual machine is called a `machine`.

Install Podman and Podman Compose with Homebrew:

```bash
brew install podman podman-compose
```

Check the installation:

```bash
podman --version
podman compose version
```

Create the Podman machine once:

```bash
podman machine init
```

Start the Podman machine:

```bash
podman machine start
```

Then check whether Podman is running:

```bash
podman info
```

Before starting the container, create the local environment files for Podman as well. `.env` contains local paths, and `opencode.env` contains the secret API key:

```bash
cp .env.example .env
cp opencode.env.example opencode.env
chmod 600 opencode.env
```

Then enter the real `GWDG_API_KEY` in `opencode.env`. Do not print the key in the terminal and do not commit it.

Change into the repository:

```bash
cd /Users/<user>/ade-dev-sandbox
```

Before the first build, log in to the GitLab container registry. Use a GitLab token with at least `read_registry` as the password:

```bash
podman login docker.gitlab-ce.gwdg.de
```

Check the Compose file without expanding variable values and secrets:

```bash
podman compose config --no-interpolate
```

Build the image and pull the pinned Sandbox base image:

```bash
podman compose build --pull
```

If `podman compose build --pull` reports that it is using an external Compose provider such as `/usr/local/bin/docker-compose`, that is not automatically an error on macOS. If the build then fails on the private GitLab base image with `Requesting bearer token` and `403 Forbidden`, the external provider probably uses different registry credentials than `podman login`. In that case, pull the base image and build the project image directly with Podman, and use Compose only for startup:

```bash
podman pull docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox@sha256:a21e15872aed8b0e4b9e18e0ff1e678318968efb4b8367ddf9fa4a63fc1d294c
podman build --pull -t ade-dev-sandbox-ade .
podman compose up -d --no-build --force-recreate
```

If Podman Desktop is visibly running but the terminal CLI still fails with a message such as `unable to connect to Podman socket`, `connection refused`, or a stale `ssh://core@127.0.0.1:<port>`, check the active connection first:

```bash
podman machine list
podman system connection list
ls -l /var/run/docker.sock
docker --host unix:///var/run/docker.sock version
```

On macOS, Podman Desktop often exposes a Docker-compatible socket. In that setup, `/var/run/docker.sock` points to a Podman socket under `~/.local/share/containers/podman/machine/podman.sock`. You can then build the image with the Docker CLI against Podman, without starting Docker Desktop:

```bash
docker --host unix:///var/run/docker.sock compose build --pull
docker --host unix:///var/run/docker.sock image inspect ade-dev-sandbox-ade --format '{{.Id}} {{.Architecture}} {{.Os}} {{.Size}}'
```

The image and container store then lives logically inside the Podman machine at `/var/home/core/.local/share/containers/storage` and usually uses the `overlay` driver. Physically on macOS, that store is inside the Podman machine's virtual disk, for example `~/.local/share/containers/podman/machine/applehv/podman-machine-default-arm64.raw`. This file is not a single image file; it is the virtual Linux disk used by the Podman machine.

Then continue directly with the status check.

Start the container in the background:

```bash
podman compose up -d
```

Show the status:

```bash
podman compose ps
```

Open Bash inside the running `ade` container:

```bash
podman compose exec ade bash
```

Leave the container shell again:

```bash
exit
```

Stop the container but keep data:

```bash
podman compose down
```

Stop the container and delete persistent container and volume data from this Compose project:

```bash
podman compose down -v
```

If Podman is not needed afterwards, the Podman machine can also be stopped:

```bash
podman machine stop
```

If `podman compose ...` is not available on an installation, run the same flow with `podman-compose ...`, for example:

```bash
podman-compose build --pull
podman-compose up -d
podman-compose exec ade bash
podman-compose down
```

### Use Podman on Windows with Podman Desktop

Podman is an alternative to Docker Desktop. On Windows, Linux containers run inside a small virtual machine. Podman calls this virtual machine a `machine`. Podman Desktop can set up Podman, the machine, and Compose support.

Install Podman Desktop with Winget:

```powershell
winget install --id RedHat.Podman-Desktop -e
```

Then start Podman Desktop from the Start menu. During first-time setup:

- Use WSL2 as the provider unless Hyper-V is required.
- Let Podman Desktop install Podman if Podman is missing.
- Create a Podman machine.
- Install Compose support.

If WSL2 is not ready yet, open PowerShell as Administrator and update or enable WSL:

```powershell
wsl --update
wsl --install --no-distribution
```

If Windows asks for a restart, restart the computer. Then verify the setup:

```powershell
wsl --status
podman --version
podman machine list
podman info
podman compose version
```

If no machine exists yet or the machine is stopped:

```powershell
podman machine init
podman machine start
```

Before starting the container, create the local environment files in the repository. Run these commands in PowerShell on the Windows host:

```powershell
Copy-Item .env.example .env
Copy-Item opencode.env.example opencode.env
```

Then enter the real `GWDG_API_KEY` in `opencode.env`. Do not print the key in the terminal and do not commit it.

Set Windows paths in `.env` if Rider or Java projects are outside this repository:

```text
RIDER_PROJECTS_DIR=C:\Users\<user>\RiderProjects
JAVA_PROJECTS_DIR=C:\Users\<user>\JavaProjects
```

If no separate Rider or Java project directory is needed, keep the defaults from `.env.example`. Then `/rider-projects` points to `workspace/` and `/java-projects` points to `java-projects/`.

Change into the repository:

```powershell
cd C:\Users\<user>\ade-dev-sandbox
```

Before the first build, log in to the GitLab container registry. Use a GitLab token with at least `read_registry` as the password:

```powershell
podman login docker.gitlab-ce.gwdg.de
```

Windows-specific note: on many installations, `podman compose` uses an external Compose provider, often `docker-compose.exe`. That provider does not necessarily read the same Podman auth file as `podman pull`. Create a Docker-compatible auth file and log in there as well:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.docker" | Out-Null
podman login --compat-auth-file "$env:USERPROFILE\.docker\config.json" docker.gitlab-ce.gwdg.de
podman login --get-login --compat-auth-file "$env:USERPROFILE\.docker\config.json" docker.gitlab-ce.gwdg.de
```

The last command must print the GitLab username. If only `podman login` works but the Docker-compatible auth file is missing, `podman pull` can succeed while `podman compose build --pull` still fails on the pinned GitLab base image with `Requesting bearer token` and `403 Forbidden`.

Check the Compose file without expanding variable values and secrets:

```powershell
podman compose config --no-interpolate
```

On Windows, pull the pinned base image with Podman first. This step verifies that the registry login works for Podman:

```powershell
podman pull docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox@sha256:a21e15872aed8b0e4b9e18e0ff1e678318968efb4b8367ddf9fa4a63fc1d294c
```

Then build the project image through Compose. With the Docker-compatible auth file in place, the external `docker-compose.exe` provider can pull the private GitLab base image:

```powershell
podman compose build --pull
```

Start the container in the background:

```powershell
podman compose up -d --force-recreate
```

Fallback: if `podman compose build --pull` still fails with `403 Forbidden` even after the Docker-compatible auth file is configured, re-check the login and the direct pull first. As a short-term workaround, build the project image directly with Podman and use Compose only for startup:

```powershell
podman pull docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox@sha256:a21e15872aed8b0e4b9e18e0ff1e678318968efb4b8367ddf9fa4a63fc1d294c
podman build --pull -t ade-dev-sandbox-ade .
podman compose up -d --no-build --force-recreate
```

Show the status:

```powershell
podman compose ps
```

Open Bash in the running `ade` container:

```powershell
podman compose exec ade bash
```

Leave the container shell again:

```bash
exit
```

Stop the container and keep data:

```powershell
podman compose down
```

Stop the container and delete persistent container and volume data from this Compose project:

```powershell
podman compose down -v
```

If `podman compose ...` reports that it is using an external Compose provider such as `docker-compose.exe`, that is not automatically an error. The important part is the auth context: on Windows, `docker-compose.exe` needs a Docker-compatible auth file. Without `podman login --compat-auth-file "$env:USERPROFILE\.docker\config.json" docker.gitlab-ce.gwdg.de`, `podman pull` can work while `podman compose build --pull` still fails with `403 Forbidden` on the private GitLab base image.

WSL2 and Windows note: If the same environment is started once with Podman Desktop on Windows and once with Podman in WSL2, both containers must not run at the same time. Both variants publish the same port range `127.0.0.1:5100-5199`. Before starting on Windows, stop the WSL2 container:

```bash
podman-compose down
```

Before starting in WSL2, stop the Windows container in Podman Desktop or PowerShell:

```powershell
podman compose down
```

### Check Docker permissions

If `docker info` fails with `permission denied`, the current user is not allowed to access Docker yet.

Note for Podman: Podman runs rootless by default, so a Docker group is usually not needed. This section mainly applies to Docker.

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

> **Docker or Podman:** These commands use Docker. With Podman they apply in the same way — replace `docker compose` with `podman compose` or `podman-compose` (see [Docker and Podman: the same commands](#docker-and-podman-the-same-commands)). A full Podman guide is in the sections [Use Podman on Ubuntu](#use-podman-on-ubuntu-2404-lts), [Use Podman on macOS](#use-podman-on-macos-with-homebrew), and [Use Podman on Windows](#use-podman-on-windows-with-podman-desktop).

Change into the repository:

```bash
cd /home/<user>/ade-dev-sandbox
```

Before the first build, log in to the GitLab container registry. Use a GitLab token with at least `read_registry` as the password:

```bash
docker login docker.gitlab-ce.gwdg.de
```

Build the image and pull the pinned Sandbox base image:

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

The first build downloads the pinned Sandbox base image, the .NET SDK package, and npm packages. This can take several minutes.

### Mount Rider projects from Windows

The host directory for Rider projects is set through `RIDER_PROJECTS_DIR`. Typical values are:

```text
RIDER_PROJECTS_DIR=/mnt/c/Users/<user>/RiderProjects
RIDER_PROJECTS_DIR=C:\Users\<user>\RiderProjects
RIDER_PROJECTS_DIR=/Users/<user>/RiderProjects
```

The directory is mounted inside the container here:

```text
/rider-projects
```

Inside the container, change to that directory:

```bash
cd /rider-projects
ls
```

Changes inside the container are written directly to the host files. Rider on the host sees the same files. Builds on Windows or macOS bind mounts can be slower than builds inside the Linux file system.

To avoid .NET problems with `bin`, `obj`, AppHost files, or file timestamps on host files, an MSBuild configuration file is mounted into the container:

```text
dotnet/ContainerBuild.props -> /dotnet-config/ContainerBuild.props
```

Compose sets the `DirectoryBuildPropsPath` environment variable for this. The configuration is loaded very early in the MSBuild process. Repository-specific `Directory.Build.props` files are still imported by `ContainerBuild.props`, so project settings remain active.

Build artifacts are written to the Linux volume `/dotnet-build` instead of `/rider-projects`. This prevents common errors such as `Access to the path ... obj ... is denied` or errors while creating `apphost`.

### Use .NET and C# inside the container

Open a shell inside the container:

```bash
docker compose exec ade bash
```

With Podman: `podman compose exec ade bash` or `podman-compose exec ade bash`.

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

`dotnet new console` creates a simple console application. `dotnet run` builds and starts the project. The files are stored on the host in the `RIDER_PROJECTS_DIR` directory and can be opened there with Rider.

If a project already has broken `bin` or `obj` folders on the Windows mount, delete them in Rider or in the terminal. Then build again inside the container.

### Mount Java projects

The host directory for Java projects is set through `JAVA_PROJECTS_DIR`. In a WSL2 environment, a typical value is:

```text
JAVA_PROJECTS_DIR=/mnt/c/Users/<user>/JavaProjects
```

The directory is mounted inside the container here:

```text
/java-projects
```

This keeps .NET/Rider projects and Java projects separated:

- `/rider-projects`: .NET, C#, and Rider projects.
- `/java-projects`: Java, Maven, and Spring Boot projects.
- `/workspace`: general exercises, for example Go, Rust, or Python projects.

### Use Java and Maven inside the container

Check Java versions:

```bash
java --version
javac --version
mvn --version
```

Example for a new Maven project:

```bash
cd /java-projects
mvn archetype:generate -DgroupId=com.example -DartifactId=demo-java -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
cd demo-java
mvn test
```

Spring Boot projects are normally started through Maven or a project wrapper, for example:

```bash
mvn spring-boot:run
```

Gradle and Spring Boot CLI are intentionally not installed globally. Many company projects include their own Maven or Gradle wrapper. This is more reproducible than global tool versions.

### Use Go inside the container

Check the Go version and Go tools:

```bash
go version
gopls version
staticcheck -version
govulncheck -version
dlv version
```

Example for a small Go project:

```bash
cd /workspace
mkdir -p demo-go
cd demo-go
go mod init example.com/demo-go
cat > main.go <<'EOF'
package main

import "fmt"

func main() {
    fmt.Println("Hello from Go")
}
EOF
gofmt -w main.go
go test ./...
go run .
```

Go web frameworks are not installed globally. For first web exercises, the standard library package `net/http` is enough. Frameworks such as `gin`, `fiber`, or `chi` belong in the project's `go.mod`.

For your own host projects, there is also the configurable mount `/go-projects` (variable `GO_PROJECTS_DIR`), analogous to `/java-projects`. `/workspace` is the simple default for quick exercises.

### Use Rust inside the container

Check the Rust version and Rust tools:

```bash
rustc --version
cargo --version
rustfmt --version
cargo clippy --version
rust-analyzer --version
```

Example for a small Rust project:

```bash
cd /workspace
cargo new demo-rust
cd demo-rust
cargo fmt
cargo clippy -- -D warnings
cargo run
```

Rust web frameworks are not installed globally. Frameworks and runtimes such as `tokio`, `axum`, `actix-web`, or `serde` belong in the project's `Cargo.toml`.

For your own host projects, there is also the configurable mount `/rust-projects` (variable `RUST_PROJECTS_DIR`), analogous to `/java-projects`. `/workspace` is the simple default for quick exercises.

### Use Python inside the container

Check the Python version and tools:

```bash
python --version
python3 --version
uv --version
```

Inside the container, `python` and `python3` are the same Python 3. The fast environment and package tool `uv` is also installed.

Example for a small Python program with a test:

```bash
cd /workspace
mkdir -p demo-python
cd demo-python
cat > main.py <<'EOF'
def greet(name: str) -> str:
    return f"Hello from Python, {name}"


if __name__ == "__main__":
    print(greet("ADE"))
EOF
cat > test_main.py <<'EOF'
import unittest

from main import greet


class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("ADE"), "Hello from Python, ADE")


if __name__ == "__main__":
    unittest.main()
EOF
python main.py
python -m unittest
```

`unittest` is part of the standard library and needs no installation. For additional packages, use a virtual environment so nothing is installed globally. The `python3-venv` package is present in the image:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install pytest
pytest
deactivate
```

`pip install` downloads from the network and only works with internet access. As a modern alternative, `uv` manages the environment and packages in one step, for example with `uv init` and `uv run`.

Python web frameworks are not installed globally. Frameworks such as `flask`, `django`, or `fastapi` belong in the project's virtual environment or in `pyproject.toml`.

For your own host projects, there is also the configurable mount `/python-projects` (variable `PYTHON_PROJECTS_DIR`), analogous to `/java-projects`. `/workspace` is the simple default for quick exercises.

### Scripting with Bash and PowerShell

Bash is the default shell **inside the container**. PowerShell is the shell **on the Windows host** that runs the container commands (`docker`/`podman`). `pwsh` is not installed inside the Linux container by default. Therefore, Bash scripts run inside the container and PowerShell scripts run on the host.

For Bash scripts, `shellcheck` (checking) and `shfmt` (formatting) are installed.

Check the Bash version and tools:

```bash
bash --version
shellcheck --version
shfmt --version
```

Example for a small Bash script inside the container:

```bash
cd /workspace
mkdir -p demo-bash
cd demo-bash
cat > hello.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

greet() {
  local name="$1"
  echo "Hello from Bash, ${name}"
}

greet "ADE"
EOF
shfmt -w hello.sh
shellcheck hello.sh
chmod +x hello.sh
./hello.sh
```

`shfmt -w` formats the script, `shellcheck` checks it for common mistakes, then it is made executable and started.

Check the PowerShell version on the Windows host:

```powershell
$PSVersionTable.PSVersion
```

Example for a small PowerShell script on the host:

```powershell
Set-Location $HOME
New-Item -ItemType Directory -Force demo-powershell | Out-Null
Set-Location demo-powershell
@'
function Get-Greeting {
    param([string]$Name)
    "Hello from PowerShell, $Name"
}

Get-Greeting -Name "ADE"
'@ | Set-Content hello.ps1
.\hello.ps1
```

If running is blocked, check the execution policy: `Get-ExecutionPolicy` and, if needed, `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`. Inside the container, scripts are written with Bash.

### Reach an ASP.NET web app from the host

The container publishes the local port range `5100-5199` to the host:

```yaml
ports:
  - "127.0.0.1:5100-5199:5100-5199"
```

After a change to `compose.yml`, recreate the container:

```bash
cd /Users/<user>/ade-dev-sandbox
docker compose up -d --force-recreate
docker compose exec ade bash
```

With Podman: `podman compose up -d --force-recreate` and `podman compose exec ade bash` (or `podman-compose ...` respectively).

An ASP.NET app must listen on `0.0.0.0` inside the container. `localhost` is not enough because `localhost` inside the container only means the container itself.

Example for a Razor Pages web app:

```bash
cd /rider-projects
dotnet new webapp -n WebApp1
cd WebApp1
dotnet run --urls http://0.0.0.0:5102
```

Then open this in a browser on the host:

```text
http://localhost:5102
```

Example for a minimal ASP.NET app:

```bash
cd /rider-projects
dotnet new web -n MinimalWebApp1
cd MinimalWebApp1
dotnet run --urls http://0.0.0.0:5103
```

Then open this in a browser on the host:

```text
http://localhost:5103
```

The difference: `dotnet new webapp` creates a web app with Razor Pages and more project structure. `dotnet new web` creates a very small ASP.NET app that is useful for understanding the basic idea.

If an app uses another port, it must be inside the published range `5100-5199` or be added to `compose.yml`.

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

### Use Opencode

Start Opencode inside the container:

```bash
opencode
```

The container does not start Opencode automatically. This is intentional. It lets you choose the project directory first.

For security and architecture checks, use the read-only `security-review` agent. It is meant for reviews and must not change files.

Start it interactively inside a project:

```bash
cd /rider-projects/MyProject
opencode --agent security-review
```

Then ask a concrete review question, for example:

```text
Check this project for security risks, unsafe configuration, secret leaks, and architecture issues. Do not change files; return findings with file and line references.
```

Run a one-off non-interactive review:

```bash
cd /rider-projects/MyProject
opencode run --agent security-review "Check this project for security risks, unsafe configuration, secret leaks, and architecture issues. Do not change files; return findings with file and line references."
```

If a finding should become a change, implement it afterwards with the normal `coding` agent or manually. `security-review` is intentionally limited to analysis.

### Use Codex CLI

Codex CLI is also installed inside the container:

```bash
codex --version
```

Codex does not start automatically. First switch to the project directory, then start Codex:

```bash
cd /rider-projects/MyProject
codex
```

Local Codex data is stored in the Docker volume `codex_data` under `/home/adedev/.codex`. This volume is not part of the Git repository. Credentials and private session data must not be copied into project folders or committed.

### Install Spec Kit governance presets

After `specify init`, the six governance presets can be installed in a project. The presets extend Spec Kit with binding rules for secure development, software architecture, iSAQB/arc42, accessibility, platform parity, and AI-agent parity.

For C#/.NET Level-2 projects in the home-baseline environment, the default decision is to install all six presets unless the project documents a justified exception.

Run the commands inside the target project directory in the container, for example under `/rider-projects/TinyPl0`:

```bash
cd /rider-projects/TinyPl0

specify preset add --from https://github.com/hindermath/spec-kit-preset-security-governance/archive/refs/tags/v0.2.0.zip --priority 10
specify preset add --from https://github.com/hindermath/spec-kit-preset-architecture-governance/archive/refs/tags/v0.2.0.zip --priority 20
specify preset add --from https://github.com/hindermath/spec-kit-preset-isaqb-architecture-governance/archive/refs/tags/v0.1.0.zip --priority 30
specify preset add --from https://github.com/hindermath/spec-kit-preset-a11y-governance/archive/refs/tags/v0.2.0.zip --priority 40
specify preset add --from https://github.com/hindermath/spec-kit-preset-cross-platform-governance/archive/refs/tags/v0.1.0.zip --priority 50
specify preset add --from https://github.com/hindermath/spec-kit-preset-agent-parity-governance/archive/refs/tags/v0.1.0.zip --priority 60
```

Priority controls which preset is applied first when template building blocks overlap. Lower number means higher priority. That is why `security-governance` uses priority `10`.

Verify the installation:

```bash
specify preset list
specify preset info security-governance
specify preset resolve constitution-template.md
specify preset resolve agent-guidance-addendum-template.md
git status --short
```

If the project should use the presets permanently, commit and push the preset files and generated agent/command files in the application repository:

```bash
git add .specify/presets .agents .claude .gemini .github .opencode
git commit -m "chore: configure spec-kit governance presets"
git push
```

Important: `.specify/presets/` then becomes part of the project policy. Local caches such as `.specify/presets/.cache/` should not be committed.

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
opencode --prompt "/init"
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

### Pilot: ASP.NET web app with Opencode and Spec Kit

For C#/.NET projects under `/rider-projects`, this pilot flow is a practical first end-to-end example. It creates a small Razor Pages web app, initializes Opencode, initializes Spec Kit, and then runs the project constitution command.

```bash
cd /rider-projects
mkdir -p specify-pilot
cd specify-pilot

dotnet new webapp -n SpecifyPilot -o . --force
dotnet restore
dotnet build --no-restore
```

Then start Opencode in the project and run the init command:

```bash
opencode
```

At the Opencode prompt:

```text
/init
```

If Opencode asks whether it may create or change `AGENTS.md`, only approve files in the current pilot project. Then initialize Spec Kit for Opencode:

```bash
specify init . --integration opencode --script sh --force
```

Install the six governance presets from [Install Spec Kit governance presets](#install-spec-kit-governance-presets), then verify them:

```bash
specify preset list
```

Finally, start Opencode again and create the Spec Kit constitution:

```bash
opencode
```

At the Opencode prompt:

```text
/speckit.constitution
```

A useful short input is:

```text
Project name: SpecifyPilot. Project type: ASP.NET Core Razor Pages web app in the ADE learning environment. Goal: minimal, auditable pilot constitution for apprentices and colleagues.
```

Afterwards, at least these files should exist:

```bash
test -f AGENTS.md
test -f .specify/memory/constitution.md
test -d .opencode/command
test -d .specify/presets
dotnet build --no-restore
```

The pilot evidence for this repository is documented in `docs/security/spec-kit-pilot.md`. The pilot project itself remains in the application area under `/rider-projects/specify-pilot` and is not copied into this Docker setup repository.

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

### Configuration

`opencode.jsonc` uses the `chat-ai` provider with this base URL:

```text
https://chat-ai.academiccloud.de/v1
```

The API key is read from `GWDG_API_KEY`. The default model for normal coding tasks is:

```text
chat-ai/qwen3-coder-30b-a3b-instruct
```

The default agent `coding` uses this model with focused coding parameters. `glm-4.7` remains configured as the smaller model for side tasks and as an alternative for analysis and brainstorming.

#### OpenCode hardening

The file `opencode.jsonc` contains security rules for OpenCode. This matters because OpenCode allows many actions by default when no custom `permission` rules are set. In an environment with ISO 9001 and ISO 27001 requirements, risky actions should not run without explicit approval.

The most important settings:

- `share` is set to `disabled`. OpenCode must not share sessions as public links.
- `autoupdate` is set to `false`. Updates happen in a controlled way through Dockerfile, Git commit, and image build.
- `enabled_providers` contains only `chat-ai`. Other automatically detected providers are not used.
- `permission` uses `ask` as the base rule. OpenCode asks when no narrower rule applies.
- Reading, searching, and listing inside the project are allowed. This is needed for code analysis.
- Real secret files and local tool data are blocked for reading and writing, for example `.env`, `opencode.env`, `codex.env`, `~/.ssh`, GitHub/GitLab CLI config, Docker/Podman config, Codex data, and OpenCode data.
- File changes use `ask`. OpenCode must not write files silently.
- Shell commands use `ask` by default. Simple status commands such as `pwd`, `ls`, `git status`, `git diff`, `git log`, and `git show` are allowed.
- Destructive commands such as `rm`, `sudo`, `su`, `dd`, `mkfs`, `mount`, and `umount` are blocked.
- Network access through OpenCode tools such as `webfetch`, `websearch`, and `codesearch` asks for approval.
- The `security-review` agent is meant for security and architecture reviews. It is read-only and must not change files.

When `opencode.jsonc` changes, there are two paths:

```bash
CONTAINER_NAME=$(podman ps --filter name=ade-dev-sandbox --format '{{.Names}}' | head -n 1)
podman cp opencode.jsonc "${CONTAINER_NAME}:/home/adedev/.config/opencode/opencode.jsonc"
podman exec --user root "$CONTAINER_NAME" chown adedev:adedev /home/adedev/.config/opencode/opencode.jsonc
```

With Docker instead of Podman, the same steps apply using `docker compose cp` and `docker compose exec --user root ade ...`.

This updates the running container immediately. It does not change the already built image. For new containers, rebuild the image:

```bash
podman compose build --pull
podman compose up -d --force-recreate
```

After a change, check the loaded configuration:

```bash
opencode debug config
opencode debug agent coding
opencode debug agent security-review
```

#### Codex hardening

Codex CLI is hardened as well. The configuration lives in the repository under `codex/config.toml` and `codex/requirements.toml`. During the image build, these files are copied system-wide to `/etc/codex`.

The most important settings in `codex/config.toml`:

- `approval_policy = "untrusted"`: Codex may run only a small trusted set of basic commands without approval.
- `sandbox_mode = "workspace-write"`: Codex may write inside the intended work areas, but must not run with full access.
- `web_search = "disabled"`: Web search is disabled by default.
- `check_for_update_on_startup = false`: Updates happen through Dockerfile and image build.
- `history.persistence = "none"`: Session transcripts are not persisted.
- `otel.exporter = "none"` and `log_user_prompt = false`: Telemetry is not exported and prompts are not logged.
- `sandbox_workspace_write.network_access = false`: Shell commands inside the sandbox have no direct network access.
- `sandbox_workspace_write.exclude_slash_tmp = true`: `/tmp` is not writable automatically.
- `sandbox_workspace_write.writable_roots`: write access is limited to `/workspace`, `/rider-projects`, `/java-projects`, `/go-projects`, `/rust-projects`, and `/python-projects`.
- `shell_environment_policy.inherit = "core"`: subprocesses inherit only a reduced environment.
- Secret variables with names such as `*KEY*`, `*SECRET*`, `*TOKEN*`, `*PASSWORD*`, and `*CREDENTIAL*` are removed from subprocesses.
- App, browser, and computer-use surfaces are disabled.

The file `codex/requirements.toml` sets constraints that normal user or project configuration must not weaken:

- `allowed_approval_policies = ["untrusted", "on-request"]`: the `never` mode is not allowed.
- `allowed_sandbox_modes = ["read-only", "workspace-write"]`: `danger-full-access` is not allowed.
- `allowed_web_search_modes = []`: only disabled web search is allowed.
- Secret files and local tool data are blocked for Codex, for example `.env`, `opencode.env`, `codex.env`, `~/.ssh`, Docker/Podman config, Codex data, and OpenCode data.
- Dangerous shell prefixes such as `rm`, `sudo`, `su`, `dd`, `mkfs`, `mount`, and `umount` are forbidden.
- Git write actions, container commands, network downloads, and build/package-manager commands require approval.

`codex/config.toml` is intentionally not copied to `/home/adedev/.codex/config.toml`. That directory is overlaid by the persistent Docker/Podman volume `codex_data`. A file baked into the image would not be visible there while Compose is running.

For a durable change, rebuild the image and recreate the container:

```bash
podman compose build --pull
podman compose up -d --force-recreate
```

For a running container, the configuration files can be copied for testing. This does not replace an image build and does not install a new package such as `bubblewrap`:

```bash
CONTAINER_NAME=$(podman ps --filter name=ade-dev-sandbox --format '{{.Names}}' | head -n 1)
podman exec --user root "$CONTAINER_NAME" mkdir -p /etc/codex
podman cp codex/config.toml "${CONTAINER_NAME}:/etc/codex/config.toml"
podman cp codex/config.toml "${CONTAINER_NAME}:/etc/codex/managed_config.toml"
podman cp codex/requirements.toml "${CONTAINER_NAME}:/etc/codex/requirements.toml"
podman exec --user root "$CONTAINER_NAME" chmod 0644 /etc/codex/config.toml /etc/codex/managed_config.toml /etc/codex/requirements.toml
```

With Docker instead of Podman, the same steps apply using `docker compose cp` and `docker compose exec --user root ade ...`.

After a change, roughly check the effective sandbox:

```bash
codex debug prompt-input "Test"
```

The output should show `sandbox_mode` as `workspace-write`, restricted network access, and the writable roots `/workspace`, `/rider-projects`, `/java-projects`, `/go-projects`, `/rust-projects`, and `/python-projects`.

Java JDK 21 and Maven are installed during the image build from the Debian package sources. They prepare the container for Java basics, Maven projects, and Spring Boot projects.

Go is installed during the image build as the official Go tarball under `/usr/local/go`. The version is pinned in the Dockerfile through `GO_VERSION`, so updates happen deliberately through a Dockerfile change, a Git commit, and a new image build. The image also installs `gopls`, `staticcheck`, `govulncheck`, and `dlv` under `/home/adedev/go/bin`; these tool versions are pinned through Dockerfile build arguments as well.

Rust is installed during the image build with `rustup` for the Linux user `adedev`. The toolchain is pinned in the Dockerfile through `RUST_TOOLCHAIN`. The image also installs the components `rustfmt`, `clippy`, `rust-analyzer`, and `rust-src`.

OpenCode and Codex CLI are installed during the image build as explicitly pinned npm packages. The versions are declared in the Dockerfile through `OPENCODE_VERSION` and `CODEX_VERSION`; updates happen deliberately through a Dockerfile change, Git commit, and a new image build:

```dockerfile
ARG OPENCODE_VERSION=1.14.50
ARG CODEX_VERSION=0.130.0
RUN npm i -g "opencode-ai@${OPENCODE_VERSION}" "@openai/codex@${CODEX_VERSION}"
```

The image also installs common CLI tools for agent workflows: `git`, `python`, `python3`, `jq`, `yq`, `rg`, `fd`, `fdfind`, `direnv`, `shellcheck`, `shfmt`, `delta`, `tree`, `just`, `wget`, `curl`, and `bubblewrap`. The Debian package for `fd` is named `fd-find` and provides the `fdfind` command; the image also adds the expected `fd` command as a symlink. `bubblewrap` is installed for Codex's Linux sandbox. `mas` is a macOS App Store tool and is not installed in the Linux container.

The `PATH` also includes `/usr/local/go/bin`, `/home/adedev/go/bin`, and `/home/adedev/.cargo/bin`. This makes Go, Go helper tools, and Rust tools directly available after opening a container shell.

Codex CLI stores local data in the Docker volume `codex_data`. This volume is mounted into the container at `/home/adedev/.codex`. This keeps Codex data across container restarts without writing it into the Git repository.

Spec Kit is installed during the image build with `uv`. For that reason, the image also includes `git`, `curl`, and `ca-certificates`.

After installation, Spec Kit is patched inside the container. The patch prevents Python copy operations from preserving file or directory metadata such as permissions or timestamps on host bind mounts. This is important because Windows and WSL mounts can reject these metadata operations with `Operation not permitted`.

The .NET workload notification is disabled inside the container:

```text
DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=true
MSBuildEnableWorkloadResolver=false
```

The first variable affects general update notifications. The second variable disables the MSBuild workload resolver. This is useful for normal console, library, test, and web projects because they do not need optional SDK workloads such as MAUI.

The image inherits from the shared `agent-sandbox` image on Debian 13. The base image is pinned in the Dockerfile by `sha256` digest; the readable `latest` tag stays only as a comment with the observation date. A base-image update happens deliberately through a digest change in the Dockerfile, review, Git commit, and a new image build. .NET is installed through the Microsoft package feed for Debian 13. The build argument `DOTNET_SDK_PACKAGE` defaults to `dotnet-sdk-10.0`.

The security approval is documented as a draft in `docs/security/sandbox-freigabe.md`. The MR/PR review guide for CISO/ISB or the AI officer (KIB) lives in `docs/security/sandbox-freigabe-review.md`. The isolation evidence lives in `docs/security/sandbox-isolation.md`. The related AI tool inventory lives in `docs/security/ai-tools-inventory.md`. Open `_TODO_` fields must be maintained by the owner, operations, CISO/ISB, or KIB and are not replaced with assumptions.

#### Secret Scanning

This repository uses `pre-commit` with `gitleaks` `v8.30.1` to find plaintext secrets before commits. Install the hook once before working:

```bash
uv tool install pre-commit
pre-commit install
```

Before a commit, or as a full scan:

```bash
pre-commit run --all-files
```

If `pre-commit` is not installed, the full scan can also run without persistent installation:

```bash
uvx pre-commit run --all-files
```

The Gitleaks configuration is in `.gitleaks.toml`. It extends the default rules and allows only documented placeholder values in example files such as `opencode.env.example`. Real secrets must not be allowlisted. The audit note is also recorded in `docs/security/secret-scanning.md`.

GitLab CE cannot fully enforce this local hook on the server side. Audit text: "Client-side Control, in GitLab CE nicht vollständig serverseitig erzwingbar; zentrale Push-Blockade nur mit GitLab Ultimate Secret Push Protection oder Admin-Server-Hook." As an additional control, `.gitlab-ci.yml` contains a `secret_scan` job with the same pinned Gitleaks release. This CI job detects secrets after push or in merge requests, but it does not replace central pre-receive blocking.

#### Audit Export

Agent use must be traceable as a metadata audit trail. The image therefore installs `audit-export` from `scripts/audit-export.sh`. The Compose service mounts `${AUDIT_DIR:-./audit-logs}` to `/audit`.

The export reads only file names and file timestamps from the OpenCode and Codex data directories. It does not read prompt text, response text, raw session contents, or API keys.

Run it at least once per workday and always before removing container volumes. The documented standard stop path is the wrapper, because it runs `audit-export` in the running container first and then executes `compose down`.

Windows PowerShell with Podman:

```powershell
.\scripts\compose-down-with-audit.ps1 -Engine podman
.\scripts\compose-down-with-audit.ps1 -Engine podman -Volumes
```

macOS/Linux with Podman or Docker:

```bash
bash scripts/compose-down-with-audit.sh --podman
bash scripts/compose-down-with-audit.sh --podman -v
bash scripts/compose-down-with-audit.sh --docker -v
```

If the wrapper cannot be used, run the export manually inside the container before running `docker compose down -v` or `podman compose down -v`:

```bash
audit-export
```

In addition, the image installs a best-effort stop hook through `/usr/local/bin/ade-entrypoint`. On normal `docker compose down`, `podman compose down`, or `SIGTERM`, the entrypoint runs `audit-export` once when `ADE_AUDIT_ON_STOP=true` is set. This hook is an additional safety net, not a replacement for the wrapper: hard kills, host aborts, or very short stop timeouts can still prevent the export.

The default path is:

```text
/audit/YYYY-MM-DD.jsonl
```

On the host, this file is written to `audit-logs/` by default. Real audit JSONL files stay untracked; only `audit-logs/README.md` and `audit-logs/.gitkeep` belong in the repository. The README in `audit-logs/` describes contents, access, retention, and deletion.

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

### Generate an image SBOM

An SBOM is a *Software Bill of Materials*, a machine-readable inventory for software. For this container image, it lists operating-system packages, libraries, installed tools, and versions. This supports supply-chain transparency: if a vulnerability is later disclosed for a specific component, the image can be checked for exposure.

This repository generates a CycloneDX JSON SBOM. Before distributing or handing over a rebuilt Sandbox image, this step is required.

Linux, macOS, or WSL2:

```bash
./scripts/build-and-sbom.sh
```

Windows PowerShell, for example with Podman:

```powershell
.\scripts\build-and-sbom.ps1 -Runtime podman
```

If the image is already built and only the SBOM should be regenerated:

```bash
./scripts/build-and-sbom.sh --skip-build
```

```powershell
.\scripts\build-and-sbom.ps1 -Runtime podman -SkipBuild
```

The scripts use a locally installed `syft` when it is available. If `syft` is not in `PATH`, they fall back to the container image `docker.io/anchore/syft:latest`. Docker or Podman must then be able to pull public images.

Generated files are written to `sboms/`, for example `sboms/2026-05-17-localhost-ade-dev-sandbox-ade-latest.cdx.json`. These files are build artifacts and are ignored by `.gitignore`. For releases, they can be attached separately as release artifacts.

### Analyze an image SBOM

The SBOM can be summarized and searched locally with the provided scripts. Without parameters, the newest file from `sboms/*.cdx.json` is used.

Windows PowerShell:

```powershell
.\scripts\analyze-sbom.ps1
```

macOS, Linux, or WSL2:

```bash
./scripts/analyze-sbom.sh
```

The output shows the format, CycloneDX version, generation time, component count, component types, package ecosystems from `purl`, and detected licenses.

Search for components:

```powershell
.\scripts\analyze-sbom.ps1 -Search "openssl|dotnet|node|python|rust|go"
.\scripts\analyze-sbom.ps1 -ComponentType library -Search "openssl|dotnet|node|python|rust|go"
```

```bash
./scripts/analyze-sbom.sh --search 'openssl|dotnet|node|python|rust|go'
./scripts/analyze-sbom.sh --type library --search 'openssl|dotnet|node|python|rust|go'
```

The `library` type filter hides raw file entries and is usually the most useful view for package and CVE questions.

Analyze a specific SBOM file:

```powershell
.\scripts\analyze-sbom.ps1 -SbomPath .\sboms\2026-05-17-localhost-ade-dev-sandbox-ade-latest.cdx.json
```

```bash
./scripts/analyze-sbom.sh --file sboms/2026-05-17-localhost-ade-dev-sandbox-ade-latest.cdx.json
```

Optionally run a vulnerability scan against the SBOM when `grype` or `trivy` is installed:

```powershell
.\scripts\analyze-sbom.ps1 -Scan
.\scripts\analyze-sbom.ps1 -Scan -Scanner trivy
```

```bash
./scripts/analyze-sbom.sh --scan
./scripts/analyze-sbom.sh --scan --scanner trivy
```

The Bash script uses `jq` for local summaries when available and otherwise falls back to `python3` or `python`. The PowerShell script uses `ConvertFrom-Json` and needs no additional tool for the basic analysis. CVE analysis requires one of the scanner tools, `grype` or `trivy`.

### Clean up

Stop the container but keep data:

```bash
docker compose down
```

Stop the container and delete persistent container and volume data for this Compose project:

```bash
docker compose down -v
```

These commands apply in the same way on Linux, macOS, and Windows. The important distinction is whether the environment was started with Docker or Podman. On Windows, the commands can run in PowerShell, Windows Terminal, or WSL2. The important point is to use the same container provider that started the containers.

Before cleaning up, first show how much space is used by containers, images, volumes, and build cache:

```bash
docker system df
podman system df
```

A cautious cleanup removes only unused data, for example stopped containers, unused networks, and no-longer-used images or caches. Running containers and the images and volumes used by them are kept:

```bash
docker system prune
podman system prune
```

With `-a`, all unused images are removed as well, not only unnamed intermediate images. Images used by running containers are still kept:

```bash
docker system prune -a
podman system prune -a
```

Targeted cleanup is also possible:

```bash
docker container prune
docker image prune
docker builder prune

podman container prune
podman image prune
podman image prune --build-cache
```

Volumes are the risky part because they can contain persistent data, for example `opencode_data`, `codex_data`, and `dotnet_build`. Delete volumes only when these data are intentionally no longer needed:

```bash
docker volume prune
podman volume prune
```

The hardest variant deletes unused images, containers, networks, build cache, and unused volumes. It is not the normal default command for this project:

```bash
docker system prune -a --volumes
podman system prune -a --volumes
```

### Common problems

If `docker compose` is not found, `docker-compose-v2` is usually missing:

```bash
sudo apt install -y docker-compose-v2
```

If Docker has no permission, use `sudo docker ...` or add the user to the `docker` group.

If the API key does not work, check `opencode.env`. Do not show the key in terminal history, screenshots, or Git output.

If `codex` or `opencode` exits inside the container with `Permission denied` or `EACCES` below `/home/adedev/.codex` or `/home/adedev/.local/share/opencode`, old persistent volumes probably still belong to an earlier container user. This can happen after an image or base-image change. The image already creates these directories for `adedev`, but existing volumes hide the image directories and need a one-time ownership fix.

For Podman on macOS, Windows, or WSL2, first resolve the actual container name. Depending on the Compose provider, it can be named for example `ade-dev-sandbox-ade-1` or `ade-dev-sandbox_ade_1`:

```bash
CONTAINER_NAME=$(podman ps --filter name=ade-dev-sandbox --format '{{.Names}}' | head -n 1)
podman exec --user root "$CONTAINER_NAME" bash -lc 'chown -R adedev:adedev /home/adedev/.codex /home/adedev/.local/share/opencode'
```

For Docker Compose:

```bash
docker compose exec --user root ade bash -lc 'chown -R adedev:adedev /home/adedev/.codex /home/adedev/.local/share/opencode'
```

If Podman fails with messages such as `container name "ade-dev-sandbox-ade-1" is already in use`, `container name "ade-dev-sandbox_ade_1" is already in use`, `can only create exec sessions on running containers`, or `rootlessport listen tcp 127.0.0.1:5100: bind: address already in use`, the same environment is usually still running in another Podman machine or an old container still owns the port range. Only one variant may run at a time.

Check and stop it in WSL2:

```bash
podman-compose ps
podman-compose down
```

Check and stop it on Windows in PowerShell:

```powershell
podman compose ps
podman compose down
```

Then restart the side you want to use. Example for WSL2:

```bash
podman-compose up -d
```

If .NET reports an `obj`, `bin`, `apphost`, or `Access denied` error under `/rider-projects`, rebuild and start the container:

```bash
docker compose build --pull
docker compose up -d
```

If the error points to `/dotnet-build/...`, the persistent build volume probably still belongs to an earlier container user. This can happen after an image or base-image change. Fix the volume ownership once:

```bash
CONTAINER_NAME=$(podman ps --filter name=ade-dev-sandbox --format '{{.Names}}' | head -n 1)
podman exec --user root "$CONTAINER_NAME" bash -lc 'chown -R adedev:adedev /dotnet-build'
```

With Docker Compose:

```bash
docker compose exec --user root ade bash -lc 'chown -R adedev:adedev /dotnet-build'
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

This procedure checks the setup in a useful order. It is a good choice after a fresh installation, after changes to `Dockerfile`, `compose.yml`, or `opencode.jsonc`, and as a first test on macOS with Docker Desktop.

> **Docker or Podman:** The examples use Docker. With Podman, run the same steps and replace `docker compose` with `podman compose` or `podman-compose` (see [Docker and Podman: the same commands](#docker-and-podman-the-same-commands)).

The test has two parts:

1. On the host, Docker Compose is checked, the image is built, and the container is started.
2. Inside the container, .NET, Java, Go, Rust, Python, OpenCode, Spec Kit, and the mounted directories are checked.

Run this on the host. The first command changes into this repository; adjust the path if needed:

```bash
cd /home/<user>/ade-dev-sandbox
docker compose config --no-interpolate
docker compose build --pull
docker compose up -d
docker compose ps
docker compose exec ade bash
```

Then check this inside the container:

```bash
dotnet --info
java --version
javac --version
mvn --version
go version
gopls version
rustc --version
cargo --version
cargo clippy --version
python --version
node --version
npm --version
opencode --version
codex --version
specify version
ls /workspace
ls /rider-projects
ls /java-projects
ls /go-projects
ls /rust-projects
ls /python-projects
```

What the commands mean:

- `docker compose config --no-interpolate` checks the Compose file without expanding variable values and secrets in the output.
- `docker compose build --pull` builds the image and checks or downloads the pinned base images first.
- `docker compose up -d` starts the container in the background.
- `docker compose ps` shows whether the `ade` service is running.
- `docker compose exec ade bash` opens a shell in the running container.
- `dotnet --info` shows whether the .NET SDK is installed and usable inside the container.
- `java --version`, `javac --version`, and `mvn --version` check JDK and Maven.
- `go version` and `gopls version` check Go and the Go language server.
- `rustc --version`, `cargo --version`, and `cargo clippy --version` check the Rust toolchain and Clippy.
- `python --version` checks the installed Python version.
- `node --version` and `npm --version` check the Node.js tools required by OpenCode and Codex CLI.
- `opencode --version` checks the installed OpenCode CLI.
- `codex --version` checks the installed Codex CLI.
- `specify version` checks the installed Spec Kit CLI.
- `ls /workspace` checks the local project workspace mount.
- `ls /rider-projects` checks the host mount configured through `RIDER_PROJECTS_DIR`.
- `ls /java-projects` checks the host mount configured through `JAVA_PROJECTS_DIR`.
- `ls /go-projects`, `ls /rust-projects`, and `ls /python-projects` check the language-specific host mounts.

Expected result:

- `docker compose ps` shows the `ade` service as running.
- `dotnet --info` prints SDK information and exits without an error.
- `java --version` and `mvn --version` print version information.
- `go version`, `gopls version`, `rustc --version`, `cargo --version`, `cargo clippy --version`, and `python --version` print version information.
- `opencode --version`, `codex --version`, and `specify version` print version information.
- `ls /rider-projects` shows the projects from the host directory or stays empty if that directory does not contain projects yet.
- `ls /java-projects` shows Java projects from the host directory or stays empty if that directory does not contain projects yet.
- `ls /go-projects`, `ls /rust-projects`, and `ls /python-projects` show language-specific projects or stay empty.

macOS note: If Docker Desktop was just installed, start Docker Desktop once and wait until the engine is running. After that, `docker --version`, `docker compose version`, and `docker info` work in the terminal.

Windows note: If Docker Desktop is used from PowerShell, set `RIDER_PROJECTS_DIR` in `.env` as a Windows path, for example `C:\Users\<user>\RiderProjects`. If the commands run from Ubuntu/WSL2, use the WSL path, for example `/mnt/c/Users/<user>/RiderProjects`.

Security note: `opencode.env` contains the API key. Never commit this file, never show it in screenshots, and do not copy it into chat or ticket systems. For tests, it is enough to check that OpenCode starts; the key must not be made visible.

If the build should intentionally run fully fresh:

```bash
docker compose build --pull --no-cache
docker compose up -d --force-recreate
```

### Quick rules

> **Docker or Podman:** The following `docker` commands apply to Podman in the same way (`podman compose` or `podman-compose`), see [Docker and Podman: the same commands](#docker-and-podman-the-same-commands).

- After changes to the `Dockerfile`, always rebuild:

```bash
docker compose build --pull --no-cache
docker compose up -d --force-recreate
```

- After changes only to `compose.yml`, this is usually enough:

```bash
docker compose up -d --force-recreate
```

- ASP.NET apps must listen on `0.0.0.0` inside the container:

```bash
dotnet run --urls http://0.0.0.0:5102
```

- Windows can then reach web apps through `http://localhost:<port>`.
- The local published port range is `5100-5199`.
- `opencode.env` contains a secret and must not be committed.
- `opencode.jsonc` is the commented OpenCode configuration for the container.
- `specify-cli` is intentionally pinned to a version. Updates are made manually in the Dockerfile.
- For new projects under `/rider-projects`, initialize inside the project:

```bash
opencode --prompt "/init"
specify init . --integration opencode --force
```

- If Spec Kit asks for script type, choose `sh`.
- OpenCode project rules belong in the project's own `AGENTS.md`.
- `.opencode/` can contain sensitive data. Decide per project whether the folder or parts of it belong in `.gitignore`.
- For `bin`, `obj`, or `apphost` errors, check:

```bash
echo "$DirectoryBuildPropsPath"
ls /dotnet-config/ContainerBuild.props
ls /dotnet-build
```

### Glossary

This glossary explains the most important terms in simple form. If you do not know a term, check here before reading on.

| Term | Meaning |
|---|---|
| Agent | An AI program such as OpenCode or Codex that can run tasks inside the container. |
| API key | A secret value that lets a program use an online service. Like a password, but for machines. |
| ASP.NET | Microsoft's web framework for server-side web applications in C#. |
| Bind mount | A directory from the host mounted directly into the container. Changes propagate in both directions. |
| Build | The step that turns source code into a runnable program. |
| Cargo | Build and package tool for Rust projects. |
| Compose | A tool that starts and stops containers based on a `compose.yml` file. |
| Container | An isolated Linux process started from an image. Like a small virtual environment, but lighter than a virtual machine. |
| Dockerfile | A text file that describes how an image is built. |
| Engine | The background daemon for Docker or Podman. Without an engine, no container. |
| Host | Your own computer. The opposite of the container. |
| Image | The template for containers. Many containers can be started from one image. |
| JDK | Java Development Kit. Contains the compiler `javac` and the runtime `java`. |
| JSONC | JSON that allows comments. Used in `opencode.jsonc`. |
| Maven | A tool for Java projects. Builds projects and manages dependencies. |
| MSBuild | Microsoft's build tool for .NET projects. |
| Mount | In general: attach a directory somewhere. Here usually a bind mount or a volume. |
| .NET SDK | Software Development Kit for the programming languages C#, F#, and VB.NET. |
| Podman | An alternative to Docker. Runs without a daemon and usually needs no root rights. |
| Port | A numbered door on a computer through which network services are reached. |
| Provider | Here: the supplier of an AI model, for example `chat-ai`. |
| Registry | An online storage for container images, for example the GitLab Container Registry. |
| Rider | An integrated development environment (IDE) from JetBrains for .NET. |
| Rootless | Without administrator or root rights. Podman runs rootless by default. |
| Rustup | A tool that installs Rust toolchains and components such as `rustfmt` or `clippy`. |
| Sandbox | A protected environment in which a program may not write everywhere. |
| SDD | Spec-Driven Development. Describe first, then plan, then implement. |
| Secret | A secret value such as an API key or a password. |
| Service | A named container in `compose.yml`. In this repository: `ade`. |
| Shell | A program such as Bash for typing commands. |
| Spec Kit | A CLI that provides a fixed flow for producing software specifications. |
| Volume | Storage managed by Docker or Podman, separate from the host file system. |
| WSL2 | Windows Subsystem for Linux Version 2. A real Linux environment inside Windows. |

### Accessibility

This README aims to meet WCAG 2.2 Level AA as far as Markdown on GitHub allows.

| WCAG criterion | Implementation |
|---|---|
| 1.3.1 Info and relationships | Consistent heading hierarchy H1 → H2 → H3 → H4. Tables with header rows. Lists instead of running text where it fits. |
| 1.4.1 Use of color | No information conveyed by color alone. Status is expressed by words such as *allowed*, *blocked*, *asks*. |
| 2.4.4 Link purpose | Descriptive link texts in the table of contents. No "click here" wording. |
| 2.4.6 Headings and labels | Bilingual headings at the top. Clear, self-contained section headings. |
| 3.1.1 Language of the page | Main language German in the DE block, English in the EN block. (Platform limitation: GitHub Markdown does not support a `lang` attribute.) |
| 3.1.5 Reading level | Target reading level CEFR B2. Short sentences. Technical terms are introduced and explained in the glossary. |
| 4.1.1 Parsing | All code blocks carry a language tag (`bash`, `powershell`, `yaml`, `dockerfile`, `text` …). |
| 4.1.2 Name, role, value | Standard Markdown elements only. No embedded HTML components with custom logic. |

Known platform limitations:

- WCAG 3.1.2 (Language of parts): GitHub strips HTML `lang` attributes. Language switches between DE and EN are signaled only through section headings.
- Long code blocks can cause horizontal scrolling on small screens. This is a Markdown limitation.

Tips for learners using a screen reader or Braille display:

- Use the table of contents to jump quickly into the right section.
- Inside a section, the steps are organized as numbered or unordered lists.
- A code block is always introduced by a sentence that explains what comes next.
