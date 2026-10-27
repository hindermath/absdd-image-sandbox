# Coverage Scope: Namentlicher Nenner / Named Denominator

**Snapshot**: 2026-10-26, Git `5e60e2110e9b788ae8eff9561f11feb6c7850566`.
**Requirement**: Spec FR-003, Clarification 2026-10-25, AC-H-344-02.

DE: 104 bereits vorhandene Dateien als konservativer Messumfang. Nicht nur
geänderte Helfer betrachten. Erfasst werden Argument-/Pfad-/Mount-/Netzwerk- /
Download-/Integritäts-/Audit-/Dispatchgrenzen sowie ihre ausführbaren Wrapper.
Die Liste schließt vorsorglich lokale Spec-Kit-Core-Skripte und zusätzliche
Prüfeinstiege ein; keine bequeme Verkleinerung auf die geänderten Module.
Der neue Retention-Kern kommt bei Implementierung hinzu. Zahlen sind eine
Dateiliste, keine Anzahl von Zweigen oder bestandenen Tests.
EN: Use 104 existing files as a conservative scope, including unchanged
boundary helpers, local Spec Kit core and additional check entrypoints.
Add the new retention core when implemented. This counts files, not branches
or successful tests; never reduce scope to edited modules only.

## Module Inventory

```text
.specify/scripts/bash/check-prerequisites.sh
.specify/scripts/bash/common.sh
.specify/scripts/bash/create-new-feature.sh
.specify/scripts/bash/setup-plan.sh
dotnet/dotnet-wrapper.sh
scripts/agent-prompt.ps1
scripts/agent-prompt.sh
scripts/analyze-sbom.ps1
scripts/analyze-sbom.sh
scripts/audit-export.ps1
scripts/audit-export.sh
scripts/build-and-sbom.ps1
scripts/build-and-sbom.sh
scripts/build-secure-development-docs.ps1
scripts/build-secure-development-docs.sh
scripts/check-container-architecture.ps1
scripts/check-container-architecture.sh
scripts/check-dockerfile-arg-renovate.py
scripts/check-gsdb-self-assessment.ps1
scripts/check-gsdb-self-assessment.sh
scripts/check-home-baseline-lock.py
scripts/check-homogeneity.ps1
scripts/check-homogeneity.sh
scripts/codex-bwrap-wrapper.sh
scripts/compose-down-with-audit.ps1
scripts/compose-down-with-audit.sh
scripts/container-entrypoint.sh
scripts/hooks/pre-push
scripts/init-stats.ps1
scripts/init-stats.sh
scripts/install-home-baseline-reference.sh
scripts/install-hooks.ps1
scripts/install-hooks.sh
scripts/install-spec-kit-governance-presets.ps1
scripts/install-spec-kit-governance-presets.sh
scripts/invoke-psscriptanalyzer.ps1
scripts/lib/agentic_workspace_fleet.py
scripts/lib/hg-a11y.ps1
scripts/lib/hg-a11y.sh
scripts/lib/hg-bilingual.ps1
scripts/lib/hg-bilingual.sh
scripts/lib/hg-deps.ps1
scripts/lib/hg-deps.sh
scripts/lib/hg-forgejo.ps1
scripts/lib/hg-forgejo.sh
scripts/lib/hg-git-scope.sh
scripts/lib/hg-hook.ps1
scripts/lib/hg-hook.sh
scripts/lib/hg-patch.ps1
scripts/lib/hg-patch.sh
scripts/lib/hg-scan.ps1
scripts/lib/hg-scan.sh
scripts/lib/hg-secrets.ps1
scripts/lib/hg-secrets.sh
scripts/lib/hg-speckit.ps1
scripts/lib/hg-speckit.sh
scripts/lib/hg-stats.ps1
scripts/lib/hg-stats.sh
scripts/lib/linux-maintenance-hardening.py
scripts/lib/maintenance_container_worker.py
scripts/lib/maintenance_execution_context.py
scripts/lib/resolve-home-baseline-source.ps1
scripts/lib/resolve-home-baseline-source.sh
scripts/lib/secure-development-hardening.ps1
scripts/lib/secure-development-hardening.sh
scripts/lib/secure_development_hardening.py
scripts/lib/statistics-ci-evidence.ps1
scripts/lib/windows-maintenance-hardening.psm1
scripts/lib/workspace_storage_maintenance.py
scripts/maintain-agentic-brew-apps.sh
scripts/maintain-agentic-winget-apps.ps1
scripts/maintain-agentic-workspace.ps1
scripts/maintain-agentic-workspace.sh
scripts/maintain-powershell-modules.ps1
scripts/maintain-workspace-storage.ps1
scripts/maintain-workspace-storage.sh
scripts/rename-lastenheft.ps1
scripts/rename-lastenheft.sh
scripts/render-project-statistics.ps1
scripts/render-project-statistics.sh
scripts/render-requirements-intake-governance.ps1
scripts/render-requirements-intake-governance.sh
scripts/resolve-model-routing.ps1
scripts/resolve-model-routing.sh
scripts/sandbox-lifecycle.ps1
scripts/sandbox-lifecycle.sh
scripts/scan-agent-secrets.ps1
scripts/scan-agent-secrets.sh
scripts/setup-antigravity-settings.ps1
scripts/setup-antigravity-settings.sh
scripts/smoke-test-documentation.sh
scripts/smoke-test-toolchains.sh
scripts/sync-home-baseline-runtime.sh
scripts/templates/antigravity-statusline.ps1
scripts/templates/antigravity-statusline.sh
scripts/test-ade-sandbox-hardening.ps1
scripts/test-ade-sandbox-hardening.sh
scripts/test-documentation-impact.ps1
scripts/test-documentation-impact.sh
scripts/test-requirements-intake-governance.ps1
scripts/test-requirements-intake-governance.sh
scripts/validate-documentation-impact.ps1
scripts/validate-documentation-impact.sh
spec-kit/patch-specify-cli.py
```

