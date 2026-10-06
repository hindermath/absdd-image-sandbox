<!-- intake-authoring:begin -->
# Technische Sandbox-Haertung / Technical Sandbox Hardening

**Status:** ReadyForReview

**Zielgruppe / Audience:** Auszubildende, Lernbegleitung, Entwicklung und Security Review

**Lieferautoritaet / Delivery authority:** LocalImplementation

## Voraussetzungen und Begriffe / Prerequisites and Terms

**DE:** Ein Intake ist eine Anforderungsdatei vor einem Spec-Kit-Lauf; Spec Kit
ordnet Anforderungen, Planung und Aufgaben. Vorausgesetzt werden nur
grundlegende Computer- und Terminalbedienung, keine Container-, Sicherheits-
oder Spec-Kit-Erfahrung. Die Zielgruppe beginnt im ersten Ausbildungsjahr
und umfasst Fachinformatiker*innen, IT-System-Elektroniker*innen und die
beiden kaufmaennischen IT-Ausbildungsberufe. LocalImplementation erlaubt nur
lokale Umsetzung; eine Review-Bereitschaft ist keine Start- oder Lieferfreigabe.

**EN:** An intake is a requirements file before a Spec Kit run; Spec Kit
organizes requirements, planning and tasks. Only basic computer and terminal
use is assumed, not container, security or Spec Kit experience. The audience
starts in the first training year and includes IT specialists, IT systems
electronics technicians and both IT management training occupations.
LocalImplementation permits local work only; review readiness does not
authorize execution or delivery.

**DE:** GSDB bezeichnet hier die generische Secure-Development-Basis, also die
lokale Richtlinie und Checklisten zur sicheren Entwicklung. Podman betreibt
Container (isolierte Arbeitsumgebungen); ein Image ist deren Bauvorlage.
Eine Toolchain ist eine zusammengehoerige Gruppe von Entwicklungswerkzeugen.
Rootless bedeutet Betrieb ohne Administratorrechte; Linux-Capabilities sind
einzelne Betriebssystemrechte. Mounts binden Verzeichnisse ein, Egress ist
ausgehender Netzwerkverkehr. Pinning legt Versionen fest; ein Digest ist ein
Inhaltspruefwert. CLI bedeutet Kommandozeilenwerkzeug, LSP bedeutet Language
Server Protocol fuer Editorfunktionen, ein Smoke-Test ist ein kleiner
Funktionstest. SBOM (Software Bill of Materials) listet Softwarebestandteile;
VEX (Vulnerability Exploitability eXchange) dokumentiert die Anwendbarkeit
von Schwachstellen, SLSA (Supply-chain Levels for Software Artifacts) beschreibt
Nachweise zur Build-Lieferkette. Eine Signatur ist ein kryptografischer
Herkunftsnachweis. A11Y steht fuer Barrierefreiheit; Human-only bezeichnet
Entscheidungen, die Menschen vorbehalten sind.

**EN:** GSDB here means the generic Secure Development Baseline: the local
guideline and checklists. Podman runs containers (isolated work environments);
an image is their build template. A toolchain groups development tools.
Rootless operation needs no administrator privileges; Linux capabilities are
individual operating-system permissions. Mounts connect directories; egress
is outgoing network traffic. Pinning fixes versions; a digest checks content.
A CLI is a command-line tool, LSP means Language Server Protocol for editor
features, and a smoke test is a small functional check. A Software Bill of
Materials (SBOM) lists software components. Vulnerability Exploitability
eXchange (VEX) records vulnerability applicability; Supply-chain Levels for
Software Artifacts (SLSA) describes build supply-chain evidence. A signature
proves cryptographic origin. A11Y means accessibility; Human-only decisions
are reserved for people.

## Zweck / Purpose

**DE:** Dieser Intake beschreibt die technische und dokumentarische Haertung
der Podman-basierten Entwicklungs-Sandbox. Die priorisierte Lueckenliste der
GSDB-Bestandspruefung ist die verbindliche fachliche Baseline.

**EN:** This intake defines technical and documentation hardening for the
Podman-based development sandbox. The prioritized gap list from the GSDB
baseline assessment is its binding baseline.

## Ausgangslage und Zielbild / Current and Target State

**DE:** Das Image stellt Agenten, Entwicklungswerkzeuge und mehrere
speichersichere Toolchain-Familien bereit. Nach dem Lauf sind anwendbare
Sicherheitsluecken mit reproduzierbaren Aenderungen behoben oder mit
begruendetem Restrisiko offen dokumentiert.

**EN:** The image provides agents, development tools, and several memory-safe
toolchain families. After the run, applicable security gaps are fixed through
reproducible changes or remain explicitly documented with justified residual
risk.

## Scope

- Basisimage, Digest-Pinning, reproduzierbare Downloads und Versions-Pinning.
- Rootless-Laufzeit, Linux-Capabilities, Mounts, Dateirechte und Schreibgrenzen.
- Netzwerkentscheidung, Paketquellen und dokumentierte Egress-Grenzen.
- OpenCode und alle erforderlichen Agenten-CLIs samt isoliertem Zustand.
- Tatsachlich installierte Toolchains, LSP-Werkzeuge und Smoke-Tests.
- SBOM, Schwachstellenbewertung, VEX/SLSA/Signatur-Anwendbarkeit.
- VS-Code-Dev-Container-Zugriff und lokale Projekt-Mappings.
- Lernenden-, A11Y- und Plattformdokumentation.

