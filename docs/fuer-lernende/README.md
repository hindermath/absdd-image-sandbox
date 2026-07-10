# Für Lernende: Einstieg in die Sandbox-Umgebung / For Learners: Getting Started

**Stand / Date:** 2026-07-10
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

---

## Worum geht es hier? / What Is This?

**DE:** Die `absdd-image-sandbox` ist eine **Container-Umgebung** für sichere Softwareentwicklung mit
KI-Agenten. Sie bietet eine abgeschottete Umgebung, in der du Fehler machen kannst, ohne dass etwas außerhalb
des Containers beschädigt wird. Du findest hier alle Werkzeuge (Sprachlaufzeiten, Testtools, KI-Agenten), die
du im Ausbildungsprojekt `Secure CaseTracker` benötigst.

**EN:** The `absdd-image-sandbox` is a **container environment** for secure software development with AI
agents. It provides a walled-off space where you can make mistakes without damaging anything outside the
container. It contains all tools (language runtimes, test tools, AI agents) you need for the three Secure
Trader training projects: CaseTracker, OrderDesk, and ServiceHarvester.

**DE:** Die öffentliche Referenzadresse lautet: `https://github.com/hindermath/absdd-image-sandbox`

**EN:** The public reference address is: `https://github.com/hindermath/absdd-image-sandbox`

---

## Neu hier? Ohne Vorkenntnisse? / New Here? No Prior Knowledge?

**DE:** Wenn du noch **nie mit Containern gearbeitet** hast, folge dieser
Reihenfolge. Jedes Dokument baut auf dem vorherigen auf und setzt kein Vorwissen
voraus.

**EN:** If you have **never worked with containers**, follow this order. Each
document builds on the previous one and assumes no prior knowledge.

