# Begrenzter Safari-A11Y-Durchlauf / Limited Safari accessibility review

## Prüfstand / Review context

DE: Datum 2026-11-09, Mac mit macOS 27.2 (Darwin 27.2.0), ARM64;
Safari 27.2. Repository-Stand:
`dfbe883946e93d727b6fe463b8e0588551eb78f3`.
Auftrag: Safari, Tastatur, VoiceOver und Zoom für OpenCode Web und den
bestehenden Lernendenpfad prüfen und dokumentieren; keine Implementierung.
Braille bleibt ausdrücklich ungeprüft. Status: **Teilprüfung; technische
Blockaden im ersten Durchlauf, keine vollständige A11Y-/WCAG-Abnahme**.
Der weiter unten dokumentierte Folgeversuch hebt die ursprüngliche
Runtime-Blockade auf; die ursprünglichen Beobachtungen bleiben historisch.

EN: Reviewed on 2026-11-09 on an ARM64 Mac running macOS 27.2 and Safari 27.2,
at the repository revision above. Scope: Safari, keyboard, VoiceOver and zoom
for OpenCode Web and the existing learner journey, with documentation only.
Braille remains untested. Status: **partial review with technical blockers;
no complete accessibility or WCAG acceptance**. The follow-up below resolves
the initial runtime blocker without rewriting the historical observations.

## Tatsächlich beobachtet / Observed evidence

| ID | Gegenstand / Subject | Beobachtung / Observation | Ergebnis / Result |
|---|---|---|---|
| M-01 | Gerenderter Einstieg / Rendered learner entry | README und lernwege.md in der öffentlichen GitHub-Vorschau am festen Commit geöffnet; keine GitHub-Anmeldung erforderlich. / Opened both pages in public GitHub preview at the fixed commit, without signing in. | Pass für diese Ansichten / Pass for these views |
| M-02 | Semantische Struktur / Semantic structure | Safari-Accessibility-Baum enthält Dokumentüberschriften, benannte Inhaltslinks sowie Tabellen mit Zeilen und Zellen. Das allein belegt keine korrekte Ansage aller Beziehungen. / Safari exposes document headings, named content links and table rows/cells; this alone does not prove correct spoken relationships. | Teilnachweis / Partial evidence |
| M-03 | Tastaturnavigation / Keyboard navigation | Nach Positionierung am Abschnitt „Neu hier?“ mit Option-Tab: Abschnitts-Permalink → Fork-/Template-Vergleich → Lizenz/Herkunft → Lernweg. Return öffnete lernwege.md am selben Commit. Einfaches Tab lief zunächst durch GitHub-Menütasten. / After positioning at the section, Option-Tab traversed the listed links; Return opened the learning path at the same commit. Plain Tab initially traversed GitHub menu buttons. | Pass für diese Folge; keine vollständige Tastaturreise / Pass for this sequence, not a complete keyboard journey |
| M-04 | Sichtbarer Fokus / Visible focus | Ein sichtbarer Fokusrahmen um GitHubs „Products“-Taste wurde im Safari-Screenshot beobachtet; weitere Fokusziele per AX-Zustand nachgewiesen. / Observed a visible focus outline on GitHub's Products button; further focus targets were recorded through AX state. | Teilnachweis; nicht alle Inhaltslinks visuell geprüft / Partial, not every content link visually checked |
| M-05 | VoiceOver | Systemeinstellungen zeigten zunächst „off“, nach temporärer Aktivierung „on“. Owner bestätigte auf Nachfrage: „Ja, Ausgabe hörbar und verständlich“. / Settings initially showed off, then on after temporary activation. The owner confirmed audible, understandable output. | Menschliche Teilbeobachtung / Human partial observation |
| M-06 | VoiceOver-Grenzen / VoiceOver limits | Separate VoiceOver-App-Abfrage endete im Timeout; Rotor-/Cursorwechsel und konkrete Ansagen von Tabellenbeziehungen, Fehlern und DE-/EN-Sprachwechsel wurden nicht zuverlässig erfasst. / Separate VoiceOver app inspection timed out; rotor/cursor transitions and exact announcements for tables, errors and language changes were not reliably captured. | Open; nicht als bestanden gezählt / Open, not counted as passed |
| M-07 | 200-%-Zoom / 200% page zoom | Im Safari-Seitenmenü 200 % ausdrücklich ausgewählt und als 200 % bestätigt. Auf lernwege.md blieben die betrachteten Überschriften, DE-/EN-Absätze und die erste Lernweg-Tabelle lesbar; Tabelle mit umgebrochenen Textzellen sichtbar. / Explicitly selected and verified 200%; sampled headings, bilingual paragraphs and the first learning-path table remained readable, with wrapped cell text. | Pass für die betrachteten Ausschnitte / Pass for sampled portions |
| M-08 | Weitere Layoutgrenzen / Further layout limits | Keine 320-CSS-Pixel-/400-%-Reflow-Abnahme; keine vollständige Prüfung langer Codeblöcke oder aller Tabellen. GitHubs fixierter Dateikopf überlagert beim Scrollen den oberen Ausschnitt; ein vollständig verdeckter Tastaturfokus wurde nicht nachgewiesen. / No full narrow-width/400% reflow, long-code or all-table review; GitHub's sticky header covers the top scroll region, without evidence of fully obscured keyboard focus. | Open |
| M-09 | Installation und erste Schritte / Installation and first steps | Nach manueller Entsperrung beide Seiten am gleichen Commit betrachtet. Bei 200 % blieb der betrachtete Einführungstext lesbar; ein umgebrochener erste-schritte.md-Link hatte einen sichtbaren blauen Fokusrahmen und ließ sich mit Return öffnen. Der Bash-Stopp-Befehl war vollständig sichtbar. Anleitungsbefehle wurden nicht ausgeführt. / After unlock, reviewed both pages at the same commit; sampled introduction text remained readable at 200%, a wrapped first-steps link had a visible blue focus outline and opened with Return. The Bash shutdown command was fully visible; guide commands were not executed. | Pass für Ausschnitte und Linkaktivierung / Pass for samples and link activation |
| M-10 | Fehlerhilfe / Troubleshooting | Fehlerhilfe aus erste-schritte.md geöffnet; Überschriften und Symptom/Ursache/Lösung als Text im AX-Baum vorhanden. Bei 200 % war der betrachtete Machine-Startfehler mit erklärendem Text lesbar. Keine Live-Fehlerdialogabnahme von OpenCode. / Opened troubleshooting from first steps; headings and symptom/cause/solution exposed as text. Sampled machine-start guidance was readable at 200%; no live OpenCode error-dialog acceptance. | Teilnachweis / Partial evidence |
| M-11 | Browserinstabilität / Browser instability | Safari zeigte ab der Installationsseite den Banner „Diese Webseite wurde neu geladen, weil ein Problem aufgetreten ist.“ Dieser blieb bei weiterer Navigation sichtbar. Ursache nicht untersucht; kein reproduzierbarer Repository- oder WCAG-Fehler daraus abgeleitet. / Safari displayed a page-reload problem banner from installation onward; it persisted during navigation. Cause not investigated; no reproducible repository or WCAG defect inferred. | Beobachtung, Ursache offen / Observation, cause open |
| M-12 | Rücksetzung / Restoration | Safari-Seitenmenü zeigte nach Rücksetzung 100 %. Systemeinstellungen zeigten nach Rücksetzung VoiceOver off. / Safari page menu confirmed restored 100% zoom; settings confirmed VoiceOver off. | Pass |

