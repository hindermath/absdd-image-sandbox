# Lastenheft: Sandbox Public Readiness

**Dokumenttyp:** Spec-Kit Intake / Lastenheft  
**Status:** Vorbereitung fuer spaeteren Spec-Kit-Lauf, kein gestarteter Lauf  
**Repository:** absdd-image-sandbox  
**Zielgruppe:** Fachinformatiker*innen in Ausbildung, Entwickler*innen, Reviewer und KI-Agenten

## Ziel / Goal

Dieses Lastenheft beschreibt einen spaeteren Spec-Kit-Lauf, der `absdd-image-sandbox` auf eine oeffentlich nutzbare Ausbildungs-Sandbox vorbereitet. Interne oder organisationsspezifische Formulierungen werden in generische Sprache ueberfuehrt.

*This intake describes a later Spec Kit run that prepares `absdd-image-sandbox` as a public-ready training sandbox. Internal or organization-specific wording is converted into generic language.*

## Scope

- README, Agenten-Dateien, Compliance-/Security-Dokumente und Lastenhefte auf generische Sprache pruefen.
- Private Pfade, private URLs, organisationsgebundene Rollen und nicht verallgemeinerbare Pflichtannahmen entfernen oder neutral formulieren.
- Bestehende Evidence-Dokumente als Lern- und Referenzbeispiele erklaeren.
- `home-baseline` als optionale Governance- und Template-Basis beschreiben, nicht als privaten Pflichtpfad.
- Fachinformatik-Ausbildung, CEFR B2 und WCAG 2.2 AA als Dokumentationsziel beibehalten.

## Nicht-Ziele / Non-Goals

- Kein Umschalten des Repositories auf Public.
- Kein Entfernen fachlich relevanter Sicherheitsanforderungen.
- Kein Container-Build.
- Keine technische Haertung des Images.
- Keine Aenderung an Secrets, Providern oder Modellzugriffen.

## Anforderungen / Requirements

1. Organisationsspezifische Formulierungen werden generisch formuliert.
2. Lernende muessen verstehen, welche Dokumente Beispiele sind und welche Regeln aktuell gelten.
3. Sicherheitsdokumente bleiben auditfaehig, aber ohne unnoetige Bindung an eine konkrete Organisation.
4. Public-Readiness-Pruefung dokumentiert offene Punkte als `Open`, nicht als erledigt.
5. Kein Dokument darf private Host-Pfade oder nicht oeffentliche Zugangsdaten voraussetzen.

## Akzeptanzkriterien / Acceptance Criteria

- README beschreibt die Sandbox als Lern- und Arbeitsumgebung fuer sichere Entwicklung.
- Agenten-Dateien verweisen auf generische Regeln statt organisationsspezifischer Pflichtsprache.
- `docs/security/` bleibt als Evidence-Beispiel nutzbar.
- Offene Freigabe-, Provider- oder Rechtsfragen sind als `_TODO_`, `Open` oder `N/A` mit Begruendung sichtbar.

## Optimaler Spec-Kit Specify Prompt

```text
/speckit-specify Nutze Lastenheft_Sandbox-Public-Readiness.md als verbindliche Eingabedatei. Erstelle die Feature-Spezifikation fuer die Public-Readiness von absdd-image-sandbox als Ausbildungs-Sandbox.

Ziel: Interne oder organisationsspezifische Formulierungen in generische Sprache ueberfuehren, ohne Sicherheitsanforderungen zu verwaessern. Das Repo soll perspektivisch fuer Fachinformatik-Auszubildende oeffentlich nutzbar werden.

Beruecksichtige README, AGENTS.md, CLAUDE.md, GEMINI.md, .github/copilot-instructions.md, COMPLIANCE-PLAN_RL-SE-001.md, docs/security/ und bestehende Lastenhefte. Starte keinen Container-Build und schalte das Repo nicht auf Public.
```