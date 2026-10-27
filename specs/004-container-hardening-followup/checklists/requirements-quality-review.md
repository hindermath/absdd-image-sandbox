# Requirements Quality Review / Anforderungsqualitätsreview

**Date**: 2026-10-27
**Scope**: [36 Fragen](requirements-quality.md) anhand ihrer individuellen Hinweise / all 36 questions using their instructions.
**Review type**: agentischer Textreview mit Korrekturen, kein unabhängiger Sicherheits-/Abnahmereview / agent text review with remediation, not independent technical acceptance.
**Baseline commit**: `88ade20` (`docs: plan container hardening and requirements review`).
**Authority**: zuerst Dokumente committen, danach Review/Textkorrekturen ohne weiteren Commit/Push / one initial document commit, then uncommitted review/remediation.

DE: Alle referenzierten Stellen in Spec, Plan, Coverage-Inventar, Datenmodell,
Research und CLI-/Quickstart-Text gelesen. Jeder unten genannte Befund betrifft
geschriebene Anforderungen; kein Testlauf oder vorhandener technischer Erfolg
wurde als Ersatz verwendet. Nach begrenzter Textkorrektur erneut gegen die
betroffenen Fragen gelesen. Der alte Specify-Qualitätsstand in requirements.md
bleibt historisch erhalten und ist nicht dieser aktuelle Review.
EN: Reviewed the referenced specification and planning text for every question.
Findings concern written requirements, never replaced by tests or historical
technical success. Reread affected text after bounded corrections. The prior
Specify quality checklist is preserved as history, not reused as this review.

## Befunde und Korrekturen / Findings and Remediation

| ID | Befund vor Korrektur / Previous gap | Textkorrektur / Correction | Status |
| --- | --- | --- | --- |
| RQ401 | Exporterfolg/Leerdatei und Schutz persistenter Testdaten gegenüber erlaubter Audit-Retention nicht präzise genug / export validity and retained data ambiguous | FR-006/SC-002: nichtleerer zugeordneter aktueller Export, ehrlicher Null-Sitzungsnachweis, UTC-/Dateinamengrenze; US1/SC-002 schützt Projekt-/Agentendaten, nicht absichtlich abgelaufene Metadaten / exact export/date/data scope | Resolved |
| RQ402 | Teilweise Löschung und erneuter Lauf nicht beschrieben / partial deletion/retry unspecified | FR-006, Plan Audit, CLI und Datenmodell: kein Lösch-Rollback behaupten, Restdaten erhalten, Down sperren, neuer Lauf mit neuem Export / honest partial state and safe retry | Resolved |
| RQ403 | Gleichzeitige Stopps/Altsperren und Pfadwechsel nicht ausreichend abgegrenzt / concurrency, stale locks and path drift unclear | FR-006 und Plan: exklusive eigene Sperre vor Export, keine automatische Fremd-/Stale-Entsperrung, Pfad-/Typprüfung, unbewiesene native Sicherheit bleibt Open / owned serialization and explicit proof limits | Resolved |
| RQ404 | Zielgruppenpräzisierung stand nur in neuer Checkliste, nicht ausdrücklich in Spec/Plan / track detail not propagated to spec/plan | Einführung/FR-012 und Plan-Dokumentation: vier Fachrichtungen namentlich und Aufgaben-/Nutzungsbezüge neben weiteren drei Berufen, keine neuen Curricula / named tracks and shared-path mapping | Resolved |
| RQ405 | Modus-/Varianten-Zähleinheit und fehlende Beobachtungen konnten unterschiedlich gelesen werden / interface counting and missing variants ambiguous | FR-003, Coverage-Scope, Datenmodell: je dokumentiertem Modus/kritischem Flow eine ID, alle beanspruchten Varianten, Skips im Nenner; 85 % je Modul, keine Zeilenquote / explicit branch/interface denominator | Resolved |
| RQ406 | CLI-Vorschau verbot jede Dateiöffnung und konnte dadurch erlaubte Konfigurationslektüre ausschließen / preview wording overbroad | CLI/Plan: notwendige Konfiguration read-only, keine Audit-/Agenten-Payloads, keine Sperre oder Schreib-/Runtimeaktionen / distinguish config reads from payload/actions | Resolved |
| RQ407 | Plan-Spec-Hash würde nach Korrektur veralten; datierter Assurance-Pfad brauchte eindeutige Zeitgrenze / stale hash and dated-path interpretation | Plan bindet neuen Spec-Rohhash, benennt historischen Entwurfsstand und reservierten Kontext; echte spätere Zeiten nicht rückdatieren / current spec hash and honest timestamps | Resolved |

