# Lernwege und Zielgruppen / Learning Paths and Audiences

[Einstieg / Start](README.md)

## Gemeinsame Grundlage / Shared Foundation

**DE:** Alle vier IT-Berufe beginnen mit demselben sicheren Einstieg. Du musst
weder programmieren noch Container oder Spec Kit kennen. Spec Kit ist ein
Werkzeug, das einen Arbeitsauftrag in Anforderungen, einen Plan und Aufgaben
gliedert. Du lernst es erst nach dem technischen Einstieg kennen. Die Wege
hier sind Empfehlungen, kein Ersatz fuer Ausbildungsordnung oder Unterricht.

**EN:** All four IT occupations start with the same safe introduction. You
need no programming, container or Spec Kit experience. Spec Kit divides a work
request into requirements, a plan and tasks. You learn it after the technical
introduction. These paths are recommendations, not a replacement for your
training regulations or lessons.

| Schritt / Step | Anleitung / Guide | Sichtbares Ergebnis / Visible result |
|---|---|---|
| 1 | [Grundlagen](container-grundlagen.md) | Host, Image, Container, Mount und Volume unterscheiden / distinguish host, image, container, mount and volume |
| 2 | [Installation](installation.md) | eigenen Plattformpfad waehlen und Konfiguration pruefen / choose your platform path and check configuration |
| 3 | [Erste Schritte](erste-schritte.md) | Programm ohne KI-Anmeldung ausfuehren / run a program without AI sign-in |
| 4 | [Alltag](alltag.md) und [Git](git-und-hosting.md) | Daten sichern, eigenen Fork nutzen und sicher stoppen / preserve data, use your own fork and stop safely |
| 5 | [Agenten und Spec Kit](agenten-und-spec-kit.md) | begrenzte Auftraege und menschliches Review verstehen / understand bounded tasks and human review |

**DE:** Nach Schritt 3 kannst du pausieren. Alle weiteren Themen sind auch im
ersten Lehrjahr moeglich, aber nur mit passender Begleitung und geltenden
Freigaben. Eine Empfehlung fuer spaeter ist kein Verbot fuer frueheres Lernen.
Nicht jede Person muss sofort alle Sprachen oder Agenten verwenden.

**EN:** You may pause after step 3. Later topics are possible in the first
year too, with suitable guidance and applicable approvals. A recommendation
for later is not a ban on earlier learning. You need not use every language
or agent immediately.

## Berufliche Vertiefung / Occupational Focus

**DE:** Wähle den Bezugsweg anhand des Lernziels: Fork für fortlaufende
Sandbox-Pflege, später optionales [Template](template-profil.md) für eine
unabhängige Sandbox, leeres Produktrepo für die Projektwerkstätten. Das
Template-Profil ist noch nicht aktiviert; kein Wechsel hebt bestehende Gates auf.

**EN:** Choose by goal: fork for maintained sandbox work, later optional
template for an independent sandbox, empty product repo for workshops. Template
use is not enabled yet and removes no existing gate.

**DE:** Waehle nach der Grundlage eine Aufgabe mit deiner Lehrperson. Verwende
nur erfundene Daten. Die Aufgaben vertiefen den Umgang mit der Sandbox; sie
behaupten keine vollstaendige Abdeckung einer Fachrichtung.

**EN:** After the foundation, choose a task with your instructor. Use fictional
data only. These tasks deepen sandbox skills; they do not claim full coverage
of an occupation or specialisation.

| Beruf oder Fachrichtung / Occupation or specialisation | Beispielaufgabe / Example task | Nachweis / Evidence |
|---|---|---|
| Fachinformatik: Anwendungsentwicklung / application development | kleines Programm in einer [Toolchain](toolchains/README.md) erweitern / extend a small program | Test und erklaerter Diff / test and explained diff |
| Fachinformatik: Systemintegration / systems integration | [Mounts und Volumes](../betrieb/compose-und-speicher.md) unterscheiden / distinguish mounts and volumes | Speicherplan ohne Secrets / storage plan without secrets |
| Fachinformatik: Daten- und Prozessanalyse / data and process analysis | erfundene CSV-Daten mit [Python](toolchains/python.md) pruefen / check fictional CSV data | dokumentierte Eingaben und Ergebnisse / documented input and results |
| Fachinformatik: Digitale Vernetzung / digital networking | [lokale Ports](troubleshooting.md) und Host-Container-Weg erklaeren / explain local ports and the host-container path | Textablauf, keine realen Netzwerkscans / text walkthrough, no real network scans |
| IT-System-Elektronik / IT systems electronics | Plattform, Netzwerkgrenze und sichere Abschaltung dokumentieren / document platform, network boundary and safe shutdown | nachvollziehbare Checkliste, keine Elektroarbeiten / clear checklist, no electrical work |
| IT-System-Management / IT systems management | Werkzeuge, Voraussetzungen und Betriebsaufwand vergleichen / compare tools, prerequisites and operating effort | begruendete Entscheidung mit Annahmen / reasoned decision with assumptions |
| Digitalisierungsmanagement / digitalisation management | erfundenen Geschaeftsprozess beschreiben und verbessern / describe and improve a fictional business process | Anforderung, Datenschutzgrenze und Erfolgskriterium / requirement, privacy boundary and success criterion |
| Softwareentwicklung ohne Spezialkenntnisse / development without specialist knowledge | [Entwickler-Kurzpfad](entwickler-kurzpfad.md) nutzen / use the developer short path | reproduzierbarer Projektstart / reproducible project start |

## Verbindung Zu Home Baseline / Connection to Home Baseline

**DE:** Die eigentlichen Lernreihen bleiben in Home Baseline. Lies im Container
`~/home-baseline-source/docs/learning-units/START-HERE-FUER-LERNENDE.md`.
Der eingebettete Stand ist schreibgeschuetzt und durch
[`home-baseline.lock.json`](../../home-baseline.lock.json) gebunden. Der
[oeffentliche Einstieg](https://github.com/hindermath/home-baseline/blob/main/docs/learning-units/START-HERE-FUER-LERNENDE.md)
kann neuer sein. Ein institutioneller Spiegel ist ebenso moeglich. Diese
Sandbox dokumentiert Werkzeugnutzung, nicht einen zweiten Lernreihenkatalog.

**EN:** Actual learning series remain in Home Baseline. Inside the container,
read the path above. The embedded copy is read-only and bound by the lock
file. The public entry may be newer; an institutional mirror is also valid.
This sandbox documents tool use, not a second learning-series catalogue.

**DE:** Naechster Schritt: [Installation](installation.md), wenn die Umgebung
noch fehlt; sonst [Erste Schritte](erste-schritte.md).

**EN:** Next: installation if the environment is missing; otherwise first steps.
