# Image-Aufbau / Image Construction

## Verbindliche Quellen / Authoritative Sources

| Thema / Topic | Kanonische Quelle / Canonical source |
|---|---|
| Basisimage, Toolversionen, Installation | `Dockerfile` |
| Renovate-Erkennung | Kommentare direkt vor jedem `ARG` und `renovate.json` |
| Codex-Untergrenzen | `codex/config.toml`, `codex/requirements.toml` |
| OpenCode-Berechtigungen | `opencode.jsonc` |
| Spec-Kit-Installationspatch | `spec-kit/patch-specify-cli.py` |
| Home-Baseline-Quelle | `home-baseline.lock.json` |
| Laufzeitstart und Stop-Hook | `scripts/container-entrypoint.sh` |

**DE:** Versionswerte werden hier nicht als zweite Tabelle kopiert. Lies die
aktuellen `ARG`-Werte im Dockerfile oder frage die laufenden Werkzeuge ab. So
bleibt das Dockerfile die einzige Versionsquelle.

**EN:** Version values are not copied into a second table here. Read the
current `ARG` values in the Dockerfile or query the running tools. This keeps
the Dockerfile as the single version source.

## Basis und Paketinstallation / Base and Package Installation

**DE:** Der Build startet mit dem Microsoft-.NET-SDK-Image aus MCR. Tag und
SHA256-Digest stehen gemeinsam in `FROM`: Der Tag bleibt lesbar, der Digest
macht den Inhalt reproduzierbar. Ubuntu-Pakete liefern unter anderem JDK,
Maven, Python, Buildwerkzeuge, PowerShell aus dem Basisimage und allgemeine
CLI-Helfer. Node.js wird über ein signiertes NodeSource-APT-Repository
installiert.

**EN:** The build starts from the Microsoft .NET SDK image in MCR. Tag and
SHA256 digest appear together in `FROM`: the tag remains readable and the
digest makes content reproducible. Ubuntu packages provide the JDK, Maven,
Python, build tools, PowerShell from the base image, and common CLI helpers.
Node.js is installed from a signed NodeSource APT repository.

**DE:** Jede `ARG`-Zeile besitzt unmittelbar davor Renovate-Metadaten mit
passendem `argName`. Ein Update ist erst nach Build, Toolchecks und Review
zulässig. `latest` ist keine zulässige Versionsstrategie für die im
Dockerfile verwalteten Werkzeuge.

**EN:** Every `ARG` line has Renovate metadata with a matching `argName`
immediately above it. An update is acceptable only after build, tool checks,
and review. `latest` is not an acceptable version strategy for tools managed
by the Dockerfile.

## Toolchain-Schichten / Toolchain Layers

| Familie / Family | Installation und Kontrolle / Installation and control |
|---|---|
| .NET und PowerShell | aus gepinntem Basisimage; Build prüft die erwartete PowerShell-Version / from pinned base image; build checks expected PowerShell version |
| Java | Ubuntu OpenJDK und Maven / Ubuntu OpenJDK and Maven |
| Go | Releasearchiv; zusätzliche Werkzeuge als Benutzer `adedev` / release archive; additional tools as user `adedev` |
| Rust | festes `rustup-init` mit SHA256-Prüfung; Komponenten über gepinnte Toolchain / pinned `rustup-init` with SHA256 verification; components through pinned toolchain |
| Python | Ubuntu Python plus verifiziertes `uv`/`uvx`-Release / Ubuntu Python plus verified `uv`/`uvx` release |
| Swift | signiertes Ubuntu-Release, Architekturprüfung, SourceKit-LSP / signed Ubuntu release, architecture check, SourceKit-LSP |
| Node.js | signierte APT-Quelle; npm für globale Agentenpakete / signed APT source; npm for global agent packages |

**DE:** Unterstützte Architekturen werden im Build explizit auf `amd64` und
`arm64` abgebildet. Ein unbekannter Wert bricht den Build ab, statt ein
unpassendes Artefakt zu laden.

**EN:** Supported architectures are mapped explicitly to `amd64` and `arm64`
during the build. An unknown value fails the build instead of downloading an
incorrect artifact.

## Agenten- und Sicherheitswerkzeuge / Agent and Security Tools

**DE:** OpenCode, Codex, Claude Code, Gemini CLI und GitHub Copilot CLI werden
als fest versionierte npm-Pakete installiert. Antigravity wird als
architekturspezifisches Release mit festem SHA256-Wert installiert. Syft wird
aus einem Releasearchiv geladen und gegen die veröffentlichte Checksumme
geprüft. Keine Installation nimmt einen Provider, ein Modell oder einen
Benutzeraccount vorweg.

