# Inventarabgleich / Inventory Reconciliation

**DE:** Soll-Angabe, statische Beobachtung und praktische Laufzeitbeobachtung bleiben getrennt. `Open` ist kein Pass. **EN:** Target claims, static observations, and practical runtime observations remain separate. Open is not a pass.

## Zusammenfassung / Summary

**DE:** Die folgenden Eintraege gleichen 29 Inventarobjekte mit statischer und verfuegbarer praktischer Evidenz ab. **EN:** The following entries reconcile 29 inventory objects with static and available practical evidence.

### INV-MSL-DOTNET

- **Name:** .NET/C# / .NET/C#
- **Kategorie / Category:** MSLToolchain; **Soll / Target:** Required memory-safe language family; **Version/Pin:** 10.0; **Count group:** mslFamilies
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-125
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `Required memory-safe language family`, result `Pass`. Command: `Inspect AGENTS.md project structure and toolchain list.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `10.0`, result `Pass`. Command: `rg -n '\.NET' Dockerfile`. Limitation: Static build declaration; no image rebuild in assessment scope.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Not executed because the intended Podman endpoint and service were unavailable in this sandbox context.

### INV-MSL-JAVA

- **Name:** Java/JVM / Java/JVM
- **Kategorie / Category:** MSLToolchain; **Soll / Target:** Required memory-safe language family; **Version/Pin:** 21; **Count group:** mslFamilies
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-125
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `Required memory-safe language family`, result `Pass`. Command: `Inspect AGENTS.md project structure and toolchain list.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `21`, result `Pass`. Command: `rg -n 'Java' Dockerfile`. Limitation: Static build declaration; no image rebuild in assessment scope.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Not executed because the intended Podman endpoint and service were unavailable in this sandbox context.

### INV-MSL-GO

- **Name:** Go / Go
- **Kategorie / Category:** MSLToolchain; **Soll / Target:** Required memory-safe language family; **Version/Pin:** 1.26.3; **Count group:** mslFamilies
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-125
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `Required memory-safe language family`, result `Pass`. Command: `Inspect AGENTS.md project structure and toolchain list.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `1.26.3`, result `Pass`. Command: `rg -n 'Go' Dockerfile`. Limitation: Static build declaration; no image rebuild in assessment scope.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Not executed because the intended Podman endpoint and service were unavailable in this sandbox context.

### INV-MSL-RUST

- **Name:** Rust / Rust
- **Kategorie / Category:** MSLToolchain; **Soll / Target:** Required memory-safe language family; **Version/Pin:** stable; **Count group:** mslFamilies
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-125
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `Required memory-safe language family`, result `Pass`. Command: `Inspect AGENTS.md project structure and toolchain list.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `stable`, result `Pass`. Command: `rg -n 'Rust' Dockerfile`. Limitation: Static build declaration; no image rebuild in assessment scope.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Not executed because the intended Podman endpoint and service were unavailable in this sandbox context.

### INV-MSL-PYTHON

- **Name:** Python / Python
- **Kategorie / Category:** MSLToolchain; **Soll / Target:** Required memory-safe language family; **Version/Pin:** base image package; **Count group:** mslFamilies
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-125
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `Required memory-safe language family`, result `Pass`. Command: `Inspect AGENTS.md project structure and toolchain list.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `base image package`, result `Pass`. Command: `rg -n 'Python' Dockerfile`. Limitation: Static build declaration; no image rebuild in assessment scope.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Not executed because the intended Podman endpoint and service were unavailable in this sandbox context.

### INV-MSL-SWIFT

- **Name:** Swift / Swift
- **Kategorie / Category:** MSLToolchain; **Soll / Target:** Required memory-safe language family; **Version/Pin:** 6.2.4; **Count group:** mslFamilies
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-125
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `Required memory-safe language family`, result `Pass`. Command: `Inspect AGENTS.md project structure and toolchain list.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `6.2.4`, result `Pass`. Command: `rg -n 'Swift' Dockerfile`. Limitation: Static build declaration; no image rebuild in assessment scope.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Not executed because the intended Podman endpoint and service were unavailable in this sandbox context.

### INV-FOUNDATION-POWERSHELL

