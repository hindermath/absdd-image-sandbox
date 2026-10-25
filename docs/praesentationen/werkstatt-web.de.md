---
title: "Webanwendung oder MVC plus REST-API"
lang: de-DE
date: 2026-10-25
---

<!-- slide: B01 -->
# Zwei Wege zu einer Webanwendung

- Ein eigenes kleines Produkt aus Hello World entwickeln
- Zwei Pflichttexte anlegen, lesen, ändern und löschen
- Erst Anforderungen und Architektur wählen, dann Spec Kit einsetzen

::: notes
Dieser Workshop baut auf der Spec-Kit-Einführung auf. Beide Wege liefern eine
Webanwendung; Weg B ergänzt eine getrennte REST-API, ersetzt nicht die
Weboberfläche. Die Referenzen zeigen mögliche Lösungen, keine schon erledigten
Übungen. Nutze nur ein eigenes Repo und fiktive Daten.
:::

<!-- slide: B02 -->
# Gemeinsam ist das fachliche Ziel

- CRUD: Create, Read, Update, Delete
- Zwei Pflichtfelder und eine erzeugte ID
- Bestätigtes Speichern und verständliche Fehler
- Keine Anmeldung oder Rechte pro Datensatz

::: notes
CRUD heißt Anlegen, Lesen, Ändern, Löschen. Eine ID identifiziert einen Datensatz,
nicht einen Benutzer. Die Übung ist eine persönliche lokale Instanz. Ohne
Anmeldung und Rechteprüfung darf daraus kein gemeinsamer öffentlicher Dienst
werden. Vorhersage: Darf eine fehlende ID eine beliebige Zeile löschen? Nein.
:::

<!-- slide: B03 -->
# Weg A: MVC und Datenbank in einem Prozess

- Browser sendet Formular oder GET an MVC
- Razor erzeugt HTML auf dem Server
- Controller verwendet EF Core direkt für SQLite
- Kein fachlicher REST-Aufruf zwischen Controller und Datenzugriff

::: notes
MVC heißt Model View Controller: Modell, Anzeige und Steuerung. EF Core ist
eine Datenzugriffsbibliothek, SQLite eine eingebettete Datenbank. Der Datenweg
lautet Browser → MVC → EF Core → SQLite; Daten gehen zurück, MVC liefert HTML.
Alle App-Bausteine außer dem Browser liegen in einem Prozess. C#-Methoden sind
ebenfalls Schnittstellen, aber nicht automatisch HTTP-REST-Endpunkte.
:::

<!-- slide: B04 -->
# Weg B: MVC spricht mit einer REST-API

- Browser erhält HTML von MVC
- Server-Client in MVC sendet HTTP und JSON zur API
- Nur die API verwendet EF Core und SQLite
- Zwei App-Prozesse mit eigenem Vertrag und Ausfallgrenzen

::: notes
API heißt Application Programming Interface, also Programmierschnittstelle.
REST bezeichnet hier einen Ressourcenvertrag über HTTP. Der vollständige Weg:
Browser → MVC samt HTTP-Client → REST-API → EF Core → SQLite; zurück als JSON
zu MVC und als HTML zum Browser. Kein Browser-JavaScript ruft direkt die API
auf. Deshalb braucht dieser Weg keine zusätzliche CORS-Freigabe.
:::

<!-- slide: B05 -->
# Die Wahl beginnt bei einer Muss-Anforderung

- Nur Browser und kompakter Einstieg: Weg A prüfen
- Vereinbarter JSON-Zugriff für weitere Clients: Weg B prüfen
- Aufwand, Vertrag und Fehlerfälle gegeneinander abwägen
- Es gibt keinen grundsätzlich besseren Weg

::: notes
Ein Muss ist eine Eigenschaft, ohne die das Ergebnis die Aufgabe verfehlt.
Ein zusätzlicher Client kann ein CLI-Programm oder später eine andere Oberfläche
sein. Die Existenz einer API beweist weder höhere Sicherheit noch bessere
Skalierung. Weg B ist nicht automatisch Microservices. Nenne auch einen Nachteil
deiner bevorzugten Option, bevor du entscheidest.
:::

<!-- slide: B06 -->
# Architektur und Betrieb getrennt entscheiden

- Beide Wege laufen zunächst als Prozesse in der vorhandenen Sandbox
- SQLite liegt im eigenen persistenten Projektbereich
- PostgreSQL und separate App-Container sind spätere Vertiefung
- Keine Engine-Sockets, Privilegien oder verschachtelten Container nötig

