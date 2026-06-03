# KI-Werkzeug-Inventar

Stand: 2026-06-03

Dieses Inventar dokumentiert die in dieser Sandbox vorgesehenen KI- und
agentischen Werkzeuge. OpenCode wird in diesem Image ohne Modellanbieter
ausgeliefert. Felder mit `_TODO_` muessen durch den Owner oder die
verantwortliche Stelle gepflegt werden; sie werden nicht aus Annahmen
abgeleitet.

## Deutsch

| Werkzeug | Variante | Vendor | Endpoint | EU-Datenresidenz | ZDR-Status | DPA-Datum | Trainings-Opt-out | OpenSSF-Scorecard | freigegeben bis | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| OpenCode | CLI im Container, npm-Paket `opencode-ai` Version `1.14.50`; kein vorkonfigurierter Modellanbieter | OpenCode-Projekt / npm-Paket; Modellanbieter nicht konfiguriert | Nicht konfiguriert | Nicht anwendbar ohne Modellanbieter | Nicht anwendbar ohne Modellanbieter | `_TODO_ (Lizenz-/DPA-Bewertung fuer opencode-ai vom Owner einzutragen)` | Nicht anwendbar ohne Modellanbieter | `_TODO_ (fuer opencode-ai zu pruefen)` | `_TODO_ (vom Owner einzutragen)` | `_TODO_ (vom Owner einzutragen)` |
| Codex CLI | CLI im Container, npm-Paket `@openai/codex` Version `0.130.0` | OpenAI / Azure OpenAI, genaue Betriebsvariante vom Owner einzutragen | `_TODO_ (Endpoint/Region vom Owner einzutragen, EU bevorzugt)` | `_TODO_ (vom Owner einzutragen)` | `_TODO_ (vom Owner einzutragen)` | `_TODO_ (vom Owner einzutragen)` | `_TODO_ (vom Owner einzutragen)` | `_TODO_ (fuer @openai/codex zu pruefen)` | `_TODO_ (vom Owner einzutragen)` | `_TODO_ (vom Owner einzutragen)` |
| Spec Kit | CLI `specify`, Version `v0.8.3` aus `github.com/github/spec-kit.git` | GitHub | GitHub-Quelle beim Image-Build; lokale CLI-Nutzung im Container | Nicht anwendbar fuer lokale CLI-Nutzung; GitHub-Zugriff beim Build vom Owner zu bewerten | Nicht anwendbar fuer lokale CLI-Nutzung; vom Owner zu bestaetigen | `_TODO_ (Lizenz-/DPA-Bewertung vom Owner einzutragen)` | Nicht anwendbar fuer lokale CLI-Nutzung; vom Owner zu bestaetigen | `_TODO_ (fuer github/spec-kit zu pruefen)` | `_TODO_ (vom Owner einzutragen)` | `_TODO_ (vom Owner einzutragen)` |

### AI-SBOM-Lieferantentransparenz (CL_09 Pruefpunkt 15)

Diese Tabelle erfasst die vier zusaetzlichen Transparenzfelder aus CL_09
Pruefpunkt 15. Sie ersetzt keine Anbieterbewertung und erzeugt keine eigene
AI-SBOM fuer fremdbezogene Modelle. Fehlende Angaben sind ein dokumentierter
Lieferketten-Befund und muessen durch Owner, CISO/ISB oder KIB bewertet
werden.

| Eintrag | Model Card / AI-SBOM / Anbieterquelle | Trainings- und Feinabstimmungsverfahren | Herkunft und Sensitivitaet der Trainingsdaten | KI-spezifische Sicherheitseigenschaften |
|---|---|---|---|---|
| OpenCode CLI | Kein KI-Modell; lokale Evidenz in `Dockerfile` und `opencode.jsonc` | Nicht anwendbar fuer CLI | Nicht anwendbar fuer CLI | Lokale Tool-Grenzen durch `opencode.jsonc`: Permission-Regeln, Webfetch-Genehmigung, Secret-Pfad-Blockliste, `share: "disabled"`, `autoupdate: false`, kein vorkonfigurierter Provider |
| Codex CLI | Kein Modell in diesem Repository; lokale Evidenz in `Dockerfile`, `codex/config.toml` und `codex/requirements.toml` | Nicht anwendbar fuer CLI; Modellbetrieb haengt vom konfigurierten OpenAI-/Azure-OpenAI-Backend ab | Nicht anwendbar fuer CLI; Backend-Datenresidenz und Datenverwendung `_TODO_ (Owner einzutragen)` | Lokale Tool-Grenzen durch `codex/config.toml` und `codex/requirements.toml`: Workspace-Sandbox, Deny-Read-Pfade, Environment-Excludes, Websuche deaktiviert |
| Spec Kit | Kein KI-Modell; lokale Evidenz in `Dockerfile`, Quelle `github.com/github/spec-kit.git` Version `v0.8.3` | Nicht anwendbar fuer CLI | Nicht anwendbar fuer CLI | Nicht anwendbar als Modell; Supply-Chain-Bewertung ueber Quellrepository, Version-Pinning und Image-SBOM |

