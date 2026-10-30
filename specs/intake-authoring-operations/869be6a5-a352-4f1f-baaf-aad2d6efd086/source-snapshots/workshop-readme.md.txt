# Workshop-Präsentationen / Workshop Presentations

## Home Baseline, Sandbox und Projekt / Home Baseline, Sandbox and Project

**DE:** Drei Bausteine gehören zusammen: **Home Baseline** liefert die
Lernreihen, Level-0-Grundlagen und agentischen Arbeitskonventionen. Die
**Sandbox** stellt dafür die kontrolliert zu nutzende Werkzeugumgebung bereit.
In **persönlichen Projektrepos** bearbeitest du die praktischen Übungen und
eigene Spec-Kit-Aufträge. Diese Repos sind keine Kopien der gesamten Sandbox.
Die Home-Baseline-Referenz im Image ist schreibgeschützt und durch
[`home-baseline.lock.json`](../../home-baseline.lock.json) gepinnt; die
Online-Referenz kann neuer sein. Es gibt keinen automatischen Runtime-Sync.
Lies den [Lernwege-Zusammenhang](../fuer-lernende/lernwege.md#verbindung-zu-home-baseline--connection-to-home-baseline)
und den [Referenz-/Override-Vertrag](../../README.md#home-baseline-referenz-und-persoenlicher-override).

**EN:** Three components work together: **Home Baseline** supplies learning
series, Level-0 foundations and agentic working conventions. The **sandbox**
provides the tooling environment for controlled use. **Personal project repos**
hold practical exercises and your own Spec Kit tasks, not copies of the whole
sandbox. The embedded Home Baseline reference is read-only and pinned by the
linked lock file; the online reference may be newer. No runtime sync runs
automatically. The linked learning-path and reference/override explanations
remain the canonical guidance.

## Materialien / Materials

**DE:** Der Workshop erklärt die Nutzung von `absdd-image-sandbox` und einen
begrenzten Spec-Kit-Arbeitsablauf. Er setzt keine Container- oder KI-Erfahrung
voraus. Beide Sprachfassungen enthalten dieselben 39 Themen, vollständige
Sprecherhinweise und die lokale Preset-Matrix vom 25.10.2026. Deutsch steht
hier zuerst; Englisch ist eine gleichwertige separate Fassung.

**EN:** The workshop explains this sandbox and a bounded Spec Kit workflow.
No container or AI experience is assumed. Both languages cover the same
39 topics, complete speaker notes and the local preset matrix dated
25 October 2026. German comes first here; English is an equivalent separate deck.

| Sprache / Language | Gepflegte Quelle / Maintained source | PowerPoint | Apple Keynote |
|---|---|---|---|
| Deutsch / German | [Workshop-Markdown](workshop-spec-kit.de.md) | [PPTX](exports/workshop-spec-kit.de.pptx) | [KEY](exports/workshop-spec-kit.de.key) |
| Englisch / English | [Workshop Markdown](workshop-spec-kit.en.md) | [PPTX](exports/workshop-spec-kit.en.pptx) | [KEY](exports/workshop-spec-kit.en.key) |

**DE:** Quellenstand und Exportzeitpunkt sind keine technische Freigabe.
Die Beispiele verwenden nur erfundene Daten. Ein Shell-Befehl auf einer
Folie ist kein Auftrag, ihn auszuführen. Projekt- und Installationsrechte,
Agenten-Anmeldung, Providerfreigaben sowie Commit und Push bleiben getrennt.
Der Workshop startet keinen aktiven Sandbox-Intake oder Produktlauf.

**EN:** Source revision and export date grant no technical approval. Examples
use fictional data. Showing a shell command does not authorize execution.
Project/install permissions, agent sign-in, provider approval, commit and push
remain separate. The workshop starts no active sandbox intake or product run.

## Inhalte pflegen / Maintain Content

**DE:** Zwei zusätzliche Projektwerkstätten führen von den Folien in eigene
Praxis-Intake-Serien: [SysInfo DE](werkstatt-sysinfo.de.md),
[SysInfo EN](werkstatt-sysinfo.en.md), [Web DE](werkstatt-web.de.md) und
[Web EN](werkstatt-web.en.md). Diese vier neuen Foliensätze werden zunächst
nur als Markdown gepflegt; der folgende 39-Folien-PPTX-Exporter bleibt auf
den Grundlagenworkshop begrenzt. Der [Werkstättenindex](../lernwerkstaetten/README.md)
erklärt Übernahme, Wahlpfade und persönliche Startentscheidungen.

**EN:** Four additional Markdown decks introduce SysInfo and the two web
architecture choices, each in German and English. They lead into personal
practice intake packages through the workshop index. They are Markdown-only
at this stage; the existing 39-slide exporter below still serves the introductory
workshop only. No additional PowerPoint/Keynote export is claimed.

**DE:** Die beiden Markdown-Dateien sind die Inhaltsquelle. `<!-- slide: W01 -->`
bis `W39` sind stabile Zuordnungen; pro Folie folgt eine Hauptüberschrift.
`::: notes` enthält die Sprecherhinweise. Änderungen an beiden Sprachen
gemeinsam prüfen und die PowerPoint- und Keynote-Dateien danach neu erzeugen. Lange
Erläuterungen bleiben in den Notizen; Kommandos werden nicht typografisch
in andere Zeichen umgewandelt. Es wurde keine fremde Präsentationsvorlage
oder institutionelle Gestaltung übernommen.

**EN:** Markdown is the content source. Stable IDs W01 through W39 pair the
languages; each slide has a main heading and a notes block. Review both
languages together and regenerate PowerPoint and Keynote afterwards. Detailed explanation
stays in notes; command punctuation must not be replaced typographically.
No external presentation template or institutional design was reused.

**DE:** Der Host-Exporter `scripts/export-workshop-presentations.mjs` liest
Markdown über Pandoc und erstellt native, bearbeitbare PowerPoint-Objekte.
Er benötigt ein vorhandenes Node.js-/`@oai/artifact-tool`-Authoring-Umfeld
sowie Arial und Courier New. Er installiert keine Pakete und greift nicht
auf Podman zu. Diese Authoring-Abhängigkeit wird nicht ins Container-Image
aufgenommen und ist keine Voraussetzung zum Lesen der Materialien.

**EN:** The host exporter reads Markdown through Pandoc and creates native,
editable PowerPoint objects. It needs an existing Node.js/artifact-tool
authoring environment plus Arial and Courier New. It installs no packages
and calls no Podman. This authoring dependency is not added to the image or
required to read the materials.

Host, Bash; vorhandene Authoring-Pfade einsetzen / supply existing authoring paths:

```bash
ARTIFACT_TOOL_MODULES=/path/to/node_modules \
  node scripts/export-workshop-presentations.mjs \
  --out /path/to/new-export-directory \
  --render-dir /path/to/private-previews
```

Host, PowerShell 7, Alternative / alternative:

```powershell
$env:ARTIFACT_TOOL_MODULES = '/path/to/node_modules'
node scripts/export-workshop-presentations.mjs `
  --out /path/to/new-export-directory `
  --render-dir /path/to/private-previews
```

**DE:** Erwartet werden zwei PPTX-Dateien und bei gewählter Render-Option
39 PNG-Vorschauen pro Sprache. Der Exporter überschreibt vorhandene PPTX
nicht. Bei fehlendem Pandoc, Paket oder Font stoppen; keine globale
Installation improvisieren. Vorschauen, temporäre Quelldownloads und
Validierungsdateien gehören nicht zu den auszuliefernden Materialien.
Vor Austausch der Dateien unter `exports/` Paketstruktur, Notizen,
Folieninhalt und Darstellung prüfen.

**EN:** Expect two PPTX files and, when rendering is requested, 39 PNG previews
per language. Existing PPTX files are not overwritten. Stop on missing Pandoc,
package or font; do not improvise global installation. Previews, temporary
source downloads and validation files are not deliverables. Check package
structure, notes, content and rendering before replacing exports.

## Keynote / Keynote

**DE:** Auf dem Authoring-Mac ist **Keynote Creator Studio 15.4** installiert.
Die Anwendung verwendet die Bundle-ID `com.apple.Keynote`; eine Suche nur
nach `Keynote.app` oder der älteren iWork-Bundle-ID reicht nicht aus.
Die frühere Aussage, Keynote sei nicht installiert, war falsch.
Beide `.key`-Dateien wurden durch tatsächlichen PPTX-Import und natives
Sichern in Keynote erstellt, nicht durch Umbenennen der Dateiendung.
Die Lieferung umfasst Markdown, PowerPoint und Apple Keynote.

**EN:** The authoring Mac has **Keynote Creator Studio 15.4**, bundle ID
`com.apple.Keynote`. Checking only the classic app name or old iWork ID
misses this installation. The earlier absence claim was incorrect. Both
`.key` files were imported and saved by Keynote, not renamed from PPTX.
Markdown, PowerPoint and native Apple Keynote are supplied.

**DE:** Nach Inhaltsänderungen zuerst PPTX neu erzeugen, dann die gewünschte
Datei in Keynote öffnen und als neue `.key`-Datei sichern. Beim aktuellen
Import fehlte die in den PPTX-Themen hinterlegte Schrift Aptos; nur diese
Schrift wurde in den Keynote-Kopien durch Arial ersetzt. Die verwendeten
Arial- und Courier-New-Texte sowie die Original-PPTX bleiben unverändert.
Keine Schriftinstallation ist nötig. Folienzahl, alle Folientexte und
Sprecherhinweise über einen separaten PowerPoint-Prüfexport vergleichen;
die Original-PPTX dabei nicht überschreiben. Rendering zusätzlich in
Keynote prüfen. [Apple-Anleitung zum PowerPoint-Import](https://support.apple.com/en-sg/guide/keynote/tan72232b56/mac).

**EN:** After content changes regenerate PPTX, import it into Keynote and
save a new `.key` file. This import lacked the PPTX theme font Aptos; only
that font was replaced with Arial in the Keynote copies. Existing Arial and
Courier New text and original PPTX remain unchanged; no font installation
is needed. Compare slide count, all text and notes through a separate
PowerPoint validation export without overwriting the original. Also inspect
native rendering. The Apple guide above describes PowerPoint import.

## Prüfbasis und offene Grenzen / Review Baseline and Open Boundaries

**DE:** Klare Überschriften, bearbeitbarer Text, geordnete Objekte,
kontrastreiche Farben und vollständige Notizen unterstützen die Nutzung.
Sie sind keine vollständige WCAG-2.2-AA- oder Präsentations-A11Y-Abnahme.
Keynote-Import, natives Speichern und Rendering-Stichproben sind lokal geprüft;
das ist keine vollständige Bedienungs- oder A11Y-Abnahme.
PowerPoint-Anwendungsprüfung, umfassende Keynote-Bedienprüfung, Screenreader, Tastaturbedienung und
Erstnutzung mit Lernenden bleiben **Open**, Owner: Learning/A11Y Review;
Follow-up: beide Sprachfassungen mit echten Nutzenden prüfen;
Trigger: vor Konformitätsbehauptung oder unbegleitetem Rollout.

**EN:** Headings, editable text, ordered objects, contrast and complete notes
support use but do not prove full WCAG or presentation accessibility.
Keynote import, native saving and rendering spot checks were performed locally,
not a full usability or accessibility assessment. Native PowerPoint, full
Keynote usability, screen-reader, keyboard and learner first-use
acceptance remain **Open**; owner: Learning/A11Y Review; follow up with real
users before conformance claims or unattended rollout.

**DE:** Für die Praxis zuerst [Installation](../fuer-lernende/installation.md)
und [sicheren Alltag](../fuer-lernende/alltag.md) lesen. Die
[Werkzeug-Nachprüfungen](../security/toolchain-followups-2026-10-25.md) bleiben
maßgeblich für offene OpenCode-2-, Plattform- und Freigabegrenzen.

**EN:** Before practice, read installation and safe daily workflow. The
follow-up register remains authoritative for open OpenCode 2, platform and
approval boundaries.
