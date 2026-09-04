# Quickstart: Geplante Validierung / Planned Validation

## Zweck und Begriffe / Purpose and Terms

**DE:** Dieses Dokument ist der ausfuehrbare Validierungsweg fuer die spaetere
Implementierung. Ein **Gate** ist eine pruefbare Abnahmebedingung. **RED**
bedeutet, dass ein Test den offenen Befund reproduziert; **GREEN** bedeutet,
dass derselbe Test nach einer gezielten Aenderung besteht. Die Planphase fuehrt
keinen Build und keine Haertung aus.

**EN:** This is the runnable validation route for later implementation. A
gate is a testable acceptance condition. RED reproduces a finding; GREEN means
the same check passes after a targeted change. Planning runs no build or
hardening.

## Voraussetzungen / Prerequisites

- Repository-Root auf Branch `003-secure-development-container-hardening`.
- PowerShell 7; auf macOS/Linux immer `pwsh -NoProfile`.
- Podman und fuer Lifecycle-Pruefungen eine gesunde rootless Podman-Laufzeit.
- `podman-compose` fuer die kanonische config-only-Pruefung.
- Keine echten Provider-Schluessel fuer die Validierung.
- macOS-, Windows-Host- und Ubuntu/WSL2-Ergebnisse getrennt protokollieren.
  Windows-Host und Ubuntu/WSL2 duerfen dieselbe physische Hardware nutzen,
  muessen aber getrennte Podman-Laufzeiten und Evidenz besitzen.

## 1. Planungs- und Eingangsgrenze / Planning and Input Boundary

```bash
git status --short --branch
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.sh \
  --state specs/003-secure-development-container-hardening/autonomous-run-state.json
```

Erwartung: aktiver Plan-Run, Run-ID
`8330f54b-97d1-424c-ad1a-842a3fad7be3`, keine Aenderung am State. / Expected:
active plan run and unchanged state.

Nach Implementierung des Validators: / After validator implementation:

```bash
bash scripts/test-ade-sandbox-hardening.sh \
  --mode input \
  --evidence docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
```

```powershell
pwsh -NoProfile -File scripts/test-ade-sandbox-hardening.ps1 `
  -Mode Input `
  -EvidencePath docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
```

Erwartung: sechs Hashes stimmen; `157/108/49`; `0` fehlende, doppelte oder
extra Gap-IDs. / Expected: six hashes match and exact counts pass.

## 2. RED-Fixtures und Vertical Slice / RED Fixtures and Vertical Slice

```bash
python3 -m unittest scripts.tests.test_secure_development_container_hardening
bash scripts/test-ade-sandbox-hardening.sh --mode static --dry-run
```

```powershell
pwsh -NoProfile -File scripts/test-ade-sandbox-hardening.ps1 -Mode Static -WhatIf
```

Erwartung: Tests weisen nach, dass manipulierte Fixtures fuer fehlende/
doppelte IDs, falsche Human-only-Rollen, ungueltige Statuskombinationen,
fehlende Trigger und stale Evidenz abgelehnt werden. Dry-run/WhatIf schreibt
nichts und beschreibt dieselben geplanten Checks. Der erste echte Slice deckt
`GAP-013`, `015`, `020`, `051`, `122`, `147`–`149` und `154` ab.

## 3. Statische GREEN-Pruefung / Static GREEN Check

```bash
podman-compose config
python3 scripts/check-dockerfile-arg-renovate.py
python3 scripts/check-home-baseline-lock.py
python3 scripts/tests/test_agent_prompt_dispatchers.py
python3 scripts/tests/test_spec_kit_agent_surface_parity.py
bash scripts/test-documentation-impact.sh
bash scripts/test-ade-sandbox-hardening.sh --mode static \
  --evidence docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
git diff --check
```

Erwartung: Compose ist statisch gueltig, Download-/ARG-/Lock-/Agenten- und
Dokumentationsvertraege bestehen, jeder geaenderte Pfad ist auf Gap und
Anforderung gemappt. `podman compose config` ist nur zusaetzliche lokale
Plausibilitaet bei gesundem Socket.

## 4. Praktischer Build und Laufzeitgrenzen / Practical Build and Runtime Boundaries

```bash
podman compose build --pull
podman compose up -d
podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh
bash scripts/test-ade-sandbox-hardening.sh --mode runtime \
  --evidence docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
```

Der Runtime-Modus prueft mindestens `whoami`, effektive Capabilities,
`no-new-privileges`, Mountliste/-modi, erlaubten und verweigerten Schreibtest,
localhost-Ports, State-Volumes, Agenten-Secret-Grenzen und dokumentierten
Egress. Ein nicht verfuegbarer Host/Socket ergibt `Blocked` oder `Open`, nie
`Pass`.

