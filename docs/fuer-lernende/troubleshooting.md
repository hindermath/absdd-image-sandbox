# Fehlerbehebung / Troubleshooting

**DE:** Fuer grundlegende Fragen lies zuerst die [FAQ](faq.md). Versions-
und imagegebundene Warnungen stehen in den
[Nachpruefungen](../security/toolchain-followups-2026-10-25.md).
Ein Socketfehler ist kein Grund fuer Storage-Reset oder Volume-Loeschung.

**EN:** For basic questions, start with the FAQ. Version- and image-bound
warnings are recorded in the follow-ups. A socket error does not justify
storage reset or volume deletion.

**Stand / Date:** 2026-10-27 (Dokumentationspflege / documentation update)
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
- **Lösung:** Prüfe auf dem Host (Bash oder PowerShell 7) mit
  `podman machine list`, ob deine eingerichtete Machine existiert und läuft.
  Erwartet wird eine Liste mit Zustand; der Befehl ändert keine Daten.
  `already exists` bedeutet nicht, dass sie beschädigt ist. Starte nur die
  vorhandene, gestoppte Machine mit `podman machine start`; dadurch wird keine
  neue angelegt. Bei mehreren Machines kläre zuerst die richtige mit der
  Lernbegleitung. Misslingt der Start, halte an und notiere Fehlermeldung,
  Zeitpunkt und Betriebssystem ohne private Pfade oder Zugangsdaten.
  Entferne weder Machine noch Volumes und führe keinen Reset aus.

**EN:**

- **Symptom:** An error like `Error: machine ... already exists` or the machine
  does not start.
- **Cause:** On macOS and Windows Podman needs a Linux VM (Podman machine). It
  is missing, damaged, or already running.
- **Solution:** On the host (Bash or PowerShell 7), use `podman machine list`
  to inspect the configured machine. Expect a state list without data changes.
  Already exists does not mean damaged. Start only an existing stopped machine
  with `podman machine start`; this creates no new machine. If several exist,
  ask your instructor which to use. If startup fails, stop and record the
  error, time and operating system without private paths or credentials.
  Do not remove machines or volumes or reset storage.

**DE:** Die Lernbegleitung diagnostiziert eine mögliche Beschädigung und prüft
vor einer gesondert genehmigten destruktiven Wiederherstellung betroffene
Projekte, Volumes, Datensicherung und Wiederherstellbarkeit. Eine Diagnose
beweist noch keinen Datenverlust oder Datenerhalt. Ubuntu/WSL2 mit eigenem
rootless Podman verwendet den Linux-Pfad ohne zusätzliche Podman-Machine;
Windows-Host und Ubuntu/WSL2 nicht als denselben Ausführungsweg behandeln.

**EN:** Your instructor diagnoses possible damage and checks affected
projects, volumes, backups and recoverability before separately authorized
destructive recovery. Diagnosis alone proves neither loss nor preservation.
Ubuntu/WSL2 with its own rootless Podman uses the Linux path without an extra
Podman machine; keep the Windows-host and Ubuntu/WSL2 execution paths distinct.

---

## Port 5100–5199 ist belegt / Port 5100–5199 Is in Use

**DE:**

- **Symptom:** Beim Start erscheint `address already in use` oder `bind:
  address already in use` für einen Port zwischen 5100 und 5199.
- **Ursache:** Ein anderes Programm belegt bereits den Port. Der Container
  veröffentlicht `127.0.0.1:5100-5199` für Web-App-Tests.
- **Lösung:** Beim Containerstart wird die gesamte Spanne gebunden. Ein anderer
  Port deiner Test-App löst diesen Compose-Konflikt daher nicht. Lass den
  belegenden Prozess mit der Lernbegleitung identifizieren. Beende nur ein
  eigenes Programm, dessen Beenden du bewusst verantworten kannst. Bei einem
  fremden oder benötigten Dienst nicht eingreifen: eine gesondert geprüfte
  lokale Portkonfiguration mit der Lernbegleitung klären, Loopback-Bindung
  erhalten. Die gemeinsame `compose.yml` nicht ungefragt ändern.
  Nur bei einem App-internen Konflikt im bereits laufenden Container kann ein
  anderer freier App-Port innerhalb 5100–5199 helfen.

**EN:**

- **Symptom:** On start you see `address already in use` or `bind: address
  already in use` for a port between 5100 and 5199.
- **Cause:** Another program already uses the port. The container publishes
  `127.0.0.1:5100-5199` for web app tests.
- **Solution:** Container startup binds the entire range; choosing another
  app port cannot fix this Compose conflict. Ask your instructor to identify
  the occupying process. Stop only your own program whose shutdown you can
  knowingly authorize. Do not interfere with another person's or a needed
  service; arrange separately reviewed local port configuration, preserving
  loopback binding. Do not change shared compose.yml without authority.
  Only an app-internal conflict in an already running container may be solved
  by another free app port within 5100–5199.

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
- **Ursache:** Der gewählte Ausführungsweg ist nicht verfügbar oder wurde
  verwechselt. Bestimme zuerst: Windows-Host oder Ubuntu in WSL2?
