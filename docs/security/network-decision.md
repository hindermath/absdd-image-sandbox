# Netzwerkentscheidung: Compose-Egress

Stand: 2026-05-15

## Deutsch

Entscheidung: Die `ade`-Lernumgebung bleibt vorerst am Compose-Default-Bridge-Netz mit freiem ausgehendem Netzwerkzugriff.

Begruendung: Die Sandbox ist eine Ausbildungs- und Entwicklungsumgebung. Mehrere vorgesehene Workflows benoetigen ausgehenden Zugriff auf externe Paketregister, Modell-Endpunkte und Installationsquellen:

- `chat-ai.academiccloud.de` fuer OpenCode-Modellzugriff
- Azure/OpenAI-Endpunkte fuer Codex CLI, sofern durch die Betriebsumgebung konfiguriert
- GitLab CE / Container Registry der GWDG
- Debian- und Microsoft-Paketquellen
- `deb.nodesource.com`
- `go.dev`
- `static.rust-lang.org` fuer gepinnte `rustup-init`-Artefakte und Rust-Toolchains
- GitHub fuer uv-Release-Artefakte, Spec Kit, Governance-Presets, Gitleaks und weitere Entwicklungswerkzeuge
- Maven Central
- NuGet
- crates.io
- npm Registry

Risikobewertung: Freier Egress vergroessert die technische Angriffsoberflaeche. Das Risiko wird fuer diese Lernumgebung vorerst akzeptiert, weil der Container isoliert laeuft, Host-Mounts explizit begrenzt sind, Codex-Shell-Netzwerkzugriff in `codex/config.toml` deaktiviert ist und OpenCode/Codex riskante Aktionen ueber Repository-Regeln bzw. Genehmigungen einschränken.

Akzeptiert bis: `_TODO_ (vom Owner einzutragen, Empfehlung: 2026-08-15)`

Offener Punkt: Variante B mit echter Egress-Allow-List soll erneut bewertet werden, sobald klar ist, ob ein geeigneter Proxy, DNS-Filter oder eine vergleichbare RZ-Infrastruktur verfuegbar ist.

## English

Decision: The `ade` learning environment remains on the Compose default bridge network with unrestricted outbound network access for now.

Rationale: The sandbox is a training and development environment. Several intended workflows need outbound access to external package registries, model endpoints, and installation sources:

- `chat-ai.academiccloud.de` for OpenCode model access
- Azure/OpenAI endpoints for Codex CLI when configured by operations
- GWDG GitLab CE / container registry
- Debian and Microsoft package sources
- `deb.nodesource.com`
- `go.dev`
- `static.rust-lang.org` for pinned `rustup-init` artifacts and Rust toolchains
- GitHub for uv release artifacts, Spec Kit, governance presets, Gitleaks, and other development tools
- Maven Central
- NuGet
- crates.io
- npm registry

Risk assessment: Unrestricted egress increases the technical attack surface. This risk is accepted for the learning environment for now because the container is isolated, host mounts are explicitly limited, Codex shell network access is disabled in `codex/config.toml`, and OpenCode/Codex risky actions are constrained through repository rules or approvals.

Accepted until: `_TODO_ (to be entered by owner, recommendation: 2026-08-15)`

Open item: Variant B with a real egress allow-list should be reassessed once it is clear whether a suitable proxy, DNS filter, or comparable data-center infrastructure is available.
