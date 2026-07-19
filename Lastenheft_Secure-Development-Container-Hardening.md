# Lastenheft: Secure-Development-Container-Hardening

**Dokumenttyp:** Spec-Kit Intake / Lastenheft
**Status:** vorbereitet fuer separaten Spec-Kit-Lauf
**Stand:** 2026-06-20
**Zielgruppe:** Fachinformatiker*innen in Ausbildung, Entwickler*innen, Reviewer und KI-Agenten

## 1. Zweck

Dieses Lastenheft beschreibt einen spaeteren Spec-Kit-Lauf fuer einen Container
zur sicheren Softwareentwicklung. Der Lauf soll aus der bestehenden
Secure-Development-Basis, den Checklisten, den mitgeltenden Dokumenten und den
Governance-Presets ableiten, welche technischen und dokumentarischen
Anforderungen ein reproduzierbarer Entwicklungscontainer erfuellen muss.

Der Lauf baut keinen Container und startet keine Umsetzung. Er erzeugt zuerst
eine belastbare Spezifikation fuer den spaeteren Container- oder
Sandbox-Hardening-Lauf.

*This requirements document describes a later Spec Kit run for a secure software
development container. The run derives technical and documentation requirements
from the secure-development baseline, checklists, related documents, and
governance presets. It does not build a container or start implementation; it
first creates a reliable specification for a later container or sandbox
hardening run.*

## 2. Ausgangslage

Die Secure-Development-Basis beschreibt bereits Anforderungen an sichere
Entwicklungsumgebungen, agentische KI-Sandboxen, Lieferkette, SBOM, Secrets,
Container-Scanning, Digest-Pinning, Signaturen und Audit-Evidenz. Fuer einen
kuenftigen Entwicklungscontainer muessen diese Punkte in ein konkretes
Container-Zielbild ueberfuehrt werden.

Relevante Bezugspunkte sind insbesondere:

- `docs/secure-development/Richtlinie_Sichere-Entwicklung.md`
- `docs/secure-development/Checklistensammelband_Sichere-Entwicklung.md`
- `docs/secure-development/checklisten/CL_10_Sichere-Entwicklungsumgebung.md`
- `docs/secure-development/checklisten/CL_12_Agentische-KI-Sandbox.md`
- `docs/secure-development/mitgeltende-dokumente/Verzahnung_Richtlinie_Checklisten_Spec-Kit-Presets.md`
- `constitution.md`, Prinzipien XII bis XIX
- die acht Governance-Presets

## 3. Zielbild

Nach dem spaeteren Spec-Kit-Lauf soll klar sein:

- welche Container-Runtime als Referenz gilt, z. B. Podman oder Docker,
- ob der Container als Entwicklungsinfrastruktur, Produktartefakt oder beides
  zu behandeln ist,
- welche Sicherheitsnachweise zwingend sind,
- welche Punkte `Applicable`, `N/A` oder `Open` sind,
- welche Evidenzpfade fuer Image, Build, Scan, Signatur, SBOM, Secrets,
  Mounts, Netzwerk und Agenten-Konfiguration genutzt werden,
- welche Anforderungen fuer Auszubildende in CEFR-B2-Sprache erklaert werden
  muessen.

## 4. Scope

In Scope:

- unprivilegierte Container-Ausfuehrung und minimale Berechtigungen,
- Image-Digest-Pinning statt nur mutable Tags,
- reproduzierbarer Build und dokumentierte Basis-Images,
- SBOM fuer Container und Toolchain,
- VEX-Bewertung fuer bekannte Schwachstellen, falls relevant,
- SLSA-/Provenance-Nachweise fuer Build-Artefakte,
- Image-Signatur oder Attestation, z. B. Cosign, sofern anwendbar,
- Trivy-/Grype-Scan oder gleichwertige Container-/Filesystem-Scans,
- Secrets-Trennung, keine Secrets im Image, keine Tokens in Layern,
- Mount-Policy fuer Host-Verzeichnisse,
- Netzwerkgrenzen und Offline-/Minimalnetz-Modus,
- Agenten-/Modell-Inventar, Tool-Versionen und deaktivierte Auto-Updates,
- Dokumentation fuer Auszubildende und Reviewer.

Out of Scope:

