<!-- intake-authoring:begin -->
# REST-01: API-Persistenz mit SQLite / API Persistence with SQLite

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität REST-01; UUID im
Receipt. [basis.md](../basis.md) gilt; REST-00 abnehmen. Persistenz heißt hier,
dass bestätigte Daten einen Prozessneustart überstehen.

- FR-01: Fixture-Speicher durch EF Core/SQLite ersetzen, HTTP-Vertrag erhalten.
  AC-01: eigener DB-Pfad im Projekt-Mount; nur API hat Datenzugriff, kein
  Nachbarbestand wird übernommen; API-Antworten bleiben vertragstreu.
- FR-02: Bestätigte CRUD-Änderungen dauerhaft speichern.
  AC-02: drei Einträge über echte HTTP-Anfragen anlegen, Neustart mit derselben
  DB, Werte/IDs prüfen, einen ändern/löschen; höchste ID zuerst.
- FR-03: Fehler atomar behandeln. AC-03: erzwungener DB-Fehler liefert keinen
  Erfolg und keinen Teilbestand; Quotes bleiben Daten, keine SQL-Steuerung.
- FR-04: Validierung/Limits und Fehlerhygiene erhalten.
  AC-04: ungültige Eingaben, 404, 413, 429 und sicherer 500-Fall mit
  unverändertem Bestand geprüft; kein Write-Retry und keine Payload-Logs.
- FR-05: Tests und Datenpflege isolieren.
  AC-05: separate temporäre Test-DBs, mindestens 70 % API-Coverage, DB/Backups
  untracked; Wiederherstellung und Grenzen von EnsureCreated dokumentiert.

**Artefakte:** EF-Modell, Konfiguration, Vertrags-/Persistenztests,
Betriebsnotiz und Abnahme. **Nicht-Ziele:** MVC, Datenmigration aus Referenzen,
PostgreSQL, Multiuser-Freigabe. Lernfrage: Was beweist ein Test nach Neustart,
das ein einzelner erfolgreicher POST nicht beweist?

## English

REST-01 is ReadyForReview, Pending after REST-00. FR/AC-01 replaces fixtures
with API-owned SQLite without changing HTTP; 02 proves IDs/values/CRUD survive
restart; 03 proves atomic failures and parameterized data; 04 preserves input,
status/limit/error hygiene without retries or payload logs; 05 isolates tests,
keeps data/backups untracked, documents restore/schema limits and proves at
least 70 % API coverage. No MVC, imported data, PostgreSQL or multiuser claim.
Deliver model/configuration/contracts/tests and human acceptance. Explain
what restart evidence adds beyond a successful POST.

<!-- intake-authoring:prompts -->
DE: Nur API besitzt die DB. EN: Only the API owns the database.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/01-sqlite.md und basis.md. Spezifiziere REST-01 nach Abnahme von REST-00 unter Erhalt des HTTP-Vertrags. Keine Implementierung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/01-sqlite.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Nur isolierte Übungsdaten; kein Commit, Push, Container-Build oder fremder Datenzugriff.
```
<!-- intake-authoring:end -->
