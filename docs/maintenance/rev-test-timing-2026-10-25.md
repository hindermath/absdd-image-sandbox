# REV-TEST-TIMING: Ursachen und Behebung / Causes and Fix

## Status Und Grenze / Status and Boundary

DE: `Resolved` fuer die untersuchten lokalen Wartungs-Fixturetests auf macOS
mit Python 3.15.0 und 3.14.9. Fixtures sind kuenstliche Testumgebungen; sie
fuehren keine globale Paketwartung aus. Die frueheren Timeout-Beobachtungen
bleiben im [vorigen Session-Log](../security/agent-session-log/2026-10-25-1211.md)
erhalten. Dieser neue Nachweis ersetzt nur deren offenen Timing-Status fuer
den unten gebundenen Quellstand, keine Plattform- oder Sandbox-Freigabe.

EN: Resolved for the local maintenance fixtures tested on macOS with Python
3.15.0 and 3.14.9. Fixtures are synthetic environments, not global package
maintenance. The previous session log retains the earlier failures. This
evidence supersedes only their timing status for the source hashes below,
not platform or sandbox approval.

## Ursachen / Causes

DE: Der Required-CLI-Drift-Fall scheiterte vor der Korrektur erneut an seiner
unveraenderten 20-Sekunden-Grenze. Ein isolierter, instrumentierter Lauf
startete Python 33-mal, oft nur zum wiederholten Lesen und Filtern derselben
Registries. Der Diagnoseprozess wurde nach 20 Sekunden beendet, bevor er
regulaer abgeschlossen war. Das belegt vermeidbaren Start-/Parsing-Aufwand,
aber keinen allgemeinen Fehler in Python 3.15.

EN: The required-CLI-drift case again exceeded its unchanged 20-second limit.
An isolated traced run launched Python 33 times, frequently rereading and
filtering the same registries. The diagnostic process was stopped at 20
seconds before normal completion. This demonstrates avoidable launch/parsing
cost, not a general Python 3.15 defect.

DE: Der Klassifikationstest setzte ausserdem voraus, dass kurze
`/usr/bin/env bash`-Fixtures garantiert vor einer Sekunde beendet sind.
Ein langsamer Launcher darf jedoch korrekt als TimedOut gelten. Ein
Exitcode-/Schwaerzungstest soll nicht von dieser Startzeitannahme abhaengen.
Der Testtreiber und per PATH gestartete Helper konnten zudem verschiedene
Python-Versionen verwenden.

EN: The classification test also assumed short env/bash fixtures would
always finish within one second. A slow launcher may legitimately time out;
exit classification and redaction tests should not depend on that assumption.
The test driver and PATH-resolved helpers could also use different Pythons.

## Korrektur / Correction

- Registry-Auswahldaten einmal in den privaten lauflokalen Arbeitsordner
  schreiben; feste TSV-Dateien mit Shell-Builtins lesen. Kein globaler Cache.
  / Snapshot registry selections in the private per-run directory and read
  fixed TSV files using shell builtins; no global cache.
- Verfuegbarkeit und Ergebnisse nicht cachen: Pruefungen vor/nach Installation
  bleiben echte Aufrufe. Pflicht-/Optional-, Plattform- und Argumentfilter
  behalten ihre Bedeutung. / Availability and results remain live; required,
  optional, platform and argument semantics are retained.
- Fehlerhafte Registry oder fehlender Snapshot bricht ab und publiziert ein
  Fehlerergebnis statt leere Auswahlen als Erfolg auszugeben. TSV-Felder mit
  Zeilen-/Tabulatorinjektion werden abgewiesen. / Invalid or missing snapshots
  fail closed; no empty-success substitute or multiline TSV injection.
- Exitcode-, Capability- und Schwaerzungslogik deterministisch pruefen; echte
  Nonzero-Prozesse und haengende Prozessgruppen weiterhin separat testen.
  Direkte POSIX-Launcher statt zusaetzlicher env/bash-Ketten. / Separate
  deterministic classification from real nonzero-exit and timeout tests;
  use direct POSIX launchers.
