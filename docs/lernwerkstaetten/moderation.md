# Moderation und Musterantworten / Instructor Notes and Example Answers

**DE:** Separat von den Arbeitsaufträgen verwenden. Erst eigene Vorhersage
und Begründung einsammeln, dann vergleichen. Die Antworten sind Orientierung,
keine bereits ausgeführte Abnahme. Für Erstjährige Begriffe am konkreten
Beispiel erklären; Entwickler vertiefen dieselben Fälle, ohne Schutz zu umgehen.

**EN:** Collect personal predictions before sharing answers. These are teaching
examples, not acceptance evidence. Explain terms through concrete first-year
examples; experienced developers deepen the same cases without bypassing controls.

## SysInfo

| Stufe / Stage | Erwartete Erklärung DE / Expected Explanation EN |
|---|---|
| SYS-00 | Ein zählender/fehlschlagender Collector-Testdouble bleibt bei Help/Version unaufgerufen; keine Live-Abfrage. / A counting/failing test double proves help/version never call collection. |
| SYS-01 | Syntaktisch gültiges YAML kann Werte verlieren oder Typen ändern; gegen dasselbe normalisierte Modell vergleichen. / Valid syntax may still lose/change values; compare the shared model. |
| SYS-02 | Fehler nach der ersten Teiloperation erzwingen, Transaktion zurückrollen und vollständige Snapshots zählen. / Inject a mid-write failure, roll back and count complete snapshots. |
| SYS-03 | GET liest gespeicherten Zustand; neuer Collector-Aufruf wäre zusätzliche Datenverarbeitung und verletzte das Opt-in. / GET reads stored state; collection would add processing outside consent. |
| SYS-04 | Generatorinput, Quellenstand, Befehl, Exitcode und neuer Output müssen zusammenpassen; alte Datei allein reicht nicht. / Bind source, command, exit and fresh output; stale files alone prove nothing. |
| SYS-05 | Übernahme bindet eine Quelle; Prüfung liefert begrenzte Evidenz; Risikoakzeptanz ist eine gesonderte menschliche Entscheidung. / Adoption binds a source; verification gives bounded evidence; risk acceptance is human. |

**DE:** Sensible Opt-ins zuerst mit Fixtures prüfen. Reale Prozessnamen können
private Tätigkeiten verraten; Exporte nicht projizieren oder in Agentenprompts
kopieren. Unverfügbare Werte sind ein zulässiger Lernfall, kein Grund für Root.
Die Referenz wird bewusst nicht funktional bytegleich nachgebaut: Standard-
Fixtures, Opt-in, sicherer Dateikonflikt und Containergrenze sind Anpassungen.

**EN:** Test sensitive opt-ins with fixtures first. Process names may reveal
private work; never project/export them unreviewed. Unavailable data is a
valid learning case, not a reason for root. Fixture defaults, consent, safe
file conflicts and container boundaries intentionally adapt reference behavior.

## Web-Entscheidung / Web Decision

**DE:** Fall A (persönliche Browsernotizen, keine weiteren Clients): Weg A
ist wegen einer App und weniger Fehlergrenzen naheliegend. Nachteile:
kein vereinbarter JSON-Vertrag, gemeinsame Ausgabe von Oberfläche und Datenzugriff.
Fall B (Browser plus zugesagter programmatischer Client): Weg B bietet den
expliziten Vertrag; Mehrkosten sind Konfiguration, Vertrauensbeziehungen,
Versionierung und Verbindungs-/Timeoutfehler. Andere Entscheidungen brauchen
eine nachvollziehbare Muss-Anforderung, nicht die größere Projektnummer.

**EN:** Personal browser-only notes favour route A's one app and fewer failure
boundaries, at the cost of no agreed JSON interface and one deployment unit.
A promised programmatic client favours route B's explicit contract, with extra
configuration, trust, versioning and failure handling. Different choices need
requirements, not preference for a larger project number.

| Stufe / Stage | Erwartete Erklärung DE / Expected Explanation EN |
|---|---|
| MVC-00 | Razor läuft serverseitig, der Browser erhält HTML/CSS/JavaScript. / Razor runs server-side; the browser receives HTML/CSS/JavaScript. |
| MVC-01 | Add merkt vor; erst bestätigtes SaveChanges schreibt. / Add tracks intent; confirmed SaveChanges persists. |
| MVC-02 | Leere Liste ist erfolgreicher Lesezustand; DB-Ausfall ist eigener Fehler mit erhaltenem Entwurf. / Empty is successful read; DB outage is distinct and preserves drafts. |
| MVC-03 | Erst ein zusätzlicher vereinbarter Client-/JSON-Bedarf begründet erneute Architekturprüfung, nicht jeder UI-Wunsch. / Agreed additional client/JSON needs justify reassessment, not every UI change. |
| REST-00 | HTTP-Vertrag ist mit unabhängigem Client prüfbar; Browser-UI ist kein API-Testwerkzeug-Zwang. / Independent HTTP clients can verify the contract before UI exists. |
| REST-01 | Neustart trennt RAM-Erfolg von dauerhafter Speicherung derselben Werte/IDs. / Restart distinguishes in-memory success from persistence. |
| REST-02 | FE kann Razor und serverseitigen API-Client umfassen; nur JavaScript als FE zu betrachten verfehlt diese Teamgrenze. / Frontend responsibility includes Razor and server API client here. |
| REST-03 | API-Vertrag ermöglicht weitere Clients, verlangt aber Kompatibilität und eigene Fehlerbehandlung. / Contract enables clients but requires compatibility and failure handling. |

## Auswertung und Grenzen / Assessment and Boundaries

**DE:** Als zusätzliche Verständnisfrage Fork, Template und Produktstarter
vergleichen lassen. Erwartung: Fork für Pflege/Beiträge, Template später
optional für eigene Sandbox mit unabhängiger Historie, leeres Produktrepo für
genau ein Praxispaket. Keine kopierten Abnahmen oder automatischen Updates.
Das Template-Profil ist vorbereitet, nicht aktiviert; Rechteklärung bleibt Gate.

**EN:** Ask learners to distinguish fork, template and product starter:
fork for maintenance/contribution, later optional independent sandbox template,
empty product repo for one practice package. No inherited approval or automatic
updates. Template use is prepared, not enabled; rights review remains a gate.

**DE:** Pro Station ein Erfolgsfall, ein Negativfall und ein begründetes
offenes Thema besprechen. Für eine erfolgreiche Lernkontrolle muss die Person
den Datenweg, den Schreibpunkt und die Aussagegrenze des Tests erklären.
Ein Agentenprotokoll allein ist keine Eigenleistungserklärung oder menschliche
Abnahme. Bei unbekannten Secrets, fehlendem Vertrauen oder unklaren Rechten
stoppen und zuständige Person fragen. Technische/human-only Punkte getrennt halten.

**EN:** Discuss one success, one negative case and one reasoned open issue per
station. Learners should explain data flow, write point and test limitations.
An agent transcript alone proves neither understanding nor human acceptance.
Stop on secrets, missing trust or unclear permissions and ask the responsible
person. Separate technical evidence from human-only decisions.
