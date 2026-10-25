# Web-MVC: gemeinsamer Produktvertrag / Shared Product Contract

## Deutsch

**Weg A:** C#/.NET mit ASP.NET Core MVC und Razor. MVC trennt Modell, Anzeige
und Steuerung; Razor erzeugt HTML auf dem Server. EF Core ist die Bibliothek
für Datenzugriff, SQLite die eingebettete Datenbank. Ein App-Prozess; **keine
fachliche REST-API**. Vor der Praxis die Entscheidung aus `decision.md`
begründen. Der andere Web-Pfad ist keine Vorbedingung.

1. Neuaufbau aus Hello World. Zwei Pflichttexte `text1`, `text2`, ein
   serverseitig vergebenes `id`; keine Anmeldung und keine Datensatzrechte.
   Nur eigene lokale Instanz mit fiktiven Daten, kein öffentlicher Dienst.
2. CRUD bedeutet Anlegen, Lesen, Ändern, Löschen. Ab Stufe 1 alle vier
   Vorgänge mit SQLite, höchste ID zuerst. Daten bleiben bei App-Neustart
   erhalten. Keine automatische Übernahme aus Referenz- oder Nachbarprojekten.
3. Beide Texte: nicht leer/Whitespace, höchstens 1000 UTF-16-Codeeinheiten vor
   Trim, keine NUL-Zeichen. Serverseitig unabhängig vom Browser prüfen.
   Abgelehnte Änderungen verändern nichts; Eingabeentwurf bleibt sichtbar.
4. HTTPS, Antiforgery für Änderungen, HTML-Kodierung, Sicherheitsheader/CSP,
   Größenlimit 64 KiB, Schreiblimit 60 je 60 Sekunden je Client-IP von Beginn
   an einplanen. 413 bei zu großem Body, 429 mit Retry-After bei verbrauchtem
   Budget. IP ist keine Identität. GET verbraucht kein Schreibbudget.
5. Allgemeine Fehler mit Kennung, ohne Rohdaten, Stacktrace oder Secrets in
   Antworten. Fehlerlogs ohne Request-/Antwortkörper, Cookies oder Tokens.
   Leere Liste, Lesefehler und unklarer Schreiberfolg sind getrennte Zustände.
   Kein automatisches Wiederholen unbestätigter Schreibaktionen.
6. Pro Person eigene Instanz. Im bestehenden Entwicklungscontainer an
   `0.0.0.0:5111` binden; Host-Veröffentlichung bleibt Loopback. HTTPS-Zertifikat
   und Browser-Vertrauen vorher bewusst einrichten, Schlüssel untracked halten.
   Keine TLS-Abschaltung, Browser-Warnungsumgehung oder pauschales curl -k.
   Nicht verfügbare Zertifikate blockieren die Praxis, nicht das Lesen.
7. Kein eigenes App-Container-Image, Engine-Socket oder PostgreSQL für den
   Basisweg. PostgreSQL/Compose sind eine getrennte spätere Vertiefung.
8. Eigenes Projekt unter einem freigegebenen Projekt-Mount. SQLite-Datenpfad
   explizit in diesen persistenten Arbeitsbereich legen; C#-Buildausgaben
   folgen dem Sandbox-Wrapper in den Build-Volume. Keine Datenbank in `bin`.
9. DE zuerst/EN danach, klare Feldbeschriftungen, textuelle Fehlerzuordnung,
   Tastaturbedienung und Fokus nach Fehlern/Löschdialog prüfen. Eine Checkliste
   oder hohe Coverage beweist keine WCAG-2.2-AA-Konformität.
10. Jede Stufe liefert positive/negative Tests und Abnahmebelege; ab messbarem
    Produktcode mindestens 70 % eigene C#-Zeilenabdeckung, Scope offenlegen.
    Offene Nachweise mit Owner, Follow-up und Trigger, N/A mit Grund.
    Vor nächster Stufe menschliche Abnahme; kein öffentliches Deployment.

## English

**Route A:** C#/.NET, ASP.NET Core MVC and server-rendered Razor HTML. EF Core
provides data access; SQLite is embedded. One app process, no business REST
API. Record the decision in decision.md first; route B is not a prerequisite.

1. Build from Hello World: two required texts and a server-generated ID. No
   authentication/record permissions; personal local fictional-data use only.
2. CRUD means create, read, update, delete. Stage 1 persists all four with
   SQLite, highest ID first; restart preserves data. Never import other data.
3. Reject empty/whitespace, NUL or more than 1000 UTF-16 units before trimming.
   Validate server-side. Rejections change nothing and preserve drafts.
4. Plan HTTPS, antiforgery, HTML encoding, CSP/security headers, 64 KiB body
   limit and 60 writes/60 seconds/IP from the outset. Oversize gives 413;
   exhausted budget gives 429/Retry-After. GET remains outside write budget.
5. Generic errors with identifiers, no internal details or raw data. Logs
   exclude payloads and credentials. Distinguish empty, failed read and
   unconfirmed write. Never automatically retry an uncertain write.
6. Inside the development container bind to 0.0.0.0:5111; host publishing stays
   loopback. Explicitly prepare trusted HTTPS and protect untracked private
   keys. No bypass flags; missing certificates block execution, not reading.
7. No separate app image, engine socket or PostgreSQL is needed for this route.
8. Use an approved project mount and explicit persistent SQLite path, separate
   from redirected build output. Never store the database under bin.
9. German-first/equivalent English, field labels, textual error links, keyboard
   access and focus handling. Static checks or coverage do not establish WCAG.
10. Positive/negative evidence per stage, at least 70 % own C# line coverage
    when measurable; record scope. Open needs owner/follow-up/trigger; N/A a
    reason. Human acceptance before progression; no public deployment.
