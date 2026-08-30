# Artefaktvertrag: Container-Haertung / Artefact Contract: Container Hardening

## Vertragszweck / Contract Purpose

**DE:** Dieser Vertrag bindet die spaeteren dateibasierten Ergebnisse. JSON ist
kanonisch; Markdown erklaert dieselben Zustaende fuer Menschen. Keine Datei
erteilt Implementierungs-, Liefer-, Risiko- oder Human-only-Autoritaet.

**EN:** This contract binds later file-based results. JSON is canonical;
Markdown explains the same states to people. No file grants implementation,
delivery, risk, or human-only authority.

## Feste Pfade / Fixed Paths

Kanonische Ausgabe: / Canonical output:

`docs/security/secure-development/2026-08-30-container-hardening/`

| Datei / File | Rolle / Role |
|---|---|
| `README.md` | DE-first/EN-second reader route, terms, scope, limits, and commands. |
| `gap-dispositions.json` | Exactly 157 canonical gap dispositions. |
| `verification-evidence.json` | Executed gates, freshness, runner/platform, exit codes, and summary. |
| `learner-first-use-results.json` | Dated, non-sensitive human evidence for SC-009; no participant names or raw notes. |
| `build-provenance.json` | Local source/build/image/SBOM binding; no invented SLSA level. |
| `vulnerability-findings.json` | Scanner observations bound to image and SBOM. |
| `vex.cdx.json` | CycloneDX-compatible VEX decisions or explicit open blockers. |
| `human-only-handoffs.md` | Readable handoff for exactly 49 Human-only gaps. |

Weitere Architecture-/Security-Dokumente duerfen eigene Pfade besitzen, werden
aber aus `README.md` und jeder betroffenen Gap-Disposition verlinkt. / Other
architecture/security documents are linked from the reader route and gaps.

## Gap-Regeln / Gap Rules

1. `gap-dispositions.json` validiert strukturell gegen
   `gap-dispositions.schema.json`.
2. Der Semantikvalidator vergleicht gegen die akzeptierte
   `assessment-results.json`: exakt `GAP-001` bis `GAP-157`, gleiche CL-IDs,
   Prioritaet und Human-only-Zuordnung.
3. Genau 157 Eintraege, 108 agentisch, 49 Human-only; keine fehlende,
   doppelte oder extra ID.
4. Statuskombinationen folgen FR-001 in fester Reihenfolge.
5. `AlreadySatisfied` und `Fulfilled` benoetigen mindestens eine aktuelle
   reproduzierbare Evidenz nach der letzten Subject-Aenderung.
6. `N/A` benoetigt Sachgrund und ereignisbezogenen Trigger;
   fehlende/alte/uebersprungene Evidenz ist nie `N/A`.
7. Alle 49 Human-only-Gaps bleiben ohne datierten Rollenbeleg `Open`,
   `Not Assessed`, `Unassessed`.
8. Jeder geaenderte Repository-Pfad erscheint in mindestens einer Disposition
   mit Gap- und Requirement-ID. Phasen-/Gate-Evidenz darf als eigener
   zwingender Scope gemappt werden.

## Evidenzregeln / Evidence Rules

`verification-evidence.json` validiert gegen
`verification-evidence.schema.json` und erfuellt zusaetzlich:

- alle Gate-IDs aus `autonomous-run-gate-requirements.json` genau einmal;
- Applicable: tatsaechlicher Command- und Runner/Platform-String enthaelt alle
  deklarierten Tokens;
- N/A: kein erfundener Lauf; `command` und `runnerOrPlatform` sind `N/A`,
  `exitCode` ist `null`, `result`/`freshness` sind `N/A`, und Begruendung sowie
  Trigger stimmen exakt;
- `Pass` nur mit Exitcode 0 und beobachtetem Ergebnis;
- `Current` nur nach letzter Subject-Aenderung und mit Source-/Image-Bindung;
- keine Secret-, Prompt-/Antwort-, Provider-/Account- oder private Endpoint-
  Inhalte;
- uebersprungene oder nicht verfuegbare Plattform bleibt `Blocked`/`Open`.

