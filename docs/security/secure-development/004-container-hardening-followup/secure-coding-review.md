# Secure-Coding-Prüfung / Secure coding review

## Deutsch

**Zwischenstand 2026-10-31: Open.** Dieses Dokument legt die Prüfmethode vor Codeänderungen fest. Es enthält noch keine gemessene Quote. Der namentliche Quellumfang steht in `coverage-modules.json`; öffentliche Modi und Varianten stehen in `interface-catalog.json`. Nach jeder Quell- oder Katalogänderung werden Hash, Nenner, Fälle und Messung erneut gebunden. Ein fehlender Zweig oder eine fehlende Plattform bleibt sichtbar.

**T040, isolierter REV-TEST-TIMING-Lauf am 2026-10-31:** Drei gezielte Unittests bestanden (`test_probe_classifies_timeout_capability_and_redacts_paths`, `test_probe_captures_real_stderr_classifies_capability_and_redacts_paths`, `test_probe_timeout_is_bounded`). Darin laufen `/bin/sh`-stderr, Capability-Fehler, Pfadredaktion und ein echter Timeout über den vorhandenen begrenzten Probeprozess. Keine Host-Wartung wurde gestartet und kein Timeout erhöht. Das ist ein konkreter Regressionstest, keine Modul- oder Interfacequote.

**Q4-Messvoraussetzung:** Das Host-Python und das getrennte ARM64-Testimage melden für `python3 -m coverage --version` Exit 1, `No module named coverage`. Eine isolierte Offline-Auflösung von `coverage==7.10.7` unter `/private/tmp` scheiterte, weil das Paket nicht im lokalen Cache liegt. Deshalb fehlen echte Python-Branch-Arcs und Roh-JSON; `covered_branches/num_branches` wird für keines der zehn benannten Python-Module behauptet. Auch für die Shell-/PowerShell-Outcomes der 106 Dateien und die 94 Interface-IDs gibt es kein vollständiges Trace-Register. Von 81 öffentlichen Modi und sieben kritischen TUI-Flows beanspruchen 84/88 mindestens Windows oder Ubuntu/WSL2; mit nur macOS sind höchstens 4/88 überhaupt vollständig über alle Varianten ausführbar. Das ist eine theoretische Obergrenze, kein bestandener Zähler. T041–T046, T053 und G004-04 bleiben Open; der Nenner wird nicht verkleinert.

**Inventarprüfung T006/T007 am 2026-10-31:** Zwei getrennte Codex-Subagenten prüften die Kataloge unabhängig. T006 umfasst 106 aktuelle Quellpfade und 48 separat zugeordnete eingebettete Codebereiche; der Entscheidungsnenner ist vorläufig und keine gemessene Abdeckung. T007 umfasst 81 öffentliche Modi, sechs interne Grenzen und sieben kritische TUI-Flows mit eindeutigen IDs und Varianten. Beanstandungen zu eingebettetem Python, Varianten, Dokumentationsquellen und TUI-Fällen wurden vor der erneuten Freigabe für T012 korrigiert. Testfälle, Quoten und native Plattformwirkung bleiben Open; spätere Quelländerungen verlangen betroffene Neubindung.

**Erneuter unabhängiger Inventarreview nach den US1/US2-Quelländerungen:**
T006 prüfte zunächst 106/106 aktuelle Quellhashes, 5.394 vorläufige
Entscheidungsstellen und 48 eingebettete Bereiche. Nach der engen Korrektur
des Dockerfile-ARG-Validators wurde dessen Quellhash neu gebunden und die
Deltaänderung unabhängig erneut geprüft: 106/106 Hashes passen, 48 Bereiche,
5.395 vorläufige Entscheidungsstellen und 11.313 Kandidaten-Outcomes,
null beobachtete Outcomes. T007 prüfte 94 eindeutige
IDs (81/6/7), aktuelle Quellhashes und die neuen Audit-/SBOM-/Feature-004-
Eingaben sowie den TUI-Degraded-Flow. Zwei zunächst fehlende TUI-Quellen
und `-Engine` wurden im Katalog ergänzt und danach erneut bestanden.
`observedOutcomes` bleibt leer; das ist keine Q4-Messung.

