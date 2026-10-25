<!-- intake-authoring:begin -->
# SYS-00: CLI und Exporte / CLI and Exports

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität SYS-00; UUID im
zugehörigen Receipt. Verbindlich: [Produktvertrag](../basis.md).
**Vorbedingung:** persönlicher Hello-World-Starter, dokumentierte Sprachwahl,
aktuelle lokale Serienprüfung und ausdrücklicher Startauftrag.
**Ziel:** ein bedienbares SysInfoTool, noch ohne Datenbank oder Server.

### Anforderungen und Abnahme

- FR-01: Alle sechs Kategorien aus basis.md mit Status/Grund darstellen.
  AC-01: Fixture für Erfolg, Teilverfügbarkeit und fehlenden Zugriff liefert
  jeweils die erwartete Textausgabe ohne erfundene Werte.
- FR-02: Menü, nicht-interaktiven Modus, `--show`, Hilfe und Version anbieten.
  AC-02: Menü lässt sich per Nummer beenden; Nicht-TTY hängt nicht; unbekannte
  Option/Kategorie endet ungleich 0; Hilfe/Version rufen keinen Collector auf.
- FR-03: JSON, CSV und XML aus demselben Modell erzeugen.
  AC-03: Formatparser lesen Voll-/Kategorieexport mit identischen fachlichen
  Werten; fehlendes `--output`, bestehende Datei und Schreibfehler ändern nichts.
- FR-04: Sprachwahl und datensparsame Laufmodi aus basis.md durchsetzen.
  AC-04: Standard ist sichtbar fiktiv; ohne Opt-in wird keine reale Abfrage
  ausgeführt, sensible Kategorien bleiben ausgeschlossen, auch beim Export.
- FR-05: Tests und verständliche Code-/CLI-Dokumentation mitliefern.
  AC-05: Unit-, CLI-Integrations- und Abnahmeprotokoll sowie mindestens 80 %
  Coverage eigener testbarer Logik liegen mit Versions-/Scope-Angabe vor.

**Nicht-Ziele:** YAML, SQLite, REST, Host-Erfassung, globale Installation und
Git-Delivery. Risiken: Containerwerte als Hostwerte missverstehen, Exporte
versehentlich teilen. Maßnahmen gelten gemäß basis.md.
**Erwartete Artefakte:** Spec, Plan, Tasks, Quellcode, Tests, Help/README und
Review-/Abnahmenotiz. Lernfrage: Welche Beobachtung beweist, dass Hilfe nichts erfasst?

## English

ReadyForReview; product stage Pending. SYS-00 identifies this intake; UUID is
in its receipt. The linked shared contract governs. Prerequisites: personal
starter, selected language, current series review and explicit start authority.
Build the CLI, not a database/server. FR/AC-01 covers six category states;
02 menu, non-TTY, invalid flags and collection-free help/version; 03 parser-
checked JSON/CSV/XML full/category exports and safe write failures; 04 fixture
default, real-collection opt-in and excluded sensitive categories; 05 unit,
CLI integration and acceptance evidence with at least 80 % scoped coverage.
Deliver specs, code, tests, user/interface docs and review/acceptance notes.
No YAML, SQLite, REST, host collection, global install or Git delivery. Explain
how the help test proves no collector call; never treat container data as host data.

<!-- intake-authoring:prompts -->
DE: Erst nach persönlicher Serienprüfung und Startentscheidung verwenden.
EN: Use only after personal series review and an explicit start decision.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/00-cli.md und basis.md. Spezifiziere ausschließlich das Produkt SYS-00 in der vorab dokumentierten Sprache, nicht die Schulung. Keine Implementierung oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/00-cli.md und basis.md mit DeliveryMode LocalImplementation nur nach ausdrücklichem persönlichem Ausführungsauftrag und erfüllten Gates. Kein Commit, Push, Build eines Container-Images, Provider- oder Berechtigungseingriff.
```
<!-- intake-authoring:end -->
