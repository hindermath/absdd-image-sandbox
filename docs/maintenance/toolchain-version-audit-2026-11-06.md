# Versionsnachweis 2026-11-06 / Version evidence 2026-11-06

## Deutsch

Stand: 2026-11-06, Arbeitsbaum vor PR und vor finaler Image-Abnahme. Der
offizielle, read-only PowerShell-Checker
`pwsh -NoProfile -File scripts/update-toolchain-pins.ps1 -Action Check -Json`
wurde im finalen ARM64-`all`-Image mit read-only Repository-Mount und
Quellenzugriff ausgefuehrt: Gesamtstatus `Ready`, Exit 0, alle 28 Gruppen
erreicht (2026-11-06). Der Hostlauf ausserhalb der Podman-VM war wegen
gesperrter DNS-Aufloesung `Blocked`; er ist kein Quellen-Nachweis. Ein frueherer
erfolgreicher Lauf lieferte Python 3.15.2 vom Build 20261026 mit beiden
Asset-Digests. Der Offline-Vertragstest bestand mit 75 Assertions. Die
verbindlichen Werte und Archiv-Hashes stehen im [Dockerfile](../../Dockerfile),
die Quellen und Gruppen im [Pin-Register](../../scripts/config/toolchain-pins.json).

| Pin oder Gruppe | Gewählter Stand | Offizielle Quelle und Entscheidung |
|---|---|---|
| .NET-Basis | `10.0.403-resolute` | [MCR SDK](https://mcr.microsoft.com/v2/dotnet/sdk/manifests/10.0.403-resolute), Multiarch-Index `sha256:2107242a0f56885d09f8a536ac300f6cb1a2b3f6d40605e5ff81bbd83ad91e3f` für Linux AMD64 und ARM64 am 2026-11-06 geprüft |
| Java | 25 | [Adoptium-LTS-Kanal](https://api.adoptium.net/v3/info/available_releases), `ChannelPinned`; Ubuntu lieferte im nativen ARM64-`java`-Build OpenJDK 25.0.4.1 aus `resolute-updates` |
| Maven | 3.10.0 | [Apache Maven Metadata](https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/maven-metadata.xml), `Current`; SHA-512 im Dockerfile |
| Python + Builddatum | 3.15.2 + 20261026 | [Astral Python-Release](https://github.com/astral-sh/python-build-standalone/releases/tag/20261026); AMD64 SHA-256 `7b03163a980c607ba8194709d4a4086735a7a9c488cc475b098157306927b36b`, ARM64 `0f23351c03b39beb880de668976074fcc3c082d9c3b03d0b43185632b2b270a0`; finaler VM-Checker `Current` |
| PowerShell | 7.6.9 | [Microsoft PowerShell](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9), `Current`; Linux x64/ARM64 SHA-256 im Dockerfile |
| Go | 1.27.3 | [Go-Downloads](https://go.dev/dl/?mode=json), `Current`; offizielle AMD64-/ARM64-Hashes im Dockerfile |
| gopls, staticcheck, govulncheck, Delve | v0.24.0, v0.8.2, v1.9.0, v1.27.2 | jeweilige [Go-Modulquelle](https://proxy.golang.org/), alle `Current` |
| Rust, rustup | 1.99.1, 1.29.3 | [Rust stable](https://static.rust-lang.org/dist/channel-rust-stable.toml) und [rustup stable](https://static.rust-lang.org/rustup/release-stable.toml), beide `Current`; rustup-Init-Hashes für beide Architekturen im Dockerfile |
| Swift | 6.4.2-resolute | [Swift 6.4.2 für Ubuntu 26.04](https://www.swift.org/install/linux/ubuntu/26_04/); beide Tarballs und beide `.sig`-Dateien per HTTPS HEAD mit 200 am 2026-11-06 geprüft. Das lokale Tool-Register wurde mit dem Pin fortgeschrieben; GPG-Signatur und Fingerprint im ARM64-Build bestätigt, AMD64-Build offen |
| Node.js, npm | Kanal 24, 12.2.2 | [Node-LTS-Index](https://nodejs.org/dist/index.json) `ChannelPinned`; nativer ARM64-`all`-Build liefert Node 24.22.2; [npm-Registry](https://registry.npmjs.org/npm) `Current` |
| uv | 0.13.7 | [uv-Release](https://github.com/astral-sh/uv/releases/tag/0.13.7), `Current`; beide SHA-256 im Dockerfile |
| OpenCode | 2.1.4 | [npm-Registry](https://registry.npmjs.org/%40opencode%2Fcli), höchster stabiler 2.1-Patch. 2.2.5 ist eine andere Minor-Linie |
| Codex | 0.164.0 | [npm-Registry](https://registry.npmjs.org/%40openai%2Fcodex), 0.167.0 liegt außerhalb der gewählten Minor-Linie |
| Claude Code | 2.1.319 | [npm-Registry](https://registry.npmjs.org/%40anthropic-ai%2Fclaude-code), `Current` |
| Gemini CLI | 0.65.0 | [npm-Registry](https://registry.npmjs.org/%40google%2Fgemini-cli), 0.67.0 außerhalb der Minor-Linie |
| Antigravity CLI | 1.4.7 | [GitHub-Release](https://github.com/google-antigravity/antigravity-cli/releases), 1.5.2 außerhalb der Minor-Linie; beide bisherigen SHA-256 im Dockerfile |
| Copilot CLI | 1.0.106 | [npm-Registry](https://registry.npmjs.org/%40github%2Fcopilot), `Current` |
| Syft | 1.55.0 | [Syft-Release](https://github.com/anchore/syft/releases), 1.57.0 außerhalb der Minor-Linie; beide SHA-256 im Dockerfile |
| actionlint | 1.7.12 | [actionlint-Release](https://github.com/rhysd/actionlint/releases), `Current`; beide SHA-256 im Dockerfile |
| .NET-Kompatibilitäts-SDK | 10.0.303 | [Microsoft .NET 10 Metadaten](https://dotnetcli.blob.core.windows.net/dotnet/release-metadata/10.0/releases.json), `Current` im freigegebenen 10.0.3xx-Band; SHA-512 für beide Architekturen im Dockerfile |
| Pandoc | 3.12.1 | [Pandoc-Release](https://github.com/jgm/pandoc/releases), 3.13 außerhalb der Minor-Linie; beide SHA-256 im Dockerfile |
| Lychee, Typst, Tinymist | 0.24.2, 0.15.1, 0.15.12 | jeweilige GitHub-Releases laut Pin-Register, alle `Current`; beide SHA-256 pro Archiv im Dockerfile |
| Spec Kit | 1.2.3, Commit `5ea8b1cf0a38699340a38e00d02770308997d8c0` | [offizielles Release](https://github.com/github/spec-kit/releases/tag/v1.2.3); unveraenderter exakter Commit und Paketversionspruefung im Dockerfile. Nicht Teil des PowerShell-Pin-Checkers; der vorhandene Release-Nachweis vom 2026-10-25 bleibt massgeblich |
| home-baseline-Referenz | Commit `9107cff07a73892076c18c6a28a4e396a250f519` | [Quell-Repository](https://github.com/hindermath/home-baseline); unveraenderter Commit in `home-baseline.lock.json`, beim ARM64-Build als read-only Referenz installiert. Nicht Teil des PowerShell-Pin-Checkers; kein Update in diesem Feature-Block |

Das 30. Dockerfile-ARG `ADE_MSL_PROFILE=all` ist ein Build-Selektor, keine
Hersteller-Version. npm-Registry-Versionen besitzen hier keinen im Dockerfile
festgelegten Paketdigest; die Paketinstallation und die finale CycloneDX-SBOM
bleiben gesonderte Build-Nachweise. Die Quellprüfung ersetzt weder einen
erfolgreichen Image-Build noch native AMD64-/ARM64-Tests.

## English

Status: 2026-11-06, working tree before PRs and final image acceptance. The
read-only PowerShell checker queried official sources inside the final ARM64
`all` image with the repository mounted read-only. All 28 groups were reached;
the overall status was `Ready` with exit 0 on 2026-11-06. A host-side run was
`Blocked` by sandbox DNS and is not source evidence. An earlier successful
run resolved Python 3.15.2 build 20261026 and both asset digests. The offline contract test
passed 75 assertions. The table above records every selected pin, its source,
date and any deliberately held newer line. Exact archive checksums are in the
Dockerfile and source mapping is in the pin registry.

The Microsoft .NET SDK 10.0.403 Resolute index digest shown above includes
Linux AMD64 and ARM64. Java 25 and Node 24 are pinned channels: Ubuntu and
NodeSource supply their specific package patches during the build. The native
ARM64 Java profile used Ubuntu OpenJDK 25.0.4.1; the final ARM64 `all`
profile used Node 24.22.2. Maven
3.10.0, PowerShell 7.6.9, Go 1.27.3, gopls v0.24.0, staticcheck v0.8.2,
govulncheck v1.9.0, Delve v1.27.2, Rust 1.99.1, rustup 1.29.3, uv 0.13.7,
Claude Code 2.1.319, Copilot CLI 1.0.106, actionlint 1.7.12, the .NET
compatibility SDK 10.0.303, Lychee 0.24.2, Typst 0.15.1, Tinymist 0.15.12
and npm 12.2.2 were current in their selected lines. Swift 6.4.2 Resolute has
signed archives for both architectures; both tarballs and signature files
returned HTTP 200 to HEAD on 2026-11-06. The local tool registry now matches
the pin. GPG signature and expected signer fingerprint passed in the ARM64
build; native AMD64 remains open. OpenCode 2.1.4 is
the highest stable 2.1 patch.
Codex 0.164.0, Gemini CLI 0.65.0, Antigravity CLI 1.4.7, Syft 1.55.0 and
Pandoc 3.12.1 stay pinned because the checker found releases in newer minor
lines. The unchanged Spec Kit release commit and home-baseline reference
commit are also recorded above; they are outside the PowerShell pin checker
and retain their previous evidence. The profile selector is not a vendor
version. npm package digests are
not locked here; installation, final CycloneDX SBOM and native architecture
tests remain separate proof.
