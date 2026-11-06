# Codex approval default correction

Owner request: correct image default, tests and documentation; commit, push
and PR. No merge or container replacement.

- P0-1 maintenance: replace explicitly unsupported `untrusted` default with
  `on-request`; preserve existing enforced sandbox and allowed policy set.
- Add offline configuration loading to both smoke modes and regression tests.
- Bilingual documentation: `docs/maintenance/codex-approval-default.md`.
- Validate corrected files in a disposable ARM64 container with Codex 0.164.0;
  no network, credentials, project mounts or model calls.
- Existing container and user logs preserved. P1-4 formal approval not inferred.
- Follow-up authority: fix rootless session startup, remove ignored settings,
  add session smoke, commit/push PR 118 and replace the container; no merge.
- Rootless masks retain empty daemon/secret overlays and read-only metadata.
  Native synthetic probes permit workspace writes and deny outside/tmp/metadata
  writes, secret reads and daemon socket access. No live model turn.
- Session smoke checks AGENTS.md instruction-source reporting and effective
  workspace-write, network-disabled, /tmp-excluded, on-request defaults.
- Candidate build and activation receipt are separate from a PR merge.
