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

**DE:** Die Dokumentation nennt die getrennt belegten macOS-, Windows-Host-
und Ubuntu/WSL2-Pfade, sechs Sprachfamilien, zwei Skriptgrundlagen, sechs
Agentenoberflaechen, getrennten Agentenstate, Loopback-Ports `5100-5199`, den
Audit-Stopp sowie die kanonische SBOM-/Grype-Kette. Sie nennt ebenso deutlich
390 weiterhin `Open`/`in_triage` gefuehrte Advisories. Die lokale macOS-
Podman-Machine ist rootful; nur Ubuntu/WSL2 liefert den kanonischen rootless
Nachweis. Kein Text erklaert offene Advisories zu `not affected` oder das
lokale Image fuer produktiv beziehungsweise distributionsbereit.

**EN:** Documentation identifies the separately evidenced macOS, Windows-host,
and Ubuntu/WSL2 paths, six language families, two scripting foundations, six
agent surfaces, separate agent state, loopback ports, audit stop, and the
canonical SBOM/Grype chain. It also clearly retains 390 Open/in_triage
advisories. The macOS Podman machine is rootful; only Ubuntu/WSL2 provides the
canonical rootless evidence. No text turns open advisories into not-affected
claims or approves the local image for production or distribution.

## Menschlicher Erstnutzungstest / Human First-Use Test

**DE:** Der Repository Owner hat am 06.09.2026 festgelegt, dass in der allein
durchgefuehrten Machbarkeitsstudie keine reale moderierte Beobachtung und keine
unabhaengige Learning-/A11Y-Review stattfinden werden. Deshalb existiert kein
`learner-first-use-results.json`; `feasibility-study-decision.json` erfasst
stattdessen `NotPerformed`. `GATE-LEARNER-01` ist nur fuer diesen bis
31.12.2026 befristeten, source-only Studienabschluss `N/A`. Vor
Lernenden-Rollout, Image-Verteilung, produktiver Nutzung oder bei Ablauf wird
der reale Test wieder verpflichtend.

**EN:** The Repository Owner decided on 2026-09-06 that this single-person
feasibility study will not perform moderated learner observation or
independent Learning/A11Y review. No learner result exists; the feasibility
decision records NotPerformed. GATE-LEARNER-01 is N/A only for this
source-only study through 2026-12-31 and becomes mandatory again before
learner rollout, image distribution, production use, or expiry.

**Exakter Neubewertungsausloeser / Exact re-evaluation trigger:** Before
learner rollout, prebuilt image distribution, production use, or at or after
2026-12-31.

## Grenzen / Limits

**DE:** Diese Dateipruefung ersetzt weder einen Screenreader-/Braille-Test mit
Menschen noch den moderierten SC-009-Test. Sie belegt ausschliesslich die
artefaktbezogene A11Y-Pruefung dieser Machbarkeitsstudie. Alle drei
Plattformpfade sind getrennt aktuell belegt; native Linux-Hardware ist kein
Akzeptanzziel fuer Feature 003.

**EN:** This file review does not replace a human screen-reader or Braille
test or the moderated SC-009 test. It proves only the artefact-level A11Y
review for this feasibility study. All three platform paths have separate
current evidence; native Linux hardware is not a Feature 003 target.

Der Homogenitaets-Dry-run erreichte 28/29 Pruefungen. Nur Statistikprofil 2
wich nach den neuen Content-Aenderungen erwartbar ab; laut Plan wird es erst
nach dem Inhaltscommit durch den Orchestrator gerendert. / The homogeneity
dry-run passed 28/29 checks. Only Statistics Profile 2 drifted after content
changes; the plan assigns rendering to the orchestrator after the content
commit.
