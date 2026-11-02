# Mac-A-Coverage: Fortsetzung / Continuation

## Deutsch

Stand: 02.11.2026, Mac A, macOS/ARM64, CPython 3.15.2, coverage.py
7.17.0 im vorhandenen isolierten venv. Basis `e115fa8`, Branch
`codex/004-mac-a-coverage`, uncommittierte Tests/Nachweise.
Quellenbindungen aktuell; unabhaengiges fuenfteiliges Reihenreview
`04d3e335-7b7a-494d-bc78-9587e1659572`: Ready. Das ist keine technische
Abnahme dieser neuen Tests. Keine Builds, Containeraktionen oder Lieferung.

### Gezielte Ergaenzungen

- 15 Delegationstests: Vertrags-/Quellen-/Mountgrenzen, Schreibbarriere,
  Identitaet, Argumente, Reparaturstufen, Registry-Translation, Storage-Vorschau.
  Alle Transport-/Storage-Aufrufe abgefangen; kein echter Podman.
- Neun Registrytests: strikte Eingaben/Resultate, SHA-256, Swift-Vertrag,
  selektive Archivextraktion, TSV-Sequenzen, Zusammenfassung und Feldgrenzen.
  Nur eigene temporaere Dateien, keine Installation oder Wartung.
- Vier Wrappertests mit 52 echten Bash-/PowerShell-Aufrufen auf Mac A:
  sieben Modi, Vorschau, Argumenterhalt, Parserablehnung und Weitergabe
  von Kern-Exitcodes 0/2/3. Der Kern ist ein aufzeichnender Stand-in.
  Das belegt Adapter, nicht Kern-/Runtime- oder Plattformabnahme.

**28 neue Testmethoden bestanden, null Skips.** Letzte Helferlaeufe:
15 Tests/0,102 s und neun Tests/0,085 s. Nur diese kurzen Suiten nach
Fixturebereinigung erneut ausgefuehrt; Wrapperlauf (78,561 s) und bisherige
169-/8-Testlaeufe nicht wiederholt. Reale REV-TEST-TIMING-Belege bleiben
Nachweise des vorigen identischen Produktquellstands, nicht neu ausgefuehrt.
Bestehende Timeoutgrenzen unveraendert.

### Messwerte

Nur identische 106 Produktquellhashes und Messkonfiguration kombiniert:
205 Testmethoden, davon 195 ausgefuehrt und zehn zuvor dokumentierte Skips.
Das sind nicht 205 neue Tests. Die [JSON-Messuebersicht](mac-a-coverage-continuation-2026-11-02.json)
bindet Tests, argv, Zeit, Exitcodes und Rohdatenhashes.
Der [vorige Bericht](mac-a-coverage-2026-11-02.md) bleibt historische Zwischenmessung.

| Datei / File | Vorher / Before | Jetzt / Now | Branchquote / Branch Ratio |
| --- | --- | --- | --- |
| `scripts/check-dockerfile-arg-renovate.py` | 64/64 | 64/64 | 100.00 % |
| `scripts/check-home-baseline-lock.py` | 19/22 | 19/22 | 86.36 % |
| `scripts/lib/agentic_workspace_fleet.py` | 43/1274 | 43/1274 | 3.38 % |
| `scripts/lib/audit_retention.py` | 48/50 | 48/50 | 96.00 % |
| `scripts/lib/linux-maintenance-hardening.py` | 85/150 | 139/150 | 92.67 % |
| `scripts/lib/maintenance_container_worker.py` | 34/58 | 56/58 | 96.55 % |
| `scripts/lib/maintenance_execution_context.py` | 40/90 | 87/90 | 96.67 % |
| `scripts/lib/secure_development_hardening.py` | 269/432 | 269/432 | 62.27 % |
| `scripts/lib/workspace_storage_maintenance.py` | 129/336 | 129/336 | 38.39 % |
| `spec-kit/patch-specify-cli.py` | 14/14 | 14/14 | 100.00 % |

Sieben statt vier **Dateiquoten** erreichen 85 %. Keine vollstaendige
Modulabnahme: provisorischer Entscheidungskatalog und coverage.py-Zweigziele
haben unterschiedliche Nenner. Beide erhalten. Alle 106 Dateien,
48 eingebetteten Bereiche, 96 Shell-/PowerShell-Dateien und 94 Interface-IDs
bleiben im Umfang. Oeffentlicher/UI-Nenner weiterhin 88, sechs interne
Grenzen gesondert. Keine globale 80-%- oder 100-%-Erfuellung behauptet.

Der Modulkatalog verlinkt Teilmessungen, ohne provisorische Outcomes
umzubenennen. Der Interfacekatalog bleibt unveraendert; Adaptertests zaehlen
nicht als vollstaendige Interfacefaelle.
macOS-PowerShell ersetzt kein Windows. Der Kataloghash im vorigen Bericht
belegt dessen damaligen Stand; aktuelle Kataloghashes stehen im neuen JSON.

### Status und Folgearbeit

