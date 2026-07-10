# KI-Werkzeug-Inventar / AI Tool Inventory

**Stand / Date:** 2026-07-10

## Zweck und Grenze / Purpose and Boundary

**DE:** Dieses Inventar dokumentiert die im Image installierten agentischen
Entwicklungswerkzeuge. Das Image enthaelt keine KI-Modelle, keine Provider-
Freigabe und keine vorgegebenen Konten. Anmeldung, Lizenz, Datenresidenz,
Aufbewahrung und Anbieterfreigabe bleiben eine Entscheidung der verantwortlichen
Person beziehungsweise Organisation.

**EN:** This inventory documents the agentic development tools installed in the
image. The image contains no AI models, provider approval, or predefined
accounts. Sign-in, licensing, data residency, retention, and provider approval
remain decisions of the responsible person or organization.

## Installierte Werkzeuge / Installed Tools

| Werkzeug / Tool | Paket und Version / Package and Version | Kommando / Command | Persistenter Zustand / Persistent State |
|---|---|---|---|
| OpenCode | `opencode-ai@1.14.50` | `opencode` | `/home/adedev/.local/share/opencode` (`opencode_data`) |
| Codex CLI | `@openai/codex@0.144.1` | `codex` | `/home/adedev/.codex` (`codex_data`, `CODEX_HOME`) |
| Claude Code | `@anthropic-ai/claude-code@2.1.206` | `claude` | `/home/adedev/.claude` (`claude_data`, `CLAUDE_CONFIG_DIR`) |
| Gemini CLI | `@google/gemini-cli@0.50.0` | `gemini` | `/home/adedev/.gemini-home/.gemini` (`gemini_data`, `GEMINI_CLI_HOME=/home/adedev/.gemini-home`) |
| GitHub Copilot CLI | `@github/copilot@1.0.70` | `copilot` | `/home/adedev/.copilot` (`copilot_data`, `COPILOT_HOME`) |
| GitHub Spec Kit | `specify-cli` aus `github/spec-kit@v0.8.3` | `specify` | lokale Projektartefakte, kein Agentenkonto |
| Syft | `anchore/syft@1.46.0` | `syft` | kein persistentes Agentenkonto |

OpenCode bleibt ein zusaetzliches Werkzeug. Die vier Required-Agenten dieser
Lernumgebung sind Codex, Claude Code, Gemini CLI und GitHub Copilot CLI.

## Anmeldung und Netzwerk / Sign-In and Network

| Werkzeug / Tool | Anmeldung / Sign-In | Netzwerkziel auf Dokumentationsebene / Documented Network Category |
|---|---|---|
| OpenCode | erst nach lokaler Providerwahl | gewaehlter Modellanbieter; kein Provider im Repository vorkonfiguriert |
| Codex CLI | interaktiver, kontobasierter CLI-Login oder freigegebene lokale Konfiguration | OpenAI-/kontobezogene Dienste gemaess lokal gewaehltem Betriebsmodell |
| Claude Code | interaktiver Claude-/Anthropic-Login | Anthropic-Dienste gemaess Konto und Vertrag |
| Gemini CLI | Google-Login oder freigegebene API-/Cloud-Konfiguration | Google-Gemini-/Google-Cloud-Dienste gemaess Anmeldeweg |
| GitHub Copilot CLI | `copilot login` beziehungsweise freigegebene GitHub-Authentifizierung | GitHub- und GitHub-Copilot-Dienste |

**DE:** Die Tabelle ist keine Egress-Allowlist. Konkrete Domains, Regionen und
Aufbewahrungsregeln muessen vor realer Nutzung gegen die aktuelle offizielle
Anbieterdokumentation und die organisatorische Freigabe geprueft werden.

**EN:** The table is not an egress allow-list. Concrete domains, regions, and
retention rules must be checked against current official provider documentation
and organizational approval before real use.

## Versions- und Update-Regel / Version and Update Rule

- Alle npm-Pakete sind ueber Dockerfile-ARGs fest gepinnt.
- Renovate gruppiert die Agenten-ARGs und erstellt nur pruefbare
  Aktualisierungsvorschlaege.
- Claude Code erhaelt `DISABLE_AUTOUPDATER=1`; andere Agenten werden nicht durch
  einen unkontrollierten Image-Lauf aktualisiert.
- Jede Versionsaenderung erfordert Image-Build, vier Agenten-Versionschecks,
  Toolchain-Smoke-Test, Secret-Scan und aktualisierte SBOM.

## Audit-Metadaten / Audit Metadata

`audit-export` schreibt nur:

- Werkzeugname und Versionszeile;
- freigegebenes Zustandsverzeichnis;
- Dateiname beziehungsweise Sitzungs-ID, Zeitstempel und Dateityp aus eng
  erlaubten Sitzungsverzeichnissen;
- Projektpfad, lokaler Actor und Exportzeitpunkt.

Der Export liest oder kopiert keine Prompt-, Antwort-, Token- oder
Credential-Inhalte. Derzeit sind Sitzungsmetadaten nur fuer folgende stabile
Pfade erlaubt:

- OpenCode: `storage/session_diff/ses_*`;
- Codex: `.codex/sessions/**`;
- Claude Code: `.claude/projects/**/*.jsonl`.

Fuer Gemini CLI und GitHub Copilot CLI werden Versions- und Zustandsmetadaten
exportiert, aber keine Sitzungsdateien. Ihre Sitzungsablage bleibt `Open`, bis
ein stabil dokumentiertes Format eine enge Allowlist erlaubt. Breites Kopieren
der jeweiligen Home-Verzeichnisse ist untersagt.

*The audit export records tool versions and narrowly allow-listed file metadata,
never prompt, response, token, or credential content. Gemini and Copilot session
collection remains open until a stable documented layout permits a narrow
allow-list.*

## Datenschutz- und Freigabefelder / Privacy and Approval Fields

| Feld / Field | Status |
|---|---|
| Formelle Werkzeug-/Providerfreigabe | `_TODO_` durch Owner/KIB/CISO/ISB; nicht agentisch abschliessbar |
| EU-Datenresidenz und Region | `_TODO_` je Anbieter, Konto und Vertrag |
| Zero-Data-Retention / Aufbewahrung | `_TODO_` je Anbieter und Vertragsmodell |
| DPA und Trainings-Opt-out | `_TODO_` je Anbieter und Vertrag |
| OpenSSF-/Supply-Chain-Bewertung | `Open`; npm-Pinning, Renovate, Build und SBOM liefern technische Basisevidenz |

Ein CLI-Eintrag ist keine AI-SBOM fuer das dahinter verwendete Modell. Bei
freigegebener Provider-/Modellnutzung sind Model Card, Lieferanteninformationen
und die AI-SBOM-Anwendbarkeit separat zu bewerten.
