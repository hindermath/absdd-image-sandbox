# KI-Agenten und Spec Kit / AI Agents and Spec Kit

## Was das Image bereitstellt / What the Image Provides

**DE:** Das Image installiert sechs aufrufbare Agentenwerkzeuge. Eine
Installation ist **keine** Provider-, Modell-, Datenschutz- oder
Kostenfreigabe. Vor dem ersten echten Auftrag meldest du das gewählte Werkzeug
über seinen offiziellen interaktiven Weg an und prüfst, ob der Einsatz für
dein Projekt erlaubt ist. Das Repository speichert keinen API-Schlüssel und
wählt kein Modell für dich aus.

**EN:** The image installs six callable agent tools. Installation is **not**
provider, model, privacy, or cost approval. Before the first real task, sign in
through the selected tool's official interactive flow and verify that its use
is allowed for your project. The repository stores no API key and selects no
model for you.

| Werkzeug / Tool | Kommando / Command | Rolle im Image / Role in image | Persistenter Zustand / Persistent state |
|---|---|---|---|
| OpenCode | `opencode` | zusätzliche, providerneutrale Oberfläche / additional provider-neutral interface | `opencode_data` |
| Codex CLI | `codex` | Required-Agent / required agent | `codex_data` |
| Claude Code | `claude` | Required-Agent / required agent | `claude_data` |
| Gemini CLI | `gemini` | zusätzliches Google-CLI / additional Google CLI | `gemini_data` |
| Antigravity CLI | `agy` | Required-Agent; Printmodus experimentell / required agent; print mode experimental | `gemini_data` |
| GitHub Copilot CLI | `copilot` | Required-Agent; GitHub-Profil / required agent; GitHub profile | `copilot_data` |

**DE:** Benannte Volumes trennen die Zustände voneinander. `podman compose
down -v` löscht diese Volumes und damit lokale Anmeldungen. Nutze vorher immer
den Audit-Wrapper und prüfe, ob die Löschung wirklich beabsichtigt ist.

**EN:** Named volumes separate the tools' state. `podman compose down -v`
deletes these volumes and local sign-ins. Always use the audit wrapper first
and verify that deletion is truly intended.

## Vor jedem Agentenlauf / Before Every Agent Run

1. **DE:** Prüfe `pwd`, `git status --short --branch` und die lokalen
   Anweisungsdateien. **EN:** Check `pwd`, `git status --short --branch`, and
   local instruction files.
2. **DE:** Formuliere einen engen Auftrag mit erwarteten Dateien und Tests.
   **EN:** Write a narrow task with expected files and tests.
3. **DE:** Entferne Secrets, echte Personendaten und vertrauliche Inhalte aus
   Prompt und Testdaten. **EN:** Remove secrets, real personal data, and
   confidential content from prompts and test data.
4. **DE:** Prüfe Berechtigungs- und Sandbox-Hinweise des Werkzeugs. Erweitere
   Rechte nicht nur aus Bequemlichkeit. **EN:** Review permission and sandbox
   notices. Do not broaden permissions merely for convenience.
5. **DE:** Lies Diff, Tests und verbleibende Warnungen selbst. **EN:** Review
   the diff, tests, and remaining warnings yourself.

## Interaktiver Einstieg / Interactive Entry

**DE:** Öffne zuerst eine Shell im laufenden Container und wechsle in dein
Projekt. Starte danach genau das freigegebene Werkzeug:

**EN:** First open a shell in the running container and change to your project.
Then start exactly the approved tool:

```bash
podman compose exec ade bash
cd /workspace
git status --short --branch
```

```text
opencode
codex
claude
gemini
agy
copilot
```

**DE:** Die letzte Liste zeigt alternative Befehle, die nicht gemeinsam
gestartet werden. Folge dem offiziellen Dialog des gewählten Werkzeugs. Die
Dokumentation automatisiert weder Anmeldung noch Provider- oder Modellwahl.

**EN:** The last list shows alternative commands; do not start all of them
together. Follow the selected tool's official dialog. This documentation does
not automate sign-in, provider selection, or model selection.

## Einzelauftrag ohne TUI / Single Task Without a TUI

**DE:** Die Bash- und PowerShell-Dispatcher besitzen dieselbe Zuordnung. Der
Host-Aufruf zielt standardmäßig auf den laufenden Compose-Service `ade`; im
Image wird die CLI direkt ausgeführt. Verwende stdin oder `--prompt-file`,
wenn der Prompt nicht in Shell-Historie oder Prozessliste erscheinen soll.

