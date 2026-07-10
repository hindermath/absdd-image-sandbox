# Erster Tag: Vom Start zum ersten Erfolg / First Day: From Start to First Success

**Stand / Date:** 2026-07-10
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

**DE:** Öffne eine Shell im Container (falls noch nicht geschehen):

**EN:** Open a shell in the container (if not already done):

```bash
podman compose exec ade bash
```

**DE:** Schau auf die Eingabeaufforderung. Steht dort `adedev@...`, bist du
**im** Container. Der Benutzer `adedev` hat bewusst **keine** Root-Rechte — das
ist Teil der Absicherung.

**EN:** Look at the prompt. If it shows `adedev@...`, you are **inside** the
container. The user `adedev` deliberately has **no** root rights — that is part
of the hardening.

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

**DE:** Jeder Befehl gibt eine **Versionsnummer** aus, zum Beispiel `10.0.x`
(für .NET) oder `go version go1.26.3 ...`. Eine Versionsnummer bedeutet: Das
Werkzeug ist installiert und einsatzbereit. Erscheint `command not found`,
stimmt etwas mit dem Container nicht — siehe
[troubleshooting.md](troubleshooting.md).

**EN:** Each command prints a **version number**, for example `10.0.x` (for
.NET) or `go version go1.26.3 ...`. A version number means: the tool is
installed and ready. If `command not found` appears, something is wrong with the
container — see [troubleshooting.md](troubleshooting.md).

**DE:** Alle Versionen auf einmal prüft dieses Skript:

**EN:** This script checks all versions at once:

```bash
bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh
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
echo 'print("Hallo aus der Sandbox / Hello from the sandbox")' > hallo.py
python hallo.py
```

**DE:** Erwartete Ausgabe:

**EN:** Expected output:

```text
Hallo aus der Sandbox / Hello from the sandbox
```

**DE:** Geschafft — du hast Code **im Container** ausgeführt, nicht auf deinem
echten Rechner. Genau das ist der Kern des Container-First-Gates.

**EN:** Done — you ran code **inside the container**, not on your real machine.
That is exactly the heart of the Container-First Gate.

**DE:** Wichtig: Nutze für Übungen fiktive, datensparsame Beispiele. Keine
echten personenbezogenen Daten, keine Secrets — auch nicht in Testdateien.

**EN:** Important: use fictitious, data-minimal examples for exercises. No real
personal data, no secrets — not even in test files.

---

## Schritt 4: Sauber und auditkonform stoppen / Step 4: Stop Cleanly and Audit-Compliant

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
bash scripts/compose-down-with-audit.sh --podman -v
```

**DE:** Das `-v` entfernt zusätzlich die persistenten Datenvolumes. Der
Audit-Export schreibt **nur Metadaten** nach `audit-logs/` — niemals Prompt-Text,
Antworten oder Secrets.

**EN:** The `-v` additionally removes the persistent data volumes. The audit
export writes **metadata only** to `audit-logs/` — never prompt text, responses,
or secrets.

**DE:** Auf Windows mit PowerShell nutzt du stattdessen:

**EN:** On Windows with PowerShell, use instead:

```powershell
.\scripts\compose-down-with-audit.ps1 -Engine podman -Volumes
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
2. **DE:** Arbeite den Lernbegleiter für dein Lehrjahr durch (verlinkt in der
   [README.md](README.md), Abschnitt „Verbindung zur Lernreihe").
   **EN:** Work through the study companion for your training year (linked in the
   [README.md](README.md), section "Connection to the Learning Series").
3. **DE:** Bei Problemen: [troubleshooting.md](troubleshooting.md).
   **EN:** If you run into problems: [troubleshooting.md](troubleshooting.md).
