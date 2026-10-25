---
title: "SysInfoTool: vom Auftrag zum geprüften Programm"
lang: de-DE
date: 2026-10-25
---

<!-- slide: S01 -->
# SysInfoTool

- Ein eigenes Programm aus Hello World entwickeln
- Spec Kit und agentische KI bewusst einsetzen
- Für Lernende ab dem ersten Ausbildungsjahr und nicht spezialisierte Entwickler

::: notes
KI bedeutet künstliche Intelligenz. Ein KI-Agent kann Werkzeuge bedienen und
Dateien ändern. Du bleibst für Auftrag, Prüfung und Entscheidungen verantwortlich.
Zuerst den Grundlagenworkshop lesen. Dieser Workshop beschreibt ein Produkt;
die Praxis beginnt erst nach eigener Freigabe im persönlichen Lernrepo.
:::

<!-- slide: S02 -->
# Was liefert eine Systeminformation?

- CPU, Speicher, Datenträger, Netzwerk, System und Prozesse
- Eine Momentaufnahme mit Zeitpunkt und Herkunft
- Verfügbare, teilweise verfügbare oder nicht verfügbare Werte

::: notes
CPU bezeichnet den Prozessor. Ein Snapshot ist eine gespeicherte Momentaufnahme.
Vorhersage: Was bedeutet eine fehlende Netzwerkadresse? Sie kann ausgeschlossen
oder nicht verfügbar sein; sie ist nicht automatisch eine leere Zeichenfolge.
Erkläre den Unterschied zwischen Wert, Status und Grund mit eigenen Worten.
:::

<!-- slide: S03 -->
# Container ist nicht physischer Host

- Das Programm läuft als adedev im Linux-Container
- Sichtbare CPU und Speicher können VM-Grenzen zeigen
- Ein Mount verbindet echte Host-Dateien
- Keine Privilegien oder zusätzlichen Mounts anfordern

::: notes
VM heißt virtuelle Maschine. Auf macOS und Windows läuft Podman häufig darin.
Containerwerte sind kein Hardwareinventar des Macs oder Windows-Rechners.
Bei fehlender Information nicht aus der Sandbox ausbrechen. Systemintegration
und IT-System-Elektronik beschreiben hier besonders die Beobachtungsgrenzen.
:::

<!-- slide: S04 -->
# Erst fiktiv, dann bewusst erfassen

- Standard und Tests verwenden markierte fiktive Daten
- Reale Erfassung nur mit --collect container
- Netzwerk und Prozesse brauchen zusätzliches Opt-in je Lauf
- Keine Prozesskommandozeilen, Nutzernamen oder Zugangsdaten

::: notes
Opt-in bedeutet bewusste Zustimmung zu einer Funktion. `--include-sensitive
network,processes` erlaubt nur diese Kategorien für diesen realen Lauf, nicht
für spätere Starts. Den exakten Vertrag in basis.md lesen. Ausgeschlossene
Kategorien bleiben mit Grund sichtbar. Keine realen Exporte in Agentenprompts kopieren.
:::

<!-- slide: S05 -->
# Eine Sprache auswählen

- C#, Java, Python, Rust, Go oder Swift
- Gleiche fachliche Funktionen und Akzeptanzkriterien
- Sprachtypische Bibliotheken erst im technischen Plan wählen
- Nicht sechs Lösungen gleichzeitig erzeugen

::: notes
Eine Akzeptanzbedingung beschreibt ein beobachtbares Ergebnis. Der Agent darf
die Sprache nicht still wählen. Vor Specify die Wahl im Lernrepo dokumentieren.
PowerShell bleibt eine Skriptsprache der Umgebung, erweitert aber diese sechs
Produktsprachen nicht. Ein Sprachwechsel ist später eine neue Entscheidung.
:::

<!-- slide: S06 -->
# Sechs Stufen mit klaren Übergaben

- SYS-00 CLI und JSON/CSV/XML → SYS-01 YAML
- SYS-02 SQLite → SYS-03 REST-API
- SYS-04 Dokumentation → SYS-05 Evidenzreview
- Erst Abnahme, dann die nächste Stufe

