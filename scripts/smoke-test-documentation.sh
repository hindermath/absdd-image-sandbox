#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
fixture_dir="${script_dir}/tests/fixtures/documentation-toolchain"
work_dir="$(mktemp -d "${TMPDIR:-/tmp}/ade-documentation.XXXXXX")"
trap 'rm -rf "${work_dir}"' EXIT

for tool in pandoc lychee typst tinymist; do
  "${tool}" --version
done
cp "${fixture_dir}/technical-documentation.md" "${fixture_dir}/reference.md" "${work_dir}/"
cd "${work_dir}"
lychee --offline --no-progress technical-documentation.md
printf '[Missing reference](missing.md)\n' >broken.md
if lychee --offline --no-progress broken.md; then
  printf '%s\n' 'FAIL: Lychee accepted a missing local link.' >&2
  exit 1
fi
pandoc technical-documentation.md --from=markdown --to=typst --standalone \
  --variable=mainfont:'DejaVu Sans' --variable=monofont:'DejaVu Sans Mono' \
  --output=technical-documentation.typ
test -s technical-documentation.typ
typst compile --root "${work_dir}" technical-documentation.typ technical-documentation.pdf
pdfinfo technical-documentation.pdf >pdf-info.txt
awk '/^Pages:/ { found = ($2 >= 1) } END { exit !found }' pdf-info.txt
pdftotext -layout technical-documentation.pdf extracted.txt
for expected in 'Technische Dokumentation' 'Technical Documentation' 'ARM64' 'AMD64' 'printf' 'Größe'; do
  grep -F -- "${expected}" extracted.txt >/dev/null
done
printf '%s\n' 'PASS: Markdown -> Pandoc -> Typst -> PDF; content and offline links checked.'
printf '%s\n' 'DE: Funktionstest; PDF-Barrierefreiheit wurde nicht bewertet.' \
  'EN: Functional check; PDF accessibility was not assessed.'