- **Name:** PowerShell 7 / PowerShell 7
- **Kategorie / Category:** ScriptingFoundation; **Soll / Target:** Separate scripting foundation; **Version/Pin:** 7.6.1; **Count group:** separateFoundations
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-125
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `Separate scripting foundation`, result `Pass`. Command: `Inspect AGENTS.md project structure and toolchain list.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `7.6.1`, result `Pass`. Command: `rg -n 'PowerShell\ 7' Dockerfile`. Limitation: Static build declaration; no image rebuild in assessment scope.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Not executed because the intended Podman endpoint and service were unavailable in this sandbox context.

### INV-FOUNDATION-NODE

- **Name:** Node.js/npm / Node.js/npm
- **Kategorie / Category:** ScriptingFoundation; **Soll / Target:** Separate supporting foundation; **Version/Pin:** 22.x; **Count group:** separateFoundations
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-125
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `Separate supporting foundation`, result `Pass`. Command: `Inspect AGENTS.md project structure and toolchain list.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `22.x`, result `Pass`. Command: `rg -n 'Node\.js' Dockerfile`. Limitation: Static build declaration; no image rebuild in assessment scope.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Not executed because the intended Podman endpoint and service were unavailable in this sandbox context.

### INV-AGENT-CODEX

- **Name:** Codex / Codex
- **Kategorie / Category:** RequiredAgent; **Soll / Target:** RequiredAgent; **Version/Pin:** 0.144.1; **Count group:** requiredAgents
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-150
- **Beobachtungen / Observations:**
  - Installation: Dockerfile, `Dockerfile`, value `Declared`, result `Pass`. Command: `Inspect Dockerfile installation step.`. Limitation: Static declaration only.
  - VersionPin: Dockerfile, `Dockerfile`, value `0.144.1`, result `Pass`. Command: `rg -n 'VERSION=' Dockerfile`. Limitation: Pin is declared; runtime version remains open.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Podman runtime unavailable; retry with intended endpoint and running ade service.
  - State: StateVolume, `compose.yml`, value `Declared`, result `Pass`. Command: `Inspect compose.yml state volumes and mounts.`. Limitation: Static Compose inspection only.
  - Dispatcher: Dispatcher, `scripts/tests/test_agent_prompt_dispatchers.py`, value `Six supported surfaces`, result `Pass`. Command: `python3 scripts/tests/test_agent_prompt_dispatchers.py`. Limitation: Four static parity tests passed; provider calls were not made.
  - ProviderSignIn: Documentation, `docs/security/ai-tools-inventory.md`, value `Open`, result `Open`. Command: `Inspect provider/sign-in evidence without accessing credentials.`. Limitation: Provider selection and sign-in are Human-only and were not changed.
  - DocumentationCategory: Documentation, `AGENTS.md`, value `RequiredAgent`, result `Pass`. Command: `Inspect repository guidance and feature specification.`. Limitation: Repository documentation category only.

### INV-AGENT-CLAUDE

- **Name:** Claude Code / Claude Code
- **Kategorie / Category:** RequiredAgent; **Soll / Target:** RequiredAgent; **Version/Pin:** 2.1.206; **Count group:** requiredAgents
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-150
- **Beobachtungen / Observations:**
  - Installation: Dockerfile, `Dockerfile`, value `Declared`, result `Pass`. Command: `Inspect Dockerfile installation step.`. Limitation: Static declaration only.
  - VersionPin: Dockerfile, `Dockerfile`, value `2.1.206`, result `Pass`. Command: `rg -n 'VERSION=' Dockerfile`. Limitation: Pin is declared; runtime version remains open.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Podman runtime unavailable; retry with intended endpoint and running ade service.
  - State: StateVolume, `compose.yml`, value `Declared`, result `Pass`. Command: `Inspect compose.yml state volumes and mounts.`. Limitation: Static Compose inspection only.
  - Dispatcher: Dispatcher, `scripts/tests/test_agent_prompt_dispatchers.py`, value `Six supported surfaces`, result `Pass`. Command: `python3 scripts/tests/test_agent_prompt_dispatchers.py`. Limitation: Four static parity tests passed; provider calls were not made.
  - ProviderSignIn: Documentation, `docs/security/ai-tools-inventory.md`, value `Open`, result `Open`. Command: `Inspect provider/sign-in evidence without accessing credentials.`. Limitation: Provider selection and sign-in are Human-only and were not changed.
  - DocumentationCategory: Documentation, `AGENTS.md`, value `RequiredAgent`, result `Pass`. Command: `Inspect repository guidance and feature specification.`. Limitation: Repository documentation category only.

### INV-AGENT-ANTIGRAVITY

