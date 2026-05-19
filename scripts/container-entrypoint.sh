#!/usr/bin/env bash
set -Eeuo pipefail

audit_ran=0
child_pid=""

run_audit_export() {
  if [ "$audit_ran" -eq 1 ]; then
    return 0
  fi
  audit_ran=1

  case "${ADE_AUDIT_ON_STOP:-true}" in
    0|false|False|FALSE|no|No|NO)
      printf 'Skipping shutdown audit export because ADE_AUDIT_ON_STOP=%s\n' "${ADE_AUDIT_ON_STOP}" >&2
      return 0
      ;;
  esac

  if ! command -v audit-export >/dev/null 2>&1; then
    printf 'audit-export is not available during shutdown; skipping audit export\n' >&2
    return 0
  fi

  audit-export || printf 'audit-export failed during shutdown; continuing container stop\n' >&2
}

shutdown() {
  run_audit_export

  if [ -n "$child_pid" ] && kill -0 "$child_pid" 2>/dev/null; then
    kill -TERM "$child_pid" 2>/dev/null || true
    wait "$child_pid" 2>/dev/null || true
  fi

  exit 0
}

trap shutdown TERM INT
trap run_audit_export EXIT

if [ "$#" -eq 0 ]; then
  set -- /bin/bash -lc 'while :; do sleep 1; done'
fi

"$@" &
child_pid="$!"

set +e
wait "$child_pid"
status="$?"
set -e

run_audit_export
exit "$status"
