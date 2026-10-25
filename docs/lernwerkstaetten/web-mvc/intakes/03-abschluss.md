<!-- intake-authoring:begin -->
# MVC-03: Dokumentation und Abschlussreview / Documentation and Closure Review

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität MVC-03; UUID im
Receipt. [basis.md](../basis.md) gilt; MVC-02 abnehmen. Ziel: den begrenzten
Lernstand prüfbar übergeben, nicht einen öffentlichen Dienst freigeben.

- FR-01: Browser → MVC → EF Core → SQLite und Antwort als HTML erklären.
  AC-01: vollständiger Text vor ergänzendem Diagramm; kein REST-Zwischenaufruf
  oder API-Vertrag behauptet. C#-Public-API-Doku ist von HTTP-REST zu unterscheiden.
- FR-02: Reproduzierbare Tests/Code-Dokumentation und Betriebsanleitung liefern.
  AC-02: aktueller Stand, Befehle, Exitcodes, mindestens 70 % scoped Coverage,
  Start/Stopp sowie Sicherung eigener gestoppter DB dokumentiert.
- FR-03: Sicherheits- und Governance-Anwendbarkeit nachweisen.
  AC-03: Anforderungen/Controls haben Belege oder begründetes N/A/Open;
  offene Punkte mit Owner, Follow-up, Trigger und human-only-Entscheidungen getrennt.
- FR-04: Entscheidungsnotiz anhand des fertigen Produkts erneut prüfen.
  AC-04: Vorteile, Nachteile und Neubewertungsauslöser mit Quellen/Beobachtungen
  verbunden; Produktionsbetrieb und Plattform-/A11Y-Abnahmen nicht überbehauptet.
- FR-05: Lernenden-Erklärung und menschliches Abschlussreview ermöglichen.
  AC-05: eine andere Person kann einen CRUD- und einen Fehlerfall mit Text
  nachvollziehen; Reviewer/Datum/Umfang festhalten oder offene Abnahme kennzeichnen.

**Artefakte:** Referenz/README, Testübersicht, Kontrollmatrix, Entscheidungsnotiz,
Review/Abnahme. **Nicht-Ziele:** neuer Scope, Deployment, SBOM-/Rechts-/Release-
Freigabe ohne Nachweis. Lernfrage: Wann wäre ein neuer REST-Pfad begründet?

## English

MVC-03 is ReadyForReview, Pending after MVC-02. Deliver a bounded learning
handover, not public approval. FR/AC-01 explains the single-process data flow
with full text and no invented REST layer; 02 records reproducible tests/docs,
70 % coverage and safe personal-data operations; 03 maps requirements/controls
to evidence or reasoned N/A/Open with named follow-ups; 04 revisits decision
tradeoffs without unsupported platform/A11Y/production claims; 05 records
another person's CRUD/error explanation and human review or Open acceptance.
No new feature, deployment or unsupported supply-chain/legal/release claims.
Explain which new requirement would justify a future separate REST route.

<!-- intake-authoring:prompts -->
DE: Abschluss ist keine Produktivfreigabe. EN: Closure is not production approval.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/03-abschluss.md und basis.md. Spezifiziere MVC-03 für Dokumentation und begrenztes Abschlussreview. Keine Implementierung, Freigabe oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/03-abschluss.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Keine formale Freigabe, kein Commit, Push, Container-Build oder Plattform-/Provideränderung.
```
<!-- intake-authoring:end -->