- **Name:** Antigravity CLI / Antigravity CLI
- **Kategorie / Category:** RequiredAgent; **Soll / Target:** RequiredAgent; **Version/Pin:** 1.1.1; **Count group:** requiredAgents
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-150
- **Beobachtungen / Observations:**
  - Installation: Dockerfile, `Dockerfile`, value `Declared`, result `Pass`. Command: `Inspect Dockerfile installation step.`. Limitation: Static declaration only.
  - VersionPin: Dockerfile, `Dockerfile`, value `1.1.1`, result `Pass`. Command: `rg -n 'VERSION=' Dockerfile`. Limitation: Pin is declared; runtime version remains open.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Podman runtime unavailable; retry with intended endpoint and running ade service.
  - State: StateVolume, `compose.yml`, value `Declared`, result `Pass`. Command: `Inspect compose.yml state volumes and mounts.`. Limitation: Static Compose inspection only.
  - Dispatcher: Dispatcher, `scripts/tests/test_agent_prompt_dispatchers.py`, value `Six supported surfaces`, result `Pass`. Command: `python3 scripts/tests/test_agent_prompt_dispatchers.py`. Limitation: Four static parity tests passed; provider calls were not made.
  - ProviderSignIn: Documentation, `docs/security/ai-tools-inventory.md`, value `Open`, result `Open`. Command: `Inspect provider/sign-in evidence without accessing credentials.`. Limitation: Provider selection and sign-in are Human-only and were not changed.
  - DocumentationCategory: Documentation, `AGENTS.md`, value `RequiredAgent`, result `Pass`. Command: `Inspect repository guidance and feature specification.`. Limitation: Repository documentation category only.

### INV-AGENT-COPILOT

- **Name:** GitHub Copilot CLI / GitHub Copilot CLI
- **Kategorie / Category:** RequiredAgent; **Soll / Target:** RequiredAgent; **Version/Pin:** 1.0.70; **Count group:** requiredAgents
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-150
- **Beobachtungen / Observations:**
  - Installation: Dockerfile, `Dockerfile`, value `Declared`, result `Pass`. Command: `Inspect Dockerfile installation step.`. Limitation: Static declaration only.
  - VersionPin: Dockerfile, `Dockerfile`, value `1.0.70`, result `Pass`. Command: `rg -n 'VERSION=' Dockerfile`. Limitation: Pin is declared; runtime version remains open.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Podman runtime unavailable; retry with intended endpoint and running ade service.
  - State: StateVolume, `compose.yml`, value `Declared`, result `Pass`. Command: `Inspect compose.yml state volumes and mounts.`. Limitation: Static Compose inspection only.
  - Dispatcher: Dispatcher, `scripts/tests/test_agent_prompt_dispatchers.py`, value `Six supported surfaces`, result `Pass`. Command: `python3 scripts/tests/test_agent_prompt_dispatchers.py`. Limitation: Four static parity tests passed; provider calls were not made.
  - ProviderSignIn: Documentation, `docs/security/ai-tools-inventory.md`, value `Open`, result `Open`. Command: `Inspect provider/sign-in evidence without accessing credentials.`. Limitation: Provider selection and sign-in are Human-only and were not changed.
  - DocumentationCategory: Documentation, `AGENTS.md`, value `RequiredAgent`, result `Pass`. Command: `Inspect repository guidance and feature specification.`. Limitation: Repository documentation category only.

### INV-AGENT-OPENCODE

- **Name:** OpenCode / OpenCode
- **Kategorie / Category:** AdditionalAgentSurface; **Soll / Target:** AdditionalAgentSurface; **Version/Pin:** 1.14.50; **Count group:** additionalAgentSurfaces
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-150
- **Beobachtungen / Observations:**
  - Installation: Dockerfile, `Dockerfile`, value `Declared`, result `Pass`. Command: `Inspect Dockerfile installation step.`. Limitation: Static declaration only.
  - VersionPin: Dockerfile, `Dockerfile`, value `1.14.50`, result `Pass`. Command: `rg -n 'VERSION=' Dockerfile`. Limitation: Pin is declared; runtime version remains open.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Podman runtime unavailable; retry with intended endpoint and running ade service.
  - State: StateVolume, `compose.yml`, value `Declared`, result `Pass`. Command: `Inspect compose.yml state volumes and mounts.`. Limitation: Static Compose inspection only.
  - Dispatcher: Dispatcher, `scripts/tests/test_agent_prompt_dispatchers.py`, value `Six supported surfaces`, result `Pass`. Command: `python3 scripts/tests/test_agent_prompt_dispatchers.py`. Limitation: Four static parity tests passed; provider calls were not made.
  - ProviderSignIn: Documentation, `docs/security/ai-tools-inventory.md`, value `Open`, result `Open`. Command: `Inspect provider/sign-in evidence without accessing credentials.`. Limitation: Provider selection and sign-in are Human-only and were not changed.
  - DocumentationCategory: Documentation, `AGENTS.md`, value `AdditionalAgentSurface`, result `Pass`. Command: `Inspect repository guidance and feature specification.`. Limitation: Repository documentation category only.

