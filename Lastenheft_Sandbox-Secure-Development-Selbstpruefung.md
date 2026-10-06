<!-- intake-authoring:begin -->
# Sandbox-Abnahme / Sandbox Acceptance Review

**Status:** ReadyForReview

**Zielgruppe / Audience:** Auszubildende, Lernbegleitung, Betrieb und unabhaengiges Review

**Lieferautoritaet / Delivery authority:** LocalImplementation

## Voraussetzungen und Begriffe / Prerequisites and Terms

**DE:** Ein Intake ist eine Anforderungsdatei vor einem Spec-Kit-Lauf; Spec Kit
ordnet Anforderungen, Planung und Aufgaben. Grundlegende Computer- und
Terminalbedienung genuegt; Container-, Sicherheits- oder Spec-Kit-Erfahrung
wird nicht vorausgesetzt. Die Zielgruppe ab dem ersten Ausbildungsjahr
umfasst Fachinformatiker*innen, IT-System-Elektroniker*innen und die beiden
kaufmaennischen IT-Ausbildungsberufe. LocalImplementation bedeutet lokale
Umsetzung ohne automatische Liefer- oder Plattformaenderungsautoritaet.

**EN:** An intake is a requirements file before a Spec Kit run; Spec Kit
organizes requirements, planning and tasks. Basic computer and terminal use
is sufficient; no container, security or Spec Kit experience is assumed.
The first-year audience includes IT specialists, IT systems electronics
technicians and both IT management training occupations. LocalImplementation
means local work without automatic delivery or platform-change authority.

**DE:** Podman betreibt Container (isolierte Arbeitsumgebungen); ein Image ist
deren Bauvorlage. Rootless bedeutet Betrieb ohne Administratorrechte;
Capabilities sind einzelne Linux-Rechte, Mounts eingebundene Verzeichnisse.
Eine CLI ist ein Kommandozeilenwerkzeug, eine Toolchain eine Gruppe von
Entwicklungswerkzeugen. LSP (Language Server Protocol) verbindet Editor und
Sprachwerkzeuge; SourceKit-LSP ist das entsprechende Swift-Werkzeug.
Ein Smoke-Test ist ein kleiner Funktionstest. Compose beschreibt und startet
Container gemeinsam; HTTP ist das Protokoll fuer Webzugriff. Eine SBOM
(Software Bill of Materials) listet Softwarebestandteile. DE-first/EN-second
bedeutet Deutsch vor Englisch, CEFR B2 bezeichnet eine mittlere sprachliche
Komplexitaet, WCAG 2.2 AA die anwendbare Barrierefreiheits-Pruefbasis.

**EN:** Podman runs containers (isolated work environments); an image is their
build template. Rootless operation needs no administrator privileges;
capabilities are individual Linux permissions and mounts connect directories.
A CLI is a command-line tool; a toolchain groups development tools. Language
Server Protocol (LSP) connects editors and language tools; SourceKit-LSP is
the Swift tool. A smoke test is a small functional check. Compose describes
and starts containers together; HTTP is the web access protocol. A Software
Bill of Materials (SBOM) lists software components. DE-first/EN-second means
German before English, CEFR B2 indicates moderate language complexity, and
WCAG 2.2 AA is the applicable accessibility review baseline.

## Zweck / Purpose

**DE:** Dieser Intake prueft die technisch gehaertete Sandbox unabhaengig auf
Sicherheit, Reproduzierbarkeit und praktische Arbeitsfaehigkeit. Eine
Abnahme bedeutet technische Evidenz, nicht die formale Freigabe durch eine
Organisation.

**EN:** This intake independently checks the technically hardened sandbox for
security, reproducibility, and practical usability. Acceptance means technical
evidence, not formal approval by an organization.

## Ausgangslage und Zielbild / Current and Target State

**DE:** Zum Start dieser Abnahme muss die technische Haertung abgeschlossen
sein und ein finales
lokales Image sowie aktualisierte Nachweise liefern. Die Abnahme wiederholt statische
und praktische Pruefungen aus Sicht von Lernenden und Reviewenden.

**EN:** Before this acceptance starts, technical hardening must be complete
and provide a final local image and
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

**EN:**
- Rootless isolation, capabilities, mounts, write and network boundaries.
- OpenCode, Codex, Claude Code, Antigravity CLI and GitHub Copilot CLI.
- Toolchain families actually installed by the Dockerfile and smoke test, including Swift.
- VS Code connection, SourceKit-LSP and documented project mappings.
- Image build, Compose startup, small project functional checks and HTTP access.
- SBOM generation and consistency of security evidence.
- Learnability, German-first/English-second, CEFR B2 and WCAG 2.2 AA.

## Nicht-Ziele / Non-Goals

- Keine weitere Haertung waehrend der unabhaengigen Abnahme.
- Keine Ausweitung auf nur geplante oder nicht installierte Sprachen.
- Keine Anmeldung mit echten Provider-Secrets als Abnahmevoraussetzung.
- Keine formale Sandbox-, Rechts-, Provider- oder Modellfreigabe.

**EN:**
- No further hardening during independent acceptance.
- No extension to planned but uninstalled languages.
- No sign-in with actual provider credentials as an acceptance prerequisite.
- No formal sandbox, legal, provider or model approval.

## Anforderungen / Requirements

1. Jede Pruefung nennt Befehl, erwartetes Ergebnis und Evidenzpfad.
2. Toolchain- und Agentenstatus werden aus Build- und Laufzeitquellen abgeleitet.
3. Fehler werden als Befund an die technische Haertung zurueckgegeben.
4. Plattformabdeckung wird ehrlich als geprueft, uebersprungen oder offen
   dokumentiert.
5. Sicherheitsrestriktionen und Lernablauf werden gemeinsam bewertet.
6. Keine positive Bewertung darf allein auf Dokumentation ohne praktischen
   Nachweis beruhen, wenn ein lokaler Check moeglich ist.

**EN:**
1. Every check names its command, expected result and evidence path.
2. Toolchain and agent status derive from build and runtime sources.
3. Failures return to technical hardening as findings.
4. Platform coverage is honestly recorded as checked, skipped or Open.
5. Security controls and learning flow are evaluated together.
6. Documentation alone cannot justify a positive result when a practical local check is possible.

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

**EN:**
- Acceptance record with Pass, Fail, Open or N/A (not applicable) for each check.
- Toolchain, agent, mount and VS Code matrix.
- Final local SBOM and reproducible check commands.
- Concrete findings returned to the hardening stage.

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

**EN:**
- Compose configuration, image build and container startup are evidenced.
- All installed agents and toolchain families pass the planned version and project smoke tests.
- VS Code can attach to the container as documented.
- Mounts point to the documented container paths.
- SBOM generation succeeds or a concrete external blocker is documented.
- The self-build template is released only after successful technical acceptance.

## Annahmen und offene Fragen / Assumptions and Open Questions

- Provider-Anmeldungen sind fuer Versions- und Konfigurationschecks nicht
  erforderlich.
- Es bestehen keine offenen Intake-Authoring-Fragen.

**EN:**
- Provider sign-in is not required for version and configuration checks.
- No intake-authoring questions remain Open.

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
