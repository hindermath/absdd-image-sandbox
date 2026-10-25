# Begrenztes Sicherheitsreview / Bounded Security Review

## Deutsch

### Auftrag und Bindung

- Datum: 2026-10-25; Host: macOS (Darwin).
- Rolle: unabhaengiger Nicht-Autor der geprueften Konfiguration und Tests.
- Vergleichsbasis: Git `HEAD` = `9a6cf88747f07f4b081d3033546f2d83861e2916`.
- Umfang: ausschliesslich `.gitleaks.toml` und
  `scripts/tests/test_gitleaks_swift_fingerprint.py` im aktuellen Arbeitsbaum.
  Die Konfiguration ist gegen HEAD geaendert; die Testdatei ist neu/untracked.
- `COMPLIANCE-PLAN_RL-SE-001.md` wurde gelesen, insbesondere P1-3 und die
  menschlichen Freigabegrenzen. Der aktuelle Ownerauftrag genehmigt diese
  eng begrenzte Ausnahme. Er erlaubt nur diesen Bericht als Repo-Schreibzugriff
  und untersagt ausdruecklich einen zusaetzlichen Session-Log.

SHA-256 der geprueften Dateien (Dateibytes, nicht Git-Objekt-IDs):

| Datei | SHA-256 |
|---|---|
| `.gitleaks.toml` | `4aa933ea9861be2d54772d0cd2ad4a8e1cbbccfbb84f453d8297767fd8b23c1e` |
| `scripts/tests/test_gitleaks_swift_fingerprint.py` | `181eae2212db067b9c587851442fe887285666d3c8ba7149844a8682a1ab51cd` |

### Findings und Verdict

**Keine bestaetigten Findings im beauftragten Umfang. Verdict: PASS fuer die
oben gebundenen Dateistaende.** Keine Reparatur vorgenommen.

Die semantische Pruefung von `.gitleaks.toml:6-16` ergibt:

1. `targetRules = ["generic-api-key"]` begrenzt ausschliesslich die neue
   Ausnahme auf diese Regel; andere Default-Regeln werden nicht ausgenommen.
2. `condition = "AND"` verlangt sowohl Pfadtreffer als auch Zeilentreffer.
   Die Pfadregex ist beidseitig verankert und erlaubt genau `Dockerfile` oder
   `specs/intake-authoring-operations/3caff22f-59d5-4142-b15b-955ee96a3037/source-snapshots/Dockerfile.txt`.
   Unterverzeichnisse, andere Operations-IDs und Pfadsuffixe sind nicht erlaubt.
3. `regexTarget = "line"` prueft mit `^` und `$` die gesamte konkrete
   Zuweisungszeile: `swift_signing_key`, doppeltes Anfuehrungszeichen, exakt
   `52BB7E3DE28A71BE22EC05FFEF80A866B47A981F`, schliessendes
   Anfuehrungszeichen, Semikolon und abschliessender Fortsetzungs-Backslash.
   Lediglich horizontale Leerzeichen sind an den ausdruecklich angegebenen
   Stellen variabel. Andere Werte, Zuweisungsnamen oder weitere Zuweisungen
   passen nicht auf diese vollstaendige Zeile.
4. `git diff HEAD -- .gitleaks.toml` zeigt nur den neuen Allowlist-Block.
   Alle drei alten Allowlists bleiben unveraendert; `[extend] useDefault = true`
   bleibt erhalten. Es gibt keine neue pauschale Pfad-, Regel- oder
   Entropieausnahme, kein `disabledRules` und keine Entropie-Absenkung.

### Tests

Auf dem macOS-Host aus der Repository-Wurzel in PowerShell 7 ohne Profil
ausgefuehrt; Voraussetzungen: vorhandenes Python mit `tomllib` und Gitleaks.
Keine Installation. `-B` verhindert Python-Bytecode-Dateien.

```powershell
python3 -B scripts/tests/test_gitleaks_swift_fingerprint.py -v
```

Ergebnis mit Gitleaks **8.30.1**: **7 Methoden erfolgreich, 0 Fehler,
0 uebersprungene Tests, Exit 0**. Bei einem Fehler waere das Urteil nicht PASS;
die Fehlermeldung waere ohne Reparatur an Parent/Owner zu melden.

| Pruefung | Ergebnis |
|---|---|
| Regelbindung, AND, Zeilenmodus, Default-Aktivierung | bestanden |
| Exakter Fingerprint im Root-Dockerfile | erlaubt |
| Exakter Fingerprint im exakten Snapshot | erlaubt |
| Anderer synthetischer Wert an beiden erlaubten Orten | erkannt |
| Gleicher Fingerprint in fremder Datei, Unterverzeichnis-Dockerfile und anderer Operations-ID | erkannt |
| Weitere Zuweisung auf derselben Zeile | erkannt |
| Fingerprint in anderer Zuweisung | erkannt |

