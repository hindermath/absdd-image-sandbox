# Secret-Scanning

Stand: 2026-05-14

## Deutsch

Dieses Repository nutzt `pre-commit` mit `gitleaks` `v8.30.1` als Mindestabsicherung gegen versehentlich committed Klartext-Geheimnisse. Hosting- oder CI-spezifische Angaben in diesem Dokument sind Kontextevidenz und muessen fuer die aktive Plattform erneut bewertet werden.

Kontrollen:

- `.pre-commit-config.yaml` pinnt den Gitleaks-Hook auf `v8.30.1`.
- `.gitleaks.toml` erweitert die Gitleaks-Standardregeln.
- Die Allowlist erlaubt nur dokumentierte Platzhalterwerte in Beispiel-Dateien wie `opencode.env.example`.
- `.gitlab-ci.yml` enthaelt einen zusaetzlichen `secret_scan`-Job mit `zricethezav/gitleaks:v8.30.1`.
- `gl-secret-detection-report.json` ist in `.gitignore` ausgeschlossen, weil es lokale Scan-Ergebnisse enthalten kann.

Audit-Text:

> Client-side Control, in GitLab CE nicht vollständig serverseitig erzwingbar; zentrale Push-Blockade nur mit GitLab Ultimate Secret Push Protection oder Admin-Server-Hook.

Bewertung:

- Der lokale Pre-Commit-Hook reduziert das Risiko vor dem Commit.
- Der GitLab-CI-Job reduziert das Risiko nach dem Push und im Merge Request.
- GitLab CE erzwingt keine zentrale Secret-Push-Protection im Pre-Receive-Hook.
- Eine zentrale Push-Blockade waere nur ueber GitLab Ultimate Secret Push Protection oder einen durch GitLab-Administratoren betriebenen Git server hook erreichbar.

Validierung:

```bash
pre-commit run --all-files
gitleaks git --config .gitleaks.toml --redact --verbose .
```

## English

This repository uses `pre-commit` with `gitleaks` `v8.30.1` as the minimum control against accidentally committed plaintext secrets. Hosting- or CI-specific statements in this document are context evidence and must be reassessed for the active platform.

Controls:

- `.pre-commit-config.yaml` pins the Gitleaks hook to `v8.30.1`.
- `.gitleaks.toml` extends the Gitleaks default rules.
- The allowlist permits only documented placeholder values in example files such as `opencode.env.example`.
- `.gitlab-ci.yml` contains an additional `secret_scan` job with `zricethezav/gitleaks:v8.30.1`.
- `gl-secret-detection-report.json` is excluded in `.gitignore` because it can contain local scan results.

Audit text:

> Client-side Control, in GitLab CE nicht vollständig serverseitig erzwingbar; zentrale Push-Blockade nur mit GitLab Ultimate Secret Push Protection oder Admin-Server-Hook.

Assessment:

- The local pre-commit hook reduces risk before commit.
- The GitLab CI job reduces risk after push and in merge requests.
- GitLab CE does not enforce central secret push protection in the pre-receive hook.
- Central push blocking would require GitLab Ultimate Secret Push Protection or a Git server hook operated by GitLab administrators.

Validation:

```bash
pre-commit run --all-files
gitleaks git --config .gitleaks.toml --redact --verbose .
```
