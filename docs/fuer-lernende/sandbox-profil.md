# Sandbox-Profil: absdd-image-sandbox / Sandbox Profile

**Stand / Date:** 2026-07-05
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

**DE:** Dieses Dokument ist das konsolidierte Sandbox-Profil für Lernende. Es fasst alle Informationen
zusammen, die du für Aufgaben im 1.–3. Lehrjahr brauchst: Mounts, Schreibgrenzen, Netzwerk, Secrets,
Toolchain und KI-Agenten-Grenzen. Die Quell-Dateien sind unter `Verweise / References` verlinkt.

**EN:** This document is the consolidated sandbox profile for learners. It summarizes all information you need
for year 1–3 tasks: mounts, write boundaries, network, secrets, toolchain, and AI agent boundaries. Source
files are linked under `Verweise / References`.

---

## 1 Container-Technologie und Laufzeit / Container Technology and Runtime

**DE:**

| Eigenschaft / Property | Wert / Value |
|---|---|
| Container-Engine | Podman (oder Docker als Alternative) |
| Basis-Image | `mcr.microsoft.com/dotnet/sdk:10.0` (per SHA256-Digest gepinnt / pinned by SHA256 digest) |
| Benutzer im Container / User inside | `adedev` (kein Root-Zugriff zur Laufzeit / no root access at runtime) |
| Betriebssystem im Container / OS inside | Ubuntu (Linux) |
| Ports nach außen / Ports to host | `127.0.0.1:5100-5199` — nur für Web-App-Tests, nicht dauerhaft belegt |
| Starten / Start | `podman compose up -d` |
| Stoppen / Stop | `bash scripts/compose-down-with-audit.sh --podman -v` (empfohlen / recommended) |

**EN:**

| Property | Value |
|---|---|
| Container engine | Podman (or Docker as an alternative) |
| Base image | `mcr.microsoft.com/dotnet/sdk:10.0` (pinned by SHA256 digest) |
| User inside | `adedev` (no root access at runtime) |
| OS inside | Ubuntu (Linux) |
| Ports to host | `127.0.0.1:5100-5199` — for web app tests only, not permanently occupied |
| Start | `podman compose up -d` |
| Stop | `bash scripts/compose-down-with-audit.sh --podman -v` (recommended) |

---

## 2 Mount-Matrix / Mount Matrix

**DE:** Diese Tabelle zeigt, welche Verzeichnisse vom Host in den Container eingebunden sind und welche
Schreibrechte gelten. Alles, was nicht in dieser Liste steht, ist vom Container aus nicht erreichbar.

**EN:** This table shows which directories are mounted from the host into the container and what write
permissions apply. Anything not listed here is unreachable from the container.

| Host-Quelle / Host Source | Container-Ziel / Container Target | Lesen / Read | Schreiben / Write | Zweck / Purpose |
|---|---|---|---|---|
| `./workspace` | `/workspace` | Ja / Yes | Ja / Yes | Allgemeiner Arbeitsbereich für Projekte |
| `${ADE_DEV_SANDBOX_DIR:-.}` | `/ade-dev-sandbox` | Ja / Yes | Ja / Yes | Checkout dieses Setup-Repos für Wartungsaufgaben aus dem Container |
| `${RIDER_PROJECTS_DIR:-./workspace}` | `/rider-projects` | Ja / Yes | Ja / Yes | .NET- und Rider-Projekte |
| `${JAVA_PROJECTS_DIR:-./java-projects}` | `/java-projects` | Ja / Yes | Ja / Yes | Java-, Maven- und Spring-Boot-Projekte |
| `${GO_PROJECTS_DIR:-./go-projects}` | `/go-projects` | Ja / Yes | Ja / Yes | Go-Projekte |
| `${RUST_PROJECTS_DIR:-./rust-projects}` | `/rust-projects` | Ja / Yes | Ja / Yes | Rust-Projekte |
| `${PYTHON_PROJECTS_DIR:-./python-projects}` | `/python-projects` | Ja / Yes | Ja / Yes | Python-Projekte |
| `${SWIFT_PROJECTS_DIR:-./swift-projects}` | `/swift-projects` | Ja / Yes | Ja / Yes | Swift-Projekte |
| `${SECURE_CASE_TRACKER_PROJECTS_DIR:-./secure-case-tracker-projects}` | `/secure-case-tracker-projects` | Ja / Yes | Ja / Yes | Secure-CaseTracker-Lern- und Projektarbeiten |
| `${SECURE_SERVICE_HARVESTER_PROJECTS_DIR:-./secure-service-harvester-projects}` | `/secure-service-harvester-projects` | Ja / Yes | Ja / Yes | Secure-Service-Harvester-Lern- und Projektarbeiten |
| `${SECURE_ORDER_DESK_PROJECTS_DIR:-./secure-order-desk-projects}` | `/secure-order-desk-projects` | Ja / Yes | Ja / Yes | Secure-OrderDesk-Lern- und Projektarbeiten |
| `${AUDIT_DIR:-./audit-logs}` | `/audit` | Ja / Yes | Ja / Yes | Audit-Metadaten (beim Container-Stopp exportiert) |
| `./dotnet/ContainerBuild.props` | `/dotnet-config/ContainerBuild.props` | Ja / Yes | **Nein / No** (`:ro`) | Read-only .NET-Build-Konfiguration |
| (benanntes Volume / named volume) `dotnet_build` | `/dotnet-build` | Ja / Yes | Ja / Yes | Persistente .NET-Build-Artefakte (kein Host-Bind-Mount) |
| (benanntes Volume) `opencode_data` | `/home/adedev/.local/share/opencode` | Ja / Yes | Ja / Yes | Persistente OpenCode-Daten (kein Host-Bind-Mount) |
| (benanntes Volume) `codex_data` | `/home/adedev/.codex` | Ja / Yes | Ja / Yes | Persistente Codex-Daten (kein Host-Bind-Mount) |
| (optional) `${HOME_BASELINE_DIR}` | `/home/adedev/home-baseline-tmp` | Ja / Yes | Ja / Yes | Nur mit `compose.home-baseline.yml`; eigenes `home-baseline`-Repo |

