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

Der lokale Sitzungsstart verwendet `codex app-server --strict-config`,
`initialize` und ein ephemeres `thread/start` mit temporaerem `AGENTS.md`.
Kein Modell-Turn wird gestartet. Server und Hilfsprozesse erhalten ein
gemeinsames Zeitlimit und werden im Cleanup beendet. Beide Smoke-Modi
melden einen fehlgeschlagenen Start als Fehler (`codex-session` im JSON).

Der rootless Adapter erhaelt die leere Modus-000-Maskierung des eigenen
Daemonverzeichnisses, ohne einen nicht unterstuetzten Read-only-Remount zu
verlangen. Fehlende oder leere geschuetzte Metadatenziele erhalten einen
Read-only-Bind eines unveraenderlichen root-eigenen leeren Verzeichnisses.
Symlinks und nichtleere Metadaten werden nicht so ersetzt. Die vorhandene
Dateimaskierung schliesst auch `history.jsonl` ein; `/tmp` bleibt read-only.
`commit_attribution` und das ignorierte Requirements-Feld
`permissions.filesystem.glob_scan_max_depth` entfallen. Explizite Mustertiefen
fuer Secret-Dateien bleiben erhalten.

Der Owner hat Image-Build und Container-Austausch aus dem PR-Branch
ausdruecklich autorisiert, jedoch keinen Merge. Native ARM64-Abnahme:
Sitzungsstart sowie synthetische Schreib-, Secret- und Socket-Negativtests.
Windows-/AMD64-Abnahme offen.
Fuer Host-Bind-Mounts setzt Compose den SELinux-Typ `container_engine_t`,
ohne SELinux oder die innere Sandbox abzuschalten. Der vorherige Standardtyp
blockierte den verschachtelten Bind-Mount von `/rider-projects`.
Abgrenzung: [Isolationsnachweis](../security/sandbox-isolation.md).
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

Both smoke modes additionally initialize an ephemeral local session with an
AGENTS.md fixture using the strict-config app server. No model turn starts;
a bounded deadline and process-group cleanup cover server and helpers.
The rootless adapter retains empty mode-000 daemon masking while avoiding an
unsupported remount. Missing or empty protected metadata uses a root-owned
immutable empty read-only bind; symlinks and nonempty metadata are excluded.
The existing file mask also covers history.jsonl and /tmp remains read-only.
Remove ignored commit_attribution and requirements glob_scan_max_depth;
explicit secret-pattern depths remain unchanged.

The owner authorized native ARM64 image build and container replacement from
the PR branch, without merging. Validation includes session startup and
synthetic negative write, secret-read and daemon-socket tests.
Windows/AMD64 acceptance remains open.
For host bind mounts Compose uses the SELinux `container_engine_t` type.
The prior default type blocked the nested /rider-projects bind mount.
SELinux and inner sandbox restrictions remain enabled; see the isolation record.

Reference: [Official configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).
