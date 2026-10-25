# Gezieltes Nachreview / Targeted Follow-Up Review

## Deutsch

### Auftrag und Dateibindung

Datum: 2026-10-25. Unabhaengiges Nachreview durch einen Nicht-Autor der
geprueften Reparatur. Geprueft wurden die aktuellen Dateibytes von
`.gitleaks.toml` und `scripts/tests/test_gitleaks_swift_fingerprint.py`.
`COMPLIANCE-PLAN_RL-SE-001.md` wurde gelesen, insbesondere P1-3 und die
Grenzen menschlicher Freigaben. Der Auftrag erlaubt ausschliesslich diesen
neuen Bericht; den Sessionlog erstellt der Parent.

Die fruehere PASS-Bindung in
[gitleaks-swift-fingerprint-review-2026-10-25.md](gitleaks-swift-fingerprint-review-2026-10-25.md)
gilt nicht fuer die reparierten Dateien. Der alte Bericht bleibt unveraendert.
Dieses Nachreview stuetzt sich auf neue lokale Pruefungen, nicht auf dessen
damaliges Testergebnis. Kein Git-Aufruf und keine Aussage zu HEAD oder Diff.

SHA-256 der Dateibytes:

| Datei | SHA-256 |
|---|---|
| `.gitleaks.toml` | `b1d7c45fed81b5506999d2ccf620902d4a971c6f83c637adddec2f7ce5272d67` |
| `scripts/tests/test_gitleaks_swift_fingerprint.py` | `e38ea8897b1fd8885f758848b19de18389e2ba76291d0099842303071dec5aa7` |
| `Dockerfile` (vollstaendige Fixture) | `a98213c4abe13322ce0be2d9012c7fad52033e04f525c453beca386161fa33d7` |
| `specs/intake-authoring-operations/3caff22f-59d5-4142-b15b-955ee96a3037/source-snapshots/Dockerfile.txt` (vollstaendige Fixture) | `b8880e957bec256e1cb166eb5251643a35c2c54327313584dff2ba052b844aa5` |
| Alter Bericht (Erhaltungsnachweis) | `d598d3d8ad86896c794bec8a1a6bcf475df0d7b06d388ffc6841b52a69d88a73` |

### Findings und Urteil

**Keine bestaetigten Findings im beauftragten Umfang. Urteil: PASS fuer die
oben gebundenen Konfigurations- und Testdateien mit Gitleaks 8.30.1.**
Keine Reparatur vorgenommen.

1. `.gitleaks.toml:6-16`: Die Ausnahme ist weiterhin an
   `targetRules = ["generic-api-key"]`, `condition = "AND"` und
   `regexTarget = "line"` gebunden. Pfad und Zeile muessen gemeinsam passen.
2. Die beidseitig verankerte Pfadregex erlaubt genau zwei repo-relative
   Pfade: das Root-`Dockerfile` und den oben genannten Snapshot. Keine
   beliebigen Unterverzeichnisse, anderen Operations-IDs oder Pfadsuffixe.
3. Die Zeilenregex akzeptiert ausschliesslich einen optionalen fuehrenden
   LF (`(?:\n)?`) und einen optionalen abschliessenden CR (`\r?`) zusaetzlich
   zur konkreten Zuweisung. Dazwischen sind nur explizite horizontale
   Leerzeichen bzw. Tabulatoren variabel. Es gibt kein `\s`, `.*`,
   Multiline-Flag oder wiederholbares LF. Die Anker umfassen den gesamten
   Zielstring, nicht beliebige Teilzeilen.
4. Erforderlich bleiben exakt `swift_signing_key`, `=`, doppelte
   Anfuehrungszeichen, der feste Fingerprint
   `52BB7E3DE28A71BE22EC05FFEF80A866B47A981F`, Semikolon und
   Fortsetzungs-Backslash. Andere Werte oder Namen, zusaetzlicher Text oder
   zusaetzliche nichtleere Zeilen passen nicht. LF/CR erlauben nur die
   Randzeichen der Fundzeile, keine weitere inhaltliche Zeile.
5. Der Auftrag nennt als Ursache, dass Gitleaks 8.30.1 in `location.go`
   den vorherigen LF in `finding.Line` einschliesst. Der Scannerquelltext
   wurde hier nicht separat geprueft. Die jetzt erfolgreichen echten
   Mehrzeilen-Fixtures bestaetigen die praktische Wirksamkeit der Reparatur.
