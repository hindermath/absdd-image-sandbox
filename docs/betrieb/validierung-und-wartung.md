# Validierung und Wartung / Validation and Maintenance

## Prüftiefe wählen / Choose Validation Depth

**DE:** Eine **statische Prüfung** liest Konfiguration und Dateien, ohne einen
Container zu starten. Eine **praktische Prüfung** baut oder startet das Image
und führt Befehle im Linux-Container aus. Plattformakzeptanz bedeutet
zusätzlich, dass die Hostbefehle auf jeder betroffenen Plattform geprüft
wurden. Diese drei Nachweisstufen dürfen nicht miteinander verwechselt werden.

**EN:** A **static check** reads configuration and files without starting a
container. A **practical check** builds or starts the image and runs commands
inside the Linux container. Platform acceptance additionally means that host
commands were tested on every affected platform. Do not confuse these three
levels of evidence.

## Betriebssystem und Werkzeuge erkennen / Detect OS and Tools

```bash
uname -s
command -v pwsh || true
command -v podman || true
command -v podman-compose || true
```

**DE:** Auf diesem macOS-Host werden vorhandene PowerShell-7-Skripte mit
`pwsh -NoProfile` ausgeführt. Für Container-Lifecycle und bestehende Bash-
Wrapper bleibt die Repository-Variante maßgeblich. Keine neue Sprache wird nur
für Bequemlichkeit eingeführt.

**EN:** On this macOS host, existing PowerShell 7 scripts run with
`pwsh -NoProfile`. For container lifecycle and existing Bash wrappers, use the
repository variant. Do not introduce a new language merely for convenience.

## Statische Mindestprüfung / Minimum Static Validation

```bash
podman-compose config
git diff --check
python3 scripts/check-dockerfile-arg-renovate.py
python3 scripts/check-home-baseline-lock.py
python3 scripts/tests/test_home_baseline_documentation_contract.py
python3 scripts/tests/test_agent_prompt_dispatchers.py
python3 scripts/tests/test_spec_kit_agent_surface_parity.py
```

Dokumentationsverträge / Documentation contracts:

```bash
bash scripts/test-documentation-impact.sh
bash scripts/validate-documentation-impact.sh \
  --evidence docs/documentation-impact/feature-025-image-documentation-expansion.json
bash scripts/validate-documentation-impact.sh \
  --evidence docs/documentation-impact/home-baseline-documentation-alignment.json
bash scripts/check-homogeneity.sh --dry-run --no-patch "$PWD"
```

```powershell
pwsh -NoProfile -File scripts/test-documentation-impact.ps1
pwsh -NoProfile -File scripts/validate-documentation-impact.ps1 `
  -Evidence docs/documentation-impact/feature-025-image-documentation-expansion.json
pwsh -NoProfile -File scripts/validate-documentation-impact.ps1 `
  -Evidence docs/documentation-impact/home-baseline-documentation-alignment.json
pwsh -NoProfile -File scripts/check-homogeneity.ps1 `
  -TargetDir $PWD -DryRun -NoPatch
```

**DE:** Lokale Markdown-Links und Anker werden mit denselben Offline-
Parametern wie im Workflow `.github/workflows/documentation-and-sandbox.yml`
geprüft. Externe Links benötigen zusätzlich eine bewusste Online-Prüfung;
deren Ausfall darf nicht als erfolgreiche Erreichbarkeit dokumentiert werden.

**EN:** Local Markdown links and anchors are checked with the same offline
arguments as workflow `.github/workflows/documentation-and-sandbox.yml`.
External links need a deliberate online check as well; a failed check must not
be reported as successful reachability.

## Image bauen und starten / Build and Start the Image

macOS oder Windows / macOS or Windows:

```bash
podman machine start
podman compose build --pull
podman compose up -d
podman compose ps
```

**DE:** Wenn `podman compose` lokal nicht verfügbar ist, nutze
`podman-compose` mit denselben Lifecycle-Argumenten. `podman-compose config`
bleibt die kanonische config-only Prüfung. Ein Machine- oder Socketfehler ist
getrennt von einem Repositoryfehler zu berichten.

**EN:** If `podman compose` is unavailable locally, use `podman-compose` with
the same lifecycle arguments. `podman-compose config` remains the canonical
config-only check. Report a machine or socket failure separately from a
repository failure.

## Werkzeug- und Smoke-Tests / Tool and Smoke Tests

```bash
podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh
```

**DE:** Der Test prüft Identität, Versionen und kleine Programme. Für eine
gezielte Agentenprüfung ohne Provideraufruf:

**EN:** The test checks identity, versions, and small programs. For a focused
agent check without a provider call:

```bash
podman compose exec ade sh -lc \
  'opencode --version; codex --version; claude --version; gemini --version; agy --version; copilot --version'
podman compose exec ade agent-prompt --dry-run codex -- \
  'Dieser Prompt wird nicht ausgegeben.'
```

**DE:** `--version` oder `--help` bestätigt Installation, aber keine Anmeldung
und keine fachliche Providerfreigabe. Ein echter Modellaufruf ist für die
Image-Abnahme nicht erforderlich.

**EN:** `--version` or `--help` confirms installation, not sign-in or provider
approval. A real model call is not required for image acceptance.

## Home-Baseline-Grenze prüfen / Check the Home Baseline Boundary

```bash
podman compose exec ade sh -lc \
  'cd /home/adedev/home-baseline-source && git log -1 --oneline'
