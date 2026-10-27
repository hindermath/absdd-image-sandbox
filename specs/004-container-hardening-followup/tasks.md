# Aufgaben: Sandbox-Härtungsnachlauf / Tasks: Sandbox Hardening Follow-Up

**Feature**: `004-container-hardening-followup`
**Branch**: `codex/004-container-hardening-followup`
**Created / Erstellt**: 2026-10-27
**Input baseline / Eingabestand**: `9eb9182` (`docs: refine sandbox usability and intake provenance`).
**Sources / Quellen**: [spec.md](spec.md), [plan.md](plan.md), [research.md](research.md), [data-model.md](data-model.md), [coverage-scope.md](coverage-scope.md), [CLI-Vertrag / CLI contract](contracts/cli.md), [quickstart.md](quickstart.md), [Constitution](../../.specify/memory/constitution.md).

## Auftrag und Leseschlüssel / Authority and Reader Key

DE: Korrekturauftrag vom 2026-10-27 nach Ausgangscommit `cb1965a`:
C1 (DE/EN-Überschriften), I1 (Inventare vor Implementierung) und I2
(serieller Änderungsblock, abschließender Code-Freeze mit Schlussmessung).
Die folgenden Hashes binden die korrigierten Texte. Aufgaben-IDs/Anzahl,
Anforderungen und Sicherheitsgrenzen bleiben erhalten; kein Commit/Push.
EN: Authorized correction after cb1965a covers bilingual headings, inventories
before implementation and serial final changes followed by freeze/measurement.
Hashes below bind corrected text; task identities, scope and security remain.

DE: Historische Erzeugungsgrenze: Diese Datei plant spätere Arbeit. Keine Aufgabe ist ausgeführt. Der Owner
hat nur den vorigen Stand committen und anschließend diese Aufgabenliste
erstellen lassen; kein weiterer Commit/Push, Test, Build, Containerzugriff oder
Implementierungsstart ist damit erlaubt. Keine neue Feature-Spec, kein
Autonomous-Run und keine Wiederaufnahme von Feature 003. Tests werden geplant,
weil Spec FR-003/SC-002/SC-003 sie ausdrücklich verlangen, nicht hier ausgeführt.
EN: Original generation boundary: this file plans future work; no task has run. The owner authorized one
baseline commit followed by this task list only, not another commit/push,
test, build, container action or implementation. Create no new specification
or autonomous run and never resume Feature 003. Tests are planned because
the specification explicitly requires them, not executed now.

DE: Format `- [ ] T### [P] [US#]`: leeres Kästchen = nicht abgeschlossen;
`[P]` = nach erfüllten Voraussetzungen in getrennten Dateien parallel möglich;
`[US#]` = zugehörige User Story. Ohne `[P]` seriell arbeiten. Evidenz ist ein
zuordenbarer Nachweis, ein Gate eine verbindliche Prüfbedingung, eine Fixture
eine künstliche isolierte Testumgebung. Prüfergebnis und Ausführungsrecht sind
verschieden. Pfade sind relativ zur Sandbox-Repo-Wurzel, nicht zu Level 0
oder einem Produktrepo. Neue Pfade unten sind geplante Arbeitsergebnisse.
EN: An unchecked box means incomplete; P permits parallel work in separate
files after prerequisites; US names the story. Work serially otherwise.
Evidence is an attributable record, a gate a required check, and a fixture an
isolated synthetic test environment. Results do not grant execution rights.
Paths are relative to this sandbox repository; new paths are future outputs.

### Geprüfte Eingaben / Validated Inputs

- Hardening-Intake-ID `a92a7ced-bbf3-4408-9754-7b739be19a41`; Receipt `9c16f468-1871-4a4d-9bb7-3d6e50143e6f`, 71 geordnete Quellen / ordered sources.
- Drei aktuelle Receipts, Reihenmanifest und unabhängiges Review `5c452360-9bf7-44d9-84e0-10cae34e72ea`: lesend gültig, Review `Ready`, vier Ziele / three current receipts, valid series and Ready four-target review.
- `spec.md` current raw SHA-256: `2b4c407f2900e1cb97e8c373804e4f66dfb32a5eef2b7ec25b238811801cdf25`.
- `plan.md` current raw SHA-256: `34237fd1cd790dc4fd218f5ed11e27792b4743ae71b64695fd5d67581ffa8f61`.
- `quickstart.md` raw SHA-256: `cd3ca50c739aa8ee3e0eb7a0a5a37f378c7f2553db6730dd6e7342fa7177a5df`.

DE: Research R06 und ältere Eingabehashes dokumentieren den damaligen
67-Quellen-Planungsstand; aktuell gelten 71 Quellen und das erneuerte Review.
Das ist erklärter historischer Kontext, kein Auftrag zur Quellenumschreibung.
Der Skill nennt `setup-tasks.sh`, das hier nicht installiert ist. Der vorhandene
lesende `check-prerequisites.sh --json` löste dieses Feature auf; verwendet wird
`.specify/templates/tasks-template.md`. Optionale before/after-Commit-Hooks
werden ausdrücklich nicht ausgeführt. Sitzungs-/Erzeugungsinformation steht
wegen der auf diese Datei beschränkten Schreibautorität hier, nicht in einem
zusätzlichen neuen Session-Log.
EN: Research R06 and older input hashes record the former 67-source planning
snapshot; current authority uses 71 sources and the renewed review. Do not
rewrite those inputs. The skill's setup-tasks script is absent; the installed
read-only prerequisite resolver identified this feature and the local tasks
template supplies structure. Skip optional commit hooks. Generation/session
information is recorded here because only this file may be created now.

## Verbindliche Arbeitsgrenzen / Mandatory Work Boundaries

DE: Vor späterer Ausführung separate Implementierungsautorität bestätigen;
Runtime, Build, menschliche Teilnahme und Lieferung benötigen ihren jeweiligen
Auftrag. Bereits vorhandene Schutzwirkung zuerst prüfen und aktuelle Belege
wiederverwenden; nur nachgewiesene Lücken ändern. Keine Updates allein wegen
alter Open-Einträge. Die sieben Clarifications, 15 FR, acht SC, 50 Delta-IDs,
14 Presets und Schwellen 30 Tage/85 %/80 % bleiben erhalten.
EN: Obtain separate implementation authority before executing these tasks;
runtime, build, participation and delivery each need appropriate authority.
Assess existing safeguards before changing evidenced gaps only. Preserve all
clarifications, requirement/delta/preset identities and thresholds.

DE: Aktive gebundene Quellen können von späteren Code-/Dokumentationsänderungen
betroffen sein. **Vor der nächsten davon abhängigen Gatebewertung stoppen**,
wenn deren Hashes driften. Nur ein separat autorisiertes Intake-Update mit
byte-identischer Archivierung und unabhängigem Vollreview darf neue Bindungen
herstellen. T001/T075 prüfen das, erneuern aber nichts eigenmächtig. Ebenso
ziehen spätere Änderungen an Code, Interfacekatalog oder Image die betroffenen
Tests/Quoten/Nachweise erneut nach sich. Unabhängige Reviewer schreiben keine
Quellen passend, um einen Pass zu erhalten.
EN: Later changes may affect bound inputs. Stop before dependent gate evaluation
on hash drift; only separately authorized archived intake update and independent
full review can renew bindings. T001/T075 never do that implicitly. Changed
code, interface catalogs or images require affected evidence to be refreshed;
reviewers never rewrite sources to manufacture a pass.

DE: Jeder relevante Checkpoint führt getrennt `Applicable`/`N/A`/`Open` und
`Fulfilled`/`Partly Fulfilled`/`Not Fulfilled`/`Not Assessed`, Begründung,
Evidenzpfad, Owner, Reviewer, Restrisiko, Follow-up, Frist und Trigger. N/A
bleibt Not Assessed und braucht Grund/Trigger. Open/_TODO_ braucht Owner,
konkrete Aktion und Trigger; Rechtsfragen zusätzlich qualifizierten Review
und Frist vor betroffener Nutzung. Ein fehlender Runner ist Open/Blocked,
nicht N/A. Technische Umsetzung startet Not Assessed. Bei Aufgaben, die reale
Ausführung verlangen, ersetzt ein Open-Vermerk niemals das erledigte Kästchen.
Eine vollständig dokumentierte offene Disposition darf hingegen Ergebnis einer
expliziten Bewertungsaufgabe sein, ohne die Kontrolle als erfüllt auszugeben.
EN: Record exact independent applicability and fulfillment states with reasons,
paths, owners, reviewers, risk, follow-up, due dates and triggers. N/A requires
reason/trigger; Open needs owned action, and legal gaps need qualified review
and pre-use deadlines. Missing platforms are not N/A. A documented gap never
completes an execution task, although an explicit assessment task may finish
with an honest Open disposition rather than fulfilled control.

DE: Alle Nachweise binden tatsächliche Revision/Eingabehashes, Runner,
Architektur, Image-ID soweit anwendbar, Zeitpunkt, argv, Exitcode und
Payload-/Entscheidungshashes. Nicht ausgeführt erhält keinen Exit 0. Nur
synthetische Daten; kein DB/WAL/SHM-, Prompt-, Antwort- oder Credential-Export.
OpenCode 2 behält `session_coverage=not-exported`. Kein globales Maintenance,
Machine-Reset, `system prune`, persönlicher Agentenzustand oder laufender
Lerncontainer als Testfixture. Ein Snapshot-Nenner von 104 Dateien ist noch
keine gemessene Coverage. Ein betreuter Pilot ist keine WCAG-/Plattformabnahme.
EN: Bind real inputs, platform, times, arguments, exits and evidence hashes;
never assign successful exits to skipped work. Use synthetic data, no sensitive
payload export, preserve OpenCode's explicit session-coverage limit and protect
the live learner environment. File counts are not coverage and pilots are not
accessibility/platform acceptance.

