# Aufgaben: Sichere Entwicklungs-Container-Haertung / Tasks: Secure Development Container Hardening

**Eingabe / Input**: Gepruefte Artefakte unter `specs/003-secure-development-container-hardening/` und die sechs in `spec.md` gebundenen Eingaben. / Reviewed artefacts under `specs/003-secure-development-container-hardening/` and the six inputs bound by `spec.md`.

**Organisation / Organization**: Die Aufgaben sind nach Evidenzaufbau, vertikalem Slice, vollstaendiger Gap-Disposition, zwoelf finding-conditioned Arbeitspaketen, finaler Validierung, Dokumentation/A11Y/Paritaet und einem getrennten Orchestrator-Abschluss geordnet. Jeder technische Schreibauftrag nennt Anforderungen und Gap-IDs; reine Querschnittsaufgaben nennen die bindende Gate-ID. / Tasks are ordered by evidence setup, vertical slice, complete gap disposition, twelve finding-conditioned work packages, final validation, documentation/accessibility/parity, and separate orchestrator closeout. Every technical writing task names requirements and gap IDs; cross-cutting work names its binding gate.

## Format: `[ID] [P?] [Story] Beschreibung mit Pfad / Description with path`

- **[P]**: Nur disjunkte Writer mit bereits erfuellten Abhaengigkeiten. / Only disjoint writers whose dependencies are already complete.
- **[US1]–[US5]**: Zuordnung zu den User Stories aus `spec.md`. / Mapping to the user stories in `spec.md`.
- **RED vor GREEN / RED before GREEN**: Ein Befund oder eine absichtlich fehlerhafte Fixture wird sichtbar reproduziert, bevor eine minimale Aenderung und aktuelle Evidenz einen positiven Zustand erlauben.
- **Statusgrenze / Status boundary**: `AcceptedBaseline` schliesst keinen Gap und akzeptiert kein Restrisiko. Fehlende, veraltete oder nicht auf der benoetigten Plattform erzeugte Evidenz bleibt `Open`, niemals `N/A` oder `Pass`.

## Plattform-Scope-Amendment 2026-09-04 / Platform Scope Amendment 2026-09-04

**DE:** `@hindermath` hat als `Repository Owner` und `Security Review` die
Entscheidung `DEC-XPLAT-WSL2-2026-09-04` genehmigt. Fuer Feature 003 ersetzt
Ubuntu unter WSL2 mit eigener rootless-Podman-Laufzeit den zuvor geforderten
separaten nativen Linux-Rechner. T051, T052 und T064 bleiben `[X]`, weil ihre
bisherige Aufgabe, ehrliche `Open`-/`Blocked`-Evidenz anzulegen, abgeschlossen
ist; das ist kein Plattform-Pass. Die spaetere Aktualisierung der realen
externen Evidenz erfolgt vor T066 auf demselben Run und veraendert weder die
Task-Anzahl `85` noch den Stand `65/85`.

**EN:** Acting as `Repository Owner` and `Security Review`, `@hindermath`
approved decision `DEC-XPLAT-WSL2-2026-09-04`. For Feature 003, Ubuntu under
WSL2 with its own rootless Podman runtime replaces the previously required
separate native Linux machine. T051, T052, and T064 remain `[X]` because their
completed scope was to create honest `Open`/`Blocked` evidence; this is not a
platform pass. Real external evidence is updated before T066 in the same run,
without changing the total of `85` tasks or the `65/85` progress state.

## Unveraenderliche Abdeckungsgrenze / Immutable Coverage Boundary

Die Task-Menge erhaelt exakt `GAP-001` bis `GAP-157`: WP01 `001–012`, WP02
`013–025`, WP03 `026–040`, WP04 `041–050`, WP05 `051–063`, WP06 `064–074`,
WP07 `075–086`, WP08 `087–099`, WP09 `100–116`, WP10 `117–133`, WP11
`134–145` und WP12 `146–157`. Das sind `157` Gaps, davon `108`
agentisch bearbeitbar und exakt diese `49` Human-only:

`GAP-011`, `GAP-012`, `GAP-034`, `GAP-035`, `GAP-070`, `GAP-075`–`GAP-086`,
`GAP-100`–`GAP-102`, `GAP-105`, `GAP-106`, `GAP-109`, `GAP-110`, `GAP-113`,
`GAP-115`, `GAP-120`, `GAP-121`, `GAP-124`, `GAP-128`–`GAP-131`,
`GAP-134`–`GAP-146`, `GAP-150`, `GAP-152` und `GAP-155`.

The work packages preserve exactly `GAP-001` through `GAP-157`, with the
unchanged `108/49` partition and the exact Human-only IDs above. Human-only
entries remain `Open`, `Not Assessed`, and `Unassessed` without dated evidence
from their named role.

---

## Phase 1: Preflight und evidence-first Grundlage / Preflight and Evidence-First Foundation

**Zweck / Purpose**: Eingabedrift ausschliessen, den kanonischen 157-Gap-Vertrag aufbauen und zuerst negative Vertragspruefungen sichtbar machen. Diese Phase blockiert jede Produkt- oder Konfigurationsaenderung. / Exclude input drift, build the canonical 157-gap contract, and make negative contract checks visible first. This phase blocks every product or configuration change.

