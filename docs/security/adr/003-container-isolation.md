# S-ADR-003 Container-Isolation / Container Isolation

Status: Accepted technical direction; formal protection-level approval Open.

**Context:** A local learning sandbox needs broad toolchains without granting
host-wide or root access. / Die Lern-Sandbox benoetigt breite Toolchains ohne
Host-Vollzugriff.

**Decision:** Rootless Podman, runtime user `adedev`, explicit mounts, named
agent volumes, localhost ports, `no-new-privileges`, `cap_drop: ALL`, and
agent-level read/write/network constraints. Read-only root filesystem is not
enabled until toolchain compatibility and every writable path are proven.

**Consequences:** Stronger least privilege with retained learning workflows.
Bind mounts and free egress remain boundaries requiring documentation and
runtime/platform evidence. Formal data-class sufficiency remains Human-only.

Trigger: user, capability, mount, port, network, state, or workflow change.
Mapping: GAP-013–GAP-019, GAP-147–GAP-155.
