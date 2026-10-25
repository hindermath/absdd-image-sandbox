# Commit-Gruppen zum Tagesabschluss / Closeout Commit Groups

DE: Expliziter Ownerauftrag vom 25.10.2026: sieben thematische Commits, danach
ein Gesamt-Push und ein gemeinsamer PR mit Merge-Commit/Admin-Bypass erst nach
aktuellen grünen Checks. Einmalige Ausnahme zur Einzel-PR-Konvention; keine
dauerhafte Governance-Abschwächung. Die vollständige Dateizuordnung wird vor
dem ersten Staging erzeugt. Zwischen-Commits sind keine separat freigegebenen
Stände; maßgeblich ist der vollständig validierte letzte PR-Head.

EN: Explicit owner authority: seven thematic commits, one combined push and
one merge-commit PR with admin bypass only after current green checks. This
is a one-time exception, not a permanent policy change. Generate the complete
file assignment before staging. Intermediate commits are not separate approved
releases; the fully validated final PR head is authoritative.

DE: Nur die unten explizit zugeordneten getrackten Änderungen und neuen
Dateien aufnehmen. Lokale Konfiguration, Secrets, Backups, temporäre Exporte,
generierte SBOMs und ignorierte Zustände bleiben ausgeschlossen. Jede Datei
gehört genau einer Gruppe. Keine pauschale Aufnahme des Arbeitsverzeichnisses.

EN: Stage only the explicitly assigned tracked changes and new files below.
Exclude local configuration, secrets, backups, temporary exports, generated
SBOMs and ignored state. Each file belongs to exactly one group; no blanket add.

<!-- closeout-file-assignment:start -->
## 1. build: update native toolchains and maintenance checks

Dateien / Files: 20

- `Dockerfile`
- `docs/maintenance/rev-test-timing-2026-10-25.md`
- `docs/maintenance/toolchain-version-audit-2026-10-25.md`
- `docs/security/ai-tools-inventory.md`
- `docs/security/dependency-update-policy.md`
- `docs/security/toolchain-followups-2026-10-25.md`
- `opencode.jsonc`
- `renovate.json`
- `scripts/build-and-sbom.ps1`
- `scripts/build-and-sbom.sh`
- `scripts/config/required-cli-tools-registry.json`
- `scripts/lib/linux-maintenance-hardening.py`
- `scripts/maintain-agentic-brew-apps.sh`
- `scripts/smoke-test-toolchains.sh`
- `scripts/tests/fixtures/opencode-v1-policy.json`
- `scripts/tests/test_linux_maintenance_hardening.py`
- `scripts/tests/test_opencode_v2_policy.py`
- `scripts/tests/test_specify_container_patch.py`
- `scripts/tests/test_toolchain_version_pins.py`
- `spec-kit/patch-specify-cli.py`

## 2. fix: harden audit shutdown and secret scanning

Dateien / Files: 11

- `.gitleaks.toml`
- `docs/security/audit-shutdown-fail-closed-2026-10-25.md`
- `docs/security/gitleaks-swift-fingerprint-followup-review-2026-10-25.md`
- `docs/security/gitleaks-swift-fingerprint-review-2026-10-25.md`
- `scripts/audit-export.ps1`
- `scripts/audit-export.sh`
- `scripts/compose-down-with-audit.ps1`
- `scripts/compose-down-with-audit.sh`
- `scripts/tests/test_audit_shutdown_fail_closed.py`
- `scripts/tests/test_audit_storage_metadata.py`
- `scripts/tests/test_gitleaks_swift_fingerprint.py`

## 3. docs: expand bilingual sandbox learner guidance

Dateien / Files: 29

