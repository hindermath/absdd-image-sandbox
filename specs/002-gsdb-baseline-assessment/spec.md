# Feature-Spezifikation: GSDB-Bestandspruefung / Feature Specification: GSDB Baseline Assessment

**Feature-Verzeichnis / Feature Directory**: `specs/002-gsdb-baseline-assessment`
**Erstellt / Created**: 2026-08-30
**Spezifikationsstatus / Specification Status**: Clarified
**Eingabe / Input**: `Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md`, der
akzeptierte aktuelle Serien-Review und der aktive autonome Laufzustand

## Zweck und Begriffe / Purpose and Terms

**DE:** Dieses Feature beschreibt eine reine Bestandspruefung der
`absdd-image-sandbox` gegen die Generische Secure-Development-Basis (GSDB).
Die GSDB ist die organisationsneutrale Ausbildungs- und Pruefgrundlage unter
`docs/secure-development/`. Die Pruefung erzeugt spaeter eine Evidenzmatrix,
also eine Tabelle, die jeden Pruefpunkt mit Status, Begruendung und Nachweis
verknuepft, sowie eine priorisierte Lueckenliste. Sie aendert keine technische
Konfiguration und behebt keine Luecke.

**EN:** This feature defines an assessment-only review of the
`absdd-image-sandbox` against the Generic Secure Development Baseline (GSDB).
The GSDB is the organisation-neutral training and review basis under
`docs/secure-development/`. The later assessment produces an evidence matrix,
which links every review item to a status, rationale, and evidence, plus a
prioritised gap list. It changes no technical configuration and remediates no
gap.

**DE:** Spec Kit ist ein Ablauf fuer spezifikationsgetriebene Entwicklung. In
dieser Phase wird nur festgelegt, was die Bestandspruefung liefern und wie sie
abgenommen werden muss. Planung, Aufgaben, Haertung und der naechste
Serien-Intake folgen nicht automatisch.

**EN:** Spec Kit is a workflow for specification-driven development. This
phase only defines what the baseline assessment must deliver and how it will be
accepted. Planning, tasks, hardening, and the next series intake do not start
automatically.

### Akzeptierte Eingangsbindung / Accepted Input Binding

**DE:** Die folgenden drei Artefakte sind die unveraenderliche Eingangsbindung
dieses Features. Ein abweichender Pfad oder SHA-256-Hash stoppt die Bewertung
bis zur ausdruecklichen Revalidierung des autonomen Laufs. Der Serien-Review
und das Serienmanifest begrenzen die Arbeit auf den einzigen als `Eligible`
markierten Serienkopf; nachfolgende Intakes bleiben `Blocked`.

**EN:** The following three artefacts are the immutable input binding for this
feature. A different path or SHA-256 hash stops the assessment until the
autonomous run is explicitly revalidated. The series review and manifest limit
the work to the only series root marked `Eligible`; subsequent intakes remain
`Blocked`.

| Rolle / Role | Pfad / Path | SHA-256 |
|---|---|---|
| Serienkopf / Series root | `Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md` | `9b1963a5cc1e4f074e8fc918455f0285a0e1138334451523bd957ff21e72026a` |
| Akzeptierter Serien-Review / Accepted series review | `specs/intake-review-results/sandbox-development-lifecycle.json` | `0d08a1e90e25965c4b529d66be6996394b963abef4ddb3c3b75dd678f464004b` |
| Serienmanifest / Series manifest | `specs/intake-series/sandbox-development-lifecycle/manifest.json` | `faa906c5acb7678265de75e28d80a337459d754ab53066f7a4f065ef24d1b3b2` |

### Abkuerzungen und Fachbegriffe / Abbreviations and Technical Terms

| Begriff / Term | Erklaerung / Explanation |
|---|---|
| MSL | Memory Safe Language, eine speichersichere Programmiersprache, die typische Speicherfehler technisch verhindert oder stark begrenzt. / A memory-safe programming language that prevents or strongly limits common memory errors. |
| A11Y und WCAG | A11Y bedeutet Barrierefreiheit; WCAG 2.2 AA ist die hier verwendete Pruefbasis fuer barrierefreie Inhalte. / A11Y means accessibility; WCAG 2.2 AA is the accessibility review baseline used here. |
| SBOM und AI-SBOM | Eine Software Bill of Materials ist eine Komponentenliste fuer Software; eine AI-SBOM ergaenzt Angaben zu KI-Modellen, Daten und Inferenzbestandteilen. / A Software Bill of Materials lists software components; an AI-SBOM adds AI models, data, and inference components. |
| VEX und CVE | Vulnerability Exploitability eXchange beschreibt, ob eine bekannte Schwachstelle eine Komponente betrifft; eine CVE ist die eindeutige Kennung einer veroeffentlichten Schwachstelle. / VEX describes whether a known vulnerability affects a component; a CVE is the unique identifier of a published vulnerability. |
| SLSA | Supply-chain Levels for Software Artifacts ist ein Modell fuer nachvollziehbare und geschuetzte Build-Herkunft. / A model for traceable and protected software build provenance. |
| STRIDE, CAPEC und Zero Trust | STRIDE ordnet Bedrohungsarten, CAPEC dokumentiert Angriffsmuster, und Zero Trust verlangt eine fortlaufende Pruefung statt pauschalen Vertrauens. / STRIDE classifies threat types, CAPEC documents attack patterns, and Zero Trust requires continuous verification instead of broad trust. |
| OWASP ASVS und SAMM | ASVS ist ein Pruefstandard fuer Anwendungssicherheit; SAMM ist ein Reifegradmodell fuer sichere Softwareentwicklung. / ASVS is an application-security verification standard; SAMM is a secure-development maturity model. |
| CRA, NIS2, DORA und EU AI Act | Europaeische Regelwerke fuer Cyberresilienz, Netz- und Informationssicherheit, digitale Resilienz im Finanzbereich und kuenstliche Intelligenz. / European rules for cyber resilience, network and information security, financial-sector digital resilience, and artificial intelligence. |
| CVD und `security.txt` | Coordinated Vulnerability Disclosure ist ein abgestimmter Prozess fuer Schwachstellenmeldungen; `security.txt` nennt den Meldeweg. / CVD is a coordinated process for vulnerability reports; `security.txt` states the reporting route. |
| ADR, S-ADR und arc42 | Ein Architecture Decision Record dokumentiert eine Architekturentscheidung; ein S-ADR ist die Sicherheitsvariante; arc42 ist eine Struktur fuer Architekturdokumentation. / An ADR records an architecture decision; an S-ADR is its security form; arc42 structures architecture documentation. |
| SoA und RoPA | Statement of Applicability ist eine Anwendbarkeitserklaerung fuer Kontrollen; Record of Processing Activities ist das Verzeichnis von Verarbeitungstaetigkeiten. / A SoA records control applicability; a RoPA records processing activities. |
| BSI C3A und BSI C5 | Pruefansaetze des Bundesamts fuer Sicherheit in der Informationstechnik fuer Cloud-Autonomie und Cloud-Sicherheitsnachweise. / German Federal Office for Information Security review approaches for cloud autonomy and cloud-security assurance. |
| CLI, API, HTTP und TLS | CLI ist eine Kommandozeilenoberflaeche, API eine Programmierschnittstelle, HTTP ein Web-Uebertragungsprotokoll und TLS dessen uebliche Transportverschluesselung. / CLI is a command-line interface, API a programming interface, HTTP a web transfer protocol, and TLS its common transport encryption. |
| CI/CD | Continuous Integration und Continuous Delivery bezeichnen automatisierte Bau-, Test- und Lieferablaeufe. / Automated build, test, and delivery workflows. |

## Benutzerszenarien und Tests / User Scenarios and Testing

### User Story 1 - Vollstaendige GSDB-Abdeckung / Complete GSDB Coverage (Priority: P1)

**DE:** Eine pruefende Person kann alle zwoelf GSDB-Checklisten und jeden ihrer
157 stabilen Pruefpunkte in einer einzigen Evidenzmatrix finden. Kein
Pruefpunkt fehlt stillschweigend und keiner wird doppelt bewertet.

**EN:** A reviewer can find all twelve GSDB checklists and each of their 157
stable review items in one evidence matrix. No item is silently omitted or
assessed twice.

**Prioritaetsgrund / Why this priority**: Die vollstaendige Abdeckung ist die
Grundlage fuer jede belastbare Aussage ueber den Ist-Zustand. / Complete
coverage is the basis for every reliable statement about the current state.

**Unabhaengiger Test / Independent Test**: Die 157 IDs aus
`docs/secure-development/baseline-manifest.json` und den kanonischen
Checklisten werden mit den Matrixzeilen verglichen. Erwartet werden genau 157
eindeutige Treffer und eine sichtbare Behandlung aller zwoelf Checklisten. / The
157 IDs from the baseline manifest and canonical checklists are compared with
the matrix rows. Exactly 157 unique matches and visible coverage of all twelve
checklists are expected.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Given** die aktuelle GSDB und das akzeptierte Intake, **When** die
   Evidenzmatrix geprueft wird, **Then** enthaelt sie jede stabile ID von
   `CL-01-01` bis zum jeweils letzten Punkt aller zwoelf Checklisten genau
   einmal. / **Given** the current GSDB and accepted intake, **When** the
   evidence matrix is reviewed, **Then** it contains every stable ID across all
   twelve checklists exactly once.
2. **Given** ein Pruefpunkt ist fuer die Sandbox nicht anwendbar, **When** die
   Zeile bewertet wird, **Then** bleibt sie vorhanden und traegt `N/A` mit
   Begruendung und Neubewertungs-Trigger. / **Given** an item does not apply to
   the sandbox, **When** its row is assessed, **Then** it remains present and
   carries `N/A` with a rationale and re-evaluation trigger.
