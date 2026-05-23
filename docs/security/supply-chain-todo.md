# Supply-Chain-Haertung TODO

Diese Datei verfolgt die verbleibenden P3-1-Arbeiten aus
`COMPLIANCE-PLAN_RL-SE-001.md`. Ziel ist, Remote-Installer nicht mehr blind
auszufuehren, sondern feste Artefakte ueber signierte Paketquellen oder
Pruefsummen zu binden.

## Deutsch

| Komponente | Aktueller Pfad | Zielzustand | Status |
|---|---|---|---|
| Node.js / NodeSource | Signierte NodeSource-Apt-Quelle mit Deb822-Source-Datei und `Signed-By`-Keyring | Beibehalten; kein `setup_lts.x \| bash -` mehr im Dockerfile | erledigt in P3-1 MR 1 |
| uv / uvx | `https://astral.sh/uv/install.sh` wird beim Image-Build per `sh` ausgefuehrt | Festes GitHub-Release-Artefakt pro Architektur herunterladen, SHA256 pruefen, `uv` und `uvx` installieren | offen fuer P3-1 MR 2 |
| Rust / rustup | `https://sh.rustup.rs` wird beim Image-Build per `sh` ausgefuehrt | `rustup-init` pro Architektur herunterladen, SHA256 pruefen, danach die gepinnte Rust-Toolchain installieren | offen fuer P3-1 MR 3 |

## English

| Component | Current path | Target state | Status |
|---|---|---|---|
| Node.js / NodeSource | Signed NodeSource Apt source with Deb822 source file and `Signed-By` keyring | Keep; the Dockerfile no longer runs `setup_lts.x \| bash -` | done in P3-1 MR 1 |
| uv / uvx | `https://astral.sh/uv/install.sh` is executed by `sh` during the image build | Download a fixed GitHub release artifact per architecture, verify SHA256, install `uv` and `uvx` | open for P3-1 MR 2 |
| Rust / rustup | `https://sh.rustup.rs` is executed by `sh` during the image build | Download `rustup-init` per architecture, verify SHA256, then install the pinned Rust toolchain | open for P3-1 MR 3 |
