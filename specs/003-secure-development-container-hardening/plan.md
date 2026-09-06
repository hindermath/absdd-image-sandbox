# Implementierungsplan: Sichere Entwicklungs-Container-Haertung / Implementation Plan: Secure Development Container Hardening

**Branch / Branch**: `003-secure-development-container-hardening`

**Datum / Date**: 2026-08-30

**Spezifikation / Specification**: [spec.md](spec.md)

**Eingabe / Input**: Geklaerte Feature-Spezifikation und die dort gebundenen sechs akzeptierten Artefakte. / Clarified feature specification and its six bound accepted artefacts.

**DE:** Dieser Plan beendet Phase 0 und Phase 1 von `/speckit-plan`. Er aendert
keine Laufzeit, implementiert keine Haertung, erzeugt keine Risikofreigabe und
fuehrt weder Commit noch Remote-Aktion aus. Ein spaeterer Umsetzungsschritt darf
nur eine durch aktuelle RED-Evidenz nachgewiesene Luecke aendern.

**EN:** This plan completes phases 0 and 1 of `/speckit-plan`. It changes no
runtime, implements no hardening, grants no risk approval, and performs no
commit or remote action. Later implementation may change only a gap proven by
current RED evidence.

## Zusammenfassung / Summary

Die Umsetzung beginnt mit einem maschinenlesbaren, exakt 157 Eintraege grossen
Gap-Register. Ein gemeinsamer speichersicherer Python-Kern und gleichwertige
Bash-/PowerShell-7-Einstiege pruefen die sechs Eingabehashes, die lueckenlose
`GAP-001`-bis-`GAP-157`-Menge, die unveraenderte Aufteilung `108` agentisch und
`49` Human-only sowie jeden Evidenzdatensatz. Erst danach werden vorhandene
Docker-, Compose-, Agenten-, Script-, Test- und Dokumentationskontrollen
praktisch geprueft. Nur ein fehlgeschlagener oder unvollstaendiger Check loest
eine minimale, auf Gap-ID und Anforderung rueckverfolgbare Aenderung aus.

The implementation starts with a machine-readable 157-entry gap register. A
shared memory-safe Python core plus equivalent Bash and PowerShell 7 entry
points verify the six input hashes, exact gap set, unchanged 108/49 partition,
and every evidence record. Existing controls are then tested in practice. Only
a failed or incomplete check triggers a minimal traceable change.

## Technischer Kontext / Technical Context

**Sprache und Version / Language and version**: Python 3 fuer wiederverwendbare
Validatorlogik; Bash und PowerShell 7 fuer plattformgerechte Einstiege; JSON,
Markdown, Dockerfile und Compose YAML als Artefakte. Keine neue nicht
speichersichere Sprache. / Python 3 for reusable validation logic; Bash and
PowerShell 7 for platform entry points; JSON, Markdown, Dockerfile, and Compose
YAML as artefacts. No new non-memory-safe language.

**Primaere Abhaengigkeiten / Primary dependencies**: vorhandenes Podman/
`podman-compose`, PowerShell 7 (`pwsh -NoProfile`), Python-Standardbibliothek,
`rg`, Git, Syft, Gitleaks/pre-commit, vorhandene Spec-Kit- und
Documentation-Impact-Validatoren. Der Python-Kern erzwingt die fuer diese zwei
JSON-Vertraege benoetigten Strukturregeln direkt und testet sie mit positiven
und negativen Fixtures; die JSON-Schemas bleiben die maschinenlesbare
Schnittstelle. Damit entsteht keine versteckte, ungepinnte Python-Abhaengigkeit.
Der bestehende SBOM-Analysepfad findet nur ungepinnte Host-Installationen von
Grype oder Trivy und ist deshalb bereits ein bestaetigter RED-Befund: Vor dem
Supply-Chain-Gate MUSS genau ein Scanner mit unveraenderlicher Identitaet und
belegter Herkunft bereitgestellt oder das Gate fail-closed blockiert werden. /
Existing tools plus standard-library structural and semantic validation; the
current host-only vulnerability-scanner discovery is a confirmed RED finding,
not an optional fallback.

**Speicherung / Storage**: Git-getrackte Vertrage und menschenlesbare Evidenz
unter `specs/003-secure-development-container-hardening/` und
`docs/security/secure-development/2026-08-30-container-hardening/`; lokale
SBOM-/Scan-Rohdaten bleiben unter `sboms/` ungetrackt. Keine Datenbank. /
Tracked contracts and readable evidence in the feature and dated security
directories; raw local SBOM/scan artefacts remain untracked. No database.

**Testen / Testing**: vorhandenes `unittest`, Shell-Syntax/`shellcheck`,
PSScriptAnalyzer soweit verfuegbar, JSON-Schema plus semantischer Validator,
`podman-compose config`, praktischer Podman-Build, Laufzeitgrenzen,
Toolchain-/Agenten-Smoke-Test, SBOM/Scan/VEX/Provenienz, Secret-Scan,
Dokumentations-/A11Y-/Agentenparitaet und Plattformmatrix. / Existing test and
validation surfaces plus practical Podman evidence.