6. `[extend] useDefault = true` bleibt aktiv. Die gesamte vorliegende
   Konfiguration enthaelt keine `disabledRules`, eigene Detektionsregeln
   oder Entropie-Absenkung. Die drei weiteren Allowlist-Bloecke bleiben
   eigenstaendig: Beispielwerte in Beispielpfaden sowie zwei historische,
   commitgebundene Dokumentationsausnahmen. Die neue Swift-Ausnahme
   erweitert diese nicht. Ein historischer Unveraendertheitsvergleich
   wurde ohne Git nicht behauptet.

### Ausgefuehrte Tests

Ausfuehrungsort: Repository-Wurzel auf dem macOS-Host (Darwin),
PowerShell 7 mit `-NoLogo -NoProfile`. Voraussetzungen: vorhandenes
Python **3.15.0** mit `tomllib` und Gitleaks **8.30.1**. Keine Installation.

```powershell
python3 -B scripts/tests/test_gitleaks_swift_fingerprint.py -v
```

**Ergebnis: 9 Testmethoden bestanden, 0 Fehler, 0 Skips, Exit 0;
gemeldete Laufzeit 0.330 s.** Bei Fehler oder Skip waere diese vollstaendige
Scanner-PASS-Aussage nicht gerechtfertigt; keine automatische Reparatur.

| Pruefung | Ergebnis |
|---|---|
| Regelbindung, AND, Zeilenmodus, Default-Aktivierung | bestanden |
| Exakter Fingerprint als einzelne Zuweisung an beiden erlaubten Pfaden | erlaubt |
| Vollstaendiges aktuelles Dockerfile und vollstaendiger Snapshot als Mehrzeilen-Fixtures | beide erlaubt |
| CRLF-Mehrzeilenkontext mit Zuweisung zwischen Nachbarzeilen | erlaubt |
| Zusaetzliches synthetisches Secret auf benachbarter Folgezeile | erkannt |
| Anderer synthetischer Wert an beiden erlaubten Pfaden | erkannt |
| Fingerprint in fremder Datei, Unterverzeichnis-Dockerfile, anderer Operations-ID | jeweils erkannt |
| Weitere synthetische Zuweisung auf derselben Zeile | erkannt |
| Fingerprint in anderer Zuweisung | erkannt |

Eine strukturelle Testmethode und acht Scanner-Testmethoden erzeugen
insgesamt 13 echte `gitleaks dir .`-Aufrufe. Die Suite erzeugt isolierte
temporaere Payload-Verzeichnisse mit repo-relativen Pfaden; redigierte
JSON-Berichte liegen ausserhalb des Payloads und werden danach entfernt.
Fehlendes Gitleaks fuehrt ausdruecklich zu Skip, nicht zu einem behaupteten
Scanner-Erfolg. `-B` verhindert Python-Bytecode-Dateien.

Die Quellen-Fixtures lesen den vollstaendigen aktuellen Text; sie sind keine
manuell verkuerzten Einzeiler. `read_text()` normalisiert vorhandene
Zeilenenden, deshalb bindet die Tabelle zusaetzlich die urspruenglichen
Dateibytes. Der separate CRLF-Test erzeugt CRLF explizit. CRLF und das
benachbarte Secret werden dynamisch am Root-Dockerfile geprueft; die
identische gemeinsame Regex gilt auch fuer den Snapshot. Die Negativtests
verlangen einen `generic-api-key`-Fund, binden aber nicht dessen exakte
Fundposition. Nicht jede theoretische Syntaxvariante oder Default-Regel
wurde dynamisch getestet; die weitergehenden Grenzen beruhen auf dem
semantischen Regex-Review.

### Grenzen

Nur dieser neue Bericht wurde geschrieben. Keine Aenderung am alten
Bericht, an Konfiguration, Tests, Fixtures oder anderen Dateien. Kein eigener
Sessionlog gemaess Auftrag. Keine Builds, Containeraktionen, globale Wartung,
Git-Befehle, Installationen oder globalen Repository-Scans.

Dies ist lokale Scanner-Evidenz, keine Image-Abnahme, kein Nachweis der
Swift-Schluesselherkunft und keine vollstaendige plattformuebergreifende
Abnahme. Keine formelle Sandbox- oder Risikofreigabe und keine Schliessung
menschlicher Compliance-Aufgaben. Aenderungen der gebundenen Dateien oder
der Scanner-Version erfordern eine erneute Bewertung.

