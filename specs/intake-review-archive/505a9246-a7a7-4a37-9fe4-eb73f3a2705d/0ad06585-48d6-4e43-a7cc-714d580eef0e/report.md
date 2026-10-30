# Vollständiges Serienreview / Complete Series Review

## Deutsch

**Ergebnis: NeedsRemediation.** Fünf Ziele vollständig gelesen und fachlich
geprüft; ein High-Befund blockiert die Gesamtbereitschaft. Es wurden keine
Anforderungen repariert und keine Risiken stellvertretend akzeptiert.

- Review-ID: `505a9246-a7a7-4a37-9fe4-eb73f3a2705d`.
- Datum: 30.10.2026; Reviewer: Codex, agentische Anforderungsprüfung.
- Repository-Head: `d5c313b5461afc09bec97e9980e2fd7632e6d2ff`, mit vorhandener lokaler Governance-Arbeit.
- Modus: Series; fünf Ziele (archivierte Root und vier aktive Mitglieder), null Kampagnen-Worker.
- Policy: `learner-a11y-bilingual-series` aus dem expliziten Auftrag und der Projekt-Guidance; installierte Intake-Review-Checkliste und Schema-2.0-Vertrag verwendet. Die generische Policy-Vorlage ist kein zusätzlich aktivierter Projektvertrag.
- Auftrag: [fünfgliedriger Request](../intake-review-requests/sandbox-development-lifecycle.json).
- Maschinenlesbar: [Ergebnis](../intake-review-results/sandbox-development-lifecycle.json).
- Findings: Critical 0, High 1, Medium 0, Low 0. Akzeptierte Risiken 0; offene materielle Fragen 0.

### IR801 — Unabhängige Abnahme übernimmt das neue Feature-Update nicht konkret

**Schwere: High. Kategorie: Serienübergabe und Prompt-Abgleich.**
Owner: Repository Owner und Security Review. Disposition: Open, blockiert Ready.

Das neue Feature-Update erweitert die Sandbox um einen geschützten Webdienst,
gemeinsame Clients, einen Basiswechsel und sieben Build-Profile. Abschnitt 7
ordnet die unabhängige Selbstprüfung ausdrücklich **nach Hardening und Update**
ein. Manifest und Reviewrequest enthalten beide Kanten korrekt.

Das empfangende `Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md`
beschreibt dagegen weiterhin nur den Abschluss und die Übergabe des Hardening.
A-344-01/04, die Abnahmekriterien und die Folgeprompts an Zeilen 395 und 400
benennen weder den neuen Update-Intake noch die FU-/FA-Verträge. Generische
HTTP- und Toolchain-Prüfungen legen nicht fest, wie die neue Authentifizierung,
Readiness, gemeinsamen Clients und Profil-/Sicherheitsnachweise unabhängig
gegengeprüft werden. Die Unabhängigkeitsregel verbietet nur Selbstabnahme der
Härtung, nicht ausdrücklich der später implementierten Update-Anteile.

**Auswirkung:** Die graphische Sperre verhindert einen zu frühen Start, aber
schließt die inhaltliche Abnahmelücke nicht. Nach Abschluss des Updates könnte
der kopierte Abnahmeprompt weiterhin einen alten, nur hardeningbezogenen
Prüfumfang liefern. Gerade die neue Web-Angriffsfläche wäre nicht eindeutig
einem unabhängigen Prüfauftrag zugeordnet.

**Konkrete Belege:** Update FU-007–020; FA-003–008 und FA-012; Abschnitt 7,
insbesondere Zeilen 307–339. Empfänger: Ausgangslage Zeilen 172–183,
A-344-01/04 Zeilen 235–270, AC-A-344-01–04 Zeilen 273–299,
Abhängigkeiten Zeilen 309–319 und beide kopierbaren Folgekommandos.

