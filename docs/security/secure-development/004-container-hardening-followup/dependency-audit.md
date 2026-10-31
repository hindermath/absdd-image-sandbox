# Dependency Audit — Feature 004

Stand: 2026-10-31. Quelle des installierten Sollstands: `Dockerfile`, `renovate.json`,
`home-baseline.lock.json`. Dies ist eine Quell- und Vertragsprüfung. Ein finaler
Image-Build, dessen SBOM und Schwachstellenbewertung gehören zu T059/T063.

## Deutsch

### Quellen, Versionen und Installationswege

| Inhalt / Maintainer | Version oder Pin | Register / Bezug | Build-Ausführung und Integrität | Lizenzstand |
|---|---|---|---|---|
| .NET SDK / Microsoft | 10.0, MCR-Digest `747cbade…1f66d2` | MCR `mcr.microsoft.com/dotnet/sdk` | `FROM` mit Digest; zusätzlich Kompatibilitäts-SDK 10.0.303 aus Microsoft Builds mit SHA-512 je Architektur | Microsoft-.NET-Bedingungen und Komponentenlizenzen: Image-SBOM/Rechteprüfung Open |
| Ubuntu-Pakete, OpenJDK 25, Node.js 24 / Ubuntu, Eclipse Adoptium/Ubuntu, NodeSource | Ubuntu 24.04-Basis, Java-/Node-Major | Ubuntu APT, NodeSource APT mit `Signed-By` | APT-Signaturen; NodeSource-Schlüssel über TLS geladen, Fingerprint nicht lokal gepinnt; Paket-Patchversionen nicht exakt | Paketbezogene Lizenzliste aus finaler SBOM Open |
| Maven / Apache | 3.10.0 | Apache CDN, danach Apache Archive | Archiv-Fallback nur nach Downloadfehler; feste SHA-512 im Dockerfile, vor Extraktion geprüft | Apache-2.0 (Upstream); Archiv-Lizenz im Image zu prüfen |
| CPython / Astral python-build-standalone | 3.15.1, Build 20261021 | GitHub Releases | Native AMD64/ARM64-Archive mit unterschiedlichen festen SHA-256; `/usr/bin/python3` bleibt Ubuntu-Python | Python-/Build-Standalone-Komponentenlizenz im Image Open |
| PowerShell / Microsoft | 7.6.8 | Microsoft-Paketquelle | Native Nupkg, feste SHA-256 pro Architektur und Versionstest | MIT (Upstream); Paketprüfung Open |
| Go und Werkzeuge / Go-Team, x/tools, honnef, x/vuln, Delve | Go 1.27.3; gopls 0.24.0; staticcheck 0.8.2; govulncheck 1.9.0; Delve 1.27.2 | go.dev, Go-Module | Go-Tarballs feste native SHA-256; Werkzeuge als versionsgebundene Module kompiliert | BSD-/MIT-/sonstige Modultexte und transitive Rechte in SBOM Open |
| Rust / Rust-Projekt | Rust 1.99.1, rustup 1.29.2 | static.rust-lang.org | Native rustup-Datei mit gleichherkunftiger SHA-256-Begleitdatei; danach gepinnte Toolchain | MIT OR Apache-2.0 (Upstream); genaue Komponentenrechte Open |
| Swift / Swift-Projekt | 6.4.1 Ubuntu 24.04 | download.swift.org | Native Archivsignatur und fest gepinnter Swift-6.x-Fingerprint per `gpg --assert-signer` | Apache-2.0 with Runtime Library Exception (Upstream); Archivprüfung Open |
| Node/npm / NodeSource, npm | Node 24, npm 12.2.1 | NodeSource APT, npm Registry | APT-Signatur; npm über Registry, keine feste transitive Lockdatei | Node/npm und Transitivrechte in finaler SBOM Open |
| OpenCode, Codex, Claude, Gemini, Copilot / jeweilige Maintainer | 2.1.4; 0.164.0; 2.1.310; 0.65.0; 1.0.103 | npm Registry | Exakte Top-Level-Versionen; nur benannte native npm-Hooks später erlaubt; kein transitive Lockfile | Upstream OpenCode MIT, Codex/Gemini Apache-2.0; exakte npm-Tarball-Rechte für alle fünf Open |
| Antigravity / Google | 1.4.7 | GitHub Release | Native AMD64/ARM64-Archive mit festen SHA-256 | Nutzungsbedingungen statt angenommener OSS-Lizenz; Rights Review Open |
| Syft / Anchore; uv / Astral | 1.55.0; 0.13.5 | GitHub Releases | Native AMD64/ARM64-Archive mit getrennten, fest eingebetteten SHA-256; keine mutable Begleitdatei als einziger Anker | Syft Apache-2.0; uv Apache-2.0 OR MIT; Archiv-/Transitivrechte Open |
| actionlint, Pandoc, Lychee, Typst, Tinymist / jeweilige Upstream-Projekte | 1.7.12; 3.12.1; 0.24.2; 0.15.1; 0.15.10 | GitHub Releases | Native AMD64/ARM64-Archive mit festen SHA-256 vor Extraktion | jeweilige Upstream-Lizenztexte im finalen Image Open |
| Spec Kit / GitHub | 1.2.3, Commit `5ea8b1cf…97d8c0` | Git-Repository | `uv tool install` vom exakten Commit; Build prüft Paketversion; lokaler Copy-Patch und Tests | Upstream-Lizenz für exakten Commit und transitive Pakete Open |
| Home-Baseline / hindermath | Commit `932a5eac…a27d9f` | öffentliches Git-Repository | Shallow-Fetch des Commits; exakte `FETCH_HEAD`-Prüfung; Lizenzdatei und Lernstartdatei verlangt | `MIT` im Lock; Inhalt der Lizenzdatei und Rechte vor Weitergabe prüfen |

