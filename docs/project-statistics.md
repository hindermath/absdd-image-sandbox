# Projektstatistik / Project Statistics — absdd-image-sandbox

**Stand / Date:** 2026-07-10
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

> **DE:** Lebendiges Dokument — nach jedem abgeschlossenen Feature, jeder
> Spec-Kit-Phase und auf ausdrückliche Anfrage aktualisieren.
>
> **EN:** Living document — update after every completed feature, Spec-Kit
> phase, or on explicit request.

**DE:** Dieses Ledger wurde mit dem Feature „Anfänger-Onboarding für Lernende"
erstmals angelegt. Ältere Arbeit vor diesem Zeitpunkt ist als kumulierter
Basis-Snapshot verdichtet, nicht rückwirkend je Feature aufgeschlüsselt.

**EN:** This ledger was created together with the "beginner onboarding for
learners" feature. Earlier work before that point is condensed into a cumulative
baseline snapshot, not retroactively broken down per feature.

---

## Methodik / Methodology

**DE:** Die Beschleunigungsfaktoren sind ein *blended repository speedup*:
Lieferdichte (Zeilen je sichtbarem Git-Aktivtag) gegen eine manuelle Referenz,
keine Stoppuhrzeit. Dieses Repository ist eine Container-/Infrastruktur- und
Dokumentationsbasis (Dockerfile, Compose, Skripte, `docs/`), kein
C#/.NET-Anwendungscode. Daher gelten hier bewusst die Infrastruktur-Basiswerte
statt der C#/.NET-Standardbasis von 125 Zeilen/Arbeitstag:

**EN:** The acceleration factors are a *blended repository speedup*: delivery
density (lines per visible git active day) against a manual reference, not
stopwatch time. This repository is a container/infrastructure and documentation
base (Dockerfile, Compose, scripts, `docs/`), not C#/.NET application code.
Therefore the infrastructure baselines apply here deliberately instead of the
C#/.NET default of 125 lines/workday:

| Referenz / Reference | Wert / Value | Bedeutung / Meaning |
|---|---:|---|
| Konservativ / Conservative | 80 Z./AT | Vorsichtige manuelle Untergrenze / cautious manual lower bound |
| Thorsten-Solo (Infrastruktur) | 100 Z./AT | Skripting-/Infrastruktur-Referenz / scripting-infrastructure reference |
| TVöD-Arbeitstag / workday | 7,8 h | 21,5 Arbeitstage je Monat / 21.5 workdays per month |

**DE:** „Z./AT" = Zeilen je Arbeitstag. „AT" = Arbeitstag. Die Zeilenzahlen
zählen alle getrackten Dateien; sie sind ein Artefakt-Umfangsmaß, kein
Qualitätsmaß.

**EN:** "Z./AT" = lines per workday. "AT" = workday. Line counts cover all
tracked files; they are an artefact-volume measure, not a quality measure.

---

## Fortschreibungsprotokoll / Update Log

**DE:** Ältester Eintrag oben, neuester Eintrag unten.
**EN:** Oldest entry at top, newest entry at bottom.

| Datum / Date | Phase / Branch | Aktivtage ges. / Active days | Zeilen ges. / Lines | Commits ges. / Commits | Hauptarbeitspakete / Main Work Packages |
|---|---|---:|---:|---:|---|
| 2026-07-10 | docs/lernende-container-onboarding | 36 | 73.081 | 129 | Erst-Erfassung der Statistik. Anfänger-Onboarding: 5 neue Lernenden-Dokumente (`container-grundlagen`, `warum-sandbox`, `installation`, `erste-schritte`, `troubleshooting`), README-Hub-Umbau, Glossar-Erweiterung, Session-Log. Diff +1.136/−74. |
| 2026-07-10 | feat/four-agent-learner-environment | 36 | 73.975 | 132 | Vier Required-Agenten und Syft im Podman-Image; getrennte Agenten-Volumes, Audit-Metadaten, image-interne SBOM, Anfängerpfad mit persönlichem Fork und erstem kontrollierten Agentenlauf, Lychee-/Static-CI. Diff +830/−379. |

---

## Gesamtstand des Repositories / Repository Snapshot

**DE:** Stand: 2026-07-10. Dieses Repository enthält keinen klassischen
Produktionscode und kein Testframework; der Schwerpunkt liegt auf
Dokumentation, Konfiguration und Skripten.

**EN:** As of 2026-07-10. This repository contains no classic production code and
no test framework; the focus is documentation, configuration, and scripts.

