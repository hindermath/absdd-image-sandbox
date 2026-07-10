# VS Code mit der Sandbox verbinden / Connecting VS Code to the Sandbox

**Stand / Date:** 2026-07-10
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

**DE:** Dieses Dokument zeigt, wie du mit **VS Code auf deinem Rechner** direkt
**im laufenden Container** arbeitest. Wenn dir die Grundbegriffe fehlen, lies
zuerst [container-grundlagen.md](container-grundlagen.md); den Container startest
du wie in [installation.md](installation.md) und
[erste-schritte.md](erste-schritte.md) beschrieben.

**EN:** This document shows how to work with **VS Code on your machine** directly
**inside the running container**. If you are missing the basics, read
[container-grundlagen.md](container-grundlagen.md) first; you start the container
as described in [installation.md](installation.md) and
[erste-schritte.md](erste-schritte.md).

---

## Was passiert hier? / What Happens Here?

**DE:** VS Code läuft auf deinem **Host** (deinem Rechner) und **hängt sich an**
den laufenden Container `ade`. Danach bearbeitest du Dateien, öffnest ein
Terminal und nutzt die Sprachunterstützung (LSP) so, als wärst du direkt im
Container — bist du auch. Der Code liegt im Container, die Oberfläche auf deinem
Rechner.

**EN:** VS Code runs on your **host** (your machine) and **attaches** to the
running container `ade`. Then you edit files, open a terminal, and use language
support (LSP) as if you were inside the container — because you are. The code
lives in the container, the interface on your machine.

**DE:** Wichtig: Es wird **kein** VS-Code-Server dauerhaft ins Image eingebaut
und **kein** zusätzlicher Port geöffnet. VS Code installiert den passenden
Remote-Server beim Verbinden **selbst** in den Container. Das hält die
Angriffsfläche klein und passt zur Härtung der Sandbox (siehe
[warum-sandbox.md](warum-sandbox.md) und
`docs/security/sandbox-isolation.md`).

**EN:** Important: **no** VS Code server is permanently baked into the image and
**no** additional port is opened. VS Code installs the matching remote server
into the container **itself** when connecting. This keeps the attack surface
small and fits the sandbox hardening (see [warum-sandbox.md](warum-sandbox.md)
and `docs/security/sandbox-isolation.md`).

---

## Voraussetzungen / Prerequisites

**DE:** Auf deinem Host brauchst du:

**EN:** On your host you need:

- **DE:** VS Code Desktop.
  **EN:** VS Code Desktop.
- **DE:** Die VS-Code-Erweiterung **„Dev Containers"**.
  **EN:** The VS Code extension **"Dev Containers"**.
- **DE:** Podman (oder Podman Desktop) mit einer Docker-kompatiblen Sicht.
  **EN:** Podman (or Podman Desktop) with a Docker-compatible view.

### Podman in VS Code einstellen / Configure Podman in VS Code

**DE:** Die Dev-Containers-Erweiterung sucht standardmäßig nach Docker. Damit sie
deinen Podman-Container findet, setze in den VS-Code-Einstellungen
(`settings.json`) den Container-Befehl auf `podman`:

**EN:** By default the Dev Containers extension looks for Docker. So it finds
your Podman container, set the container command to `podman` in your VS Code
settings (`settings.json`):

```json
{
  "dev.containers.dockerPath": "podman"
}
```

**DE:** Ohne diese Einstellung meldet die Erweiterung oft, dass kein Container
gefunden wurde — obwohl der Container läuft.

**EN:** Without this setting, the extension often reports that no container was
found — even though the container is running.

---

## Schritt für Schritt / Step by Step

**DE:** Starte zuerst den Container (aus dem Repository-Ordner):

**EN:** First start the container (from the repository folder):

```bash
podman compose up -d ade
```

**DE:** Dann in VS Code:

**EN:** Then in VS Code:

1. **DE:** Befehlspalette öffnen: `F1`. **EN:** Open the command palette: `F1`.
2. **DE:** `Dev Containers: Attach to Running Container...` auswählen.
   **EN:** Choose `Dev Containers: Attach to Running Container...`.
3. **DE:** Den Container `ade` bzw. `absdd-image-sandbox-ade-1` wählen.
   **EN:** Pick the container `ade` or `absdd-image-sandbox-ade-1`.
4. **DE:** Im verbundenen Fenster einen Ordner öffnen: `/rider-projects`,
   `/workspace`, `/python-projects`, `/swift-projects`. Für Wartung an diesem
   Setup-Repo: `/ade-dev-sandbox`.
   **EN:** In the connected window open a folder: `/rider-projects`,
   `/workspace`, `/python-projects`, `/swift-projects`. For maintenance of this
   setup repo: `/ade-dev-sandbox`.

**DE:** Kontrolle im VS-Code-Terminal — die Ausgabe muss `adedev` sein:

**EN:** Check in the VS Code terminal — the output must be `adedev`:

```bash
whoami
```

**DE:** Die Sprachunterstützung (LSP) für Go, Rust und Swift ist bereits im
Image installiert (`gopls`, `rust-analyzer`, `sourcekit-lsp`). Für Swift ist die
Erweiterung `swiftlang.swift-vscode` bereits in `.devcontainer/devcontainer.json`
vorgesehen.

