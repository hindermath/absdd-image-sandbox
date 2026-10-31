# Crypto/TLS Inventory — Feature 004

Stand: 2026-10-31; US2-Zwischenstand vor T049/T052 und finaler T053-Neubindung.
Quellen: `Dockerfile`, `compose.yml`, `opencode.jsonc`,
`codex/{config,requirements}.toml`, `scripts/build-and-sbom.{sh,ps1}`.

## Deutsch

| Grenze | Aktuelle Quelle und Schutz | Offene Prüfung / Owner |
|---|---|---|
| Build-Transport | Ubuntu APT-Quellen und NodeSource über HTTPS, signierte APT-Metadaten; Downloads von MCR, Apache, Microsoft, GitHub, go.dev, Swift und Rust per HTTPS; `uv` holt Spec Kit via Git/HTTPS. Ubuntu-CA-Vertrauen, kein eigener Zertifikatspin. | Maintainer/Security Review: CA-/Proxy-Profil und Egress-Regeln der Zielumgebung; nativer Build T059. Keine TLS-Wirkung aus URL-Text allein ableiten. |
| Build-Integrität | MCR-Basis per Digest; feste SHA-256/-512 für native Archive und Maven; Swift-Archivsignatur mit festem 6.x-Fingerprint. `home-baseline` per Git-Commit. | Maintainer: Hashwerte bei Version/Architekturwechsel separat prüfen. Rustup bezieht Datei und `.sha256` noch vom selben Host; npm-Transitiven fehlt ein repo-eigenes Lock. Finale SBOM/CVE T063. |
| Laufzeit-Agenten | TLS/Signaturen der jeweiligen OpenCode-, Codex-, Claude-, Gemini-, Copilot- und Antigravity-Implementierungen; Container stellt keine eigene Kryptoalgorithmik bereit. Keine Provider-/Modellbindung im Image. | Security/Provider Review vor Providerfreigabe: Endpunkte, Zertifikats-/Proxy-Verhalten, Protokollversionen, Datenfluss und Vertrags-/Regionsvorgaben je gewähltem Dienst. Keine Live-Probe ohne eigene Autorität. |
| Audit und persistente Daten | JSONL-Metadaten auf Host-Mount, lokale Volumes für Agenten. Export enthält keine kryptografische Signatur oder Verschlüsselung durch dieses Repo; Host-/Volume-Rechte und Retention sind getrennte Controls. | Owner/Privacy Review: Speicherung und ggf. erforderliche Verschlüsselung/Schlüsselverwaltung der Zielumgebung. Keine selbst erzeugten Schlüssel, keine Secret-Rotation durch Agent. |
| Release-Artefakte | `build-and-sbom` erzeugt SBOM; kein Image-Signing, keine VEX- oder SLSA-Attestierung im aktuellen Quellstand. | Security Review/Owner: vor Weitergabe entscheiden, ob Signatur/VEX/SLSA/Registry-Nachweise nötig sind. T063/T068 bleiben separat. |

**Profilkonflikte und Migration:** Ein FIPS-/organisationsspezifisches
Kryptoprofil ist für dieses generische Training-Image weder konfiguriert noch
belegt. Falls die Zielumgebung eines verlangt, prüft Security Review
Kompatibilität der sechs CLIs, Ubuntu-/OpenSSL-Pakete, TLS-Proxy,
Swift-/GPG- und Archivprüfungen vor dem Einsatz. Ein Versions- oder
Schlüsselwechsel aktualisiert Dockerfile-Pins, Digest/Signaturanker,
Renovate-Metadaten, native Buildbelege und dieses Inventar gemeinsam.
Keine Ausnahme von einer vorgegebenen Kryptopolicy wird hier genehmigt.

**Begrenztes N/A:** Eigene Kryptografie-Implementierung und eigenes
Modelltraining sind im aktuellen Repository nicht vorhanden. Das ist kein
N/A für TLS, Signaturprüfung, Fremdkomponenten, Provider oder
Speicherschutz. Trigger: neue Krypto-/Providerfunktion, geänderter
Buildpfad oder Image-Weitergabe. T053 muss die dann aktuelle Quelle neu
abgleichen.

## English

This interim inventory maps TLS transport, archive/signature integrity,
agent runtime services, local audit storage and release artifacts to their
current source. HTTPS URLs and source-level checks do not prove a native
build or operational TLS policy. The Swift signer and fixed archive digests
are source-level safeguards; Rustup's same-origin checksum and unlocked npm
transitives remain review boundaries. No custom cryptography, FIPS claim,
key rotation or exception approval is made. The maintainer and Security,
Provider and Privacy reviewers own the listed decisions before affected use;
T053 must rebind this inventory after the remaining code changes.
