# PR 117: Lieferung und Aktivierung / Delivery and activation

Owner-Auftrag: MergeAndSync mit Admin-Bypass und Austausch des Containers.
Owner requested merge/sync with admin bypass and container replacement.

- PR 117 merged at reviewed head e2e1dc8; 19 checks passed, two skipped,
  no review threads. Merge: f2e417b7d326ad2c0d7ba151926cb05535bd67b4.
- Local main/origin divergence: 0/0. Existing untracked logs preserved.
- P0-2/P2-3 maintenance completed technically; formal P1-4 role approval
  and live provider/model access are not inferred.
- Old writable container layer saved as local image
  localhost/absdd-image-sandbox_ade:rollback-before-routing-v026-20261105
  (725ddae75b3db1667575b170ead41584311cc22343463af02ad0b849600bf066).
- Old image lacked audit-retention. Installed the merged audit helper and
  exporter in that container before repeating the standard verified stop.
- Current audit export verified in audit-logs/2026-11-05.jsonl. Existing
  30-day retention removed 11 older daily files. Volumes were not deleted.
- Replacement container: 0d4ff0e05e75a6043bbd08fced28caf8232268f70a655cd208593036ea71842c.
- Active image: dc66ce0a897b575dcaca5d80a4f253a88458e5767adef0e4a6b0c04543d40847.
- All 20 original mounts, including six named volumes, preserved.
- Embedded Level 0: 9107cff07a73892076c18c6a28a4e396a250f519;
  Model Routing 0.2.6, Autonomous Run 0.4.10.
- Explicit runtime preview/apply/check: PASS; 48 routing installation
  assertions: PASS; all five harness CLI version checks: PASS.
- No new live inference performed. Next action: use the activated sandbox.

Lokaler Betriebsnachweis; kein weiterer Commit allein fuer Closeout-Evidence.
Local operational receipt; no additional commit solely for closeout evidence.
