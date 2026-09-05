# Windows-Host-Plattformbeleg / Windows Host Platform Evidence

Status: `Pass` (06.09.2026). Owner: Repository Maintainer. Reviewer:
Security Review. Runner-Token: `Windows-Host-PowerShell7-Podman`.

## Scope

**DE:** Diese Datei dokumentiert ausschliesslich den Windows-Hostpfad mit
PowerShell 7, Windows-Podman-Machine und VS Code Desktop. Nach
`DEC-XPLAT-WSL2-2026-09-04` darf derselbe Rechner auch den getrennten
Ubuntu/WSL2-Nachweis ausfuehren. Ergebnisse des rootless Podman innerhalb von
Ubuntu/WSL2 werden hier nicht als Windows-Nachweis wiederverwendet.

**EN:** This file documents only the Windows host path with PowerShell 7, the
Windows Podman machine, and VS Code Desktop. Under
`DEC-XPLAT-WSL2-2026-09-04`, the same computer may also run the separate
Ubuntu/WSL2 evidence path. Results from rootless Podman inside Ubuntu/WSL2 are
not reused here as Windows evidence.

## Ausfuehrungsumgebung / Execution Environment

- Git-Head: `ad5cd8bc9a9a2c541416390aa4256bc1ffe1eee7`.
- Windows: `Microsoft Windows NT 10.0.26200.0`; PowerShell `7.6.5`;
  Podman `6.0.2`; Podman Compose mit Docker-Compose-Provider `5.1.3`.
- VS Code CLI: `1.135.0`; Dev Containers:
  `ms-vscode-remote.remote-containers@0.466.0`.
- Die Windows-Podman-Machine meldete bei der Nachpruefung `Rootful=true`.
  Der Windows-Gate-Vertrag fordert die eigene Podman-Machine, waehrend die
  Entscheidung den rootless-Nachweis ausdruecklich dem Ubuntu/WSL2-Pfad
  zuordnet. / The Windows Podman machine reported `Rootful=true` during the
  follow-up check. The Windows gate requires its own Podman machine, while the
  decision explicitly assigns the rootless proof to the Ubuntu/WSL2 path.

## Technischer Nachweis / Technical Evidence

| Beobachtung / Observation | UTC-Zeit / UTC time | Ergebnis / Result |
|---|---|---|
| PowerShell-Static-`-WhatIf` / PowerShell static `-WhatIf` | `2026-09-05T22:08:15Z` bis `22:08:16Z` | Exit `0`; schreibfreier Plan bestaetigt. / Write-free plan confirmed. |
| PowerShell-Zwoelf-Preset-Pruefung / PowerShell twelve-preset check | `2026-09-05T22:08:16Z` bis `22:08:17Z` | Exit `0`; alle 12 Presets entsprachen der Matrix. / All 12 presets matched the matrix. |
| `podman compose --project-name absdd-image-sandbox-issue52-win build --pull ade` | `2026-09-04T17:28:32Z` bis `17:43:53Z` | Exit `0`; eigenes Windows-Pfad-Image fuer `linux/amd64`. / Separate Windows-path image. |
| Isolierter Lauf ohne Portveroeffentlichung / isolated run without published ports | Start `2026-09-04T17:44:13Z`; Nachpruefung `2026-09-05T22:00:13Z` bis `22:00:15Z` | Exit `0`; Container `absdd-image-sandbox-issue52-win-final-ade-run` weiterhin `running`, User `adedev`, Arbeitsverzeichnis `/rider-projects`, `no-new-privileges`, alle Standard-Capabilities entfernt und keine Portbindung. / Container remained running with the declared isolation, user, workdir, and zero port bindings. |
| Mount-Pruefung / mount validation | `2026-09-05T22:00:13Z` bis `22:01:06Z` | Exit `0`; `/workspace`, `/rider-projects`, `/ade-dev-sandbox`, die getrennten Agenten-Volumes und die Projektmounts waren vorhanden; `compose.yml` und die kanonische JSON-Evidenz waren im Repository-Mount lesbar. / Declared mounts and representative repository files were accessible. |
| `scripts/smoke-test-toolchains.sh` | `2026-09-05T22:08:17Z` bis `22:08:37Z` | Exit `0`; sechs Sprachtoolchains, PowerShell `7.6.4`, Node.js und die geforderten Agenten-/Hilfs-CLIs bestanden. / Six language toolchains, PowerShell 7.6.4, Node.js, and the required agent/helper CLIs passed. |
| `agent-prompt --dry-run codex` | `2026-09-05T22:08:37Z` bis `22:08:38Z` | Exit `0`; Prompt ueber stdin, Ausgabe redigiert, kein Provideraufruf und keine Anmeldung. / Prompt via stdin, redacted output, no provider call or sign-in. |
| `scripts/build-and-sbom.ps1 -SkipBuild` | `2026-09-05T22:08:54Z` bis `22:10:03Z` | Exit `0`; CycloneDX `1.7` mit 23.960 Komponenten und 11.556.057 Byte; lokaler Dateiname vom 06.09.2026; SHA-256 `bf36a62dfc278e5424d9dc00caea5004403dd43262943eccd4b7da38fe1d403c`. |
| VS Code Desktop und Dev Containers | Start `2026-09-05T21:57:56Z` bis `21:57:58Z`; Abschlusspruefung `2026-09-05T22:07:03Z` bis `22:07:07Z` | Exit `0`; neues Fenster `rider-projects [Container docker.io/library/absdd-image-sandbox-issue52-win-ade:latest (absdd-image-sandbox-issue52-win-final-ade-run)]`. VS-Code-Server, `extensionHost`, `ptyHost` und JSON-LSP `jsonServerMain` liefen unter `adedev`; `Folder (rider-projects)` war aktiv. / Desktop attachment, workspace, terminal backend, remote user, indicator, and JSON language server passed. |
| Menschliche Terminalbeobachtung / human terminal observation | Bestaetigung bis `2026-09-05T22:04:54Z` erfasst / confirmation recorded by this time | `whoami` ergab `adedev`, danach `whoami_exit=0`; `pwd` ergab `/rider-projects`, danach `pwd_exit=0`. / The integrated terminal returned the expected user, workspace, and explicit exit codes. |