**Zielplattform / Target platform**: Linux-Container auf rootless Podman;
Hostablaeufe fuer macOS, den Windows-Host und Ubuntu unter WSL2 mit eigener
rootless-Podman-Laufzeit. Windows-Host und Ubuntu/WSL2 duerfen auf derselben
physischen Hardware laufen, verwenden aber getrennte Evidenz. Der Planlauf ist
macOS. Native Linux-Hardware ist kein Akzeptanzziel fuer Feature 003. Nicht
verfuegbare Plattformpfade bleiben spaeter `Open` mit Owner und Trigger. /
Linux container on rootless Podman; host workflows for macOS, the Windows host,
and Ubuntu under WSL2 with its own rootless Podman runtime. Windows host and
Ubuntu/WSL2 may share physical hardware but use separate evidence. Native Linux
hardware is not a Feature 003 acceptance target.

**Projekttyp / Project type**: Container-, CLI-, Automations-, Lern- und
Governance-Repository; keine Webanwendung, API oder produktive Cloud. /
Container, CLI, automation, learning, and governance repository; no web app,
API, or production cloud.

**Leistungsziele / Performance goals**: `157/157` eindeutige Dispositionen,
`108/49` unveraendert, `0` unerklaerte Aenderungen, ein Full-Build und ein
Full-Smoke-Lauf pro finaler Image-Identitaet; gezielte Teilpruefungen waehrend
RED/GREEN statt redundanter Vollsuite. / Exact counts, zero untraced changes,
and one final full build/smoke run per image identity.

**Einschraenkungen / Constraints**: kein Registry-Push, keine formale
Freigabe, keine Risikoakzeptanz, keine Secret-/Schluesselaktion, keine externen
Register, kein Provider-/Modell-/Telemetrieentscheid, kein Bypass durch die
Modellphase und kein unabhaengiges Refactoring. Orchestrator-only bleiben
Commit, PR, Merge, Default-Branch-Sync und kausale PostMerge-Arbeit. Der fuer
diesen Run bereits autorisierte Admin-Bypass darf nur in der Provider-
Merge-Operation eingesetzt werden, wenn `REVIEW_REQUIRED` nach allen gruenen
technischen Gates, gueltiger Schema-2.0-PreMerge-Evidenz und null
handlungsrelevanten Review-Threads der einzige Policy-Blocker ist; er darf
keine technische Pruefung oder Repository-Regel umgehen. / No excluded
authority; model-phase bypass is prohibited. Commit/PR/merge/sync and causal
PostMerge work remain orchestrator-only. The Admin-Bypass already authorized
for this run is limited to the provider merge operation when
`REVIEW_REQUIRED` is the sole policy blocker after all-green technical gates,
valid schema-2.0 PreMerge evidence, and zero actionable review threads; it may
not bypass a technical check or change a repository rule.

**Umfang / Scale and scope**: 157 Gaps aus 12 Checklisten, 108 agentisch
bearbeitbar, 49 Human-only; sechs MSL-Toolchains, zwei Skriptgrundlagen, vier
Pflicht-Agenten, zwei zusaetzliche Agentenoberflaechen, Docker/Compose,
VS-Code-Dev-Container, Security-/Architektur-/A11Y-/Lernenden-Evidenz und
Statistikprofil 2. / 157 gaps and the stated repository surfaces.

## Verfassungspruefung vor Research / Constitution Check Before Research

`PASS` bedeutet hier nur: Die Planentscheidung ist vollstaendig. Der spaetere
Umsetzungsstatus bleibt `Not Assessed`. Owner ist `Repository Maintainer`,
Reviewer `Security Review`, Restrisiko `Unassessed`. / `PASS` means planning
completeness only; implementation remains unassessed.

