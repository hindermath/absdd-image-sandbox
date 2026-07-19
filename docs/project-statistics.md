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
| 2026-07-10 | docs/provider-neutral-learner-hosting | 36 | 74.073 | 133 | GitHub-unabhaengiger Lernendenpfad fuer institutionelles GitLab, Codeberg, Forgejo und weitere Git-Systeme; oeffentliche GitHub-Referenzen bleiben Herkunftsnachweis. Agenten-Guidance und Session-Log synchronisiert. Diff +141/−43. |
| 2026-07-15 | docs/home-sync-container-boundary | 40 | — | — | Eingebettete und per Override gemountete Level-0-Referenz als direkte Container-Lesequelle bestaetigt; README und vier Agenten-Dateien stellen klar, dass schreibende `sync-home.*`-Laeufe nach `/home/adedev` gesperrt sind und auf dem Host laufen. Read-only Check-/Vorschaumodi bleiben fuer Diagnosen erhalten; Compose-Mountmodell unveraendert. |

---

## Gesamtstand des Repositories / Repository Snapshot

**DE:** Stand: 2026-07-10. Dieses Repository enthält keinen klassischen
Produktionscode und kein Testframework; der Schwerpunkt liegt auf
Dokumentation, Konfiguration und Skripten.

**EN:** As of 2026-07-10. This repository contains no classic production code and
no test framework; the focus is documentation, configuration, and scripts.

| Kategorie / Category | Dateien / Files | Zeilen / Lines | Anteil / Share |
|---|---:|---:|---:|
| Dokumentation (.md) / Documentation | 349 | 60.071 | 81,1 % |
| Sonstige / Other (LICENSE, man, dotfiles) | 24 | 5.471 | 7,4 % |
| Konfiguration / Configuration | 47 | 4.242 | 5,7 % |
| Skripte / Scripts (.sh, .ps1) | 26 | 4.289 | 5,8 % |
| **Gesamt / Total** | **446** | **74.073** | **100 %** |

---

## Statistikprofil-1-Archiv / Statistics Profile 1 Archive
| Kennzahl / Metric | Verdichteter Gesamtblick / Condensed Overview |
|---|---:|
| Artefaktbasis gesamt / Total artefact base | 446 Dateien / 74.073 Zeilen |
| Beobachtbarer Projektzeitraum / Observable period | 2026-04-29 – 2026-07-10 |
| Sichtbare Git-Aktivtage / Visible git active days | 36 |
| Commits gesamt / Total commits | 133 |
| Manuelle Äquivalenz (80 Z./AT) / Manual equiv. | ~925,9 AT (~7.222,1 h) |
| Manuelle Äquivalenz (100 Z./AT) / Manual equiv. | ~740,7 AT (~5.777,7 h) |
| Repo-weiter Speedup gg. 80-Zeilen-Referenz | ~25,7x |
| Repo-weiter Speedup gg. Thorsten-Referenz (100) | ~20,6x |

### Artefaktmix / Artefact Mix

```text
Doku (.md)      | ############################################  60071  (81%)
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
Erfahren / 80 Z./AT   | ##########################################  926 AT
Thorsten-Solo / 100   | ##################################         741 AT
KI-sichtbar (real)    | ##                                          36 AT
```

