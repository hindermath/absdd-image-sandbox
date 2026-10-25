# Optionales Template: Anforderungsabgleich / Optional Template Requirements Alignment

## Deutsch

Ownerentscheidung vom 25.10.2026: zusätzliches Template-Profil, Fork bleibt
Standard; MIT nur für nachweislich eigene Inhalte. Dieser beauftragte Lauf
bereitet Dokumentation, Lizenzabgrenzung, CI-Vertrag und Quellenbindungen vor.
Er startet **nicht** die blockierte Selbstbau-Implementierung und aktiviert
keine GitHub-Einstellung. Keine Änderung der bisherigen Akzeptanzschwellen
oder Lifecycle-Folge Completed, Eligible, Blocked, Blocked.

Die bestehende FR-013 des Selbstbau-Intakes erlaubt bereits das optionale
Profil. Neue L-FR-020 bis L-FR-023 konkretisieren Rechte, Historie, persönliche
Übernahme und getrennte Aktivierung; sie ersetzen FR-001 bis FR-019 nicht.
Hardening und Selbstprüfung erhalten nur den Quellen-/Übergabeabgleich.
Einführung, Git-Anleitung, FAQ, Agent-Guidance, Präsentationen und Werkstätten
unterscheiden Fork, unabhängige Sandbox-Kopie und leeres Produktrepo.

Die referenzgebundene GSDB-Projektevidenz wird in einem eigenen Workflow-Step
nur in `hindermath/absdd-image-sandbox` geprüft. Allgemeine Generator-, Pin-,
Parity-, Negativfixture- und Assurance-Regressionsprüfungen bleiben überall
aktiv. Der exakte Statistik-Pilot mit Historienbindung wird ebenfalls nur in
der Referenz ausgeführt. Ein übersprungener historischer Proof ist ausdrücklich
kein persönlicher Erfolg; neue Repos benötigen eigene anwendbare Gates.
Keine installierten Presets oder historischen Nachweise umgeschrieben.

Byteidentische archivierte Reihenansichten behalten relative Links ihres
Ursprungsortes. Nur `order.md` und `requirements-order.md` innerhalb eines
Serien-/Operationsarchivs sind deshalb von der normalen Markdown-Linksuche
ausgenommen; Archivhashes bleiben separat geprüft. Aktive Reihenansichten,
sonstige Archivdokumente und alle Lernenden-Seiten bleiben im Linkcheck.
Der neue Template-Vertragstest läuft im allgemeinen statischen CI-Job.

Vorherige drei Intakes/Receipts, Reihenansichten und Review-Artefakte wurden
vor Edits bytegetreu archiviert. Die neuen Receipts behalten Intake-IDs,
binden zuerst den jeweiligen vorherigen Intake und danach die geordneten
aktuellen Quellen. Alte Reviews sind explizit ersetzt, nicht still weiterverwendet.
Ein vollständiges unabhängiges Serienreview beurteilt die neue Fassung;
Ready würde keine technische, rechtliche oder persönliche Ausführung freigeben.

LIC-01/02: Open; Owner Repository Owner mit Rights Review; Follow-up Herkunft/
Attribution gruppenbezogen klären; Trigger vor Aktivierung oder Weiterverteilung
betroffener Inhalte. Menschliche A11Y-Erstnutzung bleibt Open, Owner Learning/A11Y
Review; Follow-up beide Sprachen prüfen; Trigger vor Konformitätsbehauptung.

Spätere Reihenfolge: erforderliche Vorgängerabnahmen → Selbstbau-/Template-
Eignung im genehmigten Umfang prüfen → dokumentierten Stand ausliefern →
gesonderte Ownerentscheidung zum Template-Flag. Eine echte private Testkopie
braucht einen separaten Auftrag. Keine Produkt-Images als Registry-Bezugsweg.

## English

The owner selected an additional template profile while retaining fork as
default and MIT only for demonstrably original work. This run prepares docs,
rights boundaries, CI contracts and source bindings; it does not start blocked
self-build implementation or enable GitHub settings. Keep all existing
acceptance thresholds and Completed/Eligible/Blocked/Blocked lifecycle states.

Existing FR-013 permits the optional profile. L-FR-020..023 and matching
acceptance criteria make rights, independent history, personal handover and
separate activation explicit without replacing prior requirements. Hardening
and self-review receive source/handover clarification only.

Only historical reference-project GSDB evidence and the exact-history statistics
pilot are reference-repository scoped. General security, syntax, pinning,
parity, fixtures and regressions remain active for copies. Skipped source proof
is not personal acceptance; establish applicable personal gates separately.

Byte-identical archived order views retain source-relative links. Only the two
order filenames inside a series/operation archive are excluded from ordinary
link resolution; verify archive hashes separately. Active views, other archived
documents and learner pages remain checked. The template regression runs in
the general static CI job.

Three old targets/receipts, series views and review artifacts are archived
byte-for-byte. Preserve identities, bind previous target first, then ordered
current sources and explicitly supersede review. Full independent review grants
no technical/legal/personal execution authority. Rights and human A11Y checks
remain Open with owners/follow-ups/triggers above. Later activation requires
predecessor acceptance, authorized readiness work, delivered docs and a separate
owner decision. No actual template-copy creation or remote mutation in this run.
