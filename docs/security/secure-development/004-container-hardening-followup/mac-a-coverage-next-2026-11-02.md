# Mac A: gezielte Coverage-Runde / Targeted Coverage Round

## Lieferkorrektur / Delivery Correction

DE: Beim Lieferauftrag am 02.11.2026 erkannte der zusaetzliche Pre-Push-
Mustercheck den harmlosen Redigierungs-Testtext als Secretverdacht. Nur die
Darstellung dieses synthetischen Textes wurde strukturiert zusammengesetzt;
keine Scannerregel, Ausnahme, Produktlogik oder Anforderung geaendert.
Die 13 Fleet-Methoden erneut erfolgreich in 0,030 s. Alle 106 Produktquellen,
Konfiguration und zehn Branch-Nenner/-Zaehler unveraendert. Der bisherige
JSON-Bericht bleibt byte-identischer historischer Stand. Fuer die aktuelle
Fleet-Testdateibindung gilt der
[Lieferkorrektur-Nachweis](mac-a-coverage-delivery-correction-2026-11-02.json).
Kein doppeltes Zaehlen des Wiederholungslaufs, keine weitere Gateerfuellung.

EN: On the 2026-11-02 delivery, the additional pre-push regex flagged inert
redaction fixture text. Only its source representation changed to structured
construction; scanner rules/exceptions, product code and requirements remain.
All 13 fleet methods passed again in 0.030 s; 106 product hashes, configuration
and ten branch numerators/denominators match. Preserve the prior JSON byte-
identically as historical; the linked correction supplies the current fleet
test binding. Do not double-count the rerun or infer any gate approval.

## Deutsch

Stand 02.11.2026, Mac A, macOS/ARM64; Basis `ae2b552`,
Branch `codex/004-mac-a-coverage-next`. Auftrag: T041-T046 weiterbearbeiten,
ohne Builds, echte Podman-Aufrufe, Installationen, globale Wartung,
Containeraktionen, Commits oder Pushes. Anforderungen und 85/80/100 bleiben.

### Vorpruefung und Messmethode

Feature 004 explizit aufgeloest. Checklisten 16/16 und 36/36 abgeschlossen;
kein offener Punkt. Drei Receipts (79/85/81 Quellen) und unabhaengiges
fuenfteiliges Reihenreview `04d3e335-7b7a-494d-bc78-9587e1659572` aktuell,
Ready. Keine Intake-Bindung erneuert. Ready bewertet Intakes, nicht diese
neuen Tests oder eine technische/menschliche Freigabe.
Ignore-Regeln vorhanden; Messdaten bleiben ausserhalb des Repositorys.

Vorhandenes isoliertes CPython-3.15.2-/coverage.py-7.17.0-venv verwendet,
nichts installiert. Neue Prozesse erhalten eine bereinigte Umgebung ohne
Credential-Variablen und eigene HOME/USERPROFILE/Temp/Cache-Verzeichnisse.
Alle 106 Produktquellhashes und die Messkonfiguration stimmen mit der
[vorigen Zwischenmessung](mac-a-coverage-continuation-2026-11-02.md) ueberein.
Der damalige Git-Head und der heutige unterscheiden sich; die gemessenen
Produktdateien sind jedoch byte-identisch. Alte Messdaten werden wiederverwendet,
nicht als frisch ausgefuehrte Tests bezeichnet.

Ein Branch-Outcome ist ein beobachteter Ausgang eines Programmzweigs.
Die Dateiquote ist hier `covered_branches / num_branches` von coverage.py,
nicht Zeilenabdeckung und nicht die gemittelte Gesamtquote.
Der provisorische Entscheidungskatalog und die separat gemessenen Python-
Zweigziele bleiben unterschiedliche, vollstaendig erhaltene Nenner.

### Frische Tests

| Neue Suite / New Suite | Methoden / Methods | Laufzeit / Duration | Ergebnis / Result |
| --- | ---: | ---: | --- |
| `test_feature004_hardening_branches.py` | 11 | 0,065 s | bestanden / passed |
| `test_feature004_storage_branches.py` | 16 | 0,046 s | bestanden / passed |
| `test_feature004_fleet_branches.py` | 13 | 0,016 s | bestanden / passed |
| `test_feature004_child_and_preview.py` | 4 | 13,545 s | bestanden / passed |

