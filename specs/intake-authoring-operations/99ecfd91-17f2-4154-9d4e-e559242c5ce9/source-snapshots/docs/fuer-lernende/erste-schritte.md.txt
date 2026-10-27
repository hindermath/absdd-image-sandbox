# Erster Tag: Vom Start zum ersten Erfolg / First Day: From Start to First Success

**Stand / Date:** 2026-10-25
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

**DE:** Du hast Podman installiert und den Container gestartet
([installation.md](installation.md)). Dieses Dokument begleitet dich durch
deinen ersten Tag: Werkzeuge prüfen, ein winziges Programm bauen und die
Umgebung sauber stoppen. Am Ende hast du einen echten ersten Erfolg.

**EN:** You have installed Podman and started the container
([installation.md](installation.md)). This document guides you through your
first day: check the tools, build a tiny program, and stop the environment
cleanly. At the end you will have a real first success.

---

## Schritt 1: Bin ich im Container? / Step 1: Am I Inside the Container?

**DE:** Host, Bash oder PowerShell: Oeffne eine Shell im Container (falls noch nicht geschehen):

**EN:** On the host, in Bash or PowerShell: open a container shell if needed:

```bash
podman compose exec ade bash
```

**DE:** Im Container, Bash: Pruefe `id` und `pwd`. Erwartet wird Benutzer
`adedev` mit UID ungleich `0`. Der Prompt `adedev@...` hilft zur Orientierung,
ist aber allein kein Nachweis. Non-root ist ein Teil der Absicherung.

**EN:** Inside the container, in Bash: check id and pwd. Expect adedev with a
nonzero UID. The prompt helps orientation but is not proof by itself.
Non-root is one part of the hardening.

---

## Schritt 2: Werkzeuge prüfen und die Ausgabe verstehen / Step 2: Check the Tools and Understand the Output

**DE:** Prüfe, ob die sechs Sprachen (MSL — Memory-Safe Languages) da sind:

**EN:** Check that the six languages (MSL — Memory-Safe Languages) are present:

```bash
dotnet --version
go version
java --version
python --version
rustc --version
swift --version
```

**DE:** PowerShell 7 ist die zweite Skriptgrundlage neben Python und wird
separat geprueft:

**EN:** PowerShell 7 is the second scripting foundation alongside Python and
is checked separately:

```bash
pwsh --version
```

**DE:** Jeder Befehl gibt eine **Versionsnummer** aus, zum Beispiel `10.0.x`
(für .NET) oder `go version go1.27.x ...`. Das belegt die Aufrufbarkeit,
nicht alle Funktionen oder eine Freigabe. Erscheint `command not found`,
stimmt etwas mit dem Container nicht — siehe
[troubleshooting.md](troubleshooting.md).

**EN:** Each command prints a **version number**, for example `10.0.x` (for
.NET) or `go version go1.27.x ...`. This proves the executable responds,
not all functionality or approval. If `command not found` appears, something is wrong with the
container — see [troubleshooting.md](troubleshooting.md).

**DE:** Alle Versionen auf einmal prüft dieses Skript:

**EN:** This script checks all versions at once:

```bash
bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh
```

**DE:** Zu den geprueften Werkzeugen gehoeren auch die vier Required-Agenten
und Syft. Jeder Befehl muss eine Version liefern; eine Anmeldung ist fuer
diesen Installationsnachweis noch nicht erforderlich:

**EN:** The checked tools also include the four required agents and Syft. Each
command must print a version; sign-in is not required for this installation
check:

```bash
codex --version
claude --version
agy --version
copilot --version
syft version
```

**DE:** Die vollständige Übersicht mit Test- und Audit-Befehlen je Sprache steht
in der MSL-Support-Matrix im [sandbox-profil.md](sandbox-profil.md), Abschnitt 6.

**EN:** The full overview with test and audit commands per language is in the
MSL support matrix in [sandbox-profil.md](sandbox-profil.md), section 6.

---

## Schritt 3: Dein erstes Mini-Programm / Step 3: Your First Mini Program

**DE:** Jetzt schreibst du dein erstes Programm — im dafür vorgesehenen
Ordner `/python-projects`. Warum dieser Ordner? Weil er ein **freigegebener
Schreibbereich** ist (siehe [warum-sandbox.md](warum-sandbox.md)). Alles, was du
dort speicherst, liegt auch auf deinem Host im Ordner `python-projects`.

**EN:** Now you write your first program — in the folder intended for it,
`/python-projects`. Why this folder? Because it is a **released write area**
(see [warum-sandbox.md](warum-sandbox.md)). Everything you save there also lives
on your host in the `python-projects` folder.