3. **Given** Evidenz ist veraltet, widerspruechlich oder nicht reproduzierbar,
   **When** ein positiver Status erwogen wird, **Then** wird der Punkt als
   `Open` oder `FollowUp` behandelt und nicht als `AlreadySatisfied`. / **Given**
   evidence is stale, contradictory, or not reproducible, **When** a positive
   status is considered, **Then** the item is treated as `Open` or `FollowUp`,
   not `AlreadySatisfied`.

---

### User Story 2 - Nachvollziehbare Evidenz und Grenzen / Traceable Evidence and Boundaries (Priority: P1)

**DE:** Lernende, Maintainer und Security-Review koennen fuer jede Bewertung
verstehen, was geprueft wurde, welche lokale Evidenz die Aussage stuetzt und
wo eine Entscheidung ausdruecklich bei einem Menschen verbleibt.

**EN:** Learners, maintainers, and security reviewers can understand what was
checked for every assessment, which local evidence supports it, and where a
decision explicitly remains with a human.

**Prioritaetsgrund / Why this priority**: Ein Status ohne pruefbaren Nachweis
oder klare Authority-Grenze kann eine falsche Freigabe vortaeuschen. / A status
without verifiable evidence or a clear authority boundary can imply a false
approval.

**Unabhaengiger Test / Independent Test**: Eine Stichprobe aus jeder der
zwoelf Checklisten wird vom Status ueber Begruendung und Pruefmethode bis zum
Repository-Pfad verfolgt. Human-only-Zeilen werden gegen die festgelegte
Grenzenliste geprueft. / A sample from each checklist is traced from status
through rationale and verification method to the repository path. Human-only
rows are checked against the defined boundary list.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Given** eine Zeile ist `AlreadySatisfied`, **When** die Evidenz geoeffnet
   und die genannte Pruefung wiederholt wird, **Then** stuetzen beide den Status
   ohne externe, nicht belegte Annahme. / **Given** a row is
   `AlreadySatisfied`, **When** its evidence is opened and its stated check is
   repeated, **Then** both support the status without an unproven external
   assumption.
2. **Given** ein Punkt verlangt formale Freigabe, Rechtsentscheidung,
   Secret-Rotation, Plattformregel oder externen Registereintrag, **When** die
   Matrix erstellt wird, **Then** bleibt der Punkt sichtbar offen und nennt die
   menschliche Rolle sowie den Stop-Grund. / **Given** an item requires formal
   approval, a legal decision, secret rotation, a platform rule, or an external
   register entry, **When** the matrix is produced, **Then** the item remains
   visibly open and names the human role and stop reason.
3. **Given** nur ein externer Link oder eine Behauptung ohne lokalen Nachweis
   ist vorhanden, **When** der Punkt bewertet wird, **Then** genuegt dies nicht
   fuer `AlreadySatisfied`. / **Given** only an external link or an unsupported
   statement exists, **When** the item is assessed, **Then** it is insufficient
   for `AlreadySatisfied`.

---

### User Story 3 - Priorisierte Lueckenliste / Prioritised Gap List (Priority: P2)

**DE:** Die Projektverantwortung erhaelt aus der Matrix eine vollstaendige,
priorisierte Lueckenliste. Sie kann erkennen, welche Punkte spaeter zuerst
bearbeitet werden muessen, ohne dass diese Bestandspruefung bereits Haertung
umsetzt.

**EN:** The project owner receives a complete, prioritised gap list derived
from the matrix. It shows which items need later attention first without this
assessment implementing hardening.

**Prioritaetsgrund / Why this priority**: Die Lueckenliste ist die kontrollierte
Uebergabe an den spaeteren Hardening-Intake. / The gap list is the controlled
handoff to the later hardening intake.

**Unabhaengiger Test / Independent Test**: Jede Matrixzeile, die nicht
`AlreadySatisfied` oder begruendet `N/A` ist, wird auf genau einen
Lueckeneintrag oder eine dokumentierte Gruppenzuordnung zurueckverfolgt. / Each
matrix row that is neither `AlreadySatisfied` nor a justified `N/A` is traced
to exactly one gap entry or a documented grouped entry.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Given** eine bestaetigte oder ungeklärte Luecke, **When** die Liste
   geprueft wird, **Then** nennt sie Prioritaet, betroffene CL-IDs, Owner,
   Folgeaktion, Abnahmeevidenz, Restrisiko und Neubewertungs-Trigger. / **Given**
   a confirmed or unresolved gap, **When** the list is reviewed, **Then** it
   names priority, affected CL IDs, owner, follow-up action, acceptance
   evidence, residual risk, and re-evaluation trigger.
2. **Given** mehrere CL-IDs haben dieselbe Ursache, **When** sie gruppiert
   werden, **Then** bleiben alle IDs einzeln rueckverfolgbar und die Gruppierung
   ist begruendet. / **Given** several CL IDs share one root cause, **When**
   they are grouped, **Then** every ID remains individually traceable and the
   grouping is justified.
3. **Given** die Lueckenliste ist fertig, **When** die Bestandspruefung endet,
   **Then** wird der Hardening-Intake nur als naechster moeglicher Schritt
   genannt und nicht gestartet. / **Given** the gap list is complete, **When**
   the assessment ends, **Then** the hardening intake is named only as a
   possible next step and is not started.

---

### User Story 4 - Installationsangaben abgleichen / Reconcile Installation Claims (Priority: P2)

**DE:** Eine pruefende Person kann die tatsaechlich vorgesehenen Agenten,
Sprach- und Werkzeugpfade sowie Spec-Kit-Presets gegen Build-, Laufzeit-,
Smoke-Test- und Dokumentationsquellen abgleichen. Abweichende Zahlen oder
Kategorien werden als Befund sichtbar.

**EN:** A reviewer can reconcile the intended agents, language and supporting
tool paths, and Spec Kit presets against build, runtime, smoke-test, and
documentation sources. Conflicting counts or categories become visible
findings.

**Prioritaetsgrund / Why this priority**: Falsche Inventarangaben schwaechen
Tool-Pinning, Testabdeckung und Lieferkettennachweise. / Incorrect inventory
claims weaken tool pinning, test coverage, and supply-chain evidence.

**Unabhaengiger Test / Independent Test**: Die dokumentierte Inventartabelle
wird gegen `Dockerfile`, `compose.yml`, `scripts/smoke-test-toolchains.sh`, die
Agent-Prompt-Dispatcher, die Werkzeugregister und die Bedienungsdokumentation
verglichen. / The documented inventory table is compared with `Dockerfile`,
`compose.yml`, `scripts/smoke-test-toolchains.sh`, the agent prompt
dispatchers, tool registries, and operating documentation.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Given** die dokumentierte Soll-Kategorisierung, **When** die sechs
   verbindlichen MSL-Pfade geprueft werden, **Then** werden .NET/C#, Java/JVM,
   Go, Rust, Python und Swift einzeln nach Build-Quelle, Versionsnachweis und
   praktischem Smoke-Test bewertet. / **Given** the documented target
   categorisation, **When** the six required memory-safe-language paths are
   reviewed, **Then** .NET/C#, Java/JVM, Go, Rust, Python, and Swift are each
   assessed by build source, version evidence, and practical smoke test.
2. **Given** PowerShell 7 und Node.js/npm sind installiert, **When** die Zahl
   der MSL-Pfade bestimmt wird, **Then** werden sie als zweite Skriptbasis
   beziehungsweise unterstuetzendes Werkzeug ausgewiesen und nicht als zwei
   weitere verbindliche MSL-Familien gezaehlt. / **Given** PowerShell 7 and
   Node.js/npm are installed, **When** the MSL path count is determined,
   **Then** they are identified as a second scripting foundation and supporting
   tooling, not counted as two additional required MSL families.
3. **Given** Agentenquellen unterscheiden zwischen Required- und
   Zusatzwerkzeugen, **When** die Installation geprueft wird, **Then** werden
   Codex, Claude Code, Antigravity CLI und GitHub Copilot CLI als vier
   Required-Agenten sowie OpenCode und Gemini CLI als zusaetzliche Oberflaechen
   getrennt ausgewiesen. / **Given** agent sources distinguish required and
   additional tools, **When** installation is assessed, **Then** Codex, Claude
   Code, Antigravity CLI, and GitHub Copilot CLI are listed as the four required
   agents, while OpenCode and Gemini CLI are listed separately as additional
   surfaces.
4. **Given** die installierte Preset-Liste ist groesser als das verbindliche
   GSDB-Achterprofil, **When** die Presets abgeglichen werden, **Then** werden
   die acht Baseline-Presets und die vier zusaetzlichen Intake-/Routing-Presets
   mit Version, Prioritaet, Aufloesungsstatus und CL-Abdeckung getrennt
   dokumentiert. / **Given** the installed preset list is larger than the
   binding GSDB eight-preset profile, **When** presets are reconciled, **Then**
   the eight baseline presets and four additional intake/routing presets are
   documented separately with version, priority, resolution status, and CL
   coverage.

### Grenz- und Fehlerfaelle / Edge Cases

- **DE:** Manifest, Richtlinie, Einzelcheckliste und generierter Sammelband
  nennen unterschiedliche Versionen oder Anzahlen. Der Widerspruch wird als
  `Open` erfasst; keine Quelle wird stillschweigend bevorzugt.
  **EN:** The manifest, guideline, individual checklist, and generated
  compendium state different versions or counts. The conflict is recorded as
  `Open`; no source is silently preferred.