DE: Bedienungs-Setup und Zoom-Menü wurden teilweise mit AX-Klicks bedient.
Nur die ausdrücklich genannte Linkfolge ist als Tastaturfolge nachgewiesen.
Die hörbare VoiceOver-Ausgabe ist eine Ownerbeobachtung, keine vom Agenten
aufgezeichnete oder gehörte Audioanalyse. Es wurden keine Audiodaten erfasst.

EN: Setup and zoom-menu interaction partly used AX clicks. Only the stated
link sequence is established as keyboard navigation. Audible VoiceOver output
is owner-reported, not agent-recorded or agent-heard audio evidence. No audio
data was captured.

## OpenCode Web: erster Versuch blockiert / Initial attempt blocked

DE: Die vorhandene Podman-VM war anfangs gestoppt, der bestehende Container
`absdd-image-sandbox_ade_1` beendet (Exit 0). Vorhandene Image-ID:
`5f530d888485537c160bddf9330f56844d99e98518d97e2d842bb27a76a1391d`.
Der erste VM-Start meldete Erfolg; der aus der Machine-Metadatenabfrage
ermittelte API-Socket verweigerte anschließend die Verbindung. Ein gezielter
zweiter Startversuch scheiterte am `gvproxy`-Socket. Danach wurde die VM
wieder als gestoppt gelesen. Kein Containerstart gelang.

EN: The existing VM and container were initially stopped. The first VM start
reported success, but the machine-derived API socket subsequently refused
connections. One targeted retry failed at the gvproxy socket. The VM was
then observed stopped again; no container start succeeded.

