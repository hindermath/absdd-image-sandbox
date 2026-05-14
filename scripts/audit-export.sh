#!/usr/bin/env bash
set -euo pipefail

opencode_dir="${OPENCODE_DATA_DIR:-/home/adedev/.local/share/opencode}"
codex_dir="${CODEX_DATA_DIR:-/home/adedev/.codex}"
audit_dir="${AUDIT_DIR:-/audit}"
audit_date="${AUDIT_DATE:-$(date -u +%F)}"
audit_output="${AUDIT_OUTPUT:-${audit_dir}/${audit_date}.jsonl}"
project_path="${AUDIT_PROJECT_PATH:-${PWD:-unknown}}"
actor="${AUDIT_ACTOR:-$(id -un 2>/dev/null || whoami 2>/dev/null || printf 'unknown')}"
exported_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

if ! command -v jq >/dev/null 2>&1; then
  printf 'audit-export requires jq in PATH\n' >&2
  exit 1
fi

mkdir -p "$audit_dir"
tmp_output="$(mktemp "${audit_dir}/.audit-export.XXXXXX")"
trap 'rm -f "$tmp_output"' EXIT

iso_from_epoch() {
  local epoch="$1"
  date -u -d "@${epoch}" +%Y-%m-%dT%H:%M:%SZ
}

session_id_from_path() {
  local base id
  base="$(basename "$1")"
  id="${base%.jsonl}"
  id="${id%.json}"
  printf '%s' "$id"
}

emit_entry() {
  local tool="$1"
  local source_path="$2"
  local source_type session_id mtime timestamp

  if [ -d "$source_path" ]; then
    source_type="directory"
  elif [ -f "$source_path" ]; then
    source_type="file"
  else
    return 0
  fi

  session_id="$(session_id_from_path "$source_path")"
  mtime="$(stat -c %Y "$source_path")"
  timestamp="$(iso_from_epoch "$mtime")"

  jq -cn \
    --arg tool "$tool" \
    --arg session_id "$session_id" \
    --arg started_at "$timestamp" \
    --arg ended_at "$timestamp" \
    --arg project_path "$project_path" \
    --arg actor "$actor" \
    --arg source_type "$source_type" \
    --arg source_path "$source_path" \
    --arg exported_at "$exported_at" \
    '{
      tool: $tool,
      session_id: $session_id,
      started_at: $started_at,
      ended_at: $ended_at,
      project_path: $project_path,
      actor: $actor,
      source_type: $source_type,
      source_path: $source_path,
      exported_at: $exported_at
    }' >> "$tmp_output"
}

collect_opencode() {
  local session_diff_dir="${opencode_dir}/storage/session_diff"

  if [ -d "$session_diff_dir" ]; then
    while IFS= read -r -d '' path; do
      emit_entry "opencode" "$path"
    done < <(find "$session_diff_dir" -maxdepth 1 -type f -name 'ses_*' -print0 | sort -z)
  fi
}

collect_codex() {
  local sessions_dir="${codex_dir}/sessions"

  if [ -d "$sessions_dir" ]; then
    while IFS= read -r -d '' path; do
      emit_entry "codex" "$path"
    done < <(find "$sessions_dir" -type f -print0 | sort -z)
  fi
}

collect_opencode
collect_codex

cp "$tmp_output" "$audit_output"
chmod 0640 "$audit_output" 2>/dev/null || true
line_count="$(wc -l < "$audit_output" | tr -d '[:space:]')"
printf 'Wrote %s audit metadata line(s) to %s\n' "$line_count" "$audit_output" >&2
