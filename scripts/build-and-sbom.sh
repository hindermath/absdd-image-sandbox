#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="${IMAGE_NAME:-absdd-image-sandbox-ade:latest}"
SBOM_DIR="${SBOM_DIR:-sboms}"
CONTAINER_RUNTIME="${CONTAINER_RUNTIME:-podman}"
SYFT_IMAGE="${SYFT_IMAGE:-docker.io/anchore/syft:latest}"
SKIP_BUILD="${SKIP_BUILD:-false}"

usage() {
  cat <<'USAGE'
Usage: scripts/build-and-sbom.sh [options]

Build the ADE sandbox image and create a CycloneDX JSON SBOM.

Options:
  --image NAME         Image tag to build and scan.
  --sbom-dir DIR      Directory for generated SBOM files.
  --runtime NAME      Container runtime: podman.
  --syft-image NAME   Container image used when local syft is not installed.
  --skip-build        Scan the existing image without rebuilding it.
  -h, --help          Show this help.

Environment variables with the same names are also supported:
IMAGE_NAME, SBOM_DIR, CONTAINER_RUNTIME, SYFT_IMAGE, SKIP_BUILD.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --image)
      IMAGE_NAME="$2"
      shift 2
      ;;
    --sbom-dir)
      SBOM_DIR="$2"
      shift 2
      ;;
    --runtime)
      CONTAINER_RUNTIME="$2"
      shift 2
      ;;
    --syft-image)
      SYFT_IMAGE="$2"
      shift 2
      ;;
    --skip-build)
      SKIP_BUILD="true"
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

detect_runtime() {
  if [[ "${CONTAINER_RUNTIME}" != "podman" ]]; then
    echo "Unsupported container runtime: ${CONTAINER_RUNTIME}. This repository uses Podman only." >&2
    exit 1
  fi

  command -v podman >/dev/null 2>&1 || {
    echo "podman was not found in PATH." >&2
    exit 1
  }
  printf '%s\n' "podman"
  return
}

runtime="$(detect_runtime)"
mkdir -p "${SBOM_DIR}"

if [[ "${SKIP_BUILD}" != "true" ]]; then
  "${runtime}" build --pull -t "${IMAGE_NAME}" .
fi

date_stamp="$(date +%Y-%m-%d)"
safe_image="$(printf '%s' "${IMAGE_NAME}" | tr '/:@\\' '----' | tr -cd 'A-Za-z0-9._-')"
out_file="${date_stamp}-${safe_image}.cdx.json"
out_path="${SBOM_DIR}/${out_file}"

if command -v syft >/dev/null 2>&1; then
  syft "${IMAGE_NAME}" -o "cyclonedx-json=${out_path}"
else
  tmp_dir="$(mktemp -d)"
  cleanup() {
    rm -rf "${tmp_dir}"
  }
  trap cleanup EXIT

  "${runtime}" save "${IMAGE_NAME}" -o "${tmp_dir}/image.tar"
  sbom_abs_dir="$(cd "${SBOM_DIR}" && pwd)"
  "${runtime}" run --rm \
    -v "${tmp_dir}:/work:ro" \
    -v "${sbom_abs_dir}:/out" \
    "${SYFT_IMAGE}" \
    "docker-archive:/work/image.tar" \
    -o "cyclonedx-json=/out/${out_file}"
fi

if [[ ! -s "${out_path}" ]]; then
  echo "SBOM was not created or is empty: ${out_path}" >&2
  exit 1
fi

echo "SBOM written: ${out_path}"
