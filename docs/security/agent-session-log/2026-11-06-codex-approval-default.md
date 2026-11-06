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
- Next step: review PR and CI; build and activation require later authority.
