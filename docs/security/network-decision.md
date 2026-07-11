# Netzwerkentscheidung: Compose-Egress

Stand: 2026-07-10

## Deutsch

Entscheidung: Die `ade`-Lernumgebung bleibt vorerst am Compose-Default-Bridge-Netz mit freiem ausgehendem Netzwerkzugriff.

Begruendung: Die Sandbox ist eine Ausbildungs- und Entwicklungsumgebung. Mehrere vorgesehene Workflows benoetigen ausgehenden Zugriff auf externe Paketregister und Installationsquellen:

- KI-Provider-Endpunkte fuer Codex, Claude Code, Antigravity CLI, GitHub Copilot CLI
  und optional OpenCode, sofern Anmeldung und Betriebsumgebung sie freigeben
- MCR (`mcr.microsoft.com`) fuer das gepinnte .NET-SDK-Basisimage beim Podman-Build
- Ubuntu-Paketquellen
- `deb.nodesource.com`
- `go.dev`
- `static.rust-lang.org` fuer gepinnte `rustup-init`-Artefakte und Rust-Toolchains
- GitHub fuer uv-Release-Artefakte, Spec Kit, Governance-Presets, Gitleaks und weitere Entwicklungswerkzeuge
- Maven Central
- NuGet
- crates.io
- npm Registry

Risikobewertung: Freier Egress vergroessert die technische Angriffsoberflaeche. Das Risiko wird fuer diese Lernumgebung vorerst akzeptiert, weil der Container isoliert laeuft, Host-Mounts explizit begrenzt sind, Codex-Shell-Netzwerkzugriff in `codex/config.toml` deaktiviert ist und alle Agenten an Repository-Regeln, enge Arbeitsauftraege und menschliche Genehmigungen gebunden sind. Die vier CLI-Installationen sind keine Providerfreigabe.

Akzeptiert bis: `_TODO_ (vom Owner einzutragen, Empfehlung: 2026-08-15)`

Offener Punkt: Variante B mit echter Egress-Allow-List soll erneut bewertet werden, sobald klar ist, ob ein geeigneter Proxy, DNS-Filter oder eine vergleichbare RZ-Infrastruktur verfuegbar ist.

## English

Decision: The `ade` learning environment remains on the Compose default bridge network with unrestricted outbound network access for now.

Rationale: The sandbox is a training and development environment. Several intended workflows need outbound access to external package registries and installation sources:

- AI-provider endpoints for Codex, Claude Code, Antigravity CLI, GitHub Copilot CLI,
  and optional OpenCode when approved by sign-in and operating policy
- MCR (`mcr.microsoft.com`) for the pinned .NET SDK base image during Podman builds
- Ubuntu package sources
- `deb.nodesource.com`
- `go.dev`
- `static.rust-lang.org` for pinned `rustup-init` artifacts and Rust toolchains
- GitHub for uv release artifacts, Spec Kit, governance presets, Gitleaks, and other development tools
- Maven Central
- NuGet
- crates.io
- npm registry

Risk assessment: Unrestricted egress increases the technical attack surface. This risk is accepted for the learning environment for now because the container is isolated, host mounts are explicitly limited, Codex shell network access is disabled in `codex/config.toml`, and every agent is bound by repository rules, narrow tasks, and human approval. Installing the four CLIs does not grant provider approval.

Accepted until: `_TODO_ (to be entered by owner, recommendation: 2026-08-15)`

Open item: Variant B with a real egress allow-list should be reassessed once it is clear whether a suitable proxy, DNS filter, or comparable data-center infrastructure is available.