- [X] T001 Pruefe Branch, Run-ID, den fuer den Implementierungsstart revalidierten orchestratorverwalteten Phasenstatus mit abgeschlossenem `analyze`-Ergebnis, alle sechs normalisierten Eingabehashes und die vollstaendig abgehakte Requirements-Checkliste read-only in `specs/003-secure-development-container-hardening/autonomous-run-state.json`, `.specify/runtime/autonomous-routing/8330f54b-97d1-424c-ad1a-842a3fad7be3/analyze.result.json`, `specs/003-secure-development-container-hardening/spec.md` und `specs/003-secure-development-container-hardening/checklists/requirements.md`; stoppe bei Drift und bearbeite den Run-State nicht in der Modellphase (FR-002, FR-004a, AU-001–AU-003, GATE-SPEC-01; keine Abhaengigkeit).
- [X] T002 Lege den DE-first/EN-second Leser- und Evidenzindex mit Scope, Begriffen, Ownern, Human-only-Grenze, N/A-/Open-Regeln und Changed-Path-Mapping in `docs/security/secure-development/2026-08-30-container-hardening/README.md` an (FR-001–FR-004a, FR-018, FR-021, GATE-DIFF-01; depends on T001).
- [X] T003 Initialisiere `docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json` deterministisch aus `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json` mit genau 157 aufsteigenden `Open`/`Not Assessed`/`Unassessed`-Eintraegen, sechs akzeptierten Hashbindungen mit je genau einer Rolle `FeatureIntake`, `IntakeReview`, `SeriesManifest`, `AssessmentResults`, `PrioritisedGapList` und `AcceptanceDecision` sowie unveraenderter 108/49-Partition (FR-001–FR-004a, FR-021–FR-022, GAP-001–GAP-157, GATE-GAP-01; depends on T001–T002).
- [X] T004 Schreibe zuerst positive und negative Vertrags-/Semantiktests und Fixtures fuer fehlende, doppelte und zusaetzliche IDs, falsches `humanOnly`, falsche Human-only- oder Input-Binding-Rollen, ungueltige Statuskombinationen, fehlende Trigger, Zusatzfelder, widerspruechliche N/A-Laufdaten, stale Evidenz, falsche akzeptierte Hashes und nicht reziproke CL-/Evidence-Referenzen in `scripts/tests/test_secure_development_container_hardening.py` und `scripts/tests/fixtures/secure-development-container-hardening/` (FR-001–FR-004a, FR-021, GAP-001–GAP-157, GATE-GAP-01; depends on T003).
- [X] T005 Implementiere den Standardbibliothek-basierten Struktur- und Semantikvalidator mit Pfadbegrenzung, exakt sechs eindeutigen Input-Binding-Rollen, exakter 157/108/49-Pruefung, deterministischen Statusinvarianten, akzeptierten Hashchecks, reziproken Baseline-/CL-/Evidence-Referenzen, Evidenzfrische und Exitcodes 0/1/2/3 in `scripts/lib/secure_development_hardening.py` (FR-001–FR-004a, FR-008, FR-018, FR-021, GAP-001–GAP-157, GATE-GAP-01; depends on T004).
- [X] T006 Implementiere den Bash-Einstieg mit Modi `Input`, `Static`, `Runtime`, `SupplyChain`, `Documentation`, `Accessibility`, `All`, `--dry-run`, `--help`, quotierten Eingaben und unveraenderten Exitcodes in `scripts/test-ade-sandbox-hardening.sh` (FR-004a, FR-008, FR-013, CP-001–CP-004, GAP-087–GAP-099, GAP-117–GAP-133, GATE-PARITY-01; depends on T005).
- [X] T007 Implementiere den semantisch gleichen PowerShell-7-Einstieg als Advanced Function `Test-AdeSandboxHardening` mit `-WhatIf`, DE-first/EN-second Comment Help, `Set-StrictMode -Version Latest` und unveraenderten Exitcodes in `scripts/test-ade-sandbox-hardening.ps1` (FR-004a, FR-008, FR-013, CP-001–CP-004, GAP-087–GAP-099, GAP-117–GAP-133, GATE-PARITY-01; depends on T005–T006).
- [X] T008 Dokumentiere Modusvertrag, Optionen, Exitcodes, sichere Beispiele und Open-Verhalten fuer fehlende Plattformen synchron in `docs/man/test-ade-sandbox-hardening.1` (FR-019, GR-001–GR-004, CP-003–CP-005, GAP-117–GAP-133, GATE-XPLAT-01; depends on T006–T007).
- [X] T009 Ergaenze Schreibwirkungs-, Hilfe-, Modus- und Exitcode-Paritaetstests fuer beide Einstiege in `scripts/tests/test_secure_development_container_hardening.py` (FR-013, FR-020, CP-001–CP-005, GAP-117–GAP-133, GATE-PARITY-01; depends on T006–T008).
- [X] T010 Fuehre `python3 -m unittest scripts.tests.test_secure_development_container_hardening` aus und protokolliere in `docs/security/secure-development/2026-08-30-container-hardening/README.md`, dass jede absichtlich fehlerhafte Fixture vom Validator abgelehnt wird; ein unerwarteter Erfolg ist RED und blockiert T011 (FR-001–FR-004a, GAP-001–GAP-157, GATE-GAP-01; depends on T004–T009).
- [X] T011 Fuehre den Bash- und PowerShell-Inputmodus gegen die echten sechs Dateien aus und schreibe nur tatsaechliche, nicht sensible Laufdaten in `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json`; erwarte sechs Hashmatches und 157/108/49 (FR-001–FR-004a, FR-008, FR-018, GAP-001–GAP-157, GATE-SPEC-01; depends on T010).
- [X] T012 Validiere `docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json` und `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json` strukturell gegen beide Schemas sowie semantisch mit `scripts/lib/secure_development_hardening.py`; unerledigte Applicable-Gates bleiben `Blocked`/`Open`, und die begruendeten N/A-Gates fuer ASVS, Produkt-AI-SBOM, Zero Trust, Cloud/C3A/C5 und Registry/Hosting enthalten exakt ihre Sachgruende und Trigger, aber keine erfundenen Laufdaten (FR-001–FR-004a, FR-018, GAP-001–GAP-157, GATE-GAP-01, GATE-ASVS-NA-01, GATE-AISBOM-NA-01, GATE-ZT-NA-01, GATE-CLOUD-NA-01, GATE-REGISTRY-NA-01; depends on T011).

**Checkpoint**: Kein technischer Gap darf vor T012 positiv dispositioniert oder remediert werden. / No technical gap may be positively dispositioned or remediated before T012.

---

## Phase 2: Repräsentativer Vertical Slice / Representative Vertical Slice (US1, P1)

**Ziel / Goal**: Eine komplette Kette von akzeptiertem Gap ueber Requirement, RED, minimale Aenderung, aktuelle Evidenz, Owner/Reviewer und GREEN beweisen. / Prove one complete chain from accepted gap through requirement, RED, minimal change, current evidence, owner/reviewer, and GREEN.

**Unabhaengiger Test / Independent Test**: Eine fehlende Mount-Evidenz fuer `GAP-147` wird abgelehnt; derselbe Datensatz besteht erst nach einer echten, nicht sensiblen Mount-Pruefung. / Missing mount evidence for `GAP-147` is rejected and the same record passes only after a real non-sensitive mount check.

- [X] T013 [US1] Erzeuge genau eine absichtlich fehlerhafte `GAP-147`-Fixture ohne Mount-Evidenz in `scripts/tests/fixtures/secure-development-container-hardening/gap-147-missing-mount-evidence.json` (FR-002, FR-004a, FR-007, FR-021, GAP-147, GATE-GAP-01; depends on T012).
- [X] T014 [US1] Fuehre den Validator gezielt gegen `scripts/tests/fixtures/secure-development-container-hardening/gap-147-missing-mount-evidence.json` aus und protokolliere erwarteten Nichtnull-Exit sowie die Regel „kein AlreadySatisfied/Fulfilled“ ohne sensible Werte in `docs/security/secure-development/2026-08-30-container-hardening/README.md` (FR-002, FR-004a, FR-007, GAP-147, GATE-GAP-01; depends on T013).
- [X] T015 [US1] Erfasse fuer den Slice `GAP-013`, `GAP-015`, `GAP-020`, `GAP-051`, `GAP-122`, `GAP-147`, `GAP-148`, `GAP-149`, `GAP-154` aktuelle Trust-Boundary-, Least-Privilege-, Supply-Chain-, Secret-, Mount-, State- und Isolationsergebnisse; aendere `Dockerfile`, `compose.yml`, `codex/config.toml`, `codex/requirements.toml` oder `opencode.jsonc` nur bei reproduziertem RED und nur minimal (FR-005–FR-008, FR-012–FR-018, FR-020–FR-022, die neun Slice-Gaps, GATE-STATIC-01; depends on T014).
- [X] T016 [US1] Aktualisiere nur die neun Slice-Eintraege in `docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json` mit Requirement-/Evidence-IDs, Owner `Repository Maintainer`, Reviewer `Security Review`, ehrlichem Status und aktuellem Trigger (FR-001–FR-004a, FR-021, GAP-013, GAP-015, GAP-020, GAP-051, GAP-122, GAP-147–GAP-149, GAP-154, GATE-GAP-01; depends on T015).
- [X] T017 [US1] Wiederhole die gezielten Slice-Tests und den Static-Modus, verifiziere die reziproken Gap-/Requirement-/Evidence-Verweise und schreibe GREEN nur mit aktuellem Befehl, Plattform, Exitcode und Artefakthash in `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json` (FR-002, FR-004a, FR-018, FR-021, die neun Slice-Gaps, GATE-GAP-01; depends on T016).

**Checkpoint**: Der Vertical Slice ist eigenstaendig pruefbar; breite Gap-Arbeit beginnt erst nach seinem GREEN. / The vertical slice is independently testable; broad gap work starts only after its GREEN.

---

## Phase 3: Vollstaendige Gap-Disposition / Complete Gap Disposition (US1, P1)

**Ziel / Goal**: Alle 157 akzeptierten IDs und ihre 108/49-Grenze vollstaendig, reziprok und ohne impliziten Abschluss abbilden. / Map all 157 accepted IDs and the 108/49 boundary completely and reciprocally without implicit closure.

**Unabhaengiger Test / Independent Test**: Der Input-/Gap-Modus meldet exakt 157/108/49 sowie null fehlende, doppelte, extra, falsch zugeordnete oder nicht reziproke IDs. / Input and gap modes report exactly 157/108/49 with zero missing, duplicate, extra, misclassified, or non-reciprocal IDs.

