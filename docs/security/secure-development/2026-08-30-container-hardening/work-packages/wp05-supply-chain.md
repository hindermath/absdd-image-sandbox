# WP05 Lieferkette und Build-Integritaet / Supply Chain and Build Integrity

## RED-Inspektion / RED inspection

Geprueft wurden Basisimage, apt, Go, Rust, Swift, uv, Syft, Spec Kit, Home
Baseline, OpenCode sowie die fuenf weiteren Agentenoberflaechen. Die
Dockerfile-ARGs und das Basisimage sind gepinnt; Downloadpfade verwenden je
nach Quelle Digest, SHA-256, Signatur oder Paket-Keyring. `home-baseline` hat
Release- und Commit-Lock. / The audit covered every named source and tool.

Reproduzierbares RED: beide SBOM-Skripte konnten auf
`docker.io/anchore/syft:latest` fallen; die Scan-Skripte suchten ungepinntes
Grype/Trivy auf dem Host. Zudem fehlten Cmdlet-/Dry-run-/Hilfe-/Manpage-
Vertraege. / Reproduced RED: moving Syft latest and unpinned host scanner
fallbacks plus incomplete paired interfaces.

## GREEN und offene Grenzen / GREEN and open boundaries

Die Fallbacks sind entfernt. Syft muss aus dem finalen Image oder exakt in
Version `1.46.0` vom Host kommen. Der Scanner ist als Grype `v0.117.0` plus
Manifest-Digest gepinnt. Bash `--dry-run` und PowerShell `-WhatIf` schreiben
nichts. Der finale Image-/SBOM-/VEX-/Scan-Nachweis folgt ausschliesslich in
T053–T055; SLSA, Registry-Publikation und externe Signatur werden nicht
behauptet. / The moving fallbacks are removed; final supply-chain evidence is
deferred to the one planned final image chain.

Mapping: FR-005, FR-010–FR-017, `GAP-051`–`GAP-063`. Owner: Repository
Maintainer; reviewer: Security Review.
