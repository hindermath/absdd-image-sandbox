# Supply-Chain-Haertung TODO

Diese Datei verfolgt die verbleibenden P3-1-Arbeiten aus
`COMPLIANCE-PLAN_RL-SE-001.md`. Ziel ist, Remote-Installer nicht mehr blind
auszufuehren, sondern feste Artefakte ueber signierte Paketquellen oder
Pruefsummen zu binden.

## Deutsch

| Komponente | Aktueller Pfad | Zielzustand | Status |
|---|---|---|---|
| Node.js / NodeSource | Signierte NodeSource-Apt-Quelle mit Deb822-Source-Datei und `Signed-By`-Keyring | Beibehalten; kein `setup_lts.x \| bash -` mehr im Dockerfile | erledigt in P3-1 MR 1 |
| uv / uvx | Festes GitHub-Release-Artefakt `0.11.16` pro Architektur mit SHA256-Pruefung | Beibehalten; kein `astral.sh/uv/install.sh \| sh` mehr im Dockerfile | erledigt in P3-1 MR 2 |
| Rust / rustup | Festes `rustup-init`-Artefakt `1.28.2` pro Architektur mit SHA256-Pruefung | Beibehalten; kein `sh.rustup.rs \| sh` mehr im Dockerfile | erledigt in P3-1 MR 3 |

## English

| Component | Current path | Target state | Status |
|---|---|---|---|
| Node.js / NodeSource | Signed NodeSource Apt source with Deb822 source file and `Signed-By` keyring | Keep; the Dockerfile no longer runs `setup_lts.x \| bash -` | done in P3-1 MR 1 |
| uv / uvx | Fixed GitHub release artifact `0.11.16` per architecture with SHA256 verification | Keep; the Dockerfile no longer runs `astral.sh/uv/install.sh \| sh` | done in P3-1 MR 2 |
| Rust / rustup | Fixed `rustup-init` artifact `1.28.2` per architecture with SHA256 verification | Keep; the Dockerfile no longer runs `sh.rustup.rs \| sh` | done in P3-1 MR 3 |