- [X] T018 [US1] Uebertrage CL-IDs, Prioritaet, Human-only-Flag und Rollen fuer alle `GAP-001`–`GAP-157` aus der akzeptierten Baseline in `docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json`, ohne den initialen Status mangels Evidenz positiv zu veraendern (FR-001–FR-004a, FR-021–FR-022, GAP-001–GAP-157, GATE-GAP-01; depends on T017).
- [X] T019 [US1] Erstelle die lesbare Uebergabe fuer exakt 49 Human-only-IDs, gruppiert nach `Privacy/Legal Review`, `Platform Owner/Admin`, `CISO/ISB/KIB` und `Project Owner`, in `docs/security/secure-development/2026-08-30-container-hardening/human-only-handoffs.md`; dokumentiere Fakten, fehlende Entscheidung, Folgeaktion, Trigger und verbotene Agentenaktion, aber keine Freigabe oder Risikoakzeptanz (FR-004, FR-008, FR-021, die 49 Human-only-Gaps, GATE-HUMAN-01; depends on T018).
- [X] T020 [US1] Erweitere die Tests in `scripts/tests/test_secure_development_container_hardening.py` um exakte Rollenlisten, lueckenlose Bereichssummen, reziproke `affectedClIds`, eindeutige Evidence-IDs und Changed-Path-zu-Gap/Requirement-Zuordnung (FR-001, FR-004a, FR-021, GAP-001–GAP-157, GATE-GAP-01, GATE-DIFF-01; depends on T018–T019).
- [X] T021 [US1] Bewerte die 108 agentisch bearbeitbaren Eintraege in `docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json` nur als `AlreadySatisfied`, `FollowUp`, `N/A`, `Open` oder `Applicable`, wenn die jeweilige Statusinvariante und aktuelle Evidenz vorliegt; lasse alle 49 Human-only-Eintraege ohne Rollenbeleg `Open`/`Not Assessed`/`Unassessed` (FR-001–FR-004a, FR-021–FR-022, GAP-001–GAP-157, GATE-GAP-01, GATE-HUMAN-01; depends on T020).
- [X] T022 [US1] Fuehre die Schema-, Semantik-, Input- und Gap-Tests gegen `docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json` aus und protokolliere 157/108/49 sowie null Mappingfehler in `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json` (FR-001–FR-004a, GAP-001–GAP-157, GATE-GAP-01; depends on T021).

---

## Phase 4: Finding-conditioned Haertungsarbeitspakete / Finding-Conditioned Hardening Work Packages

**Arbeitsregel / Work rule**: Jedes Paket beginnt mit gezielter RED-Inspektion. Eine Produkt-, Konfigurations-, Script- oder Dokumentaenderung ist nur zulaessig, wenn diese Inspektion einen aktuellen Gap belegt; andernfalls wird `AlreadySatisfied`, begruendetes `N/A` oder `Open` mit Evidenz/Trigger dokumentiert. Die GREEN-Aufgabe eines Pakets aktualisiert die kanonische Disposition, weshalb die Pakete trotz thematisch disjunkter Analyse nicht als parallele Writer markiert sind. / Each package begins with targeted RED inspection. A change is allowed only for a current finding. The package GREEN task updates the shared canonical disposition, so packages are not marked as parallel writers.

### WP01 Standards und Statusmodell / Standards and Status Model (`GAP-001`–`GAP-012`)

- [X] T023 [US1] Pruefe Standardsanwendbarkeit, MSL, Statusmodell, NIST SSDF, CWE Top 25, ASVS-N/A, AI-SBOM-N/A und regulatorische Human-only-Grenzen gezielt und protokolliere RED/AlreadySatisfied/Open in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp01-standards.md` (FR-001–FR-004a, FR-014–FR-017, FR-021–FR-022, GAP-001–GAP-012; depends on T022).
- [X] T024 [US1] Aktualisiere bei RED minimal `docs/security/msl-applicability.md`, `docs/security/security-checklist.md`, `docs/security/regulatory-applicability.md` und danach die WP01-Eintraege in `docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json`; `GAP-011` und `GAP-012` bleiben ohne Privacy/Legal-Beleg offen (FR-001–FR-004a, FR-014–FR-017, FR-021, GAP-001–GAP-012; depends on T023).

### WP02 Sichere Architektur / Secure Architecture (`GAP-013`–`GAP-025`)

- [X] T025 [US2] Pruefe Kontext, Bausteine, Runtime, Deployment, Trust Boundaries, Isolation, Egress, Qualitaetsszenarien, Architekturentscheidungen, Risiken und Cloud-N/A gezielt und protokolliere RED/AlreadySatisfied/Open in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp02-architecture.md` (FR-006–FR-009, FR-018, FR-021, AR-001–AR-008, GAP-013–GAP-025; depends on T024).
- [X] T026 [US2] Aktualisiere bei RED minimal `docs/architecture/container-hardening.md`, `docs/architecture/container-hardening-quality-scenarios.md`, `docs/security/arc42-security.md`, `docs/security/adr/003-container-isolation.md`, `docs/security/zero-trust-applicability.md`, `docs/security/cloud-autonomy-applicability.md`, `docs/security/cloud-compliance-assurance.md` und die WP02-Dispositionen; technische Aenderungen an `Dockerfile` oder `compose.yml` erfolgen nur bei belegtem Defizit (FR-006–FR-009, FR-018, FR-020–FR-021, AR-001–AR-008, GAP-013–GAP-025; depends on T025).

### WP03 Krypto-Mindestvorgaben / Minimum Cryptography (`GAP-026`–`GAP-040`)

- [X] T027 [US3] Pruefe Download-Hashes, Signatur-/Fingerprint-Pruefung, TLS-Quellen und Abgrenzung eigener Produktkryptografie gezielt und protokolliere RED/N/A/Open in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp03-cryptography.md` (FR-005, FR-008, FR-016–FR-017, FR-021, GAP-026–GAP-040; depends on T026).
- [X] T028 [US3] Aktualisiere bei RED minimal `Dockerfile`, `scripts/build-and-sbom.sh`, `scripts/build-and-sbom.ps1`, `scripts/analyze-sbom.sh`, `scripts/analyze-sbom.ps1`, `docs/security/dependency-audit.md` und die WP03-Dispositionen; `GAP-034`/`GAP-035` bleiben ohne Platform-Owner-Schluesselbeleg offen und keine Schluesselaktion wird ausgefuehrt (FR-005, FR-008, FR-016–FR-017, FR-021, CP-001–CP-004, GAP-026–GAP-040; depends on T027).

### WP04 Bedrohungsmodellierung / Threat Modelling (`GAP-041`–`GAP-050`)

- [X] T029 [US2] Pruefe Assets, CIA, STRIDE, Datenfluesse, Trust Boundaries, Abuse Cases, CAPEC, Massnahmen und offene Restrisiken gezielt und protokolliere RED/AlreadySatisfied/Open in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp04-threat-model.md` (FR-006–FR-009, FR-018, FR-021, AR-002–AR-005, GAP-041–GAP-050; depends on T028).
- [X] T030 [US2] Aktualisiere bei RED minimal `docs/security/threat-model.md`, `docs/security/adr/004-container-threat-boundaries.md`, `docs/security/security-checklist.md` und die WP04-Dispositionen mit textorientierten STRIDE+CIA-/CAPEC-Verweisen; Restrisiko bleibt ohne menschliche Entscheidung unakzeptiert (FR-004, FR-006–FR-009, FR-018, FR-021, AR-002–AR-005, GAP-041–GAP-050; depends on T029).

### WP05 Lieferkette und Build-Integritaet / Supply Chain and Build Integrity (`GAP-051`–`GAP-063`)

- [X] T031 [US3] Fuehre einen gezielten Pin-/Quellen-/Lock-/Lizenz-/Renovate-Audit fuer Basisimage, apt, Go, Rust, Swift, uv, Syft, Spec Kit, Home Baseline und sechs Agentenoberflaechen aus; reproduziere insbesondere Syft-`latest` und ungepinnte Grype/Trivy-Erkennung als RED in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp05-supply-chain.md` (FR-005, FR-010–FR-017, FR-021, GAP-051–GAP-063; depends on T030).
- [X] T032 [US3] Entferne oder pinne bei RED ausschliesslich die belegten beweglichen Quellen in `Dockerfile`, `home-baseline.lock.json`, `renovate.json`, `scripts/build-and-sbom.sh`, `scripts/build-and-sbom.ps1`, `scripts/analyze-sbom.sh`, `scripts/analyze-sbom.ps1`; liefere `New-AdeSandboxSbom`, `--dry-run`/`-WhatIf`, bilinguale Hilfe und `docs/man/new-ade-sandbox-sbom.1`, aktualisiere `docs/security/dependency-audit.md`, `docs/security/supply-chain-evidence.md` und die WP05-Dispositionen (FR-005, FR-010–FR-017, FR-021, CP-001–CP-004, GAP-051–GAP-063; depends on T031).

### WP06 Schwachstellenoffenlegung / Vulnerability Disclosure (`GAP-064`–`GAP-074`)

- [X] T033 [US4] Pruefe CVD-Prozess, `security.txt`, Triage, Patch-/Kommunikationsweg und Uebungsnachweis gezielt und protokolliere RED/AlreadySatisfied/Open in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp06-disclosure.md` (FR-015, FR-017–FR-019, FR-021, GAP-064–GAP-074; depends on T032).
- [X] T034 [US4] Aktualisiere bei RED minimal `SECURITY.md`, `.well-known/security.txt`, `docs/security/vulnerability-disclosure.md`, `docs/security/samm-assessment.md` und die WP06-Dispositionen; `GAP-070` bleibt ohne Privacy/Legal-Entscheidung offen und es erfolgt keine externe Meldung (FR-015, FR-017–FR-019, FR-021, GAP-064–GAP-074; depends on T033).

