# Opencode Docker-Umgebung

## Inhaltsverzeichnis

- [Deutsch](#deutsch)
  - [Zielgruppe und Zweck](#zielgruppe-und-zweck)
  - [Grundidee](#grundidee)
  - [Projektstruktur](#projektstruktur)
  - [Docker unter Ubuntu oder WSL2 installieren](#docker-unter-ubuntu-oder-wsl2-installieren)
  - [Docker-Desktop-Profile fuer macOS und Windows](#docker-desktop-profile-fuer-macos-und-windows)
  - [Docker-Berechtigungen pruefen](#docker-berechtigungen-pruefen)
  - [API-Key einrichten](#api-key-einrichten)
  - [Container bauen und starten](#container-bauen-und-starten)
  - [Rider-Projekte aus Windows einbinden](#rider-projekte-aus-windows-einbinden)
  - [.NET und C# im Container nutzen](#net-und-c-im-container-nutzen)
  - [ASP.NET-Web-App aus Windows erreichen](#aspnet-web-app-aus-windows-erreichen)
  - [Spec Kit verwenden](#spec-kit-verwenden)
  - [Beispiel: ConsoleApp2 mit Opencode und Spec Kit](#beispiel-consoleapp2-mit-opencode-und-spec-kit)
  - [Pflichtablauf fuer ein SDD-Feature](#pflichtablauf-fuer-ein-sdd-feature)
  - [Opencode verwenden](#opencode-verwenden)
  - [Codex CLI verwenden](#codex-cli-verwenden)
  - [Konfiguration](#konfiguration)
  - [Aufraeumen](#aufraeumen)
  - [Haeufige Probleme](#haeufige-probleme)
  - [Kompakter Testablauf](#kompakter-testablauf)
  - [Merksaetze](#merksaetze)
- [English](#english)
  - [Target group and purpose](#target-group-and-purpose)
  - [Basic idea](#basic-idea)
  - [Project structure](#project-structure)
  - [Install Docker on Ubuntu or WSL2](#install-docker-on-ubuntu-or-wsl2)
  - [Docker Desktop profiles for macOS and Windows](#docker-desktop-profiles-for-macos-and-windows)
  - [Check Docker permissions](#check-docker-permissions)
  - [Set up the API key](#set-up-the-api-key)
  - [Build and start the container](#build-and-start-the-container)
  - [Mount Rider projects from Windows](#mount-rider-projects-from-windows)
  - [Use .NET and C# inside the container](#use-net-and-c-inside-the-container)
  - [Reach an ASP.NET web app from Windows](#reach-an-aspnet-web-app-from-windows)
  - [Use Spec Kit](#use-spec-kit)
  - [Example: ConsoleApp2 with Opencode and Spec Kit](#example-consoleapp2-with-opencode-and-spec-kit)
  - [Required flow for an SDD feature](#required-flow-for-an-sdd-feature)
  - [Use Opencode](#use-opencode)
  - [Use Codex CLI](#use-codex-cli)
  - [Configuration](#configuration)
  - [Clean up](#clean-up)
  - [Common problems](#common-problems)
  - [Compact test procedure](#compact-test-procedure)
  - [Quick rules](#quick-rules)

## Deutsch

### Zielgruppe und Zweck

Diese Anleitung richtet sich an Auszubildende der Fachinformatik ab dem 1. Lehrjahr. Sie erklaert nicht nur die Befehle, sondern auch kurz, warum sie gebraucht werden.

Dieses Repository stellt eine Docker-Umgebung fuer Opencode, .NET und C# bereit. Die Umgebung laeuft mit Docker Engine unter Linux/WSL2 und mit Docker Desktop unter macOS oder Windows. Projekte koennen weiter mit JetBrains Rider auf dem Host bearbeitet werden.

### Grundidee

Docker erstellt aus dem `Dockerfile` ein Image. Aus diesem Image startet Docker Compose einen Container. Der Container enthaelt das aktuelle Microsoft .NET SDK, Node.js, npm, Opencode und Codex CLI.

Der Container bleibt im Hintergrund aktiv. Danach kann eine Shell im Container geoeffnet werden. Dort koennen Befehle wie `dotnet`, `opencode`, `codex` oder `ls` ausgefuehrt werden.

Die Shell laeuft im Container als Linux-Benutzer `adedev`. Deshalb beginnt die Promptzeile nach dem Einstieg zum Beispiel mit `adedev@...`. Der Compose-Service heisst `ade`; das OpenCode-Programm heisst weiterhin `opencode`.

### Projektstruktur

- `Dockerfile`: beschreibt das Container-Image. Es nutzt `mcr.microsoft.com/dotnet/sdk:latest`.
- `compose.yml`: beschreibt den Service `ade`, Volumes und Build-Regeln.
- `.env.example`: Vorlage fuer den plattformabhaengigen `RIDER_PROJECTS_DIR`-Mount.
- `opencode.jsonc`: enthaelt Provider, Modelle und Agenten fuer Opencode. JSONC erlaubt Kommentare und ist deshalb fuer Lernzwecke besser lesbar.
- `opencode.env.example`: Vorlage fuer die lokale Datei `opencode.env`.
- `workspace/`: lokales Arbeitsverzeichnis, im Container unter `/workspace`.
- `RIDER_PROJECTS_DIR`: Host-Verzeichnis fuer Rider-Projekte, im Container unter `/rider-projects`.
- `dotnet/ContainerBuild.props`: leitet .NET-Build-Artefakte fuer Rider-Projekte in das Container-Volume `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: filtert eine bekannte .NET-Workload-Verifikationsmeldung aus der Ausgabe.
- `spec-kit/patch-specify-cli.py`: passt Spec Kit fuer Windows-/WSL-Bind-Mounts an.
- `codex_data`: Docker-Volume fuer Codex CLI-Daten unter `/home/adedev/.codex`.
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

### Docker-Desktop-Profile fuer macOS und Windows

Wenn Docker Desktop verwendet wird, bleibt der Container ein Linux-Container. Der Unterschied liegt nur im Host-Pfad, der nach `/rider-projects` eingebunden wird.

Docker Desktop kann fuer private Nutzung, Ausbildung, Lernen, kleine Unternehmen und nicht-kommerzielle Open-Source-Projekte kostenlos genutzt werden. Kommerzielle Nutzung in groesseren Unternehmen mit mehr als 250 Mitarbeitenden oder mehr als 10 Mio. USD Jahresumsatz benoetigt ein bezahltes Docker-Abo. Im Zweifel gelten die aktuellen Docker Subscription Service Agreement Bedingungen.

macOS mit Homebrew:

```bash
brew install --cask docker
open -a Docker
```

Danach im Terminal pruefen:

```bash
docker --version
docker compose version
docker info
```

Windows mit Winget:

```powershell
winget install --id Docker.DockerDesktop -e
```

Danach Docker Desktop aus dem Startmenue starten, die Lizenzbedingungen akzeptieren und sicherstellen, dass das WSL2-Backend aktiviert ist. Alternativ kann der Installer von der offiziellen Docker-Webseite verwendet werden.

Zuerst die Compose-Umgebungsdatei anlegen:

```bash
cp .env.example .env
```

Danach `RIDER_PROJECTS_DIR` passend zur Plattform setzen.

macOS:

```text
RIDER_PROJECTS_DIR=/Users/thorstenhindermann/RiderProjects
```

Windows mit Docker Desktop aus PowerShell:

```text
RIDER_PROJECTS_DIR=C:\Users\thinder\RiderProjects
```

Windows mit Docker Desktop aus Ubuntu/WSL2:

```text
RIDER_PROJECTS_DIR=/mnt/c/Users/thinder/RiderProjects
```

Wenn kein separates Rider-Projektverzeichnis gebraucht wird, kann der Standard aus `.env.example` bleiben. Dann zeigt `/rider-projects` wie `/workspace` auf das lokale `workspace/`-Verzeichnis.

Die Datei `.env` enthaelt keine Secrets, ist aber lokal und plattformabhaengig. Sie wird nicht committed. Der API-Key bleibt getrennt in `opencode.env`.

Konfiguration pruefen:

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

Das Host-Verzeichnis fuer Rider-Projekte wird ueber `RIDER_PROJECTS_DIR` gesetzt. Typische Werte sind:

```text
RIDER_PROJECTS_DIR=/mnt/c/Users/thinder/RiderProjects
RIDER_PROJECTS_DIR=C:\Users\thinder\RiderProjects
RIDER_PROJECTS_DIR=/Users/thorstenhindermann/RiderProjects
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

Aenderungen im Container wirken direkt auf die Host-Dateien. Rider auf dem Host sieht dieselben Dateien. Builds auf Windows- oder macOS-Bind-Mounts koennen langsamer sein als Builds im Linux-Dateisystem.

Damit .NET auf Host-Dateien keine Probleme mit `bin`, `obj`, AppHost-Dateien oder Dateizeitstempeln bekommt, wird eine MSBuild-Konfiguration in den Container eingebunden:

```text
dotnet/ContainerBuild.props -> /dotnet-config/ContainerBuild.props
```

Compose setzt dazu die Umgebungsvariable `DirectoryBuildPropsPath`. Dadurch wird die Konfiguration sehr frueh im MSBuild-Ablauf geladen. Repo-eigene `Directory.Build.props`-Dateien werden von `ContainerBuild.props` weiter importiert, damit projektspezifische Einstellungen erhalten bleiben.

Die Build-Artefakte liegen nicht unter `/rider-projects`, sondern im Linux-Volume `/dotnet-build`. Das verhindert typische Fehler wie `Access to the path ... obj ... is denied` oder Fehler beim Erstellen von `apphost`.

### .NET und C# im Container nutzen

Shell im Container oeffnen:

```bash
docker compose exec ade bash
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

`dotnet new console` erstellt eine einfache Konsolenanwendung. `dotnet run` baut und startet das Projekt. Die Dateien liegen auf dem Host im `RIDER_PROJECTS_DIR`-Verzeichnis und koennen dort mit Rider geoeffnet werden.

Wenn ein Projekt bereits fehlerhafte `bin`- oder `obj`-Ordner auf dem Windows-Mount hat, koennen diese in Rider oder im Terminal geloescht werden. Danach erneut im Container bauen.

### ASP.NET-Web-App vom Host erreichen

Der Container gibt die lokale Port-Range `5100-5199` an den Host frei:

```yaml
ports:
  - "127.0.0.1:5100-5199:5100-5199"
```

Nach einer Aenderung an `compose.yml` muss der Container neu erstellt werden:

```bash
cd /Users/thorstenhindermann/ade-dev-sandbox
docker compose up -d --force-recreate
docker compose exec ade bash
```

Eine ASP.NET-App muss im Container auf `0.0.0.0` lauschen. `localhost` reicht nicht, weil `localhost` im Container nur den Container selbst meint.

Beispiel fuer eine Razor-Pages-Web-App:

```bash
cd /rider-projects
dotnet new webapp -n WebApp1
cd WebApp1
dotnet run --urls http://0.0.0.0:5102
```

Danach auf dem Host im Browser oeffnen:

```text
http://localhost:5102
```

Beispiel fuer eine minimale ASP.NET-App:

```bash
cd /rider-projects
dotnet new web -n MinimalWebApp1
cd MinimalWebApp1
dotnet run --urls http://0.0.0.0:5103
```

Danach auf dem Host im Browser oeffnen:

```text
http://localhost:5103
```

Der Unterschied: `dotnet new webapp` erstellt eine Web-App mit Razor Pages und mehr Projektstruktur. `dotnet new web` erstellt eine sehr kleine ASP.NET-App, die gut zum Verstehen des Grundprinzips ist.

Wenn eine App einen anderen Port nutzt, muss dieser in der freigegebenen Range `5100-5199` liegen oder in `compose.yml` zusaetzlich eingetragen werden.

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
opencode --prompt "/init"
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

### Codex CLI verwenden

Codex CLI ist ebenfalls im Container installiert:

```bash
codex --version
```

Codex startet nicht automatisch. Fuer ein Projekt zuerst in das Projektverzeichnis wechseln und dann Codex starten:

```bash
cd /rider-projects/MeinProjekt
codex
```

Lokale Codex-Daten liegen im Docker-Volume `codex_data` unter `/home/adedev/.codex`. Dieses Volume ist nicht Teil des Git-Repositories. Zugangsdaten und private Sitzungsdaten duerfen nicht in Projektordner kopiert oder committed werden.

### Konfiguration

`opencode.jsonc` nutzt den Provider `chat-ai` mit dieser Basis-URL:

```text
https://chat-ai.academiccloud.de/v1
```

Der API-Key wird aus `GWDG_API_KEY` gelesen. Das Standardmodell ist:

```text
chat-ai/glm-4.7
```

Opencode und Codex CLI werden beim Image-Build mit der neuesten npm-Version installiert:

```dockerfile
RUN npm i -g opencode-ai@latest @openai/codex@latest
```

Codex CLI speichert lokale Daten im Docker-Volume `codex_data`. Dieses Volume wird im Container nach `/home/adedev/.codex` eingebunden. Dadurch bleiben Codex-Daten zwischen Container-Neustarts erhalten, ohne dass sie in das Git-Repository geschrieben werden.

Spec Kit wird beim Image-Build mit `uv` installiert. Dafuer enthaelt das Image auch `git`, `curl` und `ca-certificates`.

Nach der Installation wird Spec Kit im Container gepatcht. Der Patch verhindert, dass Python-Kopiervorgaenge Dateirechte oder Zeitstempel auf Host-Bind-Mounts uebernehmen wollen. Das ist wichtig, weil Windows- und WSL-Mounts solche Metadatenoperationen mit `Operation not permitted` ablehnen koennen.

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

Dieser Ablauf prueft das Setup in einer sinnvollen Reihenfolge. Er eignet sich gut nach einer Neuinstallation, nach Aenderungen an `Dockerfile`, `compose.yml` oder `opencode.jsonc` und als erster Test auf macOS mit Docker Desktop.

Der Test besteht aus zwei Teilen:

1. Auf dem Host wird Docker Compose geprueft, das Image gebaut und der Container gestartet.
2. Im Container wird geprueft, ob .NET, OpenCode, Spec Kit und die gemounteten Verzeichnisse funktionieren.

Auf dem Host ausfuehren:

```bash
cd /Users/thorstenhindermann/ade-dev-sandbox
docker compose config --no-interpolate
docker compose build --pull
docker compose up -d
docker compose ps
docker compose exec ade bash
```

Danach im Container pruefen:

```bash
dotnet --info
node --version
npm --version
opencode --version
codex --version
specify version
ls /workspace
ls /rider-projects
```

Was die Befehle bedeuten:

- `docker compose config --no-interpolate` prueft die Compose-Datei, ohne Variablenwerte und Secrets in der Ausgabe auszubreiten.
- `docker compose build --pull` baut das Image und laedt vorher nach Moeglichkeit aktuelle Basisimages.
- `docker compose up -d` startet den Container im Hintergrund.
- `docker compose ps` zeigt, ob der Service `ade` laeuft.
- `docker compose exec ade bash` oeffnet eine Shell im laufenden Container.
- `dotnet --info` zeigt, ob das .NET SDK im Container installiert und nutzbar ist.
- `node --version` und `npm --version` pruefen die Node.js-Werkzeuge, die OpenCode und Codex CLI brauchen.
- `opencode --version` prueft die installierte OpenCode CLI.
- `codex --version` prueft die installierte Codex CLI.
- `specify version` prueft die installierte Spec Kit CLI.
- `ls /workspace` prueft das lokale Projekt-Workspace-Mount.
- `ls /rider-projects` prueft den ueber `RIDER_PROJECTS_DIR` konfigurierten Host-Mount.

Erwartetes Ergebnis:

- `docker compose ps` zeigt den Service `ade` als laufend.
- `dotnet --info` gibt SDK-Informationen aus und endet ohne Fehler.
- `opencode --version`, `codex --version` und `specify version` geben Versionsinformationen aus.
- `ls /rider-projects` zeigt die Projekte aus dem Host-Verzeichnis oder bleibt leer, wenn das Verzeichnis noch keine Projekte enthaelt.

macOS-Hinweis: Wenn Docker Desktop gerade erst installiert wurde, Docker Desktop zuerst einmal starten und warten, bis die Engine laeuft. Danach funktionieren `docker --version`, `docker compose version` und `docker info` im Terminal.

Windows-Hinweis: Wenn Docker Desktop aus PowerShell verwendet wird, muss `RIDER_PROJECTS_DIR` in `.env` als Windows-Pfad gesetzt werden, zum Beispiel `C:\Users\thinder\RiderProjects`. Wenn die Befehle aus Ubuntu/WSL2 laufen, wird der WSL-Pfad verwendet, zum Beispiel `/mnt/c/Users/thinder/RiderProjects`.

Sicherheits-Hinweis: `opencode.env` enthaelt den API-Key. Diese Datei nie committen, nie in Screenshots zeigen und nicht in Chat- oder Ticket-Systeme kopieren. Fuer Tests reicht es, zu pruefen, dass OpenCode startet; der Key muss nicht sichtbar gemacht werden.

Wenn der Build bewusst komplett frisch laufen soll:

```bash
docker compose build --pull --no-cache
docker compose up -d --force-recreate
```

### Merksaetze

- Nach Aenderungen am `Dockerfile` immer neu bauen:

```bash
docker compose build --pull --no-cache
docker compose up -d --force-recreate
```

- Nach reinen Aenderungen an `compose.yml` reicht meistens:

```bash
docker compose up -d --force-recreate
```

- ASP.NET-Apps muessen im Container auf `0.0.0.0` lauschen:

```bash
dotnet run --urls http://0.0.0.0:5102
```

- Windows erreicht Web-Apps dann ueber `http://localhost:<port>`.
- Freigegeben ist lokal die Port-Range `5100-5199`.
- `opencode.env` enthaelt ein Secret und darf nicht committed werden.
- `opencode.jsonc` ist die kommentierte OpenCode-Konfiguration fuer den Container.
- `specify-cli` ist bewusst auf eine Version gepinnt. Updates werden manuell im Dockerfile gemacht.
- Fuer neue Projekte unter `/rider-projects` zuerst projektlokal initialisieren:

```bash
opencode --prompt "/init"
specify init . --integration opencode --force
```

- Wenn Spec Kit nach dem Script-Typ fragt, `sh` waehlen.
- Projektregeln fuer OpenCode gehoeren in die jeweilige Projektdatei `AGENTS.md`.
- `.opencode/` kann sensible Daten enthalten. Pro Projekt entscheiden, ob der Ordner ganz oder teilweise in `.gitignore` gehoert.
- Bei `bin`-, `obj`- oder `apphost`-Fehlern pruefen:

```bash
echo "$DirectoryBuildPropsPath"
ls /dotnet-config/ContainerBuild.props
ls /dotnet-build
```

## English

### Target group and purpose

This guide is written for first-year IT specialist apprentices and later. It explains the commands and also why they are needed.

This repository provides a Docker environment for Opencode, .NET, and C#. It runs with Docker Engine on Linux/WSL2 and with Docker Desktop on macOS or Windows. Projects can still be edited with JetBrains Rider on the host.

### Basic idea

Docker builds an image from the `Dockerfile`. Docker Compose starts a container from that image. The container includes the current Microsoft .NET SDK, Node.js, npm, Opencode, and Codex CLI.

The container stays active in the background. You can then open a shell inside it and run commands such as `dotnet`, `opencode`, `codex`, or `ls`.

The shell runs as the Linux user `adedev` inside the container. That is why the prompt starts with something like `adedev@...` after entering the container. The Compose service is named `ade`; the OpenCode command is still named `opencode`.

### Project structure

- `Dockerfile`: describes the container image. It uses `mcr.microsoft.com/dotnet/sdk:latest`.
- `compose.yml`: describes the `ade` service, volumes, and build rules.
- `.env.example`: template for the platform-specific `RIDER_PROJECTS_DIR` mount.
- `opencode.jsonc`: contains provider, model, and agent settings for Opencode. JSONC allows comments and is easier to read for learning.
- `opencode.env.example`: template for the local `opencode.env` file.
- `workspace/`: local working directory, mounted as `/workspace`.
- `RIDER_PROJECTS_DIR`: host directory for Rider projects, mounted as `/rider-projects`.
- `dotnet/ContainerBuild.props`: redirects .NET build artifacts for Rider projects to the container volume `/dotnet-build`.
- `dotnet/dotnet-wrapper.sh`: filters a known .NET workload verification message from command output.
- `spec-kit/patch-specify-cli.py`: adapts Spec Kit for Windows/WSL bind mounts.
- `codex_data`: Docker volume for Codex CLI data under `/home/adedev/.codex`.
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

### Docker Desktop profiles for macOS and Windows

When Docker Desktop is used, the container is still a Linux container. Only the host path mounted into `/rider-projects` changes.

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

Then set `RIDER_PROJECTS_DIR` for the current platform.

macOS:

```text
RIDER_PROJECTS_DIR=/Users/thorstenhindermann/RiderProjects
```

Windows with Docker Desktop from PowerShell:

```text
RIDER_PROJECTS_DIR=C:\Users\thinder\RiderProjects
```

Windows with Docker Desktop from Ubuntu/WSL2:

```text
RIDER_PROJECTS_DIR=/mnt/c/Users/thinder/RiderProjects
```

If no separate Rider project directory is needed, keep the default from `.env.example`. Then `/rider-projects` points to the local `workspace/` directory, just like `/workspace`.

The `.env` file contains no secrets, but it is local and platform-specific. It is not committed. The API key stays separate in `opencode.env`.

Check the configuration:

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

The host directory for Rider projects is set through `RIDER_PROJECTS_DIR`. Typical values are:

```text
RIDER_PROJECTS_DIR=/mnt/c/Users/thinder/RiderProjects
RIDER_PROJECTS_DIR=C:\Users\thinder\RiderProjects
RIDER_PROJECTS_DIR=/Users/thorstenhindermann/RiderProjects
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

### Reach an ASP.NET web app from the host

The container publishes the local port range `5100-5199` to the host:

```yaml
ports:
  - "127.0.0.1:5100-5199:5100-5199"
```

After a change to `compose.yml`, recreate the container:

```bash
cd /Users/thorstenhindermann/ade-dev-sandbox
docker compose up -d --force-recreate
docker compose exec ade bash
```

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

### Configuration

`opencode.jsonc` uses the `chat-ai` provider with this base URL:

```text
https://chat-ai.academiccloud.de/v1
```

The API key is read from `GWDG_API_KEY`. The default model is:

```text
chat-ai/glm-4.7
```

Opencode and Codex CLI are installed during the image build with the newest npm version:

```dockerfile
RUN npm i -g opencode-ai@latest @openai/codex@latest
```

Codex CLI stores local data in the Docker volume `codex_data`. This volume is mounted into the container at `/home/adedev/.codex`. This keeps Codex data across container restarts without writing it into the Git repository.

Spec Kit is installed during the image build with `uv`. For that reason, the image also includes `git`, `curl`, and `ca-certificates`.

After installation, Spec Kit is patched inside the container. The patch prevents Python copy operations from preserving file permissions or timestamps on host bind mounts. This is important because Windows and WSL mounts can reject these metadata operations with `Operation not permitted`.

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

This procedure checks the setup in a useful order. It is a good choice after a fresh installation, after changes to `Dockerfile`, `compose.yml`, or `opencode.jsonc`, and as a first test on macOS with Docker Desktop.

The test has two parts:

1. On the host, Docker Compose is checked, the image is built, and the container is started.
2. Inside the container, .NET, OpenCode, Spec Kit, and the mounted directories are checked.

Run this on the host:

```bash
cd /Users/thorstenhindermann/ade-dev-sandbox
docker compose config --no-interpolate
docker compose build --pull
docker compose up -d
docker compose ps
docker compose exec ade bash
```

Then check this inside the container:

```bash
dotnet --info
node --version
npm --version
opencode --version
codex --version
specify version
ls /workspace
ls /rider-projects
```

What the commands mean:

- `docker compose config --no-interpolate` checks the Compose file without expanding variable values and secrets in the output.
- `docker compose build --pull` builds the image and tries to download current base images first.
- `docker compose up -d` starts the container in the background.
- `docker compose ps` shows whether the `ade` service is running.
- `docker compose exec ade bash` opens a shell in the running container.
- `dotnet --info` shows whether the .NET SDK is installed and usable inside the container.
- `node --version` and `npm --version` check the Node.js tools required by OpenCode and Codex CLI.
- `opencode --version` checks the installed OpenCode CLI.
- `codex --version` checks the installed Codex CLI.
- `specify version` checks the installed Spec Kit CLI.
- `ls /workspace` checks the local project workspace mount.
- `ls /rider-projects` checks the host mount configured through `RIDER_PROJECTS_DIR`.

Expected result:

- `docker compose ps` shows the `ade` service as running.
- `dotnet --info` prints SDK information and exits without an error.
- `opencode --version`, `codex --version`, and `specify version` print version information.
- `ls /rider-projects` shows the projects from the host directory or stays empty if that directory does not contain projects yet.

macOS note: If Docker Desktop was just installed, start Docker Desktop once and wait until the engine is running. After that, `docker --version`, `docker compose version`, and `docker info` work in the terminal.

Windows note: If Docker Desktop is used from PowerShell, set `RIDER_PROJECTS_DIR` in `.env` as a Windows path, for example `C:\Users\thinder\RiderProjects`. If the commands run from Ubuntu/WSL2, use the WSL path, for example `/mnt/c/Users/thinder/RiderProjects`.

Security note: `opencode.env` contains the API key. Never commit this file, never show it in screenshots, and do not copy it into chat or ticket systems. For tests, it is enough to check that OpenCode starts; the key must not be made visible.

If the build should intentionally run fully fresh:

```bash
docker compose build --pull --no-cache
docker compose up -d --force-recreate
```

### Quick rules

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