| Pruefbereich / Checkpoint | Status | Planentscheidung / Planning decision |
|---|---|---|
| Level-2-Kontext | Applicable / PASS | Bindender Registry-Eintrag `container-images/absdd-image-sandbox`: Python/Bash/PowerShell, Podman, `80` Zeilen/Arbeitstag, text-first Docs und Repository-Surfaces. |
| MSL | Applicable / PASS | Python ist der gemeinsame Kern; Bash/PowerShell sind notwendige Schnittstellen. Keine neue unsichere Sprache. |
| Sichere Codeerzeugung | Applicable / PASS | Eingaben/Umgebungswerte validieren, Shellwerte quotieren, kein `eval`/`Invoke-Expression`, Fehler ohne interne/Secret-Daten. |
| Sichere Architektur / iSAQB | Applicable / PASS | Host, Container, Mounts, Egress, Agentenzustand, Provider und SBOM/Scan sind Trust Boundaries; Threat Model, S-ADRs, arc42 und Qualitaetsszenarien werden geplant. |
| NIST SSDF / CWE Top 25 | Applicable / PASS | Prozess- und Ursachenlinsen fuer alle agentischen Aenderungen und Reviews. |
| OWASP ASVS | N/A / PASS | Kein eigener HTTP-, API-, Authentifizierungs- oder Autorisierungsdienst. Trigger: ein solcher Dienst kommt in Scope. |
| SBOM / VEX | Applicable / PASS | Finale lokale Image-Identitaet, CycloneDX-SBOM, Scan und Status je relevantem Fund. |
| SLSA / Provenienz | Applicable target / PASS | Lokale Build-Herkunft und Reproduzierbarkeit; keine erfundene externe SLSA-Stufe. |
| AI-SBOM | N/A / PASS | Agenten sind Entwicklungswerkzeuge, kein Modell/Datensatz/Inferenzdienst ist Produkt-Runtime. Trigger: KI-Runtime wird ausgeliefert oder betrieben. |
| CAPEC / Threat Model | Applicable / PASS | Hoechstriskante Mount-, Egress-, Provider- und Artefaktpfade erhalten CAPEC-Bezug. |
| Zero Trust | N/A / PASS | Lokaler Einzelcontainer ohne Remote-Management; Providergrenze bleibt Trust Boundary. Trigger: Cloud, Multi-Device oder Remote-Service. |
| BSI C3A / C5 | N/A / PASS | Keine Cloud-/Hosting-/Managed-Service-Auswahl. Trigger: entsprechender Scope. |
| OWASP SAMM | Applicable / PASS | Dokumentarische Verbesserungsbewertung, keine formale Reifegradfreigabe. |
| Regulatorik / CRA / Datenschutz | Open, Human-only / PASS | Nur Fakten/Vorlagen; Entscheidung durch `Privacy/Legal Review`. |
| Security-first | PASS | Keine Credentials, Agentensessions, Prompt-/Antwortinhalte, private Endpunkte oder lokale Providerwerte in Evidenz. |
| Presets | Applicable / PASS | Das verwaltete Zwoelf-Preset-Profil (Standard-Acht plus Modell-Routing und drei Intake-Presets) und seine installierten Oberflaechen werden gegen `scripts/config/spec-kit-model-routing-governance-presets.json` sowie mit dem vorhandenen Paritaetstest geprueft. |
| A11Y / Lernendenbasis | Applicable / PASS | Deutsch zuerst, Englisch danach, CEFR B2, alle vier Berufe, Erstbegriffe, keine Spec-Kit-Vorkenntnis, Text zuerst, WCAG 2.2 AA soweit anwendbar. |
| Cross-Platform | Applicable / PASS | Neue/geaenderte kritische Skripte als Bash+PowerShell, `--dry-run`/`-WhatIf`, Manpage, Hilfe, Cmdlet und Plattformbeleg. |
| Agentenparitaet | Applicable when shared / PASS | Gemeinsame Regeln atomar in allen vier Guidance-Dateien, ggf. Copilot-Agentenspiegel, Templates und Constitution; projektspezifische Details bleiben lokal. |
| Statistikprofil 2 | Applicable post-content / PASS | Erst nach inhaltlichem Commit durch Orchestrator rendern, pruefen und in separatem Statistik-Commit liefern; keine Statistik im Content-Commit. |
| Dokumentationswirkung | `UpdateRequired` / PASS | Kanonisch sind Konfiguration plus Gap-Evidenz; Navigation, Sprache, Plattformbeleg und A11Y werden validiert. |
| Autonomer Lauf | Applicable / PASS | Run-State bleibt unveraendert; Gates sind vor Implementierung deklariert; Modellaufgaben und Orchestrator-/PostMerge-Aufgaben bleiben getrennt. |

Keine Verfassungsverletzung und keine offene Klaerung verbleiben. / No
constitution violation or unresolved clarification remains.

## Projektstruktur / Project Structure

```text
specs/003-secure-development-container-hardening/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── autonomous-run-state.json              # orchestrator-owned, unchanged
├── autonomous-run-evidence.md
├── autonomous-run-gate-requirements.json
├── checklists/requirements.md
├── contracts/
│   ├── hardening-evidence-contract.md
│   ├── gap-dispositions.schema.json
│   └── verification-evidence.schema.json
└── tasks.md                                # erst /speckit-tasks

scripts/
├── test-ade-sandbox-hardening.sh           # geplant, Bash entry point
├── test-ade-sandbox-hardening.ps1          # geplant, Test-AdeSandboxHardening
├── build-and-sbom.sh/.ps1                  # bestaetigten RED-Befund remediieren
├── analyze-sbom.sh/.ps1                    # gepinnten Scannerpfad herstellen
├── lib/secure_development_hardening.py     # geplanter gemeinsamer Validator
└── tests/test_secure_development_container_hardening.py

docs/security/secure-development/2026-08-30-container-hardening/
├── README.md
├── gap-dispositions.json                   # kanonisch, exakt 157
├── verification-evidence.json
├── learner-first-use-results.json          # Human evidence for SC-009
├── build-provenance.json
├── vulnerability-findings.json
├── vex.cdx.json
└── human-only-handoffs.md
```

