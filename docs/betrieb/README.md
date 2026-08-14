# Betriebs- und Maintainer-Referenz / Operations and Maintainer Reference

## Zweck / Purpose

**DE:** Diese Referenz erklärt, wie das Image gebaut ist, welche Host- und
Containergrenzen Compose setzt und wie Maintainer Änderungen nachweisbar
prüfen. Sie richtet sich an Repository-Maintainer, Lehrende, Security-Review
und ausführende Agenten. Für den geführten Einstieg ab dem ersten
Ausbildungsjahr ist [Für Lernende](../fuer-lernende/README.md) der richtige
Startpunkt.

**EN:** This reference explains how the image is built, which host and
container boundaries Compose establishes, and how maintainers validate
changes with evidence. It is intended for repository maintainers, instructors,
security review, and executing agents. [For learners](../fuer-lernende/README.md)
is the correct starting point for the guided path from the first training year.

## Leserpfad / Reader Path

1. [Image-Aufbau](image-aufbau.md) — Basisimage, Toolchains, Agenten,
   Benutzer und eingebettete Home Baseline. / Base image, toolchains, agents,
   users, and embedded Home Baseline.
2. [Compose und Speicher](compose-und-speicher.md) — Mounts, Volumes, Ports,
   Netzwerk, Umgebungsvariablen und Härtung. / Mounts, volumes, ports,
   network, environment variables, and hardening.
3. [Validierung und Wartung](validierung-und-wartung.md) — statische Checks,
   Build, Smoke-Tests, Audit, SBOM, Shutdown und Plattformnachweise. / Static
   checks, build, smoke tests, audit, SBOM, shutdown, and platform evidence.

## Source-of-Truth-Reihenfolge / Source-of-Truth Order

**DE:** Bei Widersprüchen gilt folgende Reihenfolge:

1. Ausführbares und validiertes Verhalten des aktuellen Images.
2. `Dockerfile`, `compose.yml`, Overrides, Lock-Dateien und Skripte.
3. Aktive Sicherheits- und Freigabenachweise unter `docs/security/`.
4. Diese erklärende Dokumentation.

**EN:** If statements conflict, use this order:

1. Executable and validated behavior of the current image.
2. `Dockerfile`, `compose.yml`, overrides, lock files, and scripts.
3. Active security and approval evidence under `docs/security/`.
4. This explanatory documentation.

## Systemgrenze / System Boundary

| Bereich / Area | Verantwortung / Responsibility |
|---|---|
| Image-Build | installiert gepinnte Werkzeuge und unveränderliche Referenzinhalte / installs pinned tools and immutable reference content |
| Compose-Service `ade` | verbindet explizite Host-Mounts, Volumes, Ports und Laufzeitkontrollen / connects explicit host mounts, volumes, ports, and runtime controls |
| Benutzer `adedev` | führt Lern-, Build- und Agentenarbeit ohne Root-Rechte aus / performs learning, build, and agent work without root privileges |
| Host | betreibt Podman, hält Projektquellen und entscheidet über lokale Secrets / runs Podman, stores project sources, and decides on local secrets |
| Hosting-Plattform | setzt Repository-Regeln, Reviews und Admin-Entscheidungen durch / enforces repository rules, reviews, and admin decisions |

**DE:** Das Repository beschreibt keine formelle Sandbox-, Provider-, Modell-
oder Datenklassifikationsfreigabe als abgeschlossen. Offene menschliche
Entscheidungen bleiben in den Sicherheitsnachweisen sichtbar.

**EN:** The repository does not claim formal sandbox, provider, model, or data
classification approval as complete. Open human decisions remain visible in
the security evidence.

## Sichere nächste Aktion / Safe Next Action

**DE:** Prüfe vor einer Änderung den Arbeitsbaum und die statische Compose-
Konfiguration:

**EN:** Before changing anything, inspect the worktree and the static Compose
configuration:

```bash
git status --short --branch
podman-compose config
```