podman compose exec ade sync-home-baseline-runtime --dry-run
podman compose exec ade sync-home-baseline-runtime --check-only
```

**DE:** `--apply` ist ein schreibender Vorgang und gehört nicht in einen
allgemeinen Smoke-Test. Er wird nur bei einem ausdrücklich beauftragten
Runtime-Sync verwendet. Der Wrapper besitzt keinen Force-Modus und führt kein
Pull, Push, Commit oder Git-Setup aus. Auf einem frischen Volume zeigt
`--dry-run` die fehlenden Dateien und endet erfolgreich. `--check-only` bleibt
ebenfalls schreibfrei, beendet sich bei erkanntem Drift aber mit Exitcode `1`.
Das ist ein Prüfresultat und kein Ausführungsfehler; Exitcode `0` bedeutet,
dass der ausgewählte Runtime-Inhalt bereits übereinstimmt.

**EN:** `--apply` writes data and does not belong in a general smoke test. Use
it only for an explicitly requested runtime synchronization. The wrapper has
no force mode and performs no pull, push, commit, or Git setup. On a fresh
volume, `--dry-run` lists missing files and exits successfully. `--check-only`
also remains write-free, but exits with code `1` when it detects drift. This is
a check result, not an execution failure; exit code `0` means that the selected
runtime content already matches.

## Web-App-Prüfung / Web App Check

**DE:** Lege das Beispiel unter `/tmp` an, binde es im Container an
`0.0.0.0`, wähle einen freien Port aus `5100-5199`, prüfe die Antwort vom Host
und stoppe den Prozess. Dokumentiere den genauen Port und Exitcode. Lege keine
Dokumentationsbeispiele in `/workspace` oder einem echten Projekt-Mount ab.

**EN:** Create the example under `/tmp`, bind it to `0.0.0.0` inside the
container, choose a free port from `5100-5199`, check the response from the
host, and stop the process. Record the exact port and exit status. Do not place
documentation examples in `/workspace` or a real project mount.

## Secret-Scan / Secret Scan

```bash
pre-commit install
pre-commit run --all-files
bash scripts/scan-agent-secrets.sh --fail-on-high .
```

**DE:** Ein Fund wird nicht durch eine breite Allowlist unterdrückt. Prüfe die
Quelle und eskaliere echte Credentials. Logausgaben verwenden Redaction und
enthalten keine Prompt- oder Antworttexte.

**EN:** Do not hide a finding with a broad allowlist. Inspect the source and
escalate real credentials. Log output uses redaction and contains no prompt or
response text.

## SBOM erzeugen und auswerten / Generate and Analyze an SBOM

```bash
bash scripts/build-and-sbom.sh --skip-build
bash scripts/analyze-sbom.sh
```

```powershell
pwsh -NoProfile -File scripts/build-and-sbom.ps1 -SkipBuild
pwsh -NoProfile -File scripts/analyze-sbom.ps1
```

**DE:** Die CycloneDX-JSON-Datei unter `sboms/` ist ein Build-Artefakt und
bleibt ungetrackt, sofern der Releaseprozess keine Veröffentlichung verlangt.
Eine SBOM beschreibt Komponenten; sie beweist nicht automatisch deren
Sicherheit.

**EN:** The CycloneDX JSON file under `sboms/` is a build artifact and remains
untracked unless the release process requires publication. An SBOM describes
components; it does not automatically prove their security.

## Audit und sicherer Shutdown / Audit and Safe Shutdown

Ohne Volumenlöschung / Without volume deletion:

```bash
bash scripts/compose-down-with-audit.sh --podman
```

Mit bewusst bestätigter Volumenlöschung / With deliberately confirmed volume
deletion:

```bash
bash scripts/compose-down-with-audit.sh --podman -v
```

PowerShell:

```powershell
pwsh -NoProfile -File scripts/compose-down-with-audit.ps1 -Engine podman
pwsh -NoProfile -File scripts/compose-down-with-audit.ps1 -Engine podman -Volumes
```

**DE:** Der Export schreibt nur Metadaten nach `/audit/YYYY-MM-DD.jsonl`:
Werkzeug, Sitzungs-ID, Zeit, Projektpfad und Actor-Hinweis. Prompt, Antwort und
rohe Sitzungsdaten bleiben ausgeschlossen. Der Entrypoint-Hook ist nur eine
Best-Effort-Ergänzung.

**EN:** The export writes metadata only to `/audit/YYYY-MM-DD.jsonl`: tool,
session ID, time, project path, and actor hint. Prompt, response, and raw
session data remain excluded. The entrypoint hook is only a best-effort
addition.

## Plattformnachweis / Platform Evidence

| Aussage / Claim | Erforderlicher Nachweis / Required evidence |
|---|---|
| Compose-Datei ist gültig / Compose file is valid | `podman-compose config` |
| Image ist baubar / Image builds | erfolgreicher `build --pull` auf verfügbarer Architektur / successful build on available architecture |
| Toolchain funktioniert / Toolchain works | Smoke-Test im neu gebauten Image / smoke test in rebuilt image |
| macOS-Lifecycle funktioniert / macOS lifecycle works | lokale Podman-Machine und abgeleiteter Unix-Socket / local Podman machine and derived Unix socket |
| Windows/WSL2 funktioniert / Windows or WSL2 works | tatsächlicher Lauf auf Windows/WSL2 / actual run on Windows or WSL2 |
| Linux funktioniert / Linux works | tatsächlicher Lauf auf Linux / actual run on Linux |

**DE:** Nicht verfügbare Plattformen werden mit Grund als übersprungen
dokumentiert. Eine erfolgreiche macOS-Prüfung ist keine vollständige
Cross-Platform-Akzeptanz.

**EN:** Record unavailable platforms as skipped with a reason. A successful
macOS check is not complete cross-platform acceptance.

Zurück zum [Betriebsindex](README.md). / Return to the
[operations index](README.md).