## Phase 1: Vorbereitung / Setup

**Ziel / Goal:** aktuellen Arbeitsumfang und überprüfbare Baseline herstellen / establish current scope and baseline. Keine neue Anwendung oder Installation / no new application or installation.

- [ ] T001 Prüfe vor Implementierungsbeginn die drei Receipts unter `specs/intake-authoring-receipts/`, `specs/intake-series/sandbox-development-lifecycle/{manifest,receipt}.json`, das aktuelle Ergebnis unter `specs/intake-review-results/sandbox-development-lifecycle.json` und Spec-/Plan-Hashes; protokolliere Autorität, Quelle und Driftstopp in `docs/security/secure-development/004-container-hardening-followup/input-bindings.md`. / Validate current bindings and authority; stop on drift, never renew silently. [FR-001, FR-014, FR-015; SC-001, SC-008; Q1]
- [ ] T002 [P] Erstelle nach T001 `docs/security/secure-development/004-container-hardening-followup/control-matrix.md` aus historischer `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/prioritized-gap-list.md` und `docs/maintenance/intake-gsdb344-delta-2026-10-21.md`: jeden priorisierten In-Scope-GAP aktuell einordnen und exakt 50 eindeutige Delta-IDs mit G01–G10, H-/AC-H-344-01–10, Fassung und Disposition verknüpfen, historische Quellen unverändert. / Map current findings and all fifty deltas without rewriting history or claiming blanket fulfillment. [FR-001, FR-014; SC-001; G004-01]
- [ ] T003 [P] Lege nach T001 `docs/security/secure-development/004-container-hardening-followup/checkpoints.md` als Arbeitsregister aller G004-01–18 und ergänzenden Standards aus Plan an; übernimm N/A-/Open-Gründe und Spec-Open-IDs mit Owner/Review/Frist/Trigger, keine fertigen Abnahmen. / Create the complete applicability and evidence register, not prefilled passes. [FR-014; SC-005, SC-008]
- [ ] T004 Lege in `scripts/tests/fixtures/hardening-followup/README.md` die isolierten HOME-/Projekt-/Registry-/Fake-Compose-/Netzwerkgrenzen und Schreiborte für spätere Tests fest; benenne bei absolut aufgerufenen Binärdateien notwendige echte Isolation statt vermeintlicher PATH-Stubs. / Define safe fixture boundaries, no real maintenance, credentials or learner volumes. [FR-002, FR-003, FR-006; SC-002, SC-003]

## Phase 2: Gemeinsame Voraussetzungen / Foundational

**Blocker / Prerequisite:** T001–T004 müssen vor Story-Arbeit abgeschlossen sein / finish setup before stories.

- [ ] T005 Prüfe `data-model.md` und die bestehende Feature-003-Abgrenzung in `scripts/lib/secure_development_hardening.py` ausschließlich lesend; halte geplante Status-/Pflichtfeld-/Hash-/Kontextfälle in `docs/security/secure-development/004-container-hardening-followup/input-bindings.md` fest. Noch keinen Produktivcode ändern und keine Tests starten; T006–T011 liefern zuerst die reviewten Inventare und den Sicherheitsentwurf, T012 übernimmt die Implementierung. / Review existing contracts read-only and document intended validation cases; no production edits or tests before the reviewed inventories/design. [FR-014, FR-015; SC-001, SC-008]
- [ ] T006 [P] Erzeuge `docs/security/secure-development/004-container-hardening-followup/coverage-modules.json` aus sämtlichen 104 Pfaden in `coverage-scope.md`, einschließlich unveränderter Helfer, Inline-/Patch-/Kindprozesslogik und künftigem Retention-Kern: Quellhash, Sprach-/Entscheidungsmodell, Nenner und Messlücken ausweisen; Inventar unabhängig auf Vollständigkeit reviewen lassen. / Establish the full source-bound module denominator, not only edited files. [FR-003; SC-003; G004-04]
- [ ] T007 [P] Erzeuge `docs/security/secure-development/004-container-hardening-followup/interface-catalog.json` aus README, `docs/man/`, PowerShell-Hilfen und dokumentierten kritischen UI-Flows: eine ID je öffentlichem Modus/Flow, Pflichtvarianten/-plattformen und positive/negative Fälle, keine beliebigen Optionskombinationen als neue IDs; vor Abnahmelauf unabhängig reviewen. / Review a complete logical interface denominator; missing variants stay in scope. [FR-003; SC-002, SC-003]
- [ ] T008 [P] Dokumentiere Kontext-, Deployment-/Bausteinsicht, Qualitätsziele/-szenarien, arc42 §8, ADR-/S-ADR-Verweise, Risiken und technische Schulden in `docs/architecture/004-container-hardening-followup/context-and-decisions.md`; bestehende Entscheidungen zu Rechten, Egress und Retention bewerten statt neu erfinden. / Produce scoped iSAQB architecture evidence using existing decisions where valid. [FR-002, FR-006, FR-014; CR-010/011]
- [ ] T009 [P] Erfasse Host/VM/Container, Mounts, Zustände, Build-/Runtime-Rechte, Paketquellen und optionale Provider als Datenflüsse/Trust Boundaries in `docs/security/secure-development/004-container-hardening-followup/threat-model.md`; CIA, STRIDE, relevante CAPEC-Muster und jedes Egress-Ziel begründet zuordnen, Allowlist nur als owned Open-Follow-up. / Threat-model existing boundaries and outbound flows without introducing an egress ban. [FR-002, FR-005, FR-006; G004-02]
- [ ] T010 Leite nach T008/T009 Default-/Read-only-/Audit-/Agenten-Sicherheitsfälle in `scripts/tests/fixtures/hardening-followup/` ab; speichere nur künstliche Dateibäume, Argumente und Metadaten, mit erwarteter Ablehnung und Erhaltungsumfang je Fall. / Prepare concrete safe acceptance fixtures before narrow changes. [FR-002, FR-003, FR-005, FR-006; SC-002]
- [ ] T011 Dokumentiere Python als MSL und begrenzten Bash-/PowerShell-Glue samt sprachbezogenen Regeln, SSDF-/CWE-Prüfpunkten und didaktischen Kommentaren in `docs/security/secure-development/004-container-hardening-followup/{msl-applicability,secure-coding-review}.md`; keine MSL-Pauschalgarantie, keine neue C#-Anwendung. / Establish language-specific security review and explain nontrivial changed logic. [FR-003; CR-001, CR-005–007; G004-04]
- [ ] T012 Erstelle und reviewe nach T006–T011 zuerst `specs/004-container-hardening-followup/gate-requirements.json` aus G004-01–18, Ergebnissen T002–T011 und Q1–Q8. Implementiere erst danach die geplante Feature-004-Evidenzvalidierung in `scripts/lib/secure_development_hardening.py` mit isolierten Fällen in `scripts/tests/test_hardening_followup.py`: exakte Statuskombinationen/Pflichtfelder, normalisierte versus rohe Hashes, fehlende Belege/Owner/Trigger und alte Kontexte ablehnen, historische Defaults/Fixtures erhalten. Quell-/Kataloghashes nach Änderungen aktualisieren und betroffene Gates nachreviewen, niemals alte Evidence oder Erfolgsvorlagen als Ersatz. / After reviewed inventories/design, first review and bind the feature-local gate contract; only then implement scoped validation/tests and update affected hashes/review without changing legacy acceptance. [FR-003, FR-014, FR-015; SC-001, SC-003, SC-008]

## Phase 3: US1 — Kontrolliert lernen / Learn Within Safe Boundaries (P1, MVP)

**Ziel / Goal:** sicherer, einfacher Standardbetrieb mit datenerhaltendem Audit-Stopp / safe ordinary use and state-preserving audited shutdown.

**Eigenständige Prüfung / Independent verification:** isolierte synthetische
Projekte und Agentenvolumes, Fake-Compose und beide Wrapper zeigen
Schreibgrenzen sowie Export → Retention → Down ohne Providerkonto. Default
und optionale Einschränkung werden unterschieden. Reale Plattformbeobachtung
ist zusätzlich erforderlich, nicht aus Fixtures abzuleiten. / Use isolated
synthetic state and paired-wrapper tests without accounts; distinguish default
and optional restrictions, never equating fixtures with native acceptance.

