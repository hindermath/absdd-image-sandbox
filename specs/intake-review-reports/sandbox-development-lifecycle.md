# Nachreview IR901–IR903 / IR901–IR903 Re-review — 2026-11-08

## Deutsch

**Ergebnis: Ready.** Die vollständige fünfgliedrige Reihe wurde nach der
autorisierten Reparatur erneut fachlich geprüft. Null offene Befunde aller
Schweregrade, keine akzeptierten Risiken, keine offenen Fragen, null Worker.
Ready bewertet die Anforderungs- und Provenienzbereitschaft; es startet keine
Implementierung und ersetzt keine unabhängige technische oder menschliche Abnahme.

| Befund | Reparatur und erneute Bewertung |
|---|---|
| IR901 | Die 17 Quellenänderungen wurden fachlich eingeordnet. Alle 293 Repository-Quellenbindungen in vier erneuerten Receipts sind aktuell; bisherige Quellenreihenfolge erhalten. Resolved. |
| IR902 | Tatsächlich konsumiertes Vorgänger-Receipt und seine Archivkopie sind getrennte, bytegleiche Dateien gemäß kanonischem Vertrag. Alle vier neuen Receipts bestehen; historische Receipts bleiben unverändert. Keine Validatoränderung. Resolved. |
| IR903 | FU-018, Glossar und Selbstbau-Qualitätsregeln verwenden die aktuelle Pin-Register-/Dependabot-Governance in DE/EN. Integritätsziele und manuelle Gates erhalten. Resolved. |

### Vollständige Prüfungsabdeckung

| Mitglied | Inhalt und Übergabe |
|---|---|
| Archivierte GSDB-Bestandsprüfung | Identität, Zielgruppe, zwölf Checklisten, Anwendbarkeit/Evidenz, Open/N/A, priorisierte Lückenliste und menschliche Grenzen geprüft. Keine Neubewertung historischer Kontrollerfüllung. |
| Container-Hardening | Allgemeine Anforderungen, H-344-01–10 und AC-H-344-01–10, zehn Delta-Gruppen, 85 % Branch-/80 % Interface-/UI-Abdeckung, Lieferkette, Daten/Privacy, Presets und offene Übergaben vollständig geprüft. |
| Ubuntu/OpenCode-Web/MSL | Alle FU-001–023/FA-001–012 einschließlich Basis/Architektur, Ausgabepfade, Passwort/Readiness, gemeinsame Clients, sieben Profile, Wrapper, SBOM, Daten/Audit, Sicherheitsbestand, DE/EN und A11Y vollständig geprüft. |
| Unabhängige Selbstprüfung | A-344-/AC-A-344- und A-FU-/AC-A-FU-Verträge verlangen beide abgeschlossenen Vorgänger auf passender gemeinsamer Quellrevision/Image-ID, vollständige FU/FA-Zuordnung und unabhängige risikobasierte Gegenprüfungen ohne Selbstabnahme. |
| Lernenden-Selbstbau | FR-001–015, L-FR-016–023, AC-001–012, L-AC-013–020 einschließlich Fork/Institution, origin/upstream, Selbstbau, sechs Sprachen im Standardprofil all, keine Registry-Verteilung und optionale Template-/Lizenz-/menschliche Gates vollständig geprüft. |

Je Ziel wurden zusätzlich Voraussetzungen/Begriffe, Scope/Nicht-Ziele,
Messbarkeit, Risiken, Referenzen, kopierbare Prompts, Deutsch/Englisch,
textorientierte Status-/Abhängigkeitserklärungen und Lieferautorität geprüft.
Die vier Quellenstand-Nachträge machen historische Versions-/Statusangaben
als Kontext erkennbar und nennen installierte Assurance-0.1.9-Prüfwerkzeuge
bei erhaltener GSDB-3.4.4-Baseline und strengeren menschlichen Risikometadaten.
Vorhandene Resolute-/Web-/Profilimplementierung zuerst bewerten; kein Auftrag
zur Doppelimplementierung. Datierte ARM64-Kandidatennachweise sind keine
vollständige native AMD64-/Windows-/WSL2-, WCAG- oder formale Abnahme.

Fünf Mitglieder, eine Root und fünf bindende Kanten sind konsistent.
GSDB → Hardening; Hardening → Update und Selbstprüfung; Update → Selbstprüfung;
Selbstprüfung → Selbstbau. Reihenfolge und Lifecycle bleiben
Completed/Eligible/Blocked/Blocked/Blocked. Eligible bedeutet Kandidat,
keine Startautorität. Historische Completed-Läufe ersetzen keine aktuelle
Übergabe zum erweiterten Hardening-Intake. Vier portable Rollen, sechs
Collections, de-DE-Namensprofil, kanonischer Index und Legacy-Alias sind konsistent.

