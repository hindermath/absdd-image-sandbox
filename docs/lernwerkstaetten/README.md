# Zwei Projektwerkstätten / Two Project Workshops

## Erst verstehen, dann entwickeln / Understand Before Building

**DE:** Das [optionale Sandbox-Template](../fuer-lernende/template-profil.md)
ist kein Produktstarter. Diese Werkstätten verwenden weiterhin ein **leeres
persönliches Produktrepo** und genau ein Paket. Ein `upstream` ist dort nur
sinnvoll, wenn tatsächlich eine passende Referenz besteht; ein Remote erzeugt
keine gemeinsame Historie. Home-Baseline bleibt davon getrennt.

**EN:** The optional sandbox template is not a product starter. Workshops
still use an empty personal product repo and one package. Add upstream only
for a suitable real reference; a remote cannot create shared history. Keep
Home Baseline separate.

**DE:** Du baust ein eigenes Programm aus einem Hello-World-Starter auf.
Hello World ist ein kleines Programm, das nur eine Begrüßung ausgibt. Die
Referenzprojekte liefern fachliche Beispiele, nicht den fertigen Code für
deine Lösung. Ein Intake ist ein begrenzter Arbeitsauftrag; eine Intake-Serie
ordnet mehrere solcher Aufträge. Spec Kit macht daraus Spezifikation, Plan
und Aufgaben. Ein KI-Agent unterstützt dich; du prüfst und entscheidest.

**EN:** Build your own program from a Hello World starter: a small program
that only prints a greeting. Reference projects supply examples, not a finished
solution. An intake is a bounded work request; a series orders these requests.
Spec Kit derives a specification, plan and tasks. An AI agent assists; you
review and decide.

| Werkstatt / Workshop | Präsentation DE / EN | Praxispaket / Practice Package |
|---|---|---|
| Systeminformationen / System information | [DE](../praesentationen/werkstatt-sysinfo.de.md), [EN](../praesentationen/werkstatt-sysinfo.en.md) | [SysInfo: sechs Stufen / six stages](sysinfo/README.md) |
| Web-Architektur wählen / Choose web architecture | [DE](../praesentationen/werkstatt-web.de.md), [EN](../praesentationen/werkstatt-web.en.md) | [MVC](web-mvc/README.md) **oder / or** [MVC + REST](web-rest/README.md) |

**DE:** Vorher den [Spec-Kit-Grundlagenworkshop](../praesentationen/README.md)
und die [Sandbox-Installation](../fuer-lernende/installation.md) lesen. Es sind
keine Spec-Kit-Vorkenntnisse nötig. Terminal, Dateien und Git werden dort
eingeführt. Softwareentwickler mit diesen Grundlagen können die Erklärungen
überfliegen, müssen Entscheidungen und Sicherheitsgrenzen aber ebenso prüfen.

**EN:** Read the Spec Kit introduction and sandbox installation linked above.
No prior Spec Kit experience is required; they introduce terminals, files and
Git. Developers familiar with these basics may skim the explanations, but
must still review decisions and safety boundaries.

## Vom Paket zum persönlichen Repo / From Package to Personal Repository

**DE:** Jedes der drei Pakete ist eine eigene portable Wurzel. Die relativen
Pfade in seinen JSON-Dateien gelten **ab dem Paket**, nicht ab der Sandbox.
Alle Serien sind `Draft`; alle Produktstufen sind `Pending` (noch nicht
begonnen). Ein Receipt ist ein Herkunftsbeleg, keine Abnahme. `ReadyForReview`
bedeutet nur prüfbereit, `Enabled` nur vorhandener Prompt. Auch ein vom
Validator berechnetes `eligible` ist keine Startfreigabe.

**DE:** `Completed` in einem mitgelieferten Operationsjournal bezeichnet nur
die Erstellung der Draft-Dateien. Es ist kein Completed einer Produktstufe
und kein durchgeführtes persönliches Intake-Review. Series-Receipts mit `Ready`
bestätigen ebenfalls nur die erzeugte, hashgebundene Serienstruktur.