- **DE:** Eine stabile CL-ID fehlt, ist doppelt oder wurde umbenannt. Die
  Vollstaendigkeitspruefung schlaegt fehl und nennt jede betroffene ID.
  **EN:** A stable CL ID is missing, duplicated, or renamed. The completeness
  check fails and names every affected ID.
- **DE:** Ein Nachweispfad existiert, belegt aber einen alten Stand oder eine
  andere Plattform. Die Zeile nennt Alter und Plattformgrenze und bleibt ohne
  aktuellen Gegenbeleg offen.
  **EN:** An evidence path exists but proves an old state or another platform.
  The row names the age and platform limitation and remains open without
  current counter-evidence.
- **DE:** Ein Werkzeug ist im `Dockerfile` installiert, fehlt aber im
  Smoke-Test oder in der Dokumentation. Installation, Pruefabdeckung und
  Dokumentationsparitaet werden getrennt bewertet.
  **EN:** A tool is installed in the `Dockerfile` but absent from the smoke
  test or documentation. Installation, test coverage, and documentation parity
  are assessed separately.
- **DE:** Ein Befehl kann wegen fehlendem Podman, Netzwerk oder externer
  Plattform nicht ausgefuehrt werden. Der fehlende Lauf wird mit Grund und
  Wiederholungsbedingung als `Open` erfasst; er wird nicht als negativer oder
  positiver Nachweis erfunden.
  **EN:** A command cannot run because Podman, network access, or an external
  platform is unavailable. The missing run is recorded as `Open` with its
  reason and retry condition; neither positive nor negative evidence is
  invented.
- **DE:** Eine Datei behauptet eine formale Freigabe, enthaelt aber keine
  pruefbare menschliche Entscheidung. Die formale Freigabe bleibt Human-only
  und offen.
  **EN:** A file claims formal approval but contains no verifiable human
  decision. Formal approval remains human-only and open.
- **DE:** Ein Nachweis unterstuetzt mehrere CL-IDs. Er darf wiederverwendet
  werden, aber jede Matrixzeile braucht eine eigene Begruendung.
  **EN:** One item of evidence supports several CL IDs. It may be reused, but
  each matrix row needs its own rationale.
- **DE:** Ein Punkt ist fachlich nicht anwendbar, waehrend ein verwandter
  Prozess trotzdem fehlt. `N/A` darf nur den konkreten CL-Punkt abdecken; der
  verwandte Befund bleibt separat sichtbar.
  **EN:** An item does not apply, while a related process is still missing.
  `N/A` may cover only the specific CL item; the related finding remains
  separately visible.

## Anforderungen / Requirements

### Funktionale Anforderungen / Functional Requirements

- **FR-001**: Die Bestandspruefung MUSS ausschliesslich die aktuelle,
  akzeptierte Serienwurzel `Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md`
  bearbeiten und deren akzeptierte Hash-Bindung, den aktuellen Series-Review
  und das Serienmanifest als Eingangsprovenienz nennen. / The assessment MUST
  process only the current accepted series root and record its accepted hash
  binding, current series review, and series manifest as input provenance.
- **FR-002**: Die Bestandspruefung MUSS die GSDB unter
  `docs/secure-development/` als generische, organisationsneutrale Ausbildungs-
  und Pruefgrundlage behandeln und DARF sie NICHT als Firmenrichtlinie oder
  internes Managementsystem darstellen. / The assessment MUST treat the GSDB
  as a generic, organisation-neutral training and review basis and MUST NOT
  describe it as company policy or an internal management system.
- **FR-003**: Die Bestandspruefung MUSS die kanonischen Einzelchecklisten, das
  Baseline-Manifest, die Richtlinie, den generierten Sammelband und alle im
  Manifest genannten mitgeltenden, Lern- und Referenzdokumente erfassen. / The
  assessment MUST cover the canonical individual checklists, baseline
  manifest, guideline, generated compendium, and all related, learning, and
  reference documents named by the manifest.
- **FR-004**: Die Evidenzmatrix MUSS alle 157 stabilen CL-IDs genau einmal
  enthalten und die folgende Checklistenabdeckung sichtbar ausweisen. / The
  evidence matrix MUST contain all 157 stable CL IDs exactly once and visibly
  show the following checklist coverage.

| Checkliste / Checklist | Punkte / Items | Prueffeld / Review Area |
|---|---:|---|
| CL-01 Standards-Anwendbarkeit / Standards Applicability | 12 | Standards, SBOM, VEX, SLSA, Zero Trust, CAPEC, SAMM, Regulierung |
| CL-02 Sichere Softwarearchitektur / Secure Software Architecture | 13 | Vertrauensgrenzen, Architekturprinzipien, S-ADR, arc42, Cloud-Assurance |
| CL-03 Krypto-Mindestvorgaben / Cryptographic Minimum Requirements | 15 | Verfahren, TLS, Zufall, Schluessel, Krypto-Agilitaet |
| CL-04 Bedrohungsmodellierung / Threat Modelling | 10 | Schutzbedarf, Datenfluesse, STRIDE, CAPEC, Risiken, Massnahmen |
| CL-05 Lieferkette und Build-Integritaet / Supply Chain and Build Integrity | 13 | SBOM, VEX, Provenienz, Pinning, CVE, Lizenzen, AI-SBOM |
| CL-06 Schwachstellenoffenlegung / Vulnerability Disclosure | 11 | CVD, `security.txt`, Triage, Fristen, Meldung, Lessons Learned |
| CL-07 CRA-Anwendbarkeit / CRA Applicability | 12 | Produktklasse, Pflichten, Konformitaet, Lebenszyklus, N/A |
| CL-08 Sicherheits-Code-Review / Security Code Review | 13 | Eingabe, Authentisierung, Rechte, Secrets, I/O, Tests, Sprachprofile |
| CL-09 KI-Codeerzeugung / AI Code Generation | 17 | Werkzeuge, Human Review, Datenschutz, Audit, Lieferkette, Regulierung |
| CL-10 Sichere Entwicklungsumgebung / Secure Development Environment | 17 | Host, IDE, Git, CI/CD, Secrets, Audit, Backup, Skriptparitaet |
| CL-11 Datenschutz-Folgenabschaetzung / Data Protection Impact Assessment | 12 | Schwellwert, Risiken fuer Betroffene, Rollen, RoPA, Betroffenenrechte |
| CL-12 Agentische KI-Sandbox / Agentic AI Sandbox | 12 | Freigabe, Mounts, Agentendaten, Werkzeuge, Spec Kit, Isolation, Netzwerk |

- **FR-005**: Jede Matrixzeile MUSS mindestens CL-ID, deutschen und englischen
  Kurztitel, Quellenpfad und Quellversion, Anwendbarkeit, Umsetzungsstatus,
  konsolidierten Bewertungsstatus, Lernstufe, verantwortliche Rolle,
  Begruendung, Evidenzpfad, Pruefmethode, Pruefdatum, Plattformgrenze, Reviewer,
  Restrisiko, naechste Massnahme mit Zieltermin, Neubewertungs-Trigger,
  Human-only-Kennzeichen und zugeordnete Standards oder Presets enthalten. /
  Every matrix row MUST contain at least the CL ID, German and English short
  title, source path and source version, applicability, implementation status,
  consolidated assessment status, learning stage, responsible role, rationale,
  evidence path, verification method, review date, platform limitation,
  reviewer, residual risk, next action with target date, re-evaluation trigger,
  human-only flag, and mapped standards or presets. Die Felder fuer naechste
  Massnahme und Zieltermin DUERFEN nur bei `AlreadySatisfied` oder begruendetem
  `N/A` den kontrollierten Wert `N/A` tragen; dann MUESSEN Begruendung und
  konkreter Neubewertungs-Trigger gefuellt bleiben. Bei `Applicable`, `Open`
  und `FollowUp` MUESSEN Folgeaktion und Zieltermin konkrete Werte enthalten;
  kein Pflichtfeld darf leer bleiben. / The next-action and target-date fields
  MAY carry the controlled value `N/A` only for `AlreadySatisfied` or justified
  `N/A`; rationale and a concrete re-evaluation trigger MUST then remain
  populated. For `Applicable`, `Open`, and `FollowUp`, follow-up action and
  target date MUST contain concrete values; no mandatory field may be blank.
- **FR-006**: Die Matrix MUSS das kanonische zweiachsige GSDB-Statusmodell
  bewahren: Anwendbarkeit ist genau einer der Werte `Applicable`, `N/A` oder
  `Open`; Umsetzung ist genau einer der Werte `Fulfilled`, `Partly Fulfilled`,
  `Not Fulfilled` oder `Not Assessed`. / The matrix MUST preserve the canonical
  two-axis GSDB status model: applicability is exactly one of `Applicable`,
  `N/A`, or `Open`; implementation is exactly one of `Fulfilled`, `Partly
  Fulfilled`, `Not Fulfilled`, or `Not Assessed`.
- **FR-007**: Zusaetzlich MUSS jede Zeile genau einen Intake-Bewertungsstatus
  tragen: `Applicable`, `AlreadySatisfied`, `N/A`, `Open` oder `FollowUp`.
  Die folgende Entscheidungstabelle ist bindend und wird in der angegebenen
  Reihenfolge ausgewertet; dadurch ist fuer jede Kombination genau ein
  konsolidierter Status zulaessig. / In addition, each row MUST carry exactly
  one intake assessment status: `Applicable`, `AlreadySatisfied`, `N/A`,
  `Open`, or `FollowUp`. The following decision table is binding and is applied
  in the stated order so that each combination permits exactly one consolidated
  status.

