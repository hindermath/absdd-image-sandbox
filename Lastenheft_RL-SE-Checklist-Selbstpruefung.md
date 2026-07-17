# Lastenheft: RL-SE-Checklist-Selbstpruefung

**Dokumenttyp:** Spec-Kit Intake / Lastenheft
**Status:** Vorbereitung fuer spaeteren manuellen Spec-Kit-Lauf, kein gestarteter Lauf
**Repository:** absdd-image-sandbox
**Zielgruppe:** Fachinformatiker*innen in Ausbildung, Entwickler*innen, Reviewer und KI-Agenten

## Ziel / Goal

Dieses Lastenheft beschreibt einen spaeteren Spec-Kit-Lauf, der
`absdd-image-sandbox` gegen die generische Secure-Development-Basis prueft.
Der Lauf soll die Richtlinie Sichere Entwicklung, die zwoelf Checklisten, den
Checklistensammelband, die mitgeltenden Dokumente und die sechs Governance-
Presets in eine konkrete, projektspezifische Evidenzmatrix ueberfuehren.

*This intake describes a later Spec Kit run that reviews `absdd-image-sandbox`
against the generic secure-development baseline. The run should turn the Secure
Development Guideline, the twelve checklists, the checklist compendium, related
documents, and the seven governance presets into concrete project-specific
evidence.*

## Ausgangslage / Context

Die Secure-Development-Basis liegt fuer dieses Repository lokal unter
`docs/secure-development/`. Eine uebergeordnete Template- oder Baseline-Quelle
kann projektspezifisch existieren, ist aber fuer public-ready Leserinnen und
Leser keine Voraussetzung. Die lokale Basis enthaelt:

- `Richtlinie_Sichere-Entwicklung.md`
- `Checklistensammelband_Sichere-Entwicklung.md`
- `checklisten/CL_01_Standards-Anwendbarkeit.md` bis
  `checklisten/CL_12_Agentische-KI-Sandbox.md`
- `mitgeltende-dokumente/`
- `mitgeltende-dokumente/Verzahnung_Richtlinie_Checklisten_Spec-Kit-Presets.md`

`absdd-image-sandbox` enthaelt bereits eigene Sicherheits- und Audit-
Artefakte, unter anderem `COMPLIANCE-PLAN_RL-SE-001.md`, `docs/security/`,
Agent-Guidance-Dateien und Spec-Kit-Artefakte. Diese projektspezifischen
Nachweise muessen gegen die zentrale Secure-Development-Basis eingeordnet
werden.

Die Basis ist als generische Ausbildungs-, Review- und Pruefgrundlage zu
behandeln. Sie ist keine Firmenrichtlinie und kein konkretes
Managementsystem-Artefakt. Generische Rollen wie Organisation,
Projektverantwortliche, Security-Review, CISO/ISB/KIB, Dokumentenablage,
Risikoregister, RoPA, Provider oder Plattform sind Platzhalter. Konkrete
Firmen, private URLs, lokale Hostpfade, Provider-Portale, accountgebundene
Defaults, externe DMS-/QISMS-Systeme oder Plattformregeln muessen im spaeteren
Lauf entfernt, generalisiert oder als Beispiel, Kontext, `N/A`, `Open` oder
projektspezifische Evidenz klassifiziert werden.

## Scope

- Anwendbarkeit von RL Sichere Entwicklung, CL_01 bis CL_12,
  Checklistensammelband und mitgeltenden Dokumenten fuer dieses Repo bewerten.
- Die sieben Governance-Presets als Spec-Kit-Nachweisflaeche gegen die
  einschlaegigen RL-/CL-Pruefpunkte mappen.
- Bestehende Projektnachweise in `docs/security/`,
  `COMPLIANCE-PLAN_RL-SE-001.md`, `README.md`, Agent-Guidance-Dateien,
  Compose-Dateien, Dockerfile, Spec-Kit-Artefakten und Lastenheften auswerten.
- Fuer jeden relevanten Pruefpunkt einen Status `Applicable`, `N/A` oder
  `Open` dokumentieren.
- Firmen-, system- und managementsystem-spezifische Treffer neutralisieren
  oder nachvollziehbar klassifizieren.
- Offene Punkte mit Owner, Follow-up, Evidenzpfad und Re-Evaluation-Trigger
  planen.
- Human-only-Entscheidungen klar markieren und nicht als erledigt behaupten.

## Nicht-Ziele / Non-Goals

- Keinen Spec-Kit-Lauf durch dieses Lastenheft automatisch starten.
- Keinen Container bauen und kein Image veroeffentlichen.
- Repository-Sichtbarkeit nicht aendern.
- Keine formale Sandbox-Freigabe, Rechtsfreigabe, Providerfreigabe oder
  Public-Release-Freigabe erfinden.
- Keine Secrets, Provider, Modelle oder Endpunkte konfigurieren.
- Keine Plattformregeln wie Branch Protection, Push Rules oder externe Managementsystem-Eintraege
  als agentisch erledigt markieren.
- Keine vollstaendige Kopie der Level-0-Secure-Development-Basis ohne
  Provenienz-, Lizenz- und Public-Readiness-Pruefung uebernehmen.

## Anforderungen / Requirements

1. Der spaetere Lauf erstellt oder plant eine RL-/CL-Evidenzmatrix fuer
   `absdd-image-sandbox`.
2. Jeder Pruefpunkt enthaelt mindestens Status, Begruendung, Evidenzpfad oder
   `Open`-Markierung, Owner, Follow-up und Re-Evaluation-Trigger.
