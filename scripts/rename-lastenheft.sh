#!/usr/bin/env bash
# Rename a completed Lastenheft with its feature identifier.

set -euo pipefail

dry_run=false
if [[ "${1:-}" == "--dry-run" ]]; then
	dry_run=true
	shift
fi
if [[ "${1:-}" == "--" ]]; then
	shift
fi

if [[ "$#" -ne 2 ]]; then
	printf 'Fehler: Verwendung: %s [--dry-run] [--] <Lastenheft> <Feature-Name>\n' "$0" >&2
	printf 'Error: Usage: %s [--dry-run] [--] <requirements-file> <feature-name>\n' "$0" >&2
	exit 2
fi

source_path=$1
feature_name=$2

if [[ ! -f "$source_path" ]]; then
	printf 'Fehler: Datei nicht gefunden: %s\n' "$source_path" >&2
	printf 'Error: File not found: %s\n' "$source_path" >&2
	exit 2
fi
if [[ "$source_path" != *.md ]]; then
	printf 'Fehler: Lastenheft muss eine Markdown-Datei sein: %s\n' "$source_path" >&2
	printf 'Error: Requirements file must be Markdown: %s\n' "$source_path" >&2
	exit 2
fi
if [[ ! "$feature_name" =~ ^[A-Za-z0-9][A-Za-z0-9._-]*$ ]]; then
	printf 'Fehler: Ungueltiger Feature-Name: %s\n' "$feature_name" >&2
	printf 'Error: Invalid feature name: %s\n' "$feature_name" >&2
	exit 2
fi

directory=$(dirname -- "$source_path")
filename=$(basename -- "$source_path")
stem=${filename%.md}
target_path="${directory}/${stem}.${feature_name}.md"

if [[ -e "$target_path" && "$target_path" != "$source_path" ]]; then
	printf 'Fehler: Zieldatei existiert bereits: %s\n' "$target_path" >&2
	printf 'Error: Target file already exists: %s\n' "$target_path" >&2
	exit 2
fi

if [[ "$dry_run" == true ]]; then
	printf 'Vorschau: %s -> %s\n' "$source_path" "$target_path"
	printf 'Preview: %s -> %s\n' "$source_path" "$target_path"
	exit 0
fi

git mv -- "$source_path" "$target_path"
printf 'Umbenannt: %s -> %s\n' "$source_path" "$target_path"
printf 'Renamed: %s -> %s\n' "$source_path" "$target_path"
