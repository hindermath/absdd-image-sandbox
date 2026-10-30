# Issue #104: MSL-Sprachauswahl beim Image-Build: sieben Profile mit .NET-Basis und all als Standard

Source: https://github.com/hindermath/absdd-image-sandbox/issues/104
Retrieved through GitHub connector: 2026-10-28
Issue updatedAt: 2026-10-27T22:53:01Z
Proof boundary: immutable local requirements snapshot; no upstream implementation acceptance.

## Deutsch

### Gemeinsamer nächster Feature-Update-Block

Dieses Issue gehört zusammen mit den folgenden Issues zum **nächsten Feature-Update-Block dieses Repositories**:

- [#101 – Ubuntu 26.04 und Basisimage](https://github.com/hindermath/absdd-image-sandbox/issues/101)
- [#102 – OpenCode-Webinterface](https://github.com/hindermath/absdd-image-sandbox/issues/102)
- [#104 – MSL-Sprachauswahl](https://github.com/hindermath/absdd-image-sandbox/issues/104)

Gemeinsames Ziel: Ubuntu-26.04-Basis, OpenCode-Webbetrieb und wählbare MSL-Profile als zusammenhängendes Sandbox-Update bereitstellen. #101 bildet die technische Basis; #102 und #104 werden darauf abgestimmt. Die Umsetzung kann in getrennten Änderungen erfolgen. Vor Abschluss des Blocks die Kombination auf den finalen Images einschließlich Profil-, Web-, Audit- und Plattformprüfungen validieren. Der Block ist erst abgeschlossen, wenn alle drei Issues ihre Abnahmekriterien erfüllen.

### Ziel und aktueller Quellstand

Die beim Build auswählbaren MSL-Profile (Memory-Safe Languages, speichersichere Programmiersprachen) aus [MR !74](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/merge_requests/74) übernehmen. .NET/C# bleibt immer enthalten; zusätzlich keine, genau eine oder alle fünf weiteren Sprach-Toolchains auswählen. Der bisherige vollständige Sandbox-Umfang bleibt mit `all` der Standard.

Am 2026-10-27 live geprüft: MR !74 ist als `0499e06162e0b7da93d930c07955d68d537d85b0` im Oktober-Kandidaten integriert; MR !76 dokumentiert den Alpha-Abschluss. Aktueller Kandidat: `chore/refresh-sandbox-image-2026-10` bei `4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30`. Der übergeordnete [MR !64](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/merge_requests/64) ist weiterhin offen und Draft. Quell-`main` enthält durch !75/!77 die Anleitung, aber noch nicht die Profilimplementierung. Alpha-Abschluss und Kandidatenintegration sind keine allgemeine Release-/Betriebsfreigabe.

### Profile

| Wert | Enthaltene Entwicklungs-Toolchains |
|---|---|
| `dotnet` | .NET/C# |
| `java` | .NET/C# und Java mit Maven |
| `go` | .NET/C# und Go mit gopls, Staticcheck, Govulncheck, Delve |
| `rust` | .NET/C# und Rust mit Cargo, Rustfmt, Clippy, Rust Analyzer |
| `python` | .NET/C# und Python-Entwicklung einschließlich venv |
| `swift` | .NET/C# und Swift mit Package Manager und SourceKit-LSP |
| `all` | alle sechs; kompatibler Standard |

### Umsetzung

- [ ] Gemeinsame Image-Stufe und feste Ziele `ade-dotnet`, `ade-java`, `ade-go`, `ade-rust`, `ade-python`, `ade-swift`, `ade-all` einführen. Direkter Build ohne Ziel und Compose ohne Auswahl bleiben `all`.
- [ ] Compose-Buildziel über `ADE_MSL_PROFILE` in lokaler `.env` wählen; `.env.example` ergänzen. Klar erklären: Build-Auswahl, kein Laufzeitschalter; Änderung benötigt Neubau und Container-Neuerstellung, erhält aber Volumes.
- [ ] Installationen und zugehörige LSP-/Analysewerkzeuge nur im gewählten Profil ausführen. Ungültige Profile vor dem Build ablehnen. Profilmanifest unter `/usr/local/share/ade/msl-profile.json`, Laufzeitvariable und generisches projektspezifisches Image-Label konsistent erzeugen. Organisationsspezifisches Quell-Label nicht ungeprüft übernehmen.
- [ ] Java 25 und gepinntes CPython 3.15 dieses Repos erhalten: Java-/Python-Entwicklung nur in entsprechenden Profilen und `all`; Ubuntu-`python3` für interne Skripte in allen Profilen erhalten. CPython in `/opt/cpython` von System-Python trennen. Quell-Java-21 und System-Python-Entwicklungsprofil nicht kopieren.
- [ ] PowerShell, Node/npm, uv, alle hier vorhandenen Agenten einschließlich Gemini/Copilot, Spec Kit, 14 Presets, Home-Baseline-/Runtime-Verträge und Dokumentationswerkzeuge in jedem Profil erhalten. Nicht gewählte Entwickler-Toolchains dürfen nicht über einen indirekten Installationsweg wieder hineinkommen.
- [ ] Bash-/PowerShell-Build-/SBOM-Wrapper atomar um `--profile`/`-Profile`, passende Umgebungsvariable und `all`-Fallback erweitern; Profilpräzedenz dokumentieren. Bei `--skip-build`/`-SkipBuild` tatsächliches Image-Label gegen erwartetes Profil prüfen. Profil und Architektur im SBOM-Dateinamen unterscheiden.
- [ ] Bestehende Sicherheitsanforderungen der Zielwrapper erhalten: Podman bleibt Zielruntime; imageintegriertes oder exakt gepinntes Host-Syft, kein beweglicher Scanner-Fallback. Quellwrapper unterstützen weitere Pfade und sind kein vollständiger Ersatz.
- [ ] Vorhandenes `scripts/smoke-test-toolchains.sh` profilbewusst erweitern; Quell-`install-msl-profile.sh` und `test-msl-profile.sh` angepasst verwenden. Positive und negative Prüfungen sowie kleine ausführbare Sprachprojekte vorsehen.
- [ ] Bestehende Leserpfade in `docs/fuer-lernende/` und `docs/betrieb/`, README, AGENTS und Toolchain-/Sicherheitsdokumentation Deutsch zuerst/gleichwertig Englisch aktualisieren. Gemeinsame Infrastruktur von ausgewählter Entwicklungssprache unterscheiden; Profile, Neubau, Rückkehr zu `all`, Speicherbedarf und Fehlerhilfe textorientiert erklären. Normaler Stop bleibt Audit-Wrapper ohne Volume-Löschung.

### Abnahme

- [ ] Alle sieben Profile nativ für AMD64 und ARM64 bauen und ausführen; Host/Engine/Image-Architektur, Git-Head, Profil, Datum, Image-ID und Exitcodes pro Lauf festhalten. Fehlende Plattformen offen lassen.
- [ ] Gewählte Toolchains samt kleinen Projekten bestehen; nicht gewählte Sprach-/Entwicklerbefehle fehlen. Infrastruktur-`python3`/PowerShell/Node und gemeinsame Werkzeuge funktionieren trotzdem.
- [ ] Ungültiges Profil und Image-/Profilabweichung inklusive SkipBuild schlagen fehl; Bash/PowerShell haben gleiche Semantik. `all` erhält sämtliche bisherigen sechs Toolchains und die bestehende Versions-/Integritätsprüfung.
- [ ] Vollständige gemeinsame Policy-/Audit-/Dokumentationssuite mindestens für `dotnet` und `all`; OpenCode-Webauth, Healthcheck, Non-root, CapEff=0 und NoNewPrivs=1 bleiben funktionsfähig.
- [ ] Echter Compose-Neubau, Start, Profilwechsel und regulärer Audit-Stop praktisch prüfen. Compose- und Direktbuild-Ergebnisse getrennt ausweisen.
- [ ] Vor Image-Delivery frische, profil-/architektur-/imagegebundene CycloneDX-SBOM erstellen. Größen nur mit Datum, Architektur und Imagebezug berichten. Relevante Regressionen, Compose-Validierung ohne Secrets, Pre-Commit und `git diff --check` bestehen.

### Abhängigkeiten und Referenzen

#101 liefert die Ubuntu-26.04-Basis; #102 den gemeinsamen Webbetrieb. In getrennten Änderungen entwickeln und die Kombination auf den finalen Images prüfen. Kein automatischer Start eines bestehenden Spec-Kit-Laufs.

- [Installer](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/scripts/install-msl-profile.sh), [Profiltests](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/scripts/test-msl-profile.sh), [Dockerfile](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/Dockerfile)
- [Profilanleitung und Alpha-Abschluss](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/docs/alpha-test-msl-profiles-2026-10.md)
- [AMD64-Protokoll](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/docs/security/agent-session-log/2026-10-27-1033.md), [ARM64-Bericht](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/docs/security/mr74-macos-arm64-acceptance-2026-10-27.md)

Berichte sind datierte Quellnachweise, keine eigene Abnahme. Der ARM64-Bericht gilt für den dort genannten früheren Testcommit, nicht pauschal für den späteren Kandidaten-Head. Planbezug: P0-2/P0-3, P1-2/P1-5, P2-3.

## English

### Shared next feature update block

This issue and the following issues form the **next feature update block for this repository**:

- [#101 – Ubuntu 26.04 and base image](https://github.com/hindermath/absdd-image-sandbox/issues/101)
- [#102 – OpenCode web interface](https://github.com/hindermath/absdd-image-sandbox/issues/102)
- [#104 – MSL language selection](https://github.com/hindermath/absdd-image-sandbox/issues/104)

Shared goal: deliver the Ubuntu 26.04 base, OpenCode web operation and selectable MSL profiles as one coordinated sandbox update. #101 provides the technical foundation; align #102 and #104 with it. Implementation may use separate changes. Before closing the block, validate the combined final images with profile, web, audit and platform checks. The block is complete only when all three issues meet their acceptance criteria.

### Goal and source

Adopt build-time memory-safe language profiles from MR !74: always include .NET/C# and select none, one, or all optional development toolchains. Keep `all` as the compatible default. Live source check on 2026-10-27: !74 is merged into the October candidate, !76 closes the alpha, candidate head is `4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30`. Parent MR !64 remains open/Draft; source main contains guidance through !75/!77, not the implementation. This is no general release or operational approval.

The seven values in the table mean .NET only, .NET plus the named language, or all six. Source code and dated AMD64/ARM64 evidence are linked above; the ARM64 report binds an earlier tested revision rather than every later candidate.

### Implementation and acceptance

- [ ] Add a shared core and seven fixed `ade-<profile>` targets; default direct builds and Compose to `all`. Select through local `ADE_MSL_PROFILE`; document rebuild/recreation rather than runtime switching, preserving volumes.
- [ ] Install selected toolchains and their language/analysis tools only. Reject invalid profiles before building; align runtime variable, JSON manifest and a generic project-specific image label.
- [ ] Preserve this repo's Java 25 and pinned CPython 3.15 for their development profiles and `all`; retain Ubuntu system `python3` for internal scripts in every profile. Do not copy source Java 21 or its system-Python development choice.
- [ ] Keep PowerShell, Node/npm, uv, every existing agent including Gemini/Copilot, Spec Kit, all 14 presets, Home Baseline/runtime contracts and documentation tools in every profile. Prevent indirect installation of excluded development toolchains.
- [ ] Update both build/SBOM wrappers with profile options, environment/default precedence, image-label checks including SkipBuild, and profile/architecture filenames. Preserve Podman-only runtime and integrated or exactly pinned host Syft; do not copy the source's moving scanner fallback.
- [ ] Adapt existing smoke tests plus source installer/profile tests for positive/negative checks and executable language examples.
- [ ] Update existing learner and operations paths, README, AGENTS, toolchain/security guidance in equivalent German/English. Explain profiles, infrastructure versus development runtimes, rebuild, return to all, storage and troubleshooting. Keep normal audit-wrapper shutdown without deleting volumes.
- [ ] Build/run all seven profiles natively on AMD64 and ARM64; record date, revision, profile, host/engine/image architecture, image ID and exits. Missing coverage stays open.
- [ ] Prove selected tools/projects work and excluded development commands are absent while infrastructure remains functional. Invalid profiles and image mismatches fail; Bash/PowerShell agree; all preserves existing versions and integrity checks.
- [ ] Run full common policy/audit/documentation suites at least for dotnet and all; preserve web authentication, health, non-root, zero capabilities and no-new-privileges.
- [ ] Practically test Compose build/start/profile change/audited stop separately from direct builds. Produce fresh profile/architecture/image-bound SBOMs before delivery; date measured sizes. Pass relevant regressions, secret-safe Compose validation, Pre-Commit and diff checks.

Dependencies: #101 for Ubuntu 26.04 and #102 for shared web operation. Develop separately and verify the final combination. No existing autonomous run is resumed. Plan references: P0-2/P0-3, P1-2/P1-5, P2-3.