Geordneter Abschluss ohne Volumenverlust: / Ordered stop without volume loss:

```bash
bash scripts/compose-down-with-audit.sh --podman
```

## 5. Toolchain-, Agenten- und VS-Code-Nachweis / Toolchain, Agent, and VS Code Evidence

```bash
podman compose exec ade sh -lc \
  'opencode --version; codex --version; claude --version; gemini --version; agy --version; copilot --version'
podman compose exec ade agent-prompt --dry-run codex -- 'redacted validation prompt'
```

Der bestehende Full-Smoke prueft sechs MSL-Familien und PowerShell/Node. Die
Agentenpruefung darf keinen Provideraufruf ausloesen. VS Code wird in jedem
verfuegbaren Akzeptanzpfad manuell an Service `ade` angehaengt; Belegpunkte:
`remoteUser=adedev`, Workspace-Pfad, LSP-Verfuegbarkeit, kein zusaetzlicher
Port und erwartete `code`-Shim-Grenze. Der Windows-Hostpfad nutzt Windows
PowerShell 7, Windows-Podman-Machine und VS Code Desktop. Der Linux-Pfad nutzt
Ubuntu unter WSL2, einen eigenen rootless Podman und VS Code ueber Remote WSL
plus Dev Containers. Nicht verfuegbare Plattformpfade bleiben mit Owner und
Trigger offen. Weil die drei Plattformgates als `Applicable` deklariert sind,
blockiert eine fehlende Ubuntu/WSL2- oder Windows-Host-Evidenz einen positiven
`MergeAndSync`-Abschluss; ein macOS-Lauf, gemeinsam wiederverwendete Evidenz
oder `N/A` ersetzt sie nicht. Native Linux-Hardware ist kein Akzeptanzziel von
Feature 003.

## 6. Finale SBOM, Scan, VEX und lokale Provenienz / Final Supply-Chain Evidence

Erst nach finalem Build/Smoke: / Only after final build/smoke:

```bash
bash scripts/build-and-sbom.sh --skip-build
bash scripts/analyze-sbom.sh --scan --scanner grype
bash scripts/test-ade-sandbox-hardening.sh --mode supply-chain \
  --evidence docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
```

```powershell
pwsh -NoProfile -File scripts/build-and-sbom.ps1 -SkipBuild
pwsh -NoProfile -File scripts/analyze-sbom.ps1 -Scan -Scanner grype
pwsh -NoProfile -File scripts/test-ade-sandbox-hardening.ps1 `
  -Mode SupplyChain `
  -EvidencePath docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
```

Erwartung: genau eine aktuelle CycloneDX-SBOM ist an die finale lokale Image-
ID gebunden; Scanwerkzeug/-Datenstand sind protokolliert; jeder relevante Fund
hat VEX-Status oder offenen Blocker; Provenienz behauptet keine externe
Signatur oder SLSA-Stufe. Der Implementierungsschritt muss einen ungepinnten
Scanner-/`latest`-Fallback vor diesem Gate entfernen oder blockieren.

## 7. Secret-, Dokumentations-, A11Y- und Paritaetsgate

```bash
uvx pre-commit run --all-files
bash scripts/scan-agent-secrets.sh --fail-on-high .
bash scripts/check-homogeneity.sh --dry-run --no-patch "$PWD"
bash scripts/test-ade-sandbox-hardening.sh --mode documentation \
  --evidence docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
bash scripts/test-ade-sandbox-hardening.sh --mode accessibility \
  --evidence docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
```

```powershell
pwsh -NoProfile -File scripts/check-homogeneity.ps1 -TargetDir $PWD -DryRun -NoPatch
pwsh -NoProfile -File scripts/test-ade-sandbox-hardening.ps1 `
  -Mode Documentation `
  -EvidencePath docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
pwsh -NoProfile -File scripts/test-ade-sandbox-hardening.ps1 `
  -Mode Accessibility `
  -EvidencePath docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
```

Erwartung: `0` echte Secrets; geaenderte Nutzertexte sind DE-first/EN-second,
CEFR-B2-orientiert, text-first und fuer alle vier Ausbildungsberufe ohne
Spec-Kit-Vorkenntnis nutzbar. WCAG-2.2-AA-Kriterien werden artefaktbezogen
protokolliert. Gemeinsame Agentenregeln sind atomar synchron.

