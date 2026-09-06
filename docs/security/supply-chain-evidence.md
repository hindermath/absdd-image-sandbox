# Lieferketten-Evidenz / Supply-Chain Evidence

## Aktueller Vertrag / Current contract

- Basisimage per Digest; Tool-/Agentenversionen ueber Renovate-ueberwachte
  Dockerfile-ARGs. / Base image by digest; tool and agent versions via
  Renovate-managed arguments.
- Downloadintegritaet wird mit SHA-256, PGP-Signatur oder signiertem
  Paket-Keyring geprueft, soweit die jeweilige Quelle dies bereitstellt. /
  Download integrity uses SHA-256, PGP, or a signed package keyring where the
  source provides it.
- `home-baseline.lock.json` bindet Release, Commit und Lizenz. / The lock file
  binds release, commit, and licence.
- `build-and-sbom.*` verlangt Image-Syft oder Host-Syft `1.46.0`; kein
  `latest`-Fallback. `analyze-sbom.*` nutzt das digest-gepinnte Grype-Image. /
  There is no moving SBOM/scanner fallback.

Die finale Image-ID, CycloneDX-SBOM, Scan-Datenbank, Findings, VEX und lokale
Provenienz werden erst nach dem einmaligen finalen Build gebunden. Bis dahin
bleibt das Supply-Chain-Gate offen. Es erfolgt kein Registry-Push, keine
Signatur und keine SLSA-Level-Behauptung. / Final image-bound evidence is
created only after the single final build. No registry, signature, or SLSA
claim is made.

Mapping: `GAP-051`–`GAP-063`, GATE-SUPPLY-01.