| Reihenfolge / Order | Intake-Bewertungsstatus / Assessment Status | Zulaessige GSDB-Achsen / Permitted GSDB Axes | Bindende Verwendung / Binding Use | Gap erforderlich / Gap Required |
|---:|---|---|---|---|
| 1 | `N/A` | `N/A` + `Not Assessed` | Nur bei sachlicher Nichtanwendbarkeit mit Begruendung und konkretem Neubewertungs-Trigger. / Only for factual non-applicability with rationale and a concrete re-evaluation trigger. | Nein / No |
| 2 | `Open` | `Open` + `Not Assessed` oder `Applicable` + `Not Assessed` / or | Anwendbarkeit, Evidenz oder Umsetzungsstand ist materiell ungeklaert; fehlende, veraltete, widerspruechliche oder nicht reproduzierbare Evidenz hat Vorrang vor einem positiven Status. / Applicability, evidence, or implementation state is materially unresolved; missing, stale, contradictory, or non-reproducible evidence takes precedence over a positive status. | Ja / Yes |
| 3 | `AlreadySatisfied` | `Applicable` + `Fulfilled` | Nur bei aktueller, konkreter repository-lokaler Evidenz und bestandener reproduzierbarer Pruefung. / Only with current, concrete repository-local evidence and a passing reproducible check. | Nein / No |
| 4 | `FollowUp` | `Applicable` + `Partly Fulfilled` oder `Applicable` + `Not Fulfilled` / or | Die Abweichung und die spaetere Aktion sind bestaetigt; Owner, Aktion und Abnahmeziel stehen fest. / The gap and later action are confirmed; owner, action, and acceptance target are defined. | Ja / Yes |
| 5 | `Applicable` | `Applicable` + `Not Assessed` | Nur fuer einen anwendbaren Screening- oder Pruefpunkt, dessen Umsetzung diese Assessment-only-Pruefung bewusst nicht bewertet; die Scope-Begruendung darf keine fehlende Evidenz verdecken. / Only for an applicable screening or review item whose implementation this assessment-only review deliberately does not assess; the scope rationale must not hide missing evidence. | Ja / Yes |
- **FR-008**: Jede positive Bewertung MUSS auf mindestens einen existierenden,
  repository-lokalen Nachweispfad und eine reproduzierbare Pruefmethode zeigen.
  Der Evidenzeintrag MUSS den zum Pruefzeitpunkt existierenden Pfad, die
  gepruefte Quellversion oder Hash-Bindung, den exakten Read-only-Pruefschritt,
  das erwartete und beobachtete Ergebnis, Pruefdatum, Plattform sowie bekannte
  Grenzen nennen. `AlreadySatisfied` ist nur erlaubt, wenn der Schritt im
  Assessment-Lauf bestanden hat und die Evidenz den bewerteten Stand bindet.
  Eine reine Dokumentationsbehauptung, ein externer Link, ein nicht
  protokollierter Lauf oder ein wegen fehlender Umgebung uebersprungener Check
  genuegt nicht. / Every positive assessment MUST point to at least one
  existing repository-local evidence path and a reproducible verification
  method. The evidence record MUST name the path that exists at review time,
  the reviewed source version or hash binding, the exact read-only check, its
  expected and observed result, review date, platform, and known limitations.
  `AlreadySatisfied` is permitted only when that check passed during the
  assessment and the evidence binds the assessed state. A documentation claim
  alone, an external link, an unrecorded run, or a check skipped because its
  environment is unavailable is insufficient.
- **FR-009**: Widerspruechliche, veraltete, fehlende oder nur fuer eine andere
  Plattform gueltige Evidenz MUSS als solche beschrieben und bis zur
  Aufloesung `Open` oder `FollowUp` bleiben. / Contradictory, stale, missing, or
  platform-limited evidence MUST be described as such and remain `Open` or
  `FollowUp` until resolved.
- **FR-010**: Jede Zeile MUSS genau eine verantwortliche Rolle und eine
  Reviewer-Rolle nennen; Gap-Zeilen MUESSEN zusaetzlich genau einen
  Folgeaktions-Owner nennen. Zulaessige generische Rollen sind
  `Repository Maintainer`, `Project Owner`, `Security Review`,
  `Platform Owner/Admin`, `Privacy/Legal Review`, `CISO/ISB/KIB` und
  `Learning/A11Y Review`. `Unassigned`, ein Agenten- oder Modellname und eine
  erfundene Person sind unzulaessig. Bei Human-only-Punkten MUSS die Rolle aus
  der Human-only-Grenzenliste folgen; ein Agent darf weder Owner noch Reviewer
  der formalen Entscheidung sein. Die verantwortliche Rolle traegt den
  aktuellen Bewertungsstatus, der Folgeaktions-Owner die benannte spaetere
  Aktion, und der Reviewer prueft Evidenz und Status. / Every row MUST name
  exactly one responsible role and one reviewer role; gap rows MUST also name
  exactly one follow-up owner. The allowed generic roles are those listed
  above. `Unassigned`, an agent or model name, and an invented person are not
  allowed. Human-only items MUST use the role required by the human-only
  boundary list; an agent may be neither owner nor reviewer of the formal
  decision. The responsible role owns the current assessment status, the
  follow-up owner owns the stated later action, and the reviewer checks the
  evidence and status.
- **FR-010a**: Jede Zeile MUSS genau einen Restrisiko-Wert `None identified`,
  `Low`, `Medium`, `High`, `Critical` oder `Unassessed` und eine kurze
  Begruendung enthalten. `Unassessed` ist nur bei `Open` zulaessig und erzeugt
  mindestens Prioritaet `P1`, sofern kein belegter `P0`-Sachverhalt vorliegt.
  Eine Risikoakzeptanz darf nur als Human-only-Entscheidung dokumentiert und
  niemals aus der Einstufung abgeleitet werden. / Every row MUST contain
  exactly one residual-risk value from the stated vocabulary plus a short
  rationale. `Unassessed` is allowed only for `Open` and creates at least `P1`
  priority unless evidence establishes a `P0` condition. Risk acceptance may
  only be documented as a human-only decision and must never be inferred from
  the rating.
- **FR-010b**: Jede Zeile MUSS mindestens einen konkreten, pruefbaren
  Neubewertungs-Trigger nennen. Fuer `AlreadySatisfied` bindet er mindestens
  eine Aenderung an Quelle, Version, Hash, Pruefmethode oder Plattform; fuer
  `N/A` die konkrete Scope- oder Systemaenderung, die Anwendbarkeit herstellt;
  fuer `Open`, `FollowUp` und `Applicable` das fruehere von Zieltermin oder
  benanntem Evidenz-, Freigabe-, Abhaengigkeits- beziehungsweise
  Umgebungsereignis. Formulierungen wie "bei Bedarf" sind unzulaessig. / Every
  row MUST name at least one concrete, testable re-evaluation trigger. For
  `AlreadySatisfied` it binds at least a source, version, hash, check-method, or
  platform change; for `N/A`, the specific scope or system change that would
  make the item applicable; and for `Open`, `FollowUp`, and `Applicable`, the
  earlier of the target date or named evidence, approval, dependency, or
  environment event. Phrases such as "as needed" are not allowed.
- **FR-011**: Die Bestandspruefung MUSS eine Quellen- und
  Aktualitaetskontrolle fuer Baseline-Versionen, Checklisten-Versionen, stabile
  ID-Anzahl, generierten Sammelband und Manifestkonsistenz enthalten. / The
  assessment MUST include source and currency checks for baseline versions,
  checklist versions, stable ID count, generated compendium, and manifest
  consistency.
- **FR-012**: Die Bestandspruefung MUSS vorhandene Nachweise unter
  `docs/security/`, `docs/architecture/`, `docs/accessibility/`, vorhandene
  Spec-Kit-Artefakte sowie Build-, Test-, Audit- und SBOM-Nachweise als
  moegliche Evidenzquellen katalogisieren, ohne ihre Gueltigkeit nur aus ihrer
  Existenz abzuleiten. / The assessment MUST catalogue existing evidence under
  `docs/security/`, `docs/architecture/`, `docs/accessibility/`, existing Spec
  Kit artefacts, and build, test, audit, and SBOM evidence as possible sources
  without inferring validity from existence alone.
- **FR-013**: Die Bestandspruefung MUSS eine separate Inventar-Reconciliation
  fuer Build-Deklaration, Laufzeit-Mounts und State-Volumes, Versionspruefungen,
  praktische Smoke-Tests, Prompt-Dispatcher, Werkzeugregister und
  Bedienungsdokumentation liefern. / The assessment MUST provide a separate
  inventory reconciliation across build declarations, runtime mounts and state
  volumes, version checks, practical smoke tests, prompt dispatchers, tool
  registries, and operating documentation.
- **FR-014**: Die Toolchain-Reconciliation MUSS die sechs verbindlichen
  MSL-Familien .NET/C#, Java/JVM, Go, Rust, Python und Swift einzeln behandeln.
  PowerShell 7 MUSS als zweite Skriptbasis und Node.js/npm als unterstuetzendes
  Werkzeug getrennt behandelt werden. Syft, `uv` und Spec Kit MUESSEN als
  weitere Build- oder Governance-Werkzeuge eingeordnet werden. / The toolchain
  reconciliation MUST assess the six required MSL families .NET/C#, Java/JVM,
  Go, Rust, Python, and Swift separately. PowerShell 7 MUST be treated as the
  second scripting foundation and Node.js/npm as supporting tooling. Syft,
  `uv`, and Spec Kit MUST be classified as additional build or governance
  tools.
