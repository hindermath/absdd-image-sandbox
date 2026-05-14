# Audit Logs

This directory is the default host-side mount for `/audit` inside the `ade` container.

Only this README and `.gitkeep` are tracked in Git. Generated JSONL audit files are local evidence artifacts and must not be committed.

## Stored Data

`audit-export` writes one JSON object per discovered session metadata source. The minimum fields are:

- `tool`
- `session_id`
- `started_at`
- `ended_at`
- `project_path`
- `actor`

The export also records `source_type`, `source_path`, and `exported_at` so that operators can trace which local metadata source produced an entry.

The export must not include prompt text, response text, API keys, or raw session content. The current implementation uses file names and file modification times only; it does not parse OpenCode or Codex session files.

## Access

Treat generated audit files as internal security evidence. Access should be limited to the repository owner, the responsible operator, and the audit or security role that reviews CL_12 evidence.

## Retention

Default recommendation: keep generated JSONL files for 90 days unless the applicable audit, training, or incident process requires a different retention period.

## Deletion

Delete expired local audit files from the host-side `audit-logs/` directory. Do not delete files that are needed for an open audit, security review, incident analysis, or release approval.