### INV-AGENT-GEMINI

- **Name:** Gemini CLI / Gemini CLI
- **Kategorie / Category:** AdditionalAgentSurface; **Soll / Target:** AdditionalAgentSurface; **Version/Pin:** 0.50.0; **Count group:** additionalAgentSurfaces
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-150
- **Beobachtungen / Observations:**
  - Installation: Dockerfile, `Dockerfile`, value `Declared`, result `Pass`. Command: `Inspect Dockerfile installation step.`. Limitation: Static declaration only.
  - VersionPin: Dockerfile, `Dockerfile`, value `0.50.0`, result `Pass`. Command: `rg -n 'VERSION=' Dockerfile`. Limitation: Pin is declared; runtime version remains open.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Podman runtime unavailable; retry with intended endpoint and running ade service.
  - State: StateVolume, `compose.yml`, value `Declared`, result `Pass`. Command: `Inspect compose.yml state volumes and mounts.`. Limitation: Static Compose inspection only.
  - Dispatcher: Dispatcher, `scripts/tests/test_agent_prompt_dispatchers.py`, value `Six supported surfaces`, result `Pass`. Command: `python3 scripts/tests/test_agent_prompt_dispatchers.py`. Limitation: Four static parity tests passed; provider calls were not made.
  - ProviderSignIn: Documentation, `docs/security/ai-tools-inventory.md`, value `Open`, result `Open`. Command: `Inspect provider/sign-in evidence without accessing credentials.`. Limitation: Provider selection and sign-in are Human-only and were not changed.
  - DocumentationCategory: Documentation, `AGENTS.md`, value `AdditionalAgentSurface`, result `Pass`. Command: `Inspect repository guidance and feature specification.`. Limitation: Repository documentation category only.

### INV-PRESET-SECURITY-GOVERNANCE

- **Name:** security-governance / security-governance
- **Kategorie / Category:** BindingPreset; **Soll / Target:** BindingPreset; **Version/Pin:** v0.6.2; **Count group:** bindingPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/security-governance/preset.yml`, value `security-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/security-governance/preset.yml`, value `v0.6.2`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `10`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/security-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/security-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/security-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-ARCHITECTURE-GOVERNANCE

- **Name:** architecture-governance / architecture-governance
- **Kategorie / Category:** BindingPreset; **Soll / Target:** BindingPreset; **Version/Pin:** v0.5.2; **Count group:** bindingPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/architecture-governance/preset.yml`, value `architecture-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/architecture-governance/preset.yml`, value `v0.5.2`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `20`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/architecture-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/architecture-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/architecture-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-ISAQB-ARCHITECTURE-GOVERNANCE

- **Name:** isaqb-architecture-governance / isaqb-architecture-governance
- **Kategorie / Category:** BindingPreset; **Soll / Target:** BindingPreset; **Version/Pin:** v0.2.2; **Count group:** bindingPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/isaqb-architecture-governance/preset.yml`, value `isaqb-architecture-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/isaqb-architecture-governance/preset.yml`, value `v0.2.2`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `30`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/isaqb-architecture-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/isaqb-architecture-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/isaqb-architecture-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-A11Y-GOVERNANCE

- **Name:** a11y-governance / a11y-governance
- **Kategorie / Category:** BindingPreset; **Soll / Target:** BindingPreset; **Version/Pin:** v0.4.3; **Count group:** bindingPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/a11y-governance/preset.yml`, value `a11y-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/a11y-governance/preset.yml`, value `v0.4.3`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `40`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/a11y-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/a11y-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/a11y-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-CROSS-PLATFORM-GOVERNANCE

