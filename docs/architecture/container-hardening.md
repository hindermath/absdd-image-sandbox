# Container-Haertungsarchitektur / Container Hardening Architecture

## Kontext / Context

**DE:** Der Host startet mit rootless Podman einen Linux-Entwicklungscontainer.
Lernende und Entwicklungspersonen arbeiten in expliziten Projekt-Mounts. Das
Repository liefert Buildbeschreibung, Compose-Konfiguration, Agentenregeln und
Evidenz, aber keinen Cloud-, Web- oder Mehrmandantendienst.

**EN:** The host starts one Linux development container with rootless Podman.
Learners and developers work in explicit project mounts. The repository
provides build, Compose, agent rules, and evidence but no cloud, web, or
multi-tenant service.

## Bausteine und Verantwortungen / Building Blocks and Responsibilities

- Host/Podman: Runtime, lokale Images, Ports und Bind-Mount-Quellen; Plattform-
  owner facts remain external. / Runtime, images, ports, and bind sources.
- Image: non-root `adedev`, six MSL toolchains, two scripting foundations,
  agents and supporting tools from pinned declarations.
- Compose: explicit mounts, named state volumes, localhost ports,
  `no-new-privileges`, and dropped capabilities.
- Agent configuration: workspace/write, approval, network, secret-read,
  telemetry, and persistence boundaries; no provider/model preselection.
- Evidence: repository-local non-sensitive status plus untracked raw SBOM/scan
  artefacts; no prompt/response or credential content.

## Trust Boundaries und Datenklassen / Trust Boundaries and Data Classes

1. Host ↔ container: `internal`; only declared mounts and localhost ports.
2. Repository ↔ agent state: `confidential`; named volumes separate state.
3. Project mount ↔ toolchain: `internal`; writes limited to declared workflows.
4. Container ↔ package source: `public/internal`; pinned identity and TLS are
   required; open egress is not accepted risk.
5. Agent CLI ↔ provider: `restricted`; sign-in, provider/model choice, and
   telemetry decisions remain outside automation.
6. Local image ↔ SBOM/scan: `internal`; one final image identity binds evidence.
7. Learner ↔ maintenance flow: `internal`; privileged and delivery operations
   are separate and documented.

## Runtime und Deployment / Runtime and Deployment

Build -> local image -> Compose start -> rootless/runtime checks -> smoke ->
ordered audit export and stop. Registry publication is excluded. Failure stays
visible with original exit status; no unverified fallback is selected. /
The sequence is textually complete; registry publication is excluded and
failures remain visible.

## Risiken und Schulden / Risks and Debt

Open items include unrestricted runtime egress pending Platform Owner/Admin,
final platform coverage, scanner database availability, and human approvals.
The image root filesystem remains writable because broad read-only conversion
has not yet been proven compatible with all toolchains. Re-evaluate on every
boundary or workflow change.

Mapping: `GAP-013`–`GAP-025`, AR-001–AR-008.