`learner-first-use-results.json` wird semantisch zusammen mit der Gate-Evidenz
validiert. Owner ist `Learning/A11Y Review`; erfasst werden nur Anzahl,
Erfolgsanzahl, Prozentwert, Abdeckung der vier Zielberufe, fehlende
Spec-Kit-Vorerfahrung, 30-Minuten-Grenze, Methode, Limitierungen und Trigger.
Der Agent darf den Datensatz nicht erzeugen oder positive Beobachtungen
erfinden. Fehlende oder unzureichende menschliche Evidenz blockiert
`GATE-LEARNER-01`, ohne die 49 akzeptierten Human-only-Gaps umzuklassifizieren.
/ Learner evidence is human-produced, non-sensitive, and agent-validated only.

## Supply-Chain-Regeln / Supply-Chain Rules

- Genau eine finale lokale Image-Identitaet bindet Provenienz, SBOM, Scan und
  VEX.
- SBOM-Rohdateien duerfen ungetrackt bleiben; Hash, Werkzeugversion,
  Erzeugungszeit und Image-ID stehen in getrackter Evidenz.
- Jeder relevante Scan-Fund hat genau einen VEX-Status oder offenen Blocker.
- `not affected`/`mitigated` benoetigt technische Begruendung und Reviewer.
- Keine Registry-Publikation, Signatur- oder SLSA-Level-Behauptung ohne echte
  externe Evidenz.
- AI-SBOM ist N/A mit Trigger, solange kein KI-Runtime-Bestandteil ausgeliefert
  oder betrieben wird.

## Menschenlesbare Projektionen / Human-Readable Projections

Markdown ist Deutsch zuerst und Englisch danach, ungefaehr CEFR B2. Jeder
Status, jede Abhaengigkeit, Entscheidung, Grenze und naechste Aktion ist als
Text vorhanden. Tabellen werden in kleine thematische Abschnitte geteilt;
Symbole/Farbe sind nie alleinige Information. Fachbegriffe werden beim ersten
Auftreten erklaert und Spec-Kit-Erfahrung wird nicht vorausgesetzt.

## Validierungsreihenfolge / Validation Order

Input -> Gap contract -> RED baseline -> targeted GREEN -> static config ->
final build -> runtime/smoke -> final SBOM/scan/VEX/provenance -> docs/A11Y/
learner/secret/parity -> final 157/108/49 reconciliation -> read-only delivery
set -> content commit -> separate statistics commit -> revalidate affected
gates -> temporary exact-head PreMerge -> authorized provider merge and
default-branch sync -> causal PostMerge -> final validation.

Ein spaeteres Gate darf kein frueheres Gate ersetzen oder dessen Erfolg
voraussetzen. Eine nicht verfuegbare Linux- oder Windows/WSL2-Plattform bleibt
am Gap offen und blockiert zugleich ihr Applicable-Gate sowie einen positiven
`MergeAndSync`-Abschluss. PreMerge-Evidenz wird nicht committet; PostMerge
bindet ihren normalisierten Hash und den realen Merge-Commit mit leeren
`changedPaths`. / A later gate may not replace an earlier gate; unavailable
binding platforms fail closed, and exact-head evidence follows the stated
temporary PreMerge and causal PostMerge contract.

Der fuer diesen Run bereits autorisierte Admin-Bypass ist ausschliesslich eine
Option der Provider-Merge-Operation, wenn `REVIEW_REQUIRED` nach allen gruenen
technischen Gates, null handlungsrelevanten Review-Threads und gueltiger
Schema-2.0-PreMerge-Evidenz der einzige Policy-Blocker ist. Er darf weder ein
fehlgeschlagenes, ausstehendes, fehlendes, veraltetes oder widerspruechliches
technisches/Security-Gate noch eine Repository-Regel umgehen. / The already
authorized Admin-Bypass is solely a provider-merge option when
`REVIEW_REQUIRED` is the only policy blocker after all-green technical gates,
zero actionable review threads, and valid schema-2.0 PreMerge evidence. It may
not bypass any failed, pending, missing, stale, or contradictory
technical/security gate or repository rule.
