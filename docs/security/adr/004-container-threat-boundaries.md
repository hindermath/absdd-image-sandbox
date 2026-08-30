# S-ADR 004: Container-Vertrauensgrenzen / Container Trust Boundaries

Status: Accepted as repository design; external approvals remain Open.

## Entscheidung / Decision

Die Sicherheitsanalyse trennt Host, Build-Quellen, rootless Podman-Container,
Bind-Mounts, benannte Agenten-Volumes, Audit-Ziel und externe Provider als
eigene Vertrauenszonen. Ein Uebergang ist nur ueber die in Compose,
Dockerfile, Agentenkonfiguration und Audit-Allowlist beschriebenen Pfade
zulaessig. / The security analysis treats the host, build sources, rootless
container, bind mounts, named agent volumes, audit target, and external
providers as separate trust zones. Transitions use only declared paths.

Freier Egress ist ein offener Befund, keine akzeptierte Ausnahme. Neue Mounts,
Ports, Privilegien oder State-Pfade benoetigen erneute Bedrohungsmodell- und
Runtimepruefung. / Unrestricted egress is an open finding, not an accepted
exception. New mounts, ports, privileges, or state paths require re-review.

Folgen: klare Datenfluesse und pruefbare Boundary-Evidenz; keine Aussage ueber
Host-, Provider- oder Plattformfreigabe. / Consequences: explicit data flows
and testable boundary evidence, without claiming host/provider/platform
approval.
