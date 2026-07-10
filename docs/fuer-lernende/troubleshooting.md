# Fehlerbehebung / Troubleshooting

**Stand / Date:** 2026-07-10
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

**DE:** Dieses Dokument sammelt typische Anfängerfehler beim ersten Start der
Sandbox. Jeder Eintrag folgt dem Muster **Symptom → Ursache → Lösung**. Suche
den Fehler, der zu deiner Meldung passt.

**EN:** This document collects typical beginner mistakes during the first start
of the sandbox. Each entry follows the pattern **symptom → cause → solution**.
Look for the error that matches your message.

---

## `command not found` bei `podman` oder `git` / `command not found` for `podman` or `git`

**DE:**

- **Symptom:** Das Terminal antwortet mit `podman: command not found` oder
  `git: command not found`.
- **Ursache:** Das Werkzeug ist noch nicht installiert oder nicht im Suchpfad.
- **Lösung:** Folge dem passenden Abschnitt in [installation.md](installation.md)
  (macOS: `brew`, Windows: Podman Desktop, Linux: `apt`). Öffne danach ein
  **neues** Terminal, damit der Suchpfad neu geladen wird.

**EN:**

- **Symptom:** The terminal answers with `podman: command not found` or
  `git: command not found`.
- **Cause:** The tool is not installed yet or not in the search path.
- **Solution:** Follow the matching section in
  [installation.md](installation.md) (macOS: `brew`, Windows: Podman Desktop,
  Linux: `apt`). Then open a **new** terminal so the search path reloads.

---

## `podman machine init` oder `start` schlägt fehl / `podman machine init` or `start` Fails

**DE:**

- **Symptom:** Ein Fehler wie `Error: machine ... already exists` oder die
  Machine startet nicht.
- **Ursache:** Auf macOS und Windows braucht Podman eine Linux-VM
  (Podman-Machine). Sie fehlt, ist beschädigt oder läuft schon.
- **Lösung:** Prüfe den Zustand mit `podman machine list`. Läuft sie noch nicht,
  starte mit `podman machine start`. Ist sie beschädigt, entferne und erstelle
  sie neu:

**EN:**

- **Symptom:** An error like `Error: machine ... already exists` or the machine
  does not start.
- **Cause:** On macOS and Windows Podman needs a Linux VM (Podman machine). It
  is missing, damaged, or already running.
- **Solution:** Check the state with `podman machine list`. If it is not running,
  start with `podman machine start`. If it is damaged, remove and recreate it:

```bash
podman machine stop
podman machine rm
podman machine init
podman machine start
```

**DE:** Auf Linux gibt es keine Podman-Machine — dort ist dieser Fehler nicht
möglich.

**EN:** On Linux there is no Podman machine — this error cannot occur there.

---

## Port 5100–5199 ist belegt / Port 5100–5199 Is in Use

**DE:**

- **Symptom:** Beim Start erscheint `address already in use` oder `bind:
  address already in use` für einen Port zwischen 5100 und 5199.
- **Ursache:** Ein anderes Programm belegt bereits den Port. Der Container
  veröffentlicht `127.0.0.1:5100-5199` für Web-App-Tests.
- **Lösung:** Beende das andere Programm oder wähle für deine Test-App einen
  freien Port aus dem Bereich 5100–5199. Ändere die Portspanne **nicht** in
  `compose.yml`, außer die Aufgabe verlangt es ausdrücklich.

**EN:**

- **Symptom:** On start you see `address already in use` or `bind: address
  already in use` for a port between 5100 and 5199.
- **Cause:** Another program already uses the port. The container publishes
  `127.0.0.1:5100-5199` for web app tests.
- **Solution:** Stop the other program or pick a free port from the 5100–5199
  range for your test app. Do **not** change the port range in `compose.yml`
  unless the task explicitly requires it.

---

## Build bricht mit Netzwerkfehler ab / Build Aborts with a Network Error

**DE:**

