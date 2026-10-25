<!-- intake-authoring:begin -->
# SYS-02: Snapshots in SQLite / SQLite Snapshots

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität SYS-02; UUID im
Receipt. [basis.md](../basis.md) bleibt verbindlich. Vorbedingung: SYS-01
abgenommen. Ein Snapshot ist eine gespeicherte Momentaufnahme, keine neue Live-Abfrage.

- FR-01: `--save sqlite --database snapshots.db` speichert die freigegebenen
  Kategorien; `--show cpu` beschränkt auf CPU. AC-01: Jeder Lauf erzeugt genau
  einen identifizierbaren Snapshot mit UTC-Zeit, Herkunft und Kategorien.
- FR-02: Gespeicherte Snapshots auflisten und anhand ihrer ID wieder lesen;
  genaue CLI-Schreibweise in Spec/Plan festlegen. AC-02: Neustart erhält drei
  Fixtures; jede ID liefert denselben gespeicherten Inhalt, nicht aktuelle Werte.
- FR-03: Schreibvorgang transaktional und parametriert durchführen.
  AC-03: Erzwungener Fehler nach Teiloperation hinterlässt keinen halben
  Snapshot; Quotes bleiben Daten und verändern keine Tabellen.
- FR-04: Pfad und Zugriffsfehler verständlich behandeln, Daten schützen.
  AC-04: Fehlender Dateizugriff und gesperrte Datenbank liefern Fehler ohne
  Datenverlust; DB ist untracked und liegt außerhalb von Buildausgaben.
- FR-05: Alle bisherigen Exporte erhalten. AC-05: Regressionen bestehen,
  Schema/Transaktion sind dokumentiert, Coverage mindestens 80 %.

**Artefakte:** Modell-/Schemaentscheidung, CLI, SQLite-Tests, Sicherungs- und
Wiederleseanleitung mit ausschließlich eigenen Fixtures, Review/Abnahme.
**Nicht-Ziele:** REST, Cloud-Datenbank, automatische Schema-Migration oder
Upload. Risiko: fehlgeschlagene Speicherung als erfolgreich melden.
Lernfrage: Welche Prüfung erkennt einen teilweise geschriebenen Snapshot?

## English

SYS-02 is ReadyForReview; product Pending after acceptance of SYS-01. The
shared contract governs. A snapshot is stored data, not a fresh live query.
FR/AC-01 stores all allowed or one selected category with ID/time/source;
02 lists/reads stable IDs across restart; specify exact read CLI before coding;
03 proves transaction rollback and parameterized data handling; 04 protects
untracked persistent paths and preserves data on lock/access errors; 05
preserves all exports and at least 80 % scoped coverage. Deliver schema/CLI,
isolated tests, save/read guidance and acceptance. No REST, cloud, migration
or upload. Explain the test that detects partial persistence.

<!-- intake-authoring:prompts -->
DE: Keine fremden Datenbanken verwenden. EN: Do not use another person's database.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/02-sqlite.md und basis.md. Spezifiziere SYS-02 nach Abnahme von SYS-01. Halte Speicherung und Live-Erfassung getrennt. Keine Implementierung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/02-sqlite.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Nur eigene isolierte Fixtures; kein Commit, Push, Container-Build oder Zugriff auf fremde Daten.
```
<!-- intake-authoring:end -->