- **Lösung Windows-Host:** PowerShell 7, nicht Windows PowerShell 5. Prüfe
  die vorhandene Machine in Podman Desktop oder mit `podman machine list`;
  starte nur die richtige vorhandene, gestoppte Machine. `podman info` muss
  danach antworten. Bei Fehler nicht neu initialisieren, sondern Hilfe holen.
- **Lösung Ubuntu/WSL2:** Im Ubuntu-Terminal mit Bash bleiben und dort
  `id -u` sowie `podman info` prüfen. Erwartet: UID ungleich `0` und eigener
  rootless Podman. Keine zusätzliche Machine anlegen und nicht zum
  Windows-Endpunkt wechseln. Bei fehlendem Podman, falscher Identität oder
  unklarem Kontext mit der Lernbegleitung den
  [Ubuntu/WSL2-Installationspfad](installation.md) prüfen.

**EN:**

- **Symptom:** Commands hang or report that there is no connection to the Podman
  machine.
- **Cause:** The selected execution path is unavailable or mixed up. First
  identify whether you are on the Windows host or inside Ubuntu/WSL2.
- **Windows host:** Use PowerShell 7, not Windows PowerShell 5. Inspect existing
  machines in Podman Desktop or with podman machine list; start only the correct
  existing stopped machine. Expect podman info to respond. On failure, ask for
  help rather than initialize again.
- **Ubuntu/WSL2:** Stay in Ubuntu Bash and inspect id -u and podman info there.
  Expect a nonzero UID and your own rootless Podman. Do not create another
  machine or switch to the Windows endpoint. For missing Podman, wrong identity
  or unclear context, check the Ubuntu/WSL2 installation path with your instructor.

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

- **Symptom:** `codex`, `claude`, `agy` oder `copilot` meldet `command not
  found`.
- **Ursache:** Das Image wurde vor der Vier-Agenten-Erweiterung gebaut oder der
  Build ist fehlgeschlagen.
- **Lösung:** Ein Neubau allein ersetzt keinen laufenden Container. Nutze mit
  der Lernbegleitung den [kontrollierten Austausch aus der FAQ](faq.md):
  Projektdateien im Mount speichern, Audit-Stopp erfolgreich abschließen,
  Volumes erhalten, neues Image bauen und daraus den Container kontrolliert
  neu erstellen. Bei Auditfehler abbrechen, kein direktes `down` als Ersatz.
  Erst danach im tatsächlich neuen Container die Werkzeug-Smokes nach
  [Betriebsanleitung](../betrieb/validierung-und-wartung.md) ausführen und
  verwendete Image-ID prüfen. Das ist betreute Wartung, kein normaler Lernschritt.
- **Symptom:** Nach einem Neustart ist der Agent abgemeldet.
- **Ursache:** Die Umgebung wurde mit `down -v` beendet; dadurch wurden die
  Agenten-Volumes geloescht.
- **Lösung:** Melde dich interaktiv erneut an. Nutze beim normalen Stoppen
  `bash scripts/compose-down-with-audit.sh --podman` ohne `-v`.

**EN:**

- **Symptom:** `codex`, `claude`, `agy`, or `copilot` reports `command not
  found`.
- **Cause:** The image predates the four-agent extension or its build failed.
- **Solution:** Building alone does not replace a running container. With
  your instructor, follow controlled replacement in the FAQ: save project files
  in their mount, complete audit shutdown, retain volumes, build and recreate
  from the new image. Stop on audit failure, with no direct down substitute.
  Only then run the operations guide's tool smokes in the actual new container
  and check its image ID. This is supervised maintenance, not an ordinary
  learning step.
- **Symptom:** An agent is signed out after restart.
- **Cause:** The environment was stopped with `down -v`, which removed the
  agent volumes.
- **Solution:** Sign in interactively again. For normal stops, use
  `bash scripts/compose-down-with-audit.sh --podman` without `-v`.

---

## Nichts hilft — was dann? / Nothing Helps — What Then?

### Audit-Stopp bricht ab / Audit Shutdown Fails

**DE:** Betrifft den Audit-Wrapper auf dem Host im Sandbox-Checkout (Bash
oder PowerShell 7), nicht eine Shell im Container. Voraussetzung: du wolltest
mit dem dokumentierten Wrapper stoppen. Erwartung: erfolgreicher Export von
Metadaten vor `down`, ohne Löschen der Volumes. Metadaten beschreiben einen
Vorgang, nicht dessen Prompt- oder Antwortinhalt.
Bei Exportfehler stoppt der Wrapper vor `down`: kein direktes `compose down`
als Ersatz und keine Löschoption ergänzen. Speichere offene Projektdateien
im vorgesehenen Mount und gib der Lernbegleitung Phase, Exitcode, Zeitpunkt
und geschwärzte Fehlermeldung. Nicht alle Stoppfehler sind Exportfehler;
den Containerstatus daher nicht aus einer Fehlermeldung erraten.

