# Lokale Codex-Startkorrektur / Local Codex startup activation

Explicit owner authority: fix both startup blockers, retain sandbox boundaries,
commit and push PR #118, do not merge, replace the running container.

- PR: https://github.com/hindermath/absdd-image-sandbox/pull/118 (OPEN).
- Candidate source: 7d24ca6bf9167aee44dc5877dc72a5ef86b699f6.
- Canonical main remains f2e417b7d326ad2c0d7ba151926cb05535bd67b4.
- Active image: d7da7df3287f2142b327dd955af21dbae76501acc0a9ad1f4d3c30c6942e2366.
- Active container: 89714a938b73ef1a1f1b33949887a8e4c2e041ed18da29cfbffb6c2c8b770e54.
- Local override: ~/.home-baseline/container-runtime/absdd-codex-startup/compose.override.yml.
- Rollback image: localhost/absdd-image-sandbox_ade:rollback-before-codex-startup-fix-20261106
  (cf4c8803e2c9ef3bd0d41e9466b35010046892bd7f60bf1df6518e2540600439).
- Audit archive: /private/tmp/absdd-audit-before-codex-fix-20261106.tar.gz.
- Both replacements used compose-down-with-audit.sh --podman; current export
  verified before shutdown, retention removed zero files, no volumes removed.
- All 20 original mounts and six persistent volumes match the baseline exactly.
- Effective security: CapEff=0; NoNewPrivs=1; SELinux container_engine_t enforced;
  non-root adedev, no privileged mode, Codex workspace/network restrictions retained.
- Strict config load: PASS, no ignored-setting warnings.
- Ephemeral local session in /rider-projects with preserved login volumes: PASS.
- Fresh AGENTS.md fixture session and effective policy checks: PASS.
- Extended JSON toolchain smoke on active replacement: exit 0.
- Runtime preview, manifest-bound apply and check-only: PASS.
- Installed model-routing runtime/preset parity: 48 assertions PASS.
- Offline configuration/session/adapter regressions: 14 tests PASS.
- Synthetic sandbox negative probes: outside-workspace/tmp/metadata writes,
  secret reads and daemon-socket access blocked; workspace writes permitted.
- No model turn, provider inference or GUI interaction claimed.
- At delivery, final-head CI still has pending jobs; no complete CI pass claimed.

Documentation Impact: UpdateRequired; source owner repository maintainer;
German/English reader paths README, operations validation guide, maintenance
record and sandbox-isolation policy updated in PR. This file is local operational
activation evidence, deliberately untracked; no Home sync or source-main merge.

Until PR merge, start/recreate from the main clone with both compose.yml and the
local override above. A plain compose up against unchanged main does not retain
the candidate image/SELinux selection.
