# Mac-A-Coverage: Teilmessung / Mac-A coverage: partial measurement

## Deutsch

**Stand:** 2026-11-02. **Ergebnis: Open**, keine Gesamt- oder Plattformabnahme.
Der Ausgangscommit ist `e115fa863e754a83eff212c72f130f6f8543a988`;
Quellenaktualisierung, Tests und diese Berichte sind uncommittet auf
`codex/004-mac-a-coverage`. Der Stand ist kein finaler T053-Code-Freeze.
Maschinenlesbare Eingaben, Quell-/Test-/Loghashes und argv stehen im
[Messbericht](mac-a-coverage-2026-11-02.json).

### Zuerst abgeschlossene Quellenpflege

Die sieben PR-107-Quellen wurden mit bytegleichen Vorgängerarchiven in drei
betroffenen Receipts nachgebunden. 256 lokale Quellenreferenzen sind aktuell;
19 Archive wurden geprüft. Alle fünf Intake-Texte und ihre Anforderungen
blieben unverändert. Der unabhängige Fünf-Ziel-Reihenreview
`04d3e335-7b7a-494d-bc78-9587e1659572` ist Ready, ohne Findings.
Das bezeichnet Anforderungsqualität, keine technische Abnahme. Statusfolge
bleibt Completed / Eligible / Blocked / Blocked / Blocked.

### Tatsächlich ausgeführter Umfang

