# WP12 Agentische Sandbox / Agentic Sandbox

Geprueft wurden Compose-Isolation, non-root, Capabilities, Mounts,
Schreibpfade, Agentenstate, Netzwerk, Ports, Lifecycle, Audit und Presets. /
Compose isolation, non-root, capabilities, mounts, writable paths, agent state,
network, ports, lifecycle, audit, and presets were inspected.

Repositoryevidenz: `USER adedev`, `cap_drop: ALL`,
`no-new-privileges:true`, explizite Bind-Mounts, getrennte Named Volumes,
localhost-Portbereich, Metadatenexport vor Stop, keine automatische
Providerwahl und Governance-Preset-Checks. Der Slice belegte Mount-/State-
Konfiguration statisch; Runtime folgt T053. RED: Netzwerkdokumentation nannte
freien Egress akzeptiert. GREEN: der Punkt ist jetzt offen fuer Platform
Owner/Admin und keine Risikoakzeptanz wird behauptet. / Local controls exist;
runtime evidence is deferred. Unrestricted egress is now explicitly open.

Human-only `GAP-146`, `150`, `152`, `155` bleiben Open. Mapping:
FR-006–FR-013, AR-001–AR-005, `GAP-146`–`GAP-157`.
