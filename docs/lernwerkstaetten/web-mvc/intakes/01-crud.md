<!-- intake-authoring:begin -->
# MVC-01: CRUD mit SQLite / CRUD with SQLite

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität MVC-01; UUID im
Receipt. [basis.md](../basis.md) gilt; MVC-00 muss abgenommen sein.
Ziel: aus Vorschau wird bestätigte eigene Speicherung, nicht aus einem Formular eine API.

- FR-01: EF Core/SQLite für zwei Texte und generierte ID nutzen.
  AC-01: eigener expliziter DB-Pfad im Projekt-Mount, höchste ID zuerst,
  drei fiktive Einträge nach Prozessneustart unverändert lesbar.
- FR-02: Create/Read/Update/Delete als MVC-Formularaktionen anbieten.
  AC-02: gültiger Durchlauf bestätigt erst nach SaveChanges; GET löscht nichts,
  fehlende ID ergibt 404, Bearbeitung abbrechen verändert nichts.
- FR-03: Validierung und Schutz aus MVC-00 erhalten.
  AC-03: ungültige/überlange Werte und fehlender Antiforgery-Token ändern den
  Bestand nicht; eingegebenes Markup erscheint als Text, nicht ausführbares HTML.
- FR-04: Fehler und Entwurf getrennt vom bestätigten Bestand behandeln.
  AC-04: erzwungener Schreibfehler führt nicht zu Erfolgsmeldung oder Retry;
  Lesefehler wird nicht als leere Liste dargestellt.
- FR-05: Isolierte Testdaten und Sicherungsgrenzen dokumentieren.
  AC-05: Tests benutzen separate DB, bestehen mit mindestens 70 % Coverage;
  Git enthält keine Datenbank/Backups; Schema-Neuanlage wird nicht Migration genannt.

**Artefakte:** Datenmodell, CRUD, DB-Konfiguration, Tests, Betriebs-/Abnahmenotiz.
**Nicht-Ziele:** REST, zweite App, Datentransfer aus Referenz, PostgreSQL.
Risiko: Buildausgaben und persistente Daten verwechseln.
Lernfrage: Warum ist ein erfolgreicher Controller-Aufruf vor SaveChanges kein Speicherbeleg?

## English

MVC-01 is ReadyForReview, Pending after MVC-00. FR/AC-01 creates an explicit
persistent personal SQLite store and restart evidence; 02 implements form
CRUD with post-save confirmation, non-mutating GET, 404 and cancel; 03
preserves validation, antiforgery and encoding; 04 distinguishes draft,
confirmed writes and read failure without retries; 05 uses isolated DBs,
70 % scoped coverage and untracked data/backups. Deliver model, configuration,
tests and human acceptance. No API, second app, imported data or PostgreSQL.
Explain the difference between invoking a controller and committing a write.

<!-- intake-authoring:prompts -->
DE: Nur eigene SQLite-Datei. EN: Personal SQLite file only.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/01-crud.md und basis.md. Spezifiziere MVC-01 nach Abnahme von MVC-00 ohne REST-API. Keine Implementierung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/01-crud.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Isolierte Fixtures; kein Commit, Push, Container-Build oder Zugriff auf fremde Daten.
```
<!-- intake-authoring:end -->