- Host macOS/ARM64, CPython 3.15.2, coverage.py 7.17.0 mit C-Erweiterung.
  Das offizielle [PyPI-Wheel](https://pypi.org/project/coverage/7.17.0/) wurde
  vor der Offline-Installation ins eigene temporäre venv gegen SHA-256
  `66efc0fb99cee34626fc17d3adac9c3cd816bfdad563bb1e983c3ef432f566d4`
  geprüft. Keine globale Installation und keine Imageänderung.
- 13 Testmodule: **169 Tests, 10 Skips, 507,711 s, Exit 0**.
  Die zwölf neuen Audit-Fälle prüfen Datum, Vorschau, Dateitausch,
  Recheck-Fehler, ungültigen Export, Run-ID, Doppelsätze, Übergröße,
  Kodierung und CLI-Fehler ausschließlich mit synthetischen Daten.
- Danach nur die aus gemessenen Lücken abgeleitete Pin-/Patcher-Ergänzung:
  **8 Tests, 23,116 s, Exit 0**. Einzelne Pin-/Policy-Fehler werden jeweils
  unabhängig an Dateikopien geprüft. Der Patch-CLI-Test setzt sowohl HOME
  als auch USERPROFILE, damit auch eine spätere Windows-Ausführung nie
  versehentlich das echte Benutzerprofil nutzt.
- Finale Vereinigung: **177 Testmethoden, 167 ausgeführt, 10 Skips**;
  gleicher Ausgangscommit, gleiche 106 Produktquellhashes und Messkonfiguration.
  Die volle Suite wurde für die Ergänzung nicht erneut gestartet.
  Ein früherer Ergänzungslauf bleibt lokale Diagnosehistorie; nur die finale
  USERPROFILE-korrigierte Fassung gehört zum kombinierten Ergebnis.
- REV-TEST-TIMING: echte stderr-/Capability-/Pfadschwärzung, deterministische
  Klassifikation und echter begrenzter Timeout bestanden. Keine zusätzlichen
  Launcher und keine erhöhten Test-Timeouts.
- Frisches temporäres HOME, Caches, Git-Konfiguration, Registry-/Fake-Compose-
  Fixtures und Messdateien. Die Testumgebung wurde aus einer Positivliste
  aufgebaut, ohne Credential-Umgebungsvariablen. Kein globales Maintenance,
  keine echten Provider, kein Container-/Machine-Zugriff.

### Python-Zweig-Outcomes je benannter Datei

| Datei / File | Beobachtet / Nenner | Quote / Ratio | Numerisch mindestens 85 % / Numerically at least 85% |
|---|---:|---:|---|
| `scripts/check-dockerfile-arg-renovate.py` | 64/64 | 100.00 % | Ja / Yes |
| `scripts/check-home-baseline-lock.py` | 19/22 | 86.36 % | Ja / Yes |
| `scripts/lib/agentic_workspace_fleet.py` | 43/1274 | 3.38 % | Nein / No |
| `scripts/lib/audit_retention.py` | 48/50 | 96.00 % | Ja / Yes |
| `scripts/lib/linux-maintenance-hardening.py` | 85/150 | 56.67 % | Nein / No |
| `scripts/lib/maintenance_container_worker.py` | 34/58 | 58.62 % | Nein / No |
| `scripts/lib/maintenance_execution_context.py` | 40/90 | 44.44 % | Nein / No |
| `scripts/lib/secure_development_hardening.py` | 269/432 | 62.27 % | Nein / No |
| `scripts/lib/workspace_storage_maintenance.py` | 129/336 | 38.39 % | Nein / No |
| `spec-kit/patch-specify-cli.py` | 14/14 | 100.00 % | Ja / Yes |

**Keine Mittelung und keine Erfüllungsbehauptung:** Vier Dateiquoten erfüllen
numerisch 85 %, sechs nicht. Selbst 100 % beim Patcher ist nur die Quote seiner
benannten Python-Datei, nicht automatisch die Abdeckung seines injizierten
PATCH-Programms. Alle 48 inventarisierten eingebetteten Bereiche sowie weitere
nicht zuordenbare Inline-/isolierte Kindprozesse bleiben gesondert offen.
Die 96 Bash-/PowerShell-Dateien haben hier keine vollständige
Entscheidungs-/Outcome-Messung. Der 106-Dateien-Nenner bleibt unverändert.
G004-04 und T041-T046/T053 werden dadurch nicht pauschal abgeschlossen.

### Schnittstellen und Skips

Drei zuordenbare lokale Paare aus positiven und negativen Adaptertests sind
belegt: `agent-prompt/Dispatch`, `agent-prompt/Preview` und
`compose-down-with-audit/AuditedStop`. Für
`compose-down-with-audit/Preview` ist die positive Vorschau zugeordnet,
kein vollständiges negatives Paar. Konkrete erfolgreiche Test-IDs sind im
JSON-Bericht aufgeführt. Diese Fälle gelten für macOS/Bash, ergänzend für
PowerShell auf macOS, nicht für Windows-PowerShell oder Ubuntu/WSL2.

Es gibt 94 Katalog-IDs: 81 öffentliche Modi, sieben kritische UI-Flows und
sechs interne Grenzen. Für die 80-%-Prüfung sind 88 öffentliche/UI-IDs relevant.
Eine vollständige Quote über alle beanspruchten Varianten ist **nicht
ermittelt**. Fehlende Varianten und Skips werden weder aus dem Nenner entfernt
noch als bestanden eingetragen. Erfolgreiche Fake-Adaptertests sind keine
realen Agenten-, Podman- oder IDE-Abnahmen.

Die zehn Skips sind zwei Linux-spezifische Swift-Provisioning-Fälle, sieben
Integrationsfälle mit im Consumer nicht enthaltenen kanonischen Level-0-
Fixtures und eine opt-in Assurance-Mutationsmatrix. Diese Matrix wurde in
diesem Coverage-Schnitt nicht wiederholt. Kein Skip ist ein Pass.

### Nächste gezielte Arbeit und Übergabe

- Maintainer/Security Review: fehlende Zweige der sechs Module bearbeiten.
  Der JSON-Bericht enthält Zahlen und erste fehlende Arcs; die vollständigen
  Arcs bleiben im hashgebundenen Roh-JSON. Besonders Fleet benötigt mehr als
  die hier verfügbaren Consumer-Fixtures; fehlende Tests nicht wegdefinieren.
- Maintainer: Inline-/Kindprozess-Zuordnung sowie Bash-/PowerShell-
  Entscheidungsregister mit echten Ausführungsbelegen vervollständigen.
  Absolute isolierte Interpreter ohne Messmodul bleiben Messlücken.
- Windows Platform Review und Ubuntu/WSL2 Platform Review: getrennte
  Tests für denselben später eingefrorenen Stand. Die
  [vorbereitete Übergabe](coverage-platform-handoff.md) enthält Voraussetzungen,
  lesende Vorprüfungen, sichere Ausführungsgrenzen und Evidenzfelder.
  Ein Windows-Rechner mit eigener WSL2-Laufzeit genügt; native Linux-Hardware
  wird nicht vorausgesetzt.
- Vor betroffenen Gates: Quell-/Test-/Katalogänderungen neu prüfen und messen.
  Runtime, Build und Lieferung brauchen weiterhin gesonderte Autorität.
  T063/T068, Pilot, WCAG, Rechte und menschliche Freigaben bleiben offen.

Owner der Messlücken: Maintainer/Security Review. Follow-up: benannte fehlende
Fälle ergänzen, danach betroffen nachmessen. Trigger: vor T053 und jeder
Quell-/Test-/Katalogänderung. Plattform-Owner und Trigger stehen in der Übergabe.
Keine Anforderung, Schwelle, Nutzungsgrenze oder Lifecycle-Entscheidung geändert.

### Reproduktion und Rohbelege

Host: Mac A, PowerShell 7 ohne Profil, Repository-Wurzel.
Voraussetzungen: frisches temporäres venv mit den oben gebundenen Versionen,
freigegebene aktuelle Intake-/Reviewbindungen und unveränderte Testeingaben.
Die [Konfiguration](../../../../scripts/tests/fixtures/hardening-followup/coverage-mac-a.ini)
verlangt `ADE_COVERAGE_REPO` explizit, damit Kindprozesse mit anderem cwd
denselben Quellumfang messen. Im JSON-Bericht stehen beide echten argv-Listen,
Zeitpunkte, Exitcodes, Tests und Hashes. Pfade sind dort portable Platzhalter;
die tatsächlich ausgeführten lokalen argv bleiben in den Rohmanifesten.

Vor Ausführung HOME/USERPROFILE, PATH, TMPDIR/TMP/TEMP, XDG-Cache/Config,
Git-Konfiguration und Coverage-Ausgabe auf eigene Testorte begrenzen;
keine Credential-Variablen übernehmen. `COVERAGE_FILE` und
`COVERAGE_RCFILE` müssen auf diesen Messkontext zeigen. Erst dann die
gebundenen unittest-Aufrufe unter `coverage run` starten. Nur Rohdaten mit
gleichen Quellen und gleicher Konfiguration kombinieren; danach
`coverage json` erzeugen und jede der zehn erwarteten Dateien prüfen.

Rohdaten, SQLite-Dateien, Logs, venv und Diagnosehistorie liegen ausschließlich
im eigenen temporären Messverzeichnis und werden nicht committed. Deren
Hashinventar steht im JSON. Aufbewahrung bis zur Sichtung; spätere Entfernung
nur dieses eigenen Verzeichnisses. Bei Fehlern tatsächlichen Exit und Scope
erhalten, kein automatisches Green oder erneuter globaler Wartungslauf.

## English

**2026-11-02 outcome: Open**, not overall or platform acceptance. The base
commit is recorded above; provenance, tests and reports are uncommitted and
not a final T053 freeze. The linked JSON binds actual sources, test files,
configuration, commands, times, exits and raw artifact hashes.

Source renewal and byte-identical archives preceded execution. The independent
five-target series review is Ready without findings; this means requirement
quality, not technical acceptance. All intake texts, requirements, lifecycle
and 85/80 thresholds remain unchanged.

On macOS ARM64, CPython 3.15.2 and coverage.py 7.17.0 were isolated in an owned
temporary environment after verifying the official wheel hash above.
Thirteen modules completed 169 tests with ten skips in 507.711 seconds.
Twelve new synthetic audit cases exercise date/preview/race/recheck/export/
size/encoding/CLI boundaries. A targeted pin/patcher extension then passed
eight tests in 23.116 seconds, without repeating the full suite. The child
patcher sets both HOME and USERPROFILE. Earlier extension data remain diagnostic
history only; the corrected final version is combined with the baseline.

The final data contain 177 test methods, 167 executed and ten skipped, with
identical product sources/configuration. Real-process REV-TEST-TIMING cases
passed without new launchers or larger timeouts. Test processes used a clean
environment allowlist and synthetic HOME/caches/Git/adapter fixtures, with
no credential inheritance, global maintenance, real provider or container action.

The bilingual table reports per-file covered/total branches. Four named file
ratios reach 85%; six do not. Do not average them. A 100% patcher file ratio
does not establish coverage of its injected PATCH program. All 48 nested
regions, unattributed isolated/inline child code and complete decision traces
for 96 Bash/PowerShell files remain separate gaps. Preserve all 106 scope files.
G004-04 and the full T041-T046/T053 tasks remain Open.

Three local adapter interfaces have mapped positive/negative pairs; the
audited-stop preview has only its positive case mapped. These prove
macOS/Bash plus supplemental macOS PowerShell behavior, not native Windows or
WSL2. Of 94 logical IDs, 88 are public modes/critical UI flows and six internal
boundaries. No complete all-variant 80% ratio is established. Keep missing
variants/skips in scope. Synthetic adapters are not real agent/Podman/IDE proof.

Skips comprise two Linux-only Swift cases, seven unavailable canonical Level-0
integration fixtures and one opt-in installed Assurance matrix not repeated
in this slice. None counts as passed.

Maintainer/Security Review owns six module gaps, child-code attribution and
shell/PowerShell traces before T053 and on source/test/catalog changes.
The JSON contains missing-arc samples; full raw arcs remain locally hash-bound.
Fleet needs additional safe fixtures, not a reduced denominator. Separate
Windows and own-rootless WSL2 operators use the linked handoff and the same
later frozen inputs; shared physical hardware is allowed, copied runtime
evidence is not. Runtime/build/delivery authority, T063/T068 and human
usability/WCAG/rights decisions remain separate.

Reproduce from the repository root using PowerShell 7 without a profile and
an isolated pinned venv. Verify current inputs and use the linked configuration
with explicit ADE_COVERAGE_REPO; otherwise child cwd changes can alter scope.
The JSON preserves both command vectors with portable path placeholders;
local raw manifests contain exact executed paths. Whitelist the synthetic
environment and bind COVERAGE_FILE/RCFILE; combine only same-source/configuration
data and verify all ten expected files. Raw logs/databases/venv remain in the
owned temporary directory, never tracked; keep them for review and remove only
that owned directory later. Preserve genuine failures, no fabricated passes
or global maintenance retries.
