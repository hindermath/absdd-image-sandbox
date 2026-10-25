<!-- intake-authoring:begin -->
# SYS-01: YAML-Export / YAML Export

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität SYS-01; UUID im
Receipt. [basis.md](../basis.md) gilt weiter. Vorbedingung: SYS-00 fachlich
abgenommen und Nachweise aktuell. Ziel: ein viertes Exportformat, kein neues Datenmodell.

- FR-01: `--export yaml --output snapshot.yaml` sowie Kategorieexport erlauben.
  AC-01: Ein YAML-Parser liest denselben Modellinhalt wie beim JSON-Export.
- FR-02: Skalare als Daten serialisieren, keine ausführbaren Typ-Tags verwenden.
  AC-02: Umlaute, Zeilenumbrüche, Doppelpunkte und YAML-ähnliche Texte bleiben
  nach Parser-Rücklesen unverändert; keine fremden Objekte werden instanziiert.
- FR-03: Freigabe-, Fehler- und Dateiregeln aus SYS-00 erhalten.
  AC-03: Ohne sensibles Opt-in keine sensiblen Daten; Schreibfehler und
  vorhandene Datei hinterlassen keinen Teil-/überschriebenen Export.
- FR-04: Help, Tests und Sprachfassungen synchron erweitern.
  AC-04: Regressionen für JSON/CSV/XML, YAML-Voll-/Kategorieexport und ungültiges
  Format bestehen; Coverage bleibt mindestens 80 % gemäß basis.md.

**Artefakte:** Formatvertrag, Exportimplementierung, Tests, CLI-/Code-Doku,
Review und Abnahme. **Nicht-Ziele:** YAML-Import, Objektkonstruktion aus YAML,
Datenbank oder REST. Risiko: Daten als Steueranweisung interpretieren.
Lernfrage: Warum beweist eine syntaktisch gültige Datei noch keine Modellgleichheit?

## English

SYS-01 is ReadyForReview, product stage Pending. Accept SYS-00 first; the
shared contract remains binding. Add YAML as a fourth export, not a new model.
FR/AC-01 requires parser-checked full/category parity with JSON; 02 preserves
Unicode, punctuation and multiline data without executable type tags; 03
preserves opt-in and atomic safe-output behavior; 04 updates help/docs and
regressions for all formats with at least 80 % scoped coverage. Deliver the
format contract, exporter, tests and human review/acceptance. No YAML import,
database or REST. Explain why valid syntax alone does not prove model parity.

<!-- intake-authoring:prompts -->
DE: Vorgängerabnahme und eigenen Startauftrag prüfen. EN: Check predecessor acceptance and personal authority.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/01-yaml.md und basis.md. Spezifiziere SYS-01 als YAML-Erweiterung des abgenommenen SYS-00. Keine Implementierung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/01-yaml.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Nur SYS-01; kein Commit, Push, Container-Build oder Provider-/Berechtigungseingriff.
```
<!-- intake-authoring:end -->
