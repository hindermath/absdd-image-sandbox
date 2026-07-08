# Öffentlichkeits-Bereitschafts-Evidenz / Public-Readiness Evidence

**Status:** Implementierungs-Evidenz / Implementation evidence for `specs/001-public-readiness`
**Stand / Date:** 2026-07-05

## Deutsch

Dieses Dokument klassifiziert Sicherheits-, Governance-, Freigabe-, Anbieter- und Audit-Evidenz
fuer den Public-Readiness-Lauf. Das Repository wurde nach Validierung am 2026-07-03 auf oeffentliche
Sichtbarkeit umgestellt. Dieses Dokument erteilt keine Freigabe, erzeugt keine SBOM-, VEX- oder
SLSA-Evidenz, konfiguriert keine Anbieter und schliesst keine Entscheidungen ab, die Menschen
vorbehalten sind.

### Evidenz-Klassifizierungsregeln / Evidence Classification Rules

| Klassifizierung / Classification | Bedeutung / Meaning | Pflichtdaten / Required data |
|---|---|---|
| `active-evidence` | Aktuelle Repository-Evidenz fuer eine Aussage. / Current repository evidence for a statement. | Evidenzpfad / Evidence path |
| `context-evidence` | Herkunft oder Hintergrund, der erklaert, warum eine Kontrolle existiert. / Origin or background explaining why a control exists. | Begründung / Rationale |
| `example-evidence` | Illustrierendes Beispiel, keine zwingende Anforderung. / Illustrative example, not a mandatory requirement. | Begründung / Rationale |
| `not-public-release-relevant` | Nuetzlich fuer Audit-Geschichte, kein oeffentlicher Freigabeanspruch. / Useful for audit history, not a public-release claim. | Begründung / Rationale |
| `Open` | Anwendbar, aber noch offen. / Applicable but unresolved. | Owner, Folgeaufgabe, Neu-Bewertungsausloeser |
| `N/A` | Nicht anwendbar auf dieses reine Dokumentations-Feature. / Not applicable to this documentation-only feature. | Begründung / Rationale |
| `_TODO_` | Platzhalter fuer eine menschliche oder zukuenftige Aufgabe. / Placeholder for a human or future task. | Owner, Folgeaufgabe, Neu-Bewertungsausloeser |

### Klassifizierte Evidenz / Classified Evidence

