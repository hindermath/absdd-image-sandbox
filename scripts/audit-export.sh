#!/bin/bash -p
set -euo pipefail

# The image installs this script and its system tools in root-owned paths.
# Agent-writable PATH entries must not select the interpreter or audit helpers.
export PATH=/usr/local/bin:/usr/bin:/bin

opencode_dir="${OPENCODE_DATA_DIR:-/home/adedev/.local/share/opencode}"
codex_dir="${CODEX_DATA_DIR:-/home/adedev/.codex}"
claude_dir="${CLAUDE_DATA_DIR:-/home/adedev/.claude}"
gemini_home="${GEMINI_CLI_HOME:-/home/adedev/.gemini-home}"
copilot_dir="${COPILOT_HOME:-/home/adedev/.copilot}"
audit_dir="${AUDIT_DIR:-/audit}"
audit_date="${AUDIT_DATE:-$(date -u +%F)}"
audit_output="${AUDIT_OUTPUT:-${audit_dir}/${audit_date}.jsonl}"
audit_run_id="${AUDIT_RUN_ID:-$(python3 -c 'import uuid; print(uuid.uuid4())')}"
project_path="${AUDIT_PROJECT_PATH:-${PWD:-unknown}}"
actor="${AUDIT_ACTOR:-$(id -un 2>/dev/null || whoami 2>/dev/null || printf 'unknown')}"
exported_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
session_entry_count=0

[[ "$audit_date" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || {
  printf 'Invalid audit UTC date\n' >&2
  exit 2
}
[[ "$audit_run_id" =~ ^[0-9a-fA-F-]{36}$ ]] || {
  printf 'Invalid audit run ID\n' >&2
  exit 2
}

if ! command -v jq >/dev/null 2>&1; then
  printf 'audit-export requires jq in PATH\n' >&2
  exit 1
fi

mkdir -p "$audit_dir"
tmp_output="$(mktemp "${audit_dir}/.audit-export.XXXXXX")"
trap 'rm -f "$tmp_output"' EXIT

iso_from_epoch() {
  local epoch="$1"
  if [ "$(uname -s)" = Darwin ]; then
    date -u -r "$epoch" +%Y-%m-%dT%H:%M:%SZ
  else
    date -u -d "@${epoch}" +%Y-%m-%dT%H:%M:%SZ
  fi
}

file_mtime() {
  if [ "$(uname -s)" = Darwin ]; then
    stat -f %m "$1"
  else
    stat -c %Y "$1"
  fi
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
  mtime="$(file_mtime "$source_path")"
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
    }' >>"$tmp_output"
  session_entry_count=$((session_entry_count + 1))
}

emit_tool_version() {
  local tool="$1" command_name="$2" state_dir="$3"
  local version
  command -v "$command_name" >/dev/null 2>&1 || return 0
  version="$($command_name --version 2>&1 | sed -n '1p')"
  jq -cn \
    --arg tool "$tool" \
    --arg version "$version" \
    --arg state_dir "$state_dir" \
    --arg project_path "$project_path" \
    --arg actor "$actor" \
    --arg exported_at "$exported_at" \
    '{
      record_type: "tool-version",
      tool: $tool,
      version: $version,
      state_dir: $state_dir,
      project_path: $project_path,
      actor: $actor,
      exported_at: $exported_at
    }' >>"$tmp_output"
}

collect_opencode() {
  local session_diff_dir="${opencode_dir}/storage/session_diff"
  local database="${opencode_dir}/opencode.db"

  # V2 storage presence is not per-session coverage; never open the database.
  if [ -f "$database" ] && [ ! -L "$database" ]; then
    jq -cn \
      --arg source_path "$database" \
      --arg modified_at "$(iso_from_epoch "$(file_mtime "$database")")" \
      --arg exported_at "$exported_at" \
      '{record_type: "storage-metadata", tool: "opencode",
        storage_format: "sqlite", source_path: $source_path,
        modified_at: $modified_at, exported_at: $exported_at,
        session_coverage: "not-exported"}' >>"$tmp_output"
  fi

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

collect_claude() {
  local projects_dir="${claude_dir}/projects"

  if [ -d "$projects_dir" ]; then
    while IFS= read -r -d '' path; do
      emit_entry "claude" "$path"
    done < <(find "$projects_dir" -type f -name '*.jsonl' -print0 | sort -z)
  fi
}

emit_tool_version "opencode" "opencode" "$opencode_dir"
emit_tool_version "codex" "codex" "$codex_dir"
emit_tool_version "claude" "claude" "$claude_dir"
emit_tool_version "antigravity" "agy" "${gemini_home}/.gemini/antigravity-cli"
emit_tool_version "copilot" "copilot" "$copilot_dir"
collect_opencode
collect_codex
collect_claude

# A run record proves that this invocation wrote the current day file even
# when no session metadata is discoverable. It does not claim session coverage.
jq -cn \
  --arg run_id "$audit_run_id" \
  --arg audit_date "$audit_date" \
  --arg exported_at "$exported_at" \
  --argjson session_metadata_count "$session_entry_count" \
  '{record_type: "audit-export-run", run_id: $run_id,
    audit_date: $audit_date, exported_at: $exported_at,
    session_coverage: "filesystem-metadata-only",
    session_metadata_count: $session_metadata_count}' >>"$tmp_output"

mv -f -- "$tmp_output" "$audit_output"
chmod 0640 "$audit_output" 2>/dev/null || true
line_count="$(wc -l <"$audit_output" | tr -d '[:space:]')"
printf 'Wrote %s audit metadata line(s) to %s\n' "$line_count" "$audit_output" >&2