- [ ] T013 [US1] Ergänze vor Retention-Implementierung `scripts/tests/test_audit_retention.py`: fester UTC-Tag, -31/-30/-29/heute/Zukunft, Monats-/Schaltjahrgrenzen, falsche Namen, abweichende mtime, Unterordner und fremde Dateien; exakt 30 Tage und alle jüngeren Dateien müssen bleiben. / Specify and run isolated date/selection cases before the narrow retention fix. [FR-003, FR-006; SC-002]
- [ ] T014 [US1] Ergänze `scripts/tests/test_audit_storage_metadata.py` und `scripts/tests/test_audit_shutdown_fail_closed.py` um Exit-0-ohne-Datei, leere/falscher-Mount-Datei, aktuelle zuordenbare Tagesdatei und ehrlichen Null-Sitzungsnachweis; keine DB-/WAL-/SHM-/Prompt-/Antwortinhalte lesen. / Cover actual export validity and explicit absent-session boundaries without confidential access. [FR-006; SC-002, SC-008]
- [ ] T015 [US1] Ergänze `scripts/tests/test_audit_shutdown_fail_closed.py` um beide Wrapper, Leerzeichen/Unicode/Optionszeichen, argv-Reihenfolge, unbekannte/fehlende Argumente, konkurrierende/fremde/verwaiste Sperren, Pfad-/Typwechsel, Teil-Löschfehler, Wiederanlauf und echten Down-Exitcode; Vorschau ohne Export/Payload/Sperre/Schreib-/Runtimeaktion. / Exercise the complete paired stop/preview contract in isolated processes without increasing timeouts. [FR-003, FR-006; SC-002]
- [ ] T016 [US1] Ergänze `scripts/tests/test_hardening_followup.py` um Default-/Read-only-Konfigurationsfälle: Non-root, Cap-Drops, no-new-privileges, Loopback-Ports, getrennte Volumes/Mounts und expliziten Override; keine neue Netz-/Dateischutzbehauptung aus read_only ableiten. / Establish isolated configuration expectations before optional hardening. [FR-002, FR-003; SC-002]
- [ ] T017 [US1] Implementiere nach T013–T015 den kleinen gemeinsamen Kern `scripts/lib/audit_retention.py` mit einmaligem UTC-Datum, striktem ISO-Dateinamen, verifiziertem Auditbereich und direkter regulärer Dateiauswahl; Identität/Pfad/Typ vor Entfernung erneut prüfen, Links/Reparse-Points nicht verfolgen und nicht belegbare native Sicherheit fail-closed behandeln. / Implement bounded selection/deletion, not a generic cleanup service or guessed race safety. [FR-003, FR-006; G004-07]
- [ ] T018 [US1] Integriere den Kern atomar in `scripts/compose-down-with-audit.sh` und `scripts/compose-down-with-audit.ps1`: exklusive eigene Sperre je kanonischem Bereich vor Export, aktueller nichtleerer Export, danach Retention und erst dann Down; nur eigenen Lock freigeben, Fehler verhindert Down, normale Nutzung erhält alle sechs Volumes. / Preserve arguments and owned locking/export/retention/down order in both wrappers. [FR-003, FR-006; SC-002]
- [ ] T019 [US1] Ergänze in `scripts/compose-down-with-audit.{sh,ps1}` die redigierten Fehlermeldungen mit Ursache, Phase, tatsächlich entferntem Umfang, Grenzen der Datensicherheitsaussage, sicherem nächsten Schritt und Hilfe; Wiederanlauf braucht neue eigene Sperre/Export, niemals automatische Fremdentsperrung oder behauptetes Rollback. / Make safe failure and idempotent retry understandable without bypass or false preservation promises. [FR-006, FR-012; SC-002, SC-006]
- [ ] T020 [US1] Stelle `Stop-AdeSandboxWithAudit` als Advanced Function mit approved verb `Stop` in `scripts/compose-down-with-audit.ps1` bereit; synchronisiere `--dry-run`/`-WhatIf`, SupportsShouldProcess, vollständige DE/EN-Hilfe und neue `docs/man/stop-ade-sandbox-with-audit.1` mit dem CLI-Vertrag. / Deliver paired preview semantics, approved cmdlet and bilingual help atomically. [FR-003, FR-006, FR-012; CR-002/003]
- [ ] T021 [US1] Bewerte `scripts/audit-export.sh` und `scripts/audit-export.ps1` gegen T014 und korrigiere nur belegte Lücken für aktuellen Export/Nullbestand unter Erhalt des Metadatenformats; `session_coverage=not-exported` bleibt, fehlender Sitzungsnachweis wird UPD-V2-AUDIT statt Datenbankexport. / Reuse metadata exporters; no confidential or invented session evidence. [FR-006; SC-008]
- [ ] T022 [US1] Prüfe `scripts/container-entrypoint.sh` und `scripts/sandbox-lifecycle.{sh,ps1}` auf Umgehung des sicheren Stopppfads und Best-effort-Grenzen; korrigiere nur belegte In-Scope-Lücken und ergänze zugeordnete Fälle in `scripts/tests/test_hardening_followup.py`. / Keep entrypoint best effort distinct from mandatory wrapper export and preserve normal lifecycle behavior. [FR-003, FR-006; SC-002]
- [ ] T023 [US1] Inventarisiere Default-Schreiborte, Benutzer-/Dateirechte, Projekt-Bind-Mounts, temporäre Orte und Agenten-/Build-Volumes aus `Dockerfile`, `compose.yml` und `compose.home-baseline.yml` in `docs/security/secure-development/004-container-hardening-followup/platform-parity.md`; nur aktuell belegte Rechte-Lücken gezielt ändern, keine Schutzabschaltung. / Justify existing writable boundaries and least privilege before changing configuration. [FR-002; G004-02]
- [ ] T024 [US1] Ergänze `compose.read-only.yml` als ausdrücklich optionalen Override nach dem Schreibinventar: erforderliche tmpfs-Orte begründen, Non-root/Capabilities/Portgrenzen erhalten, keine Änderung des beschreibbaren Defaults oder Behauptung schreibgeschützter Host-Mounts; Grenzen in `docs/security/secure-development/004-container-hardening-followup/platform-parity.md` festhalten. / Add only the explicit restrictive profile and its limitations. [FR-002; G004-03]
- [ ] T025 [US1] Erweitere `scripts/test-ade-sandbox-hardening.{sh,ps1}` und `scripts/lib/secure_development_hardening.py` um explizites `--feature-directory`/`-FeatureDirectory` für Feature 004; fehlende/ungültige Inputs und stille alte Evidence-Fallbacks ablehnen, historische Defaults unverändert erhalten und mit `scripts/tests/test_hardening_followup.py` abgrenzen. / Add context selection without rewriting Feature-003 behavior. [FR-003, FR-014; CLI contract]
- [ ] T026 [US1] Synchronisiere `Test-AdeSandboxHardening`, DE/EN-comment-based help und `docs/man/test-ade-sandbox-hardening.1` mit den bestehenden Modi, Vorschau und Exitklassen 0/1/2/3; `All` darf bei fehlenden Pflichtnachweisen keinen Erfolg liefern, Vorschau ist kein Testpass. / Preserve approved cmdlet, paired help and truthful exit meanings. [FR-003, FR-012, FR-014]
- [ ] T027 [US1] Prüfe `scripts/agent-prompt.{sh,ps1}` mit `scripts/tests/test_agent_prompt_dispatchers.py` gegen Argumenterhalt, Projekt-/Agentengrenzen und verbotene Login-/Provider-/Approval-Automation; Änderungen nur bei aktuellem Befund und in beiden Varianten, Mapping und zugehöriger Hilfe atomar. / Verify existing dispatch isolation without enabling providers or bypasses. [FR-003, FR-005; SC-002]
- [ ] T028 [US1] Führe nach den Änderungen T013–T027 die zugeordneten isolierten Q2-/Q3-Regressionsfälle und `podman-compose config` für Default, synthetischen Home-Baseline-Override und optionale Read-only-Datei aus; `scripts/tests/test_secure_development_container_hardening.py` schützt historische Defaults, Ergebnisse/Skips nicht als Runtimebeleg ausgeben. / Validate changed contracts/configuration safely without using the live environment. [FR-002, FR-003, FR-006; SC-002]
- [ ] T029 [US1] Gleiche tatsächliche neue Bedienung mit `docs/fuer-lernende/{erste-schritte,alltag,troubleshooting,lernwege}.md`, `README.md` und `docs/betrieb/validierung-und-wartung.md` ab: ein gewählter Einstieg ohne KI-Konto, Speichern/Stoppen/Wiederöffnen, sichere Hilfe, optionale Read-only-Grenzen; vorhandene passende Texte erhalten, geplante versus installierte Funktionen korrekt benennen. / Update only necessary canonical learner/operations text with DE-first equivalent EN and maintainer-only full acceptance. [FR-012; SC-006]
- [ ] T030 [US1] Erstelle das betreute Pilotprotokoll in `docs/security/secure-development/004-container-hardening-followup/learner-usability-review.md`: Normalablauf und ein synthetischer Sicherheitsfehler, Beobachtungsfelder/Hilfe/Fehlversuche, alle vier IT-Berufe und vier Fachinformatik-Fachrichtungen im Abdeckungsplan; Pilot zunächst Open, Owner Learning/A11Y Review, Follow-up Teilnahme organisieren, Trigger vor unbegleiteter Nutzung. / Plan voluntary supervised observation, not fictitious participation or acceptance. [FR-012; SC-006; G004-14]
- [ ] T031 [US1] Führe isoliert den vertikalen US1-Abnahmefall aus T013–T028 mit künstlichen persistenten Projekt-/Agententestdaten aus; weise keine Löschung bei Exportfehler, strikte 30-Tage-Auswahl und Datenerhalt nach normalem Stopp nach und dokumentiere Phasen-/Teilfehler in `docs/security/secure-development/004-container-hardening-followup/audit-retention-review.md`. / Verify the complete synthetic safety slice, with honest failure/retry scope. [FR-002, FR-003, FR-006; SC-002]
- [ ] T032 [US1] Bewerte den US1-Checkpoint in `docs/security/secure-development/004-container-hardening-followup/checkpoints.md`: sichere Standardabläufe und synthetischer Stopp eigenständig prüfbar, keine Admin-/Schutzumgehung als Komfort; fehlende native Plattform-/Pilotbelege explizit offen und weder globale Freigabe noch US2-Abschluss voraussetzen. / Record bounded MVP value and remaining acceptance gaps separately. [FR-012, FR-014; SC-002, SC-006, SC-008]