| Bezug | Feature-004-Prüfpunkt | Geplanter Beleg |
| --- | --- | --- |
| NIST SSDF 1.1 PO.1 / PS.1 | Anforderungen und geschützte Quellen/Änderungen binden | Spec-/Plan-/Intake-Hashes, Branch und Review; keine behauptete Plattformregel. |
| NIST SSDF 1.1 PW.4 / PW.5 | Gesicherte Komponenten wiederverwenden und sicher codieren | Gepinnte Herkunft; Python-Kern, begrenzte Wrapper, dokumentierte Eingabe-/Fehlerverträge. |
| NIST SSDF 1.1 PW.7 / PW.8 | Quellcode untersuchen und ausführbares Verhalten testen | Unabhängiger Katalogreview, statische Analyse, isolierte positive und negative Tests; direkte Prozessgrenze. |
| CWE-22 / CWE-59 | Pfaddurchlauf / symbolische Links | Kanonische Wurzel, direkte reguläre Datei, Identitäts-/Typprüfung unmittelbar vor Wirkung; Link-/Race-Fälle. |
| CWE-78 / CWE-88 | OS-Befehle / Argumente | Keine Shell-Interpolation aus Fremdeingaben, argv-Reihenfolge und Optionszeichen testen. |
| CWE-200 / CWE-532 | Offenlegung / Protokollierung | Fehler und Vorschau redigieren; kein Prompt, Token, DB-/WAL-/SHM-Inhalt als Evidence. |
| CWE-362 / CWE-367 | Konkurrenz / Check-use-Rennen | Eigene exklusive Sperre, Identitätsprüfung und fail-closed bei nicht belegbarer nativer Sicherheit; kein Versprechen atomaren Rollbacks. |
| CWE-20 / CWE-754 | Eingabeprüfung / Ausnahmebehandlung | Strict ISO-Name, Statuskombinationen, Exitklassen und fehlende Belege explizit abweisen. |
| CWE-829 / CWE-494 | Fremde Komponenten / Downloads | Herkunft, Digest, Signatur wo vorhanden, negative Hash-Fälle und feste Version dokumentieren. |

Der CWE-Bezug ist eine zielgerichtete Schwächenliste für die aktuellen Daten- und Prozessgrenzen; sie behauptet keine Vollständigkeit der CWE Top 25. Für Python zählt `coverage.py --branch` nur tatsächlich gemessene Zweig-Outcomes je Modul. Für Bash und PowerShell zählt ein statisch reviewter Entscheidungsnenner mit ausgeführten positiven und negativen Outcomes; Zeilen-/Command-Coverage ist nur ergänzend. Q4 fordert mindestens 85 % je sicherheitskritischem Modul und 80 % logische Interfaces mit beiden Fallarten für alle beanspruchten Varianten. Fehlende Messung wird nicht als 0 oder als Pass umgedeutet. T045 ist Zwischenmessung, T053 finale Messung nach Code-Freeze.

Nichttriviale Änderungen erhalten didaktische Kommentare zu Schutzgrenze, Vorbedingung und Fehlerfall: besonders Retention-Dateiselektion, eigener Lock, Export-Identität, argv-Weitergabe und Feature-Evidence-Hashbindung. Kommentare dürfen keine Sicherheit behaupten, die der Code nicht erzwingt. Owner: Repository Maintainer; Reviewer: Security Review. Trigger: Code-/Katalogänderung oder neue Angriffsfläche.

## English