- `.github/agents/copilot-instructions.md`
- `.github/copilot-instructions.md`
- `AGENTS.md`
- `CLAUDE.md`
- `docs/betrieb/image-aufbau.md`
- `docs/betrieb/README.md`
- `docs/betrieb/validierung-und-wartung.md`
- `docs/fuer-lernende/agenten-und-spec-kit.md`
- `docs/fuer-lernende/alltag.md`
- `docs/fuer-lernende/barrierefreiheit.md`
- `docs/fuer-lernende/container-grundlagen.md`
- `docs/fuer-lernende/entwickler-kurzpfad.md`
- `docs/fuer-lernende/erste-schritte.md`
- `docs/fuer-lernende/faq.md`
- `docs/fuer-lernende/git-und-hosting.md`
- `docs/fuer-lernende/installation.md`
- `docs/fuer-lernende/lernwege.md`
- `docs/fuer-lernende/README.md`
- `docs/fuer-lernende/sandbox-profil.md`
- `docs/fuer-lernende/toolchains/java.md`
- `docs/fuer-lernende/toolchains/python.md`
- `docs/fuer-lernende/toolchains/README.md`
- `docs/fuer-lernende/troubleshooting.md`
- `docs/maintenance/documentation-alignment-2026-10-25.md`
- `docs/maintenance/documentation-impact-2026-10-25.json`
- `docs/security/sandbox-freigabe.md`
- `GEMINI.md`
- `README.md`
- `scripts/tests/test_learner_documentation_contract.py`

## 4. docs: add learner workshops and presentation decks

Dateien / Files: 73

- `docs/lernwerkstaetten/moderation.md`
- `docs/lernwerkstaetten/README.md`
- `docs/lernwerkstaetten/sysinfo/basis.md`
- `docs/lernwerkstaetten/sysinfo/intakes/00-cli.md`
- `docs/lernwerkstaetten/sysinfo/intakes/01-yaml.md`
- `docs/lernwerkstaetten/sysinfo/intakes/02-sqlite.md`
- `docs/lernwerkstaetten/sysinfo/intakes/03-rest.md`
- `docs/lernwerkstaetten/sysinfo/intakes/04-dokumentation.md`
- `docs/lernwerkstaetten/sysinfo/intakes/05-review.md`
- `docs/lernwerkstaetten/sysinfo/order.md`
- `docs/lernwerkstaetten/sysinfo/README.md`
- `docs/lernwerkstaetten/sysinfo/sources.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-authoring-operations/b8b937fa-5939-47d8-9517-bed9995ba0ff/operation.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-authoring-operations/b8b937fa-5939-47d8-9517-bed9995ba0ff/proposal.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-authoring-receipts/00-cli.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-authoring-receipts/01-yaml.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-authoring-receipts/02-sqlite.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-authoring-receipts/03-rest.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-authoring-receipts/04-dokumentation.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-authoring-receipts/05-review.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-review-requests/learning.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-series/learning/manifest.json`
- `docs/lernwerkstaetten/sysinfo/specs/intake-series/learning/receipt.json`
- `docs/lernwerkstaetten/web-mvc/basis.md`
- `docs/lernwerkstaetten/web-mvc/decision.md`
- `docs/lernwerkstaetten/web-mvc/intakes/00-formular.md`
- `docs/lernwerkstaetten/web-mvc/intakes/01-crud.md`
- `docs/lernwerkstaetten/web-mvc/intakes/02-fehler-und-bedienung.md`
- `docs/lernwerkstaetten/web-mvc/intakes/03-abschluss.md`
- `docs/lernwerkstaetten/web-mvc/order.md`
- `docs/lernwerkstaetten/web-mvc/README.md`
- `docs/lernwerkstaetten/web-mvc/sources.json`
- `docs/lernwerkstaetten/web-mvc/specs/intake-authoring-operations/c9ad9291-9278-4805-9eec-3bac40b28f6e/operation.json`
- `docs/lernwerkstaetten/web-mvc/specs/intake-authoring-operations/c9ad9291-9278-4805-9eec-3bac40b28f6e/proposal.json`
- `docs/lernwerkstaetten/web-mvc/specs/intake-authoring-receipts/00-formular.json`
- `docs/lernwerkstaetten/web-mvc/specs/intake-authoring-receipts/01-crud.json`
- `docs/lernwerkstaetten/web-mvc/specs/intake-authoring-receipts/02-fehler-und-bedienung.json`
- `docs/lernwerkstaetten/web-mvc/specs/intake-authoring-receipts/03-abschluss.json`
- `docs/lernwerkstaetten/web-mvc/specs/intake-review-requests/learning.json`
- `docs/lernwerkstaetten/web-mvc/specs/intake-series/learning/manifest.json`
- `docs/lernwerkstaetten/web-mvc/specs/intake-series/learning/receipt.json`
- `docs/lernwerkstaetten/web-rest/basis.md`
- `docs/lernwerkstaetten/web-rest/decision.md`
- `docs/lernwerkstaetten/web-rest/intakes/00-vertrag.md`
- `docs/lernwerkstaetten/web-rest/intakes/01-sqlite.md`
- `docs/lernwerkstaetten/web-rest/intakes/02-mvc-client.md`
- `docs/lernwerkstaetten/web-rest/intakes/03-abschluss.md`
- `docs/lernwerkstaetten/web-rest/order.md`
- `docs/lernwerkstaetten/web-rest/README.md`
- `docs/lernwerkstaetten/web-rest/sources.json`
- `docs/lernwerkstaetten/web-rest/specs/intake-authoring-operations/eca8c4db-68e0-415d-9305-2b47156af151/operation.json`
- `docs/lernwerkstaetten/web-rest/specs/intake-authoring-operations/eca8c4db-68e0-415d-9305-2b47156af151/proposal.json`
- `docs/lernwerkstaetten/web-rest/specs/intake-authoring-receipts/00-vertrag.json`
- `docs/lernwerkstaetten/web-rest/specs/intake-authoring-receipts/01-sqlite.json`
- `docs/lernwerkstaetten/web-rest/specs/intake-authoring-receipts/02-mvc-client.json`
- `docs/lernwerkstaetten/web-rest/specs/intake-authoring-receipts/03-abschluss.json`
- `docs/lernwerkstaetten/web-rest/specs/intake-review-requests/learning.json`
- `docs/lernwerkstaetten/web-rest/specs/intake-series/learning/manifest.json`
- `docs/lernwerkstaetten/web-rest/specs/intake-series/learning/receipt.json`
- `docs/praesentationen/exports/workshop-spec-kit.de.key`
- `docs/praesentationen/exports/workshop-spec-kit.de.pptx`
- `docs/praesentationen/exports/workshop-spec-kit.en.key`
- `docs/praesentationen/exports/workshop-spec-kit.en.pptx`
- `docs/praesentationen/README.md`
- `docs/praesentationen/werkstatt-sysinfo.de.md`
- `docs/praesentationen/werkstatt-sysinfo.en.md`
- `docs/praesentationen/werkstatt-web.de.md`
- `docs/praesentationen/werkstatt-web.en.md`
- `docs/praesentationen/workshop-spec-kit.de.md`
- `docs/praesentationen/workshop-spec-kit.en.md`
- `scripts/export-workshop-presentations.mjs`
- `scripts/tests/test_learning_workshops.py`
- `scripts/tests/test_workshop_presentations.py`

