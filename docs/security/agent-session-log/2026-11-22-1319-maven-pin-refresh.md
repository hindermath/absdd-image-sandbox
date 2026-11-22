# Maven-Pin #142: lokaler ARM64-Nachweis / Local ARM64 evidence

DE: Für [PR #142](https://github.com/hindermath/absdd-image-sandbox/pull/142)
wurde der Maven-Pin 3.10.1 auf Sandbox-`main` `5b32f3a986df4b0b86ab63de593fea26de64ab4d`
vorbereitet. Nur der Maven-Pin und seine SHA-512-Prüfsumme ändern sich im
Dockerfile. Die Prüfsumme stimmt mit der veröffentlichten Apache-Maven-Prüfsumme
überein. Der laufende Container, Volumes und das aktive Image bleiben unverändert.

EN: The Maven 3.10.1 pin for PR #142 was prepared on the Sandbox main commit
above. The Dockerfile changes only the Maven pin and its SHA-512 digest, which
matches Apache Maven's published digest. The running container, volumes and
active image remain unchanged.

| Prüfung / Check | Ergebnis / Result |
|---|---|
| Dockerfile SHA-256 | `50e708d7cb12ae27470d8a35be7f583b24287e1b3a40c2e62e063f7813453250` |
| Pin-Vertrag / Pin contract | 24/24 tests passed |
| Podman Compose, static configuration | Pass, isolated Java profile |
| Podman Compose build with pull | Pass, isolated Java profile |
| Native Podman build | `linux/arm64`, `ade-java`, image `30ac439e0fe07ce6b1c1fafb399e21f3f7006b0e36bfe897246adef739c58906` |
| Network-disabled Maven smoke | Apache Maven 3.10.1, Java 25.0.5.1, aarch64 |
| CycloneDX (Syft, network disabled) | 31,307 components; SHA-256 `2843cfa6096743a027d05462c5b188b2a950da54472199dc271d6ddc27999aa9`; unreadable paths excluded, no completeness or vulnerability claim |

DE: Dieser Nachweis gilt für das Java-Profil, nicht als Freigabe für das
`all`-Profil oder eine Image-Aktivierung. Die historische AMD64-Prüfung des
PRs ersetzt keine neuen CI-Prüfungen. Menschliche Sichtung, Aktualisierung
der erzeugten Statistik und CI am neuen PR-Head bleiben offen.

EN: This evidence covers the Java profile only; it does not approve the
`all` profile or image activation. Historical AMD64 checks do not replace
fresh CI. Human review, regenerated statistics and CI on the new PR head
remain pending.

Dokumentationsauswirkung / Documentation impact: `UpdateRequired` for
pin provenance and validation evidence; no new learner-facing instructions.