::: notes
CLI bedeutet Kommandozeilenschnittstelle. JSON, CSV, XML und YAML sind
Datenformate. SQLite speichert Daten in einer Datei. REST wird in S12 erklärt.
Jede Kante bedeutet: Vorgänger menschlich abgenommen und Nachweise aktuell.
Die ausgelieferte Serie ist Draft, alle Stufen Pending. Das ist kein bisheriger
Lernerfolg und keine Startbefugnis. Die vollständige Reihenansicht steht im Paket.
:::

<!-- slide: S07 -->
# Auftrag und Spezifikation trennen

- Intake: Ziel, Grenzen und messbare Abnahme
- Specify: das Produkt spezifizieren, nicht den Workshop
- Clarify: nur entscheidungsrelevante Unklarheiten klären
- Eine Frage nach der anderen; keine Endlosschleife

::: notes
Lies zuerst SYS-00 und basis.md. Vorhersage: Welche Anforderung verhindert eine
Abfrage bei --help? Suche AC-02. Der Prompt unten ist ein Codex-Skill-Auftrag,
kein Bash-Befehl. Andere Agenten können andere installierte Aufrufnamen haben.
:::

```text
$speckit-specify Nutze intakes/00-cli.md und basis.md.
Spezifiziere nur SYS-00 in der dokumentierten Sprache.
Keine Implementierung, kein Commit oder Push.
```

<!-- slide: S08 -->
# Plan, Checklist, Tasks und Analyze

- Plan legt Bausteine, Bibliotheken und Datenvertrag fest
- Checklist prüft die Qualität der Anforderungen
- Tasks zerlegen die Umsetzung in überprüfbare Schritte
- Analyze gleicht die Artefakte ausschließlich lesend ab

::: notes
Spezifikation, Plan und Aufgabenliste sind verschiedene Artefakte, also
Arbeitsergebnisse. Eine grüne Anforderungs-Checklist beweist keinen funktionierenden
Export. Bei einem Finding die konkrete Korrektur getrennt beauftragen und nur
den betroffenen Stand erneut prüfen. Keine Freigabe durch Wiederholung erzwingen.
:::

<!-- slide: S09 -->
# SYS-00: einen Export wirklich prüfen

- Dieselbe Fixture für JSON, CSV und XML
- Datei mit einem passenden Parser zurücklesen
- Werte, Kategorie, Status und Herkunft vergleichen
- Bestehende Datei bei Fehlern unverändert lassen

::: notes
Ein Parser liest ein Datenformat strukturiert. Ein Dateiname mit .json beweist
keine gültige JSON-Datei. Basisaufgabe: erwarteten CPU-Wert und Status vorhersagen.
Vertiefung: Wie wird eine Kategorie mit mehreren Werten in CSV abgebildet?
Diese Entscheidung muss der Plan vor Codeerzeugung treffen.
:::

<!-- slide: S10 -->
# SYS-01: YAML ergänzt den Vertrag

- Nur ein weiteres Format, keine neuen Systemdaten
- Voll- und Kategorieexport müssen fachlich gleich bleiben
- Umlaute und mehrzeilige Texte sind Daten
- Keine ausführbaren YAML-Typ-Tags oder Importfunktion

::: notes
YAML kann vielfältige Typangaben enthalten. Diese Übung benötigt sichere
Datenskalare, keine Objektinstanziierung. Teste fiktive Zeichenfolgen, die wie
Syntax aussehen. Die Ausgabe muss nach Parser-Rücklesen denselben Inhalt
besitzen. Vorherige Formate behalten ihre Regressionstests.
:::

<!-- slide: S11 -->
# SYS-02: Speicherung ist ein Versprechen

- Snapshot mit ID, Zeitpunkt und Herkunft speichern
- Nach Neustart denselben Inhalt lesen
- Transaktion verhindert halbe Snapshots
- Datenbank ist kein Build-Artefakt und kein Git-Backup

::: notes
Eine Transaktion fasst Änderungen zusammen: alles oder nichts. Sage vor einem
simulierten Schreibfehler voraus, wie viele Snapshots danach existieren dürfen.
Tests nutzen nur eigene temporäre Datenbanken. Backups müssen außerhalb von Git
geschützt werden. Daten- und Prozessanalyse erklärt den Snapshot-Datenweg.
:::

