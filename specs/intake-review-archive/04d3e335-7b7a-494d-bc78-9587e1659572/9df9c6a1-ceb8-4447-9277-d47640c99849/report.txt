# Vollreview der fünfgliedrigen Sandbox-Reihe / Full Five-Member Sandbox Review

## Deutsch

Ergebnis am 2026-11-08: **NeedsRemediation**. Alle fünf Lastenhefte wurden
vollständig fachlich geprüft, nicht nur gehasht. Keine Campaign, null Worker.
Zwei hohe und ein mittlerer Befund; keine kritischen/niedrigen Befunde,
keine akzeptierten Risiken und keine offenen Entscheidungsfragen.

Reviewauftrag: `specs/intake-review-requests/sandbox-development-lifecycle.json`.
Die logische Review-ID bleibt `04d3e335-7b7a-494d-bc78-9587e1659572`;
Revision, Zeitpunkt, Head, Zielhashes und Archivpfade stehen im Ergebnis.
Geprüfter Head: `d165d49a1b206cc94cce3b640dd14dec88b8857f`.
Die installierte Intake-Review-Checkliste und Projektregeln für
`learner-a11y-bilingual-series` bilden die Prüfbasis; Schema 2.0 ist Aligned.

| ID | Schwere | Befund | Erforderlicher Folgeschritt |
|---|---|---|---|
| IR901 | High | 17 Quellen haben in je drei Receipts andere normalisierte Hashes: 51 veraltete Bindungen für Hardening, Selbstprüfung und Selbstbau. | Änderungen fachlich abgleichen und Provenienz autorisiert erneuern; keine bloße Hash-Ersetzung. |
| IR902 | High | Alle vier aktiven Receipts verwenden denselben Pfad für Vorgänger-Receipt und Archiv-Receipt. Der installierte Validator lehnt dies ab. Auch das quellenaktuelle Update-Receipt scheitert. | Historischen Receipt-Vertrag und kanonische Validatorsemantik abgleichen; konsistente Reparatur separat autorisieren und in beiden Shells prüfen. |
| IR903 | Medium | FU-018 und die Selbstbau-Qualitätsregeln verlangen Renovate; aktuelle AGENTS/Dependency-Policy verlangen das Pin-Register und erklären Renovate für abgelöst. | Veralteten Mechanismusbezug in DE/EN autorisiert aktualisieren, Integritätsziele und Reviewgates erhalten. |

Owner aller Befunde ist der Repository Owner gemeinsam mit der zuständigen
Intake-/Governance-Pflege. Jeder Befund hat im JSON Evidenz, Auswirkung,
Abhilfeschritt und Neubewertungsauslöser. IR902 ist ein nachgewiesener
Vertrags-/Kompatibilitätsfehler; daraus folgt keine Behauptung verlorener
Archivbytes oder Manipulation. Keine provisorische Kopie oder Schutzlockerung
nur zum Bestehen eines Validators.

### Vollständige inhaltliche Abdeckung

| Mitglied | Bewertung |
|---|---|
| GSDB-Bestandsprüfung, archivierte Root | Assessment-Scope, zwölf Checklisten, priorisierte Lücken, Open/N/A und menschliche Grenzen klar; historische Root wird nicht erneut ausgeführt. |
| Technisches Hardening | Allgemeine Anforderungen, H-344-01–10 und AC-H-344-01–10 einschließlich 85 % Branch-/80 % Interface-Abdeckung, zehn Delta-Gruppen und offene Übergaben nachvollziehbar. IR901/IR902 sperren aktuelle Provenienzbereitschaft. |
| Ubuntu/OpenCode-Web/MSL | Alle FU-001–023 und FA-001–012 geprüft: Basis/Swift, Ausgabepfade, Authentifizierung/Readiness, gemeinsame Clients, sieben Profile, Daten/Audit, Sicherheit, native Plattformen, DE/EN/A11Y. IR902/IR903 offen. |
| Unabhängige Selbstprüfung | A-344-/AC-A-344 sowie A-FU-/AC-A-FU-Verträge verlangen beide Vorgänger auf derselben finalen Quellrevision und passender Image-ID; vollständige FU/FA-Zuordnung und risikobasierte Gegenprüfung ohne Selbstabnahme. IR901/IR902 offen. |
| Lernenden-Selbstbau | FR-001–015, L-FR-016–023, AC-001–012 und L-AC-013–020 vollständig geprüft: Fork/Institution, origin/upstream, Selbstbau, Plattformneutralität, SBOM, optionale Template-/Rechtegrenzen. Sechs Sprachen betreffen das Standardprofil all. IR901/IR902/IR903 offen. |

Zielgruppe, vorausgesetztes Wissen, Begriffe, Sprache, Anforderungen,
Abnahme, Scope/Nicht-Ziele, Risiken, Prompts und Lieferautorität wurden je
Mitglied geprüft. Deutsch/Englisch und textuelle Zustände/Übergaben bleiben
verständlich. Das frühere IR701-Glossar und der IR801-Update-Abnahmevertrag
sind vorhanden. Fehlende praktische Usability-, Browser-, WCAG-, native
Plattform- oder menschliche Nachweise werden durch dieses Review nicht ersetzt.

Der Graph enthält fünf eindeutige Ziele, eine Root und fünf bindende Kanten.
Hardening → Update, Hardening → Selbstprüfung, Update → Selbstprüfung und
Selbstprüfung → Selbstbau bleiben erhalten; GSDB → Hardening liefert die
Baseline. Manifest, Auftrag und Reihenansichten stimmen strukturell überein.
Die de-DE-Konfiguration mit vier Rollen, sechs Collections und begrenztem
Legacy-Alias ist konsistent. Sechs physische aktive Dateien sind von vier
aktiven Serienmitgliedern und der archivierten Root zu unterscheiden.

