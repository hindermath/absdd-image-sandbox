<!-- intake-authoring:begin -->
# MVC-02: Fehler und Bedienbarkeit / Errors and Usability

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität MVC-02; UUID im
Receipt. [basis.md](../basis.md) gilt; MVC-01 abnehmen. Bestehende Schutzregeln
vertiefen, nicht erstmals einschalten.

- FR-01: Zustand für leer, geladen, Ladefehler, Feldfehler und unbestätigtes
  Schreiben explizit abbilden. AC-01: je Zustand eigener Test mit erwarteter
  Meldung; kein Fehler zeigt Erfolg oder leere Daten als Ersatz.
- FR-02: Löschbestätigung und Bearbeitung vollständig per Tastatur bedienen.
  AC-02: Abbrechen unverändert, Bestätigen löscht nur gewählte ID; Fokus und
  Fehlerzuordnung beobachtet, reine Farbhinweise reichen nicht.
- FR-03: Sichere Limits und Fehlerpfade nachweisen.
  AC-03: 413 und 429/Retry-After hinterlassen Bestand unverändert; GET bleibt
  lesbar, allgemeiner Fehler trägt Kennung ohne interne Details/Rohdaten.
- FR-04: Wiederherstellung ohne Wiederholungs-Schreibauftrag anbieten.
  AC-04: bei unklarer Antwort bleibt Entwurf; erst Lesen klärt den Bestand,
  ein testbarer Client-/Serverpfad löst keinen automatischen Write-Retry aus.
- FR-05: DE/EN und bestehende Anforderungen regressionsprüfen.
  AC-05: automatisierte Nachweise mit mindestens 70 % Coverage; menschliche
  A11Y-/Erstnutzungsprüfungen real protokollieren oder als Open mit Owner/Trigger führen.

**Artefakte:** Zustandsmodell, UI-/HTTP-Negativfälle, Bedien-/A11Y-Review,
Abnahme. **Nicht-Ziele:** Anmeldung, API, Öffnung ins Netzwerk, Sicherheitsfreigabe.
Risiko: mehrfache Speicherung nach unklarer Antwort.
Lernfrage: Wie unterscheidet die Oberfläche fehlende Daten von einem Datenbankausfall?

## English

MVC-02 is ReadyForReview, Pending after MVC-01. Deepen existing controls.
FR/AC-01 tests empty/loaded/read-error/field-error/uncertain-write separately;
02 checks keyboard delete/cancel/focus and textual errors; 03 proves 413,
429/Retry-After and safe generic errors without changing data; 04 preserves
drafts and reads before any deliberate retry; 05 preserves DE/EN and at least
70 % coverage with human A11Y evidence or named Open items. Deliver states,
negative tests and acceptance. No authentication, API or network exposure.
Explain how an empty collection differs from database failure.

<!-- intake-authoring:prompts -->
DE: Vorhandenen Schutz erhalten. EN: Preserve existing protections.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/02-fehler-und-bedienung.md und basis.md. Spezifiziere MVC-02 mit getrennten Fehlerzuständen. Keine Implementierung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/02-fehler-und-bedienung.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Kein Commit, Push, Container-Build, Trust-Bypass oder Provider-/Berechtigungseingriff.
```
<!-- intake-authoring:end -->
