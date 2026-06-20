# Lastenheft: Secure-Development-Container-Hardening

**Dokumenttyp:** Spec-Kit Intake / Lastenheft
**Status:** vorbereitet fuer separaten Spec-Kit-Lauf
**Stand:** 2026-06-20
**Zielgruppe:** Fachinformatiker*innen in Ausbildung, Entwickler*innen, Reviewer und KI-Agenten

## 1. Zweck

Dieses Lastenheft beschreibt einen spaeteren Spec-Kit-Lauf fuer die sichere
Softwareentwicklungs-Sandbox `absdd-image-sandbox`. Der Lauf soll aus der
Secure-Development-Basis, den Checklisten, den mitgeltenden Dokumenten und den
sechs Governance-Presets ableiten, welche technischen und dokumentarischen
Anforderungen die Podman-basierte Entwicklungsumgebung erfuellen muss.

Der Lauf baut kein Image und startet keine Umsetzung. Er erzeugt zuerst eine
belastbare Spezifikation fuer einen spaeteren Container- oder
Sandbox-Hardening-Lauf.

*This requirements document describes a later Spec Kit run for the secure
software development sandbox `absdd-image-sandbox`. The run derives technical
and documentation requirements from the secure-development baseline,
checklists, related documents, and the six governance presets. It does not
build an image or start implementation; it first creates a reliable
specification for a later container or sandbox hardening run.*

## 2. Ausgangslage

Dieses Repository stellt eine Podman-basierte Sandbox fuer Opencode, .NET, C#,
Java, Go, Rust, Python, Codex CLI und Spec Kit bereit. Relevante Dateien sind
insbesondere:

- `Dockerfile`
- `compose.yml`
- `compose.home-baseline.yml`
- `renovate.json`
- `scripts/build-and-sbom.sh`
- `scripts/build-and-sbom.ps1`
- `scripts/compose-down-with-audit.sh`
- `scripts/compose-down-with-audit.ps1`
- `docs/security/`
- `opencode.jsonc`
- `opencode.env.example`
- `codex/`

Die Sandbox ist Entwicklungsinfrastruktur, keine Anwendung. Genau deshalb
muessen positive Sicherheitsbehauptungen wie Digest-Pinning, SBOM, Scan,
Secrets-Trennung, Audit-Export und Provider-Konfiguration mit Evidenz oder
`N/A`-Begruendung dokumentiert werden.

## 3. Zielbild

Nach dem spaeteren Spec-Kit-Lauf soll klar sein:

- welche Runtime als Referenz gilt, aktuell Podman mit Compose-Unterstuetzung,
- ob und warum das Image Entwicklungsinfrastruktur und kein Produktartefakt ist,
- welche Sicherheitsnachweise zwingend sind,
- welche Punkte `Applicable`, `N/A` oder `Open` sind,
- welche Evidenzpfade fuer Image, Build, Scan, Signatur, SBOM, Secrets,
  Mounts, Netzwerk und Agenten-Konfiguration genutzt werden,
- welche Anforderungen fuer Auszubildende in CEFR-B2-Sprache erklaert werden.

## 4. Scope

In Scope:

- unprivilegierte Container-Ausfuehrung und minimale Berechtigungen,
- Image-Digest-Pinning statt nur mutable Tags,
- reproduzierbarer Build und dokumentierte Basis-Images,
- SBOM fuer Image und Toolchain,
- VEX-Bewertung fuer bekannte Schwachstellen, falls relevant,
- SLSA-/Provenance-Nachweise fuer Build-Artefakte,
- Image-Signatur oder Attestation, z. B. Cosign, sofern anwendbar,
- Trivy-/Grype-Scan oder gleichwertige Container-/Filesystem-Scans,
- Secrets-Trennung, keine Secrets im Image, keine Tokens in Layern,
- Mount-Policy fuer Host-Verzeichnisse und Podman-Volumes,
- Netzwerkgrenzen und Offline-/Minimalnetz-Modus,
- Agenten-/Modell-Inventar, Tool-Versionen und deaktivierte Auto-Updates,
- Audit-Export beim Herunterfahren,
- Dokumentation fuer Auszubildende und Reviewer.

Out of Scope:

- sofortiger Container-Build,
- Auswahl eines konkreten Registry-Betreibers,
- produktive Cloud-Betriebsarchitektur,
- automatische Migration bestehender Projekte in den Container,
- direkte Aenderung an `Dockerfile`, Compose-Dateien oder Toolchain-Versionen.

## 5. Governance- und Compliance-Bezug

- `security-governance`: Secure Coding, Dependency-Audit, AI-SBOM/N/A,
  regulatorische Anwendbarkeit und Lieferkette.
- `architecture-governance`: C3A/C5-Anwendbarkeit,
  Cloud-/Provider-Abhaengigkeit, Container-/Artefakt-Hosting und
  Architekturentscheidungen.
- `agent-parity-governance`: konsistente Agenten-Dateien, Tool- und
  Modell-Routing.
- `cross-platform-governance`: macOS/Linux/Windows- und Shell-Paritaet.
- `a11y-governance`: textfreundliche Dokumentation und Lernbarkeit.
- `isaqb-architecture-governance`: Architekturentscheidungen,
  Qualitaetsszenarien und nachvollziehbare Kompromisse.