| Evidenzpunkt / Evidence item | Klassifizierung / Classification | Evidenzpfad / Evidence path | Begründung / Rationale | Owner | Folgeaufgabe / Follow-up | Neu-Bewertungsausloeser / Re-evaluation trigger |
|---|---|---|---|---|---|---|
| Sandbox-Zweck und Grenzen / Public sandbox purpose and boundaries | active-evidence | `README.md` | README nennt Ausbildungszweck, Nicht-Produktions-Scope und Public-Readiness-Status. | Maintainer | Bei README-Aenderungen aktuell halten. | Public-Release-Review |
| Optionaler home-baseline-Workflow / Optional home-baseline workflow | active-evidence | `README.md`, `compose.home-baseline.yml` | Als optionaler nutzer-eigener Template-Checkout beschrieben, nicht als Image-Inhalt. | Maintainer | Template-Quelle generisch halten. | Template-Workflow-Aenderung |
| OpenCode-Anbieter-Status / OpenCode provider status | active-evidence | `README.md`, `opencode.env.example`, `opencode.jsonc` | Kein API-Schluessel oder Modell vom Image vorkonfiguriert; lokale Provider-Secrets nicht getrackt. | Owner | Nur lokal bei Bedarf konfigurieren. | Anbieter-Entscheidung |
| Codex-Anbieter-/Modell-Status / Codex provider/model status | `Open` | `codex/config.toml`, `docs/security/ai-tools-inventory.md` | Kein Repository-Anbieter-Standard konfiguriert; lokaler Backend-Status owner-kontrolliert. | Owner | Lokale Anbieter-/Backend-Details nur in genehmigter lokaler Evidenz. | Anbieter-/Modell-Freigabe |
| Formelle Sandbox-Freigabe / Formal sandbox approval | `Open` | `docs/security/sandbox-freigabe.md`, `docs/security/sandbox-freigabe-review.md` | Freigabe steht ausdruecklich aus; kann nicht durch Agenten erteilt werden. | Owner / CISO / ISB / KIB | Freigabe-Review und Unterschriftsfelder abschliessen. | Formelle Freigabe-Entscheidung |
| Zweig-Schutz / Branch protection | active-evidence | `docs/security/branch-protection.md`, `.github/CODEOWNERS`, `.github/pull_request_template.md`, `.github/workflows/homogeneity-check.yml` | Repository ist oeffentlich; GitHub-Ruleset `18493733` schuetzt `main` aktiv mit PR-Review, Code-Owner-Review, erforderlichen Agent-Secret-Scan-Checks, Loeschschutz und dokumentiertem Admin-Bypass. | Owner / Plattform-Admin | Ruleset-Evidenz bei Aenderungen aktuell halten. | GitHub-Ruleset- oder Sichtbarkeitsaenderung |
| Geheimnis-Pruefung / Secret scanning | active-evidence | `docs/security/secret-scanning.md`, `.pre-commit-config.yaml`, `.gitleaks.toml` | Repository-seitige Kontrollen dokumentiert; zentrale Push-Blockade haengt von Plattform ab. | Maintainer / Plattform-Admin | Tool-Versionen und Plattformlimits aktuell halten. | Secret-Scanning-Tool- oder Host-Aenderung |
| Netzwerk-Egress-Entscheidung / Network egress decision | active-evidence | `docs/security/network-decision.md`, `compose.yml` | Freier Egress als dokumentierte Lernumgebungs-Risikoentscheidung, kein versteckter Standard. | Owner | Egress-Allowlist-Machbarkeit neu bewerten. | Netzwerk-/Proxy-Verfuegbarkeitsaenderung |
| Sandbox-Isolation / Sandbox isolation | active-evidence | `docs/security/sandbox-isolation.md`, `compose.yml`, `codex/`, `opencode.jsonc` | Aktuelle Isolationsmechanismen dokumentiert ohne Produktions-Freigabe zu beanspruchen. | Maintainer | Bei Compose-/Dockerfile-Aenderungen ausrichten. | Laufzeit- oder Mount-Aenderung |
| Swift-Mount und Toolchain / Swift project mount and toolchain | active-evidence | `Dockerfile`, `compose.yml`, `.env.example`, `scripts/smoke-test-toolchains.sh`, `README.md` | Swift-Projekte unter `/swift-projects` mountbar; Image installiert Swift `6.3.3-noble` aus signiertem Swift.org-Release. | Maintainer | Version, Mount und Smoke-Test synchron halten. | Swift-Version oder Toolchain-Aenderung |
| Optionaler VS-Code-Zugang / Optional VS Code Dev Containers access | active-evidence | `README.md`, `.devcontainer/devcontainer.json`, `docs/security/sandbox-isolation.md` | VS Code kann vom Host an den laufenden `ade`-Container anhaengen, ohne dauerhaften Browser-IDE-Dienst zu starten. | Maintainer | Bei Dev-Containers- und Compose-Aenderungen ausrichten. | IDE-Zugang oder Laufzeit-Aenderung |
| Image-SBOM-Erzeugung / Image SBOM generation | `Open` | `README.md`, `scripts/build-and-sbom.*`, `sboms/.gitkeep` | Prozess vorhanden; generierte SBOM-JSON-Dateien sind Build-Artefakte, keine stehende Repo-Evidenz. | Maintainer | SBOM nur im Release-/Build-Workflow erzeugen. | Image-Uebergabe oder Release-Build |
| VEX-Status / VEX status | `Open` | `README.md`, `docs/security/public-readiness-evidence.md` | Keine VEX-Evidenz aus diesem Dokumentations-Lauf erzeugt. | Maintainer | VEX-Workflow in spaeterem Haertungs-/Release-Lauf entscheiden. | Schwachstellen- oder Release-Review |
| SLSA-/Provenienz-Status / SLSA/provenance status | `Open` | `README.md`, `docs/security/public-readiness-evidence.md` | Keine Provenienz oder Attestierung aus diesem Lauf erzeugt. | Maintainer | Provenienz-Workflow in spaeterem Release-Lauf entscheiden. | Release-Pipeline-Design |
| AI-SBOM-Anbieter-Transparenz / AI-SBOM supplier transparency | `_TODO_` | `docs/security/ai-tools-inventory.md` | Entwicklungswerkzeug-Eintraege vorhanden; Owner-/Anbieter-Felder bewusst offen. | Owner / KIB | Anbieter-/Modell-Lieferantendaten einzutragen, wenn Nutzung genehmigt. | Anbieter-/Modell-Freigabe |
| Historische Agent-Session-Logs / Historical agent-session logs | not-public-release-relevant | `docs/security/agent-session-log/` | Logs koennen alte Anbieter-, Image-, Hosting- oder Host-Kontext-Referenzen enthalten; Audit-Notizen, keine aktuellen Anleitungen. | Maintainer | Log nur neutralisieren, wenn als aktuelle Anleitung wiederverwendet. | Session-Log-Kuration |
| GSDB-Preflight-Bericht / GSDB preflight report | context-evidence | `docs/security/gsdb-self-assessment.md` | Preflight bereitet spaetere GSDB-Lauf vor; keine formelle Freigabe. | Maintainer | Bei GSDB-Intensivpruefung auffrischen. | GSDB-Spec-Kit-Lauf |
| RL-SE-/Checklisten-Selbstpruefung / RL-SE/checklist self-assessment | `Open` | `Lastenheft_RL-SE-Checklist-Selbstpruefung.md` | Separater Spec-Kit-Lauf; hier bewusst nicht gestartet. | Maintainer | Separat manuell starten, wenn angefordert. | Explizite Benutzeranforderung |
| Container-Haertung / Container hardening | `Open` | `Lastenheft_Secure-Development-Container-Hardening.md`, `Lastenheft_Secure-Development-Hardening.md` | Separate Haertungs-Laeufe; hier bewusst nicht gestartet. | Maintainer | Separat manuell starten, wenn angefordert. | Explizite Benutzeranforderung |