- **Name:** cross-platform-governance / cross-platform-governance
- **Kategorie / Category:** BindingPreset; **Soll / Target:** BindingPreset; **Version/Pin:** v0.2.2; **Count group:** bindingPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/cross-platform-governance/preset.yml`, value `cross-platform-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/cross-platform-governance/preset.yml`, value `v0.2.2`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `50`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/cross-platform-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/cross-platform-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/cross-platform-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-AGENT-PARITY-GOVERNANCE

- **Name:** agent-parity-governance / agent-parity-governance
- **Kategorie / Category:** BindingPreset; **Soll / Target:** BindingPreset; **Version/Pin:** v0.4.2; **Count group:** bindingPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/agent-parity-governance/preset.yml`, value `agent-parity-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/agent-parity-governance/preset.yml`, value `v0.4.2`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `60`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/agent-parity-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/agent-parity-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/agent-parity-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-MODEL-ROUTING-GOVERNANCE

- **Name:** model-routing-governance / model-routing-governance
- **Kategorie / Category:** AdditionalPreset; **Soll / Target:** AdditionalPreset; **Version/Pin:** v0.1.4; **Count group:** additionalPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/model-routing-governance/preset.yml`, value `model-routing-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/model-routing-governance/preset.yml`, value `v0.1.4`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `61`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/model-routing-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/model-routing-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/model-routing-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-INTAKE-AUTHORING-GOVERNANCE

- **Name:** intake-authoring-governance / intake-authoring-governance
- **Kategorie / Category:** AdditionalPreset; **Soll / Target:** AdditionalPreset; **Version/Pin:** v0.3.1; **Count group:** additionalPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/intake-authoring-governance/preset.yml`, value `intake-authoring-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/intake-authoring-governance/preset.yml`, value `v0.3.1`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `64`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/intake-authoring-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/intake-authoring-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/intake-authoring-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-INTAKE-REVIEW-GOVERNANCE

- **Name:** intake-review-governance / intake-review-governance
- **Kategorie / Category:** AdditionalPreset; **Soll / Target:** AdditionalPreset; **Version/Pin:** v0.2.1; **Count group:** additionalPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/intake-review-governance/preset.yml`, value `intake-review-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/intake-review-governance/preset.yml`, value `v0.2.1`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `65`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/intake-review-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/intake-review-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/intake-review-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-INTAKE-SEQUENCING-GOVERNANCE

- **Name:** intake-sequencing-governance / intake-sequencing-governance
- **Kategorie / Category:** AdditionalPreset; **Soll / Target:** AdditionalPreset; **Version/Pin:** v0.2.3; **Count group:** additionalPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/intake-sequencing-governance/preset.yml`, value `intake-sequencing-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/intake-sequencing-governance/preset.yml`, value `v0.2.3`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `66`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/intake-sequencing-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/intake-sequencing-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/intake-sequencing-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-AUTONOMOUS-RUN-GOVERNANCE

- **Name:** autonomous-run-governance / autonomous-run-governance
- **Kategorie / Category:** BindingPreset; **Soll / Target:** BindingPreset; **Version/Pin:** v0.4.1; **Count group:** bindingPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/autonomous-run-governance/preset.yml`, value `autonomous-run-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/autonomous-run-governance/preset.yml`, value `v0.4.1`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `70`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/autonomous-run-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/autonomous-run-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/autonomous-run-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-PRESET-PARALLEL-AUTONOMOUS-RUN-GOVERNANCE

- **Name:** parallel-autonomous-run-governance / parallel-autonomous-run-governance
- **Kategorie / Category:** BindingPreset; **Soll / Target:** BindingPreset; **Version/Pin:** v0.2.6; **Count group:** bindingPresets
- **Abgleich / Reconciliation:** Aligned; **Gap:** N/A
- **Beobachtungen / Observations:**
  - PresetIdentity: InstalledPreset, `.specify/presets/parallel-autonomous-run-governance/preset.yml`, value `parallel-autonomous-run-governance`, result `Pass`. Command: `specify preset list`. Limitation: Installed list completed.
  - PresetVersion: InstalledPreset, `.specify/presets/parallel-autonomous-run-governance/preset.yml`, value `v0.2.6`, result `Pass`. Command: `Both governance preset installers in check-only mode.`. Limitation: Both variants reported exact matrix parity.
  - PresetPriority: Registry, `scripts/config/spec-kit-model-routing-governance-presets.json`, value `80`, result `Pass`. Command: `Inspect managed twelve-preset profile.`. Limitation: Priority matches managed profile.
  - PresetEnabled: InstalledPreset, `.specify/presets/parallel-autonomous-run-governance/preset.yml`, value `enabled`, result `Pass`. Command: `specify preset list`. Limitation: Installed list reported enabled.
  - PresetResolution: InstalledPreset, `.specify/presets/parallel-autonomous-run-governance/preset.yml`, value `resolved`, result `Pass`. Command: `specify preset resolve plan-template`. Limitation: Resolution completed; private local paths are intentionally omitted from this artefact.
  - PresetCoverage: Documentation, `.specify/presets/parallel-autonomous-run-governance/preset.yml`, value `documented in preset metadata`, result `Pass`. Command: `specify preset info security-governance; inspect preset metadata for remaining presets.`. Limitation: Coverage metadata is present; runtime implementation claims remain separate.

### INV-TOOL-SYFT

- **Name:** Syft / Syft
- **Kategorie / Category:** AdditionalTool; **Soll / Target:** Additional build or governance tool; **Version/Pin:** 1.46.0; **Count group:** additionalTools
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-057
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `1.46.0`, result `Pass`. Command: `Inspect repository tool inventory.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `1.46.0`, result `Pass`. Command: `Inspect Dockerfile.`. Limitation: Static declaration only.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Podman runtime unavailable; no Pass is invented.