**EN:** Completed in an authoring journal means the draft files were created,
not that a product stage or personal intake review completed. Ready on a
series receipt likewise describes the generated hash-bound structure only.

1. Präsentation lesen und die zugehörigen Verständnisfragen beantworten.
2. SysInfo oder genau einen Web-Pfad wählen. Die Web-Entscheidung begründen.
3. Ein eigenes, leeres Lernrepo auf dem gewünschten Git-System bereitstellen.
   `origin` ist dein Repo, `upstream` eine bereitgestellte Referenz. GitHub ist
   nicht vorgeschrieben; ein privates Referenzrepo muss nicht zugänglich sein.
4. Nur den **Inhalt eines** Pakets einschließlich versteckter Dateien in das
   noch leere Repo übernehmen. Nichts über bestehende Dateien kopieren. Das
   erhält `basis.md`, `sources.json`, `intakes/` und `specs/` gemeinsam.
5. Die Sandbox weiterverwenden, nicht ihren Code zum Lernprodukt erklären.
   Im Lernrepo Sprache, Projektname und Arbeitsort festhalten; SysInfo wählt
   eine der sechs Sprachen, beide Web-Pfade verwenden C#/.NET und ASP.NET Core.
6. Spec Kit im Lernrepo kontrolliert initialisieren und passende verfügbare
   Presets prüfen. Keine Vorlage mit `--force` über bestehende Inhalte legen.
   Notwendige Installation bleibt ein gesondert genehmigter Schritt.
7. Zuerst die vollständige lokale Intake-Serie reviewen lassen. Die vorhandenen
   Authoring-Receipts ersetzen dieses Review nicht. Bei Anpassungen die
   Intake-Update-/Series-Update-Verfahren mit Archivierung nutzen.
8. Erst nach aktuellem Review und eigener Startentscheidung die Serie lokal
   aktivieren und genau die erste zulässige Stufe starten. Keine ausgelieferte
   JSON-Datei hier als Fortschritt einer Person bearbeiten.

**EN:** Each package is its own portable root. JSON paths resolve from that
root, not the sandbox root. All series are Draft and all stages Pending.
Receipts prove provenance, not acceptance. ReadyForReview, Enabled or computed
eligibility grant no execution authority.

1. Read the presentation and answer its questions.
2. Choose SysInfo or exactly one web route; justify the web decision.
3. Prepare an empty personal learning repository on your chosen Git host.
   Origin is personal, upstream is the provided reference; GitHub is optional.
4. Copy the entire contents of one package into that empty repository without
   overwriting files. Keep basis, sources, intakes and specs together.
5. Record language, project name and working directory. SysInfo selects one of
   six languages; web routes use C#/.NET and ASP.NET Core.
6. Initialize Spec Kit carefully and review available governance presets.
   Installation requires separate authority; do not force-copy over content.
7. Review the full local intake series before execution. Use governed updates
   and archives if you adapt it; authoring receipts are not review results.
8. After current review and a human start decision, activate locally and run
   only the first permitted stage. Personal progress never changes this copy.

## Spec-Kit-Arbeitsrunde / A Spec Kit Work Cycle

**DE:** Je Stufe: Auftrag lesen → Intake Review → Specify → bei wesentlicher
Unklarheit Clarify → Plan → Anforderungs-Checklist → Tasks → Analyze →
beauftragte Korrekturen → ausdrücklich genehmigtes Implement → technische
Prüfung und menschliche Abnahme. Die Verfassung beschreibt dauerhafte
Projektprinzipien; sie wird vor der ersten Spezifikation geprüft. Eine
Checklist prüft Anforderungen, kein funktionierendes Programm. Analyze ist
lesend. Weder wiederholte Prüfungen noch grüne Checks ersetzen Entscheidungen.
Bei einem Blocker stoppen; nicht unbegrenzt bis zum gewünschten Urteil laufen.

