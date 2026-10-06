<!-- intake-authoring:begin -->
# Technische Sandbox-Haertung / Technical Sandbox Hardening

**Status:** ReadyForReview

**Zielgruppe / Audience:** Auszubildende, Lernbegleitung, Entwicklung und Security Review

**Lieferautoritaet / Delivery authority:** LocalImplementation

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

## Nicht-Ziele / Non-Goals

- Kein fertiges Projekt-Image in GHCR oder einer anderen Projekt-Registry.
- Keine produktive Cloud- oder Mehrmandantenplattform.
- Keine echte Provider-, Modell-, Rechts- oder Sandbox-Freigabe.
- Keine Secrets im Image, in Commits oder in Testprotokollen.

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

## Abhaengigkeiten und Risiken / Dependencies and Risks

**DE:** Dieser Intake ist durch die abgeschlossene GSDB-Bestandspruefung
blockiert. Nicht reproduzierbare Downloads, ueberbreite Mounts, veraltete
Agenten oder widerspruechliche Toolchain-Angaben sind zentrale Risiken.

**EN:** Completion of the GSDB baseline assessment blocks this intake.
Non-reproducible downloads, overly broad mounts, stale agents, or conflicting
toolchain claims are key risks.

## Erwartete Artefakte und Evidenz / Expected Artefacts and Evidence

- Gezielte Aenderungen an Image, Compose, Konfiguration und Dokumentation.
- Aktualisierte SBOM- und Scan-Nachweise.
- Reproduzierbarer Toolchain- und Agenten-Smoke-Test.
- Aktualisierte projektspezifische Evidenz unter `docs/security/`.

## Akzeptanzkriterien / Acceptance Criteria

- Alle in Scope liegenden priorisierten Befunde sind behoben oder begruendet
  offen.
- Image und Compose-Konfiguration bauen beziehungsweise validieren erfolgreich.
- Agenten, Toolchains, VS-Code-Zugriff und Mounts sind praktisch geprueft.
- SBOM-Erzeugung funktioniert fuer das finale lokale Image.
- Keine Freigabe oder Remote-Verteilung wird erfunden oder automatisch
  ausgefuehrt.

## Annahmen und offene Fragen / Assumptions and Open Questions

- Podman bleibt die Referenzlaufzeit.
- Es bestehen keine offenen Intake-Authoring-Fragen.

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
