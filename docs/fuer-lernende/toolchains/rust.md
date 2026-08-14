# Rust

## Einordnung / Context

**DE:** Rust-Projekte liegen standardmäßig unter `/rust-projects`. Das Image
installiert eine festgelegte Rust-Toolchain sowie `rustfmt`, Clippy,
`rust-analyzer` und die Rust-Quellen. Cargo-Abhängigkeiten gehören in
`Cargo.toml`; `Cargo.lock` bleibt für ausführbare Anwendungen eingecheckt.

**EN:** Rust projects normally live under `/rust-projects`. The image installs
a pinned Rust toolchain plus `rustfmt`, Clippy, `rust-analyzer`, and the Rust
sources. Cargo dependencies belong in `Cargo.toml`; executable applications
keep `Cargo.lock` committed.

## Projekt anlegen / Create a Project

```bash
cd /rust-projects
cargo new hello-sandbox --bin
cd hello-sandbox
cargo fmt --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test
cargo run
```

**DE:** Nutze während der Bearbeitung `cargo fmt` zum Formatieren. Vor dem
Commit prüft `cargo fmt --check`, ob noch eine Änderung nötig wäre.

**EN:** Use `cargo fmt` to format while editing. Before a commit,
`cargo fmt --check` verifies whether formatting would still change files.

## Abhängigkeiten / Dependencies

**DE:** Füge Bibliotheken wie Tokio, Axum, Actix Web oder Serde nur dem
Projekt hinzu. Prüfe Features sorgfältig, weil sie den Build und die
Angriffsfläche verändern.

**EN:** Add libraries such as Tokio, Axum, Actix Web, or Serde only to the
project. Review features carefully because they change the build and attack
surface.

```bash
cargo tree
cargo metadata --no-deps --format-version 1
```

## Grenzen / Limits

- **DE:** `cargo audit` ist nicht als globales Werkzeug garantiert. Behaupte
  keinen erfolgreichen Audit-Lauf, bevor das Projekt es reproduzierbar
  bereitstellt. **EN:** `cargo audit` is not guaranteed as a global tool. Do
  not claim a successful audit until the project provides it reproducibly.
- **DE:** Rustup und Crates können Netzwerkzugriff benötigen. Die installierte
  Standard-Toolchain darf nicht stillschweigend geändert werden. **EN:** Rustup
  and crates may require network access. Do not silently change the installed
  default toolchain.
- **DE:** Generierte Inhalte unter `target/` sind Build-Artefakte. **EN:**
  Generated content under `target/` is build output.

Zurück zum [Toolchain-Index](README.md). / Return to the
[toolchain index](README.md).
