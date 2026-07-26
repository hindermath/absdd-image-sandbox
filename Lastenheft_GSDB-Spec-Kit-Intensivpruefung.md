<!-- intake-authoring:begin -->
# GSDB-Bestandspruefung der Sandbox / GSDB Sandbox Baseline Assessment

**Status:** ReadyForReview

**Zielgruppe / Audience:** Auszubildende ab dem ersten Ausbildungsjahr, Lernbegleitung, Entwicklung und Review

**Lieferautoritaet / Delivery authority:** LocalImplementation

## Zweck / Purpose

**DE:** Dieser Intake fuehrt die bisherigen Anforderungen aus
RL-SE-/Checklist-Selbstpruefung, GSDB-Intensivpruefung und allgemeinem
Secure-Development-Hardening in einer Bestandspruefung zusammen. Die
Generische Secure-Development-Basis (GSDB) ist die wiederverwendbare
Pruefgrundlage unter `docs/secure-development/`.

**EN:** This intake combines the previous RL-SE/checklist self-assessment,
GSDB intensive review, and general secure-development hardening requirements
into one baseline assessment. The Generic Secure Development Baseline (GSDB)
under `docs/secure-development/` is the reusable review basis.

## Ausgangslage und Zielbild / Current and Target State

**DE:** Sicherheitsnachweise, Checklisten und Governance-Regeln sind vorhanden,
aber noch nicht in einer aktuellen, vollstaendigen Anwendbarkeits- und
Evidenzmatrix zusammengefuehrt. Der spaetere Lauf liefert diese Matrix und eine
priorisierte Lueckenliste. Er setzt noch keine technische Haertung um.

**EN:** Security evidence, checklists, and governance rules exist, but they
have not yet been combined into one current applicability and evidence matrix.
The later run produces this matrix and a prioritized gap list. It does not yet
implement technical hardening.

## Scope

- Alle zwoelf GSDB-Checklisten und die mitgeltenden Dokumente pruefen.
- Constitution, installierte Governance-Presets und vorhandene
  `docs/security/`-Nachweise einbeziehen.
- Jeden relevanten Pruefpunkt als `Applicable`, `AlreadySatisfied`, `N/A`,
  `Open` oder `FollowUp` klassifizieren.
- Toolchain-, Agenten-, Lieferketten-, A11Y-, Datenschutz- und
  Plattformanforderungen pruefen.
- Abweichende Angaben zur Zahl installierter Toolchain-Familien gegen
  `Dockerfile` und `scripts/smoke-test-toolchains.sh` klaeren.
- Fuer offene Punkte Prioritaet, Owner, Folgeaktion, Restrisiko und
  Neubewertungs-Trigger festhalten.

## Nicht-Ziele / Non-Goals

- Keine Aenderung an Dockerfile, Compose, Laufzeit oder Hosting-Plattform.
- Keine formale Sandbox-, Provider-, Modell- oder Rechtsfreigabe.
- Keine Secret-Rotation und keine Branch-Protection-Aenderung.
- Keine pauschale Aussage, dass das Projekt sicher oder freigegeben sei.

## Anforderungen / Requirements

1. Kein relevanter GSDB-Pruefpunkt darf stillschweigend fehlen.
2. Positive Bewertungen muessen auf konkrete, repository-lokale Evidenz zeigen.
3. `N/A` braucht eine technische oder fachliche Begruendung.
4. `Open` und `FollowUp` brauchen Owner, Folgeaktion und Trigger.
5. Human-only-Entscheidungen bleiben sichtbar offen.
6. Status, Abhaengigkeiten und Entscheidungen werden textorientiert erklaert.
7. Lernendeninhalte bleiben Deutsch zuerst, Englisch danach und etwa CEFR B2.

## Abhaengigkeiten und Risiken / Dependencies and Risks

**DE:** Dies ist die Wurzel der Sandbox-Intake-Serie. Technische Haertung darf
ihre priorisierte Lueckenliste als Baseline verwenden. Veraltete oder
widerspruechliche Nachweise koennen zu falschen positiven Bewertungen fuehren;
deshalb gilt Evidenz ohne aktuellen Pfad oder reproduzierbaren Check als offen.

**EN:** This is the root of the sandbox intake series. Technical hardening may
use its prioritized gap list as the baseline. Stale or contradictory evidence
can cause false positive assessments, so evidence without a current path or
reproducible check remains open.

## Erwartete Artefakte und Evidenz / Expected Artefacts and Evidence

- Spec-Kit-Spezifikation, Plan und Aufgaben fuer die Bestandspruefung.
- GSDB-Evidenzmatrix mit allen Status- und Verantwortungsfeldern.
- Priorisierte Lueckenliste als Eingabe fuer die technische Haertung.
- Nachweise unter `docs/security/` oder begruendete offene Eintraege.

## Akzeptanzkriterien / Acceptance Criteria

- Alle zwoelf Checklisten sind sichtbar behandelt.
- Jede Bewertung besitzt Begruendung und Evidenzpfad oder Open-Markierung.
- Die tatsaechlich installierten Agenten und Toolchain-Familien sind gegen
  Build- und Smoke-Test-Quellen abgeglichen.
- Human-only-Punkte werden nicht als erledigt behauptet.
- Der Abschluss nennt die freigegebene Eingabe fuer den Folge-Intake, startet
  ihn aber nicht automatisch.

## Annahmen und offene Fragen / Assumptions and Open Questions

- Die GSDB im Repository ist die fachliche Basis; externe Managementsysteme
  sind nicht Teil dieses Laufs.
- Es bestehen keine offenen Intake-Authoring-Fragen.

<!-- intake-authoring:prompts -->
## Kopierbare Folgekommandos / Copy-Ready Follow-Up Commands

<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Erstelle eine Spezifikation ausschliesslich auf Grundlage von Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md. Erzeuge eine vollstaendige GSDB-Bestandspruefung mit Evidenzmatrix und priorisierter Lueckenliste. Beginne keine technische Haertung und fuehre keine Remote-Aktion aus.
```

<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Fuehre den vollstaendigen Spec-Kit-Lauf fuer Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md mit Delivery Authority LocalImplementation aus. Bearbeite nur die Bestandspruefung, bewahre alle Human-only-Grenzen und stoppe vor Commit, Push, Pull Request, Merge oder Hosting-Aenderungen.
```
<!-- intake-authoring:end -->
