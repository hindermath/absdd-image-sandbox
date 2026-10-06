# Lifecycle-Reparatur und Uebergabe / Lifecycle Repair and Handoff

## Auftrag und Ergebnis / Request and Result

DE: Der Owner beauftragte am 2026-10-06 ausdruecklich die Korrektur von
Archiv-/Lifecycle-Bindungen und der aktuellen SandboxBaseline-Uebergabe.
Operation: `9d9fce68-15cc-490c-afe0-16b98eda8a54`. RIG017 ist durch die
kanonische Archivbindung behoben. Die
[technische Uebergabe](sandbox-baseline-handoff-2026-10-06.md) benennt exakte
Quellrevision, Image-ID, lokale SBOM und unveraenderte Abnahmegrenzen.

EN: The owner explicitly requested archive/lifecycle repair and the current
SandboxBaseline handoff. The operation above fixes RIG017 through canonical
archive binding. The technical handoff identifies source revision, image ID,
local SBOM and unchanged acceptance boundaries.

## Identitaeten und Provenienz / Identities and Provenance

- Series ID retained: `65371068-4b1d-4465-9ce7-120e6b15b926`.
- New series receipt: `2e48bfc8-847e-4721-948a-25de2484884d`.
- New manifest SHA-256:
  `66f190a12d3e602681dcc4bb255263a3932631c3c79112fed4f195dc07bc420e`.
- Prior manifest SHA-256 retained in immutable archive:
  `8813d2135a092671ccb373cd9273f44fe8ec3ceabab3eaa35f44e617cf2d15c4`.
- Canonical completed GSDB target:
  `specs/intake-authoring-archive/ec50344b-6a7b-45bf-b67c-a67f24f56c01/9d9fce68-15cc-490c-afe0-16b98eda8a54/Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md`.
- Target SHA-256 remains
  `9b1963a5cc1e4f074e8fc918455f0285a0e1138334451523bd957ff21e72026a`.
- The old root file and its authoring receipt remain byte-identical as
  historical compatibility evidence. Their prompts do not authorize rerunning
  a completed intake; the canonical archive target is never Eligible.
- Prior series manifest/receipt, review request/result and reviewed governance
  report bytes are preserved in the operation archives. Existing historical
  feature-input hashes remain reproducible, not silently refreshed.
- New review ID: `09c4714d-57da-4df5-99fb-a72bf0659847`; explicit supersession
  of the archived prior series review. No new intake identity or scope.

## Lifecycle-Grenze / Lifecycle Boundary

DE: Vier Ziele, eine Root und drei typisierte Kanten bleiben erhalten.
Statusfolge: Completed, Eligible, Blocked, Blocked. Nur der kanonische
Archivpfad und seine Referenzen wurden korrigiert. Die Renderer erzeugen beide
Reihenansichten aus dieser Baseline. Feature 003 bleibt historisch Completed
als begrenzte Studie. Es wurde weder zum laufenden Intake zurueckgesetzt noch
als aktuelle Abnahme interpretiert. Eine Fortschreibung benoetigt separate
Autoritaet und erneute Gate-/Review-Pruefung.

EN: Four targets, one root and three typed edges remain, with states
Completed, Eligible, Blocked, Blocked. Only archive bindings and references
changed; both order views are rendered from that baseline. Feature 003 remains
historically completed as a bounded study, not reset or treated as current
acceptance. Advancement requires separate authority and gate/review checks.

## Validierung und Review / Validation and Review

- Bash and PowerShell requirements configuration: Aligned, exit 0, no missing
  paths; canonical active series targets 3, total targets 4.
- Candidate manifest, receipt and historical authoring receipt validated
  before publishing the prepared write set; a publication error would restore
  the exact saved paths. Initial staging-only validation errors were resolved
  without publishing partial candidates.
- Bash and PowerShell order renderers: Current, writes 0 after rendering.
- Agent-surface parity and workflow concurrency: 4 tests passed.
- Pre-commit: all five hooks passed. Agent secret scan: high=0.
- Independent review confirms the archive repair and technical handoff.
  Full-series outcome: NeedsRemediation, with IR002/IR003 (Medium) and
  IR004 (Low) for existing intake content; no accepted risks. The stale active
  review report is archived and replaced, resolving SBR-001.

## Naechste Aktion / Next Action

DE: Naechster Aenderungsschritt ist ein gesonderter, begrenzter
Inhaltskorrekturauftrag fuer IR002 bis IR004 mit anschliessendem Vollreview.
Read-only `$speckit-intake-series-status` bleibt moeglich. Reihenfortschreibung oder neuer
Abnahmelauf sind nicht Teil dieses Reparaturauftrags. Offene AMD64-,
Lernenden-/A11Y-, menschliche und Supply-Chain-Pruefungen bleiben in der
Uebergabe mit Owner, Follow-up und Trigger sichtbar.

EN: The next change requires a separate bounded content-repair mandate for
IR002 through IR004 followed by full review. Read-only series status remains available.
Advancement or a new acceptance run is outside this repair mandate. Open
AMD64, learner/A11Y, human and supply-chain checks retain owners, follow-up
and triggers in the handoff.