- **Symptom:** `podman compose build` bricht ab mit einer Meldung über
  fehlgeschlagene Downloads (z. B. von `mcr.microsoft.com`, GitHub oder einem
  Paketregister).
- **Ursache:** Der Container-Build braucht ausgehenden Netzwerkzugriff (Egress)
  auf externe Paketquellen. In manchen Netzen (Schule, Firma) blockiert ein
  Proxy oder eine Firewall diese Verbindungen.
- **Lösung:** Prüfe deine Internetverbindung. Hinter einem Proxy trägst du die
  Proxy-Einstellungen in deiner Umgebung ein und wiederholst den Build. Die
  benötigten Quellen und die Risikoentscheidung stehen in
  `docs/security/network-decision.md`.

**EN:**

- **Symptom:** `podman compose build` aborts with a message about failed
  downloads (e.g. from `mcr.microsoft.com`, GitHub, or a package registry).
- **Cause:** The container build needs outbound network access (egress) to
  external package sources. In some networks (school, company) a proxy or
  firewall blocks these connections.
- **Solution:** Check your internet connection. Behind a proxy, set the proxy
  settings in your environment and retry the build. The required sources and the
  risk decision are in `docs/security/network-decision.md`.

---

## `permission denied` bei Dateien im Mount / `permission denied` for Files in the Mount

**DE:**

- **Symptom:** Im Container erscheint `permission denied`, wenn du in einem
  Ordner wie `/workspace` schreiben willst.
- **Ursache:** Der Benutzer `adedev` im Container hat andere Rechte als dein
  Host-Benutzer, oder du versuchst außerhalb eines freigegebenen Mounts zu
  schreiben.
- **Lösung:** Schreibe nur in die freigegebenen Bereiche (`/workspace`,
  `/python-projects`, `/go-projects`, …). Die vollständige Liste steht in der
  Mount-Matrix im [sandbox-profil.md](sandbox-profil.md), Abschnitt 2. Prüfe
  auf dem Host, dass der Ordner dir gehört und beschreibbar ist.

**EN:**

- **Symptom:** Inside the container you see `permission denied` when you try to
  write in a folder like `/workspace`.
- **Cause:** The user `adedev` in the container has different rights than your
  host user, or you are trying to write outside a released mount.
- **Solution:** Write only into the released areas (`/workspace`,
  `/python-projects`, `/go-projects`, …). The full list is in the mount matrix
  in [sandbox-profil.md](sandbox-profil.md), section 2. On the host, check that
  the folder belongs to you and is writable.

---

## `podman compose` wird nicht erkannt / `podman compose` Is Not Recognized

**DE:**

- **Symptom:** `podman compose ...` meldet einen unbekannten Befehl.
- **Ursache:** Nicht jede Podman-Installation bringt das eingebaute
  `compose`-Unterkommando mit.
- **Lösung:** Nutze `podman-compose` (mit Bindestrich) und denselben Argumenten,
  zum Beispiel `podman-compose up -d`. Für reine Konfigurationsprüfung ist
  `podman-compose config` immer geeignet.

**EN:**

- **Symptom:** `podman compose ...` reports an unknown command.
- **Cause:** Not every Podman installation ships the built-in `compose`
  subcommand.
- **Solution:** Use `podman-compose` (with a hyphen) and the same arguments, for
  example `podman-compose up -d`. For config-only validation, `podman-compose
  config` always works.

---

## Windows/WSL2: Container startet nicht / Windows/WSL2: Container Does Not Start

**DE:**

- **Symptom:** Befehle hängen oder melden, dass keine Verbindung zur
  Podman-Machine besteht.
- **Ursache:** WSL2 oder die Podman-Machine läuft nicht.
- **Lösung:** Öffne Podman Desktop und starte die Podman-Machine dort, oder
  führe `podman machine start` aus. Prüfe mit `podman info`, dass eine
  Verbindung besteht. Nutze PowerShell 7, nicht die alte Windows-PowerShell 5.

**EN:**