**EN:**
- Base image, digest pinning, reproducible downloads and version pinning.
- Rootless runtime, Linux capabilities, mounts, file permissions and write boundaries.
- Network decision, package sources and documented egress limits.
- OpenCode and all required agent CLIs with isolated state.
- Actually installed toolchains, LSP tools and smoke tests.
- SBOM, vulnerability assessment and VEX/SLSA/signature applicability.
- VS Code Dev Containers access and local project mappings.
- Learner, accessibility and platform documentation.

## Nicht-Ziele / Non-Goals

- Kein fertiges Projekt-Image in GHCR oder einer anderen Projekt-Registry.
- Keine produktive Cloud- oder Mehrmandantenplattform.
- Keine echte Provider-, Modell-, Rechts- oder Sandbox-Freigabe.
- Keine Secrets im Image, in Commits oder in Testprotokollen.

**EN:**
- No ready-made project image in GitHub Container Registry (GHCR) or another project registry.
- No production cloud or multi-tenant platform.
- No actual provider, model, legal or sandbox approval.
- No secrets (credentials) in images, commits or test logs.

## Anforderungen / Requirements

1. Jede Aenderung muss auf einen Befund der GSDB-Bestandspruefung zeigen.
2. Build- und Laufzeitrechte bleiben minimal und begruendet.
3. Downloads, Toolversionen und Basisimage bleiben reproduzierbar pruefbar.
4. Agenten- und Providerzustand bleibt voneinander und vom Repository getrennt.
5. Toolchain-Behauptungen muessen durch Versions- und Projekt-Smoke-Tests
   belegt sein.
6. Sicherheitsrestriktionen duerfen die dokumentierten Lern- und
   Entwicklungsablaeufe nicht unbegruendet blockieren.
7. Offene Human-only-Punkte bleiben als solche gekennzeichnet.

**EN:**
1. Every change must trace to a GSDB baseline assessment finding.
2. Build and runtime permissions remain minimal and justified.
3. Downloads, tool versions and the base image remain reproducibly verifiable.
4. Agent and provider state stay separate from each other and the repository.
5. Toolchain claims require version and small project functional checks.
6. Security controls must not block documented learning and development flows without justification.
7. Open Human-only items remain explicitly identified.

## Abhaengigkeiten und Risiken / Dependencies and Risks

**DE:** Dieser Intake setzt eine abgeschlossene GSDB-Bestandspruefung voraus;
ihr dokumentierter Abschluss erfuellt diese fachliche Voraussetzung und ist
kein Blocker. Aktuelles Intake-Review und ausdrueckliche Ausfuehrungsautoritaet
bleiben davon getrennt erforderlich. Nicht reproduzierbare Downloads, ueberbreite Mounts, veraltete
Agenten oder widerspruechliche Toolchain-Angaben sind zentrale Risiken.

**EN:** This intake requires a completed GSDB baseline assessment; its
documented completion fulfills that prerequisite rather than blocking it.
Current intake review and explicit execution authority remain separate requirements.
Non-reproducible downloads, overly broad mounts, stale agents, or conflicting
toolchain claims are key risks.

## Erwartete Artefakte und Evidenz / Expected Artefacts and Evidence

- Gezielte Aenderungen an Image, Compose, Konfiguration und Dokumentation.
- Aktualisierte SBOM- und Scan-Nachweise.
- Reproduzierbarer Toolchain- und Agenten-Smoke-Test.
- Aktualisierte projektspezifische Evidenz unter `docs/security/`.

**EN:**
- Targeted changes to image, Compose, configuration and documentation.
- Updated SBOM and scan evidence.
- Reproducible toolchain and agent smoke test.
- Updated project-specific evidence under `docs/security/`.

## Akzeptanzkriterien / Acceptance Criteria

- Alle in Scope liegenden priorisierten Befunde sind behoben oder begruendet
  offen.
- Image und Compose-Konfiguration bauen beziehungsweise validieren erfolgreich.
- Agenten, Toolchains, VS-Code-Zugriff und Mounts sind praktisch geprueft.
- SBOM-Erzeugung funktioniert fuer das finale lokale Image.
- Keine Freigabe oder Remote-Verteilung wird erfunden oder automatisch
  ausgefuehrt.

**EN:**
- All prioritized findings in scope are resolved or remain Open with justification.
- Image build and Compose configuration validation succeed.
- Agents, toolchains, VS Code access and mounts are checked in practice.
- SBOM generation works for the final local image.
- No approval or remote distribution is invented or performed automatically.

## Annahmen und offene Fragen / Assumptions and Open Questions

- Podman bleibt die Referenzlaufzeit.
- Es bestehen keine offenen Intake-Authoring-Fragen.

**EN:**
- Podman remains the reference runtime.
- No intake-authoring questions remain Open.

<!-- intake-authoring:prompts -->
## Kopierbare Folgekommandos / Copy-Ready Follow-Up Commands

<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Erstelle eine Spezifikation ausschliesslich auf Grundlage von Lastenheft_Secure-Development-Container-Hardening.md und der abgeschlossenen GSDB-Lueckenliste. Plane technische und dokumentarische Haertung, aber keine Registry-Verteilung oder formale Freigabe.
```

<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Fuehre den vollstaendigen Spec-Kit-Lauf fuer Lastenheft_Secure-Development-Container-Hardening.md mit Delivery Authority LocalImplementation aus. Implementiere und pruefe die priorisierten Haertungen lokal und stoppe vor Commit, Push, Pull Request, Merge oder Hosting-Aenderungen.
```
<!-- intake-authoring:end -->