| Kategorie / Category | Dateien / Files | Zeilen / Lines | Anteil / Share |
|---|---:|---:|---:|
| Dokumentation (.md) / Documentation | 348 | 59.973 | 81,1 % |
| Sonstige / Other (LICENSE, man, dotfiles) | 24 | 5.471 | 7,4 % |
| Konfiguration / Configuration | 47 | 4.242 | 5,7 % |
| Skripte / Scripts (.sh, .ps1) | 26 | 4.289 | 5,8 % |
| **Gesamt / Total** | **445** | **73.975** | **100 %** |

---

## Gesamtstatistik / Overall Statistics

| Kennzahl / Metric | Verdichteter Gesamtblick / Condensed Overview |
|---|---:|
| Artefaktbasis gesamt / Total artefact base | 445 Dateien / 73.975 Zeilen |
| Beobachtbarer Projektzeitraum / Observable period | 2026-04-29 – 2026-07-10 |
| Sichtbare Git-Aktivtage / Visible git active days | 36 |
| Commits gesamt / Total commits | 132 |
| Manuelle Äquivalenz (80 Z./AT) / Manual equiv. | ~925 AT (~7.213 h) |
| Manuelle Äquivalenz (100 Z./AT) / Manual equiv. | ~740 AT (~5.770 h) |
| Repo-weiter Speedup gg. 80-Zeilen-Referenz | ~25,7x |
| Repo-weiter Speedup gg. Thorsten-Referenz (100) | ~20,5x |

### Artefaktmix / Artefact Mix

```text
Doku (.md)      | ############################################  59973  (81%)
Sonstige/Other  | ####                                           5471  ( 7%)
Konfiguration   | ###                                            4242  ( 6%)
Skripte         | ###                                            4289  ( 6%)
```

**DE:** Das Diagramm zeigt, wie sich die Zeilen auf die Kategorien verteilen.
Über 80 % sind Dokumentation — passend zu einem öffentlichen Referenz- und
Ausbildungs-Repository.

**EN:** The diagram shows how the lines split across categories. More than 80 %
is documentation — fitting for a public reference and training repository.

### Phasenvolumen: Commits je Monat / Phase Volume: Commits per Month

```text
2026-04 | #                                         1
2026-05 | #######################################  87
2026-06 | ############                             27
2026-07 | #######                                  17
```

**DE:** Feste X-Slots je Monat. Der Aufbau-Schwerpunkt lag im Mai 2026 (87
Commits an 22 Aktivtagen); danach folgen kleinere Pflege- und Feature-Wellen.

**EN:** Fixed X slots per month. The build-up peak was May 2026 (87 commits on
22 active days); smaller maintenance and feature waves followed.

### Aufwandsvergleich repo-weit / Repo-Wide Effort Comparison

```text
Erfahren / 80 Z./AT   | ##########################################  925 AT
Thorsten-Solo / 100   | ##################################         740 AT
KI-sichtbar (real)    | ##                                          36 AT
```

**DE:** Der Balken vergleicht drei Sichtweisen auf denselben Umfang (73.975
Zeilen): erfahrene manuelle Referenz (80 Z./AT), Thorsten-Solo-Infrastruktur
(100 Z./AT) und die real sichtbaren Git-Aktivtage. Es ist ein Lieferdichte-
Vergleich, keine gemessene Arbeitszeit.

**EN:** The bars compare three views of the same volume (73,975 lines):
experienced manual reference (80 l/wd), Thorsten-Solo infrastructure (100 l/wd),
and the actually visible git active days. It is a delivery-density comparison,
not measured working time.

### Beschleunigungsfaktoren / Acceleration Factors

```text
gg. 80 Z./AT (konservativ)  | ##########################  25.7x
gg. 100 Z./AT (Thorsten)    | #####################       20.5x
```

**DE:** Der repo-weite Speedup ergibt sich aus manueller Äquivalenz geteilt
durch sichtbare Aktivtage. Höhere Werte bedeuten mehr Artefaktvolumen je
sichtbarem Tag, nicht automatisch höhere Qualität.

**EN:** The repo-wide speedup is manual equivalent divided by visible active
days. Higher values mean more artefact volume per visible day, not automatically
higher quality.

### Feature-Fokus: Anfänger-Onboarding / Feature Focus: Beginner Onboarding

```text
Erfahren / 80 Z./AT   | ##############  14.2 AT
Thorsten-Solo / 100   | ###########     11.4 AT
KI-sichtbar (real)    | #                1.0 AT
```

**DE:** Das aktuelle Feature lieferte 1.136 hinzugefügte Zeilen (netto +1.062)
über 8 Dateien an einem sichtbaren Aktivtag. Manuell entspräche das grob 14
Arbeitstagen (80 Z./AT) bzw. 11 Arbeitstagen (100 Z./AT).

**EN:** The current feature delivered 1,136 added lines (net +1,062) across 8
files on one visible active day. Manually this would roughly equal 14 workdays
(80 l/wd) or 11 workdays (100 l/wd).