### Kein-Ueberanspruch-Erklaerung / No-Overclaim Statement

**DE:** Dieser Public-Readiness-Lauf beansprucht nicht, dass:

- das Container-Image formell freigegeben wurde;
- eine formelle Sandbox-Freigabe erteilt wurde;
- Anbieter-, Modell-, Rechts-, Datenresidenz- oder Plattform-Entscheidungen abgeschlossen sind;
- SBOM-, VEX-, SLSA- oder AI-SBOM-Evidenz durch diesen Lauf erzeugt wurde;
- externe Register aktualisiert wurden.

## English

This document classifies security, governance, release, provider, and audit evidence for the
Public-Readiness run. The repository was switched to public visibility on 2026-07-03 after
validation. This file does not grant approval, generate SBOM/VEX/SLSA evidence, configure
providers, or close human-only decisions.

### Evidence Classification Rules

| Classification | Meaning | Required data |
|---|---|---|
| `active-evidence` | Current repository evidence for a statement | Evidence path |
| `context-evidence` | Origin or background that explains why a control exists | Rationale |
| `example-evidence` | Illustrative example, not a mandatory public requirement | Rationale |
| `not-public-release-relevant` | Useful for audit history but not a public-release claim | Rationale |
| `Open` | Applicable but unresolved | Owner, follow-up, re-evaluation trigger |
| `N/A` | Not applicable to this documentation-only feature | Rationale |
| `_TODO_` | Placeholder for a human or future run | Owner, follow-up, re-evaluation trigger |

### Classified Evidence

