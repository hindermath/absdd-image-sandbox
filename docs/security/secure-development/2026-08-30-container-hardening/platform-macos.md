# macOS-Plattformbeleg / macOS Platform Evidence

Status: `Pass`, Frische / freshness: `Current` (06.09.2026). Owner:
Repository Maintainer. Reviewer: Security Review.

Technischer Implementierungsstand / technical implementation revision:
`ad5cd8bc9a9a2c541416390aa4256bc1ffe1eee7`. Gepruefter Repository-Head /
verified repository head: `7901cc71cfda9ea125b67b1ea91fc0ad4484accd`.
Die Commits dazwischen enthalten nur die bereits uebergebenen Windows- und
WSL2-Nachweise; die Image-Implementierung ist unveraendert. / The intervening
commits contain only the previously handed-over Windows and WSL2 evidence; the
image implementation is unchanged.

## Umgebung / Environment

- macOS `26.6.2` Build `25G83`, Apple Silicon `arm64`
- PowerShell `7.6.5`
- Podman `6.1.0`, `podman-compose` `1.6.0`
- Podman-Machine `podman-machine-default`, Status `running`, `Rootful=true`
- VS Code `1.135.0`, Commit
  `08d4889f9ec4a1685d257b9b95de036c8e1ce1e5`, `arm64`
- Dev Containers `0.466.0`

**EN:** The native macOS host used PowerShell 7, Podman 6.1.0, VS Code
1.135.0, and Dev Containers 0.466.0. The current local Podman machine reports
`Rootful=true`; this is recorded as a limitation and is not presented as
rootless evidence. The binding rootless runtime evidence remains the separate
Ubuntu/WSL2 path.

## Build und Laufzeit / Build and Runtime

- `podman compose build --pull` endete mit Exit 0. Der Digest-Pin des
  Multi-Arch-.NET-Basisimages und die Swift-Signaturpruefung bestanden.
- Image: `localhost/absdd-image-sandbox_ade:latest`
- Image-ID: `sha256:978cb724a3cf33be6891ad99c261a0bfe441a813d90a6be9eb029b10ce4e2a72`
- Plattform: `linux/arm64`; Erzeugungszeit: `2026-09-06T08:50:54Z`
- `podman compose up -d --force-recreate` startete Container
  `absdd-image-sandbox_ade_1`, ID
  `49adefa68ec670a563c1b8c92255a3368a9e9595506012e3ef5c79f4aaa09afe`.
- `bash scripts/test-ade-sandbox-hardening.sh --mode runtime --evidence ...`
  meldete `GREEN [Runtime]` und endete mit Exit 0.
- Der vollstaendige Toolchain-Smoke-Test endete mit Exit 0. Er kompilierte
  und startete Programme in allen sechs Sprachfamilien und pruefte
  PowerShell, Node.js, die sechs Agenten-CLIs, Syft und Spec Kit.
- `agent-prompt --dry-run codex` endete mit Exit 0, ohne Anmeldung,
  Provideraufruf oder Modellanfrage.
- Bash-Static-Dry-run und PowerShell-Static-WhatIf waren schreibfrei,
  inhaltlich gleichwertig und endeten jeweils mit Exit 0.

**EN:** The current image built successfully with `--pull`; the pinned base
image and Swift signature checks passed. The recreated container passed the
runtime gate, the complete six-language and agent CLI smoke test, the
provider-free dispatcher dry-run, and equivalent write-free Bash and
PowerShell static plans.

## VS-Code-Anhang / VS Code Attachment

- Dev Containers wurde lokal auf Podman eingestellt. Der fuer diese
  VS-Code-/Node-Kombination erforderliche Navigator-Kompatibilitaetsschalter
  wurde nur in den lokalen Benutzereinstellungen gesetzt; keine lokale
  Einstellung wurde in das Repository aufgenommen.
- Der reale Anhang an den laufenden Container wurde im VS-Code-Desktopfenster
  beobachtet. Der Fenstertitel zeigte
  `rider-projects [Container localhost/absdd-image-sandbox_ade:latest
  (absdd-image-sandbox_ade_1)]`.
- Explorer und `code --status` bestaetigten den Ordner `/rider-projects` und
  das Container-Remoteziel.
- `podman top` bestaetigte VS-Code-Server, `agentHost`, `ptyHost`,
  `extensionHost` und den aktiven JSON-Sprachserver `jsonServerMain`, jeweils
  als Containerbenutzer `adedev`.
- Ein menschlich abgelesener `whoami`-/`pwd`-Terminalauszug liegt fuer macOS
  nicht vor, weil der Host vor dieser zusaetzlichen Sichtpruefung gesperrt
  wurde. Remoteindikator, Workspace, Terminal-Backend, Benutzer und aktiver
  LSP sind durch UI-, Status- und Prozessnachweise belegt.

**EN:** VS Code Desktop attached to the running container and opened
`/rider-projects`. UI, `code --status`, and `podman top` confirmed the remote
container, workspace, VS Code server, terminal backend, extension host,
`adedev` user, and active JSON language server. The host locked before an
additional human-read `whoami`/`pwd` terminal capture, so that narrower
observation is not claimed.

## Grenzen und Trigger / Limitations and Trigger

Die macOS-Podman-Machine ist aktuell rootful. Dieser Plattformbeleg ersetzt
weder den kanonischen rootless Ubuntu/WSL2-Nachweis noch die dort gebundene
Image-, SBOM-, Scan-, VEX- oder Provenienzidentitaet. Bei Aenderung von macOS,
Podman-Machine-Modus, Compose, Image, Mounts, VS Code, Dev Containers,
Workspace, Remote-Benutzer oder LSP ist der Nachweis zu wiederholen.

**EN:** The current macOS Podman machine is rootful. This platform record does
not replace the canonical rootless Ubuntu/WSL2 image, SBOM, scan, VEX, or
provenance evidence. Repeat after any relevant host, runtime, image, mount, or
editor change.