DE: Diese Korrekturen erhalten die sieben Owner-Clarifications, 15 FR-IDs,
acht SC-IDs, alle 50 Delta-IDs und Schwellen 30 Tage/85 %/80 %. Keine
Veränderung der Intake-Identität, Reihe, Human-only-Autorität oder erlaubten
Plattform-Teilscope; keine technische Kontrolle wurde damit erfüllt.
EN: Preserve all seven clarifications, requirement/outcome/delta identities
and thresholds. No intake, lifecycle, human authority or bounded-platform
scope changes; textual correction fulfills no technical control.

## Bewertung je Prüfpunkt / Per-Item Assessment

DE: „Erfüllt“ bedeutet ausschließlich ausreichende Anforderungsqualität im
korrigierten Text. Quellen sind Abschnitts-/ID-Verweise, keine behauptete
Runtime-Evidenz. Jede Zeile protokolliert die konkrete Begründung.
EN: Pass means adequate requirement quality in the corrected text only;
references are textual evidence, not runtime proof.

| CHK | Ergebnis / Result | Gelesene Grundlage und Begründung / Basis and rationale |
| --- | --- | --- |
| CHK001 | Pass | Spec Assumptions/FR-001/015 und Plan Delta: neue Identität, historische GAPs und separater Folge-Intake klar / scoped identity and preserved history |
| CHK002 | Pass | FR-002/006 unterscheidet Host-/Container-/Temp-/Volumegrenzen; RQ401 trennt Projekt-/Agentendaten von abgelaufener Audit-Retention / distinct storage/data categories |
| CHK003 | Pass | FR-005 und Plan Agenten nennt sechs Clients, effektive Overrides und getrennte abschaltbare/ungeklärte Updates ohne Loginpflicht / complete client/update scope |
| CHK004 | Pass | FR-004/007/009: Herkunft, Prüfsumme, Lizenz, SBOM und TLS/Krypto getrennt, keine neue Kryptografie / distinct integrity/rights/crypto obligations |
| CHK005 | Pass after RQ401 | FR-006/SC-002 und Plan: einmaliger UTC-Tag, ISO-Dateidatum, strikt älter, genau 30 Tage/Zukunft erhalten / explicit date boundary |
| CHK006 | Pass after RQ401/RQ403 | FR-006/CLI/Plan beschränkt Auswahl auf direkten regulären Dateityp im verifizierten Mount, keine Linkverfolgung / bounded file/path selection |
| CHK007 | Pass after RQ401/RQ402 | FR-006/Plan/CLI: Export, Retention und Down getrennte Erfolge; jeder Vorfehler verhindert Down / explicit phase outcomes |
| CHK008 | Pass after RQ406 | CLI unterscheidet reine Konfigurationslektüre von Payload-/Schreibaktionen; Vorschau ist kein ausgeführter Test / precise zero-action preview |
| CHK009 | Pass after RQ401/RQ402/RQ403/RQ405 | Sieben Clarifications mit FR-002/003/005/006/007 und SC-007 verglichen; Schwellen/Teilscope erhalten, Randfälle präzisiert / clarification consistency |
| CHK010 | Pass | FR-002/Plan Read-only: expliziter Override, Default unverändert, Host-Mounts nicht implizit geschützt / distinct default and optional mode |
| CHK011 | Pass | FR-002/Plan: Default-Egress, lokale Ports und offene Allowlist-Folgearbeit getrennt / inbound/outbound controls not conflated |
| CHK012 | Pass | SC-007/Plan Abschluss/CLI All: ARM64-Handoff bei AMD64-Sperren, keine vollständige Plattform-/Assurance-Abnahme / bounded handoff not full acceptance |
| CHK013 | Pass after RQ405 | FR-003/Coverage/Data Model: alle benannten Module, Inline-/Kindprozesse und fehlende Messung; reine Branchquote je Modul / complete measurement semantics |
| CHK014 | Pass after RQ405 | FR-003/Coverage-Scope: Modus-/Flow-ID, Variantenbelege, feste reviewte Katalogbasis und Skips im Nenner; geänderte Interfaces brauchen beide Fälle / stable counting rules |
| CHK015 | Pass | FR-007/SC-004/Plan: Critical sperrt, High je Fixstatus, konkrete VEX-/Open-Zuordnung ersetzt keine Human-Akzeptanz / exact vulnerability/authority separation |
| CHK016 | Pass | Plan FR-/SC-Tabelle und Delta-Partition: 15 FR, acht SC und 50 eindeutige CL-Zuordnungen, shared Evidence ohne Doppelerfolg / complete traceability |
| CHK017 | Pass | US1-3 Independent Test/Scenarios und Umsetzungsschnitte: MVP eigenständig, Befundbearbeitung einzeln prüfbar, Gesamthandoff abhängig / clear story dependencies |
| CHK018 | Pass | FR-005/006 und Open-Register: synthetische Daten ohne Anmeldung, unbeobachteter Live-Loop/Sitzungsbeleg bleibt offen / honest synthetic/live boundary |
| CHK019 | Pass | Plan Read-only und Quickstart Q5: eigene Kandidaten, synthetische Mounts/Volumes, kein Austausch laufender Lernumgebung / protected live runtime |
| CHK020 | Pass after RQ407 | Spec/Plan/Data Model: neuer Spec-Hash und kausale Quellen-/Image-/Katalog-Revalidierung, keine Historienänderung / current input linkage |
| CHK021 | Pass after RQ401 | FR-006/Plan/CLI: Exit 0 allein nicht genug, fehlende/leere oder falsche Exportdatei verhindert Retention/Down; Null-Sitzungen ohne Fiktion / export validity cases |
| CHK022 | Pass after RQ402 | FR-006/Plan/CLI/Data Model: tatsächliche Teillöschung, kein Rollbackversprechen, neuer Export und idempotenter Restlauf / explicit partial-state recovery |
| CHK023 | Pass after RQ403 | FR-006/Plan: UTC-/Datumsfälle, Pfad-/Typwechsel, eigene exklusive Sperre und unsichere native Grenze Open / race/concurrency scope explicit |
| CHK024 | Pass | FR-013/SC-007/G004-15 bis -17: fehlender Runner Open/Blocked, gleiche Hardware erlaubt, getrennte Laufzeiten/Belege / no copied platform proof |
| CHK025 | Pass | CR-005/Plan Constitution: Python-MSL, begrenzter Shell-Glue, sprachbezogene Argument-/Pfadregeln / justified language boundaries |
| CHK026 | Pass | Spec Architecture und Plan Gates: Trust Boundaries, Datenklassen, STRIDE/CIA/CAPEC, S-ADR/arc42/Zero Trust und SAMM samt Pfaden / concrete architecture evidence |
| CHK027 | Pass | FR-012/SC-006/CR-002/003 und Plan: Kriterien je Artefakt, menschliche Tastatur-/Screenreader-/Rendering-Prüfung separat / no automated WCAG claim |
| CHK028 | Pass after RQ404 | Einführung/FR-012/Plan: alle vier Berufe und vier Fachrichtungen namentlich, gemeinsame Aufgabenbezüge und DE/EN/CEFR-B2-/Erstnutzungsregeln / explicit track coverage |
| CHK029 | Pass after RQ407 | Spec Assumptions/Plan: aktuelle Intake-Quellen separat von neuem Featuretext, autorisierte spätere Rebinds mit Vollreview / freshness versus authority |
| CHK030 | Pass after RQ407 | Plan E/A und Data Model: eindeutige Markdown-/datierte JSON-Pfade, reservierter Kontext ohne Rückdatierungsbehauptung / distinct namespace and actual times |
| CHK031 | Pass | FR-010/Plan 14er-Matrix: Versionen, Prioritäten, aktive DE/EN-Metadaten sowie Quartal/Anlass/3. Oktober mit Owner / exact profile/review obligations |
| CHK032 | Pass | FR-007/008/011 und Register: Produkt/Werkzeug/Organisation, Lizenz-/Provider-/C3A/C5-Entscheidungen rollenbezogen offen / no blanket exemption |
| CHK033 | Pass after RQ406 | CLI FeatureDirectory/Exitklassen: explizite Feature-004-Auswahl, fehlende Gate-Datei Fehler, alte Defaults keine neuen Belege / no historical fallback |
| CHK034 | Pass | FR-005/006/SC-008: session_coverage=not-exported, keine DB/WAL/SHM/Prompt-/Antwortinhalte, tatsächliche Wirkung separat Open / metadata is not session proof |
| CHK035 | Pass | FR-014/Data Model: Anwendbarkeit/Erfüllung getrennt, N/A/Not Assessed, Open-Owner/Aktion/Frist/Trigger und keine fiktive Risikoannahme / exact independent statuses |
| CHK036 | Pass | FR-015/SC-008/Plan Abschluss: Textreview, Handoff, menschliche Freigabe und Folge-Start getrennt / no execution from checklist ticks |