Weitere Dateien unter `Dockerfile`, Compose, `codex/`, `opencode.jsonc`,
`.devcontainer/`, `docs/architecture/`, `docs/security/`, `docs/betrieb/`,
`docs/fuer-lernende/`, `docs/accessibility/`, Agent-Guidance und Workflows
werden nur nach einem zugeordneten RED-Befund geaendert. / Other files change
only after a mapped RED finding.

### Verifizierte Helper-Schnittstellen und bestaetigte RED-Befunde
/ Verified Helper Interfaces and Confirmed RED Findings

Die Planpruefung hat die folgenden vorhandenen Pfade und Schnittstellen direkt
im Repository geprueft. Sie sind deshalb keine Annahmen fuer die Task-Phase: /
Plan review inspected these existing paths and interfaces directly; they are
not assumptions for task generation.

| Helper / Surface | Verifizierter Istzustand / Verified current state | Bindende Planfolge / Binding plan consequence |
|---|---|---|
| `scripts/build-and-sbom.sh` / `.ps1` | `--skip-build` / `-SkipBuild` existieren; beide fallen auf `docker.io/anchore/syft:latest` zurueck. Die PowerShell-Datei nutzt `Set-StrictMode -Version 2.0`, besitzt keine bilinguale Comment Help und exportiert kein genehmigtes Cmdlet; eine passende Manpage fehlt. | Der bewegliche Fallback MUSS entfernt oder digest-gepinnt werden. Sobald der kritische Ablauf geaendert wird, MUSS das Paar `New-AdeSandboxSbom`, `--dry-run`/`-WhatIf`, bilinguale Hilfe und `docs/man/new-ade-sandbox-sbom.1` gemeinsam liefern. |
| `scripts/analyze-sbom.sh` / `.ps1` | `--scan --scanner grype` / `-Scan -Scanner grype` sind real; der Scanner wird nur ungepinnt vom Host gesucht. Dry-run/WhatIf, genehmigtes Cmdlet, vollstaendige Comment Help und Manpage fehlen. | Ein gepinnter Scannerpfad und die Constitution-konforme Paarschnittstelle sind vor `GATE-SUPPLY-01` verpflichtend; fehlende Plattform oder Quelle ergibt `Blocked`, nie einen stillen Host-Fallback. |
| `scripts/check-homogeneity.sh` / `.ps1` | `--dry-run --no-patch "$PWD"` und `-TargetDir $PWD -DryRun -NoPatch` sind real, pruefen aber nicht allein moderierte Lernendentests oder alle artefaktbezogenen WCAG-Kriterien. | `GATE-A11Y-01` erhaelt zusaetzlich den geplanten `Accessibility`-Modus; SC-009 erhaelt einen eigenen, menschlich ausgefuehrten Gate-Nachweis. |
| `scripts/smoke-test-toolchains.sh` | Der reale Lauf prueft unter anderem `agy --version` und `copilot --version`; README und Dockerfile bestaetigen zusaetzlich `gemini`. | Der neue Validator darf den bestehenden Full-Smoke nicht ersetzen und MUSS OpenCode, Codex, Claude, Gemini, Antigravity und Copilot ohne Provideraufruf abgleichen. |
| `scripts/invoke-psscriptanalyzer.ps1` | Der Helper und die gepinnte Registry-Version existieren; `shellcheck` ist im Image installiert, aber auf dem aktuellen macOS-Host nicht vorhanden. | PowerShell-Analyse laeuft ueber den vorhandenen Helper. ShellCheck laeuft im finalen Container oder auf einem belegten Host; Host-Abwesenheit darf nicht als Pass gelten. |
| autonome Validatoren | `validate-autonomous-delivery-set.sh` verlangt `--repo` und akzeptiert fuer jeden beabsichtigten ungetrackten Pfad ein wiederholtes `--intended`; `validate-autonomous-gate-evidence.sh` verlangt `--requirements`, `--evidence` und `--head`. | Delivery- und Exact-Head-Schritte verwenden diese echten Argumente; `--intended` wird nur bei vorhandenen beabsichtigten ungetrackten Dateien gesetzt. Ein blosser Helpername oder `--help` ist keine Gate-Evidenz. |

## Phase 0: Research

[research.md](research.md) dokumentiert Entscheidungen und Alternativen zu:

- unveraenderter Hash-/157-/108-/49-Bindung;
- evidence-first RED/GREEN und representativem Vertical Slice;
- vorhandenen versus noch unbelegten Docker-/Compose-Kontrollen;
- reproduzierbaren Quellen, Download-/Agent-/Toolchain-Pins;
- Rootless-, Capability-, Mount-, Netzwerk-, Port-, State- und Credential-Grenzen;
- SBOM, Schwachstellenscan, VEX, lokaler Provenienz und N/A fuer AI-SBOM;
- VS Code, Lernenden-, A11Y-, Cross-Platform- und Agentenparitaet;
- Statistikprofil 2 als getrenntem kausalem Post-Content-Schritt.

