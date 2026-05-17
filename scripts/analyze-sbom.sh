#!/usr/bin/env bash
set -euo pipefail

SBOM_PATH=""
SEARCH=""
COMPONENT_TYPE=""
TOP=20
SCAN="false"
SCANNER="auto"

usage() {
  cat <<'USAGE'
Usage: scripts/analyze-sbom.sh [options]

Summarize a CycloneDX JSON SBOM and optionally run a vulnerability scan.

Options:
  --file PATH      SBOM file to analyze. Defaults to newest sboms/*.cdx.json.
  --search REGEX   Search component name, version, and purl.
  --type TYPE      Restrict summary and search to a component type.
  --top N          Number of grouped rows to show. Default: 20.
  --scan           Run grype or trivy against the SBOM when available.
  --scanner NAME   Scanner: auto, grype, or trivy.
  -h, --help       Show this help.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --file)
      SBOM_PATH="$2"
      shift 2
      ;;
    --search)
      SEARCH="$2"
      shift 2
      ;;
    --type)
      COMPONENT_TYPE="$2"
      shift 2
      ;;
    --top)
      TOP="$2"
      shift 2
      ;;
    --scan)
      SCAN="true"
      shift
      ;;
    --scanner)
      SCANNER="$2"
      shift 2
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

if [[ -z "${SBOM_PATH}" ]]; then
  shopt -s nullglob
  sbom_files=(sboms/*.cdx.json)
  shopt -u nullglob
  if [[ ${#sbom_files[@]} -eq 0 ]]; then
    echo "No SBOM found. Generate one with ./scripts/build-and-sbom.sh first." >&2
    exit 1
  fi
  SBOM_PATH="$(ls -t "${sbom_files[@]}" | head -n 1)"
fi

if [[ ! -s "${SBOM_PATH}" ]]; then
  echo "SBOM does not exist or is empty: ${SBOM_PATH}" >&2
  exit 1
fi

if command -v jq >/dev/null 2>&1; then
  echo "SBOM: ${SBOM_PATH}"
  jq -r '"Format: \(.bomFormat) \(.specVersion)",
         "Generated: \(.metadata.timestamp // "<unknown>")",
         "Components: \((.components // []) | length)",
         "Tools: \((.metadata.tools.components // []) | map((.name // "") + " " + (.version // "")) | join(", "))",
         "Target: \(.metadata.component.name // "<unknown>") \(.metadata.component.version // "")"' "${SBOM_PATH}"
  if [[ -n "${COMPONENT_TYPE}" ]]; then
    jq -r --arg type "${COMPONENT_TYPE}" '"Filtered components: \(([.components[]? | select((.type // "") == $type)] | length)) type=\($type)"' "${SBOM_PATH}"
  fi

  echo
  echo "Component types:"
  jq -r --arg type "${COMPONENT_TYPE}" '(.components // [])[] | select($type == "" or (.type // "") == $type) | .type // "<none>"' "${SBOM_PATH}" |
    sort |
    uniq -c |
    sort -nr |
    head -n "${TOP}"

  echo
  echo "Package ecosystems from purl:"
  jq -r --arg type "${COMPONENT_TYPE}" '(.components // [])[] | select($type == "" or (.type // "") == $type) | .purl // "" | if test("^pkg:[^/]+/") then capture("^pkg:(?<type>[^/]+)/").type else "<none>" end' "${SBOM_PATH}" |
    sort |
    uniq -c |
    sort -nr |
    head -n "${TOP}"

  echo
  echo "Licenses:"
  jq -r --arg type "${COMPONENT_TYPE}" '
    (.components // [])[] |
    select($type == "" or (.type // "") == $type) |
    if (.licenses // [] | length) == 0 then
      "<none>"
    else
      (.licenses[] | .license.id // .license.name // .expression // "<none>")
    end
  ' "${SBOM_PATH}" |
    sort |
    uniq -c |
    sort -nr |
    head -n "${TOP}"

  if [[ -n "${SEARCH}" ]]; then
    echo
    echo "Search results for '${SEARCH}':"
    jq -r --arg re "${SEARCH}" --arg type "${COMPONENT_TYPE}" '
      (.components // [])[] |
      select($type == "" or (.type // "") == $type) |
      select((.name // "" | test($re; "i")) or
             (.version // "" | test($re; "i")) or
             (.purl // "" | test($re; "i"))) |
      [.type, .name, (.version // ""), (.purl // "")] | @tsv
    ' "${SBOM_PATH}" |
      head -n 100
  fi
else
  python_bin="$(command -v python3 || command -v python || true)"
  if [[ -z "${python_bin}" ]]; then
    echo "jq or python3/python is required for local SBOM summaries." >&2
    exit 1
  fi

  "${python_bin}" - "${SBOM_PATH}" "${TOP}" "${SEARCH}" "${COMPONENT_TYPE}" <<'PY'
import json
import re
import sys
from collections import Counter

path = sys.argv[1]
top = int(sys.argv[2])
search = sys.argv[3]
component_type = sys.argv[4]

with open(path, "r", encoding="utf-8") as handle:
    sbom = json.load(handle)

all_components = sbom.get("components") or []
components = [component for component in all_components if not component_type or component.get("type") == component_type]
metadata = sbom.get("metadata") or {}
tools = metadata.get("tools") or {}
tool_names = []
for tool in tools.get("components") or []:
    name = tool.get("name") or ""
    version = tool.get("version") or ""
    label = f"{name} {version}".strip()
    if label:
        tool_names.append(label)

target = metadata.get("component") or {}

print(f"SBOM: {path}")
print(f"Format: {sbom.get('bomFormat', '<unknown>')} {sbom.get('specVersion', '')}".strip())
print(f"Generated: {metadata.get('timestamp', '<unknown>')}")
print(f"Components: {len(all_components)}")
if component_type:
    print(f"Filtered components: {len(components)} type={component_type}")
if tool_names:
    print(f"Tools: {', '.join(tool_names)}")
print(f"Target: {target.get('name', '<unknown>')} {target.get('version', '')}".strip())

def purl_type(purl):
    match = re.match(r"^pkg:([^/]+)/", purl or "")
    return match.group(1) if match else "<none>"

def licenses(component):
    entries = component.get("licenses") or []
    if not entries:
        return ["<none>"]
    names = []
    for entry in entries:
        license_obj = entry.get("license") or {}
        names.append(license_obj.get("id") or license_obj.get("name") or entry.get("expression") or "<none>")
    return names

def print_counter(title, values):
    print()
    print(title)
    for value, count in Counter(values).most_common(top):
        print(f"{count:7d} {value}")

print_counter("Component types:", [(component.get("type") or "<none>") for component in components])
print_counter("Package ecosystems from purl:", [purl_type(component.get("purl")) for component in components])
print_counter("Licenses:", [name for component in components for name in licenses(component)])

if search:
    pattern = re.compile(search, re.IGNORECASE)
    print()
    print(f"Search results for '{search}':")
    shown = 0
    for component in components:
        fields = [
            component.get("name") or "",
            component.get("version") or "",
            component.get("purl") or "",
        ]
        if any(pattern.search(field) for field in fields):
            print("\t".join([
                component.get("type") or "",
                component.get("name") or "",
                component.get("version") or "",
                component.get("purl") or "",
            ]))
            shown += 1
            if shown >= 100:
                break
PY
fi

if [[ "${SCAN}" == "true" ]]; then
  echo
  case "${SCANNER}" in
    auto)
      if command -v grype >/dev/null 2>&1; then
        echo "Vulnerability scan with grype:"
        grype "${SBOM_PATH}"
      elif command -v trivy >/dev/null 2>&1; then
        echo "Vulnerability scan with trivy:"
        trivy sbom "${SBOM_PATH}"
      else
        echo "No vulnerability scanner found. Install grype or trivy, then rerun with --scan." >&2
        exit 1
      fi
      ;;
    grype)
      echo "Vulnerability scan with grype:"
      grype "${SBOM_PATH}"
      ;;
    trivy)
      echo "Vulnerability scan with trivy:"
      trivy sbom "${SBOM_PATH}"
      ;;
    *)
      echo "Unknown scanner: ${SCANNER}" >&2
      exit 2
      ;;
  esac
fi
