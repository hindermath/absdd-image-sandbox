# Schritt-für-Schritt-Installation / Step-by-Step Installation

**Stand / Date:** 2026-07-10
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

**DE:** Diese Anleitung führt dich vom leeren Rechner bis zum laufenden
Container — ohne Vorkenntnisse. Wähle den Abschnitt für dein Betriebssystem.
Bei Fehlern hilft dir [troubleshooting.md](troubleshooting.md). Was danach
kommt, steht in [erste-schritte.md](erste-schritte.md).

**EN:** This guide takes you from an empty machine to a running container — with
no prior knowledge. Choose the section for your operating system. If something
fails, [troubleshooting.md](troubleshooting.md) helps. What comes next is in
[erste-schritte.md](erste-schritte.md).

---

## Was du am Ende hast / What You Will Have at the End

**DE:** Ein laufender Container namens `ade`, in dem C#, Go, Java, Python, Rust,
Swift und die KI-Werkzeuge bereits installiert sind. Du musst diese Sprachen
**nicht** einzeln auf deinem Rechner einrichten.

**EN:** A running container named `ade` in which C#, Go, Java, Python, Rust,
Swift, and the AI tools are already installed. You do **not** need to set up
these languages one by one on your machine.

---

## Voraussetzungen prüfen / Check Prerequisites

**DE:** Öffne ein Terminal und prüfe, ob `git` und `podman` schon da sind. Die
Befehle geben eine Versionsnummer aus, wenn das Werkzeug installiert ist.

**EN:** Open a terminal and check whether `git` and `podman` are already there.
The commands print a version number if the tool is installed.

```bash
git --version
podman --version
```

**DE:** Erwartete Ausgabe (Beispiel): `git version 2.43.0` und
`podman version 5.x.x`. Erscheint stattdessen `command not found`, ist das
Werkzeug noch nicht installiert — folge unten dem Abschnitt für dein System.

**EN:** Expected output (example): `git version 2.43.0` and
`podman version 5.x.x`. If you see `command not found` instead, the tool is not
installed yet — follow the section for your system below.

---

## macOS

**DE:** Auf macOS installierst du Podman am einfachsten mit Homebrew, dem
verbreiteten Paketmanager für macOS. Falls du Homebrew noch nicht hast,
installiere es zuerst von <https://brew.sh>.

**EN:** On macOS, the easiest way to install Podman is via Homebrew, the common
package manager for macOS. If you do not have Homebrew yet, install it first
from <https://brew.sh>.

```bash
brew install podman podman-compose
```

**DE:** Was passiert hier? Homebrew lädt Podman und `podman-compose` herunter
und installiert beide. Danach richtest du die Podman-Machine ein — die kleine
Linux-VM, die Podman auf dem Mac braucht (siehe
[container-grundlagen.md](container-grundlagen.md)).

**EN:** What happens here? Homebrew downloads Podman and `podman-compose` and
installs both. Then you set up the Podman machine — the small Linux VM that
Podman needs on the Mac (see [container-grundlagen.md](container-grundlagen.md)).

```bash
podman machine init
podman machine start
```