Die Suite verwendet reale `gitleaks dir .`-Aufrufe mit repo-relativen
Fixture-Pfaden. Das Arbeitsverzeichnis ist jeweils ein isoliertes temporaeres
Payload-Verzeichnis, nicht dieses Repository. Berichte liegen ausserhalb des
Payloads, sind redigiert und werden mit dem temporaeren Verzeichnis entfernt.
Es gibt sechs Scanner-Testmethoden mit insgesamt neun Scanneraufrufen und
eine strukturelle Testmethode. Fehlendes Gitleaks fuehrt zu Skip statt zu
behauptetem Scanner-Erfolg; bei diesem Lauf trat kein Skip auf.

### Grenzen

Kein globaler Scan, keine privaten Dateiinhalte, keine Containeraktion,
Installation oder Git-Schreiboperation. Bestehende uncommittete Aenderungen
wurden nicht repariert, zurueckgesetzt oder gestaged. Nur dieser Bericht wurde
im Repository geschrieben. Die Default-Regeln bleiben laut Konfiguration
aktiv; nicht jede Default-Regel wurde einzeln dynamisch getestet. Das Urteil
gilt fuer die lokale Scanner-Version und ist keine plattformuebergreifende
Abnahme oder Verifikation der Swift-Schluesselherkunft.

Keine Risikofreigabe, formelle Sandbox-Freigabe oder Schliessung menschlicher
Compliance-Aufgaben. Dieser neue Bericht ist kein gebundener Intake-Input.
Die beiden geprueften Dateien liegen laut Auftragsabgrenzung ausserhalb der
139 Review-Hashes; deren Manifest und Bindung wurden nicht neu geprueft oder
geaendert. Aenderungen an den oben gebundenen Dateien erfordern ein neues Review.

## English

### Authority and Binding

Date: 2026-10-25; host: macOS (Darwin). The reviewer did not author the reviewed
configuration or tests. Baseline: Git `HEAD`
`9a6cf88747f07f4b081d3033546f2d83861e2916`. Scope is limited to the two
working-tree files and their exact SHA-256 values in the table above. The
configuration is modified against HEAD; the test file is new/untracked.

`COMPLIANCE-PLAN_RL-SE-001.md` was read, including P1-3 and human approval
boundaries. The current owner request authorizes this narrow exception and
only this report as a repository write, explicitly excluding a session log.

### Findings and Verdict

**No confirmed findings within scope. Verdict: PASS for the exact file hashes
above.** No repairs were made.

The semantic review of `.gitleaks.toml:6-16` confirms:

1. Only `generic-api-key` is targeted by the new exception. Other default
   rules are not exempted by it.
2. `AND` requires both the path and line conditions. Anchored paths allow
   exactly the root `Dockerfile` or
   `specs/intake-authoring-operations/3caff22f-59d5-4142-b15b-955ee96a3037/source-snapshots/Dockerfile.txt`.
   Subdirectories, other operation IDs and path suffixes are excluded.
3. The anchored whole-line expression requires the exact assignment name,
   double-quoted fingerprint `52BB7E3DE28A71BE22EC05FFEF80A866B47A981F`,
   semicolon and final continuation backslash. Only explicitly specified
   horizontal whitespace may vary. Other values, names and additional
   assignments cannot match this complete line.
4. The diff against HEAD only adds this allowlist block. All three previous
   allowlists remain unchanged, as does `[extend] useDefault = true`.
   No blanket path, rule or entropy exception, `disabledRules`, or reduced
   entropy threshold was added.

### Tests

The PowerShell command above ran from the repository root on the macOS host
without a PowerShell profile, using existing Python with `tomllib` and
Gitleaks **8.30.1**. Nothing was installed; `-B` prevents bytecode files.
Result: **7 methods passed, 0 failures, 0 skips, exit 0**. A failure would
require a non-PASS verdict and escalation to the parent/owner without repair.

Both exact allowed locations pass. A different synthetic value is detected
at both locations. The same fingerprint is detected in an unrelated file,
a subdirectory Dockerfile and a different operation ID. A different assignment
name and an additional assignment on the same line are detected. The
structural test checks rule targeting, AND, line mode and default activation.

Six scanner methods make nine real `gitleaks dir .` calls with repo-relative
fixture paths in isolated temporary payload directories, never in this
repository. Redacted reports are outside the payload and removed with the
temporary directory. Missing Gitleaks would cause skips, not claimed scanner
success; no skips occurred in this run.

### Boundaries

No global scan, private file contents, container actions, installations or
Git writes. Existing uncommitted work was neither repaired, reverted nor
staged. This report is the only repository file written. Configuration keeps
all default rules active; each default rule was not individually exercised.
Evidence is local to the scanner version, not cross-platform acceptance or
verification of the Swift key's provenance.

This is not risk acceptance, formal sandbox approval or completion of
human-only compliance tasks. This new report is not a bound intake input.
According to the supplied scope, neither reviewed file belongs to the 139
review hashes; that manifest and its binding were not revalidated or changed.
Changes to either hash-bound file require a new review.