**Erforderliche Korrektur, hier nicht ausgeführt:** Im empfangenden DE/EN-
Abnahmevertrag und seinen Prompts beide Vorgänger sowie das finale gemeinsame
Update-Image und dessen Quellstand ausdrücklich binden. Die unabhängige,
risikobasierte Prüfung der neuen FU-/FA-Nachweise zuordnen: Webzugriff und
synthetische Negativfälle, Readiness, Clients, Profile/Architekturen sowie
fortbestehende Audit- und Sicherheitsgrenzen. Nicht blind alle Tests verdoppeln;
begründete Übernahmen und eigene Gegenprüfungen unterscheiden. Prüfer dürfen
nicht die jeweils selbst implementierten Hardening- oder Update-Anteile
abnehmen. Bestehende H-/A-Grenzwerte, Graphkanten und menschliche Gates erhalten.
Eine spätere Reparatur erneuert die betroffenen Receipt-/Manifest-/Request-
Bindungen nach Governance und benötigt ein erneutes vollständiges Review.

**Neubewertung:** nach ausdrücklich autorisierter Korrektur und erneuerten
Quellenbindungen; nicht allein nach grünen JSON-Validatoren.

### Einzelabdeckung und Reihenfolge

| Rang | Ziel | Fachliche Einordnung |
|---|---|---|
| 1 | Archivierte GSDB-Bestandsprüfung | Vollständig als abgeschlossene historische Root gelesen. Evidenzmatrix, Lückenliste und Human-only-Grenzen bleiben Quelle für H; keine Wiedereröffnung oder neue Abnahme behauptet. |
| 2 | Container-Hardening | Zweck, Nicht-Ziele, H-344-01–10, AC-H-344-01–10, GSDB 3.4.4/Assurance 0.1.8, messbare 85-/80-Prozent-Schwellen und offene Übergaben sind nachvollziehbar. Keine neue App nur für Kontrolltests. |
| 3 | Ubuntu-/Web-/MSL-Update | Alle FU-001–023, FA-001–012, Quellen #101/#102/#104, Begriffe, DE/EN-Entsprechungen und Prompts geprüft. Natives Profil-/Architekturtesten, Versionserhalt, Authentifizierung, Readiness, Audit und Human-Gates sind ausdrücklich gefordert. |
| 4 | Unabhängige Selbstprüfung | Historische H-/A-Kontrollübergabe ist klar; die neue konkrete Update-Übernahme fehlt: IR801. Dies blockiert das Gesamt-Ready. |
| 5 | Lernenden-Selbstbau | Fork/origin/upstream, lokale Builds, Rechte-/Template-Gates, Voraussetzungen, alle FR-/AC-/L-Kriterien und Prompts geprüft. Das sechs-Sprachen-Smoke-Kriterium passt zum vollständigen Standardprofil `all`; zusätzliche reduzierte Profile ändern diesen Default nicht automatisch. |

Identität, Zielgruppe, Vorwissen, Zweck, Umfang und Nicht-Ziele, atomare und
messbare Kriterien, Abhängigkeiten, Sicherheit/Datenschutz/Lieferkette,
Plattformen/A11Y, Nachweise, Lieferautorität, Risiken, Verweise und Prompts
wurden für alle fünf Texte geprüft. Der historische Roottext ist keine neue
Erstjahres-Anleitung; seine historischen Anforderungen werden nicht umgeschrieben.

Der Graph hat fünf eindeutige Ziele und fünf azyklische bindende Kanten.
Einzige Root ist die archivierte abgeschlossene GSDB-Prüfung. Bestehende Kanten
GSDB → H, H → A, A → L bleiben; zusätzlich H → U und U → A. U bezeichnet das
Feature-Update. H liefert die Sicherheitsbaseline, U muss sie erhalten und
seine Kombination auf demselben finalen Stand nachweisen. IR801 betrifft die
empfangende unabhängige Prüfverantwortung, nicht eine fehlende Graphkante.

Lifecycle bleibt **Completed → Eligible → Blocked → Blocked → Blocked**.
Hardening ist allein strukturell Eligible. Das ist weder eine neue Review-
Freigabe noch eine Startautorität; dieses Gesamt-Review ist blockierend.
L wartet auf erfolgreiche unabhängige technische Abnahme. Human-only-Fragen
und anwendbare offene Betriebskontrollen werden nicht automatisch geschlossen.