### INV-TOOL-UV

- **Name:** uv / uv
- **Kategorie / Category:** AdditionalTool; **Soll / Target:** Additional build or governance tool; **Version/Pin:** 0.11.16; **Count group:** additionalTools
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-057
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `0.11.16`, result `Pass`. Command: `Inspect repository tool inventory.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `0.11.16`, result `Pass`. Command: `Inspect Dockerfile.`. Limitation: Static declaration only.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Podman runtime unavailable; no Pass is invented.

### INV-TOOL-SPEC-KIT

- **Name:** Spec Kit / Spec Kit
- **Kategorie / Category:** AdditionalTool; **Soll / Target:** Additional build or governance tool; **Version/Pin:** v0.8.3; **Count group:** additionalTools
- **Abgleich / Reconciliation:** Open; **Gap:** GAP-057
- **Beobachtungen / Observations:**
  - TargetClaim: TargetClaim, `AGENTS.md`, value `v0.8.3`, result `Pass`. Command: `Inspect repository tool inventory.`. Limitation: Target classification only.
  - Installation: Dockerfile, `Dockerfile`, value `v0.8.3`, result `Pass`. Command: `Inspect Dockerfile.`. Limitation: Static declaration only.
  - VersionCheck: SmokeTest, `scripts/smoke-test-toolchains.sh`, value `Open`, result `Open`. Command: `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh`. Limitation: Podman runtime unavailable; no Pass is invented.

## Exakte Zaehler und Plattformen / Exact Counts and Platforms

**DE:** 6 MSL-Familien, 2 getrennte Grundlagen, 4 Required-Agenten, 2 zusaetzliche Agentenoberflaechen, 8 bindende Presets, 4 zusaetzliche Presets und 3 Zusatzwerkzeuge sind vorhanden. macOS-Static-Checks sind belegt. Linux, Windows/WSL2, praktischer Podman-Lauf, Netzwerk- und Providerbeobachtungen bleiben `Open` mit Owner Repository Maintainer und dem Trigger: erneut pruefen, sobald die jeweilige Plattform, der beabsichtigte Podman-Endpunkt, das Netzwerk oder die freigegebene Providerumgebung verfuegbar ist. **EN:** The inventory contains 6 MSL families, 2 separate foundations, 4 required agents, 2 additional agent surfaces, 8 binding presets, 4 additional presets, and 3 additional tools. macOS static checks are proven. Linux, Windows/WSL2, practical Podman, network, and provider observations remain Open, owned by the Repository Maintainer and retried when the relevant platform, intended Podman endpoint, network, or approved provider environment is available.

**DE:** Neue oder geaenderte Bash-/PowerShell-Paare, Manpages, Cmdlets, gemeinsame Agent-Guidance, Templates oder Constitution-Eintraege sind fuer diese Assessment-Implementierung `N/A`. Bestehende Paritaet bleibt bewertet. Trigger ist ein spaeterer Remediation-Scope, der eine dieser Oberflaechen aendert. **EN:** New or changed Bash/PowerShell pairs, man pages, cmdlets, shared agent guidance, templates, or constitution entries are N/A for this assessment implementation. Existing parity remains assessed. Re-evaluate when later remediation changes one of these surfaces.