### Hinweise

- Quelle fuer OpenCode-Grenzen: `opencode.jsonc`.
- Quelle fuer Tool-Versionen: `Dockerfile`.
- OpenCode hat in diesem Image keinen vorkonfigurierten Modellanbieter und
  keinen voreingestellten API-Key.
- Re-Evaluation: jedes Quartal, naechste Pruefung 2026-09-03.
- Bezugsrahmen fuer AI-SBOM-Felder: G7-Leitlinie "Software Bill of Materials
  (SBOM) for Artificial Intelligence - Minimum Elements" (2026), siehe
  <https://cyber.gouv.fr/nous-connaitre/publications/publications-internationales/software-bill-of-materials-sbom-for-artificial-intelligence/>.
- Normbezug: CL_09 Pruefpunkt 15 "KI-Lieferkettentransparenz".

## English

This inventory documents the AI and agentic tools intended for this sandbox.
OpenCode is shipped in this image without a model provider. Fields marked
`_TODO_` must be maintained by the owner or responsible office; they are not
inferred from assumptions.

| Tool | Variant | Vendor | Endpoint | EU data residency | ZDR status | DPA date | Training opt-out | OpenSSF Scorecard | Approved until | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| OpenCode | CLI in the container, npm package `opencode-ai` version `1.14.50`; no preconfigured model provider | OpenCode project / npm package; model provider not configured | Not configured | Not applicable without model provider | Not applicable without model provider | `_TODO_ (license/DPA assessment for opencode-ai to be entered by owner)` | Not applicable without model provider | `_TODO_ (check for opencode-ai)` | `_TODO_ (to be entered by owner)` | `_TODO_ (to be entered by owner)` |
| Codex CLI | CLI in the container, npm package `@openai/codex` version `0.130.0` | OpenAI / Azure OpenAI, exact operating variant to be entered by owner | `_TODO_ (endpoint/region to be entered by owner, EU preferred)` | `_TODO_ (to be entered by owner)` | `_TODO_ (to be entered by owner)` | `_TODO_ (to be entered by owner)` | `_TODO_ (to be entered by owner)` | `_TODO_ (check for @openai/codex)` | `_TODO_ (to be entered by owner)` | `_TODO_ (to be entered by owner)` |
| Spec Kit | CLI `specify`, version `v0.8.3` from `github.com/github/spec-kit.git` | GitHub | GitHub source during image build; local CLI use in the container | Not applicable for local CLI use; GitHub access during build to be assessed by owner | Not applicable for local CLI use; to be confirmed by owner | `_TODO_ (license/DPA assessment to be entered by owner)` | Not applicable for local CLI use; to be confirmed by owner | `_TODO_ (check for github/spec-kit)` | `_TODO_ (to be entered by owner)` | `_TODO_ (to be entered by owner)` |

### AI-SBOM Supplier Transparency (CL_09 Item 15)

This table records the four additional transparency fields from CL_09 item 15.
It does not replace supplier assessment and it does not create an own AI-SBOM
for externally sourced models. Missing supplier data is a documented
supply-chain finding and must be assessed by the owner, CISO/ISB, or KIB.

| Entry | Model card / AI-SBOM / supplier source | Training and fine-tuning method | Training-data origin and sensitivity | AI-specific security properties |
|---|---|---|---|---|
| OpenCode CLI | Not an AI model; local evidence in `Dockerfile` and `opencode.jsonc` | Not applicable for CLI | Not applicable for CLI | Local tool boundaries through `opencode.jsonc`: permission rules, webfetch approval, secret-path blocklist, `share: "disabled"`, `autoupdate: false`, no preconfigured provider |
| Codex CLI | No model in this repository; local evidence in `Dockerfile`, `codex/config.toml`, and `codex/requirements.toml` | Not applicable for CLI; model operation depends on the configured OpenAI/Azure OpenAI backend | Not applicable for CLI; backend data residency and data use `_TODO_ (to be entered by owner)` | Local tool boundaries through `codex/config.toml` and `codex/requirements.toml`: workspace sandbox, deny-read paths, environment excludes, web search disabled |
| Spec Kit | Not an AI model; local evidence in `Dockerfile`, source `github.com/github/spec-kit.git` version `v0.8.3` | Not applicable for CLI | Not applicable for CLI | Not applicable as a model; supply-chain assessment through source repository, version pinning, and image SBOM |

### Notes

- Source for OpenCode boundaries: `opencode.jsonc`.
- Source for tool versions: `Dockerfile`.
- OpenCode has no preconfigured model provider and no preset API key in this
  image.
- Re-evaluation: quarterly, next review 2026-09-03.
- Reference frame for AI-SBOM fields: G7 guideline "Software Bill of Materials
  (SBOM) for Artificial Intelligence - Minimum Elements" (2026), see
  <https://cyber.gouv.fr/nous-connaitre/publications/publications-internationales/software-bill-of-materials-sbom-for-artificial-intelligence/>.
- Policy reference: CL_09 item 15 "AI supply-chain transparency".
