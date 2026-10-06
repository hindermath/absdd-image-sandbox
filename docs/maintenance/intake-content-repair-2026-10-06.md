# Intake-Inhaltskorrektur / Intake Content Repair

## Auftrag / Authority

DE: Der Owner beauftragte am 2026-10-06 ausdruecklich die Erklaerung und
Korrektur der drei Inhaltsbefunde IR002 bis IR004 sowie ein erneutes
Vollreview. Operation: `8524075f-f913-41da-a68b-a0f5c5aef582`. Ausschliesslich
lokale Intake-Pflege, keine Ausfuehrung, Reihenfortschreibung oder Lieferung.

EN: The owner explicitly requested explanation and correction of IR002
through IR004 and full re-review. The operation above permits local intake
maintenance only, not execution, advancement or delivery.

## Korrekturen / Corrections

| ID | Deutsch | English |
| --- | --- | --- |
| IR002 | Abgeschlossene GSDB ist erfuellte Voraussetzung, kein Blocker. Aktuelles Review und Startautoritaet bleiben getrennt. | Completed GSDB fulfills its prerequisite; current review and execution authority remain separate. |
| IR003 | Kernlisten der Haertung und Abnahme zweisprachig ergaenzt; Voraussetzungen und Fachbegriffe beim ersten Gebrauch erklaert. Abnahme-Ausgangslage als Startvoraussetzung formuliert, nicht als aktuelle Abschlussbehauptung. | Hardening and acceptance core lists translated; prior knowledge and first-use terms explained. Acceptance prerequisites are conditional, not current completion claims. |
| IR004 | IT-System-Elektroniker*innen in deutscher und englischer Zielgruppe ergaenzt, gemaess bestehender Lernendenbasis. | IT systems electronics technician apprentices added in both audience languages, following existing policy. |

## Herkunft und Grenzen / Provenance and Boundaries

DE: Alle drei Intake-Identitaeten bleiben erhalten. Vorige Ziele und Receipts
sind byte-identisch unter `specs/intake-authoring-archive/<intakeId>/<operationId>/`
archiviert; sie sind jeweils die erste Quelle des Nachfolgers. Der vorige
Review-Bericht und AGENTS.md folgen als gebundene Aenderungsquellen.
Manifest-/Receipt- und Review-Bindungen werden gemeinsam erneuert.
Die abgeschlossene GSDB bleibt unveraendert, ebenso die Statusfolge
Completed, Eligible, Blocked, Blocked. Historische Feature-003-Hashes werden
nicht neu berechnet: der Validator liest fuer dessen abgeschlossenen Lauf
die fest zugeordnete vorherige Intake-Kopie mit demselben akzeptierten Hash.
Vorhandene Negativtests pruefen diese zusaetzliche Archivbindung mit.

EN: All three intake identities remain. Prior targets and receipts are
byte-identical archives and the first successor sources; the old review and
AGENTS.md follow as change sources. Manifest, receipt and review bindings
are refreshed together. Completed GSDB and lifecycle statuses remain
unchanged. Feature 003 retains its accepted hashes; for its completed run
the validator checks the fixed prior intake snapshot with the exact accepted
hash. Existing negative tests also cover this added archive binding.

## Review und naechste Aktion / Review and Next Action

DE: Das unabhaengige Vollreview aller vier Ziele durch Agent
`01a11148-aff2-7c33-b756-31dee15cff6c` ergibt Ready; Review-ID
`3d519e73-1ac3-44e5-a250-0b9f87f5c504`. IR002 bis IR004 sind behoben,
keine neuen materiellen Befunde, Risiken oder Fragen. Die neue Bindung ersetzt
den archivierten NeedsRemediation-Review ausdruecklich. Validator-PASS belegt
aktuelle Hashes; das semantische Urteil stammt aus dem separaten Vollreview.
Naechste exakte Aktion ist ausschliesslich read-only
`$speckit-intake-series-status specs/intake-series/sandbox-development-lifecycle/manifest.json`.
Kein Lauf, Commit, Push, Reihenfortschritt oder Plattformumbau startet.

EN: Independent full review of all four targets by the agent above concludes
Ready. IR002-IR004 are resolved; no new material findings, risks or questions.
The new binding explicitly supersedes the archived NeedsRemediation review.
Validator PASS proves current hashes; the semantic verdict comes from separate
full review. The exact next action is only read-only intake-series status.
No run, commit, push, advancement or platform reconfiguration starts.

## Validierung / Validation

- Authoring receipts (all three changed targets), series manifest/receipt,
  requirements configuration and review result validate; configuration Aligned.
- Historical evidence: 18 contract tests Passed, including fail-closed checks
  for missing/tampered archive snapshots and non-completed runs.
- Lychee offline: no link/anchor errors.
- Both Git-aware order renderers in the actual checkout: Current, writes 0.
  The temporary-stage refusal was not reported as acceptance.
- Post-publication hardening, agent-parity and workflow tests: 32 Passed.
- Pre-commit on all 29 prepared files: secret hook Passed, four unrelated
  toolchain hooks skipped because their input files were unchanged.
- Full `uvx pre-commit run --all-files`: all five hooks Passed.
- Strict JSON parsing and byte-equality of published targets against the
  independently reviewed candidate: Passed.
- Agent secret scan: high=0; existing local-settings/prompt-directory
  advisories only. `git diff --check` and `podman-compose config`: exit 0.
- Initial helper invocation failed before publication because positional
  PowerShell argument splatting was unsuitable; corrected to named arguments
  and rerun. No partial active candidate was published.
