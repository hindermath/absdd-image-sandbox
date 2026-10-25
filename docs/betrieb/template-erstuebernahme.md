# Erstübernahme einer Template-Kopie / Template Copy Handover

## Deutsch

Manuelle Checkliste für eine spätere persönliche Kopie, **kein ausführendes
Bootstrap-Skript**. Bei unklaren Rechten oder Governance stoppen. Keine
automatische Bereinigung, Git-Konfiguration, Reinitialisierung oder Freigabe.

- [ ] Herkunft: Vorlagen-URL ohne Zugangsdaten, Referenz-Commit und Zeitpunkt
  der Übernahme festhalten; persönliches `origin` mit `git remote -v` prüfen.
- [ ] Rechte: eigene MIT-Anteile und fremde Hinweise unterscheiden. LIC-01/02
  und die Vorlagenfreigabe prüfen; keine ungeklärten Inhalte weiterverteilen.
- [ ] Rollen: persönlichen Owner/Reviewer festlegen, CODEOWNERS in eigenem
  Branch prüfen und nach aktuellem Review anpassen. Referenz-Owner nicht als
  zuständige Person im neuen Repo behaupten.
- [ ] Referenzkontext: kopierte `specs/`, Receipts, Reviews, Session-Logs,
  GSDB-Matrizen, Statistiken und Run-States als Quelle inventarisieren. Nicht
  löschen, auf Pending umschreiben oder als aktuelle persönliche Nachweise behandeln.
- [ ] Agenten: vor automatischer Arbeit die gemeinsame Guidance lesen. Keine
  Referenz-Workqueue oder Autonomous-Resume starten. Eigene Anforderungen,
  Baseline und aktuelle persönliche Autorität getrennt herstellen und reviewen.
- [ ] Statistik: bisherige Messungen bleiben historisch. Eigenen Reponamen
  und eine neue persönliche Messbasis über den vorgesehenen Statistik-Init-
  Weg einrichten; Quellberichte nicht als eigene Geschwindigkeit ausgeben.
- [ ] CI: allgemeine Secret-/Pinning-/Syntax-/Regressionsprüfungen behalten.
  Referenzgebundene historische Proof-Jobs sind kein persönlicher Nachweis;
  erforderliche persönliche Gates explizit festlegen und nachweisen, nicht
  durch pauschales Überspringen grün machen.
- [ ] Hosting: Rulesets, Required Checks, Reviewrechte, Actions-Berechtigungen
  und Secrets im tatsächlichen Ziel prüfen. Keine automatische Plattformänderung.
- [ ] Betrieb: lokale Konfiguration/Mounts, Plattform und Architektur prüfen,
  dann Selbstbau, Smoke-Tests und SBOM separat beauftragen. Keine Registry-
  Veröffentlichung und keine Containeraktion durch diese Checkliste.
- [ ] Produktlernen: SysInfo/Web in ein getrenntes leeres Produktrepo legen;
  dort genau ein Paket übernehmen, persönlich entscheiden, reviewen und aktivieren.

Eine Kopie ist nicht übernahmebereit, solange anwendbare Punkte ungeklärt
sind. Open: persönlicher Repository Owner; Follow-up fehlende Zuordnungen und
Belege ergänzen; Trigger vor Agentenautomation oder Weitergabe. Kein Haken
wird durch die Existenz dieser Datei gesetzt.

## English

Manual checklist for a future personal copy, not a bootstrap script. Record
safe source URL/commit/time and personal origin; inspect license boundaries;
choose real local reviewers/CODEOWNERS; inventory copied evidence and states
as source context without deleting or resetting them. Do not resume reference
workqueues. Establish personal requirements, baseline and authority separately.

Preserve old statistics as history and initialize a personal measurement basis.
Keep general security/pin/syntax/regression checks. Source-only historical jobs
are not personal proof; establish applicable personal gates rather than blanket
skips. Inspect real hosting rules, reviewers, Actions and secrets separately.
Prepare limited local mounts; authorize self-build, smoke checks and SBOM
separately. Product exercises use separate empty repos and one reviewed package.

Any unresolved applicable item blocks handover: owner personal Repository Owner,
follow up with missing evidence before automation or redistribution. No check
is marked complete by shipping this document. No configuration or runtime
operation is performed automatically.