T041-T046 bleiben **teilweise bearbeitet/Open**; keine neue Checkbox:
52/80 erledigt, kein T053-Freeze. Anforderungen, Nenner und 85/80/100 bleiben.
Naechster lokaler Umfang: Fleet, Hardening-Kern und Storage gezielt testen;
eingebettete Programme/Kindprozesse zuordnen; vollstaendige reviewed Shell-/
PowerShell-Outcome-Register mit Trace und echte Kernfaelle ergaenzen.
Zeilen-Traces ersetzen keine Branchquote.
Owner Maintainer/Security Review; Follow-up vor T053/SC-003-Abnahme;
Trigger Quell-/Test-/Katalogwechsel oder neuer Runner.

Die [Windows-/WSL2-Uebergabe](coverage-platform-handoff.md) bleibt Plan,
keine Runtimeautoritaet. Varianten Open/Blocked; Owner Windows/WSL2 Platform
Reviewer; Follow-up getrennte native Laeufe desselben geprueften Stands;
Trigger verfuegbare freigegebene Runner, Frist vor AMD64-Abnahme.
Kein Commit/Push, Lifecycle-, Produktquellen- oder Lerncontainerwechsel.

### Reproduktion

Host Mac A, Bash aus Repo-Wurzel. Voraussetzung: vorhandenes geprueftes
venv, eigenes temporaeres HOME/USERPROFILE/Cache und bereinigte Umgebung
ohne Credential-Variablen wie im vorigen Messbericht. PYTHON bezeichnet
dessen Python, DATA ein eigenes neues Messverzeichnis. Keine Installation.

```bash
export ADE_COVERAGE_REPO="$PWD"
export COVERAGE_RCFILE="$PWD/scripts/tests/fixtures/hardening-followup/coverage-mac-a.ini"
export COVERAGE_FILE="$DATA/.coverage"
"$PYTHON" -m coverage run -m unittest -v scripts.tests.test_feature004_delegation_coverage scripts.tests.test_feature004_registry_coverage scripts.tests.test_feature004_wrapper_outcomes
```

Erwartung: 28 erfolgreiche Methoden. Bei Fehler stoppen, echte argv/Exits
festhalten, keine Timeouterhoehung oder Host-/Container-Fallback.
Vor Kombination alle Produktquellen/Konfiguration mit Altlaeufen abgleichen.
Nur der jeweils letzte unveraenderte Teststand gilt als aktueller Testbeleg.
Rohdaten bleiben temporaer zur Sichtung erhalten, ausserhalb des Git-Index.

## English

On 2026-11-02 Mac A used macOS/ARM64, CPython 3.15.2 and the existing isolated
coverage.py 7.17.0 environment at base e115fa8. The current five-target intake
review is Ready, not technical approval of this continuation.
No builds, container actions, commits or pushes.

Fifteen delegation methods cover contracts, source/mount/identity boundaries,
mutation barriers, arguments, repair stages, registry translation and storage
preview. All transport/storage calls are intercepted. Nine registry methods
cover malformed input/results, SHA-256, Swift contracts, selective extraction,
TSV sequencing, summaries and fields. Only owned temporary files are touched.

Four adapter methods execute 52 real macOS Bash/PowerShell wrappers with a
recording fake Python core: seven modes, preview, literal arguments, parser
rejection and exits 0/2/3. These are not shared-core/runtime or Windows proofs.
All 28 new methods passed without skips. Only the short helper suites were
rerun after cleanup: 15 tests/0.102 s and nine/0.085 s. The 78.561-s wrapper
run and previous 169-/8-test runs were not repeated. Existing real-process
timing evidence is historical same-source proof; no timeout was increased.

The table compares distinct Python branch outcomes, not line percentages.
Seven named-file ratios now reach 85%, versus four previously. Only identical
106 product hashes/configuration were combined: 205 discovered methods,
195 executed and ten historical skips, not 205 freshly executed tests.
The linked JSON binds tests, commands, times, exits and raw artifact hashes.

File ratios do not replace the provisional decision model or prove complete
modules. Retain 106 files, 48 nested regions, 96 shell/PowerShell files and
94 interfaces, including 88 public/UI IDs and six separate internal boundaries.
No global 80% or changed-interface 100% pass is claimed. The module catalog links
partial evidence; the interface catalog stays unchanged. Adapters do not complete
required variants. The earlier catalog hash remains a historical snapshot;
current bindings are in the new JSON. macOS PowerShell is not Windows.

T041-T046 stay partial/Open, 52/80 tasks checked, no T053 freeze. Keep
requirements, scope and 85/80/100 unchanged. Remaining Mac-A work is targeted
fleet/hardening/storage tests, attributed nested/child code, complete reviewed
shell outcome traces and real core cases. Owner Maintainer/Security Review;
follow-up before T053/SC-003; reevaluate on source/test/catalog change or new
runner. Line traces alone are not branch coverage.

The platform handoff remains a plan, not runtime authority. Windows/WSL2 stays
Open/Blocked; Platform Reviewer owns distinct same-reviewed-head native runs
when approved runners become available, before AMD64 acceptance.
No lifecycle, production source or learner-container changes.

Reproduction uses host Bash from the repository root, verified isolated venv,
owned HOME/USERPROFILE/temp/cache and a credential-free environment as in the
prior report. PYTHON selects that interpreter and DATA a new owned directory.
Expect 28 passing methods; stop on errors, record real exits and never enlarge
budgets or fall back to actual maintenance. Combine identical product sources/
configuration only, retaining current test hashes. Preserve temporary raw
evidence for review outside Git staging.
