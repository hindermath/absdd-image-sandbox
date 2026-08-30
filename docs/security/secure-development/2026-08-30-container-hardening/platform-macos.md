# macOS-Plattformbeleg / macOS Platform Evidence

Status: `Pass` fuer den beobachteten macOS-Hostpfad; VS-Code-Attach bleibt
`Open` (30.08.2026). Owner: Repository Maintainer. Reviewer: Security Review.

## Beobachtet / Observed

- `bash scripts/test-ade-sandbox-hardening.sh --mode static --dry-run` gab den
  schreibfreien Plan aus und endete mit Exit 0.
- `pwsh -NoProfile -File scripts/test-ade-sandbox-hardening.ps1 -Mode Static
  -WhatIf` zeigte denselben Plan und endete mit Exit 0.
- Die native rootless-Podman-Machine war erreichbar. Das unveraenderte finale
  Image startete und der Runtime-Modus endete mit Exit 0.
- Sechs Sprachfamilien, PowerShell und Node.js sowie OpenCode, Codex, Claude
  Code, Gemini CLI, Antigravity CLI und GitHub Copilot CLI bestanden ihre
  Versions- und Funktionspruefungen. Der Dispatcher-Dry-run loeste keinen
  Provideraufruf aus.
- Der Audit-Wrapper exportierte sechs nicht-sensible Metadatenzeilen und
  stoppte den Compose-Service geordnet.
- Das `code`-CLI war auf diesem Host nicht verfuegbar; ein manueller VS-Code-
  Attach wurde nicht beobachtet.

**EN:** Bash dry-run and PowerShell WhatIf were equivalent and write-free.
Native rootless Podman started the unchanged final image; runtime, six
languages, two scripting foundations, six agent CLIs, dispatcher dry-run, and
audit stop passed. VS Code attachment was not observed and remains Open.

Retry-Trigger fuer den offenen Teil: erneut auf einem macOS-PowerShell7-Host
mit verfuegbarem VS Code Desktop und Dev Containers an das unveraenderte Image
anhaengen. / Retry the open part when VS Code Desktop and Dev Containers are
available on the macOS PowerShell 7 host.