**EN:** The Bash and PowerShell dispatchers use the same mapping. The host
entrypoint targets the running Compose service `ade` by default; inside the
image it invokes the CLI directly. Use stdin or `--prompt-file` when the prompt
must not appear in shell history or a process list.

```bash
printf '%s\n' 'Pruefe den aktuellen Diff und aendere nichts.' | \
  scripts/agent-prompt.sh codex

scripts/agent-prompt.sh --dry-run opencode -- \
  'Dieser Prompt wird in der Vorschau nicht ausgegeben.'
```

```powershell
Get-Content -Raw .\auftrag.txt |
  pwsh -NoProfile -File scripts/agent-prompt.ps1 claude
```

**DE:** `--dry-run` zeigt Ziel und Kommando, aber schwärzt den Prompt. Der
Dispatcher setzt keine Flags für Approval-Umgehung oder erweiterte Rechte.
Antigravity-Printmodus bleibt experimentell; prüfe Ausgabe und Exitcode.

**EN:** `--dry-run` shows target and command while redacting the prompt. The
dispatcher sets no approval-bypass or permission-broadening flags.
Antigravity print mode remains experimental; review output and exit status.

Die vollständige Argumentreferenz steht in
[agent-prompt.md](agent-prompt.md). / The complete argument reference is in
[agent-prompt.md](agent-prompt.md).

## Spec Kit ohne Vorwissen / Spec Kit Without Prior Experience

**DE:** Spec Kit unterstützt **spezifikationsgetriebene Entwicklung**. Dabei
wird zuerst verständlich festgelegt, was erreicht werden soll. Danach folgen
technischer Plan, umsetzbare Aufgaben und erst dann die Implementierung.

**EN:** Spec Kit supports **specification-driven development**. First, it
states clearly what should be achieved. A technical plan and actionable tasks
follow, and implementation begins only afterwards.

| Artefakt oder Zustand / Artifact or state | Bedeutung / Meaning |
|---|---|
| `spec.md` | fachliche Anforderungen und Erfolgskriterien / requirements and success criteria |
| `plan.md` | technische Lösung und Grenzen / technical solution and boundaries |
| `tasks.md` | geordnete, prüfbare Arbeitsschritte / ordered, testable work items |
| Implementierung / implementation | Änderungen gemäß freigegebenem Plan / changes following an approved plan |
| Analyse / analysis | schreibfreie Konsistenzprüfung / read-only consistency check |

## Spec Kit prüfen und initialisieren / Check and Initialize Spec Kit

```bash
specify version
specify check
cd /rider-projects/mein-projekt
specify init . --integration opencode --force
```

**DE:** Wenn Spec Kit nach dem Skripttyp fragt, wähle in diesem Linux-
Container `sh`. Prüfe danach alle neu erzeugten Dateien und entscheide für das
Projekt, ob `.opencode/` vollständig oder teilweise versioniert wird.

**EN:** If Spec Kit asks for a script type, choose `sh` in this Linux
container. Afterwards, review every generated file and decide for the project
whether `.opencode/` is fully or partly version-controlled.

## Autoritätsgrenzen / Authority Boundaries

**DE:** Eine vorhandene Spezifikation, ein als `Ready` oder `Eligible`
markierter Intake und eine erzeugte `tasks.md` sind Reihenfolge- und
Governance-Nachweise. Sie erlauben nicht automatisch Implementierung, Commit,
Push, Pull Request, Merge oder Admin-Bypass. Dafür braucht es einen neuen,
ausdrücklichen Auftrag.

**EN:** An existing specification, an intake marked `Ready` or `Eligible`, and
a generated `tasks.md` are ordering and governance evidence. They do not
automatically authorize implementation, commit, push, pull request, merge, or
admin bypass. Those actions require a new explicit instruction.

**DE:** Modellnamen gehören nicht in Feature-Artefakte. Die operative
Agentenwahl kann sich ändern, ohne dass Anforderungen und Plan neu geschrieben
werden müssen.

**EN:** Model names do not belong in feature artifacts. Operational agent
routing may change without rewriting requirements and plans.

## Nächste Schritte / Next Steps

**DE:** Lies vor einer Änderung das [Sandbox-Profil](sandbox-profil.md) und den
[Git- und Hosting-Ablauf](git-und-hosting.md). Beginne bei einem bestehenden
Projekt immer mit dessen eigenen Anweisungen.

**EN:** Before changing anything, read the [sandbox profile](sandbox-profil.md)
and the [Git and hosting workflow](git-und-hosting.md). For an existing
project, always begin with its own instructions.