DE: Gründe nach Gruppen: Runtime-/Dispatch-/Audit-/Lifecycle-Dateien begrenzen
Containeraktionen und vertrauliche Zustände. Installer, Scanner und Hooks
begrenzen Downloads und Git. Maintenance-/Fleet-/Storage-Helfer können
Host/andere Repositories verändern. Renderer und Governance-Helfer verarbeiten
Dateipfade, Hashes oder Prozessparameter. Die zwei Statusline-Vorlagen werden
tatsächlich installiert und sind daher im Umfang. Das `.psm1` ist ausführbarer
PowerShell-Code, keine Datendatei.
EN: Runtime helpers constrain actions/data; installers/scanners/hooks constrain
downloads/Git; maintenance/fleet/storage can affect other repositories or hosts.
Renderers/governance process paths, hashes or arguments. Installed statusline
templates and the executable PowerShell module remain in scope.

## Abgrenzung / Exclusions

DE: `scripts/tests/**` und deren synthetische Fixtures sind Testtreiber,
nicht Produkt-Nenner. Testoberflächen direkt unter `scripts/` bleiben
konservativ enthalten. Unveränderte Fremdpresets/-Extensions unter
`.specify/presets/**` und `.specify/extensions/**` sind Abhängigkeiten mit
Herkunfts-/Metadaten-/Mutationstests, nicht eigene Implementierung. Lokale
Anpassungen daran würden neu in den Nenner aufgenommen. Archivierte
Spec-/Workshop-Beispiele, private ignorierte Dateien und Datenartefakte sind
keine aktive eigene Codebasis. C# und JavaScript/MJS liegen außerhalb des
sprachgebundenen Nenners, bleiben aber bei betroffenen Schnittstellen und
kritischen UI-Flows im 80-%-Review. Dockerfile/Compose sind Konfiguration,
deren integrierte Skriptlogik/Inline-Python separat mitbewertet wird.
EN: Exclude test fixtures/drivers under tests, unchanged third-party presets/
extensions, archived examples and private/generated data from product code
coverage. Include locally modified dependency code if introduced. The
language-specific scope excludes C#/JavaScript but not their affected
interfaces/UI flows. Assess embedded Dockerfile/Compose/script Python logic
separately rather than treating it as nonexistent.

## Messverfahren / Measurement

DE: Vor Implementierung pro Datei einen Quellhash und alle erreichbaren
Entscheidungs-Outcomes inventarisieren: if/elif, case/default, Kurzschluss,
Schleife (Eintritt/Austritt), Ausnahme-/Fehler-/Signalpfad. Inline-Python,
injizierter Spec-Kit-Patch-Code und Remote-Programme brauchen eigene
Zuordnung; ungemessener Kindprozess bleibt offen. Kein Weglassen für eine
schönere Quote. Ein Fachreview bestätigt Vollständigkeit vor Ausführung.
EN: Bind source hashes and enumerate decisions/outcomes per file, including
short-circuit, loops, error/signal paths and embedded/generated child code.
Review catalog completeness before execution; no omissions to improve ratios.