::: notes
Im Referenzmaterial bedeutet nativ oft direkt auf dem Entwicklungsrechner.
Hier entwickeln wir innerhalb des vorhandenen Linux-Entwicklungscontainers.
Das ist nicht dasselbe wie eigene App-Images zu bauen. REST erfordert keine
Container; Container erfordern keine REST-API. PostgreSQL ist keine notwendige
Container-Eigenschaft. Ein Volume ist außerdem kein Backup.
:::

<!-- slide: B07 -->
# Deine Entscheidung schriftlich festhalten

- Ziel, Nutzer und Muss-Anforderungen
- Gewählter Weg und abgelehnte Alternative
- Nachteile, Risiken und erwartete Belege
- Ein Anlass für eine spätere Neubewertung

::: notes
Öffne decision.md im gewählten Paket. Fall A: persönliche Browsernotizen ohne
weitere Clients, begrenzte Lernzeit. Fall B: Browser plus zugesagter JSON-Zugriff
für ein anderes Programm. Begründe beide zunächst ohne Code. Ergebnis ist
eine Entscheidung mit Annahmen, keine behauptete Produkt- oder Risiko-Freigabe.
:::

<!-- slide: B08 -->
# Genau ein Praxispaket auswählen

- Weg A: Formular → SQLite-CRUD → Fehler/Bedienung → Abschluss
- Weg B: API-Vertrag → API-SQLite → MVC-Client → Abschluss
- Beide Reihen beginnen bei Pending und brauchen eigenes Review
- Der andere Weg muss nicht vorher bearbeitet werden

::: notes
Pending heißt noch nicht begonnen. Die Serie ist Draft und weder aktiviert
noch abgenommen. ReadyForReview im Authoring-Receipt heißt nur, dass der
Arbeitsauftrag prüfbereit ist. Die Reihenansicht erklärt jede Abhängigkeit
textlich. Keine parallelen Schreibaufträge beider Wege in dasselbe Lernrepo geben.
:::

<!-- slide: B09 -->
# Spec Kit strukturiert den eigenen Auftrag

- Vor Specify Projektprinzipien und Intake prüfen
- Clarify klärt wesentliche Entscheidungen
- Plan, Checklist und Tasks bereiten Umsetzung vor
- Analyze bleibt lesend; Implement braucht ausdrücklichen Auftrag

::: notes
Nutze die vollständigen Prompts des gewählten Intakes. Plane Tests und
Sicherheitsregeln von der ersten Stufe an. Keine Modell-/Providerkonfiguration
oder Git-Delivery aus einem Beispiel ableiten. Der begleitete Weg nutzt einen
Schritt nach dem anderen. Autonomous ist nur eine gesondert genehmigte Alternative.
:::

<!-- slide: B10 -->
# Weg A: vom Formular zum bestätigten Datensatz

- Zuerst nur klar bezeichnete Fixture-Vorschau
- Danach EF Core und eigene SQLite-Datei
- Erfolg erst nach bestätigter Speicherung
- Abbrechen und ungültige Eingaben ändern nichts

::: notes
Ein Eingabeentwurf ist noch kein gespeicherter Datensatz. `SaveChanges` ist
der Schreibpunkt, nicht bereits das Vormerken eines Objekts. Tests verwenden
eine separate DB. Nach einem Neustart müssen die bestätigten Einträge noch
vorliegen. Buildausgaben im Build-Volume sind nicht der Datenbank-Speicherort.
:::

<!-- slide: B11 -->
# Weg B: erst den HTTP-Vertrag verstehen

- GET liest, POST legt an, PUT ersetzt, DELETE löscht
- Erfolg: 200, 201 mit Location oder 204 ohne Inhalt
- Fehler: 400, 404, 413, 429 oder allgemeines 500
- OpenAPI und echte HTTP-Tests müssen übereinstimmen

::: notes
Ein Statuscode ist eine kurze technische Ergebnisangabe. Location zeigt die
Adresse des neu angelegten Datensatzes. DTO heißt Datenübertragungsobjekt;
es begrenzt die Felder des Vertrags statt interne Datenbankobjekte offenzulegen.
Ein erwarteter 400-Fall ist ein bestandener Test, wenn die Ablehnung und der
unveränderte Datenbestand geprüft wurden. Erst danach folgt Persistenz.
:::