**44 neue Methoden bestanden, null Skips.** Hardening testet Evidenzschema,
Hasharten, Status-/Freigabegrenzen, Preset-Metadaten sowie Modus-/CLI-
Entscheidungen. Storage testet Policy, Registry, Pfade, Prozesssperren,
Kandidaten, atomare Berichte und Adapter-/Cache-Provider-Entscheidungen.
Fleet testet Transportargumente, abgefangene Retry-/Fehlerfaelle, Schema-/
Plan-/Run-Bindungen, Statuswechsel, Budgetmodell, Inventar und Redigierung.
Provider-, Git-, Installer- und Loeschaufrufe dieser Helfer bleiben abgefangen.

Zwei neue Fixtureannahmen wurden korrigiert: sechs statt sieben erforderliche
Lernenden-Diagnosen und ein zwischen Readern zurueckzusetzendes Testresultat.
Keine Produktanforderung wurde geaendert. Nur betroffene kurze neue Suiten
erneut gemessen; fehlgeschlagene Diagnosedaten nicht kombiniert. Die bisherigen
grossen Suiten und realen REV-TEST-TIMING-Faelle wurden nicht wiederholt.
Bestehende Timeouts bleiben unveraendert.

### Kindprozesse und native Vorschau

- `REMOTE_PROGRAM`: Probe und erlaubte Git-Argumente sowie verbotene
  Mutationen als direkte Python-Kindprozesse. Git ist ein aufzeichnender
  Stand-in; kein echtes Git-Fetch, Merge oder Push.
- `SOURCE_PROGRAM`: echte eigene temporaere Read-only-Dateien, passende/
  falsche Hashes, fehlende Datei und beschreibbare Quelle. Keine Hostquelle.
- `PHASE_PROGRAM`: passende Quelle importiert nur einen synthetischen
  Fixture-Worker; Drift scheitert vor Import. Kein echter Fleet-Lauf.
- Bash und PowerShell auf Mac A: vier native Wrapperaufrufe mit dem echten
  Hardening-Kern fuer `All`-Vorschau beziehungsweise falsche Featureauswahl.
  Exit 0 mit ausdruecklich nicht ausgefuehrten Checks beziehungsweise Exit 2,
  unveraenderter Fixturebaum, keine Runtimeaktion.

Die [JSON-Messbindung](mac-a-coverage-next-2026-11-02.json) nennt Quellpfad,
Literalzeilen und SHA-256 der drei eingebetteten Programme. Deren Ausfuehrung
ist belegt, ihre Branchquote aber weiterhin nicht separat gemessen.
Die 48 zuvor unzugeordneten Bereiche werden deshalb nicht um drei reduziert.
Die lokale Interfacebeobachtung `test-ade-sandbox-hardening/Preview` ist kein
vollstaendiges All-Variant-Interface; macOS-PowerShell ersetzt kein Windows.

### Gleichquellige Zwischenmessung

| Datei / File | Vorher / Before | Jetzt / Now | Dateiquote / File Ratio |
| --- | --- | --- | --- |
| `scripts/check-dockerfile-arg-renovate.py` | 64/64 | 64/64 | 100.00 % |
| `scripts/check-home-baseline-lock.py` | 19/22 | 19/22 | 86.36 % |
| `scripts/lib/agentic_workspace_fleet.py` | 43/1274 | 276/1274 | 21.66 % |
| `scripts/lib/audit_retention.py` | 48/50 | 48/50 | 96.00 % |
| `scripts/lib/linux-maintenance-hardening.py` | 139/150 | 139/150 | 92.67 % |
| `scripts/lib/maintenance_container_worker.py` | 56/58 | 56/58 | 96.55 % |
| `scripts/lib/maintenance_execution_context.py` | 87/90 | 87/90 | 96.67 % |
| `scripts/lib/secure_development_hardening.py` | 269/432 | 376/432 | 87.04 % |
| `scripts/lib/workspace_storage_maintenance.py` | 129/336 | 292/336 | 86.90 % |
| `spec-kit/patch-specify-cli.py` | 14/14 | 14/14 | 100.00 % |