DE: Python: coverage.py mit Branchmessung und expliziter Include-Liste aller
neun Python-Dateien; späterer Retention-Helfer und Inline-Programme zusätzlich.
Aus JSON `covered_branches / num_branches` je Datei berechnen. Mindestens
85 % je sicherheitskritischem Modul; unbekannter Nenner blockiert die
Erfüllungsbehauptung. Fehlende/gar nicht geladene Dateien bleiben sichtbar.
EN: Include all nine named Python files plus later/embedded code; compute
per-file branch ratios from JSON, retaining unexecuted files and unknowns.

DE: Shell/PowerShell: vollständiges Entscheidungsregister mit sourceHash,
decisionId, Outcome, Fixture-ID und zuordenbarem Prozess-/Tracebeleg.
Instrumentierung darf keine echten Argumente/Secrets loggen oder Semantik
ändern. Pester-/kcov-Zeilen-/Commanddaten ergänzen, ersetzen aber keine
Branchquote. Nicht zuverlässig beobachtete Outcomes sind unbedeckt oder
Messlücke Open. Keine Python- und Shell-Prozente mitteln.
EN: Require source-bound decision/outcome and fixture execution records;
instrument only synthetic runs without semantic or confidential-output
changes. Command/line data supplements rather than replaces branch evidence.
Unobserved outcomes are uncovered/Open; never average incompatible metrics.

## Schnittstellen-Nenner / Interface Denominator

DE: Initiale benannte Kandidaten sind die öffentlichen Skripte oben außerhalb
von `scripts/lib/`, plus tatsächlich dokumentierte kritische Maintenance-TUI-
Flows. Ein Paar bildet eine fachliche Interface-ID, hat aber Nachweise pro
beanspruchter Plattform. Vor erstem Test `interface-catalog.json` mit allen
README-/man-/help-Inputs/Modi und UI-Flows erzeugen und reviewen, einschließlich
read-only/default Betrieb, Auditexport, sicherer Stopp/Retention, Agenten-
Dispatch, Build/SBOM/Scan, Architekturprüfung und Wartungsvorschau.
Interne Bibliotheksfunktionen sind nicht automatisch öffentliche CLI-Interfaces.
Ein finaler Prozentwert ist vor diesem vollständigen Katalog nicht behauptbar.
EN: Start with named public entrypoints outside lib and documented critical
maintenance UI flows. Pair variants by logical identity but retain claimed
platform proof. Before tests, review the complete README/man/help mode/input
and flow catalog; library functions are not automatically public CLIs.
No coverage percentage is valid before the full catalog exists.

DE: Zähleinheit verbindlich: ein dokumentierter öffentlicher Modus oder
kritischer UI-Ablauf je fachlicher ID, mit allen beanspruchten Plattform- und
Shellvarianten als Pflichtbelege dieser ID. Reine Optionskombinationen werden
nicht beliebig als neue IDs gezählt; maßgeblich ist ein eigener dokumentierter
Bedienvertrag. Vor dem ersten Abnahmelauf den vollständigen Katalog inklusive
Quellhash reviewen. Nur IDs mit beiden Fallarten für alle beanspruchten
Varianten gehören in den Zähler; Skips/fehlende Plattformen bleiben im Nenner.
Änderungen am Katalog invalidieren die zugehörige Quote, nicht die Historie.
EN: One documented public mode or critical UI flow is one logical ID, requiring
all claimed platform/shell variants. Do not inflate counts with arbitrary
option combinations: require a distinct documented usage contract. Review
the full source-bound catalog before acceptance; count only IDs with both
case types for every claimed variant. Skips remain in the denominator and
catalog changes require remeasurement without rewriting history.

DE: Mindestens 80 % des vollständigen Katalogs brauchen tatsächlich
ausgeführte positive und negative Fälle; 100 % aller neuen/geänderten
Interfaces brauchen beide. Ein Skip zählt nicht als ausgeführter Fall.
Maintenance niemals global ausführen: isoliertes HOME, Fake-Binärdateien,
Repository-/Registry-Fixtures, gesperrtes Netzwerk und Wegwerfverzeichnisse.
Wrapper mit absoluten Binärpfaden nur isoliert nativ prüfen, nicht durch
PATH-Stubs scheinbar sicher machen. REV-TEST-TIMING: deterministische
Klassifikation plus echter `/bin/sh`-stderr-/Capability-/Redaction- und
Timeout-Test, ohne zusätzliche Launcher oder größere Timeouts, erhalten.
EN: Execute both case types for at least 80% of the complete interface/flow
catalog and for every changed interface. Skips do not count. Never perform
global maintenance; isolate home, registries, binaries, network and projects.
Absolute-path wrappers need real isolation. Preserve deterministic timing
classification and direct-shell stderr/capability/redaction/timeout tests.
