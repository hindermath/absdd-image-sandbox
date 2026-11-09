# PR #118: gruene CI und Container-Austausch / Green CI and replacement

DE: Ausdruecklicher Auftrag: CI und Reviews erneut pruefen, Fehler beheben falls
vorhanden; bei fehlerfreiem Ergebnis Container austauschen, kein Merge.
Finaler PR-HEAD: 7d24ca6bf9167aee44dc5877dc72a5ef86b699f6.
Alle 18 ausgefuehrten Checks erfolgreich; zwei bedingte Pin-Publikationsjobs
uebersprungen. Einschliesslich nativem AMD64-Build/Smoke und GSDB auf allen
drei Plattformen. Keine Reviews, PR-Kommentare, Inline-Threads oder aktuellen
Commit-Kommentare vorhanden. REVIEW_REQUIRED bleibt menschlich offen.
Keine Quellkorrektur erforderlich; PR bleibt OPEN, kein Merge oder Release.

EN: Explicit authority: recheck CI/reviews, fix errors if found, replace the
container after a clean result; no merge. All 18 executed checks passed at the
exact head above; two conditional pin-publication jobs were skipped. No review,
PR comment, inline thread or current commit comment was found. Human code-owner
review remains required. No source correction was needed; PR remains OPEN.

## Aktivierung / Activation

- Rollback before replacement: localhost/absdd-image-sandbox_ade:rollback-before-pr118-green-20261106
  (04ed13980dbcfb9d19c17977a65488966610ec1f3ac456c2fec71e926cd9ee89).
- Audit export verified before compose down; retention removed zero files.
- Old container: 89714a938b73ef1a1f1b33949887a8e4c2e041ed18da29cfbffb6c2c8b770e54.
- New running container: 203d804dd78cc11e7e7596bdd8ae14d086c69017e6604676ede6fc1f971012a0.
- Same previously tested ARM64 image: d7da7df3287f2142b327dd955af21dbae76501acc0a9ad1f4d3c30c6942e2366.
- Both main compose.yml and the local operational override were used:
  ~/.home-baseline/container-runtime/absdd-codex-startup/compose.override.yml.
- All 20 mounts and six persistent volumes exactly preserved.
- UID 1655, CapEff=0, NoNewPrivs=1; enforced SELinux container_engine_t.
- Manifest-bound runtime preview/apply/check-only: PASS.
- Actual ephemeral Codex session in /rider-projects: PASS; no model turn.
- Extended JSON toolchain smoke including config and session start: PASS.
- Installed routing parity: 48 assertions PASS.
- Temporary smoke helpers removed after validation.

Documentation Impact: NoUpdateRequired for product guidance; no source or
behavior changes in this follow-up. Local untracked operational evidence only.
No compliance-plan ID or formal human approval closed. Main remains unchanged;
no Home sync, source release, merge, or additional image build performed.

## MergeAndSync-Abschluss / MergeAndSync closeout

DE: Nach ausdruecklicher Folgefreigabe des Owners wurde PR #118 mit Admin-Bypass
und --match-head-commit am oben genannten HEAD gemergt. Owner-Review
5804343797 vom 2026-11-06: "Gesichtet und fuer in Ordnung befunden" (COMMENTED,
keine technische GitHub-APPROVED-Freigabe; Admin-Bypass ausdruecklich autorisiert).
Unmittelbar vor Merge: 20 Checks erfolgreich, zwei bedingt uebersprungen,
keine offenen Review-Threads. Merge-Commit:
8adfac3f46af603198340058ad3ce49583b4b45f, 2026-11-06T17:35:02Z.
Lokale main per Fast-forward synchronisiert, HEAD...origin/main = 0 0;
vorhandene ungetrackte lokale Nachweise erhalten. Bereits aktiver Container
bleibt unveraendert; Konfiguration, Requirements und bwrap-Adapter bytegleich
zur gemergten Quelle. Sitzungsstart in /rider-projects und erweiterter
JSON-Smoke ueber die gemergten Skripte erneut PASS. Der Owner meldete zuvor
erfolgreiche interaktive Tests aller fuenf Harnesses ohne Fehlermeldungen.
Kein weiterer Austausch, Home-Sync oder Release erforderlich/vorgenommen.

EN: Following explicit owner authority, PR #118 merged with admin bypass bound
to the reviewed head above. All 20 executed checks passed, two conditional
jobs skipped, no open review thread. Owner review 5804343797 is COMMENTED;
the explicit bypass authority, not an invented APPROVED review, governs the
merge. Local main fast-forwarded to merge commit 8adfac3 with zero divergence.
Existing local evidence preserved. Running container unchanged; configuration,
requirements and bwrap adapter match merged source byte for byte. Local session
startup and extended JSON smoke via merged scripts passed again. Owner-reported
interactive acceptance covers all five harnesses; no new model turn was run.
No additional replacement, Home sync or release performed.