**DE:** Alles außerhalb dieser Mounts ist **nicht sichtbar** und **nicht beschreibbar** aus dem Container.
Das ist gewollt: Was nicht gemountet ist, kann nicht beschädigt werden.

**EN:** Everything outside these mounts is **not visible** and **not writable** from the container. This is
intentional: what is not mounted cannot be damaged.

---

## 3 Schreibgrenzen / Write Boundaries

**DE:**

| Bereich / Area | Schreibrecht / Write Permission | Hinweis / Note |
|---|---|---|
| `/workspace`, `/rider-projects`, `/java-projects`, `/go-projects`, `/rust-projects`, `/python-projects`, `/swift-projects` | Ja / Yes | Projektarbeit; nur mit deinen eigenen Projektdaten |
| `/ade-dev-sandbox` | Ja / Yes | Nur für kontrollierte Wartungsaufgaben an diesem Setup-Repo |
| `/audit` | Ja / Yes | Audit-Metadaten — kein Prompt-Text, keine Secrets |
| `/dotnet-config/ContainerBuild.props` | **Nein / No** | Read-only gemountet |
| Host-Dateisystem außerhalb der Mounts / Host filesystem outside mounts | **Nicht erreichbar / Not reachable** | Isolation schützt den Host |
| `.ssh`, `.gnupg`, Credential-Dateien | **Lesen verboten / Read denied** | Durch Codex-Konfiguration blockiert |

**EN:** The container cannot write to anything outside the listed mounts. Sensitive paths like `.ssh` and
`.gnupg` are blocked from being read by the Codex agent.

---

## 4 Netzwerk-Profil / Network Profile

**DE:** Die Sandbox nutzt das Standard-Compose-Bridge-Netzwerk mit freiem ausgehenden Netzwerkzugriff
(Egress). Das ist eine **bewusste Risikoentscheidung** für die Lernumgebung: Mehrere Workflows benötigen
externe Paketquellen.

**EN:** The sandbox uses the default Compose bridge network with free outbound network access (egress). This
is a **deliberate risk decision** for the learning environment: several workflows need external package
sources.

| Verbindung / Connection | Erlaubt? / Allowed? | Zweck / Purpose |
|---|---|---|
| Ausgehender Internetzugriff (Egress) / Outbound internet (egress) | Ja / Yes (dokumentiertes Risiko / documented risk) | Paketregister, MCR, GitHub, go.dev, crates.io, npm, PyPI |
| Eingehender Zugriff (Ingress) / Inbound access (ingress) | Nur Ports 5100–5199 vom Host / Only ports 5100–5199 from host | Web-App-Tests lokal |
| Codex-Shell-Netzwerkzugriff / Codex shell network access | **Nein / No** | In `codex/config.toml` deaktiviert (`network_access = false`) |
| KI-Provider-Endpunkte / AI provider endpoints | Nur wenn lokal konfiguriert / Only when locally configured | Via `opencode.env` |