- Testhelper und temporaere `python3`-Verknuepfung verwenden denselben
  ausgewaehlten Interpreter. Keine Host-PATH-/Versionsumstellung. / Helpers
  use the selected test interpreter without changing global PATH or versions.

DE: Die Grenzen bleiben unveraendert: 20 Sekunden fuer den Fixture-
Wartungslauf, eine Sekunde fuer den kurzen Probe-Fall, 0,2 Sekunden fuer den
haengenden Prozess und drei Sekunden fuer die bestehende Laufzeitassertion.
Keine Retry-until-green-Logik oder neue Plattform-Skips hinzugefuegt.

EN: Existing limits remain unchanged: 20 seconds for a fixture maintenance
run, one second for the short probe, 0.2 seconds for a hanging process, and
the existing three-second elapsed-time assertion. No retry-until-green logic
or new platform skips.

## Nachweis / Evidence

| Pruefung / Check | Ergebnis / Result |
|---|---|
| Instrumentierter Required-Drift-Lauf, finaler Quellstand / traced drift run, final sources | 18 statt 33 Python-Starts; regulaeres Ende nach 4,390s mit erwartetem Exit 1 wegen fehlendem Pflichtwerkzeug / 18 rather than 33 launches; normal exit after 4.390s, expected missing-required-tool exit 1 |
| Python 3.15.0: Wartung plus fokussierte Regressionen und Agent-Paritaet / maintenance plus focused regressions and agent parity | 78 Tests: 76 bestanden, 2 bestehende Linux-only-Skips, 0 Fehler; 208,429s / 76 passed, two existing Linux-only skips, zero failures |
| Python 3.14.9: Wartung / maintenance | 24 Tests: 22 bestanden, 2 bestehende Linux-only-Skips, 0 Fehler; 82,591s / 22 passed, two existing skips, zero failures |

DE: Die zwei ausgelassenen Faelle betreffen echte Linux-Swift-Bereitstellung.
macOS-Fixtures sind keine native Linux-/Windows-/WSL2-Abnahme. Nach der
letzten Codeaenderung wurde die finale Matrix erneut ausgefuehrt; fruehere
Zwischenlaeufe werden nicht als Beleg fuer spaetere Aenderungen ausgegeben.

EN: The two skips require actual Linux Swift provisioning. macOS fixtures
do not establish native Linux, Windows or WSL2 acceptance. The final matrix
was rerun after the last code change; intermediate runs do not prove later edits.

## Gebundener Quellstand / Bound Sources

| Datei / File | SHA-256 |
|---|---|
| `scripts/maintain-agentic-brew-apps.sh` | `bf89331b0b68fc6d770c3efcc40c8f9d0cb20dabab0e15216f6f67e85b7b6598` |
| `scripts/lib/linux-maintenance-hardening.py` | `00cd96654100aaf2ab2355fceae22f7a90f98e638616203e07a166317c9ca864` |
| `scripts/tests/test_linux_maintenance_hardening.py` | `3cfbf5e718ef25e6384de74ad86547bf49e5cc58765554ad5c5de632cba3b6b5` |

DE: Die 81 Quellenbindungen des vorigen Intake-Inhaltsreviews bleiben
unveraendert. Diese drei Code-/Testdateien waren keine gebundenen Inputs
jenes Urteils; es wird deshalb nicht als unabhaengiges Review dieser neuen
Implementierung ausgegeben. Historische Reports/Logs bleiben unveraendert.
Kein Container-Build, Neustart, Commit oder Push. Weitere Abschlusschecks
stehen im [neuen Session-Log](../security/agent-session-log/2026-10-25-1303.md).

EN: All 81 prior intake-content review bindings remain unchanged. These
three implementation/test files were not bound inputs of that verdict, so
it is not claimed as independent review of this new code. Historical reports
and logs remain unchanged. No container build, restart, commit or push.
The new session log records the remaining closeout checks.
