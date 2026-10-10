#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
action="${1:-}"
case "$action" in
build | up | recreate) shift ;;
*)
  echo 'Usage: sandbox-lifecycle.sh build|up|recreate [--home-baseline] [--platform linux/arm64|linux/amd64] [--allow-cross-architecture]' >&2
  exit 2
  ;;
esac
architecture_args=()
compose_files=(-f compose.yml)
while (($#)); do
  case "$1" in
  --home-baseline)
    compose_files+=(-f compose.home-baseline.yml)
    shift
    ;;
  --platform)
    (($# >= 2)) || {
      echo '--platform requires a value' >&2
      exit 2
    }
    architecture_args+=(--platform "$2")
    shift 2
    ;;
  --allow-cross-architecture)
    architecture_args+=(--allow-cross-architecture)
    shift
    ;;
  *)
    echo "Unknown option: $1" >&2
    exit 2
    ;;
  esac
done
cd "${script_dir}/.."
image='localhost/absdd-image-sandbox_ade:latest'
platform="$(bash "${script_dir}/check-container-architecture.sh" ${architecture_args[@]+"${architecture_args[@]}"})"
override="$(mktemp "${TMPDIR:-/tmp}/ade-platform.XXXXXX")"
trap 'rm -f "$override"' EXIT
printf 'services:\n  ade:\n    image: %s\n    platform: %s\n' "$image" "$platform" >"$override"
compose_files+=(-f "$override")
podman compose "${compose_files[@]}" config >/dev/null
if [[ "$action" == build ]]; then
  podman compose "${compose_files[@]}" build --pull -- ade
  bash "${script_dir}/check-container-architecture.sh" ${architecture_args[@]+"${architecture_args[@]}"} --image "$image" >/dev/null
  exit 0
fi
bash "${script_dir}/check-container-architecture.sh" ${architecture_args[@]+"${architecture_args[@]}"} --image "$image" >/dev/null
expected_image="$(podman image inspect --format '{{.Id}}' "$image")"
if [[ "$action" == recreate ]]; then
  echo 'Recreate: back up non-persistent container files first. Volumes are retained.' >&2
  podman compose "${compose_files[@]}" up -d --no-build --pull never --force-recreate ade
else
  # A plain up must not silently destroy a previous writable container layer.
  existing="$(podman compose "${compose_files[@]}" ps -q)"
  if [[ -n "$existing" ]]; then
    [[ "$existing" != *$'\n'* ]] || {
      echo 'Expected at most one ADE container' >&2
      exit 1
    }
    existing_image="$(podman inspect --format '{{.Image}}' "$existing")"
    [[ "$existing_image" == "$expected_image" ]] || {
      echo 'Existing container uses an older image; back up its files, then use recreate.' >&2
      exit 1
    }
  fi
  podman compose "${compose_files[@]}" up -d --no-build --pull never --no-recreate ade
fi
container="$(podman compose "${compose_files[@]}" ps -q)"
[[ -n "$container" && "$container" != *$'\n'* ]] || {
  echo 'Expected exactly one ADE container' >&2
  exit 1
}
container_image="$(podman inspect --format '{{.Image}}' "$container")"
bash "${script_dir}/check-container-architecture.sh" ${architecture_args[@]+"${architecture_args[@]}"} --image "$container_image" >/dev/null
[[ "$expected_image" == "$container_image" ]] || {
  echo 'Existing container uses an older image; back up its files, then use recreate.' >&2
  exit 1
}