### WP07 CRA-Anwendbarkeit / CRA Applicability (`GAP-075`–`GAP-086`)

- [X] T035 [US1] Sammle ausschliesslich repositorylokale Produkt-, Distributions- und Lebenszyklusfakten fuer `GAP-075`–`GAP-086` in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp07-cra-facts.md`; fuehre keine Rechtsbewertung, Marktentscheidung oder externe Registeraktion aus (FR-003–FR-004, FR-021, GAP-075–GAP-086, GATE-HUMAN-01; depends on T034).
- [X] T036 [US1] Verlinke die Fakten in `docs/security/regulatory-applicability.md` und `docs/security/secure-development/2026-08-30-container-hardening/human-only-handoffs.md`; halte alle zwoelf WP07-Dispositionen ohne datierten Privacy/Legal-Beleg `Open`/`Not Assessed`/`Unassessed` (FR-003–FR-004, FR-021, GAP-075–GAP-086, GATE-HUMAN-01; depends on T035).

### WP08 Sicherheits-Code-Review / Security Code Review (`GAP-087`–`GAP-099`)

- [X] T037 [US2] Pruefe Eingabe-, Dateipfad-, Subprozess-, Netzwerk-, Fehler-, Log-, Test- und Dependency-Grenzen der geaenderten Python-/Bash-/PowerShell-Logik gezielt gegen sichere Sprachregeln, NIST SSDF und CWE Top 25 und protokolliere RED/AlreadySatisfied/Open in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp08-security-review.md` (FR-005–FR-020, FR-021, GAP-087–GAP-099; depends on T036).
- [X] T038 [US2] Behebe nur belegte WP08-Befunde in `scripts/lib/secure_development_hardening.py`, `scripts/test-ade-sandbox-hardening.sh`, `scripts/test-ade-sandbox-hardening.ps1`, `scripts/tests/test_secure_development_container_hardening.py`, aktualisiere `docs/security/secure-coding-language-rules.md`, `docs/security/security-checklist.md` und die WP08-Dispositionen; keine unabhaengige Bereinigung (FR-005–FR-021, GR-005, GAP-087–GAP-099; depends on T037).

### WP09 KI-Codeerzeugung / AI Code Generation (`GAP-100`–`GAP-116`)

- [X] T039 [US3] Pruefe Werkzeug-/Lieferketteninventar, Provider-/Telemetriegrenzen, Audit-Metadaten, Approval-Verhalten, Agentenstate, Schulung und didaktische Kommentare gezielt und protokolliere RED/AlreadySatisfied/Open in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp09-ai-code-generation.md` (FR-008, FR-010–FR-012, FR-017–FR-019, FR-021, GAP-100–GAP-116; depends on T038).
- [X] T040 [US3] Aktualisiere bei RED minimal `docs/security/ai-tools-inventory.md`, `docs/security/network-decision.md`, `scripts/audit-export.sh`, `scripts/audit-export.ps1`, `codex/config.toml`, `codex/requirements.toml`, `opencode.jsonc`, `docs/fuer-lernende/agenten-und-spec-kit.md` und die WP09-Dispositionen; `GAP-100`–`GAP-102`, `GAP-105`, `GAP-106`, `GAP-109`, `GAP-110`, `GAP-113`, `GAP-115` bleiben ohne Rollenbeleg offen, und keine Anmeldung, Provider-/Modellwahl oder Telemetrieentscheidung wird automatisiert (FR-008, FR-010–FR-012, FR-017–FR-021, GR-005, GAP-100–GAP-116; depends on T039).

### WP10 Sichere Entwicklungsumgebung / Secure Development Environment (`GAP-117`–`GAP-133`)

- [X] T041 [US2] Pruefe Host-/IDE-/VS-Code-Fakten, Compose-Mappings, Secrets, CI-Reproduzierbarkeit, Testdaten, Backup-Grenzen, Bash/PowerShell-Paritaet und Plattformabdeckung gezielt und protokolliere RED/AlreadySatisfied/Open in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp10-development-environment.md` (FR-006–FR-013, FR-017–FR-020, FR-021, CP-001–CP-005, GAP-117–GAP-133; depends on T040).
- [X] T042 [US2] Aktualisiere bei RED minimal `compose.yml`, `compose.home-baseline.yml`, `.devcontainer/devcontainer.json`, `scripts/smoke-test-toolchains.sh`, `scripts/scan-agent-secrets.sh`, `docs/fuer-lernende/vscode-dev-containers.md`, `docs/betrieb/compose-und-speicher.md` und die WP10-Dispositionen; `GAP-120`, `GAP-121`, `GAP-124`, `GAP-128`–`GAP-131` bleiben ohne Platform-Owner-Beleg offen (FR-006–FR-013, FR-017–FR-021, CP-001–CP-005, GAP-117–GAP-133; depends on T041).

### WP11 Datenschutz-Folgenabschaetzung / Data Protection Impact Assessment (`GAP-134`–`GAP-145`)