**DE:** Das freie Egress wird als Risikoentscheidung in `docs/security/network-decision.md` dokumentiert.
Es ist keine technische Blockade: Es liegt in deiner Verantwortung, keine sensiblen Daten nach außen zu
senden.

**EN:** The free egress is documented as a risk decision in `docs/security/network-decision.md`. It is not a
technical block: it is your responsibility not to send sensitive data outward.

---

## 5 Secret-Regeln / Secret Rules

**DE:** Diese Regeln gelten immer — im 1., 2. und 3. Lehrjahr, unabhängig davon, ob du die Sandbox aktiv
nutzt oder nicht.

**EN:** These rules always apply — in year 1, 2, and 3, regardless of whether you actively use the sandbox.

| Regel / Rule | Erklärung / Explanation |
|---|---|
| **Keine Secrets im Repository** / No secrets in repository | API-Schlüssel, Passwörter, Tokens gehören nicht in Git-Dateien. |
| **Keine Secrets in Prompts** / No secrets in prompts | KI-Agenten-Prompts dürfen keine echten Credentials enthalten. |
| **Keine Secrets in Logs** / No secrets in logs | Audit-Logs und Screenshots dürfen keine Secrets zeigen. |
| **Keine echten Personendaten** / No real personal data | Testdaten bleiben fiktiv und datensparsam. |
| **Secrets nur in `opencode.env`** / Secrets only in `opencode.env` | Diese Datei ist in `.gitignore` und wird nicht hochgeladen. |

**DE:** Berechtigungen: `chmod 600 opencode.env` (nur für dich lesbar).

**EN:** Permissions: `chmod 600 opencode.env` (readable only by you).

---

## 6 MSL-Support-Matrix (Toolchain) / MSL Support Matrix

**DE:** MSL bedeutet Memory-Safe Language — eine Programmiersprache, die häufige Speicherfehler durch
ihr Design verhindert. Die Sandbox unterstützt sechs MSL-Sprachen. Die Tabelle zeigt Version, Test-Befehl
und Audit-Tool je Sprache. `Supported` = funktioniert, `Open` = in Arbeit, `N/A` = nicht zutreffend.

**EN:** MSL means Memory-Safe Language — a programming language that prevents common memory errors by design.
The sandbox supports six MSL languages. The table shows version, test command, and audit tool per language.
`Supported` = works, `Open` = in progress, `N/A` = not applicable.

| Sprache / Language | Version | Status | Test-Befehl / Test Command | Audit-Tool |
|---|---|---|---|---|
| **C# / .NET** | .NET SDK 10.0 (MCR) | `Supported` | `dotnet test` | `dotnet list package --vulnerable` |
| **Go** | 1.26.3 | `Supported` | `go test ./...` | `govulncheck ./...` |
| **Java** | OpenJDK 21 | `Supported` | `mvn test` | `mvn dependency:analyze` |
| **Python** | 3.x (Ubuntu) | `Supported` | `python -m pytest` | `pip-audit` (via `uv`) |
| **Rust** | 1.95.0 | `Supported` | `cargo test` | `cargo audit` |
| **Swift** | 6.3.3 | `Open` | `swift test` | Kein globales Audit-Tool installiert / No global audit tool installed |

**DE:** Swift läuft im Container, aber iOS-Build-Tools und vollständige Apple-Plattform-Unterstützung fehlen.
Das ist als `Open` dokumentiert.

**EN:** Swift runs in the container, but iOS build tools and full Apple platform support are missing. This is
documented as `Open`.

**DE:** Prüfe Versionen mit `smoke-test-toolchains.sh` im Container:

**EN:** Check versions with `smoke-test-toolchains.sh` in the container:

```bash
bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh
```

---

## 7 KI-Agenten-Parität / AI Agent Parity

**DE:** Die Sandbox enthält vier KI-Agenten. Sie folgen denselben Regeln (keine Secrets in Prompts, keine
echten Daten, Schreibgrenzen einhalten). Die Tabelle zeigt, was gleich ist und was sich unterscheidet.

**EN:** The sandbox contains four AI agents. They follow the same rules (no secrets in prompts, no real data,
respect write boundaries). The table shows what is equal and what differs.