## Phase 1: Design und Vertrage / Design and Contracts

[data-model.md](data-model.md) definiert Gap-Disposition, Evidenz, Boundary,
Werkzeug, Schwachstellen-/VEX-Status und Human-only-Uebergabe. Der
[Artefaktvertrag](contracts/hardening-evidence-contract.md) bindet Pfade,
Kardinalitaeten, Statusregeln, Evidenzfrische und Projektionen. Die JSON-Schemas
pruefen Struktur; der semantische Validator prueft exakte Mengen, eindeutige
IDs, wechselseitige Referenzen und die 108/49-Partition.

### Traceability, Gate-Owner und Evidence-Owner
/ Traceability, Gate Owners, and Evidence Owners

`autonomous-run-gate-requirements.json` ist die vollstaendige, kanonische
Gate-Liste. Die kuerzere Gate-Tabelle in `spec.md` bindet die stabilen
fachlichen Mindestgates, ersetzt aber nicht die zusaetzlichen Plan-, Plattform-,
Dokumentations-, Statistik-, Delivery- und begruendeten N/A-Gates. Jede
Task-Phase MUSS auf die vollstaendige JSON-Liste abbilden. / The gate
requirements JSON is exhaustive; the shorter specification table is a minimum
semantic set and does not supersede the additional reviewed gates.

Der Statuskopf und der Abschnitt `Naechste Phase` in `spec.md` beschreiben den
damaligen Abschluss der Specify-/Clarify-Artefakte und sind historische
Phasenhinweise, kein aktueller Orchestrierungsstatus. Fuer die aktuelle Phase
ist ausschliesslich der unveraenderte orchestratorverwaltete Run-State
massgeblich. So wird die akzeptierte Spec-Hashbindung nicht fuer eine rein
operative Statusfortschreibung gebrochen. / The specification's phase-local
status text is historical; current orchestration state comes only from the
orchestrator-owned run state.

| Scope | Requirement-/Story-Bindung | Primaere Evidenz / Primary evidence | Owner | Reviewer |
|---|---|---|---|---|
| Gap-Vertrag und Eingaben | User Story 1; FR-001–FR-004a, FR-021–FR-022 | `gap-dispositions.json`, Input-/Gap-Gates | Repository Maintainer | Security Review |
| Container, Mount, State, Egress | User Story 2; FR-006–FR-009, FR-012–FR-013, FR-020; AR-001–AR-005 | Runtime-, Human- und Architecture-Evidenz | Repository Maintainer | Security Review |
| Quellen, Toolchains und Agenten | User Story 3; FR-005, FR-010–FR-013, FR-016–FR-017 | Static-, Build-, Smoke- und Paritaetsgates | Repository Maintainer | Security Review |
| SBOM, Scan, VEX, Provenienz | User Story 4; FR-014–FR-018 | Supply-Chain-Gate und finale Image-Bindung | Repository Maintainer | Security Review |
| Lernende, Dokumentation, A11Y | User Story 5; FR-019–FR-020; GR-001–GR-006; SC-008–SC-009 | Documentation-, Accessibility- und Learner-Gates | Learning/A11Y Review | Security Review |
| Plattformparitaet | CP-001–CP-005 | gemeinsames Gate sowie getrennte Gates fuer macOS, Windows-Host und Ubuntu/WSL2 | Repository Maintainer je Plattformpfad; Windows-Host und Ubuntu/WSL2 duerfen dieselbe Hardware mit getrennten Laufzeiten nutzen | Security Review |
| Agenten-/Template-Paritaet | AP-001–AP-004 | Paritaetsgate und Changed-Path-Mapping | Repository Maintainer | Security Review |
| Begruendete N/A-Gates | ASVS, Produkt-AI-SBOM, Zero Trust, Cloud/C3A/C5, Registry/Hosting | exakt eine N/A-Primary-Zeile je Gate ohne Laufdaten, aber mit Sachgrund und Trigger | Repository Maintainer | Security Review; formale Rechts-/Providerentscheidung bleibt ausser Scope |
| Autonomer Abschluss | AU-001–AU-006 | Delivery-Set, temporaeres PreMerge, kausales PostMerge, finaler State | Orchestrator unter aktuell revalidierter Autoritaet | erforderliche menschliche/Plattform-Reviews |

Der moderierte Erstnutzungstest aus SC-009 ist weiterhin fuer einen spaeteren
Lernenden-Rollout verpflichtend und keine Umklassifizierung der 49 akzeptierten
Human-only-Gaps. Fuer die bis 31.12.2026 befristete, allein durchgefuehrte und
source-only Machbarkeitsstudie dokumentiert
`DEC-FEASIBILITY-SINGLE-PERSON-2026-09-06` jedoch ausdruecklich
`NotPerformed`; `GATE-LEARNER-01` ist nur fuer diesen Studienabschluss `N/A`.
Vor Lernenden-Rollout, vorgebauter Image-Verteilung, produktiver Nutzung oder
bei Ablauf wird es wieder `Applicable`. / SC-009 remains mandatory before
learner rollout and does not reclassify the 49 Human-only gaps. The time-bound
single-person feasibility decision records NotPerformed and makes the learner
gate N/A only for this source-only study closeout.

