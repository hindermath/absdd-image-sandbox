<!-- intake-authoring:begin -->
# MVC-00: Formular und Datenweg / Form and Data Flow

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität MVC-00; UUID im
Receipt. [basis.md](../basis.md) ist verbindlich. Vorbedingung: persönlicher
C#-Starter, begründete Wahl A in decision.md, aktuelle Serienprüfung und eigener
Startauftrag. Noch keine Datenbank; die erste Oberfläche nutzt Fixture-Daten.

- FR-01: Razor-Seite mit zwei beschrifteten Pflichtfeldern und einer Fixture-Liste.
  AC-01: Browser erhält HTML; Modell, View und Controller werden am Request
  erklärt, kein REST-Client oder zweiter App-Prozess existiert.
- FR-02: Formular serverseitig validieren. AC-02: leer, Whitespace, NUL und
  1001 UTF-16-Einheiten werden abgelehnt; 1000 sind erlaubt, Trim erst danach.
- FR-03: Sicheren temporären Zustand sichtbar machen.
  AC-03: gültige Eingabe wird nur als ungespeicherte Vorschau bezeichnet,
  ungültiger Entwurf bleibt erhalten; Neustart beansprucht keine Persistenz.
- FR-04: HTTPS-/Formularschutz und barrierearme Bedienung einplanen.
  AC-04: Antiforgery-Negativfall, HTML-Kodierung, Body-/Schreiblimit, Labels,
  Tastatur und verständliche Fehler nach basis.md sind prüfbar beschrieben.
- FR-05: Nachweise mitliefern. AC-05: Unit- und echte HTTP-Fälle, UI-Sichtung,
  mindestens 70 % scoped Coverage und DE/EN-Dokumentation vorhanden.

**Artefakte:** MVC-Produkt, Datenweg, Tests, Review/Abnahme. **Nicht-Ziele:**
SQLite, fachliche REST-API, Benutzerverwaltung, Deployment oder App-Container.
Risiko: Vorschau als gespeicherten Datensatz ausgeben.
Lernfrage: Wo wird Razor ausgeführt, und was sieht der Browser?

## English

MVC-00 is ReadyForReview; Pending. The shared contract governs. Require a
personal C# starter, recorded route-A decision, current review and authority.
FR/AC-01 builds a labelled Razor form and fictional list in one MVC process;
02 tests all validation boundaries; 03 clearly labels unsaved preview and
preserves invalid drafts without persistence claims; 04 covers HTTPS, form
security, limits, keyboard, labels and errors; 05 supplies unit/HTTP/UI evidence,
70 % scoped coverage and DE/EN docs. No SQLite, API, account system, deployment
or app containers. Explain server-side Razor and browser-side HTML.

<!-- intake-authoring:prompts -->
DE: Nur Weg A starten. EN: Start route A only.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/00-formular.md und basis.md. Spezifiziere MVC-00 nach dokumentierter Wahl A. Keine Implementierung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/00-formular.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Kein Commit, Push, Container-Build, Trust-Bypass oder Provider-/Berechtigungseingriff.
```
<!-- intake-authoring:end -->
