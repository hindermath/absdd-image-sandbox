# Statistik-Drift: Wartungsnachweis / Statistics drift: maintenance evidence

DE: Ownerauftrag: Statistik-Drift beheben und bei gruener technischer Pruefung
mit DeliveryMode MergeAndSync und Admin-Bypass liefern. Sauberer Ausgangsstand
f4e43af5bde625476aaeef30d3361895d1fdd811 reproduziert Exit 1. Der unveraenderte
Renderer ergibt identische Mengenwerte und dieselbe Quellenrevision
74dfc73a9408; ausschliesslich Zeitraumende, aktuelle Tageszelle und bilinguale
Textalternative wechseln vom 09. auf den 10.11.2026. PR #131 wurde am 09.11.
gerendert und erst am 10.11. gemergt. Normalbetrieb verwendet das aktuelle
Datum in Europe/Berlin; SOURCE_DATE_EPOCH bleibt nur die dokumentierte
Reproduzierbarkeitsoption und wird fuer diese Lieferung nicht gesetzt.

Dokumentationsentscheidung: GeneratedUpdate. Kanonische Quellen:
docs/project-statistics.config.json und committierte Git-Historie;
Renderer: scripts/render-project-statistics.sh/.ps1; Ausgabe:
docs/project-statistics.md. Owner: Repository-Maintainer. Zielgruppe:
Maintainer und Lesende der Projekttransparenz; bestehender Leserpfad und
Navigation bleiben gueltig. Deutsch/Englisch gemeinsam pruefen. Source-only,
kein Home-Sync. Nach neuen Quellcommits oder Datumswechsel vor dem Merge die
Vorschau und Driftpruefung wiederholen. Zahlen zeigen sichtbare Lieferdichte,
keine gemessene Arbeitszeit oder Lernleistung. Historische Ledger-Eintraege,
optionales Pilotprofil, Renderer, Konfiguration und Runtime bleiben erhalten.
Vor Merge werden die exakten Head-Checks ausgewertet; Abschlussdaten werden
im Chat und lokalem Schlussprotokoll ergaenzt, ohne selbstreferenziellen Commit.

Planstatus: P1-1 partial (Wartungs-/Auditspur); andere Planaufgaben wegen des
begrenzten Auftrags nicht bearbeiten. P1-4, formelle Freigaben und operative
Aktivierung bleiben separat. TinyPl0 #118 bleibt zurueckgestellt.

EN: The owner authorized repair of statistics drift and MergeAndSync delivery
with admin bypass after green technical checks. The clean source commit above
reproduces exit 1. The unchanged renderer returns identical volume metrics and
measurement source 74dfc73a9408; only the period end, current day cell and
bilingual text alternative advance from 9 to 10 November 2026. PR #131 was
rendered on 9 November and merged on 10 November. Normal operation uses the
current Europe/Berlin date. SOURCE_DATE_EPOCH remains the documented
reproducibility option and is not set for this delivery.

Documentation impact: GeneratedUpdate. Canonical sources are the existing
statistics configuration and committed Git history; render through the Bash/
PowerShell renderer into docs/project-statistics.md. Owner: repository
maintainer. Audience: maintainers and project-transparency readers; retain
reader paths and navigation. Verify equivalent German/English text. Source-
only, no Home sync. Re-run preview and drift validation before merge after
source commits or a date rollover. Figures show observable delivery density,
not measured work time or learning outcomes. Preserve history, optional pilot,
renderer, configuration and runtime. Exact-head CI is required before merge;
record final delivery evidence without a self-referential extra commit.

Plan status: P1-1 partial (maintenance/audit evidence). Other plan work is out
of scope. P1-4, formal approval and operational activation remain separate.
TinyPl0 #118 remains deferred.