## Phase 4: US2 — Aktuelle Lücken gezielt härten / Harden Current Gaps (P2)

**Ziel / Goal:** aktuelle, versionsgebundene Befunde einzeln bewerten und
gezielt schließen, Herkunft und messbare Schutzwirkung zeigen / assess current
findings individually, then remediate with provenance and measured evidence.

**Eigenständige Prüfung / Independent verification:** je Befund Quelle,
Istbeobachtung, positive/negative synthetische Fälle, Datum und Disposition.
Keine neuen Providerkonten oder Modellproben. Ein historisches Open bedeutet
nicht automatisch neue Implementierung. / One finding can be evaluated with
current sources and isolated positive/negative cases, never account setup or
historical Open status as proof of a current defect.

- [ ] T033 [US2] Ergänze gezielte Lückenfälle in `scripts/tests/test_toolchain_version_pins.py`, `scripts/tests/test_container_architecture.py`, `scripts/tests/test_home_baseline_reference_pin.py` und `scripts/tests/test_specify_container_patch.py`: offizielle/native Artefakte, feste Versionen/Digests, erlaubter Maven-Fallback bei gleicher SHA-512-Prüfung und Ablehnung falscher Checksummen, keine echten Builds/Downloads als Unit-Test. / Test current native integrity and fallback boundaries using isolated fixtures. [FR-004; SC-004]
- [ ] T034 [US2] Bewerte Herkunft, Maintainer, Paketregister, Installationsskripte, Content-Hashes und konkrete Lizenzfassungen aus `Dockerfile`, `renovate.json` und `home-baseline.lock.json` in `docs/security/secure-development/004-container-hardening-followup/dependency-audit.md`, einschließlich kritischer öffentlicher Quellen/Scorecard und vorhandener Fixes. / Audit exact current supply-chain provenance; do not repin merely because an old finding exists. [FR-004, FR-007; H-344-04]
- [ ] T035 [US2] Schließe nur durch T033/T034 bestätigte Integritäts-/Pinning-Lücken in `Dockerfile`, `renovate.json` oder betroffenen Installern aus `coverage-scope.md`; pflege erforderliche ARG-Renovate-Metadaten und `docs/security/dependency-update-policy.md` synchron, keine beiläufigen Toolchain-/Lock-Upgrades. / Apply evidence-led narrow integrity fixes and rerun matching isolated cases. [FR-004; SC-004; G004-05]
- [ ] T036 [US2] Inventarisiere die sechs Agenten OpenCode, Codex, Claude, Gemini, Copilot und Antigravity mit tatsächlicher Version, effektiven Konfigurationsebenen, Zustand, Datenfluss und Updatefähigkeit in `docs/security/secure-development/004-container-hardening-followup/agent-security-review.md`; Dateiexistenz und Ignore-Regeln nicht als Wirksamkeitsbeleg verwenden. / Review each installed client separately against current configuration/version. [FR-005; SC-004; G004-06]
- [ ] T037 [US2] Ergänze `scripts/tests/test_opencode_v2_policy.py` und `scripts/tests/fixtures/hardening-followup/` um synthetische globale, Agenten-, Projekt- und Subagent-Overrides, Ausschlüsse, Loop-Grenzen und Fake-Updater; positive/negative Wirkung unterscheiden und nicht testbare Live-Eigenschaften ausdrücklich UPD-V2-LOOP zuordnen. / Exercise effective synthetic policy without sign-in, model calls or invented live evidence. [FR-003, FR-005; SC-004]
- [ ] T038 [US2] Deaktiviere nach T036/T037 nachweislich unterstützte Agenten-Selbstupdates in `Dockerfile`, `compose.yml` oder `opencode.jsonc`; keine ungeprüften Schalter raten, nicht abschaltbare Updates mit Versionsbezug/Negativtest/Nutzungsgrenze in `docs/security/secure-development/004-container-hardening-followup/agent-security-review.md` offen führen; Dockerfile/Renovate bleibt Updateweg. / Disable only supported self-update paths and retain explicit limitations otherwise. [FR-005; SC-004]
- [ ] T039 [US2] Korrigiere nur belegte Override-/Ausschluss-/Zustandslücken in `opencode.jsonc`, `codex/{config,requirements}.toml` oder `compose.yml`; wiederhole zugeordnete synthetische Negative aus T037, erhalte getrennte Volumes, keine pauschale Rechte-/Provider-/Modellkonfiguration. / Remediate effective agent isolation without broadening privileges or claiming unsupported session/loop safety. [FR-002, FR-005; SC-002, SC-004]
- [ ] T040 [US2] Erhalte und führe isoliert REV-TEST-TIMING-Fälle in `scripts/tests/test_linux_maintenance_hardening.py` aus: deterministische Klassifikation plus direkte `/bin/sh`-stderr-/Capability-/Pfadschwärzungs- und reale Timeouttests; `scripts/lib/linux-maintenance-hardening.py`/Wartungswrapper nur bei belegtem Defekt ändern, keine Launcher-Kette oder höheren Timeouts. / Retain real-process and deterministic evidence without weakening timing budgets or running maintenance. [FR-003; SC-003]
- [ ] T041 [US2] Ergänze isolierte Branch-Fixtures der neun Python-Module aus `coverage-scope.md`, `scripts/lib/audit_retention.py` und zugeordneter Inline-/Kindprozesslogik in passenden `scripts/tests/test_*.py`; fehlende Import-/Subprozessmessung in `docs/security/secure-development/004-container-hardening-followup/coverage-modules.json` sichtbar halten. / Cover the full named Python scope, not just edited modules. [FR-003; SC-003]
- [ ] T042 [US2] Ergänze isolierte synthetische Bash-Entscheidungs-/Outcome-Fälle für sämtliche Bash-Pfade in `coverage-scope.md` unter `scripts/tests/fixtures/hardening-followup/` und bestehenden `scripts/tests/test_*.py`; Betrieb/Lifecycle, Downloads/Scanner/Hooks sowie Maintenance/Fleet/Renderer/Core getrennt zuordnen, nie globale Hostaktionen ausführen. / Cover every named shell boundary using source-bound fixtures and safe process isolation. [FR-003; SC-003]
- [ ] T043 [US2] Ergänze entsprechende PowerShell-Entscheidungs-/Outcome-Fälle einschließlich `.psm1` und installierter Vorlagen aus `coverage-scope.md` unter `scripts/tests/fixtures/hardening-followup/`; gepinnte isolierte Messumgebung und echte benötigte native Prozessbelege, Pester-Command-/Zeilenwerte nur ergänzend. / Cover the complete named PowerShell scope without treating line coverage as branch coverage. [FR-003; SC-003]
- [ ] T044 [US2] Ergänze positive/negative Fälle für den vollständigen reviewten Modus-/Flow-Katalog in `docs/security/secure-development/004-container-hardening-followup/interface-catalog.json` und zugeordneten `scripts/tests/`: alle neuen/geänderten Interfaces zu 100 %, übriger Katalog mit ehrlichen fehlenden Varianten, kein künstliches App-/API-Projekt. / Implement executable cases against the actual documented interface denominator. [FR-003; SC-002, SC-003]
- [ ] T045 [US2] Miss nach T040–T044 gemäß Q4 zunächst den Zwischenstand von 85 % Zweig-Outcomes je sicherheitskritischem Modul und 80 % logischen Interfaces mit beiden Fallarten für alle beanspruchten Varianten; sichere temporäre Rohdaten und Hash-/Nenner-/Skips-/Lückenbericht in `docs/security/secure-development/004-container-hardening-followup/secure-coding-review.md`. Dies ist die Lückenbasis für T046, kein finaler Freeze; die verbindliche Schlussmessung folgt in T053 nach T049/T052. / Measure the initial full-scope coverage and gaps without averaged or invented ratios; final acceptance measurement follows all remaining code changes in T053. [FR-003; SC-003; G004-04]
- [ ] T046 [US2] Bearbeite die durch T045 konkret belegten Lücken nur in zugeordneten `scripts/tests/`-Fixtures beziehungsweise sicherheitskritischen Modulen aus `coverage-scope.md`; wiederhole betroffene Messungen nach Quell-/Katalogänderung, aktualisiere `coverage-modules.json`/`interface-catalog.json` im Feature-Evidenzverzeichnis; unerreichte Quote bleibt Abnahmelücke, keine Nennerverkleinerung. / Close evidenced coverage/security gaps without deleting scope or diluting thresholds. [FR-003; SC-003]
- [ ] T047 [US2] Inventarisiere den aktuellen US2-Zwischenstand der TLS-, Signatur-/Kryptoabhängigkeiten, Profilkonflikte, Migration und begründeten Ausnahmen in `docs/security/secure-development/004-container-hardening-followup/crypto-tls-inventory.md`; noch keinen finalen Code-Freeze behaupten. T053 gleicht die Quellen nach T049/T052 erneut ab; keine eigene Kryptografie oder Schlüssel-/Secret-Rotation. / Assess current crypto dependencies serially, retaining Security Review questions; revalidate against the final code in T053. [FR-009; SC-004; G004-10]
- [ ] T048 [US2] Verknüpfe Ergebnisse aus T047 und tatsächlich vorhandene Rechte-/Integritätsmaßnahmen mit `docs/security/secure-development/004-container-hardening-followup/{control-matrix,dependency-audit}.md`; prüfe G04/G07 inklusive begrenzter N/A-Gründe, keine neue rechtliche oder kryptografische Ausnahme ohne zuständige Entscheidung. / Preserve H-344-04/07 rationale and open decisions, not blanket compliance claims. [FR-004, FR-007, FR-009; SC-001, SC-004]
- [ ] T049 [US2] Prüfe seriell `scripts/build-and-sbom.{sh,ps1}` und `scripts/analyze-sbom.{sh,ps1}` mit isolierten Fällen in `scripts/tests/test_hardening_followup.py` gegen explizite unveränderliche Image-/SBOM-Auswahl, Scanner-/DB-Fehler, Argumenterhalt und native Architektur; nur aktuell belegte Lücken vor dem finalen Freeze korrigieren, keine Latest-Datei-Heuristik. T053 muss geänderte Module/Interfaces erneut messen. / Validate and narrowly remediate supply-chain selection serially before the final freeze, followed by affected remeasurement in T053. [FR-003, FR-007; SC-004]
- [ ] T050 [US2] Vergleiche seriell nach T049 genau 14 installierte Presets mit Version, Priorität, Overrides und Kontrollabdeckung gegen die Planmatrix und `scripts/config/spec-kit-project-statistics-governance-presets.json` in `docs/security/secure-development/004-container-hardening-followup/preset-assurance-review.md`; kein neues Profil/Auto-Update, Quartal/Anlass/3. Oktober mit Owner terminieren. / Verify the installed fourteen-preset profile and cadence without incidental installation; the final freeze is established only in T053. [FR-010; SC-005; G004-11]
- [ ] T051 [US2] Ergänze projektspezifische isolierte Assurance-Mutationsfälle in `scripts/tests/test_hardening_followup.py` und `scripts/tests/fixtures/hardening-followup/` gegen die bestehenden Assurance-0.1.8-Prüfer: falsche aktive Version, CL-Dokument-ID, Sammelband-Baseline, Duplikate, Fließtext-only und DE/EN-Widerspruch müssen trotz frisch berechneter Hashes scheitern; auch gültige Positivfälle in Bash/PowerShell. / Test semantics as well as hashes without editing vendored contracts to pass. [FR-010; SC-005]
- [ ] T052 [US2] Integriere die geprüften Feature-004-/Assurance-Bindungen in `scripts/lib/secure_development_hardening.py` und `scripts/test-ade-sandbox-hardening.{sh,ps1}`; gültige JSON-Struktur schließt keine Human-only-/Open-Gates, falsche Metadaten liefern Fehler ohne Evidenzumschreibung, historische Defaults weiter schützen. / Apply contract-aware validation with honest status and no schema fork. [FR-010, FR-014; SC-005, SC-008]
- [ ] T053 [US2] Stelle erst nach T049–T052 und sämtlichen nötigen Korrekturen den finalen US2-Code-/Katalogstand fest: aktualisiere/reviewe `docs/security/secure-development/004-container-hardening-followup/{coverage-modules,interface-catalog}.json`, gleiche T047-Inventar und übrige Versions-/Konfigurationsbelege erneut ab und führe Q2/Q4-Schlussmessung samt Quellen-/Nenner-/Skipsbericht in `secure-coding-review.md` desselben Verzeichnisses durch. Bei weiterer Code-/Katalogkorrektur Freeze aufheben, betroffene Kataloge/Prüfungen/Messungen wiederholen und erst danach neu einfrieren; unerfüllte 85-/80-%-Gates bleiben Open. Konsolidiere anschließend alle G01–G10-/H-/AC-H-344-Zuordnungen in `control-matrix.md`. / Freeze only after all remaining production changes and reviewed catalogs, rerun final regression/coverage and current evidence, and reopen the freeze on further changes; map findings without blanket fulfillment. [FR-001, FR-003, FR-014; SC-001, SC-003, SC-004, SC-005]

