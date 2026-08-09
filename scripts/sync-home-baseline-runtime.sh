#!/usr/bin/env bash
set -euo pipefail

readonly source_dir="/opt/home-baseline"
readonly home_dir="/home/adedev"
readonly lock_file="/usr/local/share/absdd-image-sandbox/home-baseline.lock.json"

usage() {
	cat >&2 <<'EOF'
Verwendung / Usage: sync-home-baseline-runtime MODE

Modi / Modes:
  --dry-run     Aenderungen nur anzeigen / only show changes
  --check-only  Drift schreibfrei pruefen / check drift without writing
  --apply       Home Runtime anwenden / apply the Home Runtime
EOF
}

if [[ $# -ne 1 ]]; then
	usage
	exit 2
fi

case "$1" in
--dry-run | --check-only | --apply) mode="$1" ;;
*)
	usage
	exit 2
	;;
esac

if [[ "$(id -un)" != "adedev" || "${HOME:-}" != "${home_dir}" ]]; then
	echo "Fehler: Der Wrapper darf nur als adedev mit HOME=${home_dir} laufen." >&2
	echo "Error: The wrapper must run as adedev with HOME=${home_dir}." >&2
	exit 2
fi

if [[ ! -f "${lock_file}" || ! -d "${source_dir}/.git" || ! -f "${source_dir}/scripts/sync-home.sh" ]]; then
	echo "Fehler: Die gepinnte Home-Baseline-Quelle ist unvollstaendig." >&2
	echo "Error: The pinned Home Baseline source is incomplete." >&2
	exit 1
fi

resolved_source="$(realpath -e "${source_dir}")"
resolved_home="$(realpath -e "${home_dir}")"
case "${resolved_source}" in
"${resolved_home}" | "${resolved_home}"/*)
	echo "Fehler: Die Home-Baseline-Quelle darf nicht im Ziel-Home liegen." >&2
	echo "Error: The Home Baseline source must not be inside the target home." >&2
	exit 1
	;;
esac

jq -e '.schemaVersion == 1 and (.commit | test("^[0-9a-f]{40}$"))' \
	"${lock_file}" >/dev/null

sync_args=(--runtime-only)
case "${mode}" in
--dry-run) sync_args+=(--dry-run) ;;
--check-only) sync_args+=(--check-only) ;;
--apply) ;;
esac

exec bash "${source_dir}/scripts/sync-home.sh" "${sync_args[@]}"
