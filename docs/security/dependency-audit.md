# Abhaengigkeits- und Quellen-Audit / Dependency and Source Audit

## Methode / Method

**DE:** Geprueft werden Basisdigest, Renovate-Metadaten jedes Dockerfile-ARG,
Downloadversion/-hash, signierter Paketquellen-Key, Git-Tag/Commit-Lock,
Lizenzhinweis sowie bewegliche Tokens wie `latest`, `main` oder ungepinnte
Hostwerkzeuge. Eine Versionsnummer allein ist kein Integritaetsbeleg. / Check
base digest, Renovate metadata, download hashes, signed source keys, Git locks,
licenses, and movable tokens. A version alone is not integrity evidence.

## Aktueller Befund / Current Finding

- MCR-Basisimage: Tag plus SHA-256-Digest, pass static.
- Dockerfile ARGs: immediately preceded by Renovate metadata, local validator
  pass; practical build remains T053.
- Home Baseline: release and commit in `home-baseline.lock.json`, validator
  pass.
- Syft: version `1.46.0` in Dockerfile. Moving helper fallback removed; helper
  now fails closed if image-integrated or exact host version is unavailable.
- Grype: official container `v0.117.0` pinned by manifest digest; no host
  auto-discovery and no Trivy fallback. Database freshness remains runtime
  evidence, not a static claim.
- Go, Rust, Swift, uv, Node, Spec Kit and agent CLIs: declared pins exist;
  archive hash, key fingerprint, tag/commit, and runtime-version proof are
  reconciled in WP05/final build evidence rather than assumed here.

Keine Lizenz-, Schwachstellen- oder Registry-Freigabe wird durch dieses
Dokument erteilt. Trigger: source, version, digest, checksum, key, lock,
scanner database, license, or distribution change. / This grants no license,
vulnerability, or registry approval. Re-evaluate on the listed changes.

Mapping: GAP-020, GAP-026–GAP-040, GAP-051–GAP-063.