Neun von zehn Dateiquoten erreichen mindestens 85 %. Fleet fehlen noch
**998 von 1274 Outcomes**. Der kombinierte Datenbestand umfasst 249 Methoden,
239 ausgefuehrt und zehn historische Skips; nur die oben genannten 44 sind
frisch ausgefuehrt. Rohdateien, argv, Zeitpunkte, Exits und Testhashes stehen
im JSON. Die vorherigen Berichte bleiben historische Eingabestaende;
ihre damaligen Kataloghashes sind keine aktuellen Katalogbindungen.

Alle 106 Produktpfade, 96 Shell-/PowerShell-Dateien, 48 eingebetteten Bereiche,
94 Interface-IDs (88 oeffentliche/UI-IDs plus sechs interne Grenzen) bleiben.
Der Modulkatalog verlinkt diese Teilmessung, der Interfacekatalog bleibt
unveraendert. Keine beobachteten Outcomes oder Pass-Status erfunden.

### Offene Arbeit und Aufgabenstatus

T041-T046 bleiben teilweise/Open; **52/80 Aufgaben erledigt**, kein neuer
Haken, kein T053-Freeze. 85-%-Gesamterfuellung je vollstaendig erfasstem
Sicherheitsmodul, 80-%-Interfacequote und 100 % der geaenderten Interfaces
sind weiterhin nicht belegt. Neun Dateiquoten allein schliessen kein Gate.

Naechster lokaler Schwerpunkt ist Fleet, insbesondere
`StageBTargetTransaction.execute`, `_validate_ci_profiles`,
`classify_repository`, `load_manifest`, `_validate_ci_paths`,
`execute_fleet` und `StageBFleetPreflight.execute`. Nur synthetische,
abgefangene Transaktionen verwenden. Danach weitere Import-/Inline-/
Kindprozessmessung, vollstaendige Shell-/PowerShell-Entscheidungsregister
mit Trace und restliche positive/negative Interfacefaelle.
Owner Maintainer/Security Review; Follow-up vor T053/SC-003-Abnahme;
Trigger Quell-/Test-/Katalog-/Konfigurationswechsel oder neuer Runner.

Windows und Ubuntu/WSL2 bleiben getrennt Open/Blocked nach der
[Uebergabe](coverage-platform-handoff.md). Owner Platform Reviewer,
eigene native Laeufe nach gesonderter Runtimeautoritaet; Trigger verfuegbare
freigegebene Runner, Frist vor AMD64-Nutzung/Abnahme.
Menschliche, WCAG-, Pilot-, finale Image-/SBOM- und unabhaengige technische
Abnahmen bleiben separat offen. Der aktuelle Intake-Review ersetzt diese nicht.

### Reproduktion

Host Mac A, Bash aus Repo-Wurzel. Voraussetzungen: geprueftes vorhandenes
venv (`PYTHON`), eigene leere `TEST_HOME`/`TEST_TMP`/`DATA`-Verzeichnisse,
PowerShell 7 und dieselben Produkt-/Konfigurationshashes. Kein Installieren.
Der folgende Aufruf setzt eine bereinigte Umgebung; keine Credentials erben.

```bash
env -i HOME="$TEST_HOME" USERPROFILE="$TEST_HOME" TMPDIR="$TEST_TMP" \
  PATH="$(dirname "$PYTHON"):/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin" \
  PYTHONDONTWRITEBYTECODE=1 GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null \
  ADE_COVERAGE_REPO="$PWD" \
  COVERAGE_RCFILE="$PWD/scripts/tests/fixtures/hardening-followup/coverage-mac-a.ini" \
  COVERAGE_FILE="$DATA/.coverage" \
  "$PYTHON" -m coverage run -m unittest -v \
  scripts.tests.test_feature004_hardening_branches \
  scripts.tests.test_feature004_storage_branches \
  scripts.tests.test_feature004_fleet_branches \
  scripts.tests.test_feature004_child_and_preview
```

