# Für Lernende: Einstieg in die Sandbox-Umgebung / For Learners: Getting Started

**Stand / Date:** 2026-10-25
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

---

## Worum geht es hier? / What Is This?

**DE:** Die `absdd-image-sandbox` ist eine **Container-Umgebung** für sichere
Softwareentwicklung mit KI-Agenten. Sie bietet eine abgeschottete Umgebung, in
der du mit begrenzten Rechten lernst. Beschreibbare Host-Mounts und
Netzverbindungen bleiben echte Risiken. Sie enthält die Basiswerkzeuge (Sprachlaufzeiten, Testtools,
KI-Agenten) für die drei Secure-Trader-Lernprojekte CaseTracker, OrderDesk und
ServiceHarvester.

**EN:** The `absdd-image-sandbox` is a **container environment** for secure software development with AI
agents. It provides a restricted learning space, not absolute host isolation.
Writable host mounts and network access remain real risks. It contains the baseline tools (language runtimes, test tools, AI agents) for the three Secure
Trader training projects: CaseTracker, OrderDesk, and ServiceHarvester.

**DE:** Die öffentliche Referenzadresse lautet: `https://github.com/hindermath/absdd-image-sandbox`

**EN:** The public reference address is: `https://github.com/hindermath/absdd-image-sandbox`

**DE:** Deine Institution kann diese Referenz nach GitLab, Codeberg, Forgejo
oder ein eigenes Git-System uebertragen. Dann verwendest du die dort
bereitgestellte URL und brauchst kein GitHub-Konto.

**EN:** Your institution may transfer this reference to GitLab, Codeberg,
Forgejo, or its own Git system. In that case, use the provided URL and no
GitHub account is required.

---

## Neu hier? Ohne Vorkenntnisse? / New Here? No Prior Knowledge?

**DE:** Der [Fork-/Template-Vergleich](template-profil.md) erklärt die spätere
optionale unabhängige Sandbox-Kopie. Fork bleibt Standard; Template ist noch
nicht aktiviert. [Lizenz/Herkunft](../licensing.md) und persönliche Übernahme-
Gates gelten unabhängig vom Bezugsweg.

**EN:** The fork/template comparison explains a later optional independent
sandbox copy. Fork remains default; template is not enabled. License/provenance
and personal handover gates apply to either route.

**DE:** Waehle zuerst deinen [Lernweg](lernwege.md). Fuer Softwareentwickler
mit Git-Erfahrung gibt es einen [Kurzpfad](entwickler-kurzpfad.md). Fuer die
taegliche Nutzung helfen [Alltag](alltag.md), [FAQ](faq.md) und die
[Hinweise zur Barrierefreiheit](barrierefreiheit.md).

**EN:** Choose your learning path first. Developers with Git experience can
use the short path. Daily workflow, FAQ and accessibility guidance support
repeated use.

**DE:** Für angeleitete Gruppenarbeit gibt es den
[neutralen Spec-Kit-Workshop](../praesentationen/README.md) als Markdown und
PowerPoint, jeweils auf Deutsch und Englisch. Beispiele sind keine
automatischen Ausführungs- oder Installationsaufträge.

**EN:** Guided group work can use the neutral Spec Kit workshop linked above:
Markdown and PowerPoint in both German and English. Examples grant no
automatic execution or installation authority.

**DE:** Danach verbinden die [Projektwerkstätten](../lernwerkstaetten/README.md)
Präsentationen mit eigener praktischer Arbeit: SysInfoTool in sechs Stufen
oder eine Webanwendung mit begründeter Wahl zwischen MVC und MVC plus REST-API.
Die Intake-Pakete werden erst im persönlichen Lernrepo geprüft und aktiviert.

**EN:** The project workshops then connect presentations and personal practice:
six SysInfo stages or a justified choice between MVC and MVC plus REST API.
Intake packages are reviewed and activated only in the personal learning repo.

**DE:** Wenn du noch **nie mit Containern gearbeitet** hast, folge dieser
Reihenfolge. Jedes Dokument baut auf dem vorherigen auf und setzt kein Vorwissen
voraus.

**EN:** If you have **never worked with containers**, follow this order. Each
document builds on the previous one and assumes no prior knowledge.