Reine Entwicklungsinfrastruktur kann bei C3A/C5, NIS2, CRA, EU AI Act oder
DORA `N/A` sein. Diese Nichtanwendbarkeit muss kurz begruendet werden; sie darf
nicht stillschweigend ausgelassen werden.

## 6. Mindestanforderungen an den spaeteren Lauf

1. Container-/Sandbox-Typ und Schutzgrenzen dokumentieren.
2. Basis-Image, Runtime und Toolchain-Versionen reproduzierbar festlegen.
3. Image-Digests, SBOM, Scan-Ergebnisse und Signatur-/Attestation-Entscheidung
   als Evidenzpfade planen.
4. Host-Mounts, Secrets, Caches, Agenten-Daten und Netzwerknutzung trennen.
5. Agentische KI-Werkzeuge, Modelle und Konfigurationen inventarisieren.
6. Auto-Update-Verhalten bewerten und fuer reproduzierbare Laeufe begrenzen.
7. Audit-Export und Session-Logs als Nachweisflaechen einordnen.
8. Alle Punkte als `Applicable`, `N/A` oder `Open` dokumentieren.
9. Auszubildendenverstaendliche Kurzbegriffe fuer Container, Image, Digest,
   SBOM, VEX, SLSA, Signatur, Mount und Sandbox aufnehmen.

## 7. Erwartete Ergebnisartefakte

| Artefakt | Erwartung |
|---|---|
| Spec-Kit `spec.md` | Container-Ziel, Scope, Nicht-Ziele, Schutzgrenzen |
| Spec-Kit `plan.md` | Runtime-/Image-Strategie, Evidenzpfade, Risiken |
| Spec-Kit `tasks.md` | Pruef-, Dokumentations- und spaetere Implementierungsaufgaben |
| Security-/Architecture-Evidence | SBOM, Scan, Signatur, S-ADR, C3A/C5/N/A-Entscheidung |
| README/Guide | CEFR-B2-Erklaerung fuer Nutzung und Sicherheitsmodell |

## 8. Akzeptanzkriterien

- Der spaetere Lauf startet keinen Container-Build ohne eigene Freigabe.
- Alle Sicherheits- und Supply-Chain-Punkte sind klassifiziert.
- Jede positive Sicherheitsbehauptung verweist auf konkrete Evidenz.
- Jede Nichtanwendbarkeit ist als `N/A` begruendet.
- Der Container-Scope ist fuer Auszubildende, Reviewer und KI-Agenten
  nachvollziehbar.
- Bestehende `docs/security/`-Nachweise werden nicht automatisch befuellt.

## 9. Kopierbarer `/speckit-specify`-Prompt

```text
/speckit-specify Nutze Lastenheft_Secure-Development-Container-Hardening.md als verbindliche Eingabedatei. Erstelle die Feature-Spezifikation fuer einen sicheren Softwareentwicklungscontainer bzw. eine Entwicklungs-Sandbox im Repository absdd-image-sandbox.

Ziel: Aus der Secure-Development-Basis, den Checklisten, den mitgeltenden Dokumenten und den sechs Governance-Presets soll ein belastbares Zielbild fuer eine reproduzierbare, auditierbare Podman-basierte Entwicklungsumgebung entstehen.

Pflichtpunkte:
- Container-/Sandbox-Typ, Schutzgrenzen und Nicht-Ziele klaeren.
- Podman/Docker- bzw. Runtime-Entscheidung als Architekturentscheidung vorbereiten.
- Dockerfile, compose.yml, compose.home-baseline.yml, renovate.json, scripts/build-and-sbom.*, scripts/compose-down-with-audit.* und docs/security/ als Evidenzpfade beruecksichtigen.
- Basis-Images per Digest pinnen; mutable Tags allein reichen nicht.
- SBOM, VEX, SLSA/Provenance, Trivy/Grype-Scan, Cosign/Signatur oder begruendetes N/A einplanen.
- Secrets, Caches, Agenten-Daten, Host-Mounts, Podman-Volumes und Netzwerkzugriff getrennt betrachten.
- Agenten-/Modell-Inventar, Tool-Versionen und Auto-Update-Verhalten dokumentieren.
- C3A/C5, NIS2, CRA, EU AI Act und DORA als Anwendbarkeitsmatrix pruefen; reine Entwicklungsinfrastruktur darf N/A sein, aber nur mit Begruendung.
- Inhalte muessen DE/EN, CEFR B2 und WCAG-2.2-AA-freundlich dokumentierbar sein.

Nicht-Ziele:
- Kein Container-Build in diesem Lauf.
- Keine direkte Aenderung an Dockerfile, Compose-Dateien oder Toolchain-Versionen.
- Keine automatische Migration bestehender Repos in den Container.
- Keine Produktiv-Cloud-Architektur ohne eigenes Lastenheft.

Erzeuge eine Spezifikation mit Scope, Nicht-Zielen, Schutzmodell, Evidenzmatrix, Anforderungen, Akzeptanzkriterien, Risiken und Teststrategie.
```