Der deklarierte Lifecycle bleibt Completed/Eligible/Blocked/Blocked/Blocked.
Ein historischer Completed-Lauf für Feature 003 bindet einen anderen
Hardening-Eingabehash; er schließt das heutige erweiterte Lastenheft nicht
automatisch ab. Ebenso ersetzt vorhandener Resolute-/Web-/Profil-Code keine
finale Plattform-/Abnahmematrix. Vor jeder späteren Arbeit vorhandene Umsetzung
bewerten, keine Doppelimplementierung und keine automatische Serienpromotion.

### Evidenz, Historie und Grenzen

Die Zielhashes aller fünf Dateien, der Reviewauftrag und die Serienbindungen
passen weiterhin. Vier installierte Bash-Receipt-Prüfungen enden mit Exit 2;
Manifest und Serien-Receipt bestehen. Erwartete und aktuelle Quellenhashes
sowie vier Vorgängerbindungen stehen in
[der Evidenzdatei](sandbox-development-lifecycle-2026-11-08-evidence.json).
Der Ergebnisvalidator prüft Format und Ziel-/Auftragsbindung; ein erfolgreicher
Validatorlauf bedeutet hier ausdrücklich **NeedsRemediation**, keine Freigabe.

Das Ready vom 2026-11-02 und sein Bericht sind vor Ersetzung bytegleich
archiviert; auch der unveränderte Auftrag ist im neuen Archiv enthalten.
Der neue Ergebnisstand verweist ausdrücklich auf den Vorgänger. Keine
Lastenheft-, Receipt-, Request-, Manifest-, Run-State- oder Quelländerung.
Keine Implementierung, Builds, Containeraktionen, Inferenz, Remote-Schreib-
operationen, Commits, Pushes oder Risikoannahmen.

Nächste Aktion: die begrenzte Reparatur von **IR901, IR902 und IR903** gesondert
autorisieren, danach das vollständige fünfgliedrige Review erneut ausführen.

## English

Outcome on 2026-11-08: **NeedsRemediation**. All five complete requirements
documents, acceptance criteria and prepared prompts were reviewed. This is a
Series review with zero workers: two High and one Medium finding, no Critical
or Low findings, accepted risks or unanswered decision questions.

IR901 identifies 51 stale bindings: the same 17 source files changed in each
of the hardening, acceptance and learner receipts. Review the changes before
an authorized provenance renewal; simply replacing hashes is insufficient.
IR902 identifies a historical-receipt/installed-validator incompatibility:
all four active receipts identify the predecessor and archived receipt by
the same path, rejected by the validator's samefile guard. The update receipt
also fails despite having current source hashes. This does not prove lost
archives or tampering. Reconcile canonical contract semantics through a
separately authorized repair and both-shell positive/negative checks; do not
weaken containment or duplicate evidence merely to pass.
IR903 identifies conflicting normative instructions: FU-018 and learner
quality rules preserve Renovate, while current AGENTS and dependency policy
require the pin register/Dependabot and retire Renovate. Align both languages
under explicit authority without weakening integrity or review gates.
The Repository Owner and relevant intake/governance maintainers own these
findings; the JSON records evidence, impact, remedy and re-evaluation triggers.

Individual coverage includes the archived GSDB assessment and all twelve
checklists; hardening's general requirements, H/AC-H-344 groups and 85%/80%
thresholds; all FU-001–023/FA-001–012; acceptance's A/AC-A-344 and A-FU/AC-A-FU
handoffs; learner FR-001–015, L-FR-016–023, AC-001–012 and L-AC-013–020.
Shared web clients, authentication/readiness, seven profiles, native platforms,
security/audit persistence and profile/image identity remain measurable.
Acceptance consumes both H/U handoffs on the same final source/image per
profile/architecture, requires complete FU/FA mapping, independent risk-based
counterchecks and justified evidence reuse, and prohibits self-acceptance.
Learner self-build preserves fork/institution origin-upstream, hosting
neutrality, local SBOM, no project-image distribution and optional template,
licensing and human gates. Six-toolchain checks refer to default all.

Audience, prerequisites, terminology, German-first/equivalent-English text,
scope, non-goals, requirements, acceptance, risks, prompts and authority were
reviewed for each member. IR701 glossary and IR801 acceptance repair remain
present. Text explains states/dependencies without relying on diagrams.
This review does not perform practical usability, browser, WCAG, native
platform or human acceptance.

Five unique targets, one root and five binding DAG edges are consistent
between the manifest, request and order views. Schema2 de-DE naming, four
roles, six collections and the bounded legacy alias are Aligned. Six physical
active files differ from four active series members plus one archived root.
The declared lifecycle remains Completed/Eligible/Blocked/Blocked/Blocked.
A historical Completed Feature 003 run binds a different hardening input and
cannot close today's expanded intake. Existing Resolute/Web/profile code
does not replace final acceptance; assess existing work before later changes
and do not automatically promote lifecycle states.

All five target, request and series bindings match. Source freshness and
receipt contract checks fail as documented; successful result validation
means a valid **NeedsRemediation** report, not readiness. Exact hashes and
lineage are in the linked evidence file. The prior 2026-11-02 Ready result,
report and unchanged request were archived byte for byte and explicitly
superseded. Reviewed inputs remain unchanged. No implementation, builds,
container actions, inference, remote writes, commits, pushes or risk acceptance.

Next action: separately authorize bounded repair of **IR901, IR902 and IR903**,
then repeat the complete five-member review.