## Implementierungsstrategie / Implementation Strategy

### 1. Evidence-first RED-Baseline

1. Sechs akzeptierte Hashes und Run-State read-only pruefen.
2. `gap-dispositions.json` deterministisch aus der akzeptierten 157-Gap-Liste
   initialisieren: weiterhin `Open` + `Not Assessed`, nie automatisch positiv.
3. Schema-/Semantiktests zuerst schreiben und mit manipulierten Fixtures RED
   zeigen: fehlende/duplizierte ID, falsches Human-only-Flag, ungueltige
   Statuskombination, fehlender Trigger, unzulaessige Zusatzfelder,
   widerspruechliche N/A-Laufdaten und veraltete Evidenz.
4. Den Repository-Istzustand je Gap inspizieren. `AlreadySatisfied` erfordert
   anschliessend aktuelle GREEN-Evidenz; `N/A` erfordert Sachgrund und Trigger.

### 2. Repräsentativer Vertical Slice / Representative Vertical Slice

Der erste Slice umfasst `GAP-013`, `GAP-015`, `GAP-020`, `GAP-051`,
`GAP-122`, `GAP-147`, `GAP-148`, `GAP-149` und `GAP-154`. Er prueft in einer
durchgehenden Kette Trust Boundary, geringste Rechte, Lieferkette, SBOM,
Secret-Scan, Mounts, Agentenstate und Isolationsnachweis. Der Slice muss RED
aus einem fehlenden/alten Nachweis, die kleinste erlaubte Aenderung und GREEN
mit aktuellem Befehl, Plattform, Exitcode und Hash zeigen. Erst danach werden
die restlichen Gruppen bearbeitet.

Der Slice beginnt mit genau einer absichtlich fehlerhaften Fixture fuer
`GAP-147`: eine fehlende Mount-Evidenz MUSS RED liefern und darf weder
`AlreadySatisfied` noch `Fulfilled` erzeugen. Danach wird derselbe Datensatz
mit einer aktuellen, nicht sensiblen Mount-Pruefung GREEN. Die uebrigen acht
Slice-Gaps duerfen erst folgen, wenn dieser eine End-to-End-Vertrag vom
akzeptierten Gap ueber Requirement, Evidence-ID, Owner/Reviewer und Gate bis
zum Statuswechsel nachweisbar besteht. / One deliberately failing `GAP-147`
fixture proves the end-to-end contract before the other slice items proceed.

### 3. Finding-conditioned technische Gruppen

| Arbeitsgruppe / Work package | Exakte Gaps / Exact gaps | Anforderungen | Geplante Aenderungsflaechen nur bei RED / Conditional surfaces |
|---|---|---|---|
| WP01 Standards und Statusmodell | `GAP-001`–`GAP-012` | FR-001–004a, 014–017, 021–022 | Gap-Schema, Standards-/Regulatorik-Evidenz; `GAP-011/012` bleiben Human-only. |
| WP02 Sichere Architektur | `GAP-013`–`GAP-025` | FR-006–009, 018, 021 | Kontext, arc42, S-ADRs, Quality Scenarios, Cloud-N/A; technische Konfiguration nur bei nachgewiesenem Defizit. |
| WP03 Krypto | `GAP-026`–`GAP-040` | FR-005, 008, 016–017 | Download-Hash/Signatur/TLS-Audit; Produktkrypto meist N/A; `GAP-034/035` Human-only. |
| WP04 Threat Model | `GAP-041`–`GAP-050` | FR-006–009, 018 | STRIDE+CIA, CAPEC, Anforderungen/Massnahmen/Review. |
| WP05 Lieferkette | `GAP-051`–`GAP-063` | FR-005, 010–017 | Dockerfile-Pins, Lock-/Quellnachweis, SBOM/Scan/VEX/Provenienz, Renovate; AI-SBOM N/A. |
| WP06 Offenlegung | `GAP-064`–`GAP-074` | FR-015, 017–019 | CVD/security.txt/Triage/Patch/Uebung; `GAP-070` Human-only. |
| WP07 CRA | `GAP-075`–`GAP-086` | FR-003–004, 021 | Nur Fakten und Uebergabe an Privacy/Legal Review; alle 12 bleiben Human-only. |
| WP08 Security Review | `GAP-087`–`GAP-099` | FR-005–020 | Script-/Datei-/Netzwerk-/Fehler-/Testreview; keine Anwendungsfunktionen erfinden. |
| WP09 KI-Codeerzeugung | `GAP-100`–`GAP-116` | FR-008, 010–012, 017–019 | Inventar, Telemetrie-/Providergrenzen, Audit, Schulung, didaktische Kommentare; neun benannte Gaps Human-only. |
| WP10 Entwicklungsumgebung | `GAP-117`–`GAP-133` | FR-006–013, 017–020 | Host-Fakten, IDE/VS Code, Secret-Scan, CI-Reproduzierbarkeit, Testdaten, Paritaet; sieben benannte Gaps Human-only. |
| WP11 DPIA | `GAP-134`–`GAP-145` | FR-003–004, 021 | Nur Fakten/Vorlage/Handoff; alle 12 bleiben Human-only. |
| WP12 Agentische Sandbox | `GAP-146`–`GAP-157` | FR-006–013, 018–020 | Compose/Agenten/Mount/State/Netzwerk/Lifecycle/Preset-Evidenz; `146/150/152/155` Human-only. |