## Ergebnis und verbleibende Grenzen / Outcome and Remaining Limits

### Usability-Nachtrag 2026-10-27 / Usability Amendment

DE: Nach Ausgangscommit `596b4ca` CHK017, CHK021–024, CHK027–029 und
CHK036 erneut anhand ihrer Durchführungshinweise gelesen: FR-012/SC-006
fordern nun einen schlanken Standardpfad ohne Admin-/Schutzumgehung,
sichere Fehlerhilfe und einen getrennten betreuten Pilot. Plan und Quickstart
ordnen Ablauf, synthetischen Fehlerfall, Beobachtungen und Open-Grenzen zu.
Die 36 Fragen bleiben auf Anforderungsqualität beschränkt. Kein Pilot und
keine technische Kontrolle wurden ausgeführt oder als erfüllt markiert.
Die folgenden Aussagen zum damaligen unveränderten 67-Quellen-Stand sind
historischer Reviewkontext; die aktuelle autorisierte Quellenpflege und deren
unabhängiges Vollreview werden separat dokumentiert.
EN: After baseline commit 596b4ca, reread the named items using their review
instructions. FR-012/SC-006 now require a lean ordinary flow without admin or
bypass, safe recovery and a separate supervised pilot. Plan/quickstart define
workflow, synthetic failure, observations and Open boundaries. These 36 checks
still assess writing quality, not executed usability/security acceptance.
The unchanged 67-source statements below describe the earlier review; current
authorized provenance renewal and independent full review are separate records.