**EN:** Per stage: read intake, review it, Specify, Clarify material ambiguity,
Plan, requirements Checklist, Tasks, read-only Analyze, authorized remediation,
explicitly authorized Implement, technical validation and human acceptance.
Review the constitution before the first specification. Requirements checks
are not product tests. Stop on blockers; do not repeat until a preferred verdict.

**DE:** Die Intake-Prompts verwenden die Codex-Schreibweise `$speckit-…`.
Sie sind Agentenaufträge, keine Shell-Befehle. Für andere Integrationen die
tatsächlich installierten Befehle prüfen. Der begleitete Einzelbefehl-Weg
ist der Einstieg; Autonomous ist nur eine spätere Alternative nach eigenem
Auftrag. Kein Prompt darf anmelden, Provider wählen oder Berechtigungen erweitern.

**EN:** Intake prompts use Codex skill syntax, not shell commands. Check the
installed commands for other integrations. Guided individual steps come first;
Autonomous is an optional later route requiring its own authorization. No
prompt may sign in, choose providers or broaden permissions.

## Berufsaufgaben / Occupational Perspectives

| Perspektive / Perspective | Eigenes überprüfbares Ergebnis / Observable Result |
|---|---|
| Fachinformatik Anwendungsentwicklung / Software development | Einen Negativfall mit Eingabe, Erwartung und Test erklären / explain one negative test |
| Fachinformatik Systemintegration / Systems integration | Prozess, Port, Speicherort und Rechte zuordnen / map process, port, storage and permissions |
| Fachinformatik Daten- und Prozessanalyse / Data and process analysis | Datenweg, Pflichtfelder und Fehlzustände beschreiben / describe data flow and failure states |
| Fachinformatik Digitale Vernetzung / Digital networking | Eine Schnittstellengrenze und einen Ausfall nachvollziehen / trace an interface and failure |
| IT-System-Elektronik / IT systems electronics | Container-, VM- und Host-Beobachtung auseinanderhalten / distinguish container, VM and host observations |
| Digitalisierungsmanagement / Digitalisation management | Nutzen, Muss-Anforderung und Abnahmebeleg verbinden / connect value, requirement and evidence |
| IT-System-Management / IT systems management | Betriebsaufwand, Kostenannahme und Übergabe begründen / justify operating effort and handover |

## Prüfgrenzen / Acceptance Boundaries

**DE:** Nur eigene Übungsdaten und Instanzen verwenden. Mounts sind echte
Host-Dateien. Kein Engine-Socket, privilegierter Container oder gesamtes
Home-Verzeichnis wird für diese Werkstätten benötigt. SBOM-, Rechts-, Provider-,
Release- und Sicherheitsfreigaben nicht erfinden. Offene Punkte tragen Owner,
Follow-up und Re-Evaluation-Trigger; N/A braucht eine Begründung.

**EN:** Use only personal practice data and instances. Mounts expose real host
files. No engine socket, privileged container or whole-home mount is needed.
Do not invent SBOM, legal, provider, release or security approval. Open items
need an owner, follow-up and trigger; N/A needs a reason.

**DE:** Menschliche Erstnutzung, Screenreader-/Tastaturprüfung und vollständige
WCAG-2.2-AA-Abnahme: **Open**, Owner Learning/A11Y Review; Follow-up beide
Sprachen mit Lernenden und assistiven Werkzeugen prüfen; Trigger vor einer
Konformitätsbehauptung oder unbegleitetem Einsatz. Technische Dokumentprüfung
ist keine abgeschlossene Barrierefreiheitsabnahme.

**EN:** Human first use, screen-reader/keyboard testing and full WCAG 2.2 AA
acceptance remain Open. Owner: Learning/A11Y Review; follow up with learners
and assistive tools in both languages before conformance claims or unattended
use. Static document checks do not establish accessibility acceptance.

**Moderation / Instructor:** [Getrennte Hinweise und Musterantworten / Separate notes and example answers](moderation.md).