**DE:** `init` erzeugt die Linux-VM einmalig, `start` schaltet sie ein. Prüfe
danach mit `podman info`, dass eine Verbindung besteht. Springe dann zu
[Repository holen und starten](#repository-holen-und-starten--get-and-start-the-repository).

**EN:** `init` creates the Linux VM once, `start` powers it on. Then check with
`podman info` that a connection exists. Then jump to
[Repository holen und starten](#repository-holen-und-starten--get-and-start-the-repository).

---

## Windows (mit WSL2) / Windows (with WSL2)

**DE:** Auf Windows läuft Podman am besten über WSL2 (das Linux-Subsystem für
Windows). Installiere zuerst **Podman Desktop** von
<https://podman-desktop.io>. Podman Desktop richtet WSL2 und die Podman-Machine
über eine grafische Oberfläche ein — folge dem Assistenten und lege eine
Podman-Machine an.

**EN:** On Windows, Podman works best via WSL2 (the Linux subsystem for
Windows). First install **Podman Desktop** from <https://podman-desktop.io>.
Podman Desktop sets up WSL2 and the Podman machine through a graphical
interface — follow the wizard and create a Podman machine.

**DE:** Danach öffnest du **PowerShell 7** und installierst `podman-compose`:

**EN:** Then open **PowerShell 7** and install `podman-compose`:

```powershell
winget install podman-compose
```

**DE:** Prüfe mit `podman info`, dass die Podman-Machine läuft. Erscheint ein
Fehler, starte die Machine in Podman Desktop oder mit `podman machine start`.
Springe dann zu
[Repository holen und starten](#repository-holen-und-starten--get-and-start-the-repository).

**EN:** Check with `podman info` that the Podman machine runs. If an error
appears, start the machine in Podman Desktop or with `podman machine start`.
Then jump to
[Repository holen und starten](#repository-holen-und-starten--get-and-start-the-repository).

---

## Linux / Ubuntu

**DE:** Auf Linux brauchst du **keine** Podman-Machine — Container laufen direkt,
weil dein System bereits Linux ist. Installiere Podman aus den Paketquellen und
`podman-compose` über `pip`:

**EN:** On Linux you need **no** Podman machine — containers run directly
because your system is already Linux. Install Podman from the package sources
and `podman-compose` via `pip`:

```bash
sudo apt update
sudo apt install -y podman
pip install podman-compose
```

**DE:** Prüfe mit `podman info`, dass Podman antwortet. Fahre dann fort mit
[Repository holen und starten](#repository-holen-und-starten--get-and-start-the-repository).

**EN:** Check with `podman info` that Podman responds. Then continue with
[Repository holen und starten](#repository-holen-und-starten--get-and-start-the-repository).

---

## Repository holen und starten / Get and Start the Repository

**DE:** Ab hier sind die Schritte auf allen Systemen gleich. Zuerst holst du
eine eigene Kopie des Repositories und wechselst hinein. Verwende die von deiner
Institution bereitgestellte GitLab-, Codeberg-, Forgejo- oder andere Git-URL.
Nur im direkten GitHub-Profil verwendest du die oeffentliche Referenz.

**EN:** From here the steps are the same on all systems. First you get your own
copy of the repository and change into it. Use the GitLab, Codeberg, Forgejo, or
other Git URL provided by your institution. Only the direct GitHub profile uses
the public reference.

```bash
SANDBOX_REPO_URL="<INSTITUTIONELLE-URL-ODER-HTTPS://GITHUB.COM/HINDERMATH/ABSDD-IMAGE-SANDBOX.GIT>"
git clone "$SANDBOX_REPO_URL"
cd absdd-image-sandbox
```

**DE:** Lege die lokale Secrets-Datei an. Du brauchst noch keinen echten
Schlüssel — die Datei darf leer bleiben, solange du keinen KI-Provider nutzt.

**EN:** Create the local secrets file. You do not need a real key yet — the file
may stay empty as long as you do not use an AI provider.

```bash
cp opencode.env.example opencode.env
```

**DE:** Prüfe zuerst die Konfiguration, **ohne** den Container zu starten. Das
findet Tippfehler früh und startet nichts.

**EN:** First validate the configuration **without** starting the container.
This finds typos early and starts nothing.

```bash
podman-compose config
```

**DE:** Erwartete Ausgabe: die zusammengeführte Compose-Konfiguration als Text,
**ohne** Fehlermeldung. Baue jetzt das Image und starte den Container. Der erste
Build lädt viele Werkzeuge und dauert einige Minuten.

**EN:** Expected output: the merged Compose configuration as text, **without** an
error message. Now build the image and start the container. The first build
downloads many tools and takes several minutes.

```bash
podman compose build --pull
podman compose up -d
```

**DE:** `build --pull` erstellt das Image und lädt das Basis-Image frisch;
`up -d` startet den Container im Hintergrund (`-d` = detached). Öffne dann eine
Shell im Container:

**EN:** `build --pull` creates the image and pulls the base image fresh; `up -d`
starts the container in the background (`-d` = detached). Then open a shell in
the container:

```bash
podman compose exec ade bash
```

**DE:** Wenn alles klappt, ändert sich deine Eingabeaufforderung zu etwas wie
`adedev@...:/rider-projects$`. Du bist jetzt **im** Container.

**EN:** If everything works, your prompt changes to something like
`adedev@...:/rider-projects$`. You are now **inside** the container.

**DE:** Hinweis: Ist `podman compose` auf deinem System nicht verfügbar, nutze
`podman-compose` mit denselben Argumenten.

**EN:** Note: if `podman compose` is not available on your system, use
`podman-compose` with the same arguments.

---

## Nächster Schritt / Next Step

**DE:** Der Container läuft. In [erste-schritte.md](erste-schritte.md) prüfst du
die Werkzeuge, baust dein erstes Mini-Programm und lernst, die Umgebung sauber
und auditkonform zu stoppen.

**EN:** The container is running. In [erste-schritte.md](erste-schritte.md) you
check the tools, build your first mini program, and learn to stop the
environment cleanly and audit-compliant.
