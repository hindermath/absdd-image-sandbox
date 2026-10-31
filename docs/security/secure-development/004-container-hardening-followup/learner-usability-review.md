# Betreuter Lernenden-Pilot / Supervised learner pilot

**Stand 2026-10-31: Open.** Es hat noch keine Teilnahme und keine
Barrierefreiheits- oder Nutzungsabnahme stattgefunden. Owner: Learning/A11Y
Review. Nächste Aktion: freiwillige Teilnehmende und einen betreuten Termin
organisieren. Trigger und Frist: vor unbegleiteter Nutzung oder öffentlicher
Behauptung zur Bedienbarkeit. Der Review dokumentiert Einwilligung und
Beobachtung getrennt von persönlichen Projekt- oder Agenteninhalten.

## Ablauf (Host und Container klar trennen)

1. Auf dem **Host** im Repository mit Podman/Compose und bestehendem
   Test-Image die [ersten Schritte](../../../fuer-lernende/erste-schritte.md)
   lesen. Einen eigenen Einstieg wählen; ein KI-Providerkonto ist nicht
   Voraussetzung für lokale Schritte.
2. In einem **synthetischen Projekt** einen kleinen Text speichern. Den
   angezeigten Projektpfad notieren. Auf dem Host die schreibfreie Vorschau
   `bash scripts/compose-down-with-audit.sh --podman --dry-run` zeigen,
   anschließend den normalen Audit-Stopp unter Aufsicht ausführen.
3. Auf dem Host nach dem Stopp wieder starten, den Projekttext öffnen und
   feststellen, ob er erhalten blieb. Fehlermeldung und tatsächliche Hilfe
   in eigenen Worten erklären lassen.
4. Einen **synthetischen Sicherheitsfehler** zeigen: isolierter Fake-Compose-
   Export endet ohne aktuelle Auditdatei. Der Stopp muss blockieren.
   Lernende suchen die Phase in der Meldung und nennen den sicheren nächsten
   Schritt: Audit-Mount/Exporter prüfen, Wrapper erneut ausführen; kein
   `down -v`, keine fremde Sperre entfernen. Keine echten Sitzungsdaten
   einsehen.

## Beobachtungsbogen

| Feld | Protokoll |
| --- | --- |
| Datum, freiwillige Rolle, Fachrichtung | Open; keine Personendaten hier eintragen |
| Plattform, Shell, Test-Image-ID, Einstieg | Open |
| Aufgabe ohne Hilfe abgeschlossen? Schritte/Fehlversuche | Open |
| Wo wurde Hilfe benötigt? War DE/EN verständlich? | Open |
| Tastatur, Fokus, Screenreader, Kontrast, Zoom, Fehlermeldung | Open; WCAG 2.2 AA gezielt prüfen |
| Sicherheitsfehler erkannt und sicherer Wiederanlauf genannt? | Open |
| Verbesserung, Owner, Termin, erneuter Versuch | Open |

Abdeckungsplan: Fachinformatiker*innen in **Anwendungsentwicklung,
Systemintegration, Daten- und Prozessanalyse, Digitale Vernetzung**;
IT-System-Elektroniker*innen; Kaufleute für IT-System-Management;
Kaufleute für Digitalisierungsmanagement. Eine Teilnahme pro Profil ist
zunächst nur geplant, keine Quote erreicht. Unterschiedliche Vorerfahrung,
assistive Technik und Sprache sollen freiwillig berücksichtigt werden.

## English

**Open as of 2026-10-31.** No participant observation or accessibility
acceptance has happened. Learning/A11Y Review must arrange voluntary,
supervised sessions before unattended use or a usability claim. The sequence
uses a synthetic project: choose a local path without needing an AI account,
save a file, preview and perform the audit stop, reopen the project, then
interpret an isolated missing-export failure. Record help, errors, keyboard
and assistive-tech observations in the fields above without storing personal
agent content. Cover all four IT occupations and the four IT-specialist
disciplines listed above. WCAG 2.2 AA is the review target, not an automated
Markdown pass.
