# Web-MVC plus REST: gemeinsamer Produktvertrag / Shared Product Contract

## Deutsch

**Weg B:** C#/.NET, ASP.NET Core MVC und eine getrennte REST-API. API heißt
Application Programming Interface, also Programmierschnittstelle. REST
beschreibt hier den Zugriff auf Ressourcen über HTTP. Der Browser bekommt
HTML von MVC; ein **serverseitiger** HTTP-Client in MVC spricht JSON mit der
API. Nur die API verwendet EF Core und SQLite. Keine SPA und kein direkter
JavaScript-API-Zugriff; keine zusätzliche CORS-Freigabe erforderlich.

1. Neuaufbau aus Hello World, zwei Pflichttexte `text1`, `text2`, serverseitiges
   `id`. Nur eigene lokale Instanz und fiktive Daten. Keine Anmeldung,
   Datensatzrechte, Multiuser- oder Produktivfreigabe. Entscheidung in
   `decision.md` begründen; Weg A ist keine Vorbedingung.
2. Vertrag ab Stufe 0: GET `/api/textentries` 200, GET mit `/{id}` 200/404,
   POST 201 mit Location und Datensatz, PUT/DELETE mit ID 204/404.
   Fehler: 400 ValidationProblemDetails, 413 Body zu groß, 429 mit Retry-After,
   allgemeines 500 mit Kennung. Keine Rohdaten in Fehlern oder Logs.
3. `text1`, `text2`: Pflicht, keine reinen Leerzeichen/NUL, maximal 1000 UTF-16-
   Codeeinheiten vor Trim. API validiert unabhängig von MVC/Browser.
   Ungültige Schreibaktionen ändern nichts. Liste nach ID absteigend.
4. HTTPS, 64-KiB-Bodylimit, 60 Schreibaktionen/60 Sekunden/IP und sichere
   Fehlerbehandlung von Anfang an. Keine automatische Wiederholung von POST,
   PUT oder DELETE bei unbestätigter Antwort. Nicht als Microservices,
   automatisch sicherer oder skalierbarer bezeichnen.
5. Ab Stufe 1 persistente eigene SQLite-Datei nur bei der API. Pfad im
   freigegebenen Projekt-Mount explizit konfigurieren, getrennt von `bin` und
   Build-Volume; kein geteilter Bestand mit Weg A. Transaktion/Fehler darf
   keinen halben Datensatz erzeugen. EnsureCreated ist keine Migration.
6. Ab Stufe 2 eigene MVC-Oberfläche; Antiforgery, HTML-Kodierung, CSP und
   Sicherheitsheader. Server-Client prüft Antwortschema/ID und hat zehn
   Sekunden Timeout ohne automatische Retries. Entwürfe bleiben bei Fehlern
   erhalten; leere Liste, API-Ausfall und unsicherer Schreiberfolg getrennt.
7. Prozesse im vorhandenen Entwicklungscontainer: MVC `0.0.0.0:5111`, API
   `0.0.0.0:5112`; Host-Veröffentlichung nur Loopback. Vertrauenswürdige HTTPS-
   Zertifikate mit passendem Namen und Vertrauen im Client/Browser bewusst
   vorbereiten. Keine TLS-Abschaltung, Trust-All-Callbacks oder curl -k.
   Bei fehlendem Vertrauen stoppen. Keine unaufgeforderte Store-Änderung.
8. Keine App-Container, Engine-Sockets oder PostgreSQL im Basisweg. Keine
   Secrets, Payloads oder Rohsystemdaten an Agenten übergeben. Datenbanken und
   private Schlüssel untracked und geschützt halten.
9. DE zuerst/EN danach, Tastatur, klare Labels und textliche Fehlerzuordnung;
   Client-/API-Zustände vollständig erklären. WCAG 2.2 AA ist Prüfbasis,
   nicht durch Dokumentprüfung bereits abgenommen.
10. Unit-, echte HTTP-Vertrags-, Integrations- und ab Stufe 2 UI-Abnahmefälle.
    Mindestens 70 % eigene C#-Zeilenabdeckung **je App**, keine Verschleierung
    durch Aggregation. Open mit Owner, Follow-up und Trigger; N/A mit Grund.
    Menschliche Abnahme vor Folgestufe; kein öffentliches Deployment.

## English

**Route B:** C#/.NET, MVC and a separate REST API (Application Programming
Interface). The browser receives server-rendered HTML. MVC's server-side HTTP
client exchanges JSON with the API; only the API uses EF Core/SQLite. No SPA,
direct browser API calls or additional CORS permission is needed.

1. Rebuild from Hello World with two texts and a server-generated ID. Personal
   local fictional data only; no authentication, record rights or production
   approval. Record decision.md; route A is not required.
2. GET collection 200; GET ID 200/404; POST 201 with Location/body; PUT/DELETE
   ID 204/404. Validation 400, oversize 413, budget 429/Retry-After, generic
   500 with identifier. No raw data in errors/logs.
3. Both texts required, no whitespace-only/NUL, maximum 1000 UTF-16 units
   before Trim. Validate at the API independently; invalid writes change
   nothing. Sort highest ID first.
4. HTTPS, 64 KiB limit, 60 writes/60 seconds/IP and safe errors from stage 0.
   Never retry uncertain writes automatically. This is not automatically a
   microservice architecture or inherently safer/more scalable.
5. Stage 1 gives the API its own persistent SQLite file at an explicit approved
   mount path, outside bin/build output. No shared route-A data or partial
   rows on failure. EnsureCreated does not manage schema migrations.
6. Stage 2 adds MVC with antiforgery, encoding, CSP and security headers.
   Validate API responses; ten-second client timeout, no retries. Preserve
   drafts and distinguish empty, failed read and uncertain write.
7. Existing sandbox processes: MVC 0.0.0.0:5111, API 0.0.0.0:5112, loopback
   host publishing. Explicitly prepare correctly named trusted HTTPS for
   browser and API client. No trust bypass or unsolicited trust-store changes.
8. No app images, engine sockets or PostgreSQL in this route. Protect untracked
   databases/keys and never send payloads or secrets to agents.
9. Equivalent DE/EN, keyboard access, labels and textual errors; explain every
   state. WCAG 2.2 AA remains a review basis, not a completed acceptance.
10. Unit, real HTTP contract, integration and later UI evidence. At least 70 %
    own C# line coverage per app, not only aggregated. Open needs owner,
    follow-up and trigger. Human acceptance before progression; no public service.