<!-- slide: S12 -->
# SYS-03: REST arbeitet mit gespeicherten Daten

- API bedeutet Application Programming Interface
- HTTP-Operationen lesen oder ändern Snapshots
- Ein Aufruf darf keine neue Systemerfassung auslösen
- Lokales HTTPS, Grenzen und Fehlantworten gehören zum Vertrag

::: notes
REST bezeichnet hier einen Ressourcenvertrag über HTTP. GET liest, POST legt
an, PUT ersetzt und DELETE löscht. Ein Collector ist das Modul für Erfassung;
ein HTTP-Test ersetzt es durch ein Modul, das beim Aufruf fehlschlägt. Der CRUD-
Durchlauf muss dennoch bestehen. CRUD heißt Create, Read, Update, Delete.
Das beweist die Trennung besser als ein bloßer Kommentar. Port 5113 bleibt lokal.
:::

<!-- slide: S13 -->
# SYS-04: Dokumentation gehört zum Produkt

- Code-Referenz aus sprachtypischen Kommentaren
- CLI-Hilfe mit Optionen und Exitcodes
- API-Referenz aus aktuellem OpenAPI-Vertrag
- Dokumenterzeugung startet keinen Server

::: notes
OpenAPI ist eine maschinenlesbare Beschreibung der HTTP-Schnittstelle. Eine
Code-API kann dagegen eine öffentliche Methode sein; beides nicht verwechseln.
Vorhersage: Was soll passieren, wenn Eingabedateien des Generators fehlen?
Fehler melden, nicht eine alte Ausgabe als aktuell verkaufen. Beispiele bleiben fiktiv.
:::

<!-- slide: S14 -->
# SYS-05: Nachweise statt Freigabe behaupten

- Anforderungen und Kontrollen auf Evidenz abbilden
- Applicable, N/A und Open begründen
- Open braucht Owner, Follow-up und Trigger
- Quellenübernahme ist keine Risikoakzeptanz

::: notes
Evidenz ist ein überprüfbarer Nachweis. Applicable bedeutet anwendbar, N/A nicht
anwendbar, Open offen. Eine installierte Richtlinie erfüllt nicht jede Kontrolle.
Technische Tests, menschliche Abnahme und formale Freigabe getrennt halten.
Sicherheitskontrollen gelten seit SYS-00; SYS-05 prüft ihre Nachweise.
:::

<!-- slide: S15 -->
# Gemeinsam prüfen, unterschiedlich vertiefen

- Basis: einen Erfolgs- und einen Fehlerfall erklären
- Entwicklung: Test und Implementierung verbinden
- Betrieb/Vernetzung: Grenzen, Rechte und Schnittstellen beschreiben
- Management: Nutzen, Aufwand und Abnahme begründen

::: notes
Wähle die passende Aufgabe aus der Berufstabelle im Werkstättenindex. Keine
Perspektive bekommt weniger Schutz. Mindestens 80 % Coverage eigener testbarer
Logik ist ein Nachweis mit Grenzen, kein Qualitätszertifikat. Lernenden- und
A11Y-Review mit echten Nutzenden bleibt separat erforderlich.
:::

<!-- slide: S16 -->
# Jetzt den ersten Auftrag vorbereiten

- Das SysInfo-Paket in ein leeres persönliches Repo übernehmen
- Sprache und Arbeitsort festhalten
- Ganze Serie prüfen und selbst über Start entscheiden
- Nur SYS-00 beginnen, keine Folgeaufgabe vorziehen

::: notes
Eine optionale Template-Kopie ist nur die eigene Sandbox, nicht das SysInfo-
Produkt. Sie übernimmt keine Abnahmen und ist derzeit nicht als Bezugsprofil
aktiviert. Materialien: [SysInfo-Paket](../lernwerkstaetten/sysinfo/README.md) und
[Übernahme-/Spec-Kit-Ablauf](../lernwerkstaetten/README.md). Bearbeite nun die
Lernfrage von SYS-00, bevor du einen Prompt startest. Lehrende finden getrennte
Musterantworten im Moderationskapitel. Dieser Foliensatz führt selbst nichts aus.
:::
