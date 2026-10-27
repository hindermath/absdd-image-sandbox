# Taeglicher Arbeitsablauf / Daily Workflow

[Einstieg / Start](README.md)

## Der kurze Normalablauf / The Short Ordinary Workflow

**DE:** Öffnen → eine Aufgabe wählen → im Projekt-Mount speichern → sicher
stoppen → wieder öffnen und Datei wiederfinden. Die folgenden Abschnitte
erklären diese Schritte. Nach abgeschlossener Einrichtung brauchst du dafür
keine Admin-Rechte oder Agentenanmeldung und musst keine vollständige
Governance-Abnahme selbst durchführen. Die Lernbegleitung verantwortet die eingerichtete,
für deinen Lernzweck geprüfte Umgebung; das ersetzt keine Freigabe.
Der Standard bleibt beschreibbar, jedoch nur innerhalb deiner Rechte und
Agentenregeln. Ein zusätzlich eingeschränktes Read-only-Profil ist optional,
kein stiller Standard und kein Grund, Schutzmaßnahmen abzuschalten.

**EN:** Open → choose one task → save in its project mount → stop safely →
reopen and find your file. The following sections explain these steps. After
setup, this needs no admin rights, agent sign-in or full governance acceptance
performed by you. Your instructor owns the configured environment checked
for your learning purpose; this does not replace approval. The default is
writable within your permissions and agent rules. An additional read-only
profile is optional, not a silent default or reason to disable safeguards.

## Ziel Und Voraussetzungen / Goal and Prerequisites

**DE:** Du kannst eine eingerichtete Sandbox wieder benutzen, Ergebnisse
erhalten und ohne Datenverlust stoppen. Voraussetzung: [Installation](installation.md)
abgeschlossen, eigenes Repository vorhanden und gewuenschte Mounts lokal
festgelegt. Mounts verbinden Ordner des Hosts mit dem Container. Aenderungen
darin aendern auch die Host-Dateien. Eine Sandbox ist keine Datensicherung.

**EN:** Reuse an installed sandbox, preserve results and stop without losing
data. Prerequisites: completed installation, your own repository and locally
chosen mounts. Mounts connect host folders to the container. Changes there
also change host files. A sandbox is not a backup.

## Vor Dem Start: Host / Before Starting: Host

**DE:** Oeffne dein Terminal im Sandbox-Checkout. Auf Windows verwende
PowerShell 7; unter Ubuntu/WSL2 bleibe fuer diesen Lauf in Bash. Pruefe die
Machine auf macOS und im Windows-Hostpfad mit `podman machine list` und starte
nur eine vorhandene, gestoppte Machine. Ubuntu/WSL2 mit eigenem rootless
Podman braucht keine zusaetzliche Podman-Machine.

**EN:** Open your terminal in the sandbox checkout. Use PowerShell 7 on the
Windows host; stay in Bash for an Ubuntu/WSL2 run. On macOS and the Windows
host, inspect machines with `podman machine list` and start an existing stopped
machine only. Ubuntu/WSL2 with its own rootless Podman needs no extra machine.

Host, Bash oder PowerShell / Host, Bash or PowerShell:

```bash
git status --short --branch
podman info
podman-compose config
podman compose up -d --no-build --no-recreate --pull never ade
podman compose ps
```

**DE:** Erwartung: Podman antwortet, die Konfiguration ist gueltig und `ade`
laeuft. Der Befehl baut und laedt kein Image und ersetzt keinen vorhandenen
Container. Nach dem Audit-Stopp mit `down` erstellt er einen neuen Container
aus dem vorhandenen lokalen Image und verbindet die erhaltenen Volumes.
Fehlt das lokale Image, bricht er ab: nicht die Schutzoptionen entfernen,
sondern die Lernbegleitung fragen. Pruefe vor einem Wiederanlauf, ob Git-Stand,
lokale Compose-Werte und das verwendete Image noch dem zuletzt geprueften
Stand entsprechen. Bei Drift stoppe und klaere die kontrollierte Neuerstellung
aus der FAQ; nicht unbemerkt neue Werkzeuge oder Mounts uebernehmen.
`podman-compose` ist der
Lifecycle-Ersatz, wenn `podman compose` lokal nicht bereitsteht.

