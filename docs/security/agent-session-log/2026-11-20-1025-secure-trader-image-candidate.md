# Secure-Trader-Sandbox: Image-Kandidat / Image candidate

DE: Für den lokalen Austausch wurde ein Kandidat aus Sandbox-Commit
`6e5a235f608902ba598ea839a0475ee87b10908d` gebaut. Der isolierte Build-Kontext
ändert nur den Level-0-Pin auf `c2c238c657b063ab7a5904654677875f96665de9`.
Der native ARM64-Build mit Profil `all` und Benutzer `adedev` ist bestanden.

EN: The local replacement candidate was built from the sandbox commit above.
The isolated build context changes only the Level 0 pin given above. The
native ARM64 build with profile `all` and user `adedev` passed.

- Image: `sha256:b322ef2abd9402db6ec67f807a676765c4a5eaef8cbeb276b9efde80f6621499`
- Level-0-Paket / package: `609f5b3e92aa8d5f458893dbf83f958ed5ea8ee7d8a36aef3fba3b60f1bd65a2`
- CycloneDX: 34.285 Komponenten / 34,285 components
  (`2f14c8ff61ecb677ca3f341039581edcf60742b9693e51ce0168dca63c8800b5`)
- Offline-Smoke: Exit 0
  (`801215e10050738fc5d759c14f130cafd935d71ab188bbc6755a03dd8f660e1d`)

DE: Der Offline-Smoke prüfte Werkzeuge, Dokumentationsablauf und 173
unveränderliche Paketdateien. P0-2 wurde technisch geprüft. Die exakte
Owner-Freigabe und die operative Aktivierung stehen aus. Das vorherige Image
und die sechs Volumes blieben erhalten.

EN: Offline checks verified the tools, documentation workflow and 173
immutable package files. P0-2 was technically verified. Exact owner approval
and operational activation remain pending. The previous image and six volumes
were preserved.

## Aktivierung / Activation

DE: Der Owner erteilte die exakte Freigabe am 20.11.2026. Der lokale
Level-0-Vertrag und der datierte Owner-Nachweis wurden abgeglichen. Sechs
Volume-Archive und der vorhandene Auditexport wurden anhand ihrer
Prüfsummen verifiziert. Image, Benutzer, Capability-Drop, Audit- und
Workspace-Mounts, Loopback-Bindung und Paketfingerabdruck bestanden den
Preflight. `absdd-image-sandbox_ade_1` läuft mit `healthy`. Das zuvor
vorhandene Image `5f530d888485` wurde erst danach gezielt entfernt.

EN: The owner approved the exact candidate on 20 November 2026. The local
Level 0 contract and dated approval were verified. Checksums confirmed six
volume backups and the prior audit export. The image, user, capability
drop, audit and workspace mounts, loopback binding and package fingerprint
passed preflight. `absdd-image-sandbox_ade_1` is running and healthy.
The previous image `5f530d888485` was removed after those checks.