**Interim status 2026-10-31: Open.** This is the review method, not a measured pass. Bind source hashes, module decisions, logical interfaces and platform variants to executed cases. Apply SSDF 1.1 requirements/source protection, secure reuse/coding, code review and executable testing. Check path and link handling, command arguments, disclosure, races, input validation and downloaded components against the mapped CWE examples above. Python branch data and reviewed Bash/PowerShell outcome traces are different evidence types; line counts do not replace decision coverage. Keep missing modules, variants and native observations Open. Re-measure after every relevant code or catalog change before claiming the Q4 thresholds.

Three focused T040 tests passed on 2026-10-31, covering real `/bin/sh` stderr, capability classification, path redaction and a bounded timeout without host maintenance. This is regression evidence only. Host Python and the separate ARM64 image lack `coverage.py`; isolated offline resolution of `coverage==7.10.7` found no cached package. Of 88 public modes and critical TUI flows relevant to the 80% gate, 84 require at least one unavailable Windows or Ubuntu/WSL2 variant. At most four could be fully exercised on the available Mac; that is a theoretical ceiling, not observed passing coverage. No Python branch ratio, complete Shell/PowerShell outcome trace or interface ratio is claimed. T041–T046, T053 and G004-04 remain Open.

Two separate Codex subagents reviewed the T006/T007 catalogs on 2026-10-31. Their corrected inventories are ready as T012 inputs: 106 source paths, 48 nested code regions, 81 public modes, six internal boundaries and seven critical TUI flows. Decision counts are provisional; executed cases, coverage thresholds and native behavior remain Open. Rebind affected hashes and review after source changes.

After the US1/US2 source edits, two independent reviewers checked all 106
source hashes, 5,394 provisional decision sites and 48 nested regions, plus
all 94 unique interface IDs (81 public, six internal, seven TUI). The catalog
was corrected for two TUI flow sources and `-Engine`, then passed re-review.
Observed outcomes are still empty; Q4 coverage is not measured.
After the Dockerfile-ARG-validator correction, an independent delta review
passed all 106 current hashes, 48 nested regions, 5,395 provisional decision
sites and 11,313 candidate outcomes. The affected source hash was rebound;
observed outcomes remain zero.

## Mac-A-Teilmessung vom 02.11.2026 / Mac-A partial measurement on 2026-11-02

DE: Der Stand vom 31. Oktober oben bleibt historisch. Nach erneuerten
Quellenbindungen und unabhaengigem Ready wurde coverage.py 7.17.0 in einem
eigenen temporaeren CPython-3.15.2-venv mit geprueftem ARM64-Wheel bereitgestellt.
169 Tests mit zehn Skips bestanden; nur die gezielte Pin-/Patcher-Ergaenzung
mit acht Tests wurde danach ausgefuehrt. Finale Daten: 177 Testmethoden,
167 ausgefuehrt, zehn Skips, unveraenderte Produktquellen und Grenzwerte.

DE: [Bericht und Grenzen](mac-a-coverage-2026-11-02.md) sowie
[hashgebundene Messdatenuebersicht](mac-a-coverage-2026-11-02.json) zeigen
vier numerische Dateiquoten ab 85 %: Dockerfile-ARG-Validator 100 %, Home-
Baseline-Validator 86,36 %, Audit-Retention 96 %, Spec-Kit-Patcher 100 %.
Sechs weitere Python-Dateien liegen darunter. Diese Dateiquoten beweisen
weder die vollstaendige Zuordnung der 48 eingebetteten Bereiche noch
Bash-/PowerShell-Entscheidungsabdeckung oder alle Interfacevarianten.
Insbesondere ist die Patcher-Dateiquote keine Quote ihres injizierten Codes.
Der vollstaendige 106-Dateien-/Interface-Nenner bleibt erhalten; T041-T046,
T053 und G004-04 bleiben als Gesamtaufgaben Open. Keine Coverage-Senkung,
kein finaler Freeze, keine Plattform-/Human-Abnahme.

