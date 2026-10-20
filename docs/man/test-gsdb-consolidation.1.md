# test-gsdb-consolidation(1)

## Name

`test-gsdb-consolidation` - isolierte GSDB- und Profilregressionen / isolated GSDB and profile regressions

## Synopsis

```powershell
pwsh -NoProfile -File scripts/tests/test-gsdb-consolidation.ps1
```

## Beschreibung / Description

DE: Auf macOS/Linux Bash zuerst und danach PowerShell prüfen; unter Windows
native PowerShell prüfen. Benötigt die jeweilige Shell, Git, jq für Bash und
Python 3 für die bestehende Bash-Matrixprüfung. Keine Downloads oder
Installationen. Fixtures im Temp-Verzeichnis werden anschließend entfernt.

EN: On macOS/Linux test Bash first, then PowerShell; on Windows test native
PowerShell. Requires the respective shell, Git, jq for Bash, and Python 3 for
the existing Bash matrix check. No downloads or installations. Temporary
fixtures are removed afterward.

## Fälle / Cases

Positive Basis, fehlendes Dokument, doppelte Dokument-/Prüfpunkt-ID, CRLF-Presetmanifest, falsche Dokumentversion,
veralteter Baseline-Header, fehlender Profilverweis, Sammelbanddrift,
unvollständige Preset-Matrix, Manifestversionsdrift, Prioritätsdrift,
unbekanntes Profil und Registry-Profilzuordnung. Alle Läufe vergleichen
Dateinamen und SHA-256 vorher/nachher und müssen read-only bleiben.

Positive baseline, missing document, duplicate document/item ID, CRLF preset manifest, wrong document version,
stale baseline header, missing profile reference, stale compendium, incomplete
preset matrix, manifest-version drift, priority drift, unknown profile, and
registry-assigned profile. Before/after file and SHA-256 snapshots assert
read-only behavior.

DE: Der negative Baseline-Fall liest die Ausgangsversion aus dem Manifest und
setzt gezielt eine andere Version. Ein fehlender Ausgangsheader bricht den Test
ab; neue Baseline-Releases duerfen die Mutation nicht still unwirksam machen.

EN: The negative baseline case reads its starting version from the manifest
and replaces it with a different version. A missing starting header fails the
test; new baseline releases must not silently disable the mutation.

DE: Zusaetzliche Metadatenfaelle pruefen veraltete Header mit gueltigem Zweitfeld,
einen nur im Fliesstext vorhandenen Header, Versionspraefixe, doppelte Versionen,
CRLF-Metadaten und erlaubte historische Versionstabellen. Negative Fälle
müssen ausdrücklich am vorgesehenen Metadatenfehler scheitern; ein veralteter
Sammelband allein genügt nicht.

EN: Additional metadata cases cover stale headers with a valid duplicate,
body-only headers, version prefixes, duplicate versions, CRLF metadata and
allowed historical version tables. Negative cases must fail with the intended
metadata error rather than merely detecting a stale compendium.

## Exit-Status / Exit Status

0: alle Fälle bestanden / all cases passed. Non-zero: Regression oder fehlendes
Werkzeug / regression or missing tool. Der Test ist kein fachlicher Normreview.
The test does not replace a subject-matter standards review.

DE: Beide aktiven Richtlinien-Metadatentabellen werden abschnittsgebunden und exakt gegen das Manifest geprüft. Veraltete DE-/EN-Werte, Präfixe, Duplikate, doppelte Sprachabschnitte und nur im Text vorhandene Felder scheitern; CRLF und historische Versionszeilen bleiben zulässig. Negative Regressionen prüfen den konkreten Fehler samt betroffenem Feld/Pfad. Ein anzahlgleiches ID-Duplikat prüft die eigentliche Duplikaterkennung. Insgesamt 34 Fälle je Shell, 68 auf macOS/Linux.

EN: Both active guideline metadata tables are section-bound and checked exactly against the manifest. Stale DE/EN values, prefixes, duplicate fields/sections and body-only fields fail; CRLF and historical version rows remain valid. Negative regressions assert the specific error and affected field/path. A count-preserving duplicate exercises actual ID detection. There are 34 cases per shell, 68 on macOS/Linux.

DE: Vier zusätzliche Negativfälle belassen den aktiven Baseline-/Versionswert korrekt und ergänzen nur ein gleiches Zweitfeld (auch Richtlinie DE/EN). So wird die Eindeutigkeitsbedingung unabhängig von einem falschen aktiven Wert getestet. / EN: Four additional negative cases keep the active baseline/version correct and add an identical duplicate, including DE/EN guideline fields, isolating uniqueness from value mismatch.