- [X] T043 [US1] Sammle ausschliesslich repositorylokale Datenfluss-, Datenklassen-, Agentenstate-, Audit- und Empfaengerfakten fuer `GAP-134`–`GAP-145` in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp11-dpia-facts.md`; fuehre keine DPIA-, Datenschutz- oder externe Registerentscheidung aus (FR-003–FR-004, FR-008, FR-021, GAP-134–GAP-145, GATE-HUMAN-01; depends on T042).
- [X] T044 [US1] Verlinke die Fakten in `docs/security/regulatory-applicability.md` und `docs/security/secure-development/2026-08-30-container-hardening/human-only-handoffs.md`; halte alle zwoelf WP11-Dispositionen ohne datierten Privacy/Legal-Beleg `Open`/`Not Assessed`/`Unassessed` (FR-003–FR-004, FR-008, FR-021, GAP-134–GAP-145, GATE-HUMAN-01; depends on T043).

### WP12 Agentische Sandbox / Agentic Sandbox (`GAP-146`–`GAP-157`)

- [X] T045 [US2] Pruefe Compose-Isolation, non-root, Capabilities, Mounts, Schreibpfade, Agentenstate/-Volumes, Netzwerk, Ports, Lifecycle, Audit und Preset-Evidenz gezielt und protokolliere RED/AlreadySatisfied/Open in `docs/security/secure-development/2026-08-30-container-hardening/work-packages/wp12-agentic-sandbox.md` (FR-006–FR-013, FR-018–FR-020, FR-021, AR-001–AR-005, GAP-146–GAP-157; depends on T044).
- [X] T046 [US2] Aktualisiere bei RED minimal `Dockerfile`, `compose.yml`, `codex/config.toml`, `codex/requirements.toml`, `opencode.jsonc`, `docs/security/sandbox-isolation.md`, `docs/security/sandbox-freigabe.md`, `docs/security/network-decision.md`, `scripts/compose-down-with-audit.sh`, `scripts/compose-down-with-audit.ps1` und die WP12-Dispositionen; `GAP-146`, `GAP-150`, `GAP-152`, `GAP-155` bleiben ohne Rollenbeleg offen und freier Egress wird nicht als akzeptiertes Risiko bezeichnet (FR-006–FR-013, FR-018–FR-021, AR-001–AR-005, GAP-146–GAP-157; depends on T045).

**Checkpoint**: Alle zwoelf Bereiche sind ehrlich dispositioniert. Kein Human-only-Punkt wurde geschlossen und keine formale, Secret-, Provider-, Registry-, Plattform- oder Risikoaktion wurde ausgefuehrt. / All twelve ranges are honestly dispositioned; no excluded authority was exercised.

---

## Phase 5: Technische Validierung und finale lokale Image-Evidenz / Technical Validation and Final Local Image Evidence

**Zweck / Purpose**: Zuerst gezielte statische Checks, danach genau eine proportionale finale Build-/Runtime-/Full-Smoke-Sequenz und erst anschliessend genau eine aktuelle SBOM-/Scan-/VEX-/Provenienz-Kette. / Run targeted static checks first, then exactly one proportional final build/runtime/full-smoke sequence, followed by exactly one current SBOM/scan/VEX/provenance chain.

- [X] T047 Fuehre `python3 -m unittest scripts.tests.test_secure_development_container_hardening`, `python3 scripts/check-dockerfile-arg-renovate.py`, `python3 scripts/check-home-baseline-lock.py`, `python3 scripts/tests/test_agent_prompt_dispatchers.py`, `python3 scripts/tests/test_spec_kit_agent_surface_parity.py`, `bash scripts/test-documentation-impact.sh`, den Hardening-`Static`-Modus und `git diff --check` aus; aktualisiere nur reale Ergebnisse in `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json` (FR-004a, FR-005, FR-008, FR-013, FR-017, FR-021, GATE-STATIC-01, GATE-DIFF-01; depends on T046).
- [X] T048 Fuehre `pwsh -NoProfile -File scripts/invoke-psscriptanalyzer.ps1` fuer geaenderte PowerShell-Dateien und ShellCheck fuer geaenderte Bash-Dateien im belegten Host oder spaeteren finalen Container aus; dokumentiere Host-Abwesenheit als `Open`, nicht `Pass`, in `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json` (FR-013, FR-018, CP-001–CP-005, GATE-STATIC-01; depends on T047).
- [X] T049 Fuehre die kanonische statische Compose-Pruefung `podman-compose config` aus und protokolliere das Ergebnis in `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json`; `podman compose config` ist nur eine zusaetzliche Plausibilitaet bei gesundem Socket (FR-006–FR-009, FR-013, FR-018, SC-004, GAP-117–GAP-133, GAP-146–GAP-157, GATE-CONFIG-01; depends on T048).
- [X] T050 Erfasse auf macOS den Bash-Dry-run, PowerShell-`-WhatIf` und verfuegbare praktische Podman-/VS-Code-Ergebnisse in `docs/security/secure-development/2026-08-30-container-hardening/platform-macos.md`; bei fehlender Laufzeit bleibt der Status `Open` mit Owner und Retry-Trigger (FR-004a, FR-013, FR-019–FR-020, CP-001–CP-005, GATE-XPLAT-MAC-01; depends on T049).
- [X] T051 [P] Erfasse fuer Ubuntu unter WSL2 Bash-/PowerShell-Paritaet, einen normalen Linux-Benutzer, eine eigene rootless-Podman-Laufzeit und verfuegbare VS-Code-Ergebnisse in `docs/security/secure-development/2026-08-30-container-hardening/platform-linux.md`; ist dieser Ausfuehrungspfad nicht verfuegbar, schreibe `Open`, Owner und Trigger „erneut bei verfuegbarem Ubuntu-WSL2-Bash-rootless-Podman-Runner“, niemals Windows-Podman-Machine-/macOS-Ersatz oder `N/A` (FR-004a, FR-013, FR-019–FR-020, CP-001–CP-005, GATE-XPLAT-LINUX-01; depends on T049; amended by DEC-XPLAT-WSL2-2026-09-04).
- [X] T052 [P] Erfasse auf dem Windows-Host PowerShell-`-WhatIf`, Windows-Podman-Machine, Runtime und verfuegbare VS-Code-Desktop-Ergebnisse in `docs/security/secure-development/2026-08-30-container-hardening/platform-windows-wsl2.md`; ist kein Runner verfuegbar, schreibe `Open`, Owner und Trigger „erneut bei verfuegbarem Windows-Host-PowerShell7-Podman-Runner“, niemals Ubuntu/WSL2-/macOS-Ersatz oder `N/A` (FR-004a, FR-013, FR-019–FR-020, CP-001–CP-005, GATE-XPLAT-WIN-01; depends on T049; amended by DEC-XPLAT-WSL2-2026-09-04).
- [X] T053 Fuehre genau einmal fuer den finalen technischen Stand `podman compose build --pull`, `podman compose up -d`, `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`, den Hardening-`Runtime`-Modus, die sechs Agenten-Versionen (`opencode`, `codex`, `claude`, `gemini`, `agy`, `copilot`), `agent-prompt --dry-run` ohne Provideraufruf und danach `bash scripts/compose-down-with-audit.sh --podman` aus; binde Build-, Runtime-, 6/6-MSL-, 2/2-Script-, 4/4-Pflichtagenten- und 2/2-Zusatzagenten-Evidenz in `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json` an dieselbe finale lokale Image-ID (FR-005–FR-013, FR-018, FR-020, SC-004–SC-005, GAP-051–GAP-063, GAP-100–GAP-133, GAP-146–GAP-157, GATE-BUILD-01, GATE-RUNTIME-01, GATE-SMOKE-01; depends on T050–T052).
- [X] T054 Erzeuge nach T053 genau eine aktuelle CycloneDX-SBOM mit `bash scripts/build-and-sbom.sh --skip-build`, scanne sie mit dem gepinnten Pfad `bash scripts/analyze-sbom.sh --scan --scanner grype`, gleiche jeden relevanten Fund mit VEX oder offenem Blocker ab und aktualisiere `docs/security/secure-development/2026-08-30-container-hardening/build-provenance.json`, `vulnerability-findings.json`, `vex.cdx.json` sowie `verification-evidence.json`; kein Registry-Push, keine Signatur- oder SLSA-Level-Behauptung (FR-014–FR-018, FR-021, SC-006, GAP-051–GAP-074, GATE-SUPPLY-01; depends on T053).
- [X] T055 Fuehre den Hardening-`SupplyChain`-Modus gegen die finale Image-/SBOM-/Scanner-/VEX-/Provenienz-Kette aus und aktualisiere nur bei aktuellem GREEN die zugehoerigen Dispositionen in `docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json`; Scanner- oder Datenbankausfall bleibt `Open` (FR-004a, FR-014–FR-018, GAP-051–GAP-074, GATE-SUPPLY-01; depends on T054).

---

## Phase 6: Dokumentation, A11Y, Lernenden- und Agentenparitaet / Documentation, A11Y, Learner, and Agent Parity (US5, P2)

**Ziel / Goal**: Die belegte technische Wahrheit fuer alle vier Ausbildungsberufe DE-first/EN-second, CEFR-B2-orientiert, text-first und plattformtreu erklaeren. / Explain the evidenced technical truth for all four training occupations, German first and English second, at CEFR B2, text first, and without platform overclaims.

**Unabhaengiger Test / Independent Test**: Dokumentations-, Accessibility-, Documentation-Impact-, Homogeneity- und Paritaetsvalidatoren bestehen; SC-009 wird nur durch echte `Learning/A11Y Review`-Evidenz erfuellt. / Documentation, accessibility, Documentation Impact, homogeneity, and parity validators pass; SC-009 is met only by real Learning/A11Y Review evidence.

- [X] T056 [US5] Aktualisiere Reader Path, Build, Start, Stop, Mounts, Ports, Netzwerk, Agentenstate, Toolchains, Smoke, SBOM/Scan, sichere Fehlerbehebung und Human-only-Folgeschritt konsistent in `README.md`, `docs/betrieb/README.md`, `docs/betrieb/compose-und-speicher.md`, `docs/betrieb/image-aufbau.md`, `docs/betrieb/validierung-und-wartung.md`, `docs/fuer-lernende/README.md`, `docs/fuer-lernende/erste-schritte.md`, `docs/fuer-lernende/troubleshooting.md` und `docs/fuer-lernende/vscode-dev-containers.md` (FR-019–FR-021, GR-001–GR-003, GR-006, GAP-117–GAP-133, GAP-146–GAP-157, GATE-DOC-01; depends on T055).
- [X] T057 [US5] Erstelle die exakte Documentation-Impact-Entscheidung `UpdateRequired` mit Zielgruppen, Reader Path, kanonischer Quelle/Owner, Navigation, Dokumentklasse, Sprachpartner, Plattformbeleg, Distribution, Home-Sync-Entscheidung, Evidenz, Follow-up und Trigger in `docs/documentation-impact/feature-003-secure-development-container-hardening.json` (FR-019, FR-021, GR-006, GAP-117–GAP-133, GATE-DOC-01; depends on T056).
- [X] T058 [US5] Fuehre `bash scripts/test-documentation-impact.sh`, den Hardening-`Documentation`-Modus und lokale Link-/Command-Plausibilitaetspruefungen aus und aktualisiere `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json`; nicht verfuegbare Plattformbeispiele bleiben `Open` mit Trigger (FR-004a, FR-019–FR-021, GR-006, GATE-DOC-01; depends on T057).
- [X] T059 [US5] Dokumentiere die artefaktbezogene WCAG-2.2-AA-Pruefung, DE-first/EN-second, CEFR B2, Erstbegriffserklaerung, vier Berufe, keine Spec-Kit-Vorerfahrung und vollstaendige Textalternativen in `docs/accessibility/container-hardening.md` (FR-019–FR-020, GR-001–GR-005, SC-008, GAP-100–GAP-133, GATE-A11Y-01; depends on T058).
- [X] T060 [US5] Fuehre `bash scripts/check-homogeneity.sh --dry-run --no-patch "$PWD"` und den Hardening-`Accessibility`-Modus aus; aktualisiere nur beobachtete Ergebnisse in `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json` und behandle fehlende Human-Evidenz als `Blocked`/`Open` (FR-004a, FR-018–FR-020, GR-001–GR-005, GATE-A11Y-01; depends on T059).
- [X] T061 [US5] Bewahre den moderierten, datierten Erstnutzungstest fuer einen spaeteren Lernenden-Rollout. Fuer die bis 31.12.2026 befristete, allein durchgefuehrte und source-only Machbarkeitsstudie validiere stattdessen ausschliesslich `feasibility-study-decision.json`: `NotPerformed`, keine Ersatzdaten und `GATE-LEARNER-01` nur fuer diesen Studienabschluss `N/A`; vor Rollout, Image-Verteilung, produktiver Nutzung oder bei Ablauf wird reale `Learning/A11Y Review`-Evidenz wieder verpflichtend (FR-018–FR-020, GR-001–GR-004, SC-009, GATE-LEARNER-01; depends on T060; amended by DEC-FEASIBILITY-SINGLE-PERSON-2026-09-06).
- [X] T062 [US5] Pruefe gemeinsame Regelanderungen und synchronisiere nur bei tatsaechlicher Shared-Guidance-Wirkung `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.github/agents/copilot-instructions.md`, passende Dateien unter `.specify/templates/`, `scripts/templates/` und `.specify/memory/constitution.md`; projektspezifische Details bleiben mit Begruendung lokal (FR-019–FR-021, AP-001–AP-004, GAP-100–GAP-133, GATE-PARITY-01; depends on T060).
- [X] T063 [US5] Fuehre `bash scripts/install-spec-kit-governance-presets.sh --check-only --preset-config scripts/config/spec-kit-model-routing-governance-presets.json`, `pwsh -NoProfile -File scripts/install-spec-kit-governance-presets.ps1 -CheckOnly -PresetConfig scripts/config/spec-kit-model-routing-governance-presets.json`, `python3 scripts/tests/test_spec_kit_agent_surface_parity.py` und den exakten Hardening-Paritaetsbefehl `python3 scripts/tests/test_secure_development_container_hardening.py` aus und aktualisiere `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json` (FR-012, FR-017–FR-019, AP-001–AP-004, GAP-100–GAP-116, GAP-146–GAP-157, GATE-PARITY-01; depends on T062).
- [X] T064 [US5] Konsolidiere macOS-, Windows-Host- und Ubuntu/WSL2-Ergebnisse ohne Ersatzannahmen in `docs/security/secure-development/2026-08-30-container-hardening/platform-parity.md`; Windows-Host und Ubuntu/WSL2 duerfen dieselbe physische Hardware, aber keine gemeinsame Laufzeit oder wiederverwendete Evidenz nutzen. Ein fehlendes Applicable-Plattformgate bleibt `Open` und blockiert positiven `MergeAndSync`-Abschluss bis zum genannten Runner-Trigger (FR-004a, FR-013, FR-019–FR-020, CP-001–CP-005, GATE-XPLAT-01; depends on T050–T052, T063; amended by DEC-XPLAT-WSL2-2026-09-04).

---

## Phase 7: Modell-Validierung und sicherer Implementierungsrand / Model Validation and Safe Implementation Boundary

**Erlaubte Modellarbeit / Permitted model work**: Bis einschliesslich T069 darf die Modellphase lokale Feature-, Produkt-, Evidenz- und Dokumentationsartefakte bearbeiten und validieren. Sie darf nicht committen, pushen, einen PR oeffnen oder mergen, Admin-Bypass verwenden, die Intake-Serie aendern, auf `main` wechseln, externe Register pflegen, Registry-Artefakte veroeffentlichen, Provider-/Secret-Aktionen ausfuehren oder `specs/003-secure-development-container-hardening/autonomous-run-state.json` bearbeiten. / Through T069, the model phase may edit and validate local feature/product/evidence/documentation artefacts only; all listed delivery and external actions are prohibited.

- [X] T065 Fuehre `uvx pre-commit run --all-files` und `bash scripts/scan-agent-secrets.sh --fail-on-high .` aus, protokolliere keine Trefferwerte und aktualisiere nur das Ergebnis in `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json`; jeder moegliche echte Fund stoppt an der menschlichen Eskalationsgrenze (FR-008, FR-018, FR-021, SC-007, GAP-087–GAP-133, GATE-SECRET-01; depends on T064).
- [X] T066 Fuehre fuer jeden durch expliziten Resume-Audit freigegebenen Kandidaten genau einmal den finalen `bash scripts/test-ade-sandbox-hardening.sh --mode all --evidence docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json` aus; der fruehere fehlgeschlagene Kandidat bleibt belegt und darf erst nach korrigierter Gate-Inventur und Paritaet durch genau einen neuen Resume-Kandidaten ersetzt werden. Erwarte 157/108/49, aktuelle Evidenz fuer alle 108 ehrlichen Zustaende, exakt 49 offene Human-only-Gaps, null erfundene Freigaben, null ungemappte Changed Paths und erneut exakt begruendete N/A-Zeilen fuer alle sechs N/A-Gates einschliesslich der befristeten Machbarkeitsentscheidung fuer `GATE-LEARNER-01` (FR-001–FR-004a, FR-021–FR-022, SC-001–SC-003, GAP-001–GAP-157, GATE-GAP-01, GATE-HUMAN-01, GATE-DIFF-01, GATE-ASVS-NA-01, GATE-AISBOM-NA-01, GATE-ZT-NA-01, GATE-CLOUD-NA-01, GATE-REGISTRY-NA-01, GATE-LEARNER-01; depends on T061, T065; amended by DEC-FEASIBILITY-SINGLE-PERSON-2026-09-06).
- [X] T067 Fuehre `git diff --check` und die read-only Liefermengenpruefung mit `.specify/presets/autonomous-run-governance/scripts/validate-autonomous-delivery-set.sh --repo "$PWD"` plus je einem expliziten `--intended` fuer jede tatsaechlich beabsichtigte ungetrackte Datei aus; dokumentiere null unabhaengige Refactorings in `docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json` (FR-021, SC-010, AU-002–AU-005, GATE-DIFF-01, GATE-DELIVERY-01; depends on T066).
- [X] T068 Schreibe fuer jede Implementierungssitzung eine kurze, nicht sensible Bilanz mit erledigten/teilweisen/eskalierten Plan-IDs, ausgelassenen Plattformchecks samt Grund und Human-only-Grenzen unter `docs/security/agent-session-log/`; behaupte keine kuenftigen Provider-, CI-, Review- oder Freigabefakten (FR-008, FR-018, AU-005–AU-006, GATE-DIFF-01; depends on T067).
- [X] T069 Halte den validierten lokalen Arbeitsbaum als sicheren Modellrand in `specs/003-secure-development-container-hardening/autonomous-run-evidence.md` fest und uebergib ausschliesslich Pfad-/Gate-/Open-Status an den Orchestrator; fuehre keinen Commit, Push, PR, Merge, Bypass, Branchwechsel, State-Edit oder Remote-Schritt aus (FR-018, FR-021, AU-002–AU-005, GATE-DELIVERY-01; depends on T068).

**SICHERER RAND / SAFE BOUNDARY**: Die Modell-Implementierungsphase endet nach T069. T070–T085 sind explizit orchestrator-owned und benoetigen jeweils aktuelle Autoritaet sowie die genannten Gates. / The model implementation phase ends after T069. T070–T085 are explicitly orchestrator-owned and require current authority and gates.

---

## Phase 8: Orchestrator-owned Delivery Closeout

- [X] T070 Revalidiere als Orchestrator Run-ID, Branch `003-secure-development-container-hardening`, `MergeAndSync`-Autoritaet einschliesslich der fuer diesen Run bereits erteilten eng begrenzten Admin-Bypass-Merge-Autoritaet, Stop-/Driftstatus, alle Inputhashes und die exakte Content-Liefermenge read-only mit `.specify/presets/autonomous-run-governance/scripts/validate-autonomous-delivery-set.sh --repo "$PWD"` plus je einem expliziten `--intended` fuer jeden tatsaechlich beabsichtigten ungetrackten Pfad; bearbeite `specs/003-secure-development-container-hardening/autonomous-run-state.json` nur ueber die autorisierten Orchestrator-Wrapper und fordere fuer diesen unveraenderten Run keine zusaetzliche Bypass-Autoritaet an (AU-001–AU-005, GATE-SPEC-01, GATE-DELIVERY-01; depends on T069; orchestrator-owned).
- [X] T071 Stage ausschliesslich den validierten Content-Satz und erstelle den inhaltlichen Commit nach Repositorykonvention; schliesse `docs/project-statistics.md` und reine Statistikartefakte aus diesem Commit aus und validiere vorher erneut Secret-/Diff-Gates in der konkreten Liefermenge (FR-008, FR-021, AU-002, GATE-SECRET-01, GATE-DIFF-01, GATE-DELIVERY-01; depends on T070; orchestrator-owned).
- [X] T072 Rendere erst nach T071 Statistikprofil 2 mit `pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo .`, validiere mit `-CheckOnly` und `git diff --check`, und lasse ausschliesslich Statistikpfade in der Liefermenge `docs/project-statistics.md` sowie gegebenenfalls dem zugehoerigen Profil-2-Ledger zu (GR-007, AU-005, GATE-STATS-01; depends on T071; orchestrator-owned).
- [X] T073 Erstelle einen separaten Statistics-Profile-2-Commit nur fuer die in T072 validierten Statistikpfade; fuehre danach nur die durch diesen Commit betroffenen Diff-, Secret-, Documentation-Impact- und Statistikchecks erneut aus und wiederhole Build/Runtime/Smoke nur bei geaenderter Subject-/Image-Identitaet (GR-007, AU-005, GATE-STATS-01, GATE-DIFF-01; depends on T072; orchestrator-owned).
- [X] T074 Pushe den Feature-Branch ohne Force und oeffne oder aktualisiere den Pull Request mit Content-/Statistik-Trennung, realen Validierungsbefehlen, Secret-/Konfigurationshinweisen, Open-Plattform-/Human-only-Grenzen und ohne Registry-/Providerbehauptungen (AU-002, AU-005, GATE-DELIVERY-01; depends on T073 and current remote-write authority; orchestrator-owned).
- [X] T075 Warte auf CI fuer den exakten gepushten Head, pruefe Checks, Review-Entscheidungen und alle handlungsrelevanten Threads bis zur Konvergenz und wiederhole nur von Aenderungen invalidierte Gates; schreibe keine kuenftigen Provider-/Jobfakten vor ihrer Beobachtung in `specs/003-secure-development-container-hardening/autonomous-run-evidence.md` (FR-004a, AU-002–AU-005, GATE-DELIVERY-01; depends on T074; orchestrator-owned).
- [X] T076 Erzeuge fuer den exakt reviewten Head eine temporaere Schema-2.0-`PreMerge`-Momentaufnahme unter `/tmp/003-container-hardening-premerge.json` mit genau einer Primary-Zeile je Gate und validiere sie mit `.specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh --requirements specs/003-secure-development-container-hardening/autonomous-run-gate-requirements.json --evidence /tmp/003-container-hardening-premerge.json --head <full-reviewed-head>`; committe die Momentaufnahme nicht (FR-004a, AU-002–AU-005, GATE-DELIVERY-01; depends on T075; orchestrator-owned).
- [X] T077 Werte nach T076 die beobachteten Provider-Metadaten fail-closed aus, ohne bereits einen Bypass auszufuehren: Nur wenn der exakte reviewte Head alle technischen Checks gruen hat, kein handlungsrelevanter Review-Thread offen ist, die Schema-2.0-`PreMerge`-Evidenz gueltig ist und `REVIEW_REQUIRED` der einzige verbleibende Policy-Blocker ist, markiere den fuer diesen Run bereits autorisierten Admin-Bypass als fuer T079 zulaessig; bei jedem fehlgeschlagenen, ausstehenden, fehlenden, veralteten oder widerspruechlichen technischen/Security-Gate bleibt der Merge `Blocked`. Fordere keine weitere Autoritaet an und aendere keine Repository-Regel (AU-002–AU-005, GATE-DELIVERY-01; depends on T076; orchestrator-owned).
- [X] T078 Revalidiere unmittelbar vor Merge exakten Head, unveraenderte `MergeAndSync`- und eng begrenzte Admin-Bypass-Autoritaet, aktuelle Primary-Gates, null handlungsrelevante Threads, Content-/Statistik-Commits, den alleinigen Policy-Blocker oder dessen Abwesenheit und die akzeptierte PreMerge-Hashbindung in `/tmp/003-container-hardening-premerge.json`; jedes fehlgeschlagene, ausstehende, fehlende, veraltete oder widerspruechliche technische/Security-Gate blockiert (FR-004a, AU-002–AU-005, GATE-DELIVERY-01; depends on T076–T077; orchestrator-owned).
- [X] T079 Merge den Pull Request ausschliesslich nach erfolgreichem T078 ueber die Provider-Merge-Operation: nutze die normale autorisierte Merge-Methode, wenn kein Policy-Blocker verbleibt; ist `REVIEW_REQUIRED` nachweislich der einzige verbleibende Policy-Blocker, nutze den fuer diesen Run bereits autorisierten Admin-Bypass nur in dieser Merge-Operation. Umgehe niemals ein technisches/Security-Gate, aendere keine Repository-Regel und fuehre keine Registry-, Secret-, Provider-Administrations-, Plattformadministrations- oder Risikoaktion aus (AU-002, AU-005, GATE-DELIVERY-01; depends on T078; orchestrator-owned).
- [X] T080 Wechsle nach beobachtetem Merge auf den Default-Branch, aktualisiere ihn ausschliesslich per Fast-forward auf den realen Merge-Commit und verifiziere dessen Identitaet; kein Reset, Force-Push oder unabhängiger Cleanup (AU-002, AU-005, GATE-DELIVERY-01; depends on T079; orchestrator-owned).
- [X] T081 Erzeuge die kausale Schema-2.0-`PostMerge`-Evidenz in `/tmp/003-container-hardening-postmerge.json`, binde den normalisierten Hash von `/tmp/003-container-hardening-premerge.json` und den realen Merge-Commit, setze `changedPaths` leer und validiere mit `.specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh --requirements specs/003-secure-development-container-hardening/autonomous-run-gate-requirements.json --evidence /tmp/003-container-hardening-postmerge.json --head <full-reviewed-head> --merge-commit <full-merge-commit>`; fuehre keine unabhaengige Nacharbeit aus (FR-018, AU-005, GATE-DELIVERY-01; depends on T080; orchestrator-owned).
- [X] T082 Aktualisiere und validiere den Schema-1.1-Run-State ueber die autorisierten Orchestrator-Wrapper, bis Merge/Publikation, Default-Branch-Sync, deklarierte PostMerge-Aktionen und finale Validierung terminal sind; ein offenes Applicable-Plattform-, Learner-, CI- oder Review-Gate blockiert `Completed` in `specs/003-secure-development-container-hardening/autonomous-run-state.json` (AU-001–AU-005, GATE-DELIVERY-01; depends on T081; orchestrator-owned).
- [X] T083 Entferne erst nach T082 den gemergten lokalen und remote Feature-Branch mit den sicheren Hosting-/Git-Abläufen und belege fuer Default- und Feature-Referenzen lokalen/remote Ahead/Behind-Stand `0/0` in `specs/003-secure-development-container-hardening/autonomous-run-evidence.md` (AU-002, AU-005, GATE-DELIVERY-01; depends on T082; orchestrator-owned).
- [X] T084 Fuehre erst nach validiertem Abschluss die Retrospektive gemaess `speckit-autonomous-retrospective` aus und dokumentiere nur belegte wiederverwendbare Erkenntnisse ohne Provider-/Accountdetails, Secrets, projektspezifische Risikoakzeptanz oder erfundene Remote-Fakten in `specs/003-secure-development-container-hardening/autonomous-run-evidence.md` (AU-006, GATE-DELIVERY-01; depends on T083; orchestrator-owned).
- [X] T085 Schreibe die abschliessende Orchestrator-Sitzungsbilanz mit erledigten, teilweisen und eskalierten Plan-/Feature-IDs unter `docs/security/agent-session-log/`; nenne Open-/N/A-Trigger und tatsaechlich beobachtete Delivery-Fakten, ohne spaetere Intake-Serienfortschreibung zu behaupten (FR-018, AU-005–AU-006, GATE-DELIVERY-01; depends on T084; orchestrator-owned).

**Ausserhalb dieses Feature-Runs / Outside this feature run**: Eine spaetere Advancement-, Update- oder Auswahlaktion fuer `specs/intake-series/sandbox-development-lifecycle/` ist absichtlich keine Aufgabe T001–T085 und benoetigt einen neuen, ausdruecklich autorisierten Lauf. / Any later intake-series advancement, update, or selection is deliberately outside T001–T085 and needs a new explicitly authorized run.

---

## Abhaengigkeiten und Ausfuehrungsreihenfolge / Dependencies and Execution Order

### Phasenabhaengigkeiten / Phase Dependencies

1. **Phase 1** startet read-only und blockiert jede technische Aenderung bis zum gueltigen Input-/Schema-/Semantikvertrag.
2. **Phase 2** haengt von Phase 1 ab und beweist genau einen End-to-End-RED→GREEN-Slice.
3. **Phase 3** haengt vom Slice ab und baut die vollstaendige 157/108/49-Disposition auf.
4. **Phase 4** bearbeitet WP01→WP12 in dieser Reihenfolge. Analyse darf vorbereitet werden; GREEN und Shared-JSON-Schreiben bleiben sequenziell.
5. **Phase 5** beginnt nach allen finding-conditioned Paketen. Statisch→Config→Plattform→ein finaler Build/Runtime/Smoke→eine finale Supply-Chain-Kette.
6. **Phase 6** dokumentiert nur den belegten finalen Zustand; SC-009 bleibt Human-owned.
7. **Phase 7** fuehrt Secret-, einmaligen Gesamt- und Delivery-Set-Check aus und endet am sicheren Modellrand.
8. **Phase 8** ist Orchestrator-only: Content-Commit→separater Statistik-Commit→Push/PR→Exact-Head-Review→PreMerge→fail-closed Bypass-Eignungspruefung→normale Provider-Merge-Operation oder bereits autorisierter Admin-Bypass nur bei alleinigem `REVIEW_REQUIRED`-Blocker→Fast-forward→PostMerge→State→Cleanup/0/0→Retrospektive/Session-Log.

### User-Story-Abhaengigkeiten / User Story Dependencies

- **US1 (P1)**: Phasen 2 und 3 liefern das MVP der nachweisbaren Gap-Disposition; sie benoetigen nur Phase 1.
- **US2 (P1)**: Least-Privilege-/Sandbox-Pakete benoetigen das US1-Gap- und Evidenzmodell.
- **US3 (P1)**: Reproduzierbarkeits-/Toolchain-Pakete benoetigen dasselbe Modell und muessen vor dem finalen Image abgeschlossen sein.
- **US4 (P2)**: SBOM/Scan/VEX/Provenienz benoetigt die finale Image-ID aus T053 und darf nicht vorgezogen werden.
- **US5 (P2)**: Dokumentation/A11Y beschreibt den Zustand nach T055; der menschliche SC-009-Datensatz kann vorbereitet, aber nicht agentisch erzeugt werden.

### Echte Parallelmoeglichkeit / Genuine Parallel Opportunity

Nach T049 duerfen T050, T051 und T052 auf drei echten Hostplattformen parallel
laufen, weil sie in drei getrennte Plattformdateien schreiben. T053 wartet auf
alle drei Ergebnisse oder deren ehrlichen `Open`-Status. Andere scheinbar
disjunkte Work Packages schreiben spaeter gemeinsam
`gap-dispositions.json`/`verification-evidence.json` und tragen deshalb kein
`[P]`.

```text
T049
 |- T050 -> platform-macos.md
 |- T051 -> platform-linux.md
 `- T052 -> platform-windows-wsl2.md
T050 + T051 + T052 -> T053
```