## English

### Scope and Byte Binding

Date: 2026-10-25. Independent follow-up by a reviewer who did not author the
repair. Scope covers the current bytes of `.gitleaks.toml` and
`scripts/tests/test_gitleaks_swift_fingerprint.py`.
`COMPLIANCE-PLAN_RL-SE-001.md` was read, including P1-3 and human approval
boundaries. Only this new report is authorized for writing; the parent
creates the session log.

The earlier report linked above no longer binds the repaired files and was
left unchanged. This verdict uses fresh local checks, not its previous test
result. The SHA-256 table above binds both reviewed files, both complete
source fixtures, and the preserved earlier report. No Git commands were run;
no HEAD or diff claim is made.

### Findings and Verdict

**No confirmed findings within scope. Verdict: PASS for the hash-bound
configuration and test files with Gitleaks 8.30.1.** No repairs were made.

1. `.gitleaks.toml:6-16` still targets only `generic-api-key`, uses `AND`,
   and checks `line`. Both path and line must match.
2. The anchored path expression allows exactly the root `Dockerfile` and
   the exact snapshot path in the hash table. Other directories, operation
   IDs and suffixes are excluded.
3. The line expression adds only one optional leading LF and one optional
   trailing CR. Within the assignment, only the explicit horizontal spaces
   or tabs may vary. There is no `\s`, `.*`, multiline flag or repeatable
   LF. Anchors cover the complete target string, not arbitrary partial lines.
4. The exact variable name, equals sign, double-quoted fixed fingerprint,
   semicolon and continuation backslash remain mandatory. Different values
   or names, extra text and additional nonempty lines cannot match. LF/CR
   accommodate boundary characters, not another line of content.
5. The request identifies Gitleaks 8.30.1 `location.go` including the preceding
   LF in `finding.Line` as the cause. Scanner source was not separately
   inspected. Successful complete multiline fixtures establish that the
   repaired expression works in practice.
6. `[extend] useDefault = true` is active. The current configuration contains
   no `disabledRules`, custom detection rules or lowered entropy thresholds.
   Its three other allowlist blocks remain separate: example-file values and
   two historical, commit-bound documentation exceptions. The Swift exception
   does not expand them. Historical unchangedness was not asserted without Git.

### Tests and Coverage

The command above ran from the repository root on macOS (Darwin), through
PowerShell 7 with `-NoLogo -NoProfile`, using existing Python **3.15.0**
and Gitleaks **8.30.1**. No installation was performed.

**9 methods passed, 0 failures, 0 skips, exit 0; reported runtime 0.330 s.**
A failure or skip would not justify this full scanner-PASS statement and
would be reported without automatic repair.

Both exact-path single assignments and both complete current source files
pass. Explicit CRLF context passes. A neighboring synthetic secret is
detected. Different synthetic values at both allowed paths, the fingerprint
at three disallowed paths, an additional same-line assignment and a renamed
assignment are detected. The structural method checks rule targeting, AND,
line mode and default activation.

Eight scanner methods make 13 real `gitleaks dir .` calls; one further method
checks structure. Temporary isolated payloads preserve repo-relative paths.
Redacted JSON reports are outside the payload and removed afterward. Missing
Gitleaks explicitly causes skips, not claimed scanner success; none occurred.
`-B` prevents Python bytecode files.

Complete fixtures read current source text, not shortened single-line copies.
`read_text()` normalizes source line endings; the table separately binds raw
source bytes. The CRLF test explicitly creates CRLF. CRLF and neighboring
secret behavior are dynamically tested at the root Dockerfile; the same
shared expression also governs the snapshot. Negative tests require a
`generic-api-key` finding but do not assert its exact location. Not every
possible syntax variant or default rule was dynamically exercised; broader
boundary conclusions come from semantic regex review.

### Boundaries

Only this new report was written. The earlier report, configuration, tests,
fixtures and all other files were left untouched. No separate session log,
builds, container actions, global maintenance, Git commands, installations
or global repository scans were performed.

This is local scanner evidence, not image acceptance, Swift key provenance
verification or full cross-platform acceptance. It grants no formal sandbox
or risk approval and closes no human-only compliance task. Changes to the
bound files or scanner version require renewed assessment.
