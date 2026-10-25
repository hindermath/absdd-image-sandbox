# Entwickler-Kurzpfad / Developer Short Path

[Einstieg / Start](README.md)

## Ziel / Goal

**DE:** Dieser Pfad setzt normale Git- und Programmiererfahrung voraus, aber
keine Container-, KI- oder Spec-Kit-Spezialkenntnisse. Ohne Shell-Erfahrung
beginne bei den [Lernwegen](lernwege.md). Es ist ein kuerzerer Leserpfad,
keine Abkuerzung um Sicherheitskontrollen.

**EN:** This path assumes normal Git and programming experience, but no
container, AI or Spec Kit expertise. Without shell experience, start with the
learning paths. This is a shorter reading route, not a security bypass.

## Ablauf / Workflow

**DE:** Der Fork-/Upstream-Standard gilt weiter. Ein bewusst unabhängiges Repo
kann später das [optionale Template-Profil](template-profil.md) nutzen; es ist
noch nicht aktiviert. Keine unverbundenen Historien mergen oder kopierte
Freigaben als eigene ausgeben. Persönliche Produktrepos bleiben getrennt.

**EN:** Fork/upstream remains the default. Deliberately independent repos may
later use the optional template profile; it is not enabled yet. Do not merge
unrelated histories or inherit approvals. Personal product repos stay separate.

1. **DE:** [Sandbox-Profil](sandbox-profil.md) lesen: Mounts erlauben Zugriff
   auf echte Host-Dateien; Netzwerk und Secrets sind eigene Grenzen.
   **EN:** Read the sandbox profile: mounts expose real host files; network
   and secrets are separate boundaries.
2. **DE:** Eigenen Fork oder institutionelles Repo als `origin`, Referenz als
   `upstream` waehlen. [Git-Anleitung](git-und-hosting.md) beachten.
   **EN:** Use your own fork or institutional repository as origin and the
   reference as upstream; follow the Git guide.
3. **DE:** [Installation](installation.md) fuer genau einen Hostpfad
   durchlaufen. `.env` ist lokale Compose-Konfiguration, kein Image-Inhalt.
   **EN:** Follow installation for exactly one host path. `.env` is local
   Compose configuration, not image content.
4. **DE:** Projekt im vorgesehenen Mount oeffnen, Lock-Dateien und lokale
   Build-Wrapper nutzen. [Toolchain auswaehlen](toolchains/README.md).
   **EN:** Open your project in its designated mount, use lock files and
   project-local build wrappers; select its toolchain.
5. **DE:** Optional [VS Code anbinden](vscode-dev-containers.md).
   Desktop-Anwendung auf dem Host, Shell und Compiler im Container nicht
   verwechseln. Installierte CLI bedeutet keine Desktop-Fernsteuerung.
   **EN:** Optionally attach VS Code. Distinguish the host desktop app from
   the container shell and compiler. Installing a CLI does not provide
   desktop remote control.
6. **DE:** Vor KI-Nutzung [Agenten und Spec Kit](agenten-und-spec-kit.md)
   lesen. Nur genehmigte Daten und Werkzeuge nutzen. Fuer Einzelauftraege
   [Prompt-Dispatcher](agent-prompt.md) verwenden; er richtet keine Anmeldung
   oder Freigabe ein.
   **EN:** Before AI use, read agents and Spec Kit. Use approved data and
   tools only. Use the prompt dispatcher for individual tasks; it does not
   configure sign-in or approval.
7. **DE:** Projekttests, menschliches Diff-Review und [sicherer Stopp](alltag.md)
   abschliessen. Ein erfolgreiches Smoke-Skript ist keine Security-Freigabe.
   **EN:** Finish project tests, human diff review and safe shutdown. A
   successful smoke script is not security approval.

## Erste Diagnose / First Diagnosis

**DE:** Diese Befehle laufen auf dem Host im Sandbox-Checkout. Sie aendern
keine Projektdateien. Erwartet werden ein erreichbares Podman, ein laufender
Service sowie ein Non-root-Benutzer im Container.

**EN:** Run these commands on the host in the sandbox checkout. They change
no project files. Expect reachable Podman, a running service and a non-root
container user.

```bash
podman info
podman compose ps
podman compose exec ade id
```

**DE:** Fehlerhilfe: [FAQ](faq.md). Versions-Soll und laufendes Image sind
verschieden: Ein Dockerfile-Update aendert einen vorhandenen Container nicht.

**EN:** Troubleshooting: FAQ. Target versions and a running image differ:
updating the Dockerfile does not change an existing container.