DE: Deshalb keine aktuelle Browser-Anmeldung, Web-Tastaturfolge, VoiceOver-
Fehleransage oder Zoomprüfung von OpenCode durchgeführt. Die tatsächliche
Container-OpenCode-Version konnte nicht abgefragt werden. Das Repository
enthält inzwischen den Pin 2.2.6 aus PR #129, ausdrücklich ohne lokale
Runtime-Aktivierung; weder diese Version noch der frühere 2.1.4-Prüfstand
werden durch diesen Durchlauf als getestet behauptet. Keine neue Image-
Installation, kein Build, keine Konfigurationsreparatur und keine Inferenz.

EN: No current OpenCode browser login, keyboard sequence, VoiceOver error
announcement or zoom review was performed. The container's actual OpenCode
version could not be queried. Repository pin 2.2.6 arrived through PR #129
without local runtime activation; neither that version nor historical 2.1.4
evidence is claimed tested here. No new image, build, configuration repair or
inference was performed.

## Abschluss des ersten Durchlaufs / Initial review closeout

DE: Beim Wechsel zur Installationsanleitung verlor die UI-Steuerung das
Safari-Fenster. Die anschließende Bestandsabfrage meldete: Mac gesperrt,
automatische Entsperrung nicht möglich. Der Owner entsperrte den Mac manuell
und bestätigte dies. Danach wurden Installation, erste Schritte einschließlich
Stopp-Anleitung und Fehlerhilfe wie M-09/M-10 betrachtet. Kein erster
Programmlauf oder Installations-/Stopp-Befehl wurde ausgeführt. VoiceOver
wurde anschließend auf off und der Seitenzoom auf den ursprünglichen Wert
100 % zurückgesetzt und beides beobachtet. Der Beschriftungsbereich war
bereits eingeschaltet und wurde nicht geändert.

EN: The UI lost the Safari window when moving to installation. Inventory
then reported a locked Mac that could not be unlocked automatically. The
owner manually unlocked it and confirmed. Installation, first steps/shutdown
guidance and troubleshooting were then sampled as M-09/M-10. No exercise or
installation/shutdown command was executed. VoiceOver off and original 100%
zoom were restored and observed. The caption panel was already enabled and
was not changed.

DE: Für #101/#102/#104 bleibt der gemeinsame A11Y-Status **partial/open**.
Braille **nicht geprüft**, weitere Browser/Plattformen und reale
Einsteigerbeobachtungen offen. Keine Issue-Schließung oder vollständige
WCAG-Konformität ableiten. Follow-up: Runtime-Blockade getrennt klären und
erst danach die tatsächlich laufende OpenCode-Version mit Anmeldung,
Tastatur, Fokus, VoiceOver und Zoom prüfen. Für den Lernendenpfad bleiben
detaillierte Screenreader-Beziehungen, DE-/EN-Sprachansagen und vollständige
Reflow-/Kontrast-/Erstnutzungstests offen. Kein Commit, Push oder Issue-Update
in diesem Auftrag.

EN: Shared accessibility status for #101/#102/#104 remains partial/open.
Braille is untested; other browsers/platforms and real beginner observations
remain open. No issue closure or full WCAG conformity follows. Resolve the
runtime blocker separately before testing actual OpenCode login, keyboard,
focus, VoiceOver and zoom. Detailed spoken relationships, language switching,
full reflow/contrast and first-use tests remain open for the learner journey.
No commit, push or issue update.

## OpenCode-Web-Folgeprüfung / OpenCode Web follow-up — 2026-11-09

DE: Der Owner meldete die Podman-VM als gestartet und erreichbar. Live-
Prüfung bestätigte den Zustand running. Der API-Socket wurde erneut aus
`podman machine inspect` ermittelt und nur für den jeweiligen Prozess als
CONTAINER_HOST verwendet; der Socketpfad wird nicht als Repository-Default
festgeschrieben. Engine: Podman 6.0.2, ARM64. Der vorhandene Container
`absdd-image-sandbox_ade_1` war beendet und wurde unverändert gestartet;
danach running/healthy, stiller authentifizierter Healthcheck Exit 0.
Keine weitere gvproxy-Reparatur, kein Reset und keine persistente
Verbindungsänderung erforderlich; die Ursache des ersten Fehlers ist damit
nicht rückwirkend bewiesen.

EN: The owner reported the VM running and reachable. Live inspection
confirmed running; the API socket was rediscovered through machine inspect
and used only as a process-local CONTAINER_HOST, not a repository default.
Podman engine 6.0.2, ARM64. Started the existing stopped container unchanged;
it became running/healthy, silent authenticated healthcheck exit 0. No
further gvproxy repair, reset or persistent connection change was needed;
the original failure's root cause is not retrospectively established.