**EN:** OpenCode, Codex, Claude Code, Gemini CLI, and GitHub Copilot CLI are
installed as fixed-version npm packages. Antigravity is installed from an
architecture-specific release with a fixed SHA256 value. Syft is downloaded
from a release archive and checked against the published checksum. No
installation preselects a provider, model, or user account.

**DE:** Codex erhält systemweite Benutzer-, Managed- und Requirements-Layer.
OpenCode erhält eine kommentierte Berechtigungskonfiguration. Benutzerzustand
wird erst zur Laufzeit in getrennten Volumes geschrieben.

**EN:** Codex receives system-wide user, managed, and requirements layers.
OpenCode receives a commented permission configuration. User state is written
only at runtime into separate volumes.

## Spec Kit / Spec Kit

**DE:** Spec Kit wird mit `uv tool install` aus einem festgelegten Git-Tag
installiert. Der anschließende Python-Patch verändert nur die Kopieroperation,
damit Initialisierung auf Windows-/WSL2-Bind-Mounts stabiler funktioniert. Er
darf keine Spec-Kit-Kommandosemantik verändern.

**EN:** Spec Kit is installed with `uv tool install` from a fixed Git tag. The
following Python patch changes only the copy operation so initialization works
more reliably on Windows and WSL2 bind mounts. It must not change Spec Kit
command semantics.

## Benutzer und Dateirechte / User and File Permissions

**DE:** Systempakete und Dateien werden als `root` in das Image installiert.
Danach wird der Benutzer `adedev` angelegt. Der finale `USER` ist `adedev`;
auch der Compose-Service startet nicht privilegiert. `/dotnet-build` und die
Agentenverzeichnisse sind für diesen Benutzer vorbereitet.

**EN:** System packages and files are installed into the image as `root`.
Then user `adedev` is created. The final `USER` is `adedev`; the Compose service
also starts without privileged mode. `/dotnet-build` and agent directories are
prepared for this user.

## Eingebettete Home Baseline / Embedded Home Baseline

**DE:** `home-baseline.lock.json` enthält öffentliche Quelle, Release-Tag,
exakten Commit und Lizenz. Der Build prüft Tag und Commit, erstellt einen
shallow Git-Checkout unter `/opt/home-baseline` und entfernt Schreibrechte.
`/home/adedev/home-baseline-source` ist der kanonische Link;
`/home/adedev/home-baseline-tmp` bleibt nur als veralteter Kompatibilitätslink.

**EN:** `home-baseline.lock.json` records the public source, release tag, exact
commit, and license. The build verifies tag and commit, creates a shallow Git
checkout under `/opt/home-baseline`, and removes write permissions.
`/home/adedev/home-baseline-source` is the canonical link;
`/home/adedev/home-baseline-tmp` remains only as a deprecated compatibility
link.

**DE:** Kein Baseline-Skript läuft beim Build oder Start automatisch. Nur der
explizite Wrapper `sync-home-baseline-runtime` kennt die drei Modi
`--dry-run`, `--check-only` und `--apply`. Ein Schreibmodus benötigt einen
bewussten Aufruf und bleibt auf manifestdefinierte `homeRuntime`-Inhalte
begrenzt.

**EN:** No baseline script runs automatically during build or startup. Only
the explicit `sync-home-baseline-runtime` wrapper supports the three modes
`--dry-run`, `--check-only`, and `--apply`. A write mode needs a deliberate
call and remains limited to manifest-defined `homeRuntime` content.

## Entrypoint und Lebenszyklus / Entrypoint and Lifecycle

**DE:** `ade-entrypoint` startet den Compose-Prozess als Kindprozess. Bei
`TERM`, `INT` und normalem Ende versucht er einmal, `audit-export` auszuführen.
Dieser Best-Effort-Hook ersetzt nicht den dokumentierten Stop-Wrapper, weil ein
Hard Kill oder Hostabbruch den Hook umgehen kann.

**EN:** `ade-entrypoint` starts the Compose process as a child. On `TERM`,
`INT`, and normal exit, it attempts to run `audit-export` once. This
best-effort hook does not replace the documented stop wrapper because a hard
kill or host abort can bypass it.

## Änderungskontrolle / Change Control

**DE:** Bei Änderungen am Dockerfile mindestens Renovate-Metadaten, Digest-
und Checksum-Verträge, beide Architekturen, Build, Toolversionen, Smoke-Test,
SBOM und Dokumentation prüfen. Ein erfolgreicher Build auf nur einer
Architektur ist kein vollständiger Multi-Arch-Nachweis.

**EN:** For Dockerfile changes, verify at least Renovate metadata, digest and
checksum contracts, both architectures, build, tool versions, smoke test,
SBOM, and documentation. A successful build on one architecture is not full
multi-architecture evidence.

Weiter zu [Compose und Speicher](compose-und-speicher.md). / Continue with
[Compose and storage](compose-und-speicher.md).
