# Bedrohungsmodell der Lern-Sandbox / Learning Sandbox Threat Model

## Scope und Schutzwerte / Scope and assets

Die Analyse gilt fuer Image-Build, Compose-Laufzeit, Host-Mounts, benannte
Agenten-Volumes, Audit-Metadaten und externe Download-/Providergrenzen. Sie ist
keine Freigabe fuer produktive oder sensible Daten. / The analysis covers the
image build, Compose runtime, host mounts, named agent volumes, audit metadata,
and external download/provider boundaries. It is not approval for production
or sensitive data.

| Schutzwert / Asset | Vertraulichkeit | Integritaet | Verfuegbarkeit | Hauptmassnahme / Main control |
|---|---|---|---|---|
| Quellcode und Lernprojekte | mittel | hoch | mittel | explizite Mounts, non-root, Reviews |
| Lokale Secrets und Providerzustand | hoch | hoch | mittel | untracked Datei, Lesegrenzen, getrennte Volumes |
| Image und Toolchain | niedrig | hoch | mittel | Version-/Digest-Pins, Hash-/Signaturpruefung, SBOM |
| Agenten- und Audit-Metadaten | hoch | hoch | niedrig | getrennte Volumes, Metadaten-Allowlist, kein Promptinhalt |

## Datenfluesse und Vertrauensgrenzen / Data flows and trust boundaries

1. Der Host uebergibt nur deklarierte Bind-Mounts und lokale Umgebungswerte an
   Compose. Grenze: Host zu rootless Podman. / The host passes declared mounts
   and local environment values to Compose; boundary: host to rootless Podman.
2. Der Build laedt gepinnte oder verifizierte Artefakte und erzeugt das lokale
   Image. Grenze: externe Quelle zu Build. / The build retrieves pinned or
   verified artifacts; boundary: external source to build.
3. `adedev` bearbeitet Projekte und schreibt Agentenstate in getrennte Volumes.
   Grenze: Container zu Host-Mount beziehungsweise Named Volume. / `adedev`
   writes project data and separated agent state.
4. Agenten koennen nach lokaler menschlicher Freigabe externe Dienste nutzen.
   Grenze: Container zu Internet/Provider; diese Grenze ist technisch nicht
   allowlist-beschraenkt und bleibt offen. / Agents may use external services
   only after local human approval; unrestricted egress remains open.
5. `audit-export` schreibt nur erlaubte Metadaten nach `/audit`; Inhalte und
   Zugangsdaten sind ausgeschlossen. / Audit export writes allow-listed
   metadata only.

## STRIDE, Missbrauch und CAPEC / STRIDE, abuse, and CAPEC

| STRIDE | Beispiel / Example | Missbrauch / Abuse case | CAPEC-Bezug | Massnahme / Mitigation |
|---|---|---|---|---|
| Spoofing | manipulierte Downloadquelle | falsches Werkzeug wird installiert | CAPEC-94 | TLS, Digest-/Signaturpruefung, Pins |
| Tampering | Host-Mount oder SBOM wird veraendert | Evidenz passt nicht zum Image | CAPEC-153 | explizite Mounts, SHA-256-Bindung, finale Image-ID |
| Repudiation | Agentenlauf ist nicht nachvollziehbar | Aenderung ohne Metadaten | CAPEC-93 | enger Audit-Export, Git-Diff, Session-Log |
| Information disclosure | Secret gelangt in Log/Artefakt | Prompt oder Token wird exportiert | CAPEC-118 | Leseverbote, Secret-Scan, Metadaten-only |
| Denial of service | Build/Scannerquelle faellt aus | Gate wird uebersprungen | CAPEC-125 | fail-closed `Open`, kein stiller Fallback |
| Elevation of privilege | Containerprozess erlangt Rechte | Host-/Volume-Schaden | CAPEC-233 | non-root, `cap_drop: ALL`, `no-new-privileges` |

## Restrisiken und Aktualisierung / Residual risks and update

Freier Egress, Plattformkontrollen, Provider-/Modellfreigabe und formelle
Sandboxfreigabe sind offen. Dieses Dokument akzeptiert kein Restrisiko.
Security Review prueft es bei Aenderungen an Mounts, Ports, Egress, Agenten,
Toolchains, State oder Datenklassen erneut. / Open egress, platform controls,
provider/model approval, and formal sandbox approval remain open. This document
does not accept residual risk and must be reviewed on boundary changes.

Mapping: `GAP-041`–`GAP-050`, FR-006–FR-009, AR-002–AR-005.