DE: Tatsächlich abgefragte Laufzeit: **OpenCode v2.1.4**, Image
`5f530d888485537c160bddf9330f56844d99e98518d97e2d842bb27a76a1391d`,
Container-ID `7c604c361d0711b08f6a7e28addceace47223d6727fd19b38e7e6c82a8f3cccd`.
Quellstand weiterhin `dfbe883946e93d727b6fe463b8e0588551eb78f3` mit dem
noch nicht aktivierten Pin 2.2.6. Die „Über“-Seite der tatsächlich
dargestellten Weboberfläche zeigte **Version 2.1.3**. Diese drei
Versionsangaben bleiben getrennt; kein 2.2.6-Runtime-Nachweis. Keine neue
Imageinstallation oder Implementierung.

EN: Observed runtime: OpenCode v2.1.4, image and container IDs above. Source
revision remains the same with unactivated pin 2.2.6. The displayed web UI's
About page showed version 2.1.3. Keep all three observations separate; no
2.2.6 runtime acceptance. No new image or implementation.

| ID | Gegenstand / Subject | Ergebnis / Result |
|---|---|---|
| W-01 | Öffnen / Open | Safari zeigt unter lokalem Loopback die OpenCode-Verbindungsseite mit Überschrift, beschriftetem Pairing-Feld, QR-Alternative und Passwort-Alternative. / Safari displays the local connection page with heading, labelled pairing field, QR and password alternatives. |
| W-02 | Tastatur vor Anmeldung / Keyboard before login | Option-Tab vom Pairing-Feld zu QR-Taste und Use password; Return öffnet Passwortformular. Einfaches Tab erreichte nicht dieselbe vollständige Folge. / Option-Tab traversed pairing field, QR and password buttons; Return opened password form. Plain Tab did not establish the same complete traversal. |
| W-03 | Beschriftung und Fehler / Labels and errors | Serveradresse und verdecktes Passwortfeld sind im AX-Baum benannt. Ein synthetisch falsches Passwort führte nach Aktivieren von Verbinden zu erklärendem Text über Serveradresse/Passwort. Der Fehler erschien als Text im AX-Baum, nicht nachgewiesen als automatisch angesagter Alarm. / Address and secure password field have AX names; synthetic invalid password produced explanatory error text, exposed in AX but not established as an automatically announced alert. |
| W-04 | Erfolgreiche Anmeldung / Successful login | Owner meldete sich manuell unter localhost:5199 an. Anfangs war im gesteuerten Fenster weiter das Formular sichtbar; nach erneutem Abgleich wurde die Projekt-/Sitzungsoberfläche auch tatsächlich beobachtet. 127.0.0.1 und localhost sind getrennte Browserursprünge. Keine echten Zugangsdaten ausgelesen oder protokolliert. / Owner logged in manually at localhost; after resolving the observation mismatch, the project/session UI was observed. The two hostnames are separate browser origins. No real credentials read or recorded. |
| W-05 | Navigation nach Anmeldung / Post-login navigation | Suche, Sitzungseinträge, Startseite, Neue Sitzung, Projekt hinzufügen und Einstellungen per Option-Tab erreicht. Einstellungen mit Return geöffnet. In der Einstellungs-Tabgruppe war normales Tab erforderlich; damit Sprache, Tabs und Standardumgebung bis zum ausgeschalteten Berechtigungsschalter erreichbar, Shift-Tab führte zurück. Keine Einstellung verändert. / Reached listed home controls by Option-Tab and opened settings with Return. Plain Tab traversed the settings panel; Shift-Tab moved back. No settings changed. |
| W-06 | VoiceOver-Zweckansage / VoiceOver purpose announcement | Fokus auf ausgeschaltetem „Berechtigungen automatisch akzeptieren“, ohne ihn zu betätigen. Der AX-Werkzeugbaum zeigte nur Schalter/off; Owner bestätigte „Zweck wird verständlich angesagt“. Kein Labeldefekt allein aus der Werkzeugdarstellung abgeleitet. / Focused the off permission switch without toggling it. AX tooling showed only switch/off; owner confirmed understandable purpose announcement. No label defect inferred solely from the tool tree. |
| W-07 | Such-Leerzustand / Empty search state | Synthetischer Suchbegriff zeigte den Text „Keine Sitzungen für … gefunden“ im AX-Baum. Suche anschließend geleert. Automatische Live-Ansage nicht gesondert nachgewiesen. / Synthetic query exposed a textual no-results state; query then cleared. Automatic live announcement not separately established. |
| W-08 | Projektauswahl und Abbruch / Project chooser cancellation | Projekt hinzufügen öffnete „Projekt öffnen“, Fokus in Pfad-Combo-Box. Keine Ordnerauswahl übernommen. Escape schloss die Auswahl; Fokus danach auf scrollbarem Inhaltscontainer statt auslösendem Knopf. / Opened project chooser, focus in path combo box; selected no folder. Escape closed it, with focus on a scrollable content container rather than the trigger. |
| W-09 | Zoom / Page zoom | Safari bestätigte 200 %. Startseite ordnete sich vertikal an; betrachtete Suche, Projekt-/Sitzungsbereiche, Einstellungen und Hilfe blieben lesbar und erreichbar. Keine 400-%-/320-CSS-Pixel- oder vollständige Editor-/Codeprüfung. / Verified 200%; home view stacked vertically, sampled controls remained readable/reachable. No full 400%/narrow-width or editor/code review. |
| W-10 | Rücksetzung / Restoration | Safari-Menü bestätigte wieder 100 %, Systemeinstellungen VoiceOver off. Synthetisches Passwort und Suchbegriff entfernt. Keine Projekte/Sitzungen angelegt oder vorhandene Sitzung geöffnet; keine Modellanfrage. / Restored and verified 100% zoom and VoiceOver off; cleared synthetic password/query. Created no project/session, opened no existing session and sent no model request. |