<!-- slide: B12 -->
# Weg B: die neue Fehlergrenze ernst nehmen

- API-Ausfall ist keine erfolgreiche leere Liste
- JSON-Syntax allein beweist keinen gültigen Datensatz
- Zehn Sekunden Timeout sind von bewusstem Abbruch zu unterscheiden
- Unklare Schreibantwort nicht automatisch wiederholen

::: notes
Ein Timeout beendet das Warten; die API könnte schon gespeichert haben.
Entwurf erhalten, Liste bewusst neu lesen und dann selbst entscheiden.
Teste den MVC-Client mit falschem Status, ungültiger ID, kaputtem JSON und
Verbindungsfehlern. Verändere oder stoppe keine Instanz einer anderen Person.
:::

<!-- slide: B13 -->
# Schutz ist ab der ersten Stufe erforderlich

- HTTPS und bewusst eingerichtetes Vertrauen
- Serverseitige Validierung, Kodierung und Formularschutz
- Body- und Schreiblimits, sichere Fehler und Logs
- Diese Kontrollen ersetzen keine Benutzerrechte

::: notes
HTML-Kodierung zeigt eingegebenes Markup als Text. Antiforgery schützt
Formularaktionen mit Token und Cookie; CSP begrenzt Browserinhalte.
Keine TLS-Abschaltung, Trust-All-Funktion oder pauschales curl -k verwenden.
Ohne passende Zertifikate stoppt die Ausführung. Lesen und Planen bleiben möglich.
Ports: MVC 5111, API 5112; Bindung im Container 0.0.0.0, Veröffentlichung nur Loopback.
:::

<!-- slide: B14 -->
# Testbelege richtig einordnen

- Unit-Test: eine abgegrenzte Logik prüfen
- HTTP-/Integrationstest: echte Übergänge und SQLite prüfen
- UI-Prüfung: Tastatur, Labels, Fokus und Fehler beobachten
- Coverage je App ist keine vollständige Qualitäts- oder A11Y-Abnahme

::: notes
Bei Weg B mindestens 70 % eigene C#-Zeilenabdeckung je Anwendung, nicht nur
gemeinsam. Bei Weg A dieselbe Grenze für seine eine App. Scope dokumentieren.
Windows, Ubuntu/WSL2 und macOS brauchen eigene Ergebnisse. Alte Referenzberichte
sind keine aktuellen lokalen Tests. Nicht gemessene oder manuell ungeprüfte
Punkte als Open mit Owner, Follow-up und Trigger führen.
:::

<!-- slide: B15 -->
# Einen Fall aus deinem Berufsweg erklären

- Entwicklung: Validierungsregel und Test zuordnen
- Integration/Vernetzung/Elektronik: Prozess- und Portgrenzen erklären
- Datenanalyse: Text vom Formular bis zur Zeile verfolgen
- IT-Management: Nutzen, Aufwand und Übergabe abwägen

::: notes
Ergänze die passende Aufgabe aus dem Werkstättenindex. Basis: einen Eintrag
erstellen und den Datenweg ohne Fachkürzel erklären. Vertiefung: eine ausgefallene
API oder DB als Zustandsfolge beschreiben und geeignete Belege benennen.
Alle sieben beruflichen Perspektiven nutzen dieselben Schutzgrenzen.
:::

<!-- slide: B16 -->
# Von der Präsentation zur Praxis

- Entscheidungsnotiz ausfüllen und genau ein Paket übernehmen
- Ganze Serie prüfen und selbst über den Start entscheiden
- Erste Stufe planen, dann ausdrücklich implementieren lassen
- Nach Abnahme weitergehen, nicht nach einem bloßen grünen Haken

::: notes
Ein späteres Sandbox-Template ersetzt nicht das leere Produktrepo und startet
keine persönliche Intake-Reihe. Das Profil ist noch nicht aktiviert.
Pakete: [MVC](../lernwerkstaetten/web-mvc/README.md) oder
[MVC plus REST](../lernwerkstaetten/web-rest/README.md).
[Übernahme und Spec-Kit-Runde](../lernwerkstaetten/README.md) erklären die Schritte.
Lehrende erhalten getrennte Musterantworten. Dieser Workshop baut oder startet
keine Anwendung und erteilt keine Commit-, Push- oder Public-Release-Befugnis.
:::
