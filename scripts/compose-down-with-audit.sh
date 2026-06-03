#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/compose-down-with-audit.sh [--podman|--podman-compose] [compose down args...]

Runs audit-export inside the ade container, then runs compose down with the
remaining arguments. Examples:

  scripts/compose-down-with-audit.sh --podman
  scripts/compose-down-with-audit.sh --podman -v
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

if "${compose_cmd[@]}" exec -T ade audit-export; then
  printf 'Audit metadata export completed before compose down.\n' >&2
else
  printf 'Warning: audit metadata export did not complete; continuing with compose down.\n' >&2
fi

exec "${compose_cmd[@]}" down "$@"
