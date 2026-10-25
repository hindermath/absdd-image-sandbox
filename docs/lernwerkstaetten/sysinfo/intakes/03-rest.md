<!-- intake-authoring:begin -->
# SYS-03: Gespeicherte Snapshots über REST / Stored Snapshots over REST

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität SYS-03; UUID im
Receipt. [basis.md](../basis.md) gilt. Vorbedingung: SYS-02 abgenommen und
vertrauenswürdiges lokales HTTPS bewusst vorbereitet; keine Trust-Umgehung.

- FR-01: Servermodus `--serve --database snapshots.db --host 0.0.0.0 --port 5113`
  im Entwicklungscontainer; Host-Freigabe nur Loopback. AC-01: eigene HTTPS-
  Instanz erreichbar, kein Host-Collector und keine erhöhte Berechtigung nötig.
- FR-02: POST/GET `/snapshots`, GET/PUT/DELETE `/snapshots/{id}` und `/health`
  dokumentieren. AC-02: POST 201/Location, GET 200, PUT/DELETE 204, fehlende ID
  404; neu angelegte Fixture wird gelesen, ersetzt und gelöscht.
- FR-03: Nur übermittelte/gespeicherte Snapshots, nie Live-Erfassung auslösen.
  AC-03: Alle HTTP-Tests benutzen einen Collector, der bei Aufruf fehlschlägt;
  der CRUD-Durchlauf besteht trotzdem, Opt-in kann remote nicht gesetzt werden.
- FR-04: JSON-Vertrag, Validierung und Limits festlegen. AC-04: kaputtes JSON
  oder ungültiges Schema 400, Body über 64 KiB 413, 60 Schreibaufrufe je 60
  Sekunden/IP als Budget mit 429/Retry-After; keine Datenänderung bei Ablehnung.
- FR-05: Allgemeine Fehler ohne Payload/Secrets, kein automatischer Write-Retry,
  OpenAPI aktuell. AC-05: echte HTTP-Vertrags- und Fehlerfälle mit isolierter DB,
  Unit-/Integrationsnachweise und mindestens 80 % Coverage liegen vor.

**Artefakte:** OpenAPI, Servermodus, Threat-/Risikonotiz, Tests, Betriebsgrenzen
und Abnahme. **Nicht-Ziele:** Authentifizierung, öffentlicher Betrieb oder
Telemetrie. Eigene nichtproduktive Instanz ist keine Mehrbenutzerlösung.
Lernfrage: Warum darf ein GET-Aufruf keine neue Systemerfassung bewirken?

## English

SYS-03 is ReadyForReview, Pending after SYS-02 acceptance and explicitly
prepared trusted HTTPS. Bind the sandbox server to 0.0.0.0:5113 with loopback
host exposure. FR/AC-01 proves local reachability without escalation; 02
defines snapshot CRUD, health and 201/200/204/404; 03 proves HTTP never calls
a collector or grants real-data opt-in; 04 checks 400, 64-KiB 413 and the
60-writes/60-seconds/IP budget with 429/Retry-After; 05 checks safe errors,
no retries, OpenAPI and at least 80 % scoped coverage. Deliver contract,
server, isolated HTTP/unit/integration tests, risks and acceptance. No public
deployment, telemetry or multiuser/auth claim. Explain read-versus-collection.

<!-- intake-authoring:prompts -->
DE: Fehlendes HTTPS-Vertrauen stoppt Ausführung. EN: Missing HTTPS trust blocks execution.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/03-rest.md und basis.md. Spezifiziere SYS-03 mit gespeicherten Snapshots und den lokalen Sicherheitsgrenzen. Keine Implementierung, Zertifikatsänderung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/03-rest.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Kein Commit, Push, Container-Build, Trust-Bypass, Provider- oder Berechtigungseingriff.
```
<!-- intake-authoring:end -->