3. `N/A` ist nur mit konkreter technischer oder fachlicher Begruendung erlaubt.
4. `Open` enthaelt eine naechste Massnahme und darf nicht als Freigabe gelten.
5. Bestehende Sicherheitsanforderungen werden nicht abgeschwaecht, sondern
   oeffentlichkeitsfaehig, generisch und auditierbar eingeordnet.
6. Die Pruefung trennt Entwicklungswerkzeug-KI von ausgelieferten oder
   betriebenen KI-Komponenten; AI-SBOM bleibt konditional.
7. Die Pruefung dokumentiert, ob eine lokale Snapshot-Kopie der
   Secure-Development-Basis im Sandbox-Repo sinnvoll ist, und welche Dateien
   aus Lizenz-, Public-Readiness- oder Binaerartefakt-Gruenden ausgeschlossen
   bleiben sollen.
8. Die Pruefung verwendet die Bezeichnung "generische Secure-Development-Basis"
   und vermeidet Begriffe wie Firmenrichtlinie, interne Richtlinie oder
   konkretes QISMS-Artefakt, sofern sie nicht als historischer Kontext oder
   projektspezifische Evidenz markiert sind.

## Erwartete Artefakte / Expected Artefacts

- `specs/<feature>/spec.md` fuer die RL-SE-/CL-Selbstpruefung.
- `specs/<feature>/plan.md` mit Governance-, Sicherheits-, A11Y-,
  Cross-Platform- und Agent-Parity-Gates.
- `specs/<feature>/data-model.md` fuer Evidenz- und Pruefobjekte, falls fuer
  die Planung sinnvoll.
- `specs/<feature>/quickstart.md` mit reinen Validierungsbefehlen.
- Geplante oder erstellte Projektnachweise unter `docs/security/`, zum
  Beispiel:
  - `docs/security/rl-se-self-assessment.md`
  - `docs/security/rl-se-checklist-matrix.md`
  - `docs/security/rl-se-related-documents-mapping.md`
  - `docs/security/spec-kit-preset-evidence-matrix.md`

## Akzeptanzkriterien / Acceptance Criteria

- Die spaetere Spezifikation beschreibt die Pruefung als Dokumentations- und
  Governance-Feature, nicht als Runtime-Feature.
- CL_12, CL_10, CL_05 und CL_09 werden explizit bewertet.
- CL_01, CL_02, CL_04 und CL_08 werden mindestens als Governance- oder
  Review-Pruefflaechen eingeordnet.
- CL_03, CL_06, CL_07 und CL_11 werden nicht geloescht, sondern als
  `Applicable`, `N/A` oder `Open` begruendet.
- Human-only-Punkte sind sichtbar eskaliert und nicht als erledigt markiert.
- Keine Behauptung entsteht, dass die Sandbox formal freigegeben, rechtlich
  geprueft, providerseitig genehmigt oder bereits oeffentlich veroeffentlicht
  ist.
- Die Validierung nutzt `podman-compose config` fuer statische Compose-
  Pruefung; kein Container-Build ist Teil dieses Lastenhefts.

## Optimaler Spec-Kit Specify Prompt

```text
Nutze Lastenheft_RL-SE-Checklist-Selbstpruefung.md als verbindliche Eingabedatei. Erstelle die Feature-Spezifikation fuer eine RL-SE-/Checklist-Selbstpruefung von absdd-image-sandbox.

Ziel: Pruefe absdd-image-sandbox als Ausbildungs-Sandbox gegen die generische Secure-Development-Basis aus docs/secure-development/. Beruecksichtige Richtlinie_Sichere-Entwicklung.md, Checklistensammelband_Sichere-Entwicklung.md, CL_01 bis CL_12, mitgeltende Dokumente, Verzahnung_Richtlinie_Checklisten_Spec-Kit-Presets.md und die sieben Governance-Presets.

Neutralitaet: Behandle die Richtlinie, Checklisten, den Sammelband und die mitgeltenden Dokumente als generische Ausbildungs-, Review- und Pruefgrundlage, nicht als Firmenrichtlinie oder konkretes Managementsystem-Artefakt. Konkrete Firmen, private URLs, lokale Hostpfade, Provider-Portale, accountgebundene Defaults, externe DMS-/QISMS-Systeme oder Plattformregeln muessen entfernt, generalisiert oder als Beispiel, Kontext, `N/A`, `Open` oder projektspezifische Evidenz klassifiziert werden.

Erzeuge eine projektspezifische Evidenz- und Anwendbarkeitslogik mit `Applicable`, `N/A` und `Open`. Jeder relevante Pruefpunkt braucht Begruendung, Evidenzpfad oder Open-Markierung, Owner, Follow-up und Re-Evaluation-Trigger. Human-only-Punkte wie formale Freigabe, externe Managementsystem-Eintraege, Plattform-Branch-Protection, Secrets, Provider und Modellfreigaben duerfen nicht als erledigt behauptet werden.

Beruecksichtige README, AGENTS.md, CLAUDE.md, GEMINI.md, .github/copilot-instructions.md, COMPLIANCE-PLAN_RL-SE-001.md, docs/security/, Dockerfile, compose.yml, compose.home-baseline.yml, bestehende Lastenhefte und bestehende Spec-Kit-Artefakte.

Technische Einordnung: Dokumentations-/Governance-Feature, keine Anwendung, kein Runtime-Code, keine Datenbank, keine API. Falls eine lokale Snapshot-Kopie der Secure-Development-Basis im Sandbox-Repo geplant wird, dokumentiere Quelle, Lizenz, Commit-SHA, ausgeschlossene Dateien und Public-Readiness-Pruefung. Starte keinen Container-Build, schalte das Repo nicht auf Public und konfiguriere keine Secrets, Provider oder Modelle.
```
