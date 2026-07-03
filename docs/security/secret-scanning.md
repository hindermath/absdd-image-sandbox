# Secret-Scanning

Stand: 2026-07-03

## Deutsch

Dieses Repository nutzt `pre-commit` mit `gitleaks` `v8.30.1` als Mindestabsicherung gegen versehentlich committed Klartext-Geheimnisse. Hosting- oder CI-spezifische Angaben in diesem Dokument muessen fuer die aktive Plattform erneut bewertet werden.

Kontrollen:

- `.pre-commit-config.yaml` pinnt den Gitleaks-Hook auf `v8.30.1`.
- `.gitleaks.toml` erweitert die Gitleaks-Standardregeln.
- Die Allowlist erlaubt nur dokumentierte Platzhalterwerte in Beispiel-Dateien wie `opencode.env.example`.
- `.github/workflows/homogeneity-check.yml` enthaelt Agent-Secret-Scan-Jobs
  fuer Linux, macOS und Windows.
- Lokale Scan-Ergebnisse bleiben untracked und duerfen keine Klartext-Secrets
  in Commits einbringen.

Audit-Text:

> Client-side Control; zentrale Secret-Push-Blockade haengt von den auf
> GitHub aktivierten Repository-Regeln, Secret-Scanning-Funktionen und
> Owner-/Admin-Einstellungen ab.

Bewertung:

- Der lokale Pre-Commit-Hook reduziert das Risiko vor dem Commit.
- Die GitHub-Workflow-Jobs reduzieren das Risiko nach dem Push und im Pull
  Request.
- Zentrale Push-Blockade ist ein Plattform-/Admin-Thema und wird in diesem
  Repository nicht als erledigt behauptet.

Validierung:

```bash
pre-commit run --all-files
gitleaks git --config .gitleaks.toml --redact --verbose .
```

## English

This repository uses `pre-commit` with `gitleaks` `v8.30.1` as the minimum control against accidentally committed plaintext secrets. Hosting- or CI-specific statements in this document must be reassessed for the active platform.

Controls:

- `.pre-commit-config.yaml` pins the Gitleaks hook to `v8.30.1`.
- `.gitleaks.toml` extends the Gitleaks default rules.
- The allowlist permits only documented placeholder values in example files such as `opencode.env.example`.
- `.github/workflows/homogeneity-check.yml` contains agent secret scan jobs
  for Linux, macOS, and Windows.
- Local scan results remain untracked and must not introduce plaintext secrets
  into commits.

Audit text:

> Client-side control; central secret push blocking depends on the GitHub
> repository rules, secret-scanning features, and owner/admin settings that are
> active for this repository.

Assessment:

- The local pre-commit hook reduces risk before commit.
- The GitHub workflow jobs reduce risk after push and in pull requests.
- Central push blocking is a platform/admin topic and is not claimed as
  complete by this repository.

Validation:

```bash
pre-commit run --all-files
gitleaks git --config .gitleaks.toml --redact --verbose .
```