Die Bereiche sind disjunkt und ergeben genau 157. Die Human-only-Liste aus
`spec.md` ist unveraenderlich und wird nicht aus Themenannahmen neu berechnet.

### 4. Docker, Compose und Laufzeit

- Bestehende Positivkontrollen zuerst beweisen: Basisdigest, non-root
  `adedev`, `no-new-privileges`, `cap_drop: ALL`, localhost-Portbindung,
  getrennte Agenten-Volumes und read-only .NET-Konfigurationsmount.
- Downloadquellen automatisiert auf bewegliche Tags, fehlende Integritaet und
  ungepinnte Fallbacks pruefen. Der `SyftImage`-`latest`-Fallback und die
  ungepinnte Host-Erkennung fuer Grype/Trivy sind durch die Planpruefung
  bestaetigte RED-Befunde. Go-Tarball, Node-Paketversion/Key-Fingerprint,
  Spec-Kit-Tagbindung und Checksummen aus demselben Downloadkanal bleiben bis
  zum reproduzierbaren Audit Pruefhypothesen, keine vorweggenommenen Edits.
- Schreibbare Root-Dateisysteme, PID-/Ressourcenlimits und breite RW-Mounts
  durch praktische Lernablaufe pruefen. Eine Restriktion wird nur gesetzt,
  wenn alle benoetigten Schreibpfade explizit abgedeckt und Smoke-Tests gruen
  bleiben; sonst bleibt der Punkt begruendet `Open`.
- Freier Egress darf nicht als akzeptiertes Risiko bezeichnet werden.
  Repository-Fakten und erreichbare Endpunkte werden dokumentiert;
  Allow-List-/Proxy- oder formale Netzwerkentscheidung bleibt `GAP-155`
  Human-only.

### 5. Cross-Platform, VS Code und Lernende

Der neue einheitliche Pruefeinstieg wird als
`test-ade-sandbox-hardening.sh` und `test-ade-sandbox-hardening.ps1` geplant.
PowerShell exportiert `Test-AdeSandboxHardening`; die Bash-Manpage lautet
`docs/man/test-ade-sandbox-hardening.1`. Bestehende SBOM-Einstiege erhalten bei
erforderlicher Aenderung `New-AdeSandboxSbom` und
`docs/man/new-ade-sandbox-sbom.1`. Beide Paare bieten
`--dry-run`/`-WhatIf`, identische Modi und Exitcodes.

Der Haertungs-Pruefeinstieg besitzt die Modi `Input`, `Static`, `Runtime`,
`SupplyChain`, `Documentation`, `Accessibility` und `All`. `Accessibility`
validiert die artefaktbezogene WCAG-/Bilingual-/Text-first-Pruefliste und den
separaten, von `Learning/A11Y Review` erzeugten SC-009-Datensatz; er erzeugt
keine menschliche Evidenz selbst. / Accessibility validates, but never
fabricates, the human review record.

VS Code wird ohne permanenten Server oder neuen Port praktisch geprueft:
Compose-Service `ade`, `remoteUser: adedev`, Workspace-Mappings, LSP-Identitaet
und die dokumentierte Grenze des `code`-Shims. Nutzertexte bleiben
Deutsch-zuerst/Englisch-danach, ungefaehr CEFR B2, nennen alle vier
Ausbildungsberufe, erklaeren Spec Kit und Fachbegriffe beim ersten Auftreten
und besitzen vollstaendige Textalternativen.

### 6. Abschlussreihenfolge / Closeout Order

1. Alle 108 agentischen Gaps ehrlich dispositionieren und technische GREEN-
   Evidenz an die finale lokale Image-Identitaet binden.
2. Einmal finale Config, Build, Runtime und Full-Smoke ausfuehren.
3. Erst danach finale SBOM, Scan, VEX und lokale Provenienz erzeugen.
4. Dokumentation, A11Y, Paritaet, Secret-Scan und 157/108/49-Abgleich finalisieren.
5. Fehlende Ubuntu/WSL2- oder Windows-Host-Evidenz bleibt am Gap ehrlich
   `Open`, blockiert aber das zugehoerige `Applicable`-Plattformgate und damit
   einen positiven `MergeAndSync`-Abschluss. Beide Pfade duerfen dieselbe
   Windows-Hardware nutzen, aber weder Laufzeit noch Evidenz wiederverwenden.
   `N/A` oder ein macOS-Ersatzlauf sind unzulaessig.