**EN:** Language support (LSP) for Go, Rust, and Swift is already installed in
the image (`gopls`, `rust-analyzer`, `sourcekit-lsp`). For Swift, the extension
`swiftlang.swift-vscode` is already declared in
`.devcontainer/devcontainer.json`.

---

## Der `code`-Befehl: Wahrheit und Grenzen / The `code` Command: Truth and Limits

**DE:** In einer **verbundenen** Dev-Containers-Session kannst du im integrierten
Terminal eine Datei so in VS Code öffnen:

**EN:** In a **connected** Dev Containers session you can open a file in VS Code
from the integrated terminal like this:

```bash
code hallo.py
```

**DE:** Das funktioniert, weil VS Code beim Verbinden einen kleinen `code`-Helfer
(Shim) in den Container legt. Dieser Helfer spricht über einen internen Kanal
(IPC-Socket) mit deinem bereits geöffneten VS-Code-Fenster.

**EN:** This works because VS Code places a small `code` helper (a shim) into the
container when connecting. This helper talks to your already open VS Code window
over an internal channel (an IPC socket).

**DE:** **Grenze:** `code <datei>` startet **kein** VS Code und baut **keine**
Verbindung auf. In einer gewöhnlichen Shell (z. B. `podman compose exec ade
bash`) ohne aktive VS-Code-Verbindung gibt es diesen Kanal nicht — der Befehl
kann dann nichts öffnen. Die Reihenfolge ist immer: **erst** vom Host anhängen,
**dann** funktioniert `code` im Terminal.

**EN:** **Limit:** `code <file>` does **not** start VS Code and does **not**
establish a connection. In an ordinary shell (e.g. `podman compose exec ade
bash`) without an active VS Code connection, this channel does not exist — the
command cannot open anything. The order is always: **first** attach from the
host, **then** `code` works in the terminal.

---

## Bezug zum Container-First-Gate / Relation to the Container-First Gate

**DE:** Wenn du VS Code an den Container hängst und im **integrierten Terminal**
arbeitest, läuft alles **im Container** — auch KI-Agenten, die du dort startest.
Damit erfüllst du das Container-First-Gate (siehe
[warum-sandbox.md](warum-sandbox.md)). Reines Lesen, Navigieren und Review darf
weiterhin außerhalb der Sandbox stattfinden.

**EN:** When you attach VS Code to the container and work in the **integrated
terminal**, everything runs **inside the container** — including AI agents you
start there. This satisfies the Container-First Gate (see
[warum-sandbox.md](warum-sandbox.md)). Plain reading, navigation, and review may
still happen outside the sandbox.

**DE:** Achte darauf: Ein KI-Agent muss im **Container-Terminal** laufen, nicht
in einem Host-Terminal. Das Anhängen mit VS Code stellt genau das sicher.

**EN:** Watch out: an AI agent must run in the **container terminal**, not in a
host terminal. Attaching with VS Code ensures exactly that.

---

## Fehlerbehebung / Troubleshooting

**DE:**

- **Symptom:** „Dev Containers" findet keinen Container, obwohl `ade` läuft.
  **Ursache:** Die Erweiterung sucht nach Docker. **Lösung:**
  `"dev.containers.dockerPath": "podman"` setzen (siehe oben) und VS Code neu
  laden.
- **Symptom:** Kein Container wählbar / Verbindung schlägt fehl. **Ursache:** Die
  Podman-Machine läuft nicht. **Lösung:** `podman machine start`, prüfen mit
  `podman info`; Details in [troubleshooting.md](troubleshooting.md).
- **Symptom:** `specify check` meldet im Container `Visual Studio Code (not
  found)`. **Ursache:** VS Code ist ein Host-Werkzeug, kein Dienst im Container.
  **Lösung:** Keine — diese Meldung ist bei diesem Setup erwartbar.

**EN:**

- **Symptom:** "Dev Containers" finds no container although `ade` runs.
  **Cause:** The extension looks for Docker. **Solution:** set
  `"dev.containers.dockerPath": "podman"` (see above) and reload VS Code.
- **Symptom:** No container selectable / connection fails. **Cause:** The Podman
  machine is not running. **Solution:** `podman machine start`, check with
  `podman info`; details in [troubleshooting.md](troubleshooting.md).
- **Symptom:** `specify check` reports `Visual Studio Code (not found)` in the
  container. **Cause:** VS Code is a host tool, not a service in the container.
  **Solution:** none — this message is expected with this setup.

---

## Verweise / References

**DE:** Detailquellen:

**EN:** Detail sources:

- `README.md`, Abschnitt „VS Code von aussen verbinden" — maßgebliche Anleitung
- `.devcontainer/devcontainer.json` — Dev-Containers-Konfiguration (Service,
  Benutzer, Workspace, Swift-Erweiterung)
- [sandbox-profil.md](sandbox-profil.md) — Mounts, Ports, Härtung
- `docs/security/sandbox-isolation.md` — Isolationsmechanismen und die
  Entscheidung „kein IDE-Dienst im Image"