## Phase 5: US3 — Nachweise unabhängig beurteilen / Review Evidence Independently (P3)

**Ziel / Goal:** aktuelle technische Belege, offene menschliche Entscheidungen
und Übergabe getrennt reviewen / independently assess evidence, human decisions
and controlled handoff without starting the next intake.

**Eigenständige Prüfung / Independent verification:** ein eingefrorenes Paket
anhand Quellen, IDs, Beleg-/Image-/Runnerbindung und Sperren ohne erneuten Build
reviewen. Fehlende tatsächliche Plattform-/Pilotbeobachtungen bleiben offen.
Der Paketreviewer ist nicht dessen Implementierungsautor. / A different reviewer
can assess the frozen package without rebuilding; missing real observations
stay explicit rather than inferred from successful text checks.

- [ ] T054 [P] [US3] Erstelle nach aktuellem Kontroll-/Datenflussstand `docs/security/secure-development/004-container-hardening-followup/{regulatory-applicability,ai-act-applicability,cra-applicability,nis2-applicability,dora-applicability}.md`: Produkt, Werkzeugbetrieb und Organisation je Land/Rolle, datierte Primärquelle, direkte/vertragliche Pflicht, Anwendungsdatum und zuständigen qualifizierten Review trennen; fehlende Entscheidung Open mit Frist vor betroffener Nutzung. / Prepare legal applicability evidence and owned questions, never invent approvals or training/FOSS exemptions. [FR-008, FR-014; H-344-06; SC-005, SC-008]
- [ ] T055 [P] [US3] Dokumentiere Audit-/Agenten-Datenkategorien, Zweck, Empfänger/Region, Zugriff, Minimierung, Integrität, 30-Tage-Regel, Löschung und Betroffenenrechte in `docs/security/secure-development/004-container-hardening-followup/gdpr-applicability.md`; technische Retentionbelege verlinken, O-344-HUMAN mit Privacy Review und möglichem Vorrang späterer Entscheidung offen halten. / Map privacy by design/default without exporting contents or asserting legal acceptance. [FR-006, FR-008; SC-005, SC-008]
- [ ] T056 [P] [US3] Screen Hosting/Registry/Provider in `docs/security/secure-development/004-container-hardening-followup/{cloud-autonomy-applicability,cloud-compliance-assurance}.md`; O-344-CLOUD gehört Owner/Architecture Review, bei C3A alle 30 Kataloggruppen samt exakten C-/AC-IDs/Variante, SI nur Erklärung; C5 Typ 1/Typ 2/Unknown und Kundenscope unterscheiden. / Assess bounded cloud relevance, supplier claims and independent/customer evidence separately, no automatic C5-to-C3A equivalence. [FR-011; H-344-09; SC-005]
- [ ] T057 [US3] Dokumentiere in `docs/security/secure-development/004-container-hardening-followup/supply-chain-evidence.md` Rechte-/LIC-01-/sonstige LIC-02-Sperren, Providertransparenz, Own-model-AI-SBOM-N/A mit Trigger sowie anwendbare VEX-/SLSA-/Signatur-/Dependency-Track-Prüfung; keine erfundenen Level, Schlüssel, externe Registereinträge oder neue Dienste. / Separate rights, model applicability and supply-chain assurance; retain owned Open restrictions. [FR-007, FR-008; SC-004, SC-005]
- [ ] T058 [US3] Hole vor Q5/Q6 die gesonderte Build-/Runtime-Autorität ein und erfasse dynamischen Podman-Endpunkt, geschützten Container/Image/Volumes, freien Platz, Testprojekt-/Ressourcennamen und synthetische Caches in `docs/security/secure-development/004-container-hardening-followup/platform-parity.md`; bei fehlender Autorität/Voraussetzung blockieren, nichts automatisch starten oder ersetzen. / Secure the native-test boundary without disturbing the learner environment. [FR-002, FR-013; SC-007]
- [ ] T059 [US3] Baue nach T058 einen separaten gecachten ARM64-Kandidaten mit geprüften Inputs und `--pull`, ohne Rosetta-/AMD64-Fallback; prüfe Default/Read-only mit eigenen synthetischen Mounts/Volumes als `adedev`, Rootless-/Capabilities-/Port-/Sprach-/Dokumentations-/JSON-Smokes und beobachtetem VS-Code-Attach; exakte Belege in `docs/security/secure-development/004-container-hardening-followup/platform-macos.md`. / Execute authorized native ARM64 acceptance, not replacement of the live service or mere direct-image smoke as Compose proof. [FR-002, FR-013; SC-002, SC-007; G004-15]
- [ ] T060 [P] [US3] Prüfe nach T058/finalem Code denselben geprüften Git-Head eigenständig auf Windows-Host mit PowerShell 7, Podman-Machine, nativem `linux/amd64`, eigenem Build/Runtime und beobachtetem VS-Code-Zugriff; Befehle/Exits/Zeit/Image/Eingaben in `docs/security/secure-development/004-container-hardening-followup/platform-windows.md`, fehlender Runner = UPD-AMD64 Open/Blocked. / Obtain Windows proof independently; no macOS PowerShell or CI substitute. [FR-013; SC-007; G004-16]
- [ ] T061 [P] [US3] Prüfe nach T058/finalem Code denselben Head separat in Ubuntu/WSL2 mit Checkout im Linux-Dateisystem, Bash/PowerShell 7, UID ungleich 0, eigenem rootless Podman, nativem `linux/amd64`, Build/Runtime und beobachtetem Remote-WSL-/Dev-Containers-Zugriff in `docs/security/secure-development/004-container-hardening-followup/platform-wsl2.md`; kein Windows-Podman-Ergebnis kopieren. / Obtain distinct WSL2 proof; shared hardware is allowed, shared runtime evidence is not. [FR-013; SC-007; G004-17]
- [ ] T062 [US3] Konsolidiere tatsächlich beobachtete Plattformbefunde beziehungsweise genaue Lücken in `docs/security/secure-development/004-container-hardening-followup/platform-parity.md`; prüfe Swift-/Ubuntu-Poppler-Warnungen versionsgenau bei T059–T061, Programmstart gegenüber `swift run`, keine Filter oder PDF-A11Y-Ableitung; UPD-SMOKE-WARN/UPD-AMD64 mit Owner/Trigger erhalten. / Reconcile separate proofs without claiming native Linux hardware or unobserved platform support. [FR-013, FR-014; SC-007]
- [ ] T063 [US3] Erzeuge nach autorisiertem finalem Kandidatenlauf mit `scripts/build-and-sbom.{sh,ps1}` und `scripts/analyze-sbom.{sh,ps1}` genau passende CycloneDX-SBOM und Schwachstellenscan; Image-ID/Architektur/Baueingaben, gepinnte Syft-/Grype-Version und DB-Datum/Hash in `docs/security/secure-development/004-container-hardening-followup/supply-chain-evidence.md`, große Rohartefakte unter ignoriertem `sboms/`, keine Neueste-Datei-Heuristik. / Bind real final-image SBOM/scan to exact inputs and disclose disposable-root scan/network exceptions separately. [FR-007; SC-004]
- [ ] T064 [US3] Ordne jede Critical-/High-CVE aus T063 in `docs/security/secure-development/004-container-hardening-followup/supply-chain-evidence.md` konkret zu: Critical blockiert immer; fixable High braucht Fix, begründetes VEX not_affected oder vollständige Open-Disposition gemäß Clarification; unfixable High bleibt Restrisiko, keine agentische Risikoannahme oder Aufhebung anderer Nutzungssperren. / Apply exact vulnerability gates, not blanket VEX or scan-as-release approval. [FR-007, FR-014; SC-004, SC-008]
- [ ] T065 [US3] Lass Learning/A11Y Review die geänderten Hilfen, Texte und Ausgaben artefaktbezogen gegen WCAG 2.2 AA, `Programmierung #include<everyone>` und Spec CR-002/003 prüfen: Rendering/Reflow/Kontrast, Tastatur, Screenreader, verfügbare Braille, Sprache/Struktur/Fehlerhilfe; Ergebnisse/Gerätelücken in `docs/accessibility/004-container-hardening-followup.md`, kein automatischer Markdown-/PDF-Konformitätsclaim. / Obtain separate human accessibility evidence with explicit unobserved scope. [FR-012; SC-006; G004-14]
- [ ] T066 [US3] Führe nur mit freigegebener synthetischer Umgebung und gesonderter Teilnahme-/Runtime-Autorität das Protokoll aus T030 durch: öffnen, Ausführungsort erkennen, Aufgabe wählen, speichern, auditgesichert stoppen, wieder öffnen, Datei wiederfinden und einen synthetischen Exportfehler sicher klären; reale Beobachtungen in `docs/security/secure-development/004-container-hardening-followup/learner-usability-review.md`, normale Nutzung ohne Admin/BYPASS/Datenverlust, fehlende Zielgruppen-/Plattformbeobachtung bleibt Open. / Run the supervised pilot without credentials, fabricated participation or generalizing a small sample to broad usability/WCAG acceptance. [FR-012; SC-006]
- [ ] T067 [US3] Erzeuge aus realen aktuellen Nachweisen Assurance-0.1.8-Dateien `baseline.json`, `deltas/001-hardening-followup.json`, `closure.json`, `image-impact.json` und `evidence-matrix.md` unter `docs/security/secure-development/2026-10-26-004-container-hardening-followup/`; wahre tatsächliche Zeitstempel trotz reserviertem Pfaddatum, unveränderten ExternalComparison-Vertragswert und Gate `development`, Q7 in beiden Shells, kein Ready bei offenen Pflichtnachweisen. / Create one attributable dated context using installed schema, not backdated proof or altered contract constants. [FR-010, FR-014; SC-005, SC-008]
- [ ] T068 [US3] Lass einen anderen Reviewer als die Implementierungsautoren das eingefrorene Paket T053–T067 einschließlich vollständiger 50er-Matrix, Quoten, Current-/Historiengrenzen, Architektur, Rechts-/Cloud-/Rechte-Disposition und Plattform-/A11Y-/Pilotgrenzen prüfen; stabile Findings, konkrete Rückgabe und erneute begrenzte Prüfung nach Korrekturen in `docs/security/secure-development/004-container-hardening-followup/independent-review.md`. / Obtain independent substantive evidence review; hash validity alone is insufficient and no Ready is forced. [FR-001, FR-014, FR-015; SC-001–SC-008]
- [ ] T069 [US3] Erstelle die kontrollbezogene Übergabe an den gesonderten Intake `Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md` in `docs/security/secure-development/004-container-hardening-followup/handoff.md`: geänderte Flächen, Quellen/Hashes, tatsächliche Belege, fehlende Nachweise, Owner/Frist/Follow-up/Trigger und Nutzungsgrenzen; A darf Mängel an H zurückgeben, weder A noch Lernenden-Selbstbau automatisch starten. / Prepare the independent self-review handoff with explicit remaining restrictions and no new start authority. [FR-014, FR-015; SC-008]
- [ ] T070 [US3] Bewerte den begrenzten technischen Abschluss in `docs/security/secure-development/004-container-hardening-followup/checkpoints.md` und `handoff.md` desselben Verzeichnisses: mindestens echter aktueller ARM64-Beleg, keine Critical-CVE, alle erforderlichen Befunddispositionen; AMD64-/Human-/Pilot-/Coverage-Lücken nicht als erledigte Tests oder Assurance-Gesamtabnahme ausgeben, `All` bleibt bei Pflichtlücken nonzero. / Decide bounded handoff versus blocked full acceptance without relaxing any gate or changing series lifecycle. [FR-007, FR-013, FR-014, FR-015; SC-003, SC-004, SC-007, SC-008]

