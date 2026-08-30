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

## Dokumentationsverantwortung / Documentation Responsibility

| Thema / Topic | Kanonische Quelle / Canonical source |
|---|---|
| Lernpfad, institutionelles Git-Hosting, Governance und Home-Source-/Runtime-Vertrag / learner path, institutional Git hosting, governance, and Home source/runtime contract | [Home-Baseline-Architektur](https://github.com/hindermath/home-baseline/blob/main/docs/architecture/source-and-home-runtime.md) und die dort verlinkten Lernleitfaeden / Home Baseline architecture and its linked learner guides |
| Image-Build, Toolversionen, Container-Mounts, Laufzeitbefehle und installierter Runtime-Wrapper / image build, tool versions, container mounts, runtime commands, and installed runtime wrapper | dieses Repository: `Dockerfile`, Compose-Dateien, Skripte und `docs/betrieb/` / this repository: `Dockerfile`, Compose files, scripts, and `docs/betrieb/` |

**DE:** `home-baseline.lock.json` bestimmt den exakten eingebetteten und offline
lesbaren Stand. Ein Link auf `home-baseline/main` zeigt den aktuellen Upstream
und kann neuer sein. Das Image stellt eigene Mounts fuer genau drei
Secure-Trader-Reihen bereit: CaseTracker, ServiceHarvester und OrderDesk. Dieser
operative Ausschnitt erweitert oder beschraenkt den kanonischen Home-Baseline-
Katalog nicht.

**EN:** `home-baseline.lock.json` defines the exact embedded, offline-readable
state. A link to `home-baseline/main` shows the current upstream and may be
newer. The image provides dedicated mounts for exactly three Secure Trader
series: CaseTracker, ServiceHarvester, and OrderDesk. This operational subset
neither extends nor restricts the canonical Home Baseline catalog.

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

## Aktueller Verifikationsstand / Current Verification State

**DE:** Der technische Referenzstand fuer diese Dokumentation ist das lokale
Image `sha256:5bec1910211e61f60d140907a75689f9f6e31c2ec5baceaac7ff10b99d846eaf`.
Build, macOS-rootless-Podman-Runtime, Toolchain-Smoke, sechs Agenten-CLIs,
Dispatcher-Dry-run, Audit-Stopp und genau eine SBOM-/Grype-Kette sind belegt.
Linux- und Windows/WSL2-Hostparitaet, VS-Code-Attach, der menschliche
Erstnutzungstest sowie 14 Critical- und 360 High-Matches bleiben offen. Darum
bleibt der Feature-Abschluss blockiert.

**EN:** The technical reference state is the local image above. Build, native
macOS rootless-Podman runtime, toolchain smoke, six agent CLIs, dispatcher
dry-run, audit stop, and one SBOM/Grype chain are evidenced. Linux and
Windows/WSL2 host parity, VS Code attachment, the human first-use test, and 14
Critical plus 360 High matches remain open, so feature completion is blocked.

Die kanonischen Laufdaten stehen im
[Feature-Evidenzindex](../security/secure-development/2026-08-30-container-hardening/README.md).
Sie ersetzen keine formelle Security- oder Plattformfreigabe. / Canonical run
data is in the feature evidence index and does not replace formal approval.
