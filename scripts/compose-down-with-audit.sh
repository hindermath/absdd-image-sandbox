#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/compose-down-with-audit.sh [--podman|--podman-compose] [--dry-run] [compose down args...]

DE: Prueft Audit-Mount und aktuellen Export, behaelt 30 UTC-Tage und fuehrt
    erst dann compose down mit den uebrigen Argumenten aus. Jeder Fehler vor
    down blockiert down. --dry-run zeigt nur den Plan und schreibt nichts.
EN: Verifies the audit mount and current export, retains 30 UTC days, then
    calls compose down with remaining arguments. Any earlier failure blocks
    down. --dry-run only previews the plan without writing.
    Normal use preserves named volumes. -v deletes them by explicit choice.
Examples:

  scripts/compose-down-with-audit.sh --podman --dry-run
  scripts/compose-down-with-audit.sh --podman
  scripts/compose-down-with-audit.sh --podman --remove-orphans
USAGE
}

compose_cmd=()

case "${1:-}" in
  --help|-h)
    usage
    exit 0
    ;;
  --podman)
    compose_cmd=(podman compose)
    shift
    ;;
  --podman-compose)
    compose_cmd=(podman-compose)
    shift
    ;;
  *)
    if command -v podman >/dev/null 2>&1; then
      compose_cmd=(podman compose)
    elif command -v podman-compose >/dev/null 2>&1; then
      compose_cmd=(podman-compose)
    else
      printf 'Neither podman nor podman-compose was found in PATH\n' >&2
      exit 1
    fi
    ;;
esac

if [ "${1:-}" = "--dry-run" ]; then
  printf 'DRY-RUN: verify audit mount, export current metadata, retain 30 UTC days, then compose down\n'
  exit 0
fi

audit_dir="${AUDIT_DIR:-./audit-logs}"
if [ -L "$audit_dir" ]; then
  printf 'Audit stop blocked: audit directory is a symlink.\n' >&2
  exit 1
fi
mkdir -p -- "$audit_dir"
audit_dir="$(cd "$audit_dir" && pwd -P)"
day="$(date -u +%F)"
run_id="$(python3 -c 'import uuid; print(uuid.uuid4())')"
lock_dir="$audit_dir/.audit-stop.lock"
if ! mkdir -- "$lock_dir" 2>/dev/null; then
  printf 'Audit stop blocked: audit directory is locked; inspect the owner before retry.\n' >&2
  exit 1
fi
marker=""
cleanup() {
  [ -z "$marker" ] || rm -f -- "$marker"
  if [ -d "$lock_dir" ] && [ ! -L "$lock_dir" ] \
      && { [ ! -e "$lock_dir/owner" ] || [ "$(cat "$lock_dir/owner" 2>/dev/null || true)" = "$run_id" ]; }; then
    rm -f -- "$lock_dir/owner" 2>/dev/null || true
    rmdir -- "$lock_dir" 2>/dev/null || true
  fi
}
trap cleanup EXIT
printf '%s\n' "$run_id" > "$lock_dir/owner"
marker="$(mktemp "$audit_dir/.audit-mount.XXXXXXXX")"

if ! "${compose_cmd[@]}" exec -T ade /usr/bin/test -f "/audit/$(basename "$marker")"; then
  printf 'Audit stop blocked at mount check: host audit directory is not visible at /audit. Check the Compose audit mount, then retry this wrapper; no down was started. See --help.\n' >&2
  exit 1
fi
if "${compose_cmd[@]}" exec -T -e "AUDIT_DATE=$day" -e "AUDIT_RUN_ID=$run_id" ade /usr/local/bin/audit-export; then
  :
else
  audit_status=$?
  printf 'Audit stop blocked at export (exit %s): exporter failed; no down was started. Check the exporter and retry this wrapper. See --help.\n' "$audit_status" >&2
  exit "$audit_status"
fi
if [ ! -s "$audit_dir/$day.jsonl" ] || [ -L "$audit_dir/$day.jsonl" ]; then
  printf 'Audit stop blocked at verification: host day file is absent, empty or a link. Check the audit mount and retry this wrapper; no down was started. See --help.\n' >&2
  exit 1
fi
if ! "${compose_cmd[@]}" exec -T ade /usr/local/bin/audit-retention verify --audit-dir /audit --date "$day" --run-id "$run_id" >/dev/null; then
  printf 'Audit stop blocked at verification: current nonempty export run record missing. Check the exporter and retry this wrapper; no down was started. See --help.\n' >&2
  exit 1
fi
if retention_output="$("${compose_cmd[@]}" exec -T ade /usr/local/bin/audit-retention retain --audit-dir /audit --date "$day" 2>&1)"; then
  printf '%s\n' "$retention_output"
else
  removed='unknown'
  if [[ "$retention_output" =~ removed=([0-9]+) ]]; then
    removed="${BASH_REMATCH[1]}"
  fi
  printf 'Audit stop blocked at retention: removed=%s old audit files before failure. Inspect the audit directory, then retry this wrapper for a new export; no down was started. See --help.\n' "$removed" >&2
  exit 1
fi
printf 'Current audit export verified; retention completed before compose down.\n' >&2

"${compose_cmd[@]}" down "$@"