| Eigenschaft / Property | OpenCode | Codex CLI | Claude (VS Code) | Gemini |
|---|---|---|---|---|
| Vorinstalliert im Container / Pre-installed | Ja / Yes | Ja / Yes | Nein (VS Code-Erweiterung) / No (VS Code extension) | Nein / No |
| Schreibgrenzen konfiguriert / Write boundaries configured | Ja — `opencode.jsonc` | Ja — `codex/config.toml` | Indirekt über Repo-Regeln / Indirectly via repo rules | Indirekt / Indirectly |
| Netzwerkzugriff (Shell-Ebene) / Network access (shell level) | Anfrage nötig / Requires approval | **Nein** (`network_access = false`) | Anfrage nötig / Requires approval | Anfrage nötig / Requires approval |
| Secrets in Prompts / Secrets in prompts | **Verboten / Forbidden** | **Verboten / Forbidden** | **Verboten / Forbidden** | **Verboten / Forbidden** |
| Darf Systemdateien ändern? / May modify system files? | Nein — blockiert / No — blocked | Nein — blockiert / No — blocked | Nein — Repo-Regeln / No — repo rules | Nein — Repo-Regeln / No — repo rules |
| Agent-Caches im Repo committen / Commit agent caches | **Nicht erlaubt / Not allowed** | **Nicht erlaubt / Not allowed** | **Nicht erlaubt / Not allowed** | **Nicht erlaubt / Not allowed** |
| Konfigurationsquelle / Config source | `opencode.jsonc` | `codex/config.toml`, `codex/requirements.toml` | CLAUDE.md, Repo-Regeln | GEMINI.md, Repo-Regeln |

**DE:** Alle Agenten gelten als gleichwertig — die Sicherheitsregeln sind nicht agentenspezifisch.

**EN:** All agents are treated as equivalent — the security rules are not agent-specific.

---

## 8 Laufzeit-Härtung / Runtime Hardening

**DE:** Die Container-Laufzeit ist zusätzlich abgesichert:

**EN:** The container runtime has additional hardening:

| Maßnahme / Measure | Einstellung / Setting | Wirkung / Effect |
|---|---|---|
| Kein Root zur Laufzeit / No root at runtime | `USER adedev` im Dockerfile | Keine Root-Rechte für laufende Prozesse |
| Keine neuen Privilegien / No new privileges | `security_opt: no-new-privileges:true` | `setuid`/`setgid`-Binaries können keine Rechte erhöhen |
| Alle Linux-Capabilities entzogen / All Linux capabilities dropped | `cap_drop: ALL` | Minimale Systemberechtigungen |
| Kein privilegierter Modus / No privileged mode | kein `privileged: true` in `compose.yml` | Container hat keine Host-Kernel-Kontrolle |

---

## 9 Abweichungen begründen / Justifying Deviations

**DE:** Es ist erlaubt, außerhalb der Sandbox zu arbeiten — aber Abweichungen müssen begründet dokumentiert
werden. Eine undokumentierte Abweichung ist ein verstecktes Risiko. Eine begründete Abweichung ist eine
bewusste Entscheidung.

**EN:** It is allowed to work outside the sandbox — but deviations must be documented with a rationale. An
undocumented deviation is a hidden risk. A justified deviation is a conscious decision.

**DE:** Format für eine Abweichung:

**EN:** Format for a deviation:

```text
Abweichung / Deviation: [Was lief außerhalb / What ran outside]
Grund / Reason:          [Warum nötig / Why necessary]
Auswirkung / Effect:     [Was kann dadurch schiefgehen / What could go wrong]
Restrisiko / Residual risk: [Wie begrenzt / How limited]
Status:                  Open / N/A
```

---

## Verweise / References

**DE:** Detailquellen für dieses Profil:

**EN:** Detail sources for this profile:

- `compose.yml` — Mount-Konfiguration
- `docs/security/sandbox-freigabe.md` — Genehmigte Mount- und Tool-Liste
- `docs/security/sandbox-isolation.md` — Isolationsmechanismen und Evidenz
- `docs/security/network-decision.md` — Netzwerk-Risikoentscheidung
- `codex/config.toml` — Codex-Schreibgrenzen
- `opencode.jsonc` — OpenCode-Sicherheitsregeln
- `Dockerfile` — Tool-Versionen und Image-Build
- `docs/secure-development/checklisten/CL_12_Agentische-KI-Sandbox.md` — Checkliste Sandbox-Governance
