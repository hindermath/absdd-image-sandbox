# Schritt-für-Schritt-Installation / Step-by-Step Installation

**Stand / Date:** 2026-10-25
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

**DE:** Du brauchst ein normales Benutzerkonto, ausreichend freien Speicher
fuer Toolchains, Images und Build-Cache sowie Internet fuer den ersten Build.
Installationen koennen Administratorrechte erfordern; die Arbeit im Container
erfolgt als `adedev`, nicht als Root. Klaere institutionelle Vorgaben zuerst.
Die [Betriebsreferenz](../betrieb/validierung-und-wartung.md) erklaert
Plattformnachweise, gibt aber keine pauschale Speichergarantie. Installiere Git und auf Windows PowerShell 7 aus den
offiziellen oder institutionell freigegebenen Paketquellen, falls sie fehlen.

**EN:** You need a normal user account, enough free space for toolchains,
images and build cache, and internet for the first build. Installation may
require administrator rights; container work uses adedev, not root. Check
institutional rules first. The operations reference explains platform
evidence, not a blanket capacity guarantee. Install Git and, on Windows,
PowerShell 7 from official or institution-approved sources if missing.

| Pfad / Path | Shell und Engine / Shell and engine | Architektur / Architecture |
|---|---|---|
| Apple-Silicon-macOS | Terminal, Bash/zsh, Podman-Machine / terminal, Bash/zsh, Podman machine | `linux/arm64`, ohne Rosetta-Fallback / no Rosetta fallback |
| Windows auf Intel/AMD / Windows on Intel/AMD | PowerShell 7, Windows-Podman-Machine | `linux/amd64` |
| Ubuntu in WSL2 auf Intel/AMD / Ubuntu in WSL2 on Intel/AMD | Bash, eigenes rootless Podman / own rootless Podman | `linux/amd64` |

**DE:** Die letzten beiden sind getrennte Laufzeiten, auch auf demselben
Rechner. Natives Linux bleibt technisch ein eigener Pfad; eine WSL2-Pruefung
beweist keine Abnahme auf nativer Linux-Hardware. Pruefe den
[aktuellen Nachweisstand](../security/toolchain-followups-2026-10-25.md).

**EN:** The last two are separate runtimes, even on one computer. Native
Linux remains a separate path; a WSL2 check does not prove native Linux
hardware acceptance. Check the current evidence state.

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

### Speicher Vorher Pruefen / Check Capacity First

**DE:** Dieser Kapazitaetscheck gilt auch fuer die anderen Plattformen unten.
Auf macOS oder in Ubuntu/WSL2 zeigt `df -h .` den freien Platz des aktuellen
Checkout-Dateisystems. Auf Windows zeigt der folgende PowerShell-Befehl die
Dateisystem-Laufwerke mit genutztem und freiem Speicher. Fuehre nur die zu
deinem Host passende Variante aus; beide Befehle loeschen nichts.

**EN:** This capacity check also applies to the other platforms below.
On macOS or Ubuntu/WSL2, df shows free space on the checkout filesystem.
The PowerShell command lists Windows filesystem drives with used and free
space. Use only the variant for your host; neither command deletes data.

Host, Bash / Host, Bash:

```bash
df -h .
```

Host, PowerShell 7, Alternative / Host, PowerShell 7, alternative:

```powershell
Get-PSDrive -PSProvider FileSystem
```

**DE:** Erwartet wird eine Speicheruebersicht, kein bestandenes Gate. Der
freie Host-Speicher ist nicht identisch mit dem freien Platz in der
Podman-Machine oder ihrer konfigurierten Festplattengroesse. Klaere mit der
Lernbegleitung auch Machine-Speicher, RAM und Platz fuer weitere Build-
Schichten. Bei knappem Platz nicht starten und keinen globalen Prune oder
Reset improvisieren. Ohne gemessene Reserve gibt diese Anleitung keine
garantierte Mindestkapazitaet an.

**EN:** Expect a capacity overview, not a passed gate. Free host space differs
from free space inside the Podman machine and its configured disk size.
Check machine storage, RAM and room for more build layers with your
instructor. If space is low, do not start or improvise a global prune/reset.
Without measured reserve this guide states no guaranteed minimum capacity.

### Podman Einrichten / Set Up Podman

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
podman machine list
```

**DE:** Nur wenn noch keine Machine besteht, einmal `podman machine init`
ausfuehren. Eine vorhandene gestoppte Machine startest du so:

**EN:** Only if no machine exists, run `podman machine init` once. Start an
existing stopped machine as follows:

```bash
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

**DE:** Oeffne danach **PowerShell 7**. Fuer die statische Repo-Pruefung
benoetigst du `podman-compose`, nicht nur einen anderen Compose-Provider.
Installiere Python und `uv` bei Bedarf ueber die freigegebene Paketquelle;
danach:

**EN:** Then open PowerShell 7. Static repository validation needs
podman-compose, not merely another Compose provider. If needed, install
Python and uv through your approved package source; then:

