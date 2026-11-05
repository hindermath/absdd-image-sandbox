# Image-Refresh Model Routing 0.2.6 / Image refresh

Documentation Impact: `UpdateRequired`. Owner: Repository Maintainer.
Zielgruppe / Audience: Betrieb, Maintainer / operators, maintainers.
Kanonische Quelle / Canonical source: `home-baseline.lock.json`, Dockerfile,
`scripts/sync-home-baseline-runtime.sh`. Leserpfad / Reader path:
`docs/betrieb/image-aufbau.md`. DE/EN in diesem Dokument / in this document.
Distribution: Image und Repository; kein Host-Home-Sync / no host Home sync.
Neu bewerten bei Pin- oder Wrapperaenderungen / reevaluate on pin or wrapper changes.

## Umfang / Scope

Level-0-Pin: `9107cff07a73892076c18c6a28a4e396a250f519`.
Model Routing: 0.2.6. Autonomous Run: 0.4.10.
Kandidat / Candidate: `localhost/absdd-image-sandbox_ade:routing-v026-20261105`.
Der Bestandscontainer `9e5b3649ae91` bleibt beendet und unveraendert.
The existing stopped container and its volumes are preserved.

Der Wrapper akzeptiert nun beide vom Installer unterstuetzten Lock-Schemas.
Negative Tests verwerfen falsche Versionen, Referenztypen und Commit-Werte.
The wrapper now accepts both installer-supported lock schemas. Negative
tests reject invalid schema versions, reference types and commit values.

## Validierung / Validation

Build und isolierte Runtime-Pruefung: PASS / Build and isolated runtime: PASS.
Image-ID: `sha256:dc66ce0a897b575dcaca5d80a4f253a88458e5767adef0e4a6b0c04543d40847`.
SBOM: `sboms/2026-11-05-localhost-absdd-image-sandbox_ade-routing-v026-20261105-dc66ce0a897b.cdx.json`
(lokales ignoriertes Artefakt / local ignored artifact), CycloneDX 1.7,
30,500 components, SHA-256 `af11ac600e569095a82b8999181d3408df22d5e18364dd9df86e96375e57cbb9`.

- 10 Pin-, Dokumentations- und Runtime-Lock-Vertragstests: PASS.
- SBOM-Digest-Normalisierung: PASS, rohe und praefixierte SHA-256-IDs;
  unvollstaendige, mehrzeilige oder fremde IDs werden abgewiesen.
- Compose-Konfiguration, Bash-Syntax und Diff-Whitespace: PASS.
- 13 Architektur-/Lifecycle-Regressionstests (Bash und PowerShell): PASS.
- Eingebetteter Commit und beide Preset-Versionen: PASS.
- Runtime-Vorschau, explizites Apply und driftfreier Folgestatus: PASS.
- 48 Routing-Installationsassertionen im Container: PASS.
- Vollstaendiger Toolchain-/Dokumentations-Smoke: PASS, Exit 0.
- Non-root `adedev`, cap-drop ALL und no-new-privileges im Test: PASS.

The checks above passed on the native ARM64 image. Runtime validation used
a disposable container without credentials or project volumes. The full smoke
test built and ran language examples and checked the documentation PDF path.
Its broken-link fixture is an intentional negative test. Swift emitted
safeExec signal warnings but built and ran successfully. No live inference or
vulnerability assessment was performed; the SBOM is an inventory.

Zwei Infrastrukturkorrekturen / Two infrastructure corrections:
Der Runtime-Wrapper akzeptiert Schema 2; beide SBOM-Shellvarianten normalisieren
vollstaendige Podman-IDs ohne Algorithmuspraefix. Das Image enthaelt die
Wrapperkorrektur; SBOM-Erzeugung verwendet die Host-Skripte dieses Branches.
The image contains the runtime-wrapper correction; SBOM generation uses this
branch's host scripts with digest normalization.

Kein Austausch des Bestandscontainers, kein Push oder Merge.
The existing container was not replaced; no push or merge was performed.
Alle kurzlebigen Testcontainer wurden entfernt; die sechs bestehenden Volumes
und Container `9e5b3649ae91` mit Image `9cbfe8a74a94` sind erhalten.
All disposable test containers were removed; existing volumes and container
identity were preserved. Source delivery uses the candidate branch
`codex/image-refresh-model-routing-v026`; merge and container activation
require separate authorization.
Plattform: macOS-Host mit nativem Podman-Linux-Image; keine Windows-/AMD64-Abnahme.
Platform: macOS host, native Podman Linux image; no Windows/AMD64 acceptance.
