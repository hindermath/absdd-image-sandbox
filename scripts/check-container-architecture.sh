#!/usr/bin/env bash
set -euo pipefail

platform=""
image=""
allow_cross=false
while (($#)); do
  case "$1" in
  --platform | --image)
    if (($# < 2)) || [[ -z "$2" ]]; then
      echo "$1 requires a value" >&2
      exit 2
    fi
    if [[ "$1" == --platform ]]; then platform="$2"; else image="$2"; fi
    shift 2
    ;;
  --allow-cross-architecture)
    allow_cross=true
    shift
    ;;
  -h | --help)
    echo 'Usage: check-container-architecture.sh [--platform linux/arm64|linux/amd64] [--allow-cross-architecture] [--image NAME]'
    exit 0
    ;;
  *)
    echo "Unknown option: $1" >&2
    exit 2
    ;;
  esac
done

normalize_arch() {
  case "$1" in
  arm64 | aarch64 | ARM64) echo arm64 ;;
  amd64 | x86_64 | AMD64) echo amd64 ;;
  *)
    echo "Unknown architecture / Unbekannte Architektur: $1" >&2
    return 1
    ;;
  esac
}

host_os="$(uname -s)"
host_arch="$(uname -m)"
case "$host_os" in
Darwin)
  # uname can describe the translated process rather than the Apple hardware.
  apple_arm="$(sysctl -n hw.optional.arm64)"
  case "$apple_arm" in
  1) host_arch=arm64 ;;
  0) ;;
  *)
    echo 'Cannot determine Apple hardware architecture' >&2
    exit 1
    ;;
  esac
  ;;
Linux) ;;
MINGW* | MSYS* | CYGWIN*)
  host_arch="${PROCESSOR_ARCHITEW6432:-${PROCESSOR_ARCHITECTURE:-}}"
  ;;
*)
  echo "Unsupported host OS: $host_os" >&2
  exit 1
  ;;
esac
host_arch="$(normalize_arch "$host_arch")"
native="linux/$host_arch"
explicit="$platform"
if $allow_cross && [[ -z "$explicit" ]]; then
  echo 'Cross-build approval requires an explicit --platform' >&2
  exit 2
fi
platform="${platform:-$native}"
case "$platform" in
linux/arm64 | linux/amd64) ;;
*)
  echo "Unsupported target platform: $platform" >&2
  exit 2
  ;;
esac

for setting in DOCKER_DEFAULT_PLATFORM CONTAINER_DEFAULT_PLATFORM; do
  value="${!setting:-}"
  if [[ -n "$value" && "$value" != "$platform" ]]; then
    echo "$setting=$value conflicts with target $platform" >&2
    exit 1
  fi
done
engine="$(podman info --format '{{.Host.OS}}/{{.Host.Arch}}')"
[[ "$engine" == linux/* && "$engine" != *$'\n'* ]] || {
  echo 'Invalid Podman engine platform' >&2
  exit 1
}
engine="linux/$(normalize_arch "${engine#linux/}")"
if ! $allow_cross && [[ "$platform" != "$native" || "$engine" != "$native" ]]; then
  echo "Native architecture required: host=$native engine=$engine target=$platform" >&2
  exit 1
fi
if [[ -n "$image" ]]; then
  observed="$(podman image inspect --format '{{.Os}}/{{.Architecture}}' "$image")"
  [[ "$observed" == linux/* && "$observed" != *$'\n'* ]] || {
    echo 'Invalid image platform' >&2
    exit 1
  }
  observed="linux/$(normalize_arch "${observed#linux/}")"
  [[ "$observed" == "$platform" ]] || {
    echo "Image platform mismatch: expected=$platform observed=$observed" >&2
    exit 1
  }
fi
printf 'Architecture OK: host=%s engine=%s target=%s cross=%s\n' "$native" "$engine" "$platform" "$allow_cross" >&2
printf '%s\n' "$platform"