```powershell
uv tool install podman-compose
podman-compose --version
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
`podman-compose` ebenfalls aus den Ubuntu-Paketquellen. Dieser Abschnitt ist
auch fuer Ubuntu unter WSL2 gedacht; dort arbeite als normaler Linux-Benutzer
und lege den Checkout im Linux-Dateisystem unter deinem Home ab, nicht unter
`/mnt/c`. Nutze nicht den Windows-Podman-Client ueber eine Socket-Weiterleitung.

**EN:** On Linux you need **no** Podman machine — containers run directly
because your system is already Linux. Install Podman from the package sources
and podman-compose from Ubuntu packages. This also applies to Ubuntu under
WSL2: use a normal Linux user and a checkout in your Linux home, not /mnt/c.
Do not forward the Windows Podman client's socket for this separate test path.

```bash
sudo apt update
sudo apt install -y git podman podman-compose uidmap slirp4netns
id -u
podman info --format '{{.Host.Security.Rootless}}'
```

**DE:** Prüfe mit `podman info`, dass Podman antwortet. Fahre dann fort mit
[Repository holen und starten](#repository-holen-und-starten--get-and-start-the-repository).

**EN:** Check with `podman info` that Podman responds. Then continue with
[Repository holen und starten](#repository-holen-und-starten--get-and-start-the-repository).

---

## Repository holen und starten / Get and Start the Repository

**DE:** Standard bleibt der persönliche Fork oder eine institutionelle Kopie
mit gemeinsamer Historie. Der später optionale
[Template-Weg](template-profil.md) erzeugt eine unabhängige Sandbox und ist
derzeit noch nicht aktiviert. Auch dort klonst du dein eigenes `origin` und
baust lokal; sein Update-Weg unterscheidet sich aber vom Fork. Keine fremden
Run-States oder Abnahmen als eigene übernehmen. Die folgende Einrichtung
ändert keine GitHub-Einstellung und erstellt kein entferntes Repo automatisch.

**EN:** The default is a personal fork/shared-history institutional copy. The
later optional template route creates an independent sandbox and is not enabled
yet. It still clones personal origin and self-builds, but updates differ.
Never inherit source run/acceptance claims. This guide changes no platform
setting and creates no remote repository automatically.

**DE:** Ab hier ist der Ablauf gleich, die Shell-Syntax jedoch nicht. Waehle
zuerst deinen eigenen Fork oder das institutionell bereitgestellte Repo als
`origin`; die Referenz bleibt `upstream`. Der
[Git-Grundkurs](git-und-hosting.md) erklaert diese Begriffe und das Forken.
Die oeffentliche Referenz-URL ist Herkunft, nicht dein beschreibbarer Ursprung.
Danach holst du
eine eigene Kopie des Repositories und wechselst hinein. Verwende die von deiner
Institution bereitgestellte GitLab-, Codeberg-, Forgejo- oder andere Git-URL.
Im direkten GitHub-Profil klonst du die URL deines persoenlichen Forks.

**EN:** From here the workflow is the same, but shell syntax differs. Choose
your own fork or institutional repository as origin and the reference as
upstream; the Git guide explains these terms and forking. The public reference
URL records provenance, not your writable origin. Then get your own
copy of the repository and change into it. Use the GitLab, Codeberg, Forgejo, or
other Git URL provided by your institution. The direct GitHub profile clones
your personal fork URL, not the public reference as a writable origin.

Host, Bash; URL-Platzhalter vorher ersetzen / Host, Bash; replace URL placeholder first:

```bash
SANDBOX_REPO_URL="<URL-DEINES-FORKS-ODER-INSTITUTIONELLEN-REPOS>"
git clone "$SANDBOX_REPO_URL" absdd-image-sandbox
cd absdd-image-sandbox
```

Host, PowerShell 7, Alternative; URL vorher ersetzen / Alternative; replace URL first:

```powershell
$SandboxRepoUrl = '<URL-DEINES-FORKS-ODER-INSTITUTIONELLEN-REPOS>'
git clone $SandboxRepoUrl absdd-image-sandbox
Set-Location absdd-image-sandbox
```

**DE:** Lege die lokale Secrets-Datei an. Du brauchst noch keinen echten
Schlüssel — die Datei darf leer bleiben, solange du keinen KI-Provider nutzt.

**EN:** Create the local secrets file. You do not need a real key yet — the file
may stay empty as long as you do not use an AI provider.

**DE:** Lege auch `.env` fuer Projekt-Mounts aus `.env.example` an. Vorhandene
Dateien niemals durch Vorlagen ueberschreiben. Trage nur existierende,
bewusst ausgewaehlte Host-Ordner ein; kein komplettes Host-Home mounten.
`.env` wird von Compose gelesen und nicht in das Image eingebaut.

**EN:** Also create .env from .env.example for project mounts. Never overwrite
existing files with templates. Select existing host directories deliberately;
do not mount your entire host home. Compose reads .env; it is not embedded
in the image.

Host, Bash / Host, Bash:

```bash
if [ ! -e .env ]; then cp .env.example .env; fi
if [ ! -e opencode.env ]; then cp opencode.env.example opencode.env; fi
chmod 600 .env opencode.env
```

Host, PowerShell 7, Alternative / Host, PowerShell 7, alternative:

```powershell
if (-not (Test-Path -LiteralPath .env)) { Copy-Item .env.example .env }
if (-not (Test-Path -LiteralPath opencode.env)) { Copy-Item opencode.env.example opencode.env }
```

**DE:** Unter Windows sichere lokale Dateien ueber die Benutzerrechte des
Dateisystems; `chmod` ist dort keine allgemeine ACL-Anweisung. Pruefe
`git status --short`: keine der beiden lokalen Dateien darf zum Commit
vorgemerkt werden.

**EN:** On Windows, protect local files using filesystem user permissions;
chmod is not a general Windows ACL instruction. Check git status: neither
local file may be staged for commit.

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

**DE:** `build --pull` erstellt das Image und prueft das digest-gepinnte Basisimage;
`up -d` startet den Container im Hintergrund (`-d` = detached). Öffne dann eine
Shell im Container:

**EN:** `build --pull` builds the image and checks the digest-pinned base; `up -d`
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