DE: Owner der weiteren Messluecken: Maintainer/Security Review. Follow-up:
fehlende Zweige der sechs Module, Inline-/Kindprozesse und Shell-/PWS-
Outcomes mit sicheren Fixtures bearbeiten. Trigger: vor T053 und bei
Quell-/Test-/Katalogaenderung. Windows/WSL2 erhalten getrennte Auftraege
nach der [vorbereiteten Uebergabe](coverage-platform-handoff.md).

EN: Preserve the historical 31 October record above. After renewed bindings
and independent Ready, an owned temporary CPython 3.15.2 environment used
the SHA-verified ARM64 coverage.py 7.17.0 wheel. Baseline 169 tests with ten
skips passed; only eight targeted pin/patcher tests followed. Final data
cover 177 test methods, 167 executed and ten skipped, with unchanged product
sources and thresholds. The linked report/JSON bind actual inputs and limits.

EN: Four named file ratios reach 85%: ARG validator 100%, baseline validator
86.36%, retention 96%, patcher 100%. Six Python files remain below threshold.
File ratios do not prove 48 nested programs, shell/PowerShell decisions or
all interface variants; the patcher ratio does not measure injected code.
Preserve all scope and leave complete T041-T046/T053/G004-04 Open. No lower
threshold, freeze or platform/human acceptance. Maintainer/Security Review
owns safe missing-branch/child/shell fixtures before T053 and after source,
test or catalog changes; separate Windows/WSL2 work follows the linked handoff.

## Gezielte Fortsetzung / Targeted Continuation

DE: Die obige erste Messung bleibt historischer Zwischenstand. Der
[Fortsetzungsbericht](mac-a-coverage-continuation-2026-11-02.md) mit
[aktueller Messbindung](mac-a-coverage-continuation-2026-11-02.json) ergaenzt
28 erfolgreiche Testmethoden ohne Skips, nur isolierte neue Faelle. Gleiche
106 Produktquellen/Konfiguration: 205 Methoden im kombinierten Bestand,
195 ausgefuehrt und zehn historische Skips, nicht 205 frische Ausfuehrungen.
Linux-Maintenance 139/150 (92,67 %), Worker 56/58 (96,55 %), Kontext 87/90
(96,67 %): jetzt sieben von zehn numerischen Dateiquoten ab 85 %.
Fleet/Hardening-Kern/Storage bleiben darunter. Der Modulkatalog verweist auf
Teilmessungen, der Interfacekatalog bleibt unveraendert. Nenner/Outcomes
werden nicht geaendert. 52 native
Shell-/PWS-Wrapperaufrufe gegen aufzeichnenden Fake-Kern sind Adapterbelege,
keine komplette Interface-/Windows-Abnahme. T041-T046/T053/G004-04 Open;
85/80/100 und alle Plattform-/Human-Grenzen unveraendert. Maintainer/Security
Review bearbeitet verbleibende Python-/Nested-/Shell-/Kernluecken vor T053;
Trigger Quell-/Test-/Katalogwechsel. Keine Builds oder Containeraktionen.

EN: The earlier measurement remains historical. The linked continuation adds
28 passing methods without skips using isolated fixtures. Identical 106
product hashes/configuration yield 205 combined methods, 195 executed and ten
historical skips, not 205 fresh executions. Linux maintenance reaches 139/150
(92.67%), worker 56/58 (96.55%), context 87/90 (96.67%): seven named files
reach 85%. Fleet/hardening/storage still do not. The module catalog links
partial measurements; interface catalog, denominators and outcomes stay unchanged.
Fifty-two native shell/PowerShell
wrapper invocations use a recording fake core: adapter proof, not complete
interface/Windows acceptance. Keep T041-T046/T053/G004-04 Open and 85/80/100
unchanged. Maintainer/Security Review owns remaining Python/nested/shell/core
gaps before T053, reevaluated on source/test/catalog change. No build/runtime.