Der Accessibility-Modus validiert zusaetzlich
`docs/security/secure-development/2026-08-30-container-hardening/learner-first-use-results.json`.
Diese Datei wird von `Learning/A11Y Review` nach einem moderierten Test erzeugt
und enthaelt nur aggregierte, nicht sensible Ergebnisse: alle vier Zielberufe,
keine Spec-Kit-Vorerfahrung, 30-Minuten-Grenze und mindestens 90 Prozent Erfolg
fuer sicheren Start, Verifikationsstatus und naechsten Human-only-Schritt. Der
Agent darf die Datei pruefen, aber keine Teilnehmenden oder Beobachtungen
erfinden. Fehlt der Datensatz, bleibt `GATE-LEARNER-01` offen.

## 8. Finaler 157-Abgleich / Final 157 Reconciliation

```bash
bash scripts/test-ade-sandbox-hardening.sh --mode all \
  --evidence docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json
```

Erwartung: `157/157`, `108/49`, keine erfundene positive Evidenz, alle 49
Human-only-Gaps ohne Rollenbeleg weiterhin offen, jeder geaenderte Pfad
rueckverfolgbar. Ein offener Plattform- oder Human-only-Punkt blockiert nur
die davon abhaengige positive Behauptung, nicht seine ehrliche Dokumentation.

## 9. Orchestrator-only Delivery und Statistik / Orchestrator-Only Delivery and Statistics

Modellaufgaben fuehren die folgenden Aktionen nicht selbst aus. Der
Orchestrator revalidiert Autoritaet und Gates, erstellt erst den Content-
Commit, rendert dann Statistikprofil 2 und erstellt einen separaten
Statistik-Commit:

```bash
pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo .
pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo . -CheckOnly
git diff --check
```

Vor jedem Commit prueft der Orchestrator die konkrete Liefermenge read-only;
jedes derzeit ungetrackte, beabsichtigte Artefakt wird einzeln als
`--intended` angegeben: / Before each commit the orchestrator validates the
exact delivery set read-only and names every intended untracked file.

```bash
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-delivery-set.sh \
  --repo "$PWD" \
  --intended specs/003-secure-development-container-hardening/plan.md
```

Die reale Liste wird aus dem beabsichtigten Content- beziehungsweise
Statistik-Satz erzeugt; das Beispiel ist absichtlich kein Sammel-Glob. Danach
folgen Content-Commit und separater Statistik-Commit. Fuer den exakten final
reviewten Head wird eine Schema-2.0-PreMerge-Datei temporaer erzeugt und mit
den realen Pflichtargumenten validiert: / Generate a temporary schema-2.0
PreMerge snapshot for the exact reviewed head and validate it with the real
interface.

```bash
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh \
  --requirements specs/003-secure-development-container-hardening/autonomous-run-gate-requirements.json \
  --evidence /tmp/003-container-hardening-premerge.json \
  --head <full-reviewed-head>
```

Die PreMerge-Datei wird nicht committet. PR, Review-Konvergenz, Merge und
Default-Branch-Sync bleiben Orchestrator-only und erfordern aktuelle
Autoritaet. Fuer diesen Run ist Admin-Bypass bereits eng begrenzt autorisiert:
nur innerhalb der Provider-Merge-Operation, nur wenn der exakte reviewte Head
alle technischen Checks gruen hat, kein handlungsrelevanter Review-Thread
offen ist, die Schema-2.0-PreMerge-Evidenz gueltig ist und
`REVIEW_REQUIRED` der einzige verbleibende Policy-Blocker ist. Er darf niemals
ein fehlgeschlagenes, ausstehendes, fehlendes, veraltetes oder
widerspruechliches technisches/Security-Gate umgehen oder Repository-Regeln
aendern; eine weitere Autoritaetsanfrage ist fuer diesen Run nicht notwendig.
Das anschliessende kausale PostMerge bindet den normalisierten
PreMerge-Hash sowie den realen Merge-Commit, hat leere `changedPaths` und wird
mit demselben Validator plus `--merge-commit <full-merge-commit>` geprueft.
Keine Registry-Verteilung und keine unabhaengige Bereinigung wird angehaengt.

## Ergebnisinterpretation / Result Interpretation

- Exit `0`: der angeforderte Scope ist belegt.
- Exit `1`: fachlicher RED-/GREEN-Fehler; Evidenz bleibt `Open`.
- Exit `2`: Bedien-/Vertragsfehler.
- Exit `3`: Plattform/Runner fehlt; als `Blocked`/`Open` dokumentieren.
- Kein Exitcode darf durch Wrapper verschluckt werden.
