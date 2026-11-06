# Codex-Konfigurationsstandard / Codex configuration default

Documentation Impact: `UpdateRequired`. Owner: Repository Maintainer.
Audience: operators and maintainers. Canonical sources: `codex/config.toml`,
`codex/requirements.toml`, `scripts/smoke-test-toolchains.sh`.
Reader paths: README and `docs/betrieb/validierung-und-wartung.md`.
Language: German first, English second; document class: ActiveSemantic.
Distribution: image and repository; no host Home sync.
Reevaluate on Codex upgrades or changes to approvals and smoke commands.

## Deutsch

Codex 0.164.0 meldet seine Version, ohne die Konfiguration zu laden. Deshalb
bestand die bisherige Versionspruefung trotz des nicht mehr unterstuetzten
expliziten Standards `approval_policy = "untrusted"`.
Der Image-Standard ist jetzt `on-request`. Die Requirements behalten
`untrusted` fuer automatisch abgeleitete Projekt-Policies und `never` fuer
den bestehenden Headless-Pfad. Sandbox-, Netzwerk- und Secret-Grenzen sowie
Modellrouting bleiben unveraendert.

Beide Smoke-Modi laden die Konfiguration mit `codex features list`, ohne
Policy-Override oder Modellaufruf. Der komplette Smoke-Test bricht bei einem
Ladefehler ab; der JSON-Modus meldet `codex-config` als fehlgeschlagen.
Ein synthetischer Regressionstest prueft erfolgreiche Versionsausgabe bei
gleichzeitigem Konfigurationsfehler. Pin-Vertragstests verhindern das Entfernen
des Ladetests und einen nicht erlaubten interaktiven Standard.

Lokale Abnahme: Codex 0.164.0 aus dem bereits gebauten ARM64-Image mit den
korrigierten Konfigurationsdateien als Read-only-Mounts, ohne Netzwerk oder
persistente Agenten-/Projektvolumes. Kein Image-Neubau, kein Austausch des
bestehenden Containers in dieser Aenderung. Windows-/AMD64-Abnahme offen.
Lokal bestanden: 2 Smoke-Regressionstests, 8 Pin-Abdeckungstests,
15 Versions-Pin-Tests, Pin-Validator, Bash-Syntax und Compose-Konfiguration.
Die Pin-CI fuehrt den neuen Regressionstest explizit auf ihrer vorhandenen
Plattformmatrix aus.

## English

Codex 0.164.0 reports its version without loading configuration. The previous
version check therefore passed despite the unsupported explicit `untrusted`
default. Use `on-request` for interactive image sessions. Requirements retain
`untrusted` for derived project policies and `never` for the existing headless
path. Sandbox, network, secret boundaries and model routing remain unchanged.

Both smoke modes now run `codex features list` without policy overrides or
model calls. Loading errors fail smoke; JSON reports the `codex-config` entry
as failed. Regression coverage distinguishes successful version reporting
from failed configuration loading. Pin contracts reject removing the loading
test or changing the interactive default.

Local validation uses the existing ARM64 image and corrected read-only config
mounts, without network or persistent agent/project volumes. No image rebuild
or replacement of the existing container is part of this change.
Windows/AMD64 acceptance remains open.

Reference: [Official configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).