### Konfiguration, Sprache und Prüfgrenzen

Schema 2.0 meldet Aligned: `de-DE`, deutsches Benennungsprofil, vier portable
Rollen, konfigurierte Sammlungen und begrenzter Legacy-Pfad passen zusammen.
Sechs physische aktive Intake-Dateien sind von vier aktiven Serienmitgliedern
und insgesamt fünf Serienzielen zu unterscheiden; `SeriesManifest` erlaubt die
beiden eigenständigen Intakes außerhalb dieser Serie. Canonical Index und
beide textuellen Reihenansichten stimmen mit dem Manifest überein.

Die aktiven Texte erklären Vorwissen und Spec-Kit-/Fachbegriffe und enthalten
deutsche und gleichwertige englische Anforderungen sowie textorientierte
Status-/Entscheidungswege. Readability und ungefähr CEFR B2 wurden redaktionell
beurteilt. Rendering, Tastatur, Screenreader/Braille und reale Lernendenpiloten
wurden nicht ausgeführt; daraus entsteht keine WCAG-AA- oder Usability-Abnahme.

Sicherheitsstandards, regulatorische Anwendbarkeit und Cloud-Nachweise werden
als Anforderungen und begründete offene menschliche Entscheidungen gelesen,
nicht in diesem Intake-Review rechtlich zertifiziert. Kein Build, Container-
oder Modelllauf und keine Secret-/Provider-/Hosting-Aktion wurden ausgeführt.

### Herkunft, Validierung und Dokumentationsauswirkung

- Request-Normalized-SHA-256: `52ae3f2a08bc2836d0be3315651e9502d8547a369bfd1ae23ee603e7b7c8a1da`.
- Manifest: `0f8f3685aaba88448bbe160e4b7b6d62f63b0508f96525179546e4d33f15bcf1`.
- Serienreceipt: `e8b940d18d6de069d5e7a2076db6360c32a53b0d8bd86a59a777c5d38b2ced45`.
- Alle fünf Zielhashes mit strengem UTF-8, optional einem entfernten BOM und ausschließlich normalisierten Zeilenenden geprüft; Inhalt unverändert. Git-Blob-IDs im JSON beschreiben Inhalt, nicht dessen Veröffentlichung.
- Konfiguration, Manifest, Serienreceipt und alle vier aktiven Authoring-Receipts mit installierten Bash-Validatoren geprüft: 71 + 7 + 73 + 73 = 224 aktuelle Quellenbindungen.
- Der vorherige Supersession-Marker und PendingReview-Bericht wurden vor Ersatz bytegleich unter `specs/intake-review-archive/505a9246-a7a7-4a37-9fe4-eb73f3a2705d/pre-review-20261030/` archiviert. Rohhashes im JSON. Der frühere viergliedrige Ready-Bericht bleibt unverändert historisch; seine Entscheidung gilt nicht für fünf Mitglieder.
- Ergebnisvalidierung mit installierten Bash- und PowerShell-Validatoren: beide PASS für Series/NeedsRemediation/fünf Ziele. Dies bestätigt die korrekte Bindung des blockierenden Ergebnisses, nicht Ready.
- Abschlussvergleich: 740 geschützte Bestandsdateien unverändert, aggregierter Roh-SHA-256 `364dc8e465bbe84b71180bb588818f8e20c86940e25ba9b5a2f7f16374ba741a`; HEAD unverändert. Ausgenommen sind ausschließlich die beiden ausdrücklich erneuerten Reviewdateien, deren neue Archivkopien und das neue Sitzungsprotokoll.
- Secret-Scans aller fünf Zieltexte und neuer Review-Evidence sowie `git diff --check`: bestanden.

Documentation Impact: **UpdateRequired**, Owner Repository Owner. Geändert
werden ausschließlich der Review-Leserpfad (dieser Bericht und Ergebnis-JSON),
archivierte Vorstände und das vorgeschriebene Sitzungsprotokoll. Klasse
`sourceOnly`; kein Home-Sync. Neubewertung bei Ziel-, Request-, Graph-, Receipt-
oder Findings-Änderung. Die bestehende fremde lokale Arbeit bleibt erhalten;
kein Commit, Push, Specify- oder Autonomous-Lauf.