### Provenienz, Validierung und Grenzen

Vier Intake-IDs bleiben erhalten. Neue Receipt-/Operations-IDs und
Vorgängerbindungen sind im
[Reparaturnachweis](sandbox-development-lifecycle-2026-11-08-repair-evidence.json)
aufgeführt. 22 Vorgängersicherungen sind bytegleich. Der vorherige
NeedsRemediation-Bericht, sein JSON und der Auftrag sind archiviert;
`supersedes` benennt die ersetzte Bewertung ausdrücklich.

Bash-/PowerShell-Receipt-Prüfungen, Serienmanifest/-Receipt und die
vorhandenen positiven/negativen Lifecycle-Fixtures prüfen die reparierte
Bindung. Die Ergebnisvalidatoren prüfen anschließend das neue Ready auf
aktuelle Ziel-/Auftragshashes. Das ist keine praktische Produktabnahme.

Autor und Reviewer dieser begrenzten Intake-Reparatur sind derselbe Agent.
Dieses vollständige Nachreview ist entsprechend transparent; es behauptet
keine unabhängige technische oder menschliche Abnahme. Die spätere
Unabhängigkeit je selbst implementiertem Hardening-/Update-Anteil bleibt
verbindlich. Kein Risiko wird agentisch akzeptiert.
Keine Feature-Implementierung, Builds, Containeraktionen, Inferenz,
Commit-, Push- oder Remote-Schreiboperationen.

Nächste Aktion, nicht ausgeführt:

```text
$speckit-intake-series-status specs/intake-series/sandbox-development-lifecycle/manifest.json
```

## English

**Outcome: Ready.** The complete five-member series was semantically
re-reviewed after the authorized repair. No open findings at any severity,
accepted risks, unanswered questions or campaign workers. Ready concerns
requirements/provenance readiness, without implementation authority or
independent technical/human acceptance.

IR901 is Resolved: all 17 source changes were assessed and all 293 local
source bindings in four successor receipts are current, preserving inherited
order. IR902 is Resolved: the consumed predecessor receipt and its archival
copy are distinct files with identical bytes, following the canonical
positive/negative contract. Historical receipts are unchanged and validators
were not modified. IR903 is Resolved: FU-018, glossary and learner quality
rules now name current pin-registry/Dependabot governance in both languages,
preserving integrity and manual gates.

Full coverage includes the archived twelve-checklist GSDB assessment;
hardening general/H-344/AC-H-344 requirements and 85%/80% thresholds;
all FU-001–023/FA-001–012; acceptance A-344/AC-A-344 and A-FU/AC-A-FU handoffs;
learner FR-001–015, L-FR-016–023, AC-001–012 and L-AC-013–020.
Audience, prerequisites, terms, scope/non-goals, measurability, risks,
references, prompts, language, text-first states and authority were reviewed
for every target. Acceptance still consumes both completed H/U handoffs on
the same final source/image per profile/architecture, with complete FU/FA
mapping, independent risk-based counterchecks and justified evidence reuse.
Learner standard all retains six languages; optional template, licence and
human gates remain separate from fork/institution self-build.

Current Assurance 0.1.9 is separated from historical 0.1.8 references while
retaining GSDB3.4.4 and stricter human risk metadata. Existing Resolute/Web/
profile work must be assessed before later changes. Dated ARM64 candidate
evidence grants no complete native AMD64/Windows/WSL2, WCAG or formal approval.

Five members, one root and five binding DAG edges are preserved, with
Completed/Eligible/Blocked/Blocked/Blocked lifecycle. H precedes U and A;
U also precedes A; A precedes L; GSDB supplies H's baseline. Eligibility
grants no execution authority. Historical completed runs do not close today's
expanded handoff. Schema2 de-DE roles/collections, canonical index/order and
bounded legacy alias remain consistent.

Intake identities are retained; successor receipts and operation evidence
bind current hashes and 22 exact predecessor snapshots. Prior
NeedsRemediation/report/request are explicitly archived and superseded.
Both-shell receipts, series validators and canonical positive/negative
lifecycle fixtures validate the repair; result validators bind the new
outcome to current targets/request. No product acceptance follows from this.

The same agent repaired and re-reviewed these intake artifacts; no independent
external, technical or human review is claimed. Later portion-specific
independence and human decisions remain mandatory. No risks were accepted.
No feature implementation, builds, runtime, inference, commits, pushes or
remote writes. Next action is the read-only series-status command above.