Die Versionsangaben sind Build-Inputs, keine Aussage über tatsächlich gebaute
Artefakte. Die verlinkten [Go-Downloads](https://go.dev/dl/),
[Swift-Signierschlüssel](https://www.swift.org/download/#swift-signing-keys),
[Syft-Releases](https://github.com/anchore/syft/releases/tag/v1.55.0) und
[uv-Releases](https://github.com/astral-sh/uv/releases/tag/0.13.5) sind
öffentliche Upstream-Quellen. Die Upstream-Repositories nennen
[Codex Apache-2.0](https://github.com/openai/codex/blob/main/docs/license.md),
[Gemini Apache-2.0](https://github.com/google-gemini/gemini-cli/blob/main/docs/resources/tos-privacy.md),
[uv Apache-2.0 OR MIT](https://github.com/astral-sh/uv/blob/main/README.md),
[Syft Apache-2.0](https://github.com/anchore/syft/blob/main/LICENSE) und
[OpenCode MIT](https://github.com/anomalyco/opencode/blob/main/LICENSE).
Diese aktuellen Repo-Angaben ersetzen keine Paket- und Release-spezifische
Lizenzprüfung.

### Befund und Disposition

- Die vorhandenen Syft-/uv-Digests und die Swift-Signerbindung beheben die
  entsprechenden Standard-Scan-Befunde auf Quellniveau. Der native Build und
  das finale Image bleiben unbewertet.
- `renovate.json` erkannte bislang Home-Baseline-Schema 2 nicht: sein Regex
  verlangte einen `tag`, der im aktuellen Lock nicht existiert. Der tote
  Manager wurde entfernt. Ein neuer Commit-Pin benötigt bewusste Prüfung;
  keine Renovate-PR wird hierfür behauptet.
- Kritische öffentliche Bezugspunkte sind MCR, Ubuntu und NodeSource APT,
  Apache CDN/Archive, GitHub Releases und Git, go.dev, Swift, Rust-Distribution,
  Microsoft-Paket-/Buildserver sowie npm. Digest/Signatur senken das
  Austauschrisiko; CDN, Schlüsselbezug, npm-Transitiven und gleichherkunftige
  Rust-Prüfsumme bleiben gesonderte Grenzen.
- Eine [OpenSSF Scorecard](https://securityscorecards.dev/) für die konkreten
  Upstreams wurde in dieser Quellprüfung nicht ausgeführt. Owner: Repository
  Maintainer mit Security Review; vor Release/Weitergabe oder Quellwechsel.
  Weder Scorecard-Score noch SLSA-Level oder Signaturgrad wird erfunden.
- T033: 38 isolierte Tests für Pins, native Architektur, Maven-Fallback,
  falsche Prüfsummen, Home-Baseline-Lock und Spec-Kit-Patch bestanden am
  2026-10-31 auf macOS ARM64. Das ist kein Container-Build.
- Die [Kontrollmatrix](control-matrix.md) ordnet diese Quellnachweise G04,
  H-344-04 und AC-H-344-04 zu; das [Krypto-/TLS-Inventar](crypto-tls-inventory.md)
  begrenzt G07/H-344-07/AC-H-344-07. Beide Gruppen bleiben wegen der offenen
  Image-, Rechte- und Security-Review-Nachweise `Not Assessed`.

## English

This source audit binds the intended versions, maintainers, registries,
download scripts, integrity checks and license questions to the current
Dockerfile and locks. The table above is the authoritative row-level inventory;
the final image, package-level rights and vulnerabilities remain open for
T059/T063. The prior Renovate rule for tag plus commit could not match the
active commit-only home-baseline lock. It was removed, and commit updates now
require explicit manual review. The 38 isolated T033 tests passed on macOS
ARM64, without a build or provider call. The repository maintainer and Security
Review must assess upstream Scorecards and exact artifact rights before release
or distribution. Source integrity checks do not establish a SLSA level or
permission to distribute third-party content.
