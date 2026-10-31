# Agent Security Review — Feature 004

Stand: 2026-10-31. Sollversionen und Basiskonfiguration aus `Dockerfile`,
`opencode.jsonc`, `codex/{config,requirements}.toml`, `compose.yml`; kein
Providerlogin, Modellaufruf oder Zugriff auf persistente Agentendaten.

## Deutsch

| Client / Sollversion | Konfigurationsschichten und Zustand | Datenfluss bei bewusster Nutzung | Updateweg und aktueller Schalter |
|---|---|---|---|
| OpenCode 2.1.4 | Image kopiert globale `opencode.jsonc` nach `/home/adedev/.config/opencode/`; User-/Projekt-/Agenten-/Inline-Overrides können je nach V2-Präzedenz wirksam werden. Persistente Daten unter `opencode_data`. | Projektinhalt, Prompts und Antworten können nach Providerwahl an den gewählten Dienst gehen; im Repo kein Schlüssel/Modell vorausgewählt. | `update: disable` in globaler Konfiguration; Image/Renovate ist vorgesehener Updateweg. Die [V2-Konfiguration](https://dev.opencode.ai/v2/docs/config/) dokumentiert, dass Projektwerte dieses Updatefeld nicht überschreiben. |
| Codex 0.164.0 | `/etc/codex/config.toml` als Default, `/etc/codex/requirements.toml` als restriktive Vorgaben; User- und Projektkonfiguration weiter möglich innerhalb der Vorgaben. `codex_data` separat. | Nach Anmeldung können Aufgaben-/Kontextdaten an den gewählten Dienst gehen; kein Provider/Modell im Image erzwungen. | npm-Paket ist gepinnt; kein belegter, im Container laufender Selbstupdater. User-initiiertes CLI-/npm-Update wird nicht als ausgeschlossen behauptet. |
| Claude Code 2.1.310 | `CLAUDE_CONFIG_DIR=/home/adedev/.claude` mit `claude_data`; lokale Settings/Projektdateien bleiben mögliche Overrides. | Nach Anmeldung können Projektkontext und Dialog an den Dienst gehen. | `DISABLE_AUTOUPDATER=1` im Image; [Anthropic-Dokumentation](https://docs.anthropic.com/en/docs/claude-code/getting-started) nennt diesen Schalter. |
| Gemini CLI 0.65.0 | `GEMINI_CLI_HOME=/home/adedev/.gemini-home`, persistentes `gemini_data`; User-/Workspace-Settings sind möglich. Neues root-eigenes `/etc/gemini-cli/settings.json` enthält `general.enableAutoUpdate=false`. Der [Quellstand v0.65.0](https://raw.githubusercontent.com/google-gemini/gemini-cli/v0.65.0/packages/cli/src/config/settings.ts) mischt System-Overrides nach User/Workspace; die [v0.65.0-Settings](https://raw.githubusercontent.com/google-gemini/gemini-cli/v0.65.0/docs/cli/settings.md) nennen `true` als Default. | Anmeldung/Projektfreigabe kann Code und Dialog an Google-Dienste senden; keine Anmeldung im Image. | System-Override deaktiviert automatische Updates; npm/Renovate bleibt Updateweg. `GEMINI_CLI_SYSTEM_SETTINGS_PATH` oder CLI-/Umgebungs-Overrides können die Wirksamkeit verändern und brauchen nativen Test. |
| GitHub Copilot CLI 1.0.103 | `COPILOT_HOME=/home/adedev/.copilot` mit `copilot_data`; benutzereigene Einstellungen/Projektkontext möglich. | Nach Anmeldung können Projektkontext und Dialog an GitHub-Dienste gehen. | `COPILOT_AUTO_UPDATE=false` laut [GitHub-Referenz](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) für CLI und First-Party-Plugins. |
| Antigravity CLI 1.4.7 | `agy` ist native Release-Binärdatei; Zustand unter `gemini_data` geteilt, keine separate Antigravity-Volume-Isolation behauptet. Konfigurations- und Berechtigungsebenen der Binärdatei bleiben versionsgebunden zu prüfen. | Nach expliziter Anmeldung können Kontext/Dialog an Google-Dienste gehen; Printmodus ist im Dispatcher experimentell. | `AGY_CLI_DISABLE_AUTO_UPDATE=true` gesetzt. [Upstream-Issue #1046](https://github.com/google-antigravity/antigravity-cli/issues/1046) zeigt `true` mit Logbeleg für 1.2.6 und dass `1` dort nicht reicht; für 1.4.7 ist native Wirkung Open. |

### Synthetische Wirkungsprüfung und Grenzen

`scripts/tests/test_opencode_v2_policy.py` prüft den aktuellen globalen
OpenCode-Regelsatz, Exclusions und eine explizit **synthetische** Folge
globaler, Agenten-, Projekt- und Subagentenregeln. Die Fälle zeigen auch,
dass spätere passende Allow-Regeln den modellierten Schutz schwächen können.
Sie prüfen keine interne Merge-Implementierung des installierten CLI.
Ein isolierter Fake-Updater prüft die fünf gesetzten Werte und einen
Negativfall; er startet keinen Agenten und keinen Download. Sieben Tests
bestanden auf dem macOS-Host am 2026-10-31. Vollzug bei Image-Start,
Projekt-Overrides, echte Subagentenberechtigungen und Modellschleifen sind
damit **nicht** belegt.

`UPD-V2-LOOP` bleibt Open: Owner Security Review mit Repository Maintainer;
Trigger vor freigabepflichtiger realer Nutzung, bei OpenCode-V2-Update oder
Änderung von Agenten-/Projektkonfiguration. Bis zur Entscheidung keine
unbeaufsichtigten realen Modell-/Providerläufe als Nachweis verwenden.
Das Repo ist kein Zugriffsschutz gegen bewusst gewählte eigene CLI-Flags,
User-Dateien oder Host-/Containerrechte. Die getrennten Volumes verhindern
keinen Datenfluss an einen explizit angemeldeten Provider.

### Disposition T038/T039

Der aktuelle Quellstand zeigt automatische Updates als behebbaren Defekt bei
Gemini, Copilot und Antigravity; die engen Schalter stehen jetzt im Image.
Claude und OpenCode waren bereits deaktiviert. Für Codex ist kein belegter
Selbstupdatepfad in diesem Paketstand identifiziert; er bleibt als
Nutzungs-/Updategrenze dokumentiert. Die vorhandenen OpenCode- und
Codex-Regeln wurden nicht gelockert. Es ist keine zusätzliche
Override-/Ausschlusslücke belegt, die eine breite Rechteänderung rechtfertigt.
Native Wirksamkeit und Versionschecks folgen im separaten T059-Build.

## English

The table records each of the six image clients separately, with intended
version, configuration layers, persistent state, possible provider data flow
and update control. No image provider or model is preselected. The isolated
seven-case policy suite and fake updater check committed controls only; they
do not prove CLI behavior, provider isolation or real loop limits. Gemini,
Copilot and Antigravity update switches have been added narrowly. OpenCode and
Claude controls were already present. `UPD-V2-LOOP`, version-specific native
effects and any owner approval remain Open before approval-bound real use.
