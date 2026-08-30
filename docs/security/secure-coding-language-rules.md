# Sichere Sprachregeln / Secure Coding Language Rules

## Python

- Repositorypfade normalisieren, Traversal und absolute Fremdpfade ablehnen.
- JSON strukturell und semantisch pruefen; unbekannte Felder fail-closed.
- Subprozesse als Argumentliste ohne `shell=True`; Inhalte/Secrets nie loggen.

## Bash

- `set -euo pipefail`, Variablen quoten, Optionen strikt parsen, unbekannte
  Modi mit Exit 2 ablehnen.
- Keine `eval`- oder Curl-Pipe-Shell-Pfade; Downloads nur gepinnt/verifiziert.
- Dry-run schreibt nichts; native Exitcodes bleiben sichtbar.

## PowerShell 7

- Advanced Functions mit `SupportsShouldProcess`, `Set-StrictMode -Version
  Latest`, `-LiteralPath` und Argumentarrays.
- Keine Profile auf macOS/Linux; native `$LASTEXITCODE` pruefen.
- Comment Help DE-first/EN-second; `-WhatIf` bleibt schreibfrei.

**EN:** Bound paths, validate structured input, avoid shell interpolation,
preserve failures, never log secrets, and keep Bash dry-run and PowerShell
WhatIf semantically paired. Mapping: NIST SSDF, CWE Top 25,
`GAP-087`–`GAP-099`.
