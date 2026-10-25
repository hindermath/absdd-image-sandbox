<!-- intake-authoring:begin -->
# REST-02: MVC als API-Client / MVC as API Client

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität REST-02; UUID im
Receipt. [basis.md](../basis.md) gilt; REST-01 abnehmen. Ziel: zweiter
App-Prozess für die Oberfläche, keine zweite Datenbank.

- FR-01: MVC/Razor mit serverseitigem HTTP-Client anbinden.
  AC-01: Browser erhält HTML, MVC tauscht JSON mit API, nur API liest SQLite;
  kein direkter Browser-API-Aufruf und keine CORS-Freigabe nötig.
- FR-02: CRUD mit gleichen zwei Pflichttexten und verständlichen Entwürfen.
  AC-02: Create/Read/Update/Delete über UI erfolgreich, Abbrechen verändert
  nichts, API validiert unabhängig von Browser und MVC.
- FR-03: Antwortvertrag und Fehler prüfen.
  AC-03: ungültiges JSON, falsches Schema/ID, unerwarteter Erfolgsstatus,
  leere Antwort und API-Ausfall sind unterscheidbar getestet, nicht als Erfolg verborgen.
- FR-04: Zehn Sekunden Client-Timeout, Abbruch und unsichere Schreibantwort behandeln.
  AC-04: Timeout und bewusster Abbruch unterschieden; kein automatischer
  Write-Retry, Entwurf bleibt und Lesen klärt den Bestand vor manueller Wiederholung.
- FR-05: Formularschutz und Bedienbarkeit nach basis.md.
  AC-05: Antiforgery/Encoding/CSP/Limits, Tastatur/Löschdialog/Labels,
  Unit-/HTTP-/UI-Nachweise; mindestens 70 % Coverage je App, nicht nur insgesamt.

**Artefakte:** MVC und API-Client, Datenweg mit Textalternative, Vertrauens-
konfiguration ohne Secrets, Tests und Review/Abnahme. **Nicht-Ziele:** SPA,
zusätzliche DB, Trust-All, neue API-Routen, öffentliche Bereitstellung.
Lernfrage: Warum ist FE-Arbeit hier nicht gleichbedeutend mit JavaScript im Browser?

## English

REST-02 is ReadyForReview, Pending after REST-01. FR/AC-01 adds a separate
server-rendered MVC app with server HTTP client and no DB access/CORS;
02 proves UI CRUD/cancel and independent API validation; 03 rejects bad
JSON/schema/IDs/status/empty responses and distinguishes API failure; 04
tests ten-second timeout versus cancellation, preserves drafts and never
automatically retries uncertain writes; 05 proves form protections, keyboard
behavior and at least 70 % own-code coverage per app. Deliver client/UI,
text-first flow, trust configuration without keys, tests and acceptance.
No SPA, second DB, trust bypass, new routes or public deployment. Explain
why frontend responsibility can include server-side MVC code.

<!-- intake-authoring:prompts -->
DE: API-Vertrag nicht still ändern. EN: Do not silently change the API contract.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/02-mvc-client.md und basis.md. Spezifiziere REST-02 als serverseitigen MVC-Client der abgenommenen API. Keine Implementierung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/02-mvc-client.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Kein Commit, Push, Container-Build, Trust-Bypass oder Provider-/Berechtigungseingriff.
```
<!-- intake-authoring:end -->