## Phase 6: Abschluss und spätere Liefergrenzen / Cross-Cutting Closeout

DE: Nach Story-Arbeit Belege finalisieren. Nicht verfügbare Pflichtnachweise
bleiben offene Aufgaben; weder Polish noch lokaler Handoff machen sie grün.
Keine Delivery Authority aus dieser Liste ableiten. / Finalize evidence after
stories; missing mandatory execution stays incomplete. Neither polish nor a
local handoff grants delivery authority or converts gaps into passes.

- [ ] T071 Synchronisiere nach tatsächlichen gemeinsamen Regeländerungen atomar `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.github/agents/copilot-instructions.md` und betroffene aktive `scripts/templates/`/`.specify/templates/`-Ableitungen; lokale Constitution nur bei gesondert autorisierter Grundregeländerung gemeinsam pflegen, sonst begründet unverändert; Ergebnis in `docs/security/secure-development/004-container-hardening-followup/agent-parity-review.md`. / Maintain five-surface semantic parity and approved templates without silently changing governance principles. [FR-012; CR-004; G004-13]
- [ ] T072 Finalisiere genau eine Documentation-Impact-Entscheidung UpdateRequired in `docs/security/secure-development/004-container-hardening-followup/documentation-review.md`, inklusive zugeordnetem JSON-Vertragsnachweis: Zielgruppen/Owner/Kanonik/Navigation, DE/EN/CEFR B2/Erstbegriffe, Command-Ort/Shell/Voraussetzung/Ergebnis/Fehlerhilfe, Distribution als Repo-Doku, Home-sync begründet N/A mit Trigger; vorhandene Lernenden-/Betriebsindizes verlinken aktuelle statt historische Belege. / Complete the documented reader contract, not a second curriculum or registry release. [FR-012; SC-006; CR-013]
- [ ] T073 Führe die betroffenen isolierten Q2-/Q8-Regressions- und Paritäts-/Offline-Link-/Documentation-Impact-Prüfungen aus `quickstart.md`, statisches `podman-compose config`, Pre-Commit und pfadbewussten Secret-Scan aus; protokolliere echte Ergebnisse/Skips in `docs/security/secure-development/004-container-hardening-followup/documentation-review.md`, keine persönlichen `.env`-/Agenten-/Keynote-Daten als Testumfang. / Validate the explicit final scope safely; changed sources require only affected revalidation, never manufactured passes. [FR-003, FR-012, FR-014; SC-006, SC-008]
- [ ] T074 Prüfe Statistikprofil 2 mit `scripts/render-project-statistics.{sh,ps1}` im dokumentierten Check-Modus, aktualisiere bei autorisiertem Bedarf `docs/project-statistics.md` und zugehörige aktive Artefakte; Methodik, manuelle Basis 80 und eingefrorene `docs/project-statistics-pilot/`-Historie erhalten, aktuelle Statistik nicht mit historischer Reproduzierbarkeit verwechseln. / Preserve statistics methodology and frozen evidence; no acceleration claim from this work. [CR-004]
- [ ] T075 Prüfe abschließend erneut aktuelle Bindungen unter `specs/intake-authoring-receipts/`, `specs/intake-review-results/` und `specs/intake-series/sandbox-development-lifecycle/`, Quell-/Interface-/Imagehashes und Evidence-Referenzen in `docs/security/secure-development/004-container-hardening-followup/input-bindings.md`; bei Drift stoppen und separat autorisiertes Update/Review verlangen, Identitäten/Completed→Eligible→Blocked→Blocked nie eigenmächtig ändern. / Verify freshness after all edits; no unauthorized rebinding or copied acceptance. [FR-014, FR-015; SC-008]
- [ ] T076 Erstelle beim tatsächlichen Ende des späteren vollständigen Featurelaufs `specs/004-container-hardening-followup/completion-report.md` anhand `.specify/templates/completion-report-template.md`, einschließlich gitgebundener Umfangszahlen, realem Verlauf, offenem technischem/menschlichem Status und textlicher Ablauf-/Abhängigkeitserklärung; bei Blockade ehrlich Zwischenbericht, keine erfundene Implementierungsfertigstellung. / Report the real full-run outcome, not a planning-only completion. [FR-014, FR-015; SC-008]
- [ ] T077 Erstelle zum Ende der späteren Implementierung `docs/security/agent-session-log/<YYYY-MM-DD-HHMM>.md` mit realem Datum/Zeit, P1-1/P1-5/P3-4-Zuordnung, erledigten/teilweisen/eskalierten Aufgaben, tatsächlichen Prüfungen und unverändert offenen Freigaben; keine vertraulichen Ausgaben und keine rückdatierten Ergebnisse. / Record the actual future session, not present-tense execution of this task list. [FR-014; SC-008]
- [ ] T078 Entferne nach Befundsicherung ausschließlich in T058 inventarisierte eigene Wegwerf-Testcontainer/-Volumes/-Projektdateien, temporäre Messdaten und Kandidatenressourcen soweit entbehrlich; dokumentiere erhaltenen Lerncontainer/Image/Volumes in `docs/security/secure-development/004-container-hardening-followup/platform-parity.md`, kein globales Prune/Reset oder Löschen fremder Daten. / Perform ownership-scoped authorized test cleanup only, not ordinary user-state deletion. [FR-002, FR-006, FR-013; SC-002, SC-007]
- [ ] T079 Prüfe den endgültigen lokalen Handoff-Stand aus `specs/004-container-hardening-followup/` gegen sämtliche FR/SC/H-/AC-H-/G004-Zuordnungen und Reviewerdispositionen in `docs/security/secure-development/004-container-hardening-followup/handoff.md`; nach Änderungen T068 gezielt erneut reviewen lassen, erst danach lokale Übergabe berichten, kein Commit/Push/PR/Merge oder nachfolgender Intake ohne gesonderten Auftrag. / Confirm exact final inputs and restrictions, not implicit delivery authority. [FR-001–FR-015; SC-001–SC-008]
- [ ] T080 **Nur nach gesondert autorisierter Lieferung und vollständig gemergter Featureimplementierung:** die konstitutionell vorgesehene Archivumbenennung von `Lastenheft_Secure-Development-Container-Hardening.md` mit `scripts/rename-lastenheft.{sh,ps1}` unter Erhalt der Intake-/Reihen-/Receipt-/Review-Linie koordiniert durchführen; autorisierten Rename-Commit in dieser Aufgabe nachweisen. Bis dahin ausdrücklich zurückgestellt, kein lokales Implementierungs-, Freigabe- oder Lifecycle-Signal. / Deferred post-merge archival task only; preserve provenance and obtain separate lifecycle/delivery authority before any rename or commit. [Constitution Commit & Pull Request Standards; FR-015]

