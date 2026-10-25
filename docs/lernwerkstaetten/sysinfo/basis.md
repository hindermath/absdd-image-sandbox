# SysInfo: gemeinsamer Produktvertrag / Shared Product Contract

## Deutsch

Gilt für alle sechs Intakes. Produktname: **SysInfoTool**; keine Bindung an
eine Institution. Neuaufbau aus Hello World, nicht Kopie fertigen Produktcodes.
Zielgruppe und Lernablauf stehen im Werkstättenindex. Vor Specify genau eine
Sprache dokumentieren: C#, Java, Python, Rust, Go oder Swift. Der Plan wählt
idiomatische Bibliotheken; keine sechs Implementierungen gleichzeitig.

1. Betriebssysteminformationen meinen das Linux-System im Container. CPU,
   Speicher und Dateisystem können VM-/Containergrenzen widerspiegeln; sie
   beweisen keine physischen Host-Eigenschaften. Fehlende Daten sichtbar als
   nicht verfügbar kennzeichnen, nicht durch Host-Abfragen ergänzen.
2. Kategorien: `cpu`, `memory`, `disk`, `network`, `system`, `processes`.
   Hilfe und Version fragen keine Systemdaten ab. Ohne Argumente erscheint ein
   textorientiertes Menü mit nummerierten Optionen und Beenden. Bei stdin ohne
   Terminal stattdessen Hilfe ausgeben; nicht hängen oder ein Menü erzwingen.
3. Deutsch ist Standardsprache, `--lang en` Englisch. Unbekannte Sprache:
   Warnung und Deutsch. Ungültige Optionen oder Kategorien: Fehler und Exit
   ungleich 0. Erfolg: Exit 0. Keine nur durch Farbe verständlichen Zustände.
4. `--show cpu` zeigt eine Kategorie. `--export json --output snapshot.json`
   exportiert ohne Kategorie nur die freigegebenen Kategorien; dieselbe
   Regel gilt für CSV und XML, ab Stufe 1 auch YAML. Kombination mit `--show`
   beschränkt den Export auf diese Kategorie. Vorhandene Dateien nicht
   still überschreiben; bei Konflikt ohne Änderung fehlschlagen.
5. Tests und Beispiele nutzen fiktive Provider. Ein Provider ist hier ein
   Modul, das Informationen liefert, kein KI-Anbieter. Reale Erfassung braucht
   den expliziten Laufmodus `--collect container`. `network` und `processes`
   sind auch dann standardmäßig ausgenommen und nur mit
   `--include-sensitive network,processes` für diesen Lauf freigegeben.
   Ausgenommene Kategorien und der Grund bleiben sichtbar. Kein persistentes
   Opt-in, keine Kommandozeilen von Prozessen, Nutzernamen, Umgebungsvariablen,
   Tokens, Seriennummern oder fremden Dateien erfassen.
6. Standardlauf ohne `--collect container` verwendet ausdrücklich als fiktiv
   markierte Daten. `--include-sensitive` ohne realen Laufmodus ist ein
   Optionsfehler. Unbekannte Einträge werden abgelehnt; kein pauschales `all`.
7. Gemeinsames Exportmodell ab Stufe 0: `schemaVersion`, `capturedAt` (UTC),
   `source` (`fixture` oder `container`), Kategorien mit Status und Daten.
   Der Plan definiert die Feldtypen und CSV-Abbildung vor Implementierung;
   dieselben Begriffe bleiben über YAML, SQLite und REST erhalten. Kategorien
   verwenden `ok`, `partial` oder `unavailable` mit erklärtem Grund; bewusst
   ausgeschlossene Kategorien sind `unavailable`, nicht vermeintlich leer.
   CSV hat die UTF-8-Spalten `category,key,value,status,message`.
8. Nur eigene Instanzen und Arbeitsdateien; keine erhöhten Rechte,
   Host-Collector oder zusätzlichen Mounts. Exporte und SQLite können sensible
   Daten enthalten: untracked halten, Zugriff begrenzen, nicht Agenten oder
   Dritten ungeprüft übergeben. REST liefert nur gespeicherte Snapshots und
   löst niemals neue Systemabfragen aus.
9. Sicherheitsanforderungen, Tests, sprachtypische Public-API-Dokumentation
   und lesbare Fehler gehören zu jeder Stufe. Mindestens 80 % Line-/Statement-
   Coverage für testbaren eigenen Produktcode; Umfang und ausgeschlossene
   Plattformadapter offenlegen. Fehlende Messung ist Open, kein Erfolg.
10. Jede Stufe liefert spezifizierte Unit-, Integrations- und Abnahmefälle,
    eine Reviewnotiz sowie offene Punkte mit Owner, Follow-up und Trigger.
    Erst menschliche Abnahme erlaubt die nächste Stufe. Keine Produktivfreigabe.

## English

This contract governs all six intakes. Build **SysInfoTool** from Hello World
in exactly one recorded language: C#, Java, Python, Rust, Go or Swift. Choose
idiomatic libraries during planning, not six implementations at once.

1. Report the container's Linux environment; CPU, memory and disks may reflect
   VM/container constraints, not physical host properties. Mark unavailable
   values instead of expanding access.
2. Categories are cpu, memory, disk, network, system and processes. Help/version
   collect nothing. No arguments give a numbered text menu with exit; non-TTY
   stdin gives help without hanging.
3. German is default, `--lang en` selects English. Unknown language warns and
   falls back to German. Invalid options/categories fail nonzero; success is 0.
4. `--show` selects a category; `--export json|csv|xml --output` exports allowed
   categories, YAML from stage 1. Combining show and export narrows the output.
   Existing files are never silently overwritten.
5. Fixtures are the default. Real, read-only collection requires
   `--collect container`; network/processes additionally need this-run-only
   `--include-sensitive network,processes`. Show excluded categories and reasons.
   Never collect process command lines, users, environment, tokens, serials or
   unrelated files. A data provider is not an AI service provider.
6. Label fixtures visibly. Reject sensitive opt-in without real collection,
   unknown sensitive names and broad all-category shortcuts.
7. Exports share schemaVersion, UTC capturedAt, source fixture/container and
   categories with status/data. Status is ok, partial or unavailable with a
   reason, also for excluded categories. UTF-8 CSV columns are
   category,key,value,status,message. Plan types before implementation and
   preserve them through later formats/storage/API.
8. No privilege escalation, host collection or extra mounts. Protect untracked
   exports/databases and review before sharing. REST reads stored snapshots
   only; it never triggers collection.
9. Tests, secure coding and public-interface documentation apply from stage 0.
   Require at least 80 % line/statement coverage for testable own code and
   document scope/exclusions. Missing measurements remain Open.
10. Each stage supplies unit/integration/acceptance evidence, review and named
    open follow-ups. Human acceptance precedes the next stage, without claiming
    production approval.
