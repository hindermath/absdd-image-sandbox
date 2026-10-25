# Verstaendlichkeit Und Barrierefreiheit / Readability and Accessibility

[Einstieg / Start](README.md)

## Ziel Und Nachweisgrenze / Goal and Evidence Boundary

**DE:** Die Dokumentation richtet sich nach
[WCAG 2.2 Level AA](https://www.w3.org/TR/WCAG22/), soweit Kriterien anwendbar
sind. WCAG sind pruefbare Anforderungen fuer barrierefreie Web-Inhalte.
CEFR B2 bezeichnet unser Sprachziel: klare Saetze, erklaerte Begriffe und
ueberschaubare Schritte. B2 ist ein zusaetzliches redaktionelles Ziel, kein
Nachweis erfuellter WCAG-Kriterien.

**EN:** Documentation targets WCAG 2.2 Level AA where criteria apply. WCAG
provides testable requirements for accessible web content. CEFR B2 is our
language target: clear sentences, explained terms and manageable steps. B2
is an additional editorial goal, not proof of WCAG conformance.

**DE:** Es gibt noch keine vollstaendige WCAG-Konformitaetsabnahme dieser
Dokumentation. Markdown-Quelltext, GitHub-Rendering und die Bedienung mit
Hilfstechnologie sind verschiedene Pruefgegenstaende. Plattformgrenzen werden
als offen dokumentiert, nicht als bestandene Kriterien. Das in WCAG 2.2
entfernte Kriterium 4.1.1 und das AAA-Lesbarkeitskriterium 3.1.5 werden nicht
faelschlich als AA-Nachweise gezaehlt.

**EN:** Full WCAG conformance acceptance is not yet available. Markdown source,
GitHub rendering and assistive-technology use are different review subjects.
Platform limitations remain open, not passed criteria. Removed criterion
4.1.1 and AAA reading-level criterion 3.1.5 are not counted as AA evidence.

## Redaktionelle Regeln / Editorial Rules

| Regel / Rule | Durchfuehrungshinweis / Review instruction |
|---|---|
| Deutsch zuerst, Englisch gleichwertig / German first, equivalent English | Warnungen, Voraussetzungen, Ergebnis und Fehlerhilfe in beiden Sprachen vergleichen / compare warnings, prerequisites, result and error help |
| klare Gliederung / clear structure | genau eine Hauptueberschrift, sinnvolle Unterueberschriften und beschreibende Linktexte / one main heading, meaningful subheadings and descriptive links |
| lesbare Befehle / readable commands | Host oder Container, Shell, Zielordner und erwartete Ausgabe nennen; keine Zugangsdaten / state host or container, shell, target directory and expected output; no credentials |
| einfache Tabellen / simple tables | Kopfzeile, kurze Zellen und keine notwendige Information nur in breiten Tabellen / headers, short cells, no essential information only in wide tables |
| textorientierte Erklaerung / text-first explanation | Diagramme vollstaendig in Text erklaeren; Farbe und Position allein genuegen nicht / explain diagrams fully in text; colour and position alone are insufficient |
| sichere Schritte / safe steps | Loeschwirkung vor destruktiven Befehlen erklaeren; sichere Alternative zuerst / explain deletion before destructive commands; safe alternative first |

## Praktisches Review / Practical Review

**DE:** Learning/A11Y Review prueft den vollstaendigen Einstieg in der
gerenderten GitHub-Ansicht: README, Lernweg, Installation, erste Uebung,
Fehlerhilfe und Stopp. Fuer jeden Schritt werden Browser, Version,
Betriebssystem, Hilfsmittel, Datum, Beobachtung und Ergebnis festgehalten.

**EN:** Learning/A11Y Review checks the complete entry journey in rendered
GitHub: README, learning path, installation, first exercise, error help and
shutdown. Record browser, version, OS, assistive technology, date, observation
and outcome for each step.

1. **DE:** Nur Tastatur verwenden: Links erreichen, Fokus erkennen, zur
   Uebersicht zurueckkehren. **EN:** Use the keyboard only: reach links,
   identify focus and return to the overview.
2. **DE:** Mit Screenreader Ueberschriften, Listen, Tabellen und Code lesen;
   DE-/EN-Wechsel und Sprachansage pruefen. **EN:** Read headings, lists,
   tables and code with a screen reader; check language changes and speech.
3. **DE:** Mit Zoom und schmaler Ansicht pruefen, ob Fliesstext ohne
   Informationsverlust lesbar bleibt. Code und Tabellen separat bewerten.
   **EN:** Check zoom and narrow view for readable text without loss;
   assess code and tables separately.
4. **DE:** Eine Person ohne Spezialkenntnisse fuehrt den Lernpfad aus und
   erklaert Mount-, Datenverlust- und Freigabegrenzen in eigenen Worten.
   **EN:** A non-specialist follows the path and explains mount, data-loss
   and approval boundaries in their own words.

**DE:** Status `Open`: diese menschlichen Beobachtungen fehlen im aktuellen
Auftrag. Owner: Learning/A11Y Review. Follow-up: Tests mit echten
Teilnehmenden aus den vier Berufen und Einsteiger-Entwicklern organisieren.
Trigger: vor A11Y-Konformitaetsbehauptung oder unbegleitetem Rollout und bei
wesentlichen Navigationsaenderungen. Automatische Linktests schliessen dies
nicht. Markdown-Sprachbloecke garantieren keine korrekte `lang`-Auszeichnung
durch GitHub. Eine spaetere PDF braucht eine eigene Barrierefreiheitspruefung.

**EN:** Open: these human observations are missing in this task. Owner:
Learning/A11Y Review. Follow up with real participants from the four
occupations and non-specialist developers. Re-evaluate before claiming A11Y
conformance or unattended rollout, and after major navigation changes.
Automated links do not close this item. Markdown language blocks do not
guarantee correct GitHub lang attributes. PDFs need separate accessibility
assessment.

**DE:** Bei einer Barriere melde Seite, Abschnitt und Problem ohne persoenliche
Gesundheitsdaten. Hilfsmittel duerfen freiwillig genannt werden. Siehe
[Fehler melden](faq.md#wie-melde-ich-einen-fehler--how-do-i-report-a-problem).

**EN:** Report a barrier with page, section and problem, without personal
health data. Naming assistive technology is optional. See reporting guidance.
