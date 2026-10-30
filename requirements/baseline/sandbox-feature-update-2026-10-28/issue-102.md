# Issue #102: OpenCode-Webinterface beim Containerstart mit Passwort, Healthcheck und gemeinsamer TUI bereitstellen

Source: https://github.com/hindermath/absdd-image-sandbox/issues/102
Retrieved through GitHub connector: 2026-10-28
Issue updatedAt: 2026-10-27T22:53:00Z
Proof boundary: immutable local requirements snapshot; no upstream implementation acceptance.

## Deutsch

### Gemeinsamer nächster Feature-Update-Block

Dieses Issue gehört zusammen mit den folgenden Issues zum **nächsten Feature-Update-Block dieses Repositories**:

- [#101 – Ubuntu 26.04 und Basisimage](https://github.com/hindermath/absdd-image-sandbox/issues/101)
- [#102 – OpenCode-Webinterface](https://github.com/hindermath/absdd-image-sandbox/issues/102)
- [#104 – MSL-Sprachauswahl](https://github.com/hindermath/absdd-image-sandbox/issues/104)

Gemeinsames Ziel: Ubuntu-26.04-Basis, OpenCode-Webbetrieb und wählbare MSL-Profile als zusammenhängendes Sandbox-Update bereitstellen. #101 bildet die technische Basis; #102 und #104 werden darauf abgestimmt. Die Umsetzung kann in getrennten Änderungen erfolgen. Vor Abschluss des Blocks die Kombination auf den finalen Images einschließlich Profil-, Web-, Audit- und Plattformprüfungen validieren. Der Block ist erst abgeschlossen, wenn alle drei Issues ihre Abnahmekriterien erfüllen.

### Aktualisierung nach MR !74/!76

Stand 2026-10-27: Webbetrieb ist in der Quelle umgesetzt und in den profilfähigen Oktober-Kandidaten `4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30` integriert. [MR !74](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/merge_requests/74) ergänzt eine wichtige Webtest-Korrektur: Ein frühes HTTP 401 beweist nur die Authentifizierungsschranke, noch keine erfolgreiche authentifizierte Startbereitschaft. Der anschließende authentifizierte Zugriff kann vorübergehend HTTP 503 liefern. Der Test wartet dafür mit einer festen Frist von 45 Sekunden; Healthcheck und ausführbare Python-Datei werden ebenfalls berücksichtigt (LF-Zeilenenden).

- [ ] Aktuelle Version von `scripts/test-opencode-local-web.py` übernehmen: begrenzte Bereitschaftsprüfung für temporäre HTTP-503-/Verbindungsfehler, andere HTTP-Fehler sofort sichtbar lassen. Dauerhaftes 503 muss fehlschlagen; Auth-401 nicht mit Readiness verwechseln. Healthcheck-Ausführung inklusive LF unter Windows-Checkouts testen.
- [ ] OpenCode-Webserver, Healthcheck und benötigte Infrastruktur im gemeinsamen Image-Kern aller sieben MSL-Profile (#104) belassen. Reale Compose-/Auth-/Audit-Tests mindestens mit `dotnet` und `all`, gemeinsame Build-Gates in allen Profilen prüfen.
- [ ] Zielversion 2.1.4 weiter beibehalten und tatsächliche CLI-Semantik prüfen; Quellversion 2.1.3 ist kein Downgrade-Auftrag.

[ARM64-Quellbericht](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/docs/security/mr74-macos-arm64-acceptance-2026-10-27.md): alle sieben Profile nativ geprüft; praktische Compose-/HTTP-/Audit-Prüfung für `dotnet` und `all`. Der Bericht bindet den dort genannten Testcommit, nicht automatisch den späteren Kandidaten-Head. [AMD64-Protokoll](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/docs/security/agent-session-log/2026-10-27-1033.md): Direktbuilds bestanden, praktischer Windows-Compose-Build in dieser Session durch Provider-/Named-Pipe-Problem blockiert. Diese Grenze erhalten, nicht als vollständigen Windows-Compose-Pass darstellen.

### Ziel und geprüfter Ausgangspunkt

OpenCode beim Containerstart als lokalen, passwortgeschützten Webserver anbieten. Browser, Terminaloberfläche (TUI) und nicht-interaktive CLI sollen denselben Server verwenden können.

Quelle: [MR !71](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/merge_requests/71), Implementierung [e60c68a](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/commit/e60c68a77349b0662f9c5544f8e3f693061c3eb4), geprüft am 2026-10-27 im Aktualisierungsbranch `chore/refresh-sandbox-image-2026-10` bei `4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30`. Dort implementiert; der übergeordnete MR !64 bleibt offen/Draft. Quell-`main` enthält die Testanleitung, noch nicht die Implementierung.

[Web-Wrapper](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/scripts/opencode-web.sh), [TUI-Wrapper](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/scripts/opencode-tui.sh), [Healthcheck](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/scripts/healthcheck-opencode-web.py), [Tests](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/scripts/test-opencode-local-web.py).

Hier besteht bereits eine Loopback-Portfreigabe `5100-5199`; der Container wird bisher durch eine Warteschleife am Leben gehalten. Dieses Repo pinnt OpenCode **2.1.4**, die Quelle **2.1.3**. Befehle und Authentifizierung gegen die tatsächlich gepinnte Zielversion prüfen; kein Downgrade. Das Vorbild verwendet `serve`, `mini --server` und `run --server`.

### Arbeitspakete

- [ ] Web- und TUI-Wrapper passend zur Zielversion übernehmen. Im Container an `0.0.0.0:5199` lauschen, am Host ausschließlich über `127.0.0.1:5199` erreichbar; kein Pairing, mDNS, Remote-Tunnel oder zusätzliches CORS ohne eigenen Auftrag.
- [ ] Webserver als Vordergrundprozess statt Warteschleife starten; vorhandenen `ade-entrypoint`, Signalweitergabe und Audit-Export beim Stoppen erhalten. Fehler bei fehlendem Passwort einschließlich möglicher Restart-Schleife verständlich dokumentieren.
- [ ] `OPENCODE_PASSWORD` in ignorierter `opencode.env` dokumentieren: mindestens 16 Zeichen, leere Werte und bekannte Platzhalter ablehnen. Tatsächliche Auth-Variable der Zielversion verifizieren. Keine Passwörter in Prozessargumenten, URLs, Logs, Testausgaben oder getrackten Dateien.
- [ ] Authentifizierten, stillen Healthcheck und Compose-Readiness ergänzen. Browser-Anmeldung mit Benutzer `opencode`, Startfehler, Portkonflikt und Wiederanlauf dokumentieren.
- [ ] Port 5199 reservieren; Anwendungsbeispiele auf `5100-5198` begrenzen. Bestehende Beispiele und Tests mit 5199 systematisch prüfen. Konflikte mit parallel laufenden Sandbox-Stacks erklären.
- [ ] TUI aus dem jeweiligen Projektverzeichnis und nicht-interaktive CLI an den lokalen Server anbinden. Gemeinsame Sitzungen erklären; parallele Prompts in derselben Sitzung vermeiden, getrennte Sitzungen/Forks verwenden. Standalone-Verhalten und vorhandenen Agent-Prompt-Dispatcher auf Verträglichkeit prüfen.
- [ ] Bestehende Leserpfade in `docs/fuer-lernende/` und `docs/betrieb/`, README, `opencode.env.example`, AGENTS und Sicherheits-/Netzwerkdokumentation konsistent pflegen. Keine zweite Lernreihe schaffen. Befehle mit Host/Container, Shell, Voraussetzungen, Ergebnis und Fehlerhilfe erklären; Deutsch zuerst und gleichwertiges Englisch.

### Abnahme für die spätere Umsetzung

- [ ] Zielversion belegt: fehlendes, kurzes und Platzhalter-Passwort werden abgelehnt; unbelegte Ports werden erkannt; Start funktioniert mit synthetischem Testpasswort.
- [ ] Geschützter HTTP-Endpunkt liefert ohne/falsche Anmeldung 401 und mit korrekter Anmeldung 200. Healthcheck ist bei Fehlern rot und gibt keine Secrets aus. Weboberfläche im Hostbrowser tatsächlich öffnen und Anmeldung prüfen.
- [ ] TUI und CLI erreichen denselben Server aus einem Testprojekt; Tests benötigen weder echte API-Keys noch Modellaufrufe. Projekt-/Sitzungszuordnung und keine Secret-Leaks prüfen.
- [ ] Serverneustart erhält persistente Daten; Stop über den vorhandenen Audit-Wrapper exportiert weiter ausschließlich erlaubte Metadaten und bewahrt Volumes. OpenCode-2-Datenbankmetadaten bleiben `session_coverage=not-exported`; keine Inhalte exportieren.
- [ ] Non-root, Capability-Drop, no-new-privileges und bestehende Agent-Policies bleiben erhalten. Compose, relevante Regressionen, Pre-Commit, Secret-Scan und `git diff --check` bestehen; Neubau und finale SBOM bei Image-Delivery.
- [ ] Native macOS-/ARM64-, Windows-/AMD64- und Ubuntu/WSL2-Prüfungen getrennt mit Datum, Git-Head, Image-ID, Befehlen und Exitcodes dokumentieren; fehlende Nachweise offen lassen.
- [ ] Tastaturbedienung, Fokusführung, Anmeldung und Fehlermeldungen anhand der anwendbaren WCAG-2.2-AA-Kriterien prüfen; automatische HTTP-/Markdown-Checks sind keine A11Y-Abnahme.

Bezug: P1-1, P1-5, P3-2, P3-4. Für ein kombiniertes Release zuerst #101 integrieren, danach den Webbetrieb auf dem finalen Image erneut prüfen. Das Webfeature kann separat entwickelt werden. Keine formelle Betriebsfreigabe oder Fortsetzung eines bestehenden Spec-Kit-Laufs durch dieses Issue.

## English

### Shared next feature update block

This issue and the following issues form the **next feature update block for this repository**:

- [#101 – Ubuntu 26.04 and base image](https://github.com/hindermath/absdd-image-sandbox/issues/101)
- [#102 – OpenCode web interface](https://github.com/hindermath/absdd-image-sandbox/issues/102)
- [#104 – MSL language selection](https://github.com/hindermath/absdd-image-sandbox/issues/104)

Shared goal: deliver the Ubuntu 26.04 base, OpenCode web operation and selectable MSL profiles as one coordinated sandbox update. #101 provides the technical foundation; align #102 and #104 with it. Implementation may use separate changes. Before closing the block, validate the combined final images with profile, web, audit and platform checks. The block is complete only when all three issues meet their acceptance criteria.

### Refresh after MR !74/!76

As of 2026-10-27 the web implementation is integrated into profile-capable candidate `4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30`. MR !74 corrects startup testing: early HTTP 401 proves the authentication gate, not authenticated readiness. Authenticated requests may temporarily return 503; the source uses a bounded 45-second wait and normalizes the executable Python healthcheck to LF.

- [ ] Adopt the current web test with bounded retries for temporary HTTP 503/connection errors; surface other HTTP errors, fail persistent 503 and distinguish authentication from readiness. Test executable healthcheck LF handling on Windows checkouts.
- [ ] Keep server/healthcheck infrastructure in the common core for all seven profiles (#104). Run practical Compose/auth/audit checks at least for dotnet and all, plus common build gates across every profile.
- [ ] Preserve target OpenCode 2.1.4 and verify its CLI semantics; source 2.1.3 is no downgrade instruction.

The linked ARM64 report records all seven native profile tests and actual dotnet/all Compose, HTTP and audit checks at its stated earlier test revision. The AMD64 log records direct builds but a Windows Compose build blocked by provider/named-pipe configuration in that session. Preserve these limits; do not claim complete Windows Compose or target-repository acceptance.

### Goal and evidence

Start a local password-protected OpenCode web server with the container and let the browser, TUI and non-interactive CLI share it. The exact source links above belong to MR !71, merged into the refresh branch at `4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30`, with parent MR !64 still open/Draft, verified on 2026-10-27. Source main contains test guidance rather than this implementation. This repository pins 2.1.4; the source uses 2.1.3. Verify commands and authentication against the target version without downgrading.

### Work and acceptance

- [ ] Adapt web/TUI wrappers; listen on container `0.0.0.0:5199` and publish only to host `127.0.0.1:5199`. Keep pairing, mDNS, tunnels and extra CORS disabled.
- [ ] Replace the idle command with the foreground server while preserving the entrypoint, signal forwarding and metadata audit on shutdown. Explain missing-password failures and restart loops.
- [ ] Document `OPENCODE_PASSWORD` in ignored local configuration; require at least 16 characters and reject empty/placeholder values. Verify the actual target-version auth variable; never expose passwords through arguments, URLs, logs, test output or tracked files.
- [ ] Add a silent authenticated healthcheck and readiness; document browser login as `opencode`, startup errors, port conflicts and restart.
- [ ] Reserve 5199 and migrate application examples to `5100-5198`; check examples/tests and explain conflicts with concurrent sandbox stacks.
- [ ] Connect TUI and CLI from the intended project directory to the shared server. Explain shared sessions, separate sessions/forks for concurrent prompts, standalone operation and dispatcher compatibility.
- [ ] Update existing learner/operations paths, README, example environment, AGENTS and security/network documents in equivalent German and English. Explain command location, shell, prerequisites, expected results and troubleshooting; create no second learning source.
- [ ] Test missing/short/placeholder password rejection, port conflicts and successful startup using synthetic credentials. Protected endpoints must return 401 without valid authentication and 200 with it; failed healthchecks stay unhealthy and silent. Actually open the browser interface and verify login.
- [ ] Verify TUI/CLI connectivity, project/session mapping and no secret leaks without real API keys or inference.
- [ ] Preserve data through restart and metadata-only export through the normal audit stop wrapper, without volume deletion. Keep `session_coverage=not-exported`; do not export database contents.
- [ ] Preserve non-root operation, capability drops, no-new-privileges and agent policies. Pass Compose validation, relevant regressions, Pre-Commit, secret scan and diff checks; rebuild and generate a final SBOM before image delivery.
- [ ] Record separate native macOS/ARM64, Windows/AMD64 and Ubuntu/WSL2 evidence with date, Git revision, image ID, commands and exit codes; leave missing coverage open.
- [ ] Review keyboard access, focus, login and errors against applicable WCAG 2.2 AA criteria; HTTP/Markdown tests do not establish accessibility acceptance.

Plan references: P1-1, P1-5, P3-2, P3-4. For a combined release, integrate #101 first and repeat web validation on the final image. Separate development is possible. This issue grants neither formal operation approval nor resumption of an existing Spec Kit run.

