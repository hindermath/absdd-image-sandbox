#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="${IMAGE_NAME:-localhost/absdd-image-sandbox_ade:latest}"
SBOM_DIR="${SBOM_DIR:-sboms}"
CONTAINER_RUNTIME="${CONTAINER_RUNTIME:-podman}"
SYFT_VERSION="${SYFT_VERSION:-1.46.0}"
SKIP_BUILD="${SKIP_BUILD:-false}"
DRY_RUN="false"

usage() {
  cat <<'USAGE'
Usage: scripts/build-and-sbom.sh [options]

DE: ADE-Sandbox-Image bauen und eine CycloneDX-JSON-SBOM erzeugen.
EN: Build the ADE sandbox image and create a CycloneDX JSON SBOM.

Options:
  --image NAME         Image tag to build and scan.
  --sbom-dir DIR      Directory for generated SBOM files.
  --runtime NAME      Container runtime: podman.
  --skip-build        Scan the existing image without rebuilding it.
  --dry-run           Show the planned build and SBOM checks without writes.
  -h, --help          Show this help.

Sicherheit / Security:
  Syft muss im Image oder exakt in SYFT_VERSION vorhanden sein. Es gibt keinen
  moving fallback. / Syft must be in the image or exactly match SYFT_VERSION;
  no moving fallback is used.

Environment variables with the same names are also supported:
IMAGE_NAME, SBOM_DIR, CONTAINER_RUNTIME, SYFT_VERSION, SKIP_BUILD.
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
  --skip-build)
    SKIP_BUILD="true"
    shift
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

if [[ "${DRY_RUN}" == "true" ]]; then
  printf '%s\n' "DRY-RUN: ${runtime} build --pull -t <local-image> . (unless --skip-build)"
  printf '%s\n' "DRY-RUN: require image-integrated Syft or host Syft exactly ${SYFT_VERSION}; no moving container fallback"
  printf '%s\n' "DRY-RUN: write one CycloneDX JSON file below ${SBOM_DIR}"
  exit 0
fi

mkdir -p "${SBOM_DIR}"

if [[ "${SKIP_BUILD}" != "true" ]]; then
  "${runtime}" build --pull -t "${IMAGE_NAME}" .
fi

date_stamp="$(date +%Y-%m-%d)"
safe_image="$(printf '%s' "${IMAGE_NAME}" | tr '/:@' '---' | tr -cd 'A-Za-z0-9._-')"
out_file="${date_stamp}-${safe_image}.cdx.json"
out_path="${SBOM_DIR}/${out_file}"
source_version="${IMAGE_NAME##*:}"

if "${runtime}" run --rm --entrypoint syft "${IMAGE_NAME}" version >/dev/null 2>&1; then
  # The one-shot scanner uses root only to read every image layer path; the
  # actual sandbox service continues to run as the non-root adedev user.
  "${runtime}" run --rm --user 0 --entrypoint syft "${IMAGE_NAME}" \
    "dir:/" \
    --select-catalogers "+javascript-package-cataloger" \
    --source-name "${IMAGE_NAME}" \
    --source-version "${source_version}" \
    -o "cyclonedx-json" >"${out_path}"
elif command -v syft >/dev/null 2>&1; then
  observed_syft="$(syft version 2>/dev/null | awk '/^Version:/ {print $2; exit}')"
  if [[ "${observed_syft}" != "${SYFT_VERSION}" ]]; then
    echo "Host Syft version mismatch: expected ${SYFT_VERSION}, observed ${observed_syft:-unknown}." >&2
    exit 1
  fi
  syft "${IMAGE_NAME}" -o "cyclonedx-json=${out_path}"
else
  echo "Syft is unavailable in the target image and no host Syft ${SYFT_VERSION} is available; refusing an unpinned fallback." >&2
  exit 1
fi

if [[ ! -s "${out_path}" ]]; then
  echo "SBOM was not created or is empty: ${out_path}" >&2
  exit 1
fi

echo "SBOM written: ${out_path}"