## Abdeckung / Traceability

DE: Diese Tabellen ordnen geplante Arbeit zu, nicht bestandene Kontrollen.
H-344-NN und AC-H-344-NN bleiben paarweise identisch erhalten. Die genaue
50-ID-Partition aus Plan wird durch T002/T053/T068/T079 vollständig geprüft.
EN: These mappings prove task coverage only. Preserve each intake requirement/
acceptance pair and verify the plan's exact fifty-control partition.

| Requirement | Intake/Gates | Tasks | Success criteria |
| --- | --- | --- | --- |
| FR-001 | H-/AC-H-344-01, G004-01 | T001–T003, T053, T068, T079 | SC-001 |
| FR-002 | G02, G004-02/03 | T004, T008–T010, T016, T023–T024, T028, T031–T032, T058–T062, T078 | SC-002, SC-007 |
| FR-003 | H-/AC-H-344-02, G004-04 | T006–T007, T010–T028, T033, T037, T040–T046, T049, T053, T073 | SC-002, SC-003 |
| FR-004 | H-/AC-H-344-04, G004-05 | T033–T035, T048–T049 | SC-004 |
| FR-005 | H-/AC-H-344-03, G004-06 | T009, T027, T036–T039, T053 | SC-004 |
| FR-006 | H-/AC-H-344-05, G004-07 | T013–T022, T028, T031, T055, T069 | SC-002, SC-008 |
| FR-007 | H-/AC-H-344-04, G004-08 | T034–T035, T048–T049, T057, T063–T064, T070 | SC-004 |
| FR-008 | H-/AC-H-344-06, G004-09 | T054–T055, T057, T068–T070 | SC-005, SC-008 |
| FR-009 | H-/AC-H-344-07, G004-10 | T047–T048, T068 | SC-004 |
| FR-010 | H-/AC-H-344-08, G004-11 | T050–T052, T067–T068 | SC-005 |
| FR-011 | H-/AC-H-344-09, G004-12 | T056, T068–T070 | SC-005 |
| FR-012 | H-/AC-H-344-10, G004-13/14 | T019–T020, T026, T029–T030, T032, T065–T066, T071–T073 | SC-006 |
| FR-013 | G004-15/16/17 | T058–T062, T063, T068–T070, T078 | SC-007 |
| FR-014 | G004-01/18 and all checkpoints | T001–T003, T005, T012, T032, T053–T079 | SC-001, SC-005, SC-008 |
| FR-015 | G004-18 | T001, T005, T012, T068–T070, T075–T076, T079–T080 | SC-008 |

| Intake requirement / Anforderung | Unverändertes Kriterium / Preserved criterion | Zuordnung / Mapping |
| --- | --- | --- |
| H-344-01 | AC-H-344-01 | FR-001/014; T002, T003, T053, T068 |
| H-344-02 | AC-H-344-02 | FR-002/003; T006–T007, T013–T028, T040–T046 |
| H-344-03 | AC-H-344-03 | FR-005; T036–T039 |
| H-344-04 | AC-H-344-04 | FR-004/007; T033–T035, T048–T049, T057, T063–T064 |
| H-344-05 | AC-H-344-05 | FR-006; T013–T022, T031, T055 |
| H-344-06 | AC-H-344-06 | FR-008; T054–T055, T057, T068 |
| H-344-07 | AC-H-344-07 | FR-009; T047–T048 |
| H-344-08 | AC-H-344-08 | FR-010; T050–T052, T067 |
| H-344-09 | AC-H-344-09 | FR-011; T056, T068 |
| H-344-10 | AC-H-344-10 | FR-012; T029–T030, T065–T066, T071–T073 |

| Outcome | Concrete verification tasks / Konkrete Prüfaufgaben |
| --- | --- |
| SC-001 | T002/T053: historische Befunde und genau 50 eindeutige Delta-IDs; T068/T079 unabhängiger/finaler Vergleich / historical disposition and exact delta partition |
| SC-002 | T013–T028/T031: Erhaltungs-/Abbruch-/Argument-/Isolationsfälle; T059–T062 native Grenzen / retention, failure, argument and native isolation evidence |
| SC-003 | T006–T007/T040–T046/T053: vollständige Nenner, Zwischen- und Schlussmessung nach allen Codeänderungen, 85 % je Modul, 80 % Interfaces, 100 % geänderte Interfaces; Skips sichtbar / complete scope and final measurement after all changes |
| SC-004 | T033–T039/T047–T049/T057/T063–T064: Versions-/Herkunfts-/Rechte-/Konfigurations- und finale CVE-Disposition / current origin, rights and vulnerability evidence |
| SC-005 | T003/T050–T057/T067–T068: zehn Gruppen, 14 Presets, aktuelle Assurance-Metadaten und owned Human-/Cloud-Fragen / complete profile and scoped applicability |
| SC-006 | T019–T020/T026/T029–T030/T065–T066/T071–T073: verständliche DE/EN-Nutzung, separate Human-A11Y- und Pilotbelege / readable use and separate actual human observations |
| SC-007 | T058–T062/T068–T070: drei getrennte Pfade, ARM64-Mindestbeleg und explizite AMD64-Sperren / real distinct runtime paths and honest bounded handoff |
| SC-008 | T003/T014–T022/T054–T057/T067–T070/T075–T079: kein Payloadexport, unabhängige Entscheidungen/Übergabe, keine unberechtigte Freigabe / separate authority and evidence |

### Ergänzende Governance-Artefakte / Additional Governance Evidence

DE: T008/T009/T011/T054–T057/T068/T072 ergänzen innerhalb des geplanten
Feature-Evidenzverzeichnisses `zero-trust-applicability.md`,
`samm-assessment.md` und `asvs-verification.md` sowie nötige S-ADRs unter
`docs/security/adr/`. Zero Trust für Grenz-/Remotezugriffe bewerten, SAMM als
begrenzten Verbesserungsplan statt Organisationsreife; neue eigene
Web-/API-/Login-App/ASVS begründet N/A mit Trigger. Security führt regulatorische
Anwendbarkeit, Architecture referenziert statt zweiter Rechtsentscheidung.
SSDF/CWE/Scorecard-Ausgaben brauchen Quellenfassung/Datum, nicht nur Namen.
EN: Produce the additional planned Zero Trust, bounded SAMM and justified
ASVS-N/A records and necessary linked security ADRs. Security owns legal
applicability; architecture references it. Record exact editions/dates and
evidence, not names-only checklists. No new application or cloud service.

## Abhängigkeiten und Parallelität / Dependencies and Parallel Work

