#!/usr/bin/env bash
# DE: Podman-Pin-Pflege ueber PowerShell 7. EN: PowerShell 7 pin maintenance.
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
args=()
while (($#)); do
  case "$1" in
    --action) args+=(-Action "${2:?--action requires a value}"); shift 2 ;;
    --repo) args+=(-Repo "${2:?--repo requires a value}"); shift 2 ;;
    --output-directory) args+=(-OutputDirectory "${2:?output path required}"); shift 2 ;;
    --payload-directory) args+=(-PayloadDirectory "${2:?payload path required}"); shift 2 ;;
    --json) args+=(-Json); shift ;;
    --dry-run) args+=(-WhatIf); shift ;;
    -h|--help)
      printf '%s\n' 'Usage: bash scripts/update-toolchain-pins.sh [--action Check|Prepare|Verify|Apply]' \
        '  [--repo PATH] [--output-directory NEW_EXTERNAL_PATH]' \
        '  [--payload-directory PATH] [--json] [--dry-run]' \
        'DE: Check ist read-only; Apply nur nach Payload-Pruefung.' \
        'EN: Check is read-only; Apply requires verified payload input.'
      exit 0 ;;
    *) printf 'Unknown option / Unbekannte Option: %s\n' "$1" >&2; exit 2 ;;
  esac
done
exec pwsh -NoProfile -File "${script_dir}/update-toolchain-pins.ps1" "${args[@]}"
