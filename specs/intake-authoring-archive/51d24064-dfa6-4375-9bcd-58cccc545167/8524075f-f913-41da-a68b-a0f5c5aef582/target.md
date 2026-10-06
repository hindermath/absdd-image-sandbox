<!-- intake-authoring:begin -->
# Sandbox-Abnahme / Sandbox Acceptance Review

**Status:** ReadyForReview

**Zielgruppe / Audience:** Auszubildende, Lernbegleitung, Betrieb und unabhaengiges Review

**Lieferautoritaet / Delivery authority:** LocalImplementation

## Zweck / Purpose

**DE:** Dieser Intake prueft die technisch gehaertete Sandbox unabhaengig auf
Sicherheit, Reproduzierbarkeit und praktische Arbeitsfaehigkeit. Eine
Abnahme bedeutet technische Evidenz, nicht die formale Freigabe durch eine
Organisation.

**EN:** This intake independently checks the technically hardened sandbox for
security, reproducibility, and practical usability. Acceptance means technical
evidence, not formal approval by an organization.

## Ausgangslage und Zielbild / Current and Target State

**DE:** Die technische Haertung ist abgeschlossen und liefert ein finales
lokales Image sowie aktualisierte Nachweise. Die Abnahme wiederholt statische
und praktische Pruefungen aus Sicht von Lernenden und Reviewenden.

**EN:** Technical hardening is complete and provides a final local image and
updated evidence. Acceptance repeats static and practical checks from learner
and reviewer perspectives.

## Scope

- Rootless-Isolation, Capabilities, Mounts, Schreib- und Netzwerkgrenzen.
- OpenCode, Codex, Claude Code, Antigravity CLI und GitHub Copilot CLI.
- Die im Dockerfile und Smoke-Test tatsaechlich installierten
  Toolchain-Familien, einschliesslich Swift.
- VS-Code-Verbindung, SourceKit-LSP und dokumentierte Projekt-Mappings.
- Image-Build, Compose-Start, praktische Projekt-Smoke-Tests und HTTP-Zugriff.
- SBOM-Erzeugung sowie Konsistenz der Security-Evidenz.
- Lernbarkeit, DE-first/EN-second, CEFR B2 und WCAG 2.2 AA.

## Nicht-Ziele / Non-Goals

- Keine weitere Haertung waehrend der unabhaengigen Abnahme.
- Keine Ausweitung auf nur geplante oder nicht installierte Sprachen.
- Keine Anmeldung mit echten Provider-Secrets als Abnahmevoraussetzung.
- Keine formale Sandbox-, Rechts-, Provider- oder Modellfreigabe.

## Anforderungen / Requirements

1. Jede Pruefung nennt Befehl, erwartetes Ergebnis und Evidenzpfad.
2. Toolchain- und Agentenstatus werden aus Build- und Laufzeitquellen abgeleitet.
3. Fehler werden als Befund an die technische Haertung zurueckgegeben.
4. Plattformabdeckung wird ehrlich als geprueft, uebersprungen oder offen
   dokumentiert.
5. Sicherheitsrestriktionen und Lernablauf werden gemeinsam bewertet.
6. Keine positive Bewertung darf allein auf Dokumentation ohne praktischen
   Nachweis beruhen, wenn ein lokaler Check moeglich ist.

## Abhaengigkeiten und Risiken / Dependencies and Risks

**DE:** Die technische Sandbox-Haertung muss abgeschlossen sein. Lokale
Podman-, Netzwerk- oder Plattformausfaelle werden von Repository-Fehlern
getrennt dokumentiert. Nur auf macOS ausgefuehrte Checks belegen keine
vollstaendige Windows- oder Linux-Abdeckung.

**EN:** Technical sandbox hardening must be complete. Local Podman, network, or
platform failures are recorded separately from repository failures. Checks run
only on macOS do not prove full Windows or Linux coverage.

## Erwartete Artefakte und Evidenz / Expected Artefacts and Evidence

- Abnahmeprotokoll mit Pass, Fail, Open oder N/A je Pruefung.
- Toolchain-, Agenten-, Mount- und VS-Code-Matrix.
- Finale lokale SBOM und reproduzierbare Pruefbefehle.
- Rueckgabe konkreter Befunde an die Haertungsstufe.

## Akzeptanzkriterien / Acceptance Criteria

- Compose-Konfiguration, Image-Build und Containerstart sind nachweisbar.
- Alle installierten Agenten und Toolchain-Familien bestehen die vorgesehenen
  Versions- und Projekt-Smoke-Tests.
- VS Code kann gemaess Dokumentation an den Container anbinden.
- Mounts zeigen auf die dokumentierten Containerpfade.
- SBOM-Erzeugung ist erfolgreich oder ein konkreter externer Blocker ist
  dokumentiert.
- Die Selbstbau-Vorlage wird erst nach erfolgreicher technischer Abnahme
  freigegeben.

## Annahmen und offene Fragen / Assumptions and Open Questions

- Provider-Anmeldungen sind fuer Versions- und Konfigurationschecks nicht
  erforderlich.
- Es bestehen keine offenen Intake-Authoring-Fragen.

<!-- intake-authoring:prompts -->
## Kopierbare Folgekommandos / Copy-Ready Follow-Up Commands

<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Erstelle eine Spezifikation ausschliesslich auf Grundlage von Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md und den Ergebnissen der technischen Haertung. Plane eine unabhaengige technische Abnahme ohne weitere Haertung oder formale Freigabe.
```

<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Fuehre den vollstaendigen Spec-Kit-Lauf fuer Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md mit Delivery Authority LocalImplementation aus. Pruefe die Sandbox lokal, dokumentiere Plattformgrenzen ehrlich und stoppe vor Commit, Push, Pull Request, Merge oder Hosting-Aenderungen.
```
<!-- intake-authoring:end -->