- **FR-015**: Die Agenten-Reconciliation MUSS Codex, Claude Code, Antigravity
  CLI und GitHub Copilot CLI als vier Required-Agenten sowie OpenCode und
  Gemini CLI als zusaetzlich installierte Oberflaechen pruefen. Installation,
  Versions-Pinning, Versionscheck, persistenter Zustand, Dispatcher-Support,
  Provider-/Anmeldestatus und dokumentierte Kategorie MUESSEN getrennte Felder
  sein. / The agent reconciliation MUST assess Codex, Claude Code, Antigravity
  CLI, and GitHub Copilot CLI as the four required agents, with OpenCode and
  Gemini CLI as additionally installed surfaces. Installation, version
  pinning, version check, persistent state, dispatcher support, provider/sign-in
  status, and documented category MUST be separate fields.
- **FR-016**: Die Preset-Reconciliation MUSS alle zwoelf installierten Presets
  mit ID, Version, Prioritaet, Aktivstatus, wirksamer Template-Aufloesung und
  CL-Abdeckung erfassen. Sie MUSS das verbindliche Achterprofil
  (`security-governance`, `architecture-governance`,
  `isaqb-architecture-governance`, `a11y-governance`,
  `cross-platform-governance`, `agent-parity-governance`,
  `autonomous-run-governance`, `parallel-autonomous-run-governance`) von den
  vier zusaetzlichen Presets (`model-routing-governance`,
  `intake-authoring-governance`, `intake-review-governance`,
  `intake-sequencing-governance`) unterscheiden. / The preset reconciliation
  MUST record all twelve installed presets with ID, version, priority, enabled
  state, effective template resolution, and CL coverage. It MUST distinguish
  the binding eight-preset profile from the four additional model-routing and
  intake-governance presets listed above.
- **FR-017**: Jede Abweichung zwischen Soll-Angabe, Build-Quelle,
  Laufzeitpruefung, Registry, Smoke-Test und Dokumentation MUSS als eigener
  Befund oder begruendete Gruppierung in die Lueckenliste eingehen. / Every
  difference among target claim, build source, runtime check, registry, smoke
  test, and documentation MUST enter the gap list as its own finding or a
  justified grouping.
- **FR-018**: Die priorisierte Lueckenliste MUSS stabile Gap-IDs, Prioritaet,
  betroffene CL-IDs, Kurzbeschreibung in Deutsch und Englisch, Ursache,
  Nachweislage, Auswirkung, Eintrittswahrscheinlichkeit, Abhaengigkeiten, Owner,
  Folgeaktion, Abnahmekriterium und erwartete Evidenz, Zieltermin, Restrisiko,
  Neubewertungs-Trigger sowie Human-only-Status enthalten. / The prioritised
  gap list MUST include stable gap IDs, priority, affected CL IDs, German and
  English summary, root cause, evidence state, impact, likelihood,
  dependencies, owner, follow-up action, acceptance criterion and expected
  evidence, target date, residual risk, re-evaluation trigger, and human-only
  status.
- **FR-019**: Die Priorisierung MUSS folgende Bedeutung verwenden: `P0` fuer
  unmittelbar blockierende Build-, Secret-, Isolations- oder schwere
  Sicherheitsbefunde; `P1` fuer fehlende Pflichtkontrollen oder Evidenz, die
  eine belastbare GSDB-Abnahme blockiert; `P2` fuer teilweise erfuellte
  Kontrollen und wichtige Haertung; `P3` fuer Optimierung, Klarheit oder
  Defense-in-Depth. Eine hoehere Prioritaet darf nicht allein durch eine
  Human-only-Zustaendigkeit herabgestuft werden. / Prioritisation MUST use `P0`
  for immediately blocking build, secret, isolation, or severe security
  findings; `P1` for missing mandatory controls or evidence that blocks a
  reliable GSDB acceptance; `P2` for partly fulfilled controls and important
  hardening; and `P3` for optimisation, clarity, or defence in depth. A finding
  MUST NOT be downgraded merely because it is human-only.
- **FR-020**: Jede Matrixzeile, die weder `AlreadySatisfied` noch begruendet
  `N/A` ist, MUSS genau einem Gap zugeordnet sein. Gruppierungen MUESSEN alle
  betroffenen CL-IDs nennen und duerfen Einzelstatus nicht verdecken. / Every
  matrix row that is neither `AlreadySatisfied` nor a justified `N/A` MUST map
  to exactly one gap. Groupings MUST name all affected CL IDs and MUST NOT hide
  individual statuses.
- **FR-021**: Der Abschluss MUSS eine textorientierte Statuszusammenfassung mit
  exakten Zahlen je Checkliste, Status, Prioritaet und Human-only-Kategorie
  enthalten. Farbe, Diagramm oder Position duerfen keine notwendige Information
  allein tragen. / Completion MUST include a text-first status summary with
  exact counts by checklist, status, priority, and human-only category. Colour,
  diagrams, or position MUST NOT carry required information alone.
- **FR-022**: Die spaeteren Assessment-Artefakte MUESSEN unter
  `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/` als
  `evidence-matrix.md` und `prioritized-gap-list.md` gefuehrt werden. Die
  Spec-Kit-Artefakte duerfen als gleichwertige Nachweisfuehrung dienen, wenn
  die Matrix alle CL-IDs lueckenlos auf konkrete Evidenz abbildet. / The later
  assessment artefacts MUST be maintained under the stated repository path as
  `evidence-matrix.md` and `prioritized-gap-list.md`. Spec Kit artefacts may
  serve as equivalent evidence when the matrix maps every CL ID completely to
  concrete evidence.
- **FR-023**: Die Bestandspruefung DARF keine Datei ausserhalb der spaeter
  geplanten Assessment- und Spec-Kit-Nachweise veraendern und DARF insbesondere
  keine Haertung, Konfigurationskorrektur, Secret-Rotation, formale Freigabe,
  externe Registerpflege oder Plattformregel umsetzen. / The assessment MUST
  NOT change files outside the later planned assessment and Spec Kit evidence
  and specifically MUST NOT implement hardening, configuration fixes, secret
  rotation, formal approval, external register maintenance, or platform rules.
- **FR-024**: Die Bestandspruefung MUSS den Folge-Intake
  `Lastenheft_Secure-Development-Container-Hardening.md` als durch eine
  akzeptierte Lueckenliste abhaengigen naechsten Serienkandidaten benennen, ihn
  aber weder starten noch als freigegeben behaupten. / The assessment MUST name
  the follow-up intake as the next series candidate dependent on an accepted
  gap list, but MUST neither start it nor claim it is approved.
- **FR-025**: Die Zustaende MUESSEN textlich erklaert werden: `Draft` bedeutet
  unvollstaendige Bewertung; `ReviewPending` bedeutet vollstaendige Matrix und
  Lueckenliste ohne menschliche Abnahme; `AcceptedBaseline` setzt eine
  dokumentierte menschliche Review-Entscheidung voraus. Nur
  `AcceptedBaseline` kann die Eingangsbasis fuer den Folge-Intake bilden. / The
  states MUST be explained in text: `Draft` means an incomplete assessment;
  `ReviewPending` means a complete matrix and gap list without human
  acceptance; `AcceptedBaseline` requires a documented human review decision.
  Only `AcceptedBaseline` can become input to the follow-up intake.

### Verfassungs- und Governance-Anforderungen / Constitution and Governance Requirements

- **CR-001 - Projektkontext / Project context**: Dieses Repository ist die
  Sandbox- und Lernumgebung selbst und besitzt in der bindenden Constitution
  bereits den Level-2-Registry-Eintrag
  `container-images/absdd-image-sandbox`. Dieser vorhandene Eintrag und seine
  Build-/Test-, Docs-/A11Y-, Statistik- und Agenten-Surfaces sind
  `Applicable` und in der Bestandspruefung abzugleichen. Ein neuer oder
  geaenderter Registry-Eintrag ist fuer dieses Assessment-only-Feature `N/A`,
  weil es den Projektkontext nicht aendert; Neubewertung erfolgt bei einer
  Aenderung des Registry-Eintrags oder bei Scope-Erweiterung auf ein anderes
  gemountetes Level-2-Projekt. / This repository is the sandbox and learning
  environment itself and already has the binding Level-2 registry row named
  above in the constitution. That existing row and its build/test, docs/A11Y,
  statistics, and agent surfaces are `Applicable` and must be reconciled by the
  baseline assessment. Creating or changing a registry row is `N/A` for this
  assessment-only feature because it does not change project context;
  re-evaluate when the row changes or scope expands to another mounted Level-2
  project.
- **CR-002 - A11Y**: Spezifikation, Matrix, Lueckenliste und Abschlussbericht
  MUESSEN WCAG 2.2 Level AA anwenden, soweit es fuer Markdown und
  Terminalinhalte passt. Sie MUESSEN semantische Ueberschriften,
  beschreibende Links, vollstaendige Textalternativen und Statuswoerter statt
  farblicher Bedeutung verwenden. / The specification, matrix, gap list, and
  completion report MUST apply WCAG 2.2 Level AA where relevant to Markdown and
  terminal content. They MUST use semantic headings, descriptive links,
  complete text alternatives, and status words rather than colour meaning.
- **CR-003 - Lernendenbasis / Learner baseline**: Benutzer- und
  Governance-Inhalte MUESSEN Deutsch zuerst und Englisch danach bei ungefaehr
  CEFR B2 liefern, Fachbegriffe beim ersten Auftreten erklaeren, keine
  Spec-Kit-Erfahrung voraussetzen und ab dem ersten Ausbildungsjahr fuer
  Fachinformatiker*innen, IT-System-Elektroniker*innen sowie beide
  IT-Management-Berufe verstaendlich sein. / User and governance content MUST
  be German-first and English-second at about CEFR B2, explain technical terms
  on first use, assume no Spec Kit experience, and be understandable from the
  first training year for the four declared apprenticeship audiences.
