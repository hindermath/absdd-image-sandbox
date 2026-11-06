#!/usr/bin/env bash
set -euo pipefail

# Keep credentials in the environment; never put them in argv or diagnostics.
password="${OPENCODE_PASSWORD:-}"
if (( ${#password} < 16 )) || [[ ! "$password" =~ [^[:space:]] ]]; then
  printf '%s\n' 'OPENCODE_PASSWORD must contain at least 16 non-placeholder characters in the ignored opencode.env.' >&2
  exit 1
fi
case "${password,,}" in
  changeme*|change-me*|password*|example*|placeholder*|your-password*|replace-me*|opencode-password*|secret*|set-a-private-local-value*|\<*)
    printf '%s\n' 'OPENCODE_PASSWORD contains a known placeholder; set a private local value in opencode.env.' >&2
    exit 1
    ;;
esac
unset password

exec opencode serve --hostname 0.0.0.0 --port 5199