6. Modellarbeit endet am validierten Arbeitsbaum. Der Orchestrator revalidiert
   Autoritaet und prueft mit `validate-autonomous-delivery-set.sh --repo ...
   --intended ...` exakt alle vorgesehenen getrackten und ungetrackten Pfade,
   bevor er nur den Content-Satz staged und committet.
7. Statistikprofil 2 wird nach dem Content-Commit gerendert, geprueft und als
   eigener Statistik-Commit geliefert. Danach werden nur die durch diesen
   Commit betroffenen Diff-/Secret-/Dokumentations-/Statistikgates erneut
   ausgefuehrt; Build-/Runtime-Evidenz bleibt nur dann `Current`, wenn ihre
   Subject-Hashes und Image-Identitaet unveraendert sind.
8. Fuer den exakten final reviewten Head wird eine Schema-2.0-`PreMerge`-
   Momentaufnahme in einem temporaeren Pfad erzeugt. Jede Gate-ID besitzt
   genau eine Primary-Zeile; `executedCommand` und `runnerOrPlatform` stammen
   aus Definition oder Log. Die installierte Gate-Validierung laeuft mit
   `--requirements`, `--evidence` und `--head`. Die Momentaufnahme wird nicht
   committet und erteilt keine Autoritaet.
9. Erst nach aktuellen Checks, null handlungsrelevanten Threads, gueltiger
   Schema-2.0-`PreMerge`-Evidenz fuer den exakten reviewten Head und
   revalidierter `MergeAndSync`-Autoritaet darf der Orchestrator mergen. Eine
   normale Provider-Merge-Operation wird bevorzugt. Ist `REVIEW_REQUIRED` der
   einzige verbleibende Policy-Blocker, darf die bereits erteilte
   Admin-Bypass-Autoritaet ausschliesslich in dieser Provider-Merge-Operation
   genutzt werden; kein fehlgeschlagenes, ausstehendes, fehlendes, veraltetes
   oder widerspruechliches technisches/Security-Gate und keine Repository-Regel
   darf umgangen werden. Eine weitere Autoritaetsanfrage ist fuer diesen Run
   nicht erforderlich. Danach synchronisiert der Orchestrator den Default-
   Branch. Das kausale Schema-2.0-`PostMerge` bindet den
   normalisierten akzeptierten PreMerge-Hash und den realen Merge-Commit,
   besitzt leere `changedPaths` und wird erneut validiert. Keine unabhaengige
   Bereinigung oder Registry-Aktion wird angehaengt.
10. `Completed` ist erst zulaessig, wenn Merge/Publikation,
    Default-Branch-Sync, deklarierte PostMerge-Aktionen und finale Validierung
    im orchestratorverwalteten Schema-1.1-State terminal sind. Der State wird
    nur vom Orchestrator aktualisiert, nie von einer Modellphase.

## Plan-Review-Ergebnis / Plan Review Result

Die strikte Pruefung wurde vor der Task-Erzeugung ausgefuehrt; das fehlende
`tasks.md` ist fuer die autonome Phase `plan-review` erwartet, weil `tasks`
laut validiertem Run-State von `plan-review` abhaengt. Der Standard-
`/speckit.analyze`-Prerequisite-Check fuer die spaetere Phase `analyze` bleibt
unveraendert und MUSS nach `/speckit.tasks` erneut erfolgreich laufen. / The
pre-task plan review is an explicit autonomous phase; the standard post-task
Analyze prerequisite still applies later.

Remediiert wurden: vollstaendige Gate-/Requirement-/Owner-Traceability,
schema-konforme N/A-Evidenz ohne erfundenen Lauf, bestaetigte Helper- und
Scannerbefunde, ein eigener menschlich verantworteter Lernendentest, ein
staerkerer Accessibility-Nachweis, ein expliziter failing/green Vertical Slice,
fail-closed Plattformgrenzen sowie die exakte Delivery-/PreMerge-/PostMerge-
Reihenfolge. Es verbleiben keine Critical- oder High-Befunde und kein
unverantworteter Medium-Befund. Niedrige redaktionelle Varianten werden nicht
in die Task-Phase getragen. / No Critical or High finding and no unowned
Medium finding remains after remediation.

## Verfassungspruefung nach Design / Post-Design Constitution Check

Die Designartefakte erfuellen die Vorpruefung: MSL-Kern, paired interfaces,
Security-/Architecture-Evidenz, vollstaendige Gate-Deklaration, Human-only-
Grenzen, A11Y/Lernendenpolitik, Agentenparitaet und getrennter Statistik-
Closeout sind explizit. `research.md` enthaelt keine offene
`NEEDS CLARIFICATION`; die N/A-Entscheidungen besitzen Trigger. Ergebnis:
`PASS`, keine Complexity-Ausnahme. / Design passes with no unresolved
clarification or constitutional exception.

## Complexity Tracking

Keine Verfassungsverletzung. / No constitutional violation.