Erwartung: 44 erfolgreiche Methoden. Bei Fehler stoppen, echte Exits/argv
festhalten; kein globaler Fallback, keine Timeouterhoehung.
Vor Kombination alte Rohhashes sowie saemtliche Produkt-/Konfigurationshashes
pruefen. Temporaere Rohdaten zur Sichtung erhalten, nicht stagen.

## English

On 2026-11-02 Mac A used macOS/ARM64 at ae2b552 on the local continuation
branch. Scope is T041-T046 only: no builds, real Podman calls, installation,
global maintenance, container actions, commits or pushes. Keep 85/80/100.

Feature 004 resolved explicitly; checklists passed 16/16 and 36/36. Three
receipts (79/85/81 sources) and the current independent five-target intake
review are valid/Ready. No intake rebinding. Ready is not technical/human
approval. Existing ignore rules suffice; raw measurements remain outside Git.
Reused the isolated CPython 3.15.2/coverage.py 7.17.0 environment without
installing anything. Child environments exclude credentials and use owned
HOME/USERPROFILE/temp/cache. All 106 product hashes and measurement settings
match the prior run, despite a different Git head. Old data remain historical.

The first table lists 44 fresh methods, all passing without skips.
Hardening covers schema/hash/status/authority/preset/CLI boundaries. Storage
covers policy/registry/path/process/candidate/atomic-report/provider dispatch.
Fleet covers intercepted transports/retries, schemas/bindings, state, budgets,
inventory and redaction. Git/provider/installer/delete calls are intercepted.
Two fixture errors (six required learner diagnostics and independent reader
state) were corrected without changing requirements. Only affected short new
suites were repeated; failed diagnostic data are excluded. Existing broad
suites and real timing cases were not rerun; no timeout was increased.

Direct isolated children exercise the exact REMOTE_PROGRAM, SOURCE_PROGRAM
and PHASE_PROGRAM literals. Remote Git is a recorder; source checks use owned
read-only temporary files; the phase program imports a synthetic worker only.
Literal hashes/locations are bound in JSON. This is execution evidence, not a
separate branch measurement or subtraction from the 48 unresolved regions.
Four native Bash/macOS-PowerShell wrapper calls use the real shared hardening
core for All preview and wrong-feature rejection: exits 0/2, unchanged fixture
tree and no runtime operation. Preview success explicitly means no checks run.
This local interface observation is not complete all-variant acceptance.

The second table measures distinct branch outcomes, not line coverage or an
averaged gate score. Nine named Python files reach 85%. Fleet still misses
998/1274 outcomes. Same-source aggregation holds 249 discovered methods,
239 executed and ten historical skips, not 249 fresh executions. JSON binds
raw hashes, arguments, times, exits and tests. Earlier reports/catalog hashes
remain historical. Preserve the separate provisional outcome model and all
106 paths, 96 shell/PowerShell files, 48 nested regions and 94 interfaces
(88 public/UI plus six internal). Module catalog links partial results;
interface catalog, outcome labels and pass states remain unchanged.

T041-T046 stay partial/Open, 52/80 checked, no T053 freeze. Complete module
85%, interface 80% and changed-interface 100% gates remain unproven.
Next prioritize the named fleet classification/manifest/CI-profile/preflight/
transaction functions using synthetic intercepted operations, then child/
inline attribution and complete shell/interface traces. Maintainer/Security
Review owns follow-up before T053/SC-003, reevaluated on source/test/catalog/
configuration changes or runner availability.

Windows/WSL2 remains independently Open/Blocked under the linked handoff.
Platform Reviewer owns separate native runs after explicit runtime authority
when approved runners become available, before AMD64 use/acceptance. Human,
WCAG, pilot, final image/SBOM and independent technical reviews remain separate.

Reproduction is host Bash from the repository root, with the verified existing
venv, owned empty TEST_HOME/TEST_TMP/DATA directories and PowerShell 7. The
command above clears credentials and expects 44 passing methods. Stop on
failure, record real exits/arguments, never increase budgets or use actual
maintenance as fallback. Verify raw hashes and identical product/configuration
before combination; retain owned temporary evidence for review outside staging.