| Evidence item | Classification | Evidence path | Rationale | Owner | Follow-up | Re-evaluation trigger |
|---|---|---|---|---|---|---|
| Public sandbox purpose and boundaries | active-evidence | `README.md` | README now states training purpose, non-production scope, and Public-Readiness status | Maintainer | Keep current during README changes | Public release review |
| Optional `home-baseline` workflow | active-evidence | `README.md`, `compose.home-baseline.yml` | Described as user-owned optional template checkout, not as image content or mandatory private path | Maintainer | Keep template source generic unless a course-specific source is documented separately | Template workflow change |
| OpenCode provider status | active-evidence | `README.md`, `opencode.env.example`, `opencode.jsonc` | No API key or model is preconfigured by the image; the built-in provider picker remains available and local provider secrets are untracked | Owner | Configure locally only if needed | Provider setup decision |
| Codex provider/model status | `Open` | `codex/config.toml`, `docs/security/ai-tools-inventory.md` | No repository provider default is configured; local backend status is owner-controlled | Owner | Enter local provider/backend details only in approved local or operational evidence | Provider/model approval |
| Formal sandbox approval | `Open` | `docs/security/sandbox-freigabe.md`, `docs/security/sandbox-freigabe-review.md` | Approval is explicitly pending and cannot be granted by an agent | Owner / CISO / ISB / KIB | Complete approval review and signature fields | Formal approval decision |
| Branch protection / hosting enforcement | active-evidence | `docs/security/branch-protection.md`, `.github/CODEOWNERS`, `.github/pull_request_template.md`, `.github/workflows/homogeneity-check.yml` | Repository is public and GitHub Ruleset `18493733` actively protects `main` with PR review, Code Owner review, required Agent Secret Scan checks, deletion/non-fast-forward protection, and documented admin bypass | Owner / platform admin | Keep ruleset evidence current when required checks or hosting settings change | GitHub ruleset, workflow, repository visibility, or platform-rule change |
| Secret scanning | active-evidence | `docs/security/secret-scanning.md`, `.pre-commit-config.yaml`, `.gitleaks.toml` | Repository-side controls are documented; central push blocking depends on platform capability | Maintainer / platform admin | Keep tool versions and platform limits current | Secret-scanning tool or host change |
| Network egress decision | active-evidence | `docs/security/network-decision.md`, `compose.yml` | Free egress is a documented learning-environment risk decision, not a hidden default | Owner | Reassess egress allow-list feasibility | Network/proxy availability change |
| Sandbox isolation | active-evidence | `docs/security/sandbox-isolation.md`, `compose.yml`, `codex/`, `opencode.jsonc` | Current isolation mechanisms are documented without claiming production approval | Maintainer | Keep evidence aligned with Compose/Dockerfile changes | Runtime or mount change |
| Swift project mount and toolchain | active-evidence | `Dockerfile`, `compose.yml`, `.env.example`, `scripts/smoke-test-toolchains.sh`, `README.md` | Swift projects are mountable at `/swift-projects`; the image installs Swift `6.3.3-noble` from a signed Swift.org release artifact and validates it in the smoke test | Maintainer | Keep version, mount, and smoke test aligned with Swift updates | Swift version, mount, or toolchain change |
| Optional VS Code Dev Containers access | active-evidence | `README.md`, `.devcontainer/devcontainer.json`, `docs/security/sandbox-isolation.md` | VS Code can attach from the host to the running `ade` container without adding a long-running browser IDE service or publishing an additional IDE port | Maintainer | Keep aligned with Dev Containers and Compose changes | IDE access, runtime, or mount change |
| Image SBOM generation | `Open` | `README.md`, `scripts/build-and-sbom.*`, `sboms/.gitkeep` | The process exists; generated SBOM JSON files are per-image build artifacts and are not standing repository evidence unless a release workflow explicitly requires them | Maintainer | Generate SBOM only in a release/build workflow | Image handover or release build |
| VEX status | `Open` | `README.md`, `docs/security/public-readiness-evidence.md` | No VEX evidence is produced by this documentation run | Maintainer | Decide VEX workflow in a later hardening/release run | Vulnerability or release review |
| SLSA / provenance status | `Open` | `README.md`, `docs/security/public-readiness-evidence.md` | No provenance or attestation is produced by this documentation run | Maintainer | Decide provenance workflow in a later hardening/release run | Release pipeline design |
| AI-SBOM supplier transparency | `_TODO_` | `docs/security/ai-tools-inventory.md` | Development-tool entries exist; owner/provider fields remain intentionally open | Owner / KIB | Fill provider/model supplier data when provider usage is approved | Provider/model approval |
| Historical agent-session logs | not-public-release-relevant | `docs/security/agent-session-log/` | Logs may contain old provider, image, hosting, or host-context references; they are audit notes, not current public setup instructions | Maintainer | Neutralize a log only if it is reused as current guidance | Session-log curation review |
| GSDB preflight report | context-evidence | `docs/security/gsdb-self-assessment.md` | Preflight prepares a later GSDB run and is not a formal approval | Maintainer | Refresh when the GSDB intensive review starts | GSDB Spec-Kit run |
| RL-SE-/Checklist self-assessment | `Open` | `Lastenheft_RL-SE-Checklist-Selbstpruefung.md` | Separate Spec-Kit run; intentionally not executed here | Maintainer | Start separate run manually if requested | Explicit user request |
| Container hardening | `Open` | `Lastenheft_Secure-Development-Container-Hardening.md`, `Lastenheft_Secure-Development-Hardening.md` | Separate hardening runs; intentionally not executed here | Maintainer | Start separate run manually if requested | Explicit user request |

### No-Overclaim Statement

This Public-Readiness implementation does not claim that:

- the container image has been formally released;
- formal sandbox approval has been granted;
- provider, model, legal, data-residency, or platform decisions are complete;
- SBOM, VEX, SLSA, or AI-SBOM evidence has been generated by this run;
- external registers have been updated.
