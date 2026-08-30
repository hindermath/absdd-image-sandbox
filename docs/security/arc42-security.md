# arc42 Sicherheitskonzepte / arc42 Security Concepts

**DE:** Dieses projektspezifische Querschnittsdokument ergaenzt die
Architektur. Es ist keine formale Sicherheitsfreigabe. / This project-specific
cross-cutting document supplements architecture and is not formal approval.

- Identitaet/Rechte: non-root `adedev`, rootless Podman, no-new-privileges,
  all capabilities dropped; effective state requires runtime evidence.
- Dateisystem: explicit mounts, one read-only config mount, named agent/state
  volumes, Codex/OpenCode write/read boundaries.
- Secrets: ignored env files, deny-read patterns, isolated sign-in state,
  pre-commit and repository scan; values never enter evidence.
- Netzwerk: localhost project ports; build/runtime egress documented Open;
  agent shell network disabled by default where configured.
- Supply chain: digest base, version ARG metadata, locks, pinned scanner/SBOM
  paths, one final SBOM/scan/VEX/provenance chain.
- Logging/audit: metadata only, no prompts or responses, export before volume
  removal.
- Failure: fail closed, preserve exit codes, no `latest` or host-tool fallback.

Re-evaluate on architecture, mount, egress, identity, dependency, agent, or
distribution changes. Mapping: `GAP-013`–`GAP-025`, AR-002–AR-005.