## 5. chore: prepare optional sandbox template profile

Dateien / Files: 9

- `.github/workflows/documentation-and-sandbox.yml`
- `.github/workflows/gsdb-pilot-contracts.yml`
- `.github/workflows/project-statistics-pilot-native-proof.yml`
- `.pre-commit-config.yaml`
- `docs/betrieb/template-erstuebernahme.md`
- `docs/fuer-lernende/template-profil.md`
- `docs/licensing.md`
- `LICENSE`
- `scripts/tests/test_template_profile.py`

## 6. docs: refresh intake provenance and independent reviews

Dateien / Files: 169

- `docs/maintenance/closeout-eof-alignment-2026-10-25.md`
- `docs/maintenance/closeout-review-remediation-2026-10-25.md`
- `docs/maintenance/closeout-rights-alignment-2026-10-25.md`
- `docs/maintenance/intake-sources-alignment-2026-10-25.md`
- `docs/maintenance/maven-fallback-intake-alignment-2026-10-25.md`
- `docs/maintenance/template-profile-alignment-2026-10-25.md`
- `intakes/learner-fork-self-build-sandbox.md`
- `Lastenheft_Abarbeitungsreihenfolge.md`
- `Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md`
- `Lastenheft_Secure-Development-Container-Hardening.md`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/3caff22f-59d5-4142-b15b-955ee96a3037/receipt.json`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/3caff22f-59d5-4142-b15b-955ee96a3037/target.txt`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/50131ced-9c70-43d3-9fa1-51d1d37e60cd/receipt.json`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/50131ced-9c70-43d3-9fa1-51d1d37e60cd/target.txt`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/561af2f2-bbfe-45f5-a9ca-e975dd70c497/receipt.json`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/561af2f2-bbfe-45f5-a9ca-e975dd70c497/target.txt`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/receipt.json`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/target.txt`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/receipt.json`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/target.txt`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/8e843682-0ece-4a9f-a996-7068453e30f7/receipt.json`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/8e843682-0ece-4a9f-a996-7068453e30f7/target.txt`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/989f4710-2626-4256-ae70-e476244b5d1b/receipt.json`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/989f4710-2626-4256-ae70-e476244b5d1b/target.txt`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/receipt.json`
- `specs/intake-authoring-archive/51d24064-dfa6-4375-9bcd-58cccc545167/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/target.txt`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/3caff22f-59d5-4142-b15b-955ee96a3037/receipt.json`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/3caff22f-59d5-4142-b15b-955ee96a3037/target.txt`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/50131ced-9c70-43d3-9fa1-51d1d37e60cd/receipt.json`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/50131ced-9c70-43d3-9fa1-51d1d37e60cd/target.txt`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/561af2f2-bbfe-45f5-a9ca-e975dd70c497/receipt.json`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/561af2f2-bbfe-45f5-a9ca-e975dd70c497/target.txt`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/receipt.json`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/target.txt`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/receipt.json`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/target.txt`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/8e843682-0ece-4a9f-a996-7068453e30f7/receipt.json`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/8e843682-0ece-4a9f-a996-7068453e30f7/target.txt`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/989f4710-2626-4256-ae70-e476244b5d1b/receipt.json`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/989f4710-2626-4256-ae70-e476244b5d1b/target.txt`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/receipt.json`
- `specs/intake-authoring-archive/5926e53e-39b7-475f-8a6b-e2ec08b0a803/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/target.txt`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/3caff22f-59d5-4142-b15b-955ee96a3037/receipt.json`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/3caff22f-59d5-4142-b15b-955ee96a3037/target.txt`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/50131ced-9c70-43d3-9fa1-51d1d37e60cd/receipt.json`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/50131ced-9c70-43d3-9fa1-51d1d37e60cd/target.txt`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/561af2f2-bbfe-45f5-a9ca-e975dd70c497/receipt.json`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/561af2f2-bbfe-45f5-a9ca-e975dd70c497/target.txt`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/receipt.json`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/target.txt`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/receipt.json`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/target.txt`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/8e843682-0ece-4a9f-a996-7068453e30f7/receipt.json`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/8e843682-0ece-4a9f-a996-7068453e30f7/target.txt`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/989f4710-2626-4256-ae70-e476244b5d1b/receipt.json`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/989f4710-2626-4256-ae70-e476244b5d1b/target.txt`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/receipt.json`
- `specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/target.txt`
- `specs/intake-authoring-operations/3caff22f-59d5-4142-b15b-955ee96a3037/operation.json`
- `specs/intake-authoring-operations/3caff22f-59d5-4142-b15b-955ee96a3037/source-snapshots/Dockerfile.txt`
- `specs/intake-authoring-operations/3caff22f-59d5-4142-b15b-955ee96a3037/source-snapshots/docs/maintenance/documentation-impact-2026-10-25.json.txt`
- `specs/intake-authoring-operations/3caff22f-59d5-4142-b15b-955ee96a3037/source-snapshots/scripts/tests/test_toolchain_version_pins.py.txt`
- `specs/intake-authoring-operations/50131ced-9c70-43d3-9fa1-51d1d37e60cd/operation.json`
- `specs/intake-authoring-operations/50131ced-9c70-43d3-9fa1-51d1d37e60cd/source-snapshots/.github/agents/copilot-instructions.md.txt`
- `specs/intake-authoring-operations/50131ced-9c70-43d3-9fa1-51d1d37e60cd/source-snapshots/.github/copilot-instructions.md.txt`
- `specs/intake-authoring-operations/50131ced-9c70-43d3-9fa1-51d1d37e60cd/source-snapshots/AGENTS.md.txt`
- `specs/intake-authoring-operations/50131ced-9c70-43d3-9fa1-51d1d37e60cd/source-snapshots/CLAUDE.md.txt`
- `specs/intake-authoring-operations/50131ced-9c70-43d3-9fa1-51d1d37e60cd/source-snapshots/docs/fuer-lernende/lernwege.md.txt`
- `specs/intake-authoring-operations/50131ced-9c70-43d3-9fa1-51d1d37e60cd/source-snapshots/GEMINI.md.txt`
- `specs/intake-authoring-operations/50131ced-9c70-43d3-9fa1-51d1d37e60cd/source-snapshots/README.md.txt`
- `specs/intake-authoring-operations/561af2f2-bbfe-45f5-a9ca-e975dd70c497/operation.json`
- `specs/intake-authoring-operations/561af2f2-bbfe-45f5-a9ca-e975dd70c497/source-snapshots/docs/fuer-lernende/sandbox-profil.md.txt`
- `specs/intake-authoring-operations/561af2f2-bbfe-45f5-a9ca-e975dd70c497/source-snapshots/docs/licensing.md.txt`
- `specs/intake-authoring-operations/561af2f2-bbfe-45f5-a9ca-e975dd70c497/source-snapshots/scripts/tests/test_learner_documentation_contract.py.txt`
- `specs/intake-authoring-operations/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/agents-before-final-stop-examples.txt`
- `specs/intake-authoring-operations/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/agents-before-stop-guidance.txt`
- `specs/intake-authoring-operations/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/operation.json`
- `specs/intake-authoring-operations/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/proposal-before-remediation.txt`
- `specs/intake-authoring-operations/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/source-alignment-before-remediation.txt`
- `specs/intake-authoring-operations/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/operation.json`
- `specs/intake-authoring-operations/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/source-snapshots/docs/licensing.md.txt`
- `specs/intake-authoring-operations/8e843682-0ece-4a9f-a996-7068453e30f7/operation.json`
- `specs/intake-authoring-operations/989f4710-2626-4256-ae70-e476244b5d1b/operation.json`
- `specs/intake-authoring-operations/989f4710-2626-4256-ae70-e476244b5d1b/source-snapshots/docs/licensing.md.txt`
- `specs/intake-authoring-operations/989f4710-2626-4256-ae70-e476244b5d1b/source-snapshots/workshop-spec-kit.de.md.gz`
- `specs/intake-authoring-operations/989f4710-2626-4256-ae70-e476244b5d1b/source-snapshots/workshop-spec-kit.en.md.gz`
- `specs/intake-authoring-operations/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/operation.json`
- `specs/intake-authoring-operations/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/source-snapshots/.pre-commit-config.yaml.txt`
- `specs/intake-authoring-operations/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/source-snapshots/docs/betrieb/README.md.txt`
- `specs/intake-authoring-operations/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/source-snapshots/docs/fuer-lernende/sandbox-profil.md.txt`
- `specs/intake-authoring-operations/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/source-snapshots/docs/maintenance/toolchain-version-audit-2026-10-25.md.txt`
- `specs/intake-authoring-operations/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/source-snapshots/docs/security/toolchain-followups-2026-10-25.md.txt`
- `specs/intake-authoring-operations/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/source-snapshots/README.md.txt`
- `specs/intake-authoring-operations/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/source-snapshots/scripts/config/required-cli-tools-registry.json.txt`
- `specs/intake-authoring-operations/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/source-snapshots/scripts/tests/test_toolchain_version_pins.py.txt`
- `specs/intake-authoring-receipts/learner-fork-self-build-sandbox.json`
- `specs/intake-authoring-receipts/sandbox-secure-development-selbstpruefung.json`
- `specs/intake-authoring-receipts/secure-development-container-hardening.json`
- `specs/intake-review-archive/0298d3b3-7ff1-42d8-a5f7-349d01139cf4/3caff22f-59d5-4142-b15b-955ee96a3037/independent.txt`
- `specs/intake-review-archive/0298d3b3-7ff1-42d8-a5f7-349d01139cf4/3caff22f-59d5-4142-b15b-955ee96a3037/report.txt`
- `specs/intake-review-archive/0298d3b3-7ff1-42d8-a5f7-349d01139cf4/3caff22f-59d5-4142-b15b-955ee96a3037/request.json`
- `specs/intake-review-archive/0298d3b3-7ff1-42d8-a5f7-349d01139cf4/3caff22f-59d5-4142-b15b-955ee96a3037/result.json`
- `specs/intake-review-archive/0aed98b6-12c4-448d-871b-a32ad142e3f9/989f4710-2626-4256-ae70-e476244b5d1b/independent.txt`
- `specs/intake-review-archive/0aed98b6-12c4-448d-871b-a32ad142e3f9/989f4710-2626-4256-ae70-e476244b5d1b/report.txt`
- `specs/intake-review-archive/0aed98b6-12c4-448d-871b-a32ad142e3f9/989f4710-2626-4256-ae70-e476244b5d1b/request.json`
- `specs/intake-review-archive/0aed98b6-12c4-448d-871b-a32ad142e3f9/989f4710-2626-4256-ae70-e476244b5d1b/result.json`
- `specs/intake-review-archive/4398a97e-6773-4b3f-b9d5-a8fbf52005f5/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/independent.txt`
- `specs/intake-review-archive/4398a97e-6773-4b3f-b9d5-a8fbf52005f5/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/report.txt`
- `specs/intake-review-archive/4398a97e-6773-4b3f-b9d5-a8fbf52005f5/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/request.json`
- `specs/intake-review-archive/4398a97e-6773-4b3f-b9d5-a8fbf52005f5/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/result.json`
- `specs/intake-review-archive/5fa23447-e96c-403c-b7da-79c506a11586/561af2f2-bbfe-45f5-a9ca-e975dd70c497/independent.txt`
- `specs/intake-review-archive/5fa23447-e96c-403c-b7da-79c506a11586/561af2f2-bbfe-45f5-a9ca-e975dd70c497/report.txt`
- `specs/intake-review-archive/5fa23447-e96c-403c-b7da-79c506a11586/561af2f2-bbfe-45f5-a9ca-e975dd70c497/request.json`
- `specs/intake-review-archive/5fa23447-e96c-403c-b7da-79c506a11586/561af2f2-bbfe-45f5-a9ca-e975dd70c497/result.json`
- `specs/intake-review-archive/867d4a2e-f31e-4d70-a295-693c36c7a564/8e843682-0ece-4a9f-a996-7068453e30f7/report.txt`
- `specs/intake-review-archive/867d4a2e-f31e-4d70-a295-693c36c7a564/8e843682-0ece-4a9f-a996-7068453e30f7/request.json`
- `specs/intake-review-archive/867d4a2e-f31e-4d70-a295-693c36c7a564/8e843682-0ece-4a9f-a996-7068453e30f7/result.json`
- `specs/intake-review-archive/906fd637-ee39-4784-bd13-6d7f194249de/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/report.txt`
- `specs/intake-review-archive/906fd637-ee39-4784-bd13-6d7f194249de/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/request.json`
- `specs/intake-review-archive/906fd637-ee39-4784-bd13-6d7f194249de/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/result.json`
- `specs/intake-review-archive/c22a09e1-a781-4f5f-b691-a8d8839298b8/50131ced-9c70-43d3-9fa1-51d1d37e60cd/independent.txt`
- `specs/intake-review-archive/c22a09e1-a781-4f5f-b691-a8d8839298b8/50131ced-9c70-43d3-9fa1-51d1d37e60cd/report.txt`
- `specs/intake-review-archive/c22a09e1-a781-4f5f-b691-a8d8839298b8/50131ced-9c70-43d3-9fa1-51d1d37e60cd/request.json`
- `specs/intake-review-archive/c22a09e1-a781-4f5f-b691-a8d8839298b8/50131ced-9c70-43d3-9fa1-51d1d37e60cd/result.json`
- `specs/intake-review-archive/fdf7797f-aaf1-460a-a760-aa8a285bcd5c/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/independent.txt`
- `specs/intake-review-archive/fdf7797f-aaf1-460a-a760-aa8a285bcd5c/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/report.txt`
- `specs/intake-review-archive/fdf7797f-aaf1-460a-a760-aa8a285bcd5c/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/request.json`
- `specs/intake-review-archive/fdf7797f-aaf1-460a-a760-aa8a285bcd5c/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/result.json`
- `specs/intake-review-reports/sandbox-development-lifecycle-independent.txt`
- `specs/intake-review-reports/sandbox-development-lifecycle.md`
- `specs/intake-review-requests/sandbox-development-lifecycle.json`
- `specs/intake-review-results/sandbox-development-lifecycle.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/3caff22f-59d5-4142-b15b-955ee96a3037/manifest.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/3caff22f-59d5-4142-b15b-955ee96a3037/order.md`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/3caff22f-59d5-4142-b15b-955ee96a3037/receipt.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/3caff22f-59d5-4142-b15b-955ee96a3037/requirements-order.md`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/50131ced-9c70-43d3-9fa1-51d1d37e60cd/manifest.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/50131ced-9c70-43d3-9fa1-51d1d37e60cd/order.md`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/50131ced-9c70-43d3-9fa1-51d1d37e60cd/receipt.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/50131ced-9c70-43d3-9fa1-51d1d37e60cd/requirements-order.md`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/561af2f2-bbfe-45f5-a9ca-e975dd70c497/manifest.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/561af2f2-bbfe-45f5-a9ca-e975dd70c497/order.md`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/561af2f2-bbfe-45f5-a9ca-e975dd70c497/receipt.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/561af2f2-bbfe-45f5-a9ca-e975dd70c497/requirements-order.md`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/manifest.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c/receipt.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/manifest.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/order.md`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/receipt.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/7ed5b22f-e402-4e7b-aca0-1d68259a6eac/requirements-order.md`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/8e843682-0ece-4a9f-a996-7068453e30f7/manifest.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/8e843682-0ece-4a9f-a996-7068453e30f7/receipt.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/989f4710-2626-4256-ae70-e476244b5d1b/manifest.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/989f4710-2626-4256-ae70-e476244b5d1b/order.md`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/989f4710-2626-4256-ae70-e476244b5d1b/receipt.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/989f4710-2626-4256-ae70-e476244b5d1b/requirements-order.md`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/manifest.json`
- `specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/ac2d3c31-d99d-40e1-8782-0b9cc8282b22/receipt.json`
- `specs/intake-series-operations/3caff22f-59d5-4142-b15b-955ee96a3037.json`
- `specs/intake-series-operations/50131ced-9c70-43d3-9fa1-51d1d37e60cd.json`
- `specs/intake-series-operations/561af2f2-bbfe-45f5-a9ca-e975dd70c497.json`
- `specs/intake-series-operations/64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c.json`
- `specs/intake-series-operations/7ed5b22f-e402-4e7b-aca0-1d68259a6eac.json`
- `specs/intake-series-operations/8e843682-0ece-4a9f-a996-7068453e30f7.json`
- `specs/intake-series-operations/989f4710-2626-4256-ae70-e476244b5d1b.json`
- `specs/intake-series-operations/ac2d3c31-d99d-40e1-8782-0b9cc8282b22.json`
- `specs/intake-series/sandbox-development-lifecycle/manifest.json`
- `specs/intake-series/sandbox-development-lifecycle/order.md`
- `specs/intake-series/sandbox-development-lifecycle/receipt.json`

## 7. docs: record sandbox validation and operational evidence

Dateien / Files: 17

- `docs/maintenance/closeout-commit-groups-2026-10-25.md`
- `docs/maintenance/sandbox-current-state-2026-10-25.md`
- `docs/security/agent-session-log/2026-10-25-0034.md`
- `docs/security/agent-session-log/2026-10-25-0055.md`
- `docs/security/agent-session-log/2026-10-25-0919.md`
- `docs/security/agent-session-log/2026-10-25-1047.md`
- `docs/security/agent-session-log/2026-10-25-1211.md`
- `docs/security/agent-session-log/2026-10-25-1303.md`
- `docs/security/agent-session-log/2026-10-25-1414.md`
- `docs/security/agent-session-log/2026-10-25-1428.md`
- `docs/security/agent-session-log/2026-10-25-1526.md`
- `docs/security/agent-session-log/2026-10-25-1626.md`
- `docs/security/agent-session-log/2026-10-25-1714.md`
- `docs/security/agent-session-log/2026-10-25-1759.md`
- `docs/security/agent-session-log/2026-10-25-1829.md`
- `docs/security/agent-session-log/2026-10-25-1917.md`
- `docs/security/agent-session-log/2026-10-25-1934.md`

<!-- closeout-file-assignment:end -->
