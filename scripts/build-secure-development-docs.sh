#!/usr/bin/env bash
# Build and validate generated secure-development documentation.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DOC_ROOT="$REPO_ROOT/docs/secure-development"
MANIFEST="$DOC_ROOT/baseline-manifest.json"
HEADER_TEMPLATE="$SCRIPT_DIR/templates/secure-development-compendium-header.md"
CHECK_ONLY=false

usage() {
  cat <<'EOF'
build-secure-development-docs.sh - build and validate the secure-development compendium

Usage:
  bash scripts/build-secure-development-docs.sh [--check]

Options:
  --check   Validate that generated files are current without changing them.
  -h        Show this help.
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --check) CHECK_ONLY=true; shift ;;
    -h|--help) usage; exit 0 ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; exit 2 ;;
  esac
done

command -v jq >/dev/null 2>&1 || { printf 'jq is required.\n' >&2; exit 1; }
[ -f "$MANIFEST" ] || { printf 'Manifest missing: %s\n' "$MANIFEST" >&2; exit 1; }
[ -f "$HEADER_TEMPLATE" ] || { printf 'Header template missing: %s\n' "$HEADER_TEMPLATE" >&2; exit 1; }
jq -e '.schemaVersion == 1 and (.checklists | length) == 12' "$MANIFEST" >/dev/null

baseline_version="$(jq -r '.baselineVersion' "$MANIFEST")"
# DE: Nur der erste zusammenhaengende Metadatenblock ist aktiv. Ein Treffer im
# Text oder ein zweiter Header darf einen veralteten aktiven Wert nicht verdecken.
# EN: Only the first contiguous metadata block is active. Body matches and
# duplicate fields must never hide a stale active value.
check_document_metadata() {
  local relative="$1" prefix="$2" value="$3"
  [ -f "$DOC_ROOT/$relative" ] || { printf 'Controlled document missing: %s\n' "$relative" >&2; exit 1; }
  awk -v prefix="$prefix" -v expected="$prefix $value" '
    { sub(/\r$/, "") }
    !started && /^\*\*[^*]+:\*\*/ { started = 1; active = 1 }
    started && $0 !~ /^\*\*[^*]+:\*\*/ { active = 0 }
    index($0, prefix) == 1 { count++; if (active && $0 == expected) matched++ }
    END { exit !(count == 1 && matched == 1) }
  ' "$DOC_ROOT/$relative" || {
    printf 'Active metadata mismatch or duplicate: %s (%s)\n' "$relative" "$prefix" >&2; exit 1;
  }
}
metadata_files=("README.md")
while IFS= read -r relative; do metadata_files+=("$relative"); done < <(
  jq -r '(.checklists + .relatedDocuments + .learningDocuments)[].path' "$MANIFEST")
for relative in "${metadata_files[@]}"; do
  check_document_metadata "$relative" '**Baseline-Version / Baseline version:**' "$baseline_version"
done
actual_checklist_ids="$(jq -r '.checklists[].id' "$MANIFEST" | LC_ALL=C sort)"
expected_checklist_ids="$(printf 'CL-%02d\n' {1..12})"
[ "$actual_checklist_ids" = "$expected_checklist_ids" ] || { printf 'Expected unique checklist IDs CL-01..CL-12.\n' >&2; exit 1; }
[ "$(jq -r '.guideline.version' "$MANIFEST")" = "$baseline_version" ] || { printf 'Guideline/baseline version mismatch.\n' >&2; exit 1; }
alignment="$DOC_ROOT/mitgeltende-dokumente/Verzahnung_Richtlinie_Checklisten_Spec-Kit-Presets.md"
while IFS= read -r profile; do
  grep -Fq "\`$profile\`" "$alignment" || { printf 'Profile missing from alignment: %s\n' "$profile" >&2; exit 1; }
done < <(jq -r '.profiles | keys[] | select(. != "none")' "$SCRIPT_DIR/config/spec-kit-preset-profiles.json")

compendium_version="$(jq -r '.compendium.version' "$MANIFEST")"
release_date="$(jq -r '.releaseDate' "$MANIFEST")"
expected_item_count="$(jq -r '.checklistItemCount' "$MANIFEST")"
output="$DOC_ROOT/$(jq -r '.compendium.path' "$MANIFEST")"
tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