**DE:** Der Balken vergleicht drei Sichtweisen auf denselben Umfang (74.073
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
gg. 100 Z./AT (Thorsten)    | #####################       20.6x
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

## Gesamtstatistik / Overall Statistics

<!-- project-statistics-v2:begin -->

Profil 2 verwendet Git-getrackte Textdateien und sichtbare Git-Aktivitaet. Die Werte beschreiben Lieferdichte, keine persoenliche Arbeitszeit.

*Profile 2 uses Git-tracked text files and visible Git activity. The values describe delivery density, not personal working time.*

| Kennzahl / Metric | Wert / Value |
|---|---:|
| Textbasis / Text base | 91678 lines |
| Textdateien / Text files | 600 |
| Beobachtbarer Zeitraum / Observable period | 2025-07-27..2026-07-19 |
| Aktivtage / Active days | 44 |
| Relevante Commits / Relevant commits | 124 |
| Zeilen je Aktivtag / Lines per active day | 2083.6 |
| Peak-Tag im Fenster / Peak day in window | 2026-07-03 / 33733 |
| Peak-Woche im Fenster / Peak week in window | 2026-06-28 / 35995 |
| Laengste Serie / Longest streak | 8 days |
| Speedup vs. 80 lines/day | 26.0x |
| Speedup vs. 100 lines/day | 20.8x |
| Methodik / Methodology | v2; source `a8dbd90bde95` |

### Artefaktmix / Artifact Mix

```text
Produktiv / Production          [#...................]   0.1% | 82
Tests                           [#...................]   0.3% | 268
Dokumentation / Documentation   [##################..]  88.2% | 80897
Skripte / Scripts               [##..................]  10.0% | 9187
Konfiguration / Configuration   [#...................]   1.0% | 873
Daten und Medien / Data and media [....................]   0.0% | 0
Sonstiger Text / Other text     [#...................]   0.4% | 371
```

Die Balken teilen die aktuelle getrackte Textbasis in stabile Kategorien. Prozent und Zeilenwert sind die genaue, textorientierte Aussage.

*The bars split the current tracked text base into stable categories. Percentages and line counts provide the exact text-first result.*

### Tagesaktivitaet / Daily Activity

```text
Wochen / Weeks 01..26 | 2025-07-27..2026-01-24
So/Su  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Mo/Mo  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Di/Tu  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Mi/We  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Do/Th  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Fr/Fr  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Sa/Sa  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

```text
Wochen / Weeks 27..52 | 2026-01-25..2026-07-25
So/Su  0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 3 2 1 0 4 0 0 4 2 4
Mo/Mo  0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 3 0 3 2 0 0 0 0 0 4 -
Di/Tu  0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 3 3 2 3 0 0 0 0 0 3 -
Mi/We  0 0 0 0 0 0 0 0 0 0 0 0 0 1 3 0 0 2 4 0 0 0 0 2 1 -
Do/Th  0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 3 3 0 4 3 0 0 0 0 1 -
Fr/Fr  0 0 0 0 0 0 0 0 0 0 0 0 0 4 0 2 1 3 0 0 0 2 4 4 4 -
Sa/Sa  0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 2 0 0 0 2 0 4 4 0 -
```

DE: 0 = keine Aenderung; 1 = 1..79; 2 = 80..399; 3 = 400..1599; 4 = 1600+ geaenderte Textzeilen; - = noch nicht abgelaufen.

*EN: 0 = no change; 1 = 1..79; 2 = 80..399; 3 = 400..1599; 4 = 1600+ changed text lines; - = not elapsed.*

### Wochenvolumen / Weekly Volume

```text
Wochen / Weeks 01..26 | 2025-07-27..2026-01-24
Keine Aktivitaet / No activity
```

```text
Wochen / Weeks 27..52 | 2026-01-25..2026-07-25
   cap 50000 | . . . . . . . . . . . . . . . . . . . . . . . . . .
       41667 | . . . . . . . . . . . . . . . . . . . . . . . . . .
       33333 | . . . . . . . . . . . . . . . . . . . . . . # . . .
       25000 | . . . . . . . . . . . . . . . . . . # . . . # . . .
       16667 | . . . . . . . . . . . . . . . . . . # . . . # . . #
        8333 | . . . . . . . . . . . . . . . . . . # . . . # # . #
           0 +-----------------------------------------------------
```

Das Wochenvolumen zeigt Additionen plus Loeschungen. Es ist Aenderungsaktivitaet, nicht die aktuelle Groesse des Repositories.

*Weekly volume shows additions plus deletions. It represents change activity, not the current repository size.*

### Kumulative Entwicklung / Cumulative Development

```text
Wochen / Weeks 01..26 | 2025-07-27..2026-01-24
Keine Aktivitaet / No activity
```

```text
Wochen / Weeks 27..52 | 2026-01-25..2026-07-25
  cap 200000 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      166667 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      133333 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      100000 | . . . . . . . . . . . . . . . . . . . . . . . # # #
       66667 | . . . . . . . . . . . . . . . . . . . . . . # # # #
       33333 | . . . . . . . . . . . . . . . . . . # # # # # # # #
           0 +-----------------------------------------------------
```

Die kumulative Kurve summiert nur das Brutto-Aenderungsvolumen im Fenster. Sie darf nicht als aktuelle Codebasis gelesen werden.

*The cumulative curve sums gross change volume within the window only. It must not be read as the current code base.*

### Monatsvolumen / Monthly Volume

```text
Last 12 calendar months
  cap 100000 | . . . . . . . . . . . .
       83333 | . . . . . . . . . . . .
       66667 | . . . . . . . . . . . #
       50000 | . . . . . . . . . . . #
       33333 | . . . . . . . . . . # #
       16667 | . . . . . . . . . . # #
           0 +-------------------------
```

Es liegen keine belastbaren Phasendaten vor. Deshalb zeigt dieses Diagramm Monate und erfindet keine Projektphasen.

*No reliable phase series is available. This chart therefore shows months and does not invent project phases.*

### Beschleunigungsfaktoren / Acceleration Factors

```text
Scale: 0..50x
80 lines/day       [##########..........] 26.0x
100 lines/day      [########............] 20.8x
```

Die Faktoren vergleichen sichtbare Lieferdichte mit den dokumentierten manuellen Referenzen. Sie messen keine Arbeitszeit.

*The factors compare visible delivery density with documented manual references. They do not measure working time.*

### Durchsatzvergleich / Throughput Comparison

```text
Scale: 0..5000 lines/day
Experienced manual [#...................] 80
Thorsten solo      [#...................] 100
Visible repository [########............] 2083.6
```

Die gemeinsame Skala vergleicht Referenzen und sichtbare Lieferdichte. Sie schreibt die Git-Aktivitaet keiner Person oder KI pauschal zu.

*The common scale compares references with visible delivery density. It does not attribute Git activity to a person or AI by default.*

### Textalternative / Text Alternative

DE: Das Fenster beginnt am 2025-07-27 und endet am 2026-07-19. Es enthaelt 44 aktive und 314 inaktive vergangene Tage. Peak-Tag: 2026-07-03 / 33733. Peak-Woche: 2026-06-28 / 35995. Laengste Serie: 8 Tage (2026-07-10..2026-07-17).

*EN: The window starts on 2025-07-27 and ends on 2026-07-19. It contains 44 active and 314 inactive elapsed days. Peak day: 2026-07-03 / 33733. Peak week: 2026-06-28 / 35995. Longest streak: 8 days (2026-07-10..2026-07-17).*

| Monat / Month | Geaenderte Textzeilen / Changed text lines |
|---|---:|
| 2025-08 | 0 |
| 2025-09 | 0 |
| 2025-10 | 0 |
| 2025-11 | 0 |
| 2025-12 | 0 |
| 2026-01 | 0 |
| 2026-02 | 0 |
| 2026-03 | 0 |
| 2026-04 | 67 |
| 2026-05 | 12969 |
| 2026-06 | 37448 |
| 2026-07 | 76820 |

<!-- project-statistics-v2:end -->