Finales Windows-Image / Final Windows image:

- Name: `docker.io/library/absdd-image-sandbox-issue52-win-ade:latest`
- Image-ID: `57736551db228f235d45c2e07b6511f5a381088cf698f28e4178d1c21ecacd24`
- Plattform / Platform: `linux/amd64`
- Laufcontainer-ID / Runtime container ID:
  `495ec426614b9253d2a99aa684b70418aeef82c84aad62fb685e09557b8a7479`

Die bereits laufenden Windows-Container wurden nicht gestoppt oder neu
erstellt. Insbesondere blieb der eingefrorene PoC unveraendert. / Existing
Windows containers were neither stopped nor recreated. In particular, the
frozen proof of concept remained unchanged.

## Ergebnis und Grenzen / Result and Limitations

**DE:** Build, isolierter Runtime-Container, Toolchain-Smoke,
Agent-Prompt-Dry-Run, aktuelle Windows-SBOM und der reale VS-Code-Desktop-
Anhang sind fuer das getrennte Windows-Image aktuell belegt. Menschliche
Terminalausgaben und technische Status-/Prozessdaten bestaetigen
`remoteUser=adedev`, `/rider-projects`, Remote-Indikator, integriertes
Terminal und aktiven JSON-LSP. `GATE-XPLAT-WIN-01` ist deshalb `Pass`.

Die grafische Computer-Use-Schnittstelle war trotz vorgeschriebener Retries
und Sitzungs-Reset nicht erreichbar. Deshalb erfolgte der Attach ueber die
vorhandene VS-Code-CLI und die sichtbare Terminalausgabe wurde vom Repository
Owner bestaetigt. Der Repository-Mount ist lesbar; Git-Kommandos innerhalb
des Containers koennen den Windows-absoluten `.git`-Verweis dieses Linked
Worktrees jedoch nicht aufloesen. Diese Grenze betrifft nicht den
`/rider-projects`-Workspace oder den erfolgreichen Editor-Anhang und wird
nicht als behoben behauptet.

**EN:** Build, isolated runtime, toolchain smoke, agent-prompt dry run, the
current Windows SBOM, and a real VS Code Desktop attachment are current for
the separate Windows image. Human terminal output and technical status/
process data confirm `remoteUser=adedev`, `/rider-projects`, the remote
indicator, integrated terminal, and active JSON language server.
GATE-XPLAT-WIN-01 therefore passes.

The graphical Computer Use interface remained unavailable after the required
retries and session reset, so the existing VS Code CLI performed the attach
and the Repository Owner confirmed the visible terminal output. Repository
files are readable through `/ade-dev-sandbox`, but Git inside the container
cannot resolve this linked worktree's Windows-absolute `.git` pointer. This
does not affect the `/rider-projects` workspace or successful editor attach
and is not claimed as fixed.

Neubewertungsausloeser / Re-evaluation trigger: Any Windows, Podman machine,
image, container, mount, linked-worktree pointer, VS Code, Dev Containers,
workspace, terminal, remote-user, or LSP change.