- sofortiger Container-Build,
- Auswahl eines konkreten Registry-Betreibers,
- Produktive Cloud-Betriebsarchitektur,
- automatische Migration bestehender Projekte in den Container.

## 5. Governance- und Compliance-Bezug

- `security-governance`: Secure Coding, Dependency-Audit, AI-SBOM/N/A,
  regulatorische Anwendbarkeit und Lieferkette.
- `architecture-governance`: C3A/C5-Anwendbarkeit, Cloud-/Provider-Abhaengigkeit,
  Container-/Artefakt-Hosting und Architekturentscheidungen.
- `agent-parity-governance`: konsistente Agenten-Dateien, Tool- und
  Modell-Routing.
- `cross-platform-governance`: macOS/Linux/Windows- und Shell-Paritaet.
- `a11y-governance`: textfreundliche Dokumentation und Lernbarkeit.
- `isaqb-architecture-governance`: Architekturentscheidung, Qualitaetsszenarien
  und nachvollziehbare Kompromisse.

Reine Entwicklungsinfrastruktur kann bei C3A/C5, NIS2, CRA, EU AI Act oder DORA
`N/A` sein. Diese Nichtanwendbarkeit muss kurz begruendet werden; sie darf nicht
stillschweigend ausgelassen werden.

## 6. Mindestanforderungen an den spaeteren Lauf

1. Container-/Sandbox-Typ und Schutzgrenzen dokumentieren.
2. Basis-Image, Runtime und Toolchain-Versionen reproduzierbar festlegen.
3. Image-Digests, SBOM, Scan-Ergebnisse und Signatur-/Attestation-Entscheidung
   als Evidenzpfade planen.
4. Host-Mounts, Secrets, Caches, Agenten-Daten und Netzwerknutzung trennen.
5. Agentische KI-Werkzeuge, Modelle und Konfigurationen inventarisieren.
6. Auto-Update-Verhalten bewerten und fuer reproduzierbare Laeufe begrenzen.
7. Alle Punkte als `Applicable`, `N/A` oder `Open` dokumentieren.
8. Auszubildendenverstaendliche Kurzbegriffe fuer Container, Image, Digest,
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

## 9. Kopierbarer `/speckit-specify`-Prompt

```text
/speckit-specify Nutze Lastenheft_Secure-Development-Container-Hardening.md als verbindliche Eingabedatei. Erstelle die Feature-Spezifikation fuer einen sicheren Softwareentwicklungscontainer bzw. eine Entwicklungs-Sandbox.

Ziel: Aus der Secure-Development-Basis, den Checklisten, den mitgeltenden Dokumenten und den acht Governance-Presets soll ein belastbares Zielbild fuer einen reproduzierbaren, auditierbaren Entwicklungscontainer entstehen.

Pflichtpunkte:
- Container-/Sandbox-Typ, Schutzgrenzen und Nicht-Ziele klaeren.
- Podman/Docker- bzw. Runtime-Entscheidung als Architekturentscheidung vorbereiten.
- Basis-Images per Digest pinnen; mutable Tags allein reichen nicht.
- SBOM, VEX, SLSA/Provenance, Trivy/Grype-Scan, Cosign/Signatur oder begruendetes `N/A` einplanen.
- Secrets, Caches, Agenten-Daten, Host-Mounts und Netzwerkzugriff getrennt betrachten.
- Agenten-/Modell-Inventar, Tool-Versionen und Auto-Update-Verhalten dokumentieren.
- C3A/C5, NIS2, CRA, EU AI Act und DORA als Anwendbarkeitsmatrix pruefen; reine Entwicklungsinfrastruktur darf `N/A` sein, aber nur mit Begruendung.
- Inhalte muessen DE/EN, CEFR B2 und WCAG-2.2-AA-freundlich dokumentierbar sein.

Nicht-Ziele:
- Kein Container-Build in diesem Lauf.
- Keine automatische Migration bestehender Repos in den Container.
- Keine Produktiv-Cloud-Architektur ohne eigenes Lastenheft.

Erzeuge eine Spezifikation mit Scope, Nicht-Zielen, Schutzmodell, Evidenzmatrix, Anforderungen, Akzeptanzkriterien, Risiken und Teststrategie.
```