DE: 36/36 Fragen nach Textkorrekturen als Anforderungsqualität erfüllt.
Sieben Textbefunde geschlossen. Keine neue offene Scope-/Ownerfrage aus
diesem Textreview; operative Open-Punkte bleiben unverändert wirksam.
Keine unabhängige technische Abnahme, kein Analyze-Ersatz und kein Start
von Tasks/Implementierung oder Folge-Intakes. Nächster Auftrag kann Tasks
erzeugen; anschließend Cross-Artifact-Analyze vor Implementierung.
EN: All 36 requirement-quality questions pass after seven textual corrections.
No new unresolved authoring decision remains; operational Open restrictions
remain effective. This is not independent acceptance or cross-artifact
analysis, and starts no task generation, implementation or downstream intake.

DE: Quellenbindung wird nicht neu geschrieben: die geänderten Feature-
Artefakte sind keine der 67 Inputquellen des Hardening-Receipts. Das
unabhängige Intake-Review wird dadurch weder ersetzt noch zur Bewertung
dieser neuen Spec-/Plan-Korrekturen umgedeutet. Technische Gate-Erfüllung
bleibt Not Assessed, menschliche Freigaben bleiben offen.
EN: No input receipt is rewritten: modified feature artifacts are not among
its 67 sources. Existing independent intake review does not become approval
of these new edits; technical fulfillment and human authorization stay separate.