- **Symptom:** Commands hang or report that there is no connection to the Podman
  machine.
- **Cause:** WSL2 or the Podman machine is not running.
- **Solution:** Open Podman Desktop and start the Podman machine there, or run
  `podman machine start`. Check with `podman info` that a connection exists. Use
  PowerShell 7, not the old Windows PowerShell 5.

---

## .NET: `bin`/`obj` landen im Projektordner / .NET: `bin`/`obj` End Up in the Project Folder

**DE:**

- **Symptom:** Beim .NET-Bauen erscheinen `bin`- und `obj`-Ordner im gemounteten
  Projektverzeichnis, besonders störend auf einem Windows-Bind-Mount.
- **Ursache:** .NET legt Build-Ausgaben standardmäßig neben den Quellcode.
- **Lösung:** Die Sandbox lenkt Build-Ausgaben in das Volume `dotnet_build`
  (`/dotnet-build`) über die gemountete `ContainerBuild.props`-Datei. Baue aus
  `/rider-projects`, damit diese Konfiguration greift. Committe `bin`- und
  `obj`-Ordner nie ins Repository.

**EN:**

- **Symptom:** When building .NET, `bin` and `obj` folders appear in the mounted
  project directory, especially annoying on a Windows bind mount.
- **Cause:** By default .NET places build output next to the source code.
- **Solution:** The sandbox redirects build output into the `dotnet_build`
  volume (`/dotnet-build`) via the mounted `ContainerBuild.props` file. Build
  from `/rider-projects` so this configuration applies. Never commit `bin` and
  `obj` folders into the repository.

---

## Ein Required-Agent fehlt oder die Anmeldung ist weg / A Required Agent Is Missing or Signed Out

**DE:**

- **Symptom:** `codex`, `claude`, `gemini` oder `copilot` meldet `command not
  found`.
- **Ursache:** Das Image wurde vor der Vier-Agenten-Erweiterung gebaut oder der
  Build ist fehlgeschlagen.
- **Lösung:** Fuehre auf dem Host `podman compose build --pull` und danach
  `bash scripts/smoke-test-toolchains.sh` im Container aus. Alle vier Befehle
  muessen eine Version ausgeben.
- **Symptom:** Nach einem Neustart ist der Agent abgemeldet.
- **Ursache:** Die Umgebung wurde mit `down -v` beendet; dadurch wurden die
  Agenten-Volumes geloescht.
- **Lösung:** Melde dich interaktiv erneut an. Nutze beim normalen Stoppen
  `bash scripts/compose-down-with-audit.sh --podman` ohne `-v`.

**EN:**

- **Symptom:** `codex`, `claude`, `gemini`, or `copilot` reports `command not
  found`.
- **Cause:** The image predates the four-agent extension or its build failed.
- **Solution:** Run `podman compose build --pull` on the host and then
  `bash scripts/smoke-test-toolchains.sh` inside the container. All four
  commands must print a version.
- **Symptom:** An agent is signed out after restart.
- **Cause:** The environment was stopped with `down -v`, which removed the
  agent volumes.
- **Solution:** Sign in interactively again. For normal stops, use
  `bash scripts/compose-down-with-audit.sh --podman` without `-v`.

---

## Nichts hilft — was dann? / Nothing Helps — What Then?

**DE:** Prüfe der Reihe nach: Läuft die Podman-Machine (`podman machine list`)?
Antwortet Podman (`podman info`)? Ist die Konfiguration gültig
(`podman-compose config`)? Notiere die genaue Fehlermeldung und den Befehl, der
sie auslöst. Beschreibe beim Nachfragen dein Betriebssystem und den letzten
Schritt aus [installation.md](installation.md), der noch funktioniert hat.

**EN:** Check in order: is the Podman machine running (`podman machine list`)?
Does Podman respond (`podman info`)? Is the configuration valid (`podman-compose
config`)? Write down the exact error message and the command that triggers it.
When you ask for help, describe your operating system and the last step from
[installation.md](installation.md) that still worked.