- **CR-004 - Statistik und Agent-Guidance / Statistics and agent guidance**:
  Statistikdateien und gemeinsame Agent-Guidance werden in der
  Bestandspruefung nur bewertet, nicht geaendert. Synchronisierte Updates sind
  fuer dieses Assessment `N/A`; ein spaeterer Remediation-Befund muss die
  gepflegten Oberflaechen `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`,
  `.github/copilot-instructions.md`, bei gemeinsamem Copilot-Agenteninhalt
  `.github/agents/copilot-instructions.md`, relevante Templates und
  `.specify/memory/constitution.md` zusammen behandeln. / Statistics and shared
  agent guidance are assessed, not changed. Synchronized updates are `N/A` for
  this assessment; any later remediation finding must handle the maintained
  surfaces, relevant templates, and constitution mirror together.
- **CR-005 - Primaersprache und MSL / Primary language and MSL**: Eine
  Implementierungssprache ist `N/A`, weil das Feature nur Markdown-Nachweise
  spezifiziert und weder Code noch Laufzeitverhalten erzeugt. Die sechs
  installierten MSL-Pfade bleiben Gegenstand der Inventarpruefung. Neubewertung
  erfolgt, wenn ein spaeterer Schritt Code oder Skripte aendert. / A primary
  implementation language is `N/A` because the feature specifies Markdown
  evidence only and creates neither code nor runtime behaviour. The six
  installed MSL paths remain subject to inventory review. Re-evaluate when a
  later step changes code or scripts.
- **CR-006 - NIST SSDF und CWE Top 25**: `Applicable` als verbindliche
  Prueflinsen fuer die Bestandsbewertung. Dieses Feature behauptet keine
  Code-Remediation. / `Applicable` as mandatory review lenses for the baseline
  assessment. This feature claims no code remediation.
- **CR-007 - OWASP ASVS**: `N/A` fuer die Feature-Implementierung, weil kein
  Web-, API-, HTTP- oder Authentisierungsdienst erstellt oder geaendert wird.
  Vorhandene ASVS-Anwendbarkeit bleibt als CL-01- und Evidenzfrage in der
  Bestandspruefung enthalten. Neubewertung erfolgt bei entsprechendem
  Remediation-Scope. / `N/A` for feature implementation because no web, API,
  HTTP, or authentication service is created or changed. Existing ASVS
  applicability remains an assessment question. Re-evaluate for matching
  remediation scope.
- **CR-008 - SBOM, VEX und SLSA**: `Applicable` als Pruefflaechen fuer das
  verteilbare Sandbox-Image und seine vorhandenen Lieferkettennachweise. Diese
  Assessment-Phase erzeugt kein neues Image, keine neue SBOM, keine VEX und
  keine Provenienz und darf fehlende Nachweise nur als Gap erfassen. / `Applicable`
  as review areas for the distributable sandbox image and its existing
  supply-chain evidence. This assessment phase creates no new image, SBOM,
  VEX, or provenance and may only record missing evidence as gaps.
- **CR-009 - AI-SBOM**: KI wird in diesem Feature als Entwicklungswerkzeug
  genutzt; kein KI-Modell, Datensatz oder Inferenzdienst wird Teil eines neu
  erzeugten Produktartefakts. Ein neues AI-SBOM ist deshalb `N/A`. Die
  vorhandene KI-Lieferkettentransparenz der Sandbox bleibt unter CL-05-13 und
  CL-09-15 `Applicable` und wird bewertet. Neubewertung erfolgt, wenn ein
  KI-Laufzeitbestandteil veroeffentlicht oder betrieben wird. / AI is used as
  development tooling; no model, dataset, or inference service becomes part of
  a newly produced product artefact. A new AI-SBOM is therefore `N/A`. Existing
  AI supply-chain transparency remains applicable under CL-05-13 and CL-09-15.
- **CR-010 - Architektur, CAPEC und Zero Trust**: Das Feature veraendert keine
  Vertrauensgrenze, Schnittstelle, Laufzeit, Bereitstellung oder Hardware.
  Neue Bedrohungsmodelle, ADRs, S-ADRs, arc42-Aenderungen und
  Architektur-Risikoeintraege sind `N/A`; vorhandene Nachweise und Luecken
  bleiben Bestandteil der Assessment-Matrix. CAPEC und Zero Trust werden als
  GSDB-Pruefflaechen bewertet. Neubewertung erfolgt bei technischer Haertung
  oder neuer externer Datenflussgrenze. / The feature changes no trust
  boundary, interface, runtime, deployment, or hardware. New threat models,
  ADRs, S-ADRs, arc42 changes, and architecture-risk records are `N/A`; existing
  evidence and gaps remain part of the matrix. CAPEC and Zero Trust are
  assessed as GSDB review areas. Re-evaluate for technical hardening or a new
  external data-flow boundary.
- **CR-011 - Cloud-Autonomie und Assurance / Cloud autonomy and assurance**:
  Neue BSI-C3A- und BSI-C5-Artefakte sind `N/A`, weil keine Cloud-Auswahl,
  SaaS/PaaS/IaaS-Nutzung, Provider-Abhaengigkeit oder Hosting-Aenderung
  eingefuehrt wird. Vorhandene Cloud- und Hosting-Behauptungen werden bewertet;
  formale Provider-Assurance bleibt Human-only. / New BSI C3A and BSI C5
  artefacts are `N/A` because no cloud selection, SaaS/PaaS/IaaS use, provider
  dependency, or hosting change is introduced. Existing cloud and hosting
  claims are assessed; formal provider assurance remains human-only.
- **CR-012 - Security-Evidenz / Security evidence**: Die Assessment-Ausgaben
  verwenden den begruendeten Governance-Pfad
  `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/`.
  Separate neue Dateien wie `asvs-verification.md`, `samm-assessment.md`,
  `zero-trust-applicability.md` oder `regulatory-applicability.md` sind in der
  Assessment-Implementierung `N/A`; ihr vorhandener Status wird in der Matrix
  bewertet und fehlende oder erforderliche Aktualisierungen werden als Gaps
  gefuehrt. / Assessment outputs use the stated justified governance path.
  Separate new standard-specific files are `N/A` for assessment implementation;
  their existing state is assessed in the matrix and needed updates become
  gaps.
- **CR-013 - Regulatorisches Screening / Regulatory screening**: NIS2, CRA,
  EU AI Act, DORA, Datenschutz-Folgenabschaetzung und
  Schwachstellenmeldepflichten sind `Applicable` als Screening-Fragen.
  Agenten duerfen Fakten und offene Evidenz dokumentieren, aber keine
  verbindliche Rechtsbewertung, Risikoakzeptanz oder formale
  Nichtanwendbarkeitsfreigabe erteilen. / NIS2, CRA, the EU AI Act, DORA, data
  protection impact assessment, and vulnerability reporting duties are
  `Applicable` as screening questions. Agents may document facts and open
  evidence but may not issue a binding legal decision, risk acceptance, or
  formal non-applicability approval.
- **CR-014 - A11Y-Evidenzpfad / Accessibility evidence path**: Eine separate
  neue Datei unter `docs/accessibility/` ist `N/A`, weil keine UI, Website oder
  CLI geaendert wird. Die A11Y-Pruefung der Markdown-Assessment-Artefakte wird
  in der Evidenzmatrix und ihrem Abschlussabschnitt dokumentiert. Neubewertung
  erfolgt, wenn ein spaeterer Schritt Benutzeroberflaechen oder CLI-Ausgaben
  aendert. / A separate new file under `docs/accessibility/` is `N/A` because
  no UI, website, or CLI is changed. Accessibility review of the Markdown
  assessment artefacts is recorded in the matrix and its completion section.
- **CR-015 - Cross-Platform**: Neue oder geaenderte scriptfoermige Werkzeuge,
  Bash-/PowerShell-Paare, Manpages, PowerShell-Hilfe, Cmdlet-Namen und
  Dry-run-/`WhatIf`-Paritaet sind fuer die Assessment-Implementierung `N/A`.
  Bestehende Paritaet bleibt unter CL-10-17 und den Preset-Pruefpunkten im
  Assessment. Neubewertung erfolgt, wenn Remediation ein Skript aendert. / New
  or changed script-shaped tools, Bash/PowerShell pairs, man pages, PowerShell
  help, Cmdlet names, and dry-run/`WhatIf` parity are `N/A` for assessment
  implementation. Existing parity remains in scope under CL-10-17 and preset
  checks. Re-evaluate if remediation changes a script.
- **CR-016 - Agentenparitaet / Agent parity**: Gemeinsame Agent-Guidance,
  Projekt-Templates und `.specify/memory/constitution.md` werden nicht
  geaendert; Aenderungsparitaet ist daher `N/A`. Ihre vorhandene inhaltliche
  Paritaet, inklusive begruendeter Abweichungen, ist `Applicable` als
  Assessment-Thema. / Shared agent guidance, project templates, and the
  constitution mirror are not changed, so change parity is `N/A`. Their
  existing content parity, including justified deviations, is `Applicable` as
  an assessment topic.