**EN:** This concerns the audit wrapper on the host in the sandbox checkout
(Bash or PowerShell 7), not a container shell. Prerequisite: you tried the
documented stop wrapper. Expect successful metadata export before down,
without deleting volumes. Metadata describes an event, not prompt/response
content. Export failure stops before down: never substitute direct compose
down or add deletion flags. Save open project files in their mount and give
your instructor the phase, exit code, time and redacted error. Not every stop
failure is an export failure; do not infer container status from the error alone.

**DE:** Feature 004 plant zusätzliche Prüfungen für fehlende/leere Exporte,
Retention (Aufbewahrung alter Audit-Metadaten) und Sperren gegen gleichzeitige
Stopps. Das ist noch keine Aussage über installierte Funktionen. Meldet ein
späterer Wrapper eine belegte oder verwaiste Sperre: keinen zweiten Stopp
erzwingen und keine Sperrdatei selbst löschen. Die Lernbegleitung muss zuerst
den vorherigen Lauf und den richtigen Audit-Pfad prüfen. Erst nach geklärter
Ursache erneut den normalen Wrapper verwenden; er muss frisch exportieren.
Bei fehlgeschlagener Retention können alte Metadaten bereits teilweise
entfernt sein. Keine Wiederherstellung oder unveränderte Daten behaupten;
Restdaten und Volumes erhalten, tatsächlichen Umfang prüfen lassen.
Agenten-Datenbanken, Prompts, Antworten und Zugangsdaten nicht zur Diagnose
exportieren. Wenn sichere Wiederaufnahme unklar bleibt, eskalieren statt
Schutzmaßnahmen abzuschalten.

**EN:** Feature 004 plans added checks for absent/empty exports, retention
(keeping old audit metadata for a defined period) and locks preventing
concurrent stops. This does not claim those features are installed. If a
future wrapper reports an occupied or stale lock, do not force another stop
or delete the lock yourself. Your instructor must first check the previous
run and correct audit path. Once the cause is resolved, retry the ordinary
wrapper, which must export afresh. Failed retention may already have removed
some expired metadata. Do not promise restoration or unchanged data; preserve
the remainder and volumes and have the actual scope checked. Never export
agent databases, prompts, responses or credentials for diagnosis. Escalate
unclear recovery instead of disabling safeguards.

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

**DE:** Maintainer finden die vollständige Prüf-, Audit-, SBOM- und
Plattformmatrix unter
[Validierung und Wartung](../betrieb/validierung-und-wartung.md).

**EN:** Maintainers can find the complete validation, audit, SBOM, and
platform matrix in
[Validation and maintenance](../betrieb/validierung-und-wartung.md).

## Ein Validator meldet `Blocked` / A Validator Reports `Blocked`

**DE:** `Blocked` ist nicht automatisch ein Defekt an deinem Rechner. Der
aktuelle Feature-Stand bleibt absichtlich blockiert, solange der getrennte
Windows-Host- und Ubuntu/WSL2-Nachweis, die VS-Code-Attaches, der moderierte
Lernendentest oder gepruefte Dispositionen fuer offene Critical-/High-Matches
fehlen. Beide Plattformpfade duerfen dieselbe Windows-Hardware nutzen, brauchen
aber eigene Podman-Laufzeiten und Evidenz. Verwende macOS, die
Windows-Podman-Machine oder einen beliebigen Linux-Container niemals als
Ersatzbeleg fuer den jeweils anderen Ausfuehrungspfad.

**EN:** Blocked does not automatically mean your computer is broken. The
current feature remains intentionally blocked while separate Windows-host and
Ubuntu/WSL2 evidence, VS Code attachments, the moderated learner test, or
reviewed dispositions for open Critical/High matches are missing. Both paths
may share Windows hardware but require their own Podman runtimes and evidence.
Never substitute macOS, the Windows Podman machine, or an arbitrary Linux
container for the other execution path.

**DE:** Notiere nur Befehl, Exitcode, Plattform und Zeitpunkt. Kopiere keine
Secrets, Tokens, Prompttexte oder unverdeckte Scanner-Treffer in ein Ticket.
Ein moeglicher echter Secret-Fund wird sofort an den Repository-Maintainer und
Security Review uebergeben, ohne den Trefferinhalt zu protokollieren.

**EN:** Record only the command, exit code, platform, and time. Do not copy
secrets, tokens, prompt text, or unredacted scanner matches into an issue. A
possible real secret finding is handed to the repository maintainer and
Security Review immediately without logging its contents.