guideline_path="$(jq -r '.guideline.path' "$MANIFEST")"
guideline_version="$(jq -r '.guideline.version' "$MANIFEST")"
[ -f "$DOC_ROOT/$guideline_path" ] || { printf 'Guideline missing: %s\n' "$guideline_path" >&2; exit 1; }
# DE: Beide Sprachfassungen haben genau eine aktive Metadatentabelle. Historien
# bleiben erlaubt; passende Tabellenzeilen im Fliesstext sind keine Metadaten.
# EN: Each language has exactly one active metadata table. History remains valid;
# matching table rows in the body cannot substitute for active metadata.
check_guideline_metadata() {
  local heading="$1" field="$2"
  awk -v heading="$heading" -v field="$field" -v version="$guideline_version" '
    { sub(/\r$/, "") }
    /^## / { active = ($0 == heading); if (active) sections++; table = 0; ended = 0 }
    active && /^\|/ && !ended { table = 1 }
    active && table && $0 !~ /^\|/ { ended = 1 }
    index($0, "| " field " |") == 1 && split($0, cells, "[|]") == 4 {
      count++; if (active && table && !ended && $0 == "| " field " | " version " |") matched++
    }
    END { exit !(sections == 1 && count == 1 && matched == 1) }
  ' "$DOC_ROOT/$guideline_path" || {
    printf 'Active guideline metadata mismatch or duplicate: %s (%s)\n' "$guideline_path" "$field" >&2; exit 1;
  }
}
check_guideline_metadata '## Dokumenten-Metadaten' 'Versionsnummer'
check_guideline_metadata '## Document Metadata' 'Version'

while IFS=$'\t' read -r relative version; do
  [ -f "$DOC_ROOT/$relative" ] || { printf 'Controlled document missing: %s\n' "$relative" >&2; exit 1; }
  check_document_metadata "$relative" '**Version / Version:**' "$version"
done < <(jq -r '(.relatedDocuments + .learningDocuments)[] | [.path, .version] | @tsv' "$MANIFEST")

while IFS= read -r relative; do
  [ -f "$DOC_ROOT/$relative" ] || { printf 'Managed reference missing: %s\n' "$relative" >&2; exit 1; }
done < <(jq -r '(.managedBinaryFiles + .managedReferenceFiles)[]' "$MANIFEST")

sed \
  -e "s/{{BASELINE_VERSION}}/$baseline_version/g" \
  -e "s/{{COMPENDIUM_VERSION}}/$compendium_version/g" \
  -e "s/{{RELEASE_DATE}}/$release_date/g" \
  "$HEADER_TEMPLATE" > "$tmp"
header_content="$(cat "$tmp")"
printf '%s\n' "$header_content" > "$tmp"

ids_tmp="$(mktemp)"
trap 'rm -f "$tmp" "$ids_tmp"' EXIT

while IFS=$'\t' read -r id relative version; do
  source_file="$DOC_ROOT/$relative"
  [ -f "$source_file" ] || { printf 'Checklist missing: %s\n' "$relative" >&2; exit 1; }
  check_document_metadata "$relative" '**Dokument-ID / Document ID:**' "$id"
  check_document_metadata "$relative" '**Version / Version:**' "$version"
  grep -Eo '^#### CL-[0-9]{2}-[0-9]{2}:' "$source_file" | sed 's/^#### //; s/:$//' >> "$ids_tmp"

  printf '\n---\n\n' >> "$tmp"
  sed \
    -e 's#](../Richtlinie_Sichere-Entwicklung.md#](Richtlinie_Sichere-Entwicklung.md#g' \
    -e 's#](../../../constitution.md#](../../constitution.md#g' \
    -e 's#](../README.md#](README.md#g' \
    -e 's#](../mitgeltende-dokumente/#](mitgeltende-dokumente/#g' \
    -e 's#](../../maintenance/#](../maintenance/#g' \
    -e 's#](CL_#](checklisten/CL_#g' \
    "$source_file" >> "$tmp"
done < <(jq -r '.checklists[] | [.id, .path, .version] | @tsv' "$MANIFEST")

duplicate_ids="$(sort "$ids_tmp" | uniq -d)"
[ -z "$duplicate_ids" ] || { printf 'Duplicate checklist IDs:\n%s\n' "$duplicate_ids" >&2; exit 1; }
actual_item_count="$(wc -l < "$ids_tmp" | tr -d ' ')"
[ "$actual_item_count" -eq "$expected_item_count" ] || {
  printf 'Expected %s checklist items, found %s.\n' "$expected_item_count" "$actual_item_count" >&2
  exit 1
}

cat >> "$tmp" <<EOF

---

## Versionshistorie / Version History

| Version | Datum / Date | Änderung / Change |
|---|---|---|
| $compendium_version | $release_date | Aus den zwölf kanonischen Einzelchecklisten der sicheren-Entwicklung-Basis $baseline_version erzeugt; einheitliches zweiachsiges Statusmodell und klare Trennung zwischen Vorlage und Projektnachweis. / Generated from the twelve canonical individual checklists of secure-development baseline $baseline_version; unified two-axis status model and clear separation between template and project evidence. |
EOF

if $CHECK_ONLY; then
  cmp -s "$tmp" "$output" || { printf 'Generated compendium is stale: %s\n' "$output" >&2; exit 1; }
  printf 'Secure-development generated documents are current.\n'
else
  cp "$tmp" "$output"
  printf 'Generated %s\n' "$output"
fi
