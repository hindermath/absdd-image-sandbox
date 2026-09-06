# Netzwerkentscheidung: Compose-Egress

Stand: 2026-07-10

## Deutsch

Technischer Iststand: Die `ade`-Lernumgebung nutzt das Compose-Default-Bridge-
Netz mit freiem ausgehendem Netzwerkzugriff. Dies ist keine Freigabe oder
Risikoakzeptanz.

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

Risikostatus: Freier Egress vergroessert die technische Angriffsoberflaeche.
Der Punkt bleibt `Open` fuer `Platform Owner/Admin`; die vorhandenen
Container-, Mount- und Codex-Sandbox-Grenzen sind kompensierende Fakten, aber
keine stellvertretende Risikoakzeptanz. Die CLI-Installationen sind keine
Providerfreigabe.

Review-Termin: `_TODO_ (vom Platform Owner/Admin einzutragen)`

Offener Punkt: Variante B mit echter Egress-Allow-List soll erneut bewertet werden, sobald klar ist, ob ein geeigneter Proxy, DNS-Filter oder eine vergleichbare RZ-Infrastruktur verfuegbar ist.

## English

Technical current state: the `ade` learning environment uses the Compose
default bridge with unrestricted outbound access. This is not approval or risk
acceptance.

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

Risk status: unrestricted egress increases the technical attack surface. It
remains Open for Platform Owner/Admin. Existing container, mount, and Codex
sandbox boundaries are compensating facts, not proxy risk acceptance. CLI
installation does not grant provider approval.

Review date: `_TODO_ (to be entered by Platform Owner/Admin)`

Open item: Variant B with a real egress allow-list should be reassessed once it is clear whether a suitable proxy, DNS filter, or comparable data-center infrastructure is available.