- **CR-017 - Autonomous Run**: Der feature-lokale Laufzustand ist
  `specs/002-gsdb-baseline-assessment/autonomous-run-state.json`. Akzeptierte
  Eingaben sind Intake, aktueller Serien-Review und Manifest. Autonomie darf
  den Assessment-Scope oder die ausdruecklichen Git-, Remote- und
  Human-only-Grenzen nicht erweitern. Ein absichtlicher Stop oder eine
  unerwartete Unterbrechung erfordert Zustandspruefung und ausdrueckliches
  Resume; ein fehlgeschlagener Gate-Nachweis blockiert `Completed`. Veraenderliche
  Freigabe-Tokens sind `N/A`, weil dieses Feature keine solche Freigabe
  benoetigt oder speichern darf. / The feature-local run state is the stated
  file. Accepted inputs are the intake, current series review, and manifest.
  Autonomy may not broaden assessment scope or explicit Git, remote, and
  human-only boundaries. A deliberate stop or unexpected interruption requires
  state validation and explicit resume; failed gate evidence blocks
  `Completed`. Mutable approval tokens are `N/A` because this feature neither
  needs nor may store them.
- **CR-018 - Dokumentationsauswirkung / Documentation impact**:
  `UpdateRequired`. Betroffen sind Lernende ab dem ersten Ausbildungsjahr,
  Maintainer, Entwicklung und Security-Review. Dokumentfamilien sind
  Spec-Kit-Anforderungen und spaetere Security-Evidenz; Leserpfade beginnen bei
  dieser Spezifikation und fuehren spaeter zur Matrix und Lueckenliste. Diese
  Spezifikation ist die kanonische Scope-Quelle; Owner ist die generische
  Projektverantwortung mit menschlichem Security-Review. Navigation muss die
  beiden spaeteren Nachweise aus dem Feature-Abschluss auffindbar machen.
  Dokumentklasse ist repository-lokale Governance- und Pruefevidenz.
  Sprachstrategie ist DE-first/EN-second im selben Markdown-Dokument. Der
  Plattformnachweis umfasst macOS, Linux und Windows, soweit je Plattform
  Evidenz vorhanden ist; fehlende Plattformpruefung bleibt `Open`.
  Distributionsklasse ist `RepositoryDocumentation`; Home-Sync ist
  `NoUpdateRequired`, weil keine Home-Runtime-Datei geaendert wird. Evidenz sind
  diese Spezifikation, die spaetere Matrix, die spaetere Lueckenliste und deren
  Review. Neubewertung erfolgt bei geaendertem GSDB-Manifest, Checklistenstand,
  Agenten-/Toolchain-Inventar, Preset-Profil oder Assessment-Scope. / The single
  documentation-impact decision is `UpdateRequired`. It covers first-year
  learners, maintainers, development, and security review; Spec Kit
  requirements and later security evidence; reader paths from this spec to the
  matrix and gap list; this specification as canonical scope source; the
  generic project owner with human security review as owner; discoverable
  navigation; repository-local governance evidence; inline German-first and
  English-second delivery; platform evidence for macOS, Linux, and Windows
  where available; `RepositoryDocumentation` distribution; no Home Runtime
  sync; and re-evaluation on changes to the GSDB, inventory, presets, or scope.

### Human-only-Grenzen / Human-Only Boundaries

**DE:** Ein Agent darf repository-lokale Fakten pruefen, Evidenzpfade nennen,
reproduzierbare Read-only-Checks ausfuehren und Entwuerfe fuer Matrix und
Lueckenliste erstellen. Die folgenden Entscheidungen duerfen nicht als
erledigt behauptet werden und bleiben mit menschlicher Rolle offen:

**EN:** An agent may review repository-local facts, cite evidence paths, run
reproducible read-only checks, and draft the matrix and gap list. The following
decisions may not be claimed as complete and remain open with a human role:

| Entscheidungskategorie / Decision Category | Verantwortliche menschliche Rolle / Accountable Human Role | Zulaessige agentische Vorbereitung / Permitted Agent Preparation |
|---|---|---|
| Formale Sandbox-, Provider-, Modell- oder Sicherheitsfreigabe / Formal sandbox, provider, model, or security approval | `CISO/ISB/KIB` | Repository-lokale Fakten und offene Evidenz dokumentieren / Document repository-local facts and open evidence |
| Datenschutz, Rechtsfrage, regulatorische Klassifikation oder Behoerdenmeldung / Privacy, legal issue, regulatory classification, or authority notification | `Privacy/Legal Review` | Screening-Fakten und fehlende Nachweise dokumentieren / Document screening facts and missing evidence |
| Secret-Rotation, -Sperrung oder -Ausgabe / Secret rotation, revocation, or issue | `Platform Owner/Admin` | Betroffene Kontrolle und Stop-Grund ohne Secret-Wert erfassen / Record the affected control and stop reason without a secret value |
| Branch Protection, Ruleset, Required Check, Code-Owner-Regel, signierter Commit, Admin-Bypass oder Plattform-Audit / Branch protection, ruleset, required check, Code Owner rule, signed commit, admin bypass, or platform audit | `Platform Owner/Admin` | Repository-seitige Evidenz und Plattformgrenze erfassen / Record repository-side evidence and the platform boundary |
| Externes Risiko-, SoA-, RoPA-, Datenschutz-, Dokumenten- oder Softwarefreigabe-Register / External risk, SoA, RoPA, privacy, document, or approved-software register | `Project Owner` oder / or `Privacy/Legal Review`, passend zum Register / as appropriate to the register | Erforderlichen Eintrag und erwartete Abnahmeevidenz beschreiben / Describe the required entry and expected acceptance evidence |
| Restrisikoakzeptanz / Residual-risk acceptance | `Project Owner` mit / with `Security Review` | Risiko, Begruendung und offene Entscheidung darstellen / Present the risk, rationale, and open decision |
| Zweitpruefung, Vier-Augen-Freigabe und `AcceptedBaseline` / Second review, four-eyes approval, and `AcceptedBaseline` | `Project Owner` mit / with `Security Review` | Vollstaendige `ReviewPending`-Artefakte bereitstellen / Provide complete `ReviewPending` artefacts |
| Anmeldung, Provider-/Modellwahl, Telemetrie oder externe Datenuebertragung / Sign-in, provider/model selection, telemetry, or external data transfer | `Project Owner` oder / or `Platform Owner/Admin`, passend zur Betriebsverantwortung / as appropriate to operational ownership | Technische Optionen und offene Freigabe dokumentieren / Document technical options and the open approval |
| Commit, Push, Pull Request, Merge, Release, Veroeffentlichung, Hosting oder Remote-Aktion / Commit, push, pull request, merge, release, publication, hosting, or remote action | `Repository Maintainer` oder / or `Platform Owner/Admin`, erst nach gesonderter Delivery-Autoritaet / only after separate delivery authority | Keine Aktion allein aus dem Assessment-Auftrag ableiten / Infer no action from the assessment request alone |

**DE:** Wo die Tabelle zwei Rollen nennt, muss die Matrix genau eine zur
konkreten Entscheidung passende verantwortliche Rolle auswaehlen und die
Auswahl begruenden. `AcceptedBaseline` verlangt immer die dokumentierte
Mitwirkung von `Project Owner` und `Security Review`; ein Agenten- oder
Modellname ersetzt keine dieser Rollen.

**EN:** Where the table names two roles, the matrix must select exactly one
accountable role appropriate to the specific decision and justify the choice.
`AcceptedBaseline` always requires documented participation by both `Project
Owner` and `Security Review`; an agent or model name replaces neither role.

- formale Sandbox-, Provider-, Modell-, Datenschutz-, Rechts- oder
  Sicherheitsfreigabe / formal sandbox, provider, model, privacy, legal, or
  security approval;
- Rotation, Sperrung oder Ausgabe von API-Keys, Tokens, Zertifikaten oder
  anderen Secrets / rotation, revocation, or issue of API keys, tokens,
  certificates, or other secrets;
- Plattformregeln wie Branch Protection, Rulesets, verpflichtende Checks,
  Code-Owner-Freigabe, signierte Commits, Admin-Bypass oder Audit-Log-Konfiguration
  / platform rules such as branch protection, rulesets, required checks, Code
  Owner approval, signed commits, admin bypass, or audit-log configuration;
- Eintraege oder Freigaben in externen Risiko-, SoA-, RoPA-, Datenschutz-,
  Dokumentenmanagement- oder Softwarefreigabe-Registern / entries or approvals
  in external risk, SoA, RoPA, privacy, document-management, or approved-software
  registers;
- verbindliche regulatorische Klassifikation, Rechtsberatung, Meldung an eine
  Behoerde oder Akzeptanz eines Restrisikos / binding regulatory
  classification, legal advice, authority notification, or residual-risk
  acceptance;
- menschliche Zweitpruefung, Vier-Augen-Freigabe und formale Abnahme der
  `AcceptedBaseline` / human second review, four-eyes approval, and formal
  acceptance of the `AcceptedBaseline`;
- Anmeldung, Provider- oder Modellwahl sowie Freigabe von Telemetrie oder
  externen Datenuebertragungen / sign-in, provider or model selection, and
  approval of telemetry or external data transfer;
- Commit, Push, Pull Request, Merge, Release, Veroeffentlichung, Hosting- oder
  Remote-Aktion innerhalb der Assessment-Erstellung, sofern eine spaetere
  ausdrueckliche Delivery-Autoritaet sie nicht gesondert und nach bestandenem
  Gate erlaubt / commit, push, pull request, merge, release, publication,
  hosting, or remote action during assessment authoring unless later explicit
  delivery authority separately permits it after a passing gate.

### Schluesselentitaeten / Key Entities

- **GSDB-Pruefpunkt / GSDB Review Item**: Eine stabile CL-ID mit Quelle,
  Anforderung, Statusachsen, Bewertung, Evidenz und Verantwortung. / A stable
  CL ID with source, requirement, status axes, assessment, evidence, and
  responsibility.
