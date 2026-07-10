# Supply-Chain-Haertung TODO

Diese Datei verfolgt die verbleibenden P3-1-Arbeiten aus
`COMPLIANCE-PLAN_RL-SE-001.md`. Ziel ist, Remote-Installer nicht mehr blind
auszufuehren, sondern feste Artefakte ueber signierte Paketquellen oder
Pruefsummen zu binden.

## Deutsch

| Komponente | Aktueller Pfad | Zielzustand | Status |
|---|---|---|---|
| Node.js / NodeSource | Signierte NodeSource-Apt-Quelle mit Deb822-Source-Datei und `Signed-By`-Keyring | Beibehalten; kein `setup_lts.x \| bash -` mehr im Dockerfile | erledigt in P3-1 PR 1 |
| uv / uvx | Festes GitHub-Release-Artefakt `0.11.16` pro Architektur mit SHA256-Pruefung | Beibehalten; kein `astral.sh/uv/install.sh \| sh` mehr im Dockerfile | erledigt in P3-1 PR 2 |
| Rust / rustup | Festes `rustup-init`-Artefakt `1.28.2` pro Architektur mit SHA256-Pruefung | Beibehalten; kein `sh.rustup.rs \| sh` mehr im Dockerfile | erledigt in P3-1 PR 3 |
| Swift | Festes Swift-Release-Artefakt `6.3.3-noble` pro Architektur mit PGP-Signaturpruefung | Beibehalten; Swift-Toolchain wird aus `download.swift.org` geladen und vor dem Entpacken verifiziert | erledigt in Swift-Toolchain-Erweiterung |
| Syft | Festes GitHub-Release-Artefakt `1.46.0` pro Architektur mit SHA256-Pruefung | Beibehalten; Versions-ARG mit Renovate pflegen und jedes Archiv vor Installation pruefen | erledigt in Vier-Agenten-Lernumgebung |
| Agenten-CLIs | Exakt gepinnte npm-Pakete fuer Codex, Claude Code, Gemini CLI und GitHub Copilot CLI | Beibehalten; Renovate-Vorschlaege nur nach Build, Versionscheck, Smoke-Test und SBOM mergen | erledigt in Vier-Agenten-Lernumgebung |

## English

| Component | Current path | Target state | Status |
|---|---|---|---|
| Node.js / NodeSource | Signed NodeSource Apt source with Deb822 source file and `Signed-By` keyring | Keep; the Dockerfile no longer runs `setup_lts.x \| bash -` | done in P3-1 PR 1 |
| uv / uvx | Fixed GitHub release artifact `0.11.16` per architecture with SHA256 verification | Keep; the Dockerfile no longer runs `astral.sh/uv/install.sh \| sh` | done in P3-1 PR 2 |
| Rust / rustup | Fixed `rustup-init` artifact `1.28.2` per architecture with SHA256 verification | Keep; the Dockerfile no longer runs `sh.rustup.rs \| sh` | done in P3-1 PR 3 |
| Swift | Fixed Swift release artifact `6.3.3-noble` per architecture with PGP signature verification | Keep; the Swift toolchain is downloaded from `download.swift.org` and verified before extraction | done in Swift toolchain extension |
| Syft | Fixed GitHub release artifact `1.46.0` per architecture with SHA256 verification | Keep; maintain the version ARG with Renovate and verify every archive before installation | done in four-agent learner environment |
| Agent CLIs | Exactly pinned npm packages for Codex, Claude Code, Gemini CLI, and GitHub Copilot CLI | Keep; merge Renovate proposals only after build, version checks, smoke test, and SBOM | done in four-agent learner environment |
