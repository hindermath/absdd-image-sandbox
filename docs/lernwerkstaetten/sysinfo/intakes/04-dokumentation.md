<!-- intake-authoring:begin -->
# SYS-04: Reproduzierbare Dokumentation / Reproducible Documentation

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität SYS-04; UUID im
Receipt. [basis.md](../basis.md) gilt; SYS-03 muss abgenommen sein.
Ziel: vorhandene Funktionen erklären, nicht die Produktoberfläche erweitern.

- FR-01: Sprachtypische Public-API-Kommentare zu lesbarer Code-Referenz erzeugen.
  AC-01: Aus sauberem Arbeitsstand entsteht die Referenz mit dokumentiertem
  Befehl; fehlende Eingangsdaten führen zu Fehler statt altem Erfolgsbericht.
- FR-02: CLI-Hilfe, Optionen, Beispiele, Datenzustände und Exitcodes aus dem
  aktuellen Vertrag dokumentieren. AC-02: automatische Prüfung vergleicht
  Optionen/Version mit CLI; alle Beispiele verwenden fiktive Werte.
- FR-03: OpenAPI zu statischer API-Dokumentation verarbeiten.
  AC-03: alle fünf CRUD-Operationen, Health, Statuscodes und Fehler sind
  verlinkt; Serverstart und Dokumenterzeugung bleiben getrennte Vorgänge.
- FR-04: DE/EN, Textalternativen, Überschriften und Links pflegen.
  AC-04: Links und Begriffe geprüft; Screenreader/Tastatur-/Lernendenprüfung
  entweder real protokolliert oder als Open mit Owner/Follow-up/Trigger erfasst.
- FR-05: Keine sensiblen Daten oder Secrets aus Laufzeitzuständen einbetten.
  AC-05: Export-/Secret-Prüfung und Regressionen dokumentiert, Coverage eigener
  Produktlogik mindestens 80 %; generierte Dateien sind nicht automatisch Evidenz.

**Artefakte:** Generatorbefehle, Code-/CLI-/API-Referenz, Prüfbericht und Abnahme.
**Nicht-Ziele:** neue Produktfunktion, öffentliche Website, formale A11Y-Freigabe.
Risiko: alte generierte Ausgabe als aktuelle Dokumentation zeigen.
Lernfrage: Woran erkennt ein Reviewer den aktuellen Eingabestand eines Exports?

## English

SYS-04 is ReadyForReview and Pending after SYS-03. The shared contract applies.
FR/AC-01 regenerates code reference and fails on missing input; 02 matches
CLI/version/options and fictional examples; 03 generates static API reference
for CRUD/health/errors without starting the service; 04 checks equivalent
languages, links and text alternatives, recording human A11Y tests or Open;
05 excludes secrets/live data, preserves regressions and at least 80 % own
logic coverage. Deliver reproducible commands, references and acceptance.
No feature expansion, public website or invented accessibility approval.
Explain how an export is tied to current source, not a stale artifact.

<!-- intake-authoring:prompts -->
DE: Nur aktuelle Produktverträge dokumentieren. EN: Document current product contracts only.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/04-dokumentation.md und basis.md. Spezifiziere SYS-04 ohne neue Produktfunktionen. Keine Implementierung, Veröffentlichung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/04-dokumentation.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Keine Veröffentlichung, kein Commit, Push, Container-Build oder Provider-/Berechtigungseingriff.
```
<!-- intake-authoring:end -->