DE: Textfolge: T001 → Setup T002–T004 → gemeinsame Grundlagen T005–T012 →
US1 T013–T032 → gezielte US2 T033–T053 → US3-Nachweispaket T054–T070 →
Polish T071–T079. T080 ist **separates späteres Post-Merge-Gate**, nicht
Voraussetzung des lokalen Handoffs. Jede Phase bezieht die stabilen Inputs der
vorigen ein; nach Änderungen nur betroffene Nachweise erneut, niemals alte
Ergebnisse als aktuell kopieren. Bei gleicher Datei serialisieren, unabhängig
von Story oder sichtbarem P-Marker. Nach Polish-Änderungen vor T079 abhängige
Quoten/Hashes und T068-Review aktualisieren. T075 ist zusätzliche Schlussprüfung,
nicht Erlaubnis, bis dahin mit veralteten Quellen zu arbeiten.
EN: Follow setup, foundation, US1, US2, US3 and closeout in that order. T080 is
a separate later post-merge gate, not local-handoff prerequisite. Serialize
shared files. Changed sources invalidate affected measurements and reviews;
T075 never permits using stale inputs earlier.

DE: T005 ist nur lesende Vertragsprüfung mit Dokumentation. T006–T011
erstellen und reviewen die Nenner, Architektur und Sicherheitsfälle, bevor
T012 erstmals Validator-Code ändert oder Tests ausführt. T045 misst bewusst
einen Zwischenstand; T047–T052 laufen seriell und dürfen noch nötige belegte
Produktivkorrekturen enthalten. Erst T053 reviewt die aktualisierten Kataloge,
wiederholt die Schlussmessung und stellt den Freeze für T058–T068 her.
Neu hinzukommende Plattformbelege aus T060/T061 aktualisieren vor T068 auch
Interface-Zähler und Schlussbericht; unbeobachtete Varianten bleiben im Nenner.
Nach T053 erfordert jede Produktiv-/Katalogänderung explizit Rückkehr zu dessen
Review-/Messschritt, bevor Runtime- oder Abnahmenachweise weitergenutzt werden.
EN: T005 is read-only contract assessment with documentation. Reviewed
inventories/design precede the first validator edits/tests in T012. T045 is
intermediate; T047–T052 remain serial and may contain evidenced fixes. Only
T053 reviews updated catalogs, reruns final measurement and freezes the inputs
for runtime/review. Newly obtained platform proof updates interface counts
before T068; missing variants remain in scope. Later production/catalog
changes reopen the T053 review/measurement before reusing affected proof.

DE: US1 bietet ohne US2-/Rechts-/Cloud-Abschluss isoliert prüfbaren Nutzen;
das ist keine allgemeine Betriebsfreigabe. US2 kann jeden Befund unabhängig
bewerten. US3-Paketreview ist ohne neuen Build prüfbar, benötigt aber reale
Belege oder ehrliche Dispositionen aus US1/US2. T060/T061/T065/T066 können bei
fehlender Umgebung/Teilnahme blockiert bleiben. T069/T070 dürfen dann nur die
explizit begrenzte Übergabe mit fortbestehenden Sperren dokumentieren, nicht
diese Ausführungsaufgaben mit X oder Assurance-All mit Erfolg markieren.
EN: US1 has independent testable value, not broad approval. US2 findings are
individually reviewable. US3 package review needs actual prior evidence or
honest gaps, not another build. Missing platform/participant work stays
incomplete; bounded handoff cannot turn those tasks or full assurance green.

| Späterer Block / Future batch | Voraussetzungen / Prerequisites | Zulässige Parallelbeispiele / Disjoint examples |
| --- | --- | --- |
| Setup | T001 abgeschlossen / complete | T002 control-matrix.md und T003 checkpoints.md |
| Grundlagen / Foundation | Setup und T005, gemeinsame Eingaberevision / shared inputs | T006 coverage-modules.json, T007 interface-catalog.json, T008 Architektur, T009 Threat Model; anschließend gemeinsam reviewen / then reconcile |
| US1 | T012; keine gleichzeitigen gemeinsamen Wrapper-/Testdateiänderungen / no concurrent shared-file writes | Bewusst serieller MVP; unmarkierte Tasks nicht parallelisieren / deliberately serial safety slice |
| US2 | T046 als Zwischenstand / intermediate state | T047–T052 seriell; keine parallelen Produktionsänderungen, finaler Freeze und Schlussmessung erst T053 / serial work, final freeze and measurement in T053 |
| US3-Regelreview / governance | finale Kontroll-/Datenflussbasis / final control/flow context | T054 Rechtsregister, T055 Datenschutz, T056 Cloud-Screening, mit getrennten Dateien / separate records |
| US3-Plattformen / platforms | T058 und gleicher finaler Head; separate Runtime/Artefakte / separate runtimes/artifacts | T060 Windows und T061 Ubuntu/WSL2 nur mit getrennten Podman-Laufzeiten und Ressourcen; danach T062 konsolidiert / consolidate afterward |

DE: T049 schreibt die zentrale neue Testsuite und darf daher nicht gleichzeitig
mit T012/T016/T022/T025/T051 laufen. T018/T019/T020 und T025/T026/T052 schreiben
je dieselben öffentlichen Paare und bleiben seriell. T054 schreibt nicht das
Datenschutzdetail von T055. Gemeinsame Kontrollmatrix/Checkpoint-/Statistik-
und Agentenflächen werden nicht parallel verändert. Keine Delegations- oder
Runtime-Erlaubnis wird durch ein P erteilt.
EN: The shared new test suite and paired wrappers are serialized; T054 leaves
T055's privacy detail file alone. Shared matrices, guidance and statistics
have one writer. P never authorizes delegation or runtime actions.

## Umsetzung und Abschluss / Implementation and Completion Strategy

1. DE: Erst separate Implementierungsautorität und später `/speckit-analyze`
   über Spec/Plan/Tasks einholen; T001 erneut vor Änderungen. EN: Obtain
   cross-artifact analysis and separate implementation authority first.
2. DE: Setup/Foundation, dann vertikaler Audit-MVP: vollständige Aufrufkette
   lesen, erforderliche sichere negative Fälle prüfen, nur belegte Lücke
   ändern, Nachweise sichern. EN: Build the narrow safety slice from current
   observations and isolated failures before evidence-led correction.
3. DE: US1-Checkpoint getrennt berichten; danach US2-Befunde einzeln mit
   offenem Nenner/aktuellen Belegen bearbeiten. EN: Report MVP limits, then
   evaluate US2 findings individually with honest measurement scope.
4. DE: Reale native Prüfung und Pilot nur bei eigener Autorität; unabhängigen
   Reviewer, offene Human-Gates und kontrollierte Übergabe separat halten.
   EN: Separate authorized runtime/pilot observation, independent review,
   human decisions and controlled handoff.
5. DE: Lokales Ergebnis mit erledigten/teilweisen/blockierten Tasks und
   Eigentümern/Triggern berichten, keine automatische Lieferung. Erst ein
   späterer ausdrücklich autorisierter Merge kann T080 ermöglichen.
   EN: Report actual local outcomes and owned gaps; no automatic delivery or
   post-merge archival action.

### Zusätzliche eindeutige Dateizuordnung / Additional Explicit File Ownership

DE: Die folgenden Dateien sind verpflichtende Teiloutputs der benannten
Tasks, keine optionalen Hinweise: T008 pflegt nötige featurebezogene S-ADRs
unter `docs/security/adr/`; T009 erstellt
`docs/security/secure-development/004-container-hardening-followup/zero-trust-applicability.md`;
T011 erstellt `docs/security/secure-development/004-container-hardening-followup/asvs-verification.md`
mit begrenztem N/A und Trigger. T030 legt
`docs/security/secure-development/004-container-hardening-followup/samm-assessment.md`
als begrenzte Ist-/Zielverbesserung und Schulungsangebot an, ohne erfundene
Teilnahme oder Reifegrade; T066 ergänzt nur tatsächlich beobachtete Teilnahme.
T072 erstellt `docs/documentation-impact/004-container-hardening-followup.json`
zum genau einen Documentation-Impact-Entscheid und lässt dessen bestehende
Validatoren in T073 prüfen. T055 ist für GDPR zuständig; T054 referenziert
diese Entscheidung, statt eine zweite Datenschutzbewertung zu erzeugen.
EN: These are mandatory named-task outputs, not optional hints: T008 owns
necessary security ADRs, T009 the Zero Trust record, T011 justified ASVS N/A,
T030 bounded SAMM/training-offer evidence without invented maturity or
attendance, and T066 only actual observed participation. T072 creates the
single documentation-impact JSON and T073 validates it. T055 owns GDPR detail;
T054 references that decision instead of duplicating it.

**MVP:** Setup + Foundation + US1; vollständiger späterer Handoff benötigt
zusätzlich die anwendbaren US2-/US3-Nachweise und dokumentierten Grenzen.
/ MVP is setup, foundation and US1; handoff additionally needs applicable
US2/US3 evidence and explicit restrictions.

**Ursprünglicher Erzeugungsumfang / Original Generation Scope:** ausschließlich diese Datei neu;
kein Evidence-Verzeichnis, Gate-JSON, Test oder Runtime-Artefakt erzeugt.
Die historische Feature-003-Studie, Quellenbindungen und Reihenstatus bleiben
unverändert. Der vorhandene fremde Session-Log `2026-10-27-0747.md` bleibt
ausgeschlossen. Optionaler `speckit.git.commit` vor/nach Tasks wird übersprungen;
die Aufgabenliste blieb bei ihrer Erzeugung uncommittet und ungepusht.
