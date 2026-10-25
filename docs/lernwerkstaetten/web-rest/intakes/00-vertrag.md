<!-- intake-authoring:begin -->
# REST-00: Vertrag und API mit Fixtures / Contract and Fixture API

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität REST-00; UUID im
Receipt. [basis.md](../basis.md) gilt. Vorbedingung: persönlicher C#-Starter,
begründete Wahl B in decision.md, aktuelles Serienreview und eigener Startauftrag.

- FR-01: HTTP-Vertrag gemäß basis.md als OpenAPI beschreiben.
  AC-01: fünf CRUD-Operationen mit DTO-Feldern, Erfolgs-/Fehlerstatus und
  Beispielen; DTO heißt Datenübertragungsobjekt und ist nicht das DB-Modell.
- FR-02: API mit isoliertem flüchtigem Fixture-Speicher bereitstellen.
  AC-02: POST/GET/PUT/DELETE funktionieren mit eigenen IDs; Neustart setzt
  Fixtures zurück und wird ausdrücklich noch nicht als Persistenz bezeichnet.
- FR-03: JSON-Eingaben unabhängig von jedem Browser validieren.
  AC-03: leer, Whitespace, NUL, 1001 Codeeinheiten oder kaputtes JSON geben
  400; 1000 sind zulässig, ungültige Aktionen verändern nichts.
- FR-04: HTTPS, Body-/Schreiblimits und sichere Fehler von Anfang an.
  AC-04: 413/429 samt Retry-After, fehlende ID 404, generischer 500-Fall ohne
  Secrets/Rohdaten nachgewiesen; kein pauschales CORS oder Trust-Bypass.
- FR-05: Vertrag und Ausführung verbinden.
  AC-05: echte HTTP-Vertragstests, Unit-Tests und mindestens 70 % scoped
  API-Coverage; Dokumente behaupten weder MVC-Oberfläche noch Datenbank.

**Artefakte:** OpenAPI, API-Fixture, Tests, Risiken und Review/Abnahme.
**Nicht-Ziele:** UI, SQLite, Authentifizierung, öffentlicher Betrieb oder App-Container.
Lernfrage: Warum kann eine API schon ohne Weboberfläche überprüft werden?

## English

REST-00 is ReadyForReview, Pending. Require personal C# starter, recorded
route-B decision, current review and start authority. FR/AC-01 defines OpenAPI
CRUD/DTO/status examples; 02 runs a clearly nonpersistent fixture API; 03
checks JSON/field boundaries independent of browser; 04 proves HTTPS, limits,
404 and generic safe errors; 05 supplies real HTTP contract/unit evidence
and at least 70 % API coverage. No MVC UI, SQLite, accounts, deployment or
app containers. Explain why the interface can be tested without a browser UI.

<!-- intake-authoring:prompts -->
DE: Nur Weg B starten. EN: Start route B only.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/00-vertrag.md und basis.md. Spezifiziere REST-00 nach dokumentierter Wahl B. Keine Implementierung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/00-vertrag.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Kein Commit, Push, Container-Build, Trust-Bypass oder Provider-/Berechtigungseingriff.
```
<!-- intake-authoring:end -->