```bash
cd /python-projects
exercise_dir="$(mktemp -d /python-projects/first-steps.XXXXXX)"
cd "$exercise_dir"
echo 'print("Hallo aus der Sandbox / Hello from the sandbox")' > hallo.py
python hallo.py
```

**DE:** Erwartete Ausgabe:

**EN:** Expected output:

```text
Hallo aus der Sandbox / Hello from the sandbox
```

**DE:** Der Code lief im Container, die Datei liegt durch den Mount auch auf
deinem echten Rechner. Der neue Uebungsordner verhindert, dass ein vorhandenes
`hallo.py` ueberschrieben wird. Die Sicherheitsgrenze bleibt der Mount.

**EN:** Code ran in the container, but the mount stores the file on your real
host too. The new exercise directory avoids overwriting an existing hallo.py.
The mount remains the security boundary.

**DE:** Wichtig: Nutze für Übungen fiktive, datensparsame Beispiele. Keine
echten personenbezogenen Daten, keine Secrets — auch nicht in Testdateien.

**EN:** Important: use fictitious, data-minimal examples for exercises. No real
personal data, no secrets — not even in test files.

---

## Schritt 4 (optional): Erster kontrollierter Agentenlauf / Step 4 (Optional): First Controlled Agent Run

**DE:** Der technische Ersttag funktioniert ohne KI-Konto. Ohne genehmigte
Agentennutzung ueberspringst du Schritt 4 und gehst direkt zu
[Schritt 5: sicher stoppen](#schritt-5-sauber-und-auditkonform-stoppen--step-5-stop-cleanly-and-audit-compliant).
Fuer diesen optionalen Schritt brauchst du ein eigenes Projekt-Repository
(Level 2), eine passende Freigabe und gegebenenfalls Anmeldung. Lies vorher
[Sandbox-Profil](sandbox-profil.md), [Git](git-und-hosting.md) und
[Agenten und Spec Kit](agenten-und-spec-kit.md), einschliesslich der offenen
OpenCode-2-Nachpruefungen. Die Anleitung erteilt keine Nutzungserlaubnis.

**EN:** The technical first day needs no AI account. Without approved agent
use, skip step 4 and go directly to step 5, safe shutdown. This optional
step needs your own project repository (Level 2), applicable approval and
possibly sign-in. First read the sandbox profile, Git guide, and agents and
Spec Kit, including OpenCode 2 follow-ups. This guide grants no usage authority.

**DE:** Fuehre diesen Schritt nur in einem eigenen Level-2-Checkout innerhalb
eines freigegebenen Projekt-Mounts aus. Pruefe zuerst den Ausgangszustand:

**EN:** Run this step only in your own Level-2 checkout inside an approved
project mount. Check the initial state first:

```bash
cd /secure-case-tracker-projects/DEIN-LEVEL-2-REPO
git status --short --branch
```

**DE:** Starte genau einen der vier Agenten mit `codex`, `claude`, `agy`
oder `copilot`. Folge bei Bedarf der offiziellen interaktiven Anmeldung. Der
erste Auftrag ist read-only:

**EN:** Start exactly one of the four agents with `codex`, `claude`, `agy`,
or `copilot`. Follow its official interactive sign-in if needed. The first task
is read-only:

```text
Erklaere mir die Repository-Struktur und nenne die vorhandenen Testbefehle.
Veraendere keine Datei und fuehre keinen Befehl aus.
```

**DE:** Beende den Agenten und kontrolliere `git status`. Es darf keine
Aenderung geben. Starte ihn danach erneut mit einem einzigen, begrenzten
Schreibauftrag auf einem Lernzweig:

**EN:** Exit the agent and inspect `git status`. There must be no change. Then
start it again with one limited write task on a learning branch:

```bash
git switch -c learning/first-agent-run
```

```text
Lege nur docs/agent-first-run-check.md an. Schreibe genau einen deutschen und
einen englischen Satz darueber, dass der Lauf in der Sandbox erfolgte. Aendere
keine andere Datei und fuehre keinen Commit aus.
```

**DE:** Die menschliche Pruefung bleibt verbindlich:

**EN:** Human review remains mandatory:

```bash
git status --short
git diff -- docs/agent-first-run-check.md
cat docs/agent-first-run-check.md
# Danach den projektspezifischen Testbefehl aus Unit 00 ausfuehren.
```

Neue ungetrackte Dateien erscheinen nicht im normalen Diff; lies sie deshalb
zusaetzlich. Nur wenn Inhalt und Test passen, darfst du die Aenderung behalten. Andernfalls
entfernst du die Uebungsdatei wieder. Der Agent darf nie selbst Freigabe oder
Merge behaupten.

New untracked files do not appear in a normal diff, so read them too.
Keep the change only if its content and test are correct. Otherwise remove the
exercise file. The agent must never claim human approval or merge completion.

---

## Schritt 5: Sauber und auditkonform stoppen / Step 5: Stop Cleanly and Audit-Compliant

**DE:** Verlasse zuerst die Container-Shell:

**EN:** First leave the container shell:

```bash
exit
```

**DE:** Stoppe die Umgebung dann mit dem empfohlenen Wrapper-Skript. Es
exportiert **zuerst** die Audit-Metadaten und fährt **danach** den Container
herunter. Das ist die Repository-Konvention — nicht `podman compose down` allein.

**EN:** Then stop the environment with the recommended wrapper script. It
**first** exports the audit metadata and **then** shuts the container down. That
is the repository convention — not `podman compose down` alone.

```bash
bash scripts/compose-down-with-audit.sh --podman
```

**DE:** Ohne `-v` bleiben die getrennten Agenten-Volumes und lokale
Anmeldezustaende erhalten. Nur fuer einen bewusst vollstaendigen Reset verwendest
du `-v`; dabei werden diese Daten entfernt. Der Audit-Export schreibt **nur
Metadaten** nach `audit-logs/` — niemals Prompt-Text, Antworten oder Secrets.

**EN:** Without `-v`, separate agent volumes and local sign-in state remain.
Use `-v` only for an intentional full reset; it removes those data. The audit
export writes **metadata only** to `audit-logs/` — never prompt text, responses,
or secrets.

**DE:** Auf Windows mit PowerShell nutzt du stattdessen:

**EN:** On Windows with PowerShell, use instead:

```powershell
.\scripts\compose-down-with-audit.ps1 -Engine podman
```

---

## Geschafft! / Well Done!

**DE:** Du hast heute:

**EN:** Today you have:

- **DE:** verstanden, was ein Container ist und warum es eine Sandbox ist.
  **EN:** understood what a container is and why it is a sandbox.
- **DE:** Podman installiert und den Container gestartet.
  **EN:** installed Podman and started the container.
- **DE:** die Werkzeuge geprüft und ein Programm im Container ausgeführt.
  **EN:** checked the tools and run a program inside the container.
- **DE:** die Umgebung sauber und auditkonform gestoppt.
  **EN:** stopped the environment cleanly and audit-compliant.

---

## Nächste Schritte / Next Steps

**DE:** Als Nächstes:

**EN:** Next:

1. **DE:** Lies das [sandbox-profil.md](sandbox-profil.md) vollständig — es ist
   deine Referenz für Mounts, Schreibgrenzen, Netzwerk und Secrets.
   **EN:** Read the full [sandbox-profil.md](sandbox-profil.md) — it is your
   reference for mounts, write boundaries, network, and secrets.
2. **DE:** Lerne den providerneutralen
   [Git- und Hosting-Ablauf](git-und-hosting.md) kennen und waehle deine
   [Toolchain](toolchains/README.md).
   **EN:** Learn the provider-neutral
   [Git and hosting workflow](git-und-hosting.md) and choose your
   [toolchain](toolchains/README.md).
3. **DE:** Lies vor einem weiteren Agentenlauf
   [Agenten und Spec Kit](agenten-und-spec-kit.md).
   **EN:** Before another agent run, read
   [Agents and Spec Kit](agenten-und-spec-kit.md).
4. **DE:** Arbeite den Lernbegleiter für dein Lehrjahr durch (verlinkt in der
   [README.md](README.md), Abschnitt „Verbindung zur Lernreihe").
   **EN:** Work through the study companion for your training year (linked in the
   [README.md](README.md), section "Connection to the Learning Series").
5. **DE:** Bei Problemen: [troubleshooting.md](troubleshooting.md).
   **EN:** If you run into problems: [troubleshooting.md](troubleshooting.md).

## Status lesen, ohne ihn zu erraten / Read Status Without Guessing

**DE:** Ein erfolgreicher Start beweist nur deinen lokalen technischen Pfad.
Pruefe den [Versionsabgleich](../maintenance/toolchain-version-audit-2026-10-25.md)
und die [offenen Nachpruefungen](../security/toolchain-followups-2026-10-25.md).
Behaupte keine Gesamtfreigabe, setze Scan-Treffer nicht selbst auf
`not affected` und nutze den Audit-Wrapper ohne Volume-Loeschung.

**EN:** Successful startup proves only your local technical path. Check the
version audit and open follow-ups. Claim no overall approval, do not mark
scan findings not affected yourself and use audit shutdown without deleting
volumes.

**DE:** Ein moderierter Erstnutzungstest durch Learning/A11Y Review bleibt
eine echte menschliche Beobachtung. Kein Agent darf Teilnehmende oder
bestandenes Screenreader-/Plattformverhalten erfinden.

**EN:** Moderated first-use testing by Learning/A11Y Review remains a real
human observation. No agent may invent participants or passed screen-reader
or platform behaviour.