DE: Das synthetische Passwort wurde vor der Übergabe entfernt. VoiceOver
war vor diesem Folgeversuch off, wurde für den Test aktiviert und danach
wieder ausgeschaltet. Bedienungs-Setup, Zoom und das Öffnen der Projektauswahl
erfolgten teilweise per AX-Klick. Die explizit genannten Tastaturfolgen und
Escape wurden praktisch geprüft; keine vollständige Tastaturreise behauptet.
Der vorhandene Container bleibt nach dem Test healthy/running; die vom Owner
gestartete VM bleibt an. Keine Stop-/Volume-/Image-Austauschoperation.

EN: Cleared synthetic password before handoff. VoiceOver was initially off,
enabled for the follow-up, then restored off. Setup, zoom and opening the
project chooser partly used AX clicks. The stated keyboard sequences and
Escape were actually tested, without claiming a complete keyboard journey.
Existing container remains healthy/running; the owner-started VM stays on.
No shutdown, volume operation or image replacement.

### Ergebnis und verbleibende Grenzen / Result and remaining limits

DE: **Begrenzter OpenCode-Web-Durchlauf nachgeholt; A11Y-Status weiterhin
partial/open.** Aktuelle VM-Verbindung und Webzugriff funktionieren. Keine
vollständige WCAG-2.2-AA-Freigabe, kein Laufzeitnachweis des Pins 2.2.6.
Braille bleibt ungeprüft. Offen bleiben insbesondere automatische Ansage
von Verbindungsfehlern/Leerzuständen, reproduzierbare Fokus-Rückgabe nach
Abbruch der Projektauswahl, detaillierte Sprachwechsel-/Kontrast-/Reflow-
und Editorprüfungen sowie weitere Plattformen. Die Fokus-Rückgabe wird als
konkrete Beobachtung dokumentiert, nicht ohne Kriterienprüfung als formaler
WCAG-Verstoß bewertet. Keine Implementierung oder neue Provideranmeldung.

EN: **Limited OpenCode Web review completed; accessibility remains
partial/open.** Current VM connectivity and web access work. No complete
WCAG 2.2 AA approval or runtime proof for pin 2.2.6. Braille untested.
Remaining work includes automatic error/status announcements, reproducible
focus restoration after project-chooser cancellation, detailed language,
contrast, reflow and editor testing, and other platforms. Record focus return
as an observation, not a formal WCAG failure without criterion assessment.
No implementation or new provider sign-in.

DE: Abschlusskontrolle: VM running, Container running/healthy, stiller
Web-Healthcheck erfolgreich. Der tägliche Metadatenexport wurde ohne
Inhalts-/Datenbankexport verifiziert: Auditdatum 2026-11-09, Run-ID
`70557c3c-5121-477c-a3a3-b46f785b7517`, zehn Metadatenzeilen,
Verifikation true. OpenCode-Datenbankmetadaten sind kein sitzungsbezogener
Auditnachweis; `session_coverage=not-exported`. Keine Retention-Löschung.

EN: Final check: VM running, container running/healthy, silent web healthcheck
successful. Verified daily metadata-only export for the audit date/run above,
ten metadata lines, verification true; no content/database export or retention
deletion. OpenCode storage metadata does not establish session-level coverage:
`session_coverage=not-exported`.
