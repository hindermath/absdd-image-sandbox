# Barrierefreiheit der Container-Haertung / Container Hardening Accessibility

## Zweck und Zielgruppen / Purpose and Audiences

**DE:** Diese artefaktbezogene Pruefung wendet WCAG 2.2 Level AA an, soweit
die Kriterien auf Markdown, JSON, Manpages und Kommandozeilenausgaben passen.
Sie gilt ab dem ersten Ausbildungsjahr fuer Fachinformatiker*innen,
IT-System-Elektroniker*innen, Kaufleute fuer IT-System-Management und
Kaufleute fuer Digitalisierungsmanagement. Spec-Kit-Erfahrung wird nicht
vorausgesetzt. Ein **Gate** ist eine pruefbare Bedingung fuer den naechsten
Schritt; **Open** bedeutet, dass der benoetigte Nachweis noch fehlt.

**EN:** This artefact review applies WCAG 2.2 Level AA where its criteria fit
Markdown, JSON, man pages, and command-line output. It covers first-year
learners in all four binding training occupations and assumes no Spec Kit
experience. A gate is a checkable condition for the next step; Open means
that required evidence is still missing.

## Pruefmatrix / Review Matrix

| Bereich / Area | Beobachtete Umsetzung / Observed implementation | Status |
|---|---|---|
| Wahrnehmbar / Perceivable | Status besitzt immer Text wie `Pass`, `Blocked`, `Open` oder `N/A`; Farbe, Symbol, Tabellenposition und Diagramm sind nie die einzige Information. / Status always has text; color, symbols, position, and diagrams are never the only source. | Erfuellt im Artefakt / Met in artefact |
| Struktur / Structure | Eine lineare Ueberschriftenfolge, kurze Abschnitte, Listen und Tabellen mit benannten Spalten bilden Reader Paths ab. / Linear headings, short sections, lists, and named table columns form the reader paths. | Erfuellt im Artefakt / Met in artefact |
| Textalternativen / Text alternatives | Abhaengigkeiten, Plattformstatus, Counts und naechste Aktionen stehen vollstaendig als Text. Es gibt keine nur visuelle Entscheidung. / Dependencies, platform status, counts, and next actions are complete in text. | Erfuellt im Artefakt / Met in artefact |
| Bedienbar / Operable | Alle dokumentierten CLI-Ablaufe sind tastaturbedienbar. Keine Maus, kein Dragging und keine Zeigerzielgroesse sind fuer diese Artefakte erforderlich. / Documented CLI flows are keyboard operable; mouse, dragging, and pointer target size do not apply. | Erfuellt oder begruendet N/A / Met or reasoned N/A |
| Zeit / Timing | Die Oberflaechen besitzen kein automatisches Zeitlimit. Die 30-Minuten-Grenze aus SC-009 ist eine menschliche Testmessung, keine erzwungene Session-Zeit. / Interfaces impose no time limit; the SC-009 limit is a human test measurement. | Erfuellt / Met |
| Verstaendlich / Understandable | Deutsch steht zuerst, Englisch danach, ungefaehr CEFR B2. Gate, Open, SBOM, Scan, VEX und Spec Kit werden beim ersten relevanten Gebrauch erklaert oder zum Glossar verlinkt. / German comes first, English second, approximately CEFR B2; terms are explained or linked. | Erfuellt im Reader Path / Met in reader path |
| Fehler und Status / Errors and status | Befehl, Exitcode, Plattform, Grenze und sichere naechste Aktion bleiben kopierbarer Text. Echte Secret- oder Scanner-Treffer werden nicht unredigiert uebernommen. / Command, exit code, platform, limit, and safe next action remain copyable text; sensitive matches are not copied. | Erfuellt / Met |
| Robustheit / Robustness | Dateien sind UTF-8, nutzen Standard-Markdown und validierte JSON-Vertraege. Die Offline-Pruefung fand bei 573 eindeutigen lokalen Links null Fehler. / Files use UTF-8, standard Markdown, validated JSON, and the offline check found zero errors across 573 unique local links. | Erfuellt / Met |

## Gepruefte textorientierte Wahrheit / Reviewed Text-First Truth

**DE:** Die Dokumentation nennt das unveraenderte Image, den belegten
macOS-rootless-Podman-Lauf, sechs Sprachfamilien, zwei Skriptgrundlagen, sechs
Agentenoberflaechen, getrennten Agentenstate, Loopback-Ports `5100-5199`, den
Audit-Stopp sowie genau eine SBOM-/Grype-Kette. Sie nennt ebenso deutlich die
offenen Linux-, Windows/WSL2- und VS-Code-Nachweise sowie 14 Critical- und 360
High-Matches. Kein Text setzt diese Grenzen auf `Pass`, `N/A`, `not affected`
oder akzeptiertes Risiko.

**EN:** Documentation names the unchanged image, evidenced macOS rootless
Podman run, six language families, two scripting foundations, six agent
surfaces, separate agent state, loopback ports, audit stop, and one SBOM/Grype
chain. It also states the open Linux, Windows/WSL2, VS Code, 14 Critical, and
360 High items. No text turns these limits into Pass, N/A, not affected, or
accepted risk.

## Menschlicher Erstnutzungstest / Human First-Use Test

**DE:** `GATE-LEARNER-01` bleibt `Blocked`. Owner ist `Learning/A11Y Review`.
Die Datei `learner-first-use-results.json` wurde nicht erzeugt, weil keine
echte moderierte Beobachtung fuer alle vier Berufe ohne Spec-Kit-Vorerfahrung
vorliegt. Der spaetere Test misst sicheren Start, sichtbaren
Verifikationsstatus und den naechsten Human-only-Schritt innerhalb von 30
Minuten mit mindestens 90 Prozent Erfolg. Er speichert nur aggregierte,
nicht-sensible Ergebnisse.

**EN:** GATE-LEARNER-01 remains Blocked and is owned by Learning/A11Y Review.
No learner result file was created because no real moderated observation
exists for all four occupations without prior Spec Kit experience. A later
test measures safe startup, visible verification status, and the next
Human-only step within 30 minutes at a success rate of at least 90 percent,
using aggregated non-sensitive results only.

**Exakter Neubewertungsausloeser / Exact re-evaluation trigger:** Any startup
path, verification-status presentation, Human-only handoff, audience policy,
test protocol, participant coverage, or learner-facing documentation change.

## Grenzen / Limits

**DE:** Diese Dateipruefung ersetzt weder einen Screenreader-/Braille-Test mit
Menschen noch den moderierten SC-009-Test. Echte Linux-, Windows/WSL2- und
VS-Code-Nachweise bleiben getrennte offene Plattformaufgaben.

**EN:** This file review does not replace a human screen-reader or Braille
test or the moderated SC-009 test. Real Linux, Windows/WSL2, and VS Code
evidence remain separate open platform tasks.

Der Homogenitaets-Dry-run erreichte 28/29 Pruefungen. Nur Statistikprofil 2
wich nach den neuen Content-Aenderungen erwartbar ab; laut Plan wird es erst
nach dem Inhaltscommit durch den Orchestrator gerendert. / The homogeneity
dry-run passed 28/29 checks. Only Statistics Profile 2 drifted after content
changes; the plan assigns rendering to the orchestrator after the content
commit.