### Nächste Aktion

IR801 nach ausdrücklicher Reparaturautorität beheben und die vollständige Reihe
erneut reviewen. Kopierbare Aktion, hier nicht ausgeführt:

`$speckit-intake-repair specs/intake-review-results/sandbox-development-lifecycle.json`

## English

**Outcome: NeedsRemediation.** All five complete intake texts and their series
relationships were semantically reviewed under the explicit learner/bilingual
policy and installed checklist. There is one High finding, IR801; no Critical,
Medium or Low findings, accepted risks, unanswered material questions, campaign
workers or operator exceptions. Schema 1.1 binds the unchanged request and all
five target hashes. This is an agent requirement review, not human approval,
independent product acceptance or permission to execute.

**IR801, High, owner Repository Owner and Security Review:** the graph and the
update intake correctly require both hardening and the completed update before
independent acceptance. However, the receiving acceptance intake's current
state, A-344-01/04, acceptance criteria and copy-ready prompts at lines 395/400
still explicitly consume only the hardening handoff. They do not concretely
assign independent checks of the new web authentication/readiness, common
clients, profile/architecture evidence and retained security/audit controls on
the final update image. Its reviewer-independence rule names hardening authors,
not authors of the update portions being accepted. Generic HTTP/tool checks
are not an explicit receiving FU/FA contract. This is a semantic handoff gap,
not a missing graph edge or proof of an implemented vulnerability.

Repair the receiving German/English requirements and prompts only under fresh
authority. Bind both predecessors, the same final source/image identity and
risk-based independent positive/negative checks of new FU/FA evidence. Explain
any evidence reuse rather than mechanically duplicating every test. Reviewers
must not accept the hardening or update portions they implemented themselves.
Keep previous thresholds, graph and human gates; renew affected governance
bindings and repeat full review. This review performs no repair or risk acceptance.

The archived assessment remains historical dependency context. Hardening's
ten delta groups retain measurable criteria and human boundaries. The update's
23 requirements and 12 acceptance criteria cover its genuine new scope.
Self-build retains the full `all` default, fork/upstream, local builds, rights
and optional-template gates. Reduced profiles do not automatically invalidate
the standard six-language smoke requirement. All five targets are ordered
exactly once, with five unique acyclic edges and one archived completed root.
The state remains Completed/Eligible/Blocked/Blocked/Blocked: hardening alone
is structurally eligible, but this full review does not permit execution.

Schema-2.0 configuration is Aligned: de-DE, naming, four portable roles,
collections, legacy alias, index and textual orders agree. Six physical active
intakes are distinct from four active series members and five total targets;
two standalone intakes are allowed. All active authoring receipts passed their
installed Bash validator with 224 bound sources. Current normalized hashes
and historical supersession evidence are preserved. The former pending marker
and report were archived byte for byte; the four-target Ready is not reused
as a five-target acceptance decision.

Prior knowledge, terminology, German-first/equivalent-English and text-first
navigation were assessed. B2 is an editorial target, not certification. No
browser/screenreader/Braille/user-pilot, image/platform, legal or formal
security acceptance is claimed. No container, model, provider, hosting,
commit, push or downstream feature action occurred. Documentation Impact is
UpdateRequired for source-only review evidence; no Home Runtime sync.

Both installed Bash and PowerShell result validators passed for the current
Series/NeedsRemediation/five-target result. This validates evidence integrity,
not readiness. All 740 protected existing files and repository HEAD remain
unchanged; the aggregate raw SHA-256 is
`364dc8e465bbe84b71180bb588818f8e20c86940e25ba9b5a2f7f16374ba741a`.
Only the two renewed review files, their new archive copies and the required
session log are excluded. Secret scans of all five targets and new review
evidence, plus diff whitespace validation, passed.

Next separately authorized action is the repair command above.