**DE:** Beginne mit der zentralen, betriebssystemuebergreifenden
`START-HERE-FUER-LERNENDE.md`. Das Image enthaelt einen gepinnten read-only
Stand unter `~/home-baseline-source`; damit kannst du die Anleitung direkt lesen.
Die [oeffentliche Referenz](https://github.com/hindermath/home-baseline/blob/main/docs/learning-units/START-HERE-FUER-LERNENDE.md)
zeigt den aktuellen Upstream-Stand und kann neuer als das Image sein. Fuer den
offline eingebauten Stand sind Release und Commit in
`home-baseline.lock.json` massgeblich. Fuer Aenderungen und Pushes ersetzt du
den eingebauten Stand spaeter durch dein persoenliches oder institutionell
bereitgestelltes `home-baseline`-Repository. Die
[Home-Baseline-Architektur](https://github.com/hindermath/home-baseline/blob/main/docs/architecture/source-and-home-runtime.md)
erklaert die Grenze zwischen Quelle und Home Runtime.

**EN:** Start with the cross-platform `START-HERE-FUER-LERNENDE.md`. The image
contains a pinned read-only copy at `~/home-baseline-source`, so you can read the
guide immediately. The
[public reference](https://github.com/hindermath/home-baseline/blob/main/docs/learning-units/START-HERE-FUER-LERNENDE.md)
shows the current upstream state and may be newer than the image. The release
and commit in `home-baseline.lock.json` define the embedded offline state. For
changes and pushes, replace the embedded reference later with your personal or
institution-provided `home-baseline` repository. The
[Home Baseline architecture](https://github.com/hindermath/home-baseline/blob/main/docs/architecture/source-and-home-runtime.md)
explains the boundary between source and Home Runtime.

| Schritt / Step | Dokument / Document | Inhalt / Content |
|---|---|---|
| 1 | [container-grundlagen.md](container-grundlagen.md) | Was ist ein Container, Image, Volume, Mount? / What is a container, image, volume, mount? |
| 2 | [warum-sandbox.md](warum-sandbox.md) | Warum eine Sandbox? Gate, Schutzziele, ISO 27001. / Why a sandbox? Gate, protection goals, ISO 27001. |
| 3 | [installation.md](installation.md) | Podman installieren je Betriebssystem. / Install Podman per operating system. |
| 4 | [erste-schritte.md](erste-schritte.md) | Container starten, erstes Programm, sauber stoppen. / Start the container, first program, stop cleanly. |
| 5 | [git-und-hosting.md](git-und-hosting.md) | `origin`, `upstream`, Branch und Review providerneutral verstehen. / Understand `origin`, `upstream`, branches, and review without provider lock-in. |
| 6 | [toolchains/README.md](toolchains/README.md) | Die passende Sprache im vorgesehenen Projekt-Mount verwenden. / Use the selected language in its intended project mount. |
| 7 | [agenten-und-spec-kit.md](agenten-und-spec-kit.md) | Agenten, sichere Auftraege und Spec-Kit-Artefakte verstehen. / Understand agents, safe tasks, and Spec Kit artifacts. |
| 8 (optional) | [vscode-dev-containers.md](vscode-dev-containers.md) | Mit VS Code direkt im Container arbeiten. / Work directly in the container with VS Code. |
| 9 | [troubleshooting.md](troubleshooting.md) | Hilfe bei typischen Fehlern. / Help with common errors. |

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
| 1. Lehrjahr / Year 1 | Grenzen verstehen; optionalen kontrollierten Agentenlauf nach Voraussetzungen durchfuehren. / Understand boundaries; perform the optional controlled agent task only after meeting prerequisites. | **Ja, sobald ein Agent genutzt wird.** Ohne Agentenlauf ist die praktische Nutzung `N/A`. / **Yes, as soon as an agent is used.** Without an agent call, practical use is `N/A`. |
| 2. Lehrjahr / Year 2 | Betriebskonzept fuer Konfiguration, Secrets, Schreib- und Laufzeitgrenzen vorbereiten. / Prepare an operating concept for configuration, secrets, write and runtime boundaries. | **Ja fuer jeden Agentenlauf.** Die Nachweistiefe steigt. / **Yes for every agent call.** Evidence depth increases. |
| 3. Lehrjahr SI / Year 3 SI | Sandbox fuer KI-Schreibarbeit und riskante Experimente nutzen; Betriebsnachweise liefern. / Use the sandbox for AI writes and risky experiments; provide operating evidence. | Ja (SI-Track und DV-Track). / Yes (SI track and DV track). |
| 3. Lehrjahr DV / Year 3 DV | Netzwerkzugriffe, Mounts und Abweichungen im Referenzprofil dokumentieren. / Document network access, mounts and deviations in the reference profile. | Ja (SI-Track und DV-Track). / Yes (SI track and DV track). |
| 3. Lehrjahr AE/DPA / Year 3 AE/DPA | Relevant, aber weniger zentral als fuer SI/DV. / Relevant, but less central than for SI/DV. | Teils — je nach Aufgabe. / Partial — depends on the task. |

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
SANDBOX_REPO_URL="<URL-DEINES-FORKS-ODER-INSTITUTIONELLEN-REPOS>"
git clone "$SANDBOX_REPO_URL" absdd-image-sandbox
cd absdd-image-sandbox
if [ ! -e .env ]; then cp .env.example .env; fi
if [ ! -e opencode.env ]; then cp opencode.env.example opencode.env; fi

# 3. Podman-Machine (nur macOS/Windows / only macOS/Windows)
podman machine list
# init nur wenn noch keine Machine besteht / init only if no machine exists
podman machine start

# 4. Konfig prüfen, bauen, starten / Validate, build, start
podman-compose config
podman compose build --pull
podman compose up -d

# 5. Shell im Container / Shell in the container
podman compose exec ade bash

# 6. Eingebaute Lernreihen-Referenz / Embedded learning-series reference
cd ~/home-baseline-source
git log -1 --oneline
```

**DE:** Läuft der Container, siehst du die Eingabeaufforderung `adedev@...`.
Prüfe dann die Werkzeuge und stoppe sauber — beides erklärt
[erste-schritte.md](erste-schritte.md) Schritt für Schritt (inklusive
`scripts/compose-down-with-audit.sh --podman` ohne Volume-Loeschung).

**EN:** When the container runs you see the prompt `adedev@...`. Then check the
tools and stop cleanly — both explained step by step in
[erste-schritte.md](erste-schritte.md) (including
`scripts/compose-down-with-audit.sh --podman` without volume deletion).

---

## Was finde ich wo? / Where Do I Find What?

| Dokument / Document | Inhalt / Content |
|---|---|
| [container-grundlagen.md](container-grundlagen.md) | Container-Grundbegriffe für Anfänger: Image, Container, Volume, Mount, Diagramm / Container basics: image, container, volume, mount and diagram |
| [warum-sandbox.md](warum-sandbox.md) | Container-First-Gate, vier Schutzziele, ISO 27001, Anfängerfehler / Container-first gate, four protection goals, ISO 27001 and beginner mistakes |
| [installation.md](installation.md) | Podman installieren je Betriebssystem, Schritt für Schritt / Install Podman for your OS, step by step |
| [erste-schritte.md](erste-schritte.md) | Erster Tag: starten, erstes Programm, sauber stoppen / First day: start, first program and safe shutdown |
| [vscode-dev-containers.md](vscode-dev-containers.md) | Host-VS-Code an den Container hängen; `code`-Befehl richtig verstehen / Attach host VS Code; understand the code command |
| [agent-prompt.md](agent-prompt.md) | Einen einzelnen Agenten-Prompt aus Bash oder PowerShell sicher an den Container uebergeben / Send one agent prompt safely from Bash or PowerShell |
| [agenten-und-spec-kit.md](agenten-und-spec-kit.md) | Alle installierten Agenten, Anmeldungsgrenzen, sicherer Arbeitsablauf und Spec Kit / Installed agents, sign-in boundaries, safe workflow and Spec Kit |
| [git-und-hosting.md](git-und-hosting.md) | Providerneutraler Fork-, `origin`-/`upstream`-, Branch- und Review-Ablauf / Provider-neutral fork, origin/upstream, branch and review workflow |
| [toolchains/README.md](toolchains/README.md) | Index fuer .NET, Java, Go, Rust, Python, PowerShell, Swift und Node.js / Index for .NET, Java, Go, Rust, Python, PowerShell, Swift and Node.js |
| [troubleshooting.md](troubleshooting.md) | Typische Anfängerfehler: Symptom, Ursache, Lösung / Beginner errors: symptom, cause and solution |
| [sandbox-profil.md](sandbox-profil.md) | Vollständiges Sandbox-Profil: Mounts, Schreibgrenzen, Netzwerk, MSL-Matrix, KI-Agenten / Full sandbox profile: mounts, write boundaries, network, language matrix and agents |
| [GLOSSAR.md](GLOSSAR.md) | Erklärungen für Abkürzungen wie MSL, SBOM, CL_12, P0 / Explain abbreviations such as MSL, SBOM, CL_12 and P0 |
| [sandbox-readiness-template.md](sandbox-readiness-template.md) | Ausfüllbare Vorlage für die Jahr-2-Sandbox-Entscheidung / Fillable template for the second-year sandbox decision |
| [betriebsnachweise-template.md](betriebsnachweise-template.md) | Vorlage für Betriebsnachweise (Jahr 3, SI- und DV-Track) / Operating-evidence template for third-year SI and DV |
| [../../README.md](../../README.md) | Ausführliche Anleitung für Entwickler und Administratoren / Detailed guide for developers and administrators |
| [../betrieb/README.md](../betrieb/README.md) | Technische Image-, Compose-, Validierungs- und Wartungsreferenz / Technical image, Compose, validation and maintenance reference |
| [../secure-development/](../secure-development/) | Richtlinie, 12 Checklisten und Leitlinien für sichere Entwicklung / Guideline, twelve checklists and secure-development guidance |

---

## Verbindung zur Lernreihe / Connection to the Learning Series

**DE:** Die `absdd-image-sandbox` ist das oeffentliche Referenz-Repository fuer
die drei Secure-Trader-Lernreihen. Die passenden Erklaerungen findest du sofort
in der eingebauten read-only Referenz unter `~/home-baseline-source`. Sobald du
Inhalte aendern, committen oder pushen willst, bindest du dort deinen
persoenlichen Checkout ein.

Diese drei eigenen Projekt-Mounts sind ein Image-Profil, kein vollstaendiges
Verzeichnis aller Home-Baseline-Lernreihen. Weitere Reihen im Home-Baseline-
Katalog bleiben dort kanonisch dokumentiert.

**EN:** The `absdd-image-sandbox` is the public reference repository for the
three Secure Trader learning series. The matching study companions are
immediately available in the embedded read-only reference at
`~/home-baseline-source`. Mount your personal checkout there when you need to edit,
commit, or push content.

These three dedicated project mounts are an image profile, not a complete
directory of every Home Baseline learning series. Additional series remain
canonically documented in the Home Baseline catalog.

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

**DE:** Lies das [sandbox-profil.md](sandbox-profil.md), um die Grenzen dieser
Umgebung zu verstehen. Prüfe danach den
[Git- und Hosting-Ablauf](git-und-hosting.md), wähle deine
[Toolchain](toolchains/README.md) und lies vor dem ersten KI-Auftrag
[Agenten und Spec Kit](agenten-und-spec-kit.md). Arbeite anschließend den
Lernbegleiter für dein Lehrjahr durch und bearbeite das zugehörige Lastenheft.

**EN:** Read [sandbox-profil.md](sandbox-profil.md) to understand the boundaries
of this environment. Then check the [Git and hosting workflow](git-und-hosting.md),
choose your [toolchain](toolchains/README.md), and read
[Agents and Spec Kit](agenten-und-spec-kit.md) before your first AI task.
Afterwards, work through the study companion for your training year and
complete the related intake document.

## Aktueller Sicherheitsstatus / Current Security Status

**DE:** Lies den [datums- und imagegebundenen Versionsabgleich](../maintenance/toolchain-version-audit-2026-10-25.md)
und die [offenen Nachpruefungen](../security/toolchain-followups-2026-10-25.md).
Dockerfile-Soll, gebautes Pruefimage und laufender Container sind verschiedene
Staende. Alte Vulnerabilitaetszahlen oder Feature-Zustaende werden hier nicht
als aktuelle Gesamtfreigabe wiederholt. Erfolgreicher Einstieg erteilt keine
Provider-, Security-, Rechts-, Plattform- oder A11Y-Freigabe.

**EN:** Read the dated, image-bound version audit and open follow-ups. Target
Dockerfile, built audit image and running container are different states.
Historical vulnerability counts and feature states are not repeated here as
current overall approval. Successful onboarding grants no provider, security,
legal, platform or accessibility approval.

**DE:** Naechster Schritt fuer Lernende: [Lernweg waehlen](lernwege.md).
Fuer Maintainer: offene Nachpruefungen und menschliche Entscheidungen lesen.
Die [historische Feature-Evidenz](../security/secure-development/2026-08-30-container-hardening/README.md)
bleibt nachvollziehbar, ersetzt aber keinen Test des neuen Kandidaten.

**EN:** Learners: choose your learning path. Maintainers: read open follow-ups
and human decisions. Historical feature evidence remains traceable but does
not replace testing the new candidate.
