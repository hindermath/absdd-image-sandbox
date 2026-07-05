# Für Lernende: Einstieg in die Sandbox-Umgebung / For Learners: Getting Started

**Stand / Date:** 2026-07-05
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

---

## Worum geht es hier? / What Is This?

**DE:** Die `absdd-image-sandbox` ist eine **Container-Umgebung** für sichere Softwareentwicklung mit
KI-Agenten. Sie bietet eine abgeschottete Umgebung, in der du Fehler machen kannst, ohne dass etwas außerhalb
des Containers beschädigt wird. Du findest hier alle Werkzeuge (Sprachlaufzeiten, Testtools, KI-Agenten), die
du im Ausbildungsprojekt `Secure CaseTracker` benötigst.

**EN:** The `absdd-image-sandbox` is a **container environment** for secure software development with AI
agents. It provides a walled-off space where you can make mistakes without damaging anything outside the
container. It contains all tools (language runtimes, test tools, AI agents) you need for the `Secure
CaseTracker` training project.

**DE:** Die öffentliche Referenzadresse lautet: `https://github.com/hindermath/absdd-image-sandbox`

**EN:** The public reference address is: `https://github.com/hindermath/absdd-image-sandbox`

---

## Bin ich bereit? / Am I Ready?

**DE:** Die Sandbox wird im Laufe der Ausbildung schrittweise wichtiger. Die Tabelle zeigt, was in welchem
Lehrjahr von dir erwartet wird.

**EN:** The sandbox becomes progressively more important during training. The table shows what is expected in
each training year.

| Lehrjahr / Year | Erwartung / Expectation | Sandbox Pflicht? / Mandatory? |
|---|---|---|
| 1. Lehrjahr / Year 1 | Verstehe, **warum** eine Sandbox existiert und was ihre Grenzen sind. Dokumentiere Mounts, Schreibgrenzen, Netzwerk und Secret-Regeln als Zielbild. | Nein — praktische Nutzung ist `N/A`, begründet. / No — practical use is `N/A`, justified. |
| 2. Lehrjahr / Year 2 | Bereite ein **Betriebskonzept** vor: Konfiguration, Secrets, Schreibgrenzen, Laufzeitannahmen, KI-Agenten-Grenzen. Entscheide dokumentiert `Applicable`/`N/A`/`Open`. | Nein — Konzept vorbereiten, Nutzung darf begründet aufschieben. / No — prepare the concept; use may be deferred with a rationale. |
| 3. Lehrjahr SI / Year 3 SI | Nutze die Sandbox **tatsächlich** für KI-gestützte Schreibarbeit und riskante Experimente. Betriebsnachweise liefern. | Ja (SI-Track und DV-Track). / Yes (SI track and DV track). |
| 3. Lehrjahr DV / Year 3 DV | Nutze die Sandbox als Referenzprofil; dokumentiere Netzwerkzugriffe, Mounts und Abweichungen nachvollziehbar. | Ja (SI-Track und DV-Track). / Yes (SI track and DV track). |
| 3. Lehrjahr AE/DPA / Year 3 AE/DPA | Sandbox ist relevant, aber weniger zentral als für SI/DV. | Teils — je nach Aufgabe. / Partial — depends on the task. |

**DE:** **Lesen und Review darf immer außerhalb der Sandbox stattfinden** — auch in JetBrains-IDEs, VS Code
oder Visual Studio. Die Sandbox ist für KI-gestützte Schreibarbeit, riskante Experimente und reproduzierbare
Toolchain-Prüfungen gedacht.

**EN:** **Reading and review may always happen outside the sandbox** — also in JetBrains IDEs, VS Code, or
Visual Studio. The sandbox is intended for AI-assisted write work, risky experiments, and reproducible
toolchain checks.

---

## Schnellstart (5 Schritte) / Quick Start (5 Steps)

**DE:** Wenn du die Sandbox zum ersten Mal startest:

**EN:** When you start the sandbox for the first time:

### Schritt 1 / Step 1: Voraussetzungen prüfen / Check Prerequisites

**DE:** Du brauchst: `git`, `podman` (oder Docker als Alternative) und `podman-compose`.

**EN:** You need: `git`, `podman` (or Docker as an alternative), and `podman-compose`.

```bash
git --version
podman --version
podman-compose --version
```

**DE:** Auf macOS: `brew install podman podman-compose`
Auf Ubuntu: `apt install podman` + `pip install podman-compose`
Auf Windows: Podman Desktop installieren, dann `winget install podman-compose`

**EN:** On macOS: `brew install podman podman-compose`
On Ubuntu: `apt install podman` + `pip install podman-compose`
On Windows: Install Podman Desktop, then `winget install podman-compose`

### Schritt 2 / Step 2: Repository klonen / Clone the Repository

```bash
git clone https://github.com/hindermath/absdd-image-sandbox.git
cd absdd-image-sandbox
```

### Schritt 3 / Step 3: Konfiguration vorbereiten / Prepare Configuration

**DE:** Erstelle die lokale Secrets-Datei. Du brauchst erst keinen echten API-Schlüssel — die Datei darf
leer bleiben, wenn du keinen KI-Provider-Schlüssel verwendest.

**EN:** Create the local secrets file. You do not need a real API key yet — the file may stay empty if you
are not using a provider key.

```bash
cp opencode.env.example opencode.env
# Keine Schluessel einzutragen, bis du sie benoenigst.
# No keys to enter until you need them.
```

### Schritt 4 / Step 4: Podman starten / Start Podman

**DE:** Auf macOS und Windows braucht Podman eine Maschine:

**EN:** On macOS and Windows, Podman needs a machine:

```bash
# macOS / Windows
podman machine init
podman machine start
```

**DE:** Auf Linux oder WSL2: `podman info` zum Prüfen reicht.

**EN:** On Linux or WSL2: `podman info` to check is enough.

### Schritt 5 / Step 5: Container bauen und starten / Build and Start the Container

```bash
# Konfiguration pruefen (ohne Start) / Validate config (without starting)
podman-compose config

# Image bauen und Container starten / Build image and start container
podman compose build --pull
podman compose up -d

# Shell im Container oeffnen / Open a shell in the container
podman compose exec ade bash
```

**DE:** Wenn der Container läuft, siehst du die Eingabeaufforderung `adedev@...`. Jetzt kannst du die
installierten Werkzeuge prüfen:

**EN:** When the container runs you see the prompt `adedev@...`. Now you can check the installed tools:

```bash
dotnet --version
go version
java --version
python --version
rustc --version
swift --version
specify version
```

---

## Was finde ich wo? / Where Do I Find What?

| Dokument / Document | Inhalt / Content |
|---|---|
| [sandbox-profil.md](sandbox-profil.md) | Vollständiges Sandbox-Profil: Mounts, Schreibgrenzen, Netzwerk, MSL-Matrix, KI-Agenten |
| [GLOSSAR.md](GLOSSAR.md) | Erklärungen für Abkürzungen wie MSL, SBOM, CL_12, P0 |
| [sandbox-readiness-template.md](sandbox-readiness-template.md) | Ausfüllbare Vorlage für die Jahr-2-Sandbox-Entscheidung |
| [betriebsnachweise-template.md](betriebsnachweise-template.md) | Vorlage für Betriebsnachweise (Jahr 3, SI- und DV-Track) |
| [../README.md](../README.md) | Ausführliche Anleitung für Entwickler und Administratoren |
| [../docs/secure-development/](../secure-development/) | Richtlinie, 12 Checklisten und Leitlinien für sichere Entwicklung |

---

## Verbindung zur Lernreihe / Connection to the Learning Series

**DE:** Die `absdd-image-sandbox` ist das öffentliche Referenz-Repository für die Lernreihe
`Secure CaseTracker`. Die passenden Erklärungen (Lernbegleiter) findest du im Repository `home-baseline-tmp`
deiner Ausbildungsstelle:

**EN:** The `absdd-image-sandbox` is the public reference repository for the `Secure CaseTracker` learning
series. The matching study companions are in the `home-baseline-tmp` repository of your training site:

| Lehrjahr / Year | Lernbegleiter-Datei / Study Companion File |
|---|---|
| 1. Lehrjahr / Year 1 | `docs/learning-units/lernbegleiter/Secure-CaseTracker_09_Sandbox-und-Agentische-Entwicklung.Lernbegleiter.md` |
| 2. Lehrjahr / Year 2 | `docs/learning-units/lernbegleiter/Secure-CaseTracker-v2_09_Sandbox-und-Betriebsnachweise.Lernbegleiter.md` |
| 3. Lehrjahr SI / Year 3 SI | `docs/learning-units/lernbegleiter/Secure-CaseTracker-Operations-Track_02_Sandbox-und-Laufzeitprofil.Lernbegleiter.md` |
| 3. Lehrjahr DV / Year 3 DV | `docs/learning-units/lernbegleiter/Secure-CaseTracker-Digital-Networking-Track_09_Sandbox-Integration-und-Betriebsnachweise.Lernbegleiter.md` |

---

## Häufige Fragen / Frequently Asked Questions

**DE:** **Ich starte im 1. Lehrjahr — muss ich die Sandbox wirklich nutzen?**
Nein. Im 1. Lehrjahr geht es darum zu verstehen, warum eine Sandbox existiert. Praktische Nutzung ist noch
`N/A` (nicht anwendbar), aber du solltest das begründen. Der Lernbegleiter erklärt genau, was du
dokumentieren sollst.

**EN:** **I am in year 1 — do I really have to use the sandbox?**
No. In year 1 the goal is to understand why a sandbox exists. Practical use is still `N/A` (not applicable),
but you should justify that. The study companion explains exactly what to document.

---

**DE:** **Darf ich die IDE außerhalb der Sandbox nutzen?**
Ja. Lesen, Review, Navigation und Debugging mit JetBrains, VS Code oder Visual Studio dürfen immer außerhalb
stattfinden. Die Sandbox ist für KI-gestützte Schreibarbeit und riskante Experimente.

**EN:** **May I use the IDE outside the sandbox?**
Yes. Reading, review, navigation, and debugging with JetBrains, VS Code, or Visual Studio may always happen
outside. The sandbox is for AI-assisted write work and risky experiments.

---

**DE:** **Was bedeutet `N/A`, `Open` und `Applicable`?**
Schau ins [GLOSSAR.md](GLOSSAR.md). Kurz: `Applicable` = gilt, wird umgesetzt; `N/A` = gilt nicht, mit
Begründung; `Open` = noch offen, Folgeaufgabe geplant.

**EN:** **What do `N/A`, `Open`, and `Applicable` mean?**
See [GLOSSAR.md](GLOSSAR.md). Briefly: `Applicable` = applies, is being implemented; `N/A` = does not apply,
with rationale; `Open` = still open, follow-up planned.

---

**DE:** **Wo soll ich Secrets eintragen?**
Niemals im Repository oder in Prompts. Nutze `opencode.env` für lokale Provider-Schlüssel. Die Datei ist
bereits in `.gitignore` eingetragen und wird nicht in das Repository hochgeladen.

**EN:** **Where do I enter secrets?**
Never in the repository or in prompts. Use `opencode.env` for local provider keys. The file is already in
`.gitignore` and will not be uploaded to the repository.

---

## Nächste Schritte / Next Steps

**DE:** Lies das [sandbox-profil.md](sandbox-profil.md), um die Grenzen dieser Umgebung zu verstehen. Dann
arbeite den Lernbegleiter für dein Lehrjahr durch und bearbeite das zugehörige Lastenheft.

**EN:** Read [sandbox-profil.md](sandbox-profil.md) to understand the boundaries of this environment. Then
work through the study companion for your training year and complete the related intake document.