- **Evidenznachweis / Evidence Record**: Ein repository-lokaler Pfad oder ein
  reproduzierbarer Prueflauf mit Datum, Plattform, Ergebnis und Grenzen. / A
  repository-local path or reproducible check with date, platform, result, and
  limitations.
- **Bewertungsstatus / Assessment Status**: Einer der Werte `Applicable`,
  `AlreadySatisfied`, `N/A`, `Open` oder `FollowUp`, ergaenzt durch das
  kanonische zweiachsige GSDB-Modell. / One of the intake assessment values,
  supplemented by the canonical two-axis GSDB model.
- **Gap / Gap**: Eine bestaetigte oder offene Abweichung mit stabiler ID,
  Prioritaet, betroffenen CL-IDs, Owner, Folgeaktion und Restrisiko. / A
  confirmed or unresolved difference with stable ID, priority, affected CL
  IDs, owner, follow-up action, and residual risk.
- **Inventareintrag / Inventory Entry**: Eine Agenten-, Toolchain-, Werkzeug-
  oder Preset-Angabe, die ueber mehrere technische und dokumentarische Quellen
  abgeglichen wird. / An agent, toolchain, supporting-tool, or preset claim
  reconciled across technical and documentation sources.
- **Human-only-Entscheidung / Human-Only Decision**: Ein Punkt, den ein Agent
  vorbereiten oder dokumentieren, aber nicht genehmigen oder abschliessen darf.
  / An item an agent may prepare or document but may not approve or complete.

## Erfolgskriterien / Success Criteria

### Messbare Ergebnisse / Measurable Outcomes

- **SC-001**: Die Matrix behandelt 12 von 12 Checklisten und 157 von 157
  stabilen CL-IDs genau einmal; fehlende und doppelte IDs sind jeweils 0. / The
  matrix covers 12 of 12 checklists and 157 of 157 stable CL IDs exactly once;
  missing and duplicate IDs are both zero.
- **SC-002**: 100 Prozent der Matrixzeilen enthalten alle Pflichtfelder aus
  FR-005 und genau einen gueltigen Wert je Statusachse sowie genau einen
  Intake-Bewertungsstatus. / One hundred percent of matrix rows contain all
  mandatory fields and exactly one valid value on each status axis plus one
  intake assessment status.
- **SC-003**: 100 Prozent der `AlreadySatisfied`-Zeilen besitzen einen
  existierenden repository-lokalen Evidenzpfad und eine reproduzierbare
  Pruefmethode; unbelegte positive Bewertungen sind 0. / One hundred percent
  of `AlreadySatisfied` rows have an existing repository-local evidence path
  and reproducible verification method; unsupported positive assessments are
  zero.
- **SC-004**: 100 Prozent der `N/A`-Zeilen enthalten Begruendung und
  Neubewertungs-Trigger; 100 Prozent der `Open`- und `FollowUp`-Zeilen enthalten
  Owner, Folgeaktion, Zieltermin, Restrisiko und Trigger. 100 Prozent aller
  Zeilen verwenden die Statuskombinationen aus FR-007, die Rollen aus FR-010,
  die Restrisiko-Werte aus FR-010a und konkrete Trigger nach FR-010b;
  ungueltige Kombinationen, `Unassigned`-Owner und unbestimmte Trigger sind
  jeweils 0. / One hundred percent of `N/A` rows include rationale and
  re-evaluation trigger; one hundred percent of `Open` and `FollowUp` rows
  include owner, action, target date, residual risk, and trigger. One hundred
  percent of all rows use the status combinations, roles, residual-risk values,
  and concrete triggers defined by FR-007 and FR-010 through FR-010b; invalid
  combinations, unassigned owners, and indefinite triggers are each zero.
- **SC-005**: Die Inventarpruefung deckt 6 von 6 verbindlichen MSL-Familien, 2
  von 2 gesonderten Skript-/Werkzeugbasen, 4 von 4 Required-Agenten, 2 von 2
  zusaetzlichen Agentenoberflaechen und 12 von 12 installierten Presets ab. / The
  inventory review covers 6 of 6 required MSL families, 2 of 2 separate
  scripting/support foundations, 4 of 4 required agents, 2 of 2 additional
  agent surfaces, and 12 of 12 installed presets.
- **SC-006**: Jede nicht als `AlreadySatisfied` oder begruendet `N/A`
  bewertete CL-ID ist genau einem priorisierten Gap zugeordnet; nicht
  zugeordnete betroffene IDs sind 0. / Every CL ID not assessed as
  `AlreadySatisfied` or justified `N/A` maps to exactly one prioritised gap;
  unassigned affected IDs are zero.
- **SC-007**: 100 Prozent der Human-only-Punkte bleiben offen, nennen eine
  menschliche Rolle und enthalten keine agentisch behauptete Freigabe oder
  Risikoakzeptanz. / One hundred percent of human-only items remain open, name
  a human role, and contain no agent-claimed approval or risk acceptance.
- **SC-008**: Eine pruefende Person kann fuer mindestens einen Punkt jeder
  Checkliste innerhalb von insgesamt 30 Minuten die Kette von CL-ID ueber
  Status und Begruendung bis zur Evidenz und, falls FR-020 einen Gap verlangt,
  bis zum genau einen zugeordneten Gap nachvollziehen, ohne zusaetzliche
  muendliche Erklaerung. / A reviewer can trace at least one item from each
  checklist from CL ID through status and rationale to evidence and, where
  FR-020 requires a gap, to the exactly one assigned gap within 30 minutes
  total, without additional oral explanation.
- **SC-009**: Alle erzeugten Lern-, Status- und Governance-Texte sind
  DE-first/EN-second, enthalten keine unerlaeuterte erste Fachbegriffsnutzung
  und transportieren 100 Prozent der Zustaende, Abhaengigkeiten und
  Entscheidungen textlich statt nur visuell. Eine dokumentierte redaktionelle
  Vollpruefung gegen CR-002 und CR-003 MUSS dabei 0 fehlende englische
  Gegenstuecke, 0 unerlaeuterte erste Fachbegriffsnutzungen, 0 ausschliesslich
  visuell vermittelte Pflichtinformationen und 0 unerklaerte Abweichungen vom
  ungefaehren CEFR-B2-Ziel ergeben. / All produced learning, status, and
  governance text is German-first/English-second, contains no unexplained first
  use of a technical term, and conveys 100 percent of states, dependencies,
  and decisions in text rather than only visually. A documented full editorial
  review against CR-002 and CR-003 MUST find zero missing English counterparts,
  zero unexplained first uses of technical terms, zero mandatory information
  conveyed only visually, and zero unexplained departures from the approximate
  CEFR B2 target.
- **SC-010**: Die Bestandspruefung endet ohne Aenderung an Dockerfile, Compose,
  Laufzeit, Hosting, Secrets oder Plattformregeln und ohne Start eines spaeteren
  Intakes; Scope-Verstoesse sind 0. / The assessment ends without changes to
  Dockerfile, Compose, runtime, hosting, secrets, or platform rules and without
  starting a later intake; scope violations are zero.

## Annahmen und Abhaengigkeiten / Assumptions and Dependencies

- **DE:** Der akzeptierte Series-Review mit Status `Ready` hat keine offenen
  fachlichen Fragen; deshalb enthaelt diese Spezifikation keine offenen
  Klaerungsmarker.
  **EN:** The accepted series review has status `Ready` and no open material
  questions, so this specification contains no clarification markers.
- **DE:** Die 157 stabilen IDs und die zwoelf kanonischen Einzelchecklisten
  bilden den erwarteten Mindestumfang. Ein Widerspruch zwischen Manifest und
  Quellen ist ein Assessment-Befund und keine Erlaubnis, Punkte auszulassen.
  **EN:** The 157 stable IDs and twelve canonical individual checklists form
  the expected minimum scope. A conflict between manifest and sources is an
  assessment finding, not permission to omit items.
- **DE:** Repository-lokale Evidenz ist lesbar, aber ihre Existenz beweist weder
  Aktualitaet noch Wirksamkeit. Jede positive Bewertung braucht eine eigene
  Pruefung.
  **EN:** Repository-local evidence is readable, but existence proves neither
  currency nor effectiveness. Every positive assessment needs its own check.
- **DE:** Praktische Container-, Plattform- oder Netzwerkpruefungen koennen
  lokal nicht verfuegbar sein. Fehlende Ausfuehrbarkeit wird transparent als
  `Open` dokumentiert und nicht durch eine Annahme ersetzt.
  **EN:** Practical container, platform, or network checks may be unavailable
  locally. Missing executability is recorded transparently as `Open` and is not
  replaced by an assumption.
- **DE:** Das Feature haengt vom aktuellen Inhalt von `Dockerfile`,
  `compose.yml`, `scripts/smoke-test-toolchains.sh`, den Werkzeugregistern,
  Agent-Prompt-Dispatchern, installierten Presets und vorhandenen
  Evidenzverzeichnissen ab. Aenderungen an diesen Quellen loesen eine
  Neubewertung aus.
  **EN:** The feature depends on the current Dockerfile, Compose file,
  toolchain smoke test, tool registries, agent prompt dispatchers, installed
  presets, and existing evidence directories. Changes to these sources trigger
  re-evaluation.
- **DE:** Die Lueckenliste ist nur eine fachliche Eingabe fuer spaetere
  Haertung. Sie erteilt keine Implementierungs-, Git-, Remote-, Merge-, Bypass-
  oder Hosting-Autoritaet.
  **EN:** The gap list is only a subject-matter input for later hardening. It
  grants no implementation, Git, remote, merge, bypass, or hosting authority.
