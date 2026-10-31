#!/usr/bin/env bash
set -euo pipefail

MODE=""
EVIDENCE=""
FEATURE_DIRECTORY=""
DRY_RUN="false"

usage() {
  cat <<'USAGE'
Usage: scripts/test-ade-sandbox-hardening.sh --mode MODE [options]

Prueft die ADE-Sandbox mit dem gemeinsamen, nicht sensiblen Evidenzvertrag.
Validates the ADE sandbox with the shared non-sensitive evidence contract.

Options:
  --mode MODE       Input, Static, Runtime, SupplyChain, Documentation,
                    Accessibility, or All.
  --evidence PATH   Repository-relative verification-evidence JSON path.
  --feature-directory PATH  Explicit Feature 004 directory; requires its own evidence.
  --dry-run         Show planned checks without execution; exit 0 is not a pass.
  -h, --help        Show this bilingual help.

Exit codes:
  0  Requested scope is evidenced.
  1  Validation or observed check failed (RED).
  2  Usage, JSON contract, or repository-path error.
  3  Required platform, runner, executable, or human evidence is unavailable.

DE: Feature 004 verwendet nur seine eigene Evidence. All mit offenen
Pflicht-Gates ist nicht GREEN. / Feature 004 uses only its own evidence;
All with mandatory Open gates is never GREEN.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      [[ $# -ge 2 ]] || { echo "--mode requires a value" >&2; exit 2; }
      MODE="$2"
      shift 2
      ;;
    --evidence)
      [[ $# -ge 2 ]] || { echo "--evidence requires a value" >&2; exit 2; }
      EVIDENCE="$2"
      shift 2
      ;;
    --feature-directory)
      [[ $# -ge 2 && -n "$2" ]] || { echo "--feature-directory requires a value" >&2; exit 2; }
      FEATURE_DIRECTORY="$2"
      shift 2
      ;;
    --dry-run)
      DRY_RUN="true"
      shift
      ;;
    -h | --help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

[[ -n "${MODE}" ]] || { echo "--mode is required" >&2; usage >&2; exit 2; }

mode_normalized="$(printf '%s' "${MODE}" | tr '[:upper:]' '[:lower:]')"
case "${mode_normalized}" in
  input) MODE="Input" ;;
  static) MODE="Static" ;;
  runtime) MODE="Runtime" ;;
  supplychain | supply-chain) MODE="SupplyChain" ;;
  documentation) MODE="Documentation" ;;
  accessibility) MODE="Accessibility" ;;
  all) MODE="All" ;;
  *) echo "Unsupported mode: ${MODE}" >&2; exit 2 ;;
esac

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
arguments=(
  "${repo_root}/scripts/lib/secure_development_hardening.py"
  run-mode
  --repo "${repo_root}"
  --mode "${MODE}"
)
if [[ -n "${EVIDENCE}" ]]; then
  arguments+=(--evidence "${EVIDENCE}")
fi
if [[ -n "${FEATURE_DIRECTORY}" ]]; then
  arguments+=(--feature-directory "${FEATURE_DIRECTORY}")
fi
if [[ "${DRY_RUN}" == "true" ]]; then
  arguments+=(--dry-run)
fi

# The Python core owns all semantic decisions so Bash and PowerShell cannot
# silently drift.  No eval or shell-composed command is used here.
python3 "${arguments[@]}"