**EN:** Expect Podman to respond, valid configuration and a running `ade`.
This command neither builds nor pulls images and never replaces an existing
container. After audit shutdown with down, it creates a new container from
the existing local image and reconnects retained volumes. If the image is
missing, it fails: keep the safeguards and ask your instructor. Before
restarting, check that Git state, local Compose values and selected image
still match the last reviewed state. Stop on drift and use controlled
recreation from the FAQ rather than silently applying new tools or mounts.
Use `podman-compose` for lifecycle operations if
`podman compose` is unavailable locally.

## Arbeiten: Container / Working: Container

Host / Host:

```bash
podman compose exec ade bash
```

Container, Bash / Container, Bash:

```bash
id
pwd
```

**DE:** Erwartung: Benutzer `adedev`, UID ungleich `0`. Waehle danach den
[Projektpfad deiner Toolchain](toolchains/README.md). Lies Projekt-README und
Agent-Regeln vor Aenderungen. Pruefe dort `git status`, bearbeite eine kleine
Aufgabe und fuehre die dokumentierten Projekttests aus. Ein Terminal-Prompt
allein beweist den Ausfuehrungsort nicht.

**EN:** Expect user `adedev` and a nonzero UID. Select your toolchain's project
path. Read the project README and agent rules before changes. Check Git
status there, work on one small task and run documented project tests. A
terminal prompt alone does not prove where a command runs.

## Ergebnisse Und Stoppen / Results and Shutdown

**DE:** Speichere dauerhafte Ergebnisse im vorgesehenen Projekt-Mount. Pruefe
auch neue Dateien: `git diff` allein zeigt keine ungetrackten Inhalte.
Commit und Push bleiben getrennte, bewusste Entscheidungen nach Review.

**EN:** Save lasting results in the designated project mount. Inspect new
files too: `git diff` alone does not show untracked content. Commit and push
remain separate, deliberate decisions after review.

Container, Bash / Container, Bash:

```bash
git status --short
git diff
exit
```

Host, Bash / Host, Bash:

```bash
bash scripts/compose-down-with-audit.sh --podman
```

Host, PowerShell 7, Alternative / Host, PowerShell 7, alternative:

```powershell
.\scripts\compose-down-with-audit.ps1 -Engine podman
```

**DE:** Ohne Volume-Option bleiben Agentenzustaende erhalten. Fuege im
Alltagsbetrieb weder `-v` noch `-Volumes` hinzu: Diese Optionen loeschen
persistente Volumes und Anmeldedaten. Ein fehlgeschlagener Audit-Export ist
ein Fehler, keine Erlaubnis zum Loeschen. Details und Grenzen von OpenCode 2
stehen in der [technischen Nachpruefung](../security/toolchain-followups-2026-10-25.md).

**EN:** Without a volume option, agent state remains. Never add `-v` or
`-Volumes` for routine shutdown: they delete persistent volumes and sign-in
state. Failed audit export is an error, not permission to delete. See the
technical follow-up for OpenCode 2 limitations.

**DE:** Fehler? Lies die [FAQ](faq.md), danach die
[Fehlerbehebung](troubleshooting.md). Keine globalen Prune- oder Reset-Befehle
als Reparaturversuch verwenden.

**EN:** Problems? Read the FAQ, then troubleshooting. Do not try global prune
or reset commands as a repair.

## Wieder öffnen / Reopen

**DE:** Notiere vor dem Stoppen deinen Projektpfad und den Namen deiner
gespeicherten Datei. Wiederhole später „Vor dem Start“ und „Arbeiten“ oben
auf dem Host und wechsle im Container in genau diesen Projekt-Mount.
Öffne deine Datei im Editor und vergleiche den gespeicherten Inhalt.
Erwartung: dieselbe Arbeit ist vorhanden; keine neue Datei als Ersatz anlegen.
Fehlt sie, prüfe mit der Lernbegleitung zuerst Projektpfad und Mount-Zuordnung.
Keine Volumes neu anlegen, löschen oder einen Reset versuchen. Daten nur in
der Container-Schreibschicht überstehen eine Container-Neuerstellung nicht
zuverlässig; Projekt-Mounts und regelmäßige Datensicherung sind deshalb wichtig.
Bei Sicherheitsabbrüchen nutze die [Audit-Fehlerhilfe](troubleshooting.md).

**EN:** Before shutdown, note your project path and saved filename. Later,
repeat Before Starting and Working above on the host and return to that exact
project mount inside the container. Open your file in the editor and compare
its saved content. Expect the same work, not a new replacement file. If it is
missing, ask your instructor to check the path and mount mapping first. Do not
create/delete volumes or try a reset. Files only in the container writable
layer do not reliably survive recreation; use project mounts and regular
backups. Use audit troubleshooting for security failures.
