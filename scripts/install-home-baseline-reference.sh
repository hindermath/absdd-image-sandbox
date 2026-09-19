#!/usr/bin/env bash
set -euo pipefail

lock_file="${1:-}"
target_dir="${2:-}"

if [[ -z "${lock_file}" || -z "${target_dir}" || $# -ne 2 ]]; then
  echo "Usage: install-home-baseline-reference.sh LOCK_FILE TARGET_DIR" >&2
  exit 2
fi

if [[ ! -f "${lock_file}" ]]; then
  echo "Home-baseline lock file not found: ${lock_file}" >&2
  exit 1
fi

if [[ -e "${target_dir}" ]]; then
  echo "Home-baseline target already exists: ${target_dir}" >&2
  exit 1
fi

# DE: Ein Commit-Pin ist kein erfundenes Release. Beide Modi binden den
# geladenen Git-Baum an den exakten Hash; unbekannte Verträge bleiben gesperrt.
# EN: A commit pin is not a fabricated release. Both modes bind the fetched
# Git tree to its exact hash; unknown contracts remain blocked.
jq -e '
  type == "object" and
  (.source | type == "string") and (.commit | type == "string") and
  (.license | type == "string") and
  ((.schemaVersion == 1 and (.tag | type == "string") and
    (keys == ["commit", "license", "schemaVersion", "source", "tag"])) or
   (.schemaVersion == 2 and .refType == "commit" and
    (keys == ["commit", "license", "refType", "schemaVersion", "source"])))
' "${lock_file}" >/dev/null || { echo "Invalid home-baseline lock contract" >&2; exit 1; }
source_url="$(jq -er '.source' "${lock_file}")"
release_tag="$(jq -r '.tag // empty' "${lock_file}")"
expected_commit="$(jq -er '.commit' "${lock_file}")"
license_id="$(jq -er '.license' "${lock_file}")"

if [[ "${source_url}" != "https://github.com/hindermath/home-baseline.git" ]]; then
  echo "Unexpected home-baseline source: ${source_url}" >&2
  exit 1
fi
if [[ "$(jq -r '.schemaVersion' "${lock_file}")" == "1" && ! "${release_tag}" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Invalid home-baseline release tag: ${release_tag}" >&2
  exit 1
fi
if [[ ! "${expected_commit}" =~ ^[0-9a-f]{40}$ ]]; then
  echo "Invalid home-baseline commit: ${expected_commit}" >&2
  exit 1
fi
if [[ "${license_id}" != "MIT" ]]; then
  echo "Unexpected home-baseline license: ${license_id}" >&2
  exit 1
fi

tmp_dir="$(mktemp -d)"
cleanup() {
  rm -rf "${tmp_dir}"
}
trap cleanup EXIT

checkout_dir="${tmp_dir}/home-baseline"
git init --quiet "${checkout_dir}"
git -C "${checkout_dir}" remote add upstream "${source_url}"
fetch_ref="${expected_commit}"
if [[ -n "${release_tag}" ]]; then
  fetch_ref="refs/tags/${release_tag}"
fi
git -C "${checkout_dir}" fetch --quiet --depth=1 --no-tags upstream "${fetch_ref}"

resolved_commit="$(git -C "${checkout_dir}" rev-parse 'FETCH_HEAD^{commit}')"
if [[ "${resolved_commit}" != "${expected_commit}" ]]; then
  echo "home-baseline ref/commit mismatch: ${fetch_ref} resolves to ${resolved_commit}, expected ${expected_commit}" >&2
  exit 1
fi

git -C "${checkout_dir}" checkout --quiet --detach "${expected_commit}"
git -C "${checkout_dir}" config advice.detachedHead false

test -f "${checkout_dir}/LICENSE"
test -f "${checkout_dir}/docs/learning-units/START-HERE-FUER-LERNENDE.md"

mkdir -p "$(dirname "${target_dir}")"
mv "${checkout_dir}" "${target_dir}"
chown -R root:root "${target_dir}"
chmod -R a-w "${target_dir}"
git config --system --add safe.directory "${target_dir}"

printf 'Installed home-baseline %s at %s\n' "${release_tag:-commit-pin}" "${expected_commit}"