**DE:** Beginne mit der zentralen, betriebssystemuebergreifenden Anleitung
[START-HERE-FUER-LERNENDE.md](https://github.com/hindermath/home-baseline/blob/main/docs/learning-units/START-HERE-FUER-LERNENDE.md).
Sie fuehrt vom persoenlichen `home-baseline`-Fork bis zum ersten kontrollierten
Agentenlauf. Dieses Verzeichnis vertieft danach die Sandbox-Schritte.

**EN:** Start with the canonical cross-platform
[learner start guide](https://github.com/hindermath/home-baseline/blob/main/docs/learning-units/START-HERE-FUER-LERNENDE.md).
It leads from the personal `home-baseline` fork to the first controlled agent
run. This directory then explains the sandbox in more detail.

| Schritt / Step | Dokument / Document | Inhalt / Content |
|---|---|---|
| 1 | [container-grundlagen.md](container-grundlagen.md) | Was ist ein Container, Image, Volume, Mount? / What is a container, image, volume, mount? |
| 2 | [warum-sandbox.md](warum-sandbox.md) | Warum eine Sandbox? Gate, Schutzziele, ISO 27001. / Why a sandbox? Gate, protection goals, ISO 27001. |
| 3 | [installation.md](installation.md) | Podman installieren je Betriebssystem. / Install Podman per operating system. |
| 4 | [erste-schritte.md](erste-schritte.md) | Container starten, erstes Programm, sauber stoppen. / Start the container, first program, stop cleanly. |
| 5 (optional) | [vscode-dev-containers.md](vscode-dev-containers.md) | Mit VS Code direkt im Container arbeiten. / Work directly in the container with VS Code. |
| 6 | [troubleshooting.md](troubleshooting.md) | Hilfe bei typischen Fehlern. / Help with common errors. |

**DE:** Die Kurzfassung des Starts steht weiter unten unter „Schnellstart". Die
ausführliche, anfängernahe Variante findest du in
[installation.md](installation.md) und [erste-schritte.md](erste-schritte.md).

**EN:** The short version of the start is below under "Quick Start". The
detailed, beginner-friendly variant is in [installation.md](installation.md) and
[erste-schritte.md](erste-schritte.md).

---

## Bin ich bereit? / Am I Ready?

**DE:** Die Sandbox wird im Laufe der Ausbildung schrittweise wichtiger. Die Tabelle zeigt, was in welchem
Lehrjahr von dir erwartet wird.

**EN:** The sandbox becomes progressively more important during training. The table shows what is expected in
each training year.

| Lehrjahr / Year | Erwartung / Expectation | Sandbox Pflicht? / Mandatory? |
|---|---|---|
| 1. Lehrjahr / Year 1 | Verstehe die Grenzen und fuehre den ersten kontrollierten Agentenlauf nach Anleitung aus. | **Ja, sobald ein Agent genutzt wird.** Ohne Agentenlauf ist die praktische Nutzung `N/A`. / **Yes, as soon as an agent is used.** Without an agent call, practical use is `N/A`. |
| 2. Lehrjahr / Year 2 | Bereite ein **Betriebskonzept** vor: Konfiguration, Secrets, Schreibgrenzen, Laufzeitannahmen, KI-Agenten-Grenzen. | **Ja fuer jeden Agentenlauf.** Die Nachweistiefe steigt. / **Yes for every agent call.** Evidence depth increases. |
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

## Schnellstart (Kurzfassung) / Quick Start (Short Version)

**DE:** Diese Kurzfassung ist für alle, die Podman schon kennen. Wenn du **ohne
Vorkenntnisse** startest, nutze die ausführliche Anleitung
[installation.md](installation.md) und danach
[erste-schritte.md](erste-schritte.md).

**EN:** This short version is for those who already know Podman. If you start
**without prior knowledge**, use the detailed guide
[installation.md](installation.md) and then
[erste-schritte.md](erste-schritte.md).

```bash
# 1. Werkzeuge vorhanden? / Tools present?
git --version
podman --version

# 2. Repo holen / Get the repo
git clone https://github.com/hindermath/absdd-image-sandbox.git
cd absdd-image-sandbox
cp opencode.env.example opencode.env

# 3. Podman-Machine (nur macOS/Windows / only macOS/Windows)
podman machine init
podman machine start

# 4. Konfig prüfen, bauen, starten / Validate, build, start
podman-compose config
podman compose build --pull
podman compose up -d

# 5. Shell im Container / Shell in the container
podman compose exec ade bash
```

**DE:** Läuft der Container, siehst du die Eingabeaufforderung `adedev@...`.
Prüfe dann die Werkzeuge und stoppe sauber — beides erklärt
[erste-schritte.md](erste-schritte.md) Schritt für Schritt (inklusive
`scripts/compose-down-with-audit.sh --podman -v`).

**EN:** When the container runs you see the prompt `adedev@...`. Then check the
tools and stop cleanly — both explained step by step in
[erste-schritte.md](erste-schritte.md) (including
`scripts/compose-down-with-audit.sh --podman -v`).

---

## Was finde ich wo? / Where Do I Find What?

| Dokument / Document | Inhalt / Content |
|---|---|
| [container-grundlagen.md](container-grundlagen.md) | Container-Grundbegriffe für Anfänger: Image, Container, Volume, Mount, Diagramm |
| [warum-sandbox.md](warum-sandbox.md) | Container-First-Gate, vier Schutzziele, ISO 27001, Anfängerfehler |
| [installation.md](installation.md) | Podman installieren je Betriebssystem, Schritt für Schritt |
| [erste-schritte.md](erste-schritte.md) | Erster Tag: starten, erstes Programm, sauber stoppen |
| [vscode-dev-containers.md](vscode-dev-containers.md) | Host-VS-Code an den Container hängen; `code`-Befehl richtig verstehen |
| [troubleshooting.md](troubleshooting.md) | Typische Anfängerfehler: Symptom, Ursache, Lösung |
| [sandbox-profil.md](sandbox-profil.md) | Vollständiges Sandbox-Profil: Mounts, Schreibgrenzen, Netzwerk, MSL-Matrix, KI-Agenten |
| [GLOSSAR.md](GLOSSAR.md) | Erklärungen für Abkürzungen wie MSL, SBOM, CL_12, P0 |
| [sandbox-readiness-template.md](sandbox-readiness-template.md) | Ausfüllbare Vorlage für die Jahr-2-Sandbox-Entscheidung |
| [betriebsnachweise-template.md](betriebsnachweise-template.md) | Vorlage für Betriebsnachweise (Jahr 3, SI- und DV-Track) |
| [../../README.md](../../README.md) | Ausführliche Anleitung für Entwickler und Administratoren |
| [../secure-development/](../secure-development/) | Richtlinie, 12 Checklisten und Leitlinien für sichere Entwicklung |

---

## Verbindung zur Lernreihe / Connection to the Learning Series

**DE:** Die `absdd-image-sandbox` ist das oeffentliche Referenz-Repository fuer
die drei Secure-Trader-Lernreihen. Die passenden Erklaerungen findest du in
deinem persoenlichen `home-baseline-tmp`-Fork. Der Startpunkt ist die oben
verlinkte zentrale Anleitung.

**EN:** The `absdd-image-sandbox` is the public reference repository for the
three Secure Trader learning series. The matching study companions are in your
personal `home-baseline-tmp` fork. Start with the canonical guide linked above.

| Lehrjahr / Year | Lernbegleiter-Datei / Study Companion File |
|---|---|
| 1. Lehrjahr / Year 1 | `docs/learning-units/lernbegleiter/Secure-CaseTracker_09_Sandbox-und-Agentische-Entwicklung.Lernbegleiter.md` |
| 2. Lehrjahr / Year 2 | `docs/learning-units/lernbegleiter/Secure-CaseTracker-v2_09_Sandbox-und-Betriebsnachweise.Lernbegleiter.md` |
| 3. Lehrjahr SI / Year 3 SI | `docs/learning-units/lernbegleiter/Secure-CaseTracker-Operations-Track_02_Sandbox-und-Laufzeitprofil.Lernbegleiter.md` |
| 3. Lehrjahr DV / Year 3 DV | `docs/learning-units/lernbegleiter/Secure-CaseTracker-Digital-Networking-Track_09_Sandbox-Integration-und-Betriebsnachweise.Lernbegleiter.md` |

---

## Häufige Fragen / Frequently Asked Questions

**DE:** **Ich starte im 1. Lehrjahr — muss ich die Sandbox wirklich nutzen?**
Unterscheide zwei Dinge. Das **Container-First-Gate** gilt ab dem 1. Lehrjahr verbindlich: Wenn du einen
KI-Agenten nutzt, läuft er **im Container**, nie auf dem Arbeitsplatz-Rechner (siehe
[warum-sandbox.md](warum-sandbox.md)). Ohne Agentenaufruf kann die praktische
Nutzung `N/A` sein. Sobald du einen Agenten startest, ist die Sandbox anwendbar
und verpflichtend; das gilt auch fuer den ersten kleinen Schreibversuch.

**EN:** **I am in year 1 — do I really have to use the sandbox?**
Distinguish two things. The **Container-First Gate** applies from year 1 as binding: if you use an AI agent,
it runs **inside the container**, never on the workstation (see [warum-sandbox.md](warum-sandbox.md)). Without
an agent call, practical use may be `N/A`. As soon as you start an agent, the
sandbox is applicable and mandatory, including the first small write exercise.

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
Niemals im Repository oder in Prompts. Nutze die offizielle interaktive
Anmeldung des gewaehlten Agenten. `opencode.env` ist nur fuer eine bewusst
lokal konfigurierte OpenCode-Provider-Variable vorgesehen und bleibt
ungetrackt.

**EN:** **Where do I enter secrets?**
Never in the repository or in prompts. Use the selected agent's official
interactive sign-in. `opencode.env` is only for a deliberately local OpenCode
provider variable and remains untracked.

---

## Nächste Schritte / Next Steps

**DE:** Lies das [sandbox-profil.md](sandbox-profil.md), um die Grenzen dieser Umgebung zu verstehen. Dann
arbeite den Lernbegleiter für dein Lehrjahr durch und bearbeite das zugehörige Lastenheft.

**EN:** Read [sandbox-profil.md](sandbox-profil.md) to understand the boundaries of this environment. Then
work through the study companion for your training year and complete the related intake document.
