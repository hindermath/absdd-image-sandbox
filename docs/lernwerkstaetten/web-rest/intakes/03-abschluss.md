<!-- intake-authoring:begin -->
# REST-03: Vertrag, Nachweise und Abschluss / Contract, Evidence and Closure

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität REST-03; UUID im
Receipt. [basis.md](../basis.md) gilt; REST-02 abnehmen. Ziel: überprüfbare
Übergabe der beiden Prozesse im lokalen, nichtproduktiven Lernumfang.

- FR-01: Code-, CLI-/Start- und REST-Dokumentation aktuell erzeugen.
  AC-01: OpenAPI stimmt mit echten HTTP-Tests überein; Code-Referenz,
  Datenweg und Fehlerpfade in DE/EN mit vollständigen Textalternativen.
- FR-02: Anwendung, API und Datenbestand getrennt betreiben erklären.
  AC-02: Startreihenfolge, Vertrauensprüfung, Stopp, eigene DB-Sicherung und
  Wiederherstellung dokumentiert; API-Ausfall ist nicht leere Liste.
- FR-03: Nachweismatrix pro Anforderung/Kontrolle liefern.
  AC-03: aktuelle Unit-/HTTP-/Integrations-/UI-Nachweise, mindestens 70 %
  Coverage je App; historische Referenzberichte sind keine lokalen Ergebnisse.
- FR-04: Sicherheitsgrenzen und offene Punkte zusammenführen.
  AC-04: Owner/Follow-up/Trigger für Open, Grund für N/A; keine formale
  Provider-, Rechts-, SBOM-/VEX-/SLSA-/AI-SBOM- oder Public-Release-Freigabe erfinden.
- FR-05: Architekturentscheidung und menschliches Review nachführen.
  AC-05: Mehrclient-/Vertragsbedarf, zusätzliche Fehlergrenzen und Aufwand
  begründet; Plattform-/A11Y-Abnahmen real dokumentieren oder Open lassen.

**Artefakte:** aktueller Vertrag/Referenz, Betriebshilfe, Matrix, Entscheidung,
Review/Abnahme. **Nicht-Ziele:** neuer Produktscope, PostgreSQL, Deployment,
Sicherheitsmaßnahmen erst hier aktivieren. Lernfrage: Welchen Vorteil und
welche zusätzliche Pflicht hat die Trennung in zwei Prozesse tatsächlich gebracht?

## English

REST-03 is ReadyForReview, Pending after REST-02. FR/AC-01 regenerates current
code/start/API references with text alternatives; 02 explains two-process
operation, trust, restart, personal backups and failure distinctions; 03
maps requirements to current tests with at least 70 % coverage per app and
does not reuse historical reference success; 04 records reasoned N/A and
named Open follow-ups without human/supply-chain/release approvals; 05
revisits tradeoffs and human review while keeping unperformed A11Y/platform
acceptance Open. No new scope, PostgreSQL or deployment. Controls applied from
the first stage. Explain one actual benefit and obligation of separation.

<!-- intake-authoring:prompts -->
DE: Technische Evidenz und Freigabe trennen. EN: Separate technical evidence from approval.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/03-abschluss.md und basis.md. Spezifiziere REST-03 als begrenzte Dokumentations-/Evidenzübergabe. Keine Implementierung, formale Freigabe oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/03-abschluss.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Kein Commit, Push, Container-Build, keine formale Freigabe oder Plattform-/Provideränderung.
```
<!-- intake-authoring:end -->