Die Textbeschreibung ist vollstaendig; das Diagramm ist nur eine zusaetzliche
Darstellung. / The prose is complete; the diagram is supplementary only.

## Implementierungsstrategie / Implementation Strategy

### MVP zuerst / MVP First

1. Phase 1 abschliessen.
2. `GAP-147` RED→GREEN in Phase 2 beweisen.
3. Phase 3 auf exakt 157/108/49 erweitern.
4. Stoppen und US1 unabhaengig pruefen. Das MVP ist Evidenz- und
   Dispositionsfaehigkeit, noch keine Feature-Lieferung oder Risikofreigabe.

### Inkrementell und fail-closed / Incremental and Fail-Closed

- Gezielte Modi waehrend RED/GREEN; kein wiederholter Full-Build oder
  Full-Smoke nach jedem Paket.
- Genau ein proportionaler finaler Build/Runtime/Smoke-Lauf nach dem letzten
  technischen Edit und genau eine daran gebundene finale SBOM-/Scan-Kette.
- Genau ein abschliessender `--mode all`-Lauf vor dem Modellrand.
- Jede spaetere Aenderung invalidiert nur die beruehrten Gates; Build/Runtime
  wird nur bei geaenderter Subject-/Image-Identitaet wiederholt.

## Abschlussbedingungen dieser Task-Liste / Task-List Completion Conditions

- Alle Aufgaben folgen Checkbox + stabilem T-ID-Format; Story-Aufgaben tragen
  `[US1]` bis `[US5]`.
- Alle 157 Gap-IDs sind genau einem WP-Bereich zugeordnet; die exakte 108/49-
  Grenze und Human-only-Liste bleiben unveraendert.
- Jede Schreibaufgabe nennt Requirements plus Gap(s) oder ein explizites
  Querschnittsgate und einen exakten Repositorypfad.
- RED ist vor GREEN sichtbar; Schema, Semantik, akzeptierte Hashes,
  reziproke Referenzen, Freshness und Changed-Path-Mapping werden getestet.
- Unverfuegbare Plattformen und menschliche Evidenz bleiben `Open` mit Owner,
  Follow-up und Trigger; sie werden nicht als `N/A` oder `Pass` simuliert.
- Modell- und Orchestrator-Aufgaben sind durch T069 klar getrennt; der
  Run-State bleibt in Modellphasen unveraendert.
- Formale Freigaben, Risikoakzeptanz, reale Secret-/Provideraktionen, externe
  Register, Registry-Publikation und spaetere Serienfortschreibung sind nicht
  als agentisch abschliessbare Feature-Arbeit geplant.
