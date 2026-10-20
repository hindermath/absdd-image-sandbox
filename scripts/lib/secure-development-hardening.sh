#!/usr/bin/env bash
# Shared helpers for secure-development hardening intake preparation.

SDH_PREPARE_RESULT=""
SDH_PREPARE_REASON=""
SDH_DETECTED_LANGUAGE=""

sdh_diagnostic_remediation() {
  case "$1" in
    LIE001) printf '%s' 'Datei als gueltiges UTF-8 ohne NUL speichern und erneut pruefen / Save the file as valid UTF-8 without NUL and check again.' ;;
    LIE002) printf '%s' 'Schema und Pflichtfelder in der kanonischen Quelle korrigieren / Correct the schema and required fields in the canonical source.' ;;
    LIE003) printf '%s' 'Repository-relativen Pfad ohne Traversal oder Optionskomponente verwenden / Use a repository-relative path without traversal or option components.' ;;
    LIE004) printf '%s' 'Kanonischen relativen Pfad und erwarteten Typ pruefen / Check the canonical relative path and expected type.' ;;
    LIE005) printf '%s' 'Symlink und physische Pfadauflosung innerhalb des Repositorys korrigieren / Correct the symlink and physical path resolution inside the repository.' ;;
    LIE006) printf '%s' 'Kanonische Identitaeten und Positionen eindeutig machen / Make canonical identities and positions unique.' ;;
    LIE007) printf '%s' 'From, To, Kind und Binding einzeln mit dem Manifest abgleichen / Compare from, to, kind, and binding individually with the manifest.' ;;
    LIE008) printf '%s' 'Genau einen expliziten vorhandenen Feature-Nachweis bereitstellen / Provide exactly one explicit existing feature proof.' ;;
    LIE009) printf '%s' 'Kanonische Quelle pruefen und den begrenzten Schreibmodus ausfuehren / Review the canonical source and run the bounded write mode.' ;;
    LIE010) printf '%s' 'Fehlerursache beheben und die vollstaendige Transaktion erneut ausfuehren / Fix the cause and run the complete transaction again.' ;;
    LIE011) printf '%s' 'Beide Ausgaben aus derselben typisierten Projektion regenerieren / Regenerate both outputs from the same typed projection.' ;;
    LIE012) printf '%s' 'Gemeinsame Fixtures, Exitklasse, Diagnose und Ausgabebytes vergleichen / Compare shared fixtures, exit class, diagnostic, and output bytes.' ;;
    *) printf '%s' 'Sicheren relativen Eingabekontext pruefen und den Befehl erneut ausfuehren / Check the safe relative input context and run the command again.' ;;
  esac
}

sdh_redact_public_diagnostic() {
  local message="$1"
  # Diagnostics are a trust boundary too: one physical line prevents terminal
  # control injection, while credential-shaped values and private home roots
  # are removed without hiding an ordinary repository-relative subject.
  printf '%s' "$message" \
    | LC_ALL=C tr '\001-\037\177' '?' \
    | sed -E \
      -e 's#(/Users/|/home/)[^[:space:]:;,]+#[private-path]#g' \
      -e 's#([Tt][Oo][Kk][Ee][Nn]|[Pp][Aa][Ss][Ss][Ww][Oo][Rr][Dd]|[Ss][Ee][Cc][Rr][Ee][Tt]|[Aa][Uu][Tt][Hh][Oo][Rr][Ii][Zz][Aa][Tt][Ii][Oo][Nn]|[Aa][Pp][Ii][_-]?[Kk][Ee][Yy])[[:space:]]*[:=][[:space:]]*[^[:space:];,]+#\1=[redacted]#g'
}

sdh_log() {
  local message="$*"
  local code remediation
  case "$message" in
    LIE[0-9][0-9][0-9]:*)
      message="$(sdh_redact_public_diagnostic "$message")"
      code="${message%%:*}"
      remediation="$(sdh_diagnostic_remediation "$code")"
      message="${message}; Abhilfe / remediation: ${remediation}"
      ;;
  esac
  printf '%s\n' "$message"
}

sdh_jq() {
  # Native jq on Windows otherwise translates output to CRLF. Binary mode
  # keeps structured values byte-stable without masking embedded CR input.
  case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*) command jq -b "$@" ;;
    *) command jq "$@" ;;
  esac
}

sdh_sha256_file() {
  local file="$1"
  if command -v sha256sum >/dev/null 2>&1; then
    command sha256sum -- "$file" | sdh_normalize_sha256_output
  elif command -v shasum >/dev/null 2>&1; then
    command shasum -a 256 -- "$file" | sdh_normalize_sha256_output
  else
    sdh_log 'LIE002: SHA-256-Werkzeug fehlt / SHA-256 tool is missing' >&2
    return 1
  fi
}

sdh_normalize_sha256_output() {
  # GNU coreutils prefixes a checksum line with "\" when an input filename
  # needs escaping, which is common for RUNNER_TEMP paths under Git Bash.
  # The marker describes the filename field and is not part of the digest.
  awk '{
    digest = $1
    sub(/^\\/, "", digest)
    if (length(digest) != 64 || digest ~ /[^0-9A-Fa-f]/) {
      exit 1
    }
    print tolower(digest)
  }'
}

sdh_sha256_stream() {
  if command -v sha256sum >/dev/null 2>&1; then
    command sha256sum | sdh_normalize_sha256_output
  elif command -v shasum >/dev/null 2>&1; then
    command shasum -a 256 | sdh_normalize_sha256_output
  else
    sdh_log 'LIE002: SHA-256-Werkzeug fehlt / SHA-256 tool is missing' >&2
    return 1
  fi
}

sdh_create_test_file_symlink() {
  local target="$1"
  local link="$2"
  local windows_target windows_link

  case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*)
      command -v cygpath >/dev/null 2>&1 || return 1
      command -v pwsh >/dev/null 2>&1 || return 1
      windows_target="$(cygpath -w -- "$target")"
      windows_link="$(cygpath -w -- "$link")"
      SDH_TEST_SYMLINK_TARGET="$windows_target" \
        SDH_TEST_SYMLINK_LINK="$windows_link" \
        pwsh -NoProfile -Command '
        Set-StrictMode -Version Latest
        $ErrorActionPreference = "Stop"
        New-Item -ItemType SymbolicLink -Path $env:SDH_TEST_SYMLINK_LINK -Target $env:SDH_TEST_SYMLINK_TARGET | Out-Null
      '
      ;;
    *) ln -s "$target" "$link" ;;
  esac
}

sdh_normalize_language() {
  printf '%s' "${1:-}" \
    | tr '[:upper:]' '[:lower:]' \
    | sed 's/[[:space:]_+-]\+//g; s#/# #g' \
    | tr -d '.'
}

sdh_is_msl_language() {
  local normalized
  normalized="$(sdh_normalize_language "$1")"
  case "$normalized" in
    csharp|cs|c#|dotnet|net|fsharp|fs|f#|rust|swift|java|kotlin|scala|go|golang|dart|python|py|ruby|javascript|js|typescript|ts|haskell|ocaml|erlang|elixir|ada|spark)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

sdh_is_known_non_msl_language() {
  local normalized
  normalized="$(sdh_normalize_language "$1")"
  case "$normalized" in
    c|cpp|cxx|cplusplus|objectivec|objc|assembly|asm|cc65|zig|nim|d)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

sdh_detect_language_from_constitution() {
  local repo="$1"
  local project_name="$2"
  local file line language

  for file in "$repo/constitution.md" "$repo/.specify/memory/constitution.md"; do
    [ -f "$file" ] || continue
    line="$(awk -F'|' -v project="$project_name" '
      index($0, project) > 0 && NF >= 4 { gsub(/^[ \t]+|[ \t]+$/, "", $3); print $3; exit }
    ' "$file")"
    if [ -n "$line" ]; then
      language="$line"
      case "$language" in
        *C#*|*.NET*|*dotnet*) printf '%s\n' "C#"; return 0 ;;
        *Rust*) printf '%s\n' "Rust"; return 0 ;;
        *Swift*) printf '%s\n' "Swift"; return 0 ;;
        *JavaScript*|*TypeScript*) printf '%s\n' "TypeScript"; return 0 ;;
        *Java*) printf '%s\n' "Java"; return 0 ;;
        *Kotlin*) printf '%s\n' "Kotlin"; return 0 ;;
        *Go*) printf '%s\n' "Go"; return 0 ;;
        *Python*) printf '%s\n' "Python"; return 0 ;;
        *C/C89*|*C89*|*C++*|*Assembly*|*Zig*) printf '%s\n' "$language"; return 0 ;;
      esac
    fi
  done

  return 1
}

sdh_detect_language_from_project_name() {
  local project_name
  project_name="$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')"

  case "$project_name" in
    *-csharp|*_csharp|*.csharp|*-c#|*_c#|*.c#) printf '%s\n' "C#" ;;
    *-fsharp|*_fsharp|*.fsharp|*-f#|*_f#|*.f#) printf '%s\n' "F#" ;;
    *-rust|*_rust|*.rust) printf '%s\n' "Rust" ;;
    *-swift|*_swift|*.swift) printf '%s\n' "Swift" ;;
    *-java|*_java|*.java) printf '%s\n' "Java" ;;
    *-kotlin|*_kotlin|*.kotlin) printf '%s\n' "Kotlin" ;;
    *-go|*_go|*.go) printf '%s\n' "Go" ;;
    *-python|*_python|*.python) printf '%s\n' "Python" ;;
    *-typescript|*_typescript|*.typescript) printf '%s\n' "TypeScript" ;;
    *-javascript|*_javascript|*.javascript) printf '%s\n' "JavaScript" ;;
    *) return 1 ;;
  esac
}

sdh_find_first() {
  local repo="$1"
  shift
  find "$repo" -maxdepth 4 "$@" -print -quit 2>/dev/null
}

sdh_detect_language_from_files() {
  local repo="$1"

  if [ -n "$(sdh_find_first "$repo" \( -name '*.sln' -o -name '*.csproj' -o -name '*.fsproj' \))" ]; then
    printf '%s\n' "C#"
  elif [ -f "$repo/Cargo.toml" ] || [ -n "$(sdh_find_first "$repo" -name Cargo.toml)" ]; then
    printf '%s\n' "Rust"
  elif [ -f "$repo/go.mod" ] || [ -n "$(sdh_find_first "$repo" -name go.mod)" ]; then
    printf '%s\n' "Go"
  elif [ -f "$repo/Package.swift" ] || [ -n "$(sdh_find_first "$repo" -name Package.swift)" ]; then
    printf '%s\n' "Swift"
  elif [ -f "$repo/tsconfig.json" ] || [ -n "$(sdh_find_first "$repo" -name tsconfig.json)" ]; then
    printf '%s\n' "TypeScript"
  elif [ -f "$repo/package.json" ] || [ -n "$(sdh_find_first "$repo" -name package.json)" ]; then
    printf '%s\n' "JavaScript"
  elif [ -f "$repo/pyproject.toml" ] || [ -n "$(sdh_find_first "$repo" -name pyproject.toml)" ]; then
    printf '%s\n' "Python"
  elif [ -n "$(sdh_find_first "$repo" \( -name 'pom.xml' -o -name 'build.gradle' -o -name 'build.gradle.kts' \))" ]; then
    printf '%s\n' "Java"
  else
    return 1
  fi
}

sdh_detect_language() {
  local repo="$1"
  local project_name="$2"
  local explicit_language="${3:-}"
  local detected=""

  if [ -n "$explicit_language" ]; then
    printf '%s\n' "$explicit_language"
    return 0
  fi

  detected="$(sdh_detect_language_from_constitution "$repo" "$project_name" 2>/dev/null || true)"
  if [ -n "$detected" ]; then
    printf '%s\n' "$detected"
    return 0
  fi

  detected="$(sdh_detect_language_from_project_name "$project_name" 2>/dev/null || true)"
  if [ -n "$detected" ]; then
    printf '%s\n' "$detected"
    return 0
  fi

  detected="$(sdh_detect_language_from_files "$repo" 2>/dev/null || true)"
  if [ -n "$detected" ]; then
    printf '%s\n' "$detected"
    return 0
  fi

  return 1
}

sdh_find_source_dir() {
  local script_dir="$1"
  local repo_dir
  repo_dir="$(cd "$script_dir/.." 2>/dev/null && pwd)"

  for candidate in \
    "$repo_dir/docs/secure-development" \
    "$HOME/docs/secure-development" \
    "$HOME/home-baseline-source/docs/secure-development"; do
    if [ -d "$candidate" ] \
      && [ -f "$candidate/README.md" ] \
      && [ -f "$candidate/mitgeltende-dokumente/README.md" ]; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done

  return 1
}

sdh_manifest_paths() {
  local manifest="$1"
  sdh_jq -r '
    ["baseline-manifest.json", .guideline.path, .compendium.path]
    + [.checklists[].path]
    + [.relatedDocuments[].path]
    + [.learningDocuments[].path]
    + .managedBinaryFiles
    + .managedReferenceFiles
    | unique[]
  ' "$manifest"
}

sdh_sync_baseline() {
  local source_dir="$1"
  local target_dir="$2"
  local dry_run="${3:-0}"
  local source_manifest="$source_dir/baseline-manifest.json"
  local target_manifest="$target_dir/baseline-manifest.json"
  local new_paths old_paths relative source_file target_file copied=0 removed=0

  command -v jq >/dev/null 2>&1 || { sdh_log "  Fehler: jq wird fuer die manifestgesteuerte Synchronisation benoetigt"; return 1; }
  [ -f "$source_manifest" ] || { sdh_log "  Fehler: Baseline-Manifest fehlt: $source_manifest"; return 1; }
  new_paths="$(mktemp)"
  old_paths="$(mktemp)"
  sdh_manifest_paths "$source_manifest" > "$new_paths"
  if [ -f "$target_manifest" ]; then
    sdh_manifest_paths "$target_manifest" > "$old_paths"
  else
    : > "$old_paths"
  fi

  while IFS= read -r relative; do
    [ -n "$relative" ] || continue
    case "$relative" in /*|*../*) sdh_log "  Fehler: unsicherer Manifestpfad: $relative"; rm -f "$new_paths" "$old_paths"; return 1 ;; esac
    if ! grep -Fqx "$relative" "$new_paths"; then
      target_file="$target_dir/$relative"
      if [ -f "$target_file" ]; then
        removed=$((removed + 1))
        [ "$dry_run" = "1" ] || rm -f "$target_file"
      fi
    fi
  done < "$old_paths"

  while IFS= read -r relative; do
    [ -n "$relative" ] || continue
    case "$relative" in /*|*../*) sdh_log "  Fehler: unsicherer Manifestpfad: $relative"; rm -f "$new_paths" "$old_paths"; return 1 ;; esac
    source_file="$source_dir/$relative"
    target_file="$target_dir/$relative"
    [ -f "$source_file" ] || { sdh_log "  Fehler: verwaltete Quelldatei fehlt: $relative"; rm -f "$new_paths" "$old_paths"; return 1; }
    if [ ! -f "$target_file" ] || ! cmp -s "$source_file" "$target_file"; then
      copied=$((copied + 1))
      if [ "$dry_run" != "1" ] && [ "$relative" != "baseline-manifest.json" ]; then
        mkdir -p "$(dirname "$target_file")"
        cp "$source_file" "$target_file"
      fi
    fi
  done < "$new_paths"

  if [ "$dry_run" != "1" ]; then
    mkdir -p "$target_dir"
    cp "$source_manifest" "$target_manifest"
    find "$target_dir" -depth -type d -empty -delete 2>/dev/null || true
  fi
  sdh_log "  Baseline-Sync: $copied aktualisiert, $removed veraltet entfernt"
  rm -f "$new_paths" "$old_paths"
}

sdh_find_template_file() {
  local script_dir="$1"
  local repo_dir
  repo_dir="$(cd "$script_dir/.." 2>/dev/null && pwd)"

  for candidate in \
    "$script_dir/templates/secure-development-hardening-lastenheft.md" \
    "$repo_dir/scripts/templates/secure-development-hardening-lastenheft.md" \
    "$HOME/scripts/templates/secure-development-hardening-lastenheft.md" \
    "$HOME/home-baseline-source/scripts/templates/secure-development-hardening-lastenheft.md"; do
    if [ -f "$candidate" ]; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done

  return 1
}

sdh_render_template() {
  local template="$1"
  local output="$2"
  local project_name="$3"
  local today
  today="$(date +%Y-%m-%d)"

  sed \
    -e "s|{{PROJECT_NAME}}|${project_name}|g" \
    -e "s|{{DATE}}|${today}|g" \
    "$template" > "$output"
}

sdh_order_rank() {
  local name
  name="$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')"

  case "$name" in
    *rl-se*checklist*selbstpruefung*|*checklist*selbstpruefung*) printf '%s\n' "45" ;;
    *gsdb*spec-kit*intensivpruefung*|*gsdb*intensiv*) printf '%s\n' "48" ;;
    *secure-development-hardening*) printf '%s\n' "50" ;;
    *constitution*|*governance*|*baseline*|*homogeneity*) printf '%s\n' "10" ;;
    *migration*|*build*|*ci*|*cicd*|*tool*|*terminalgui*|*rename*) printf '%s\n' "20" ;;
    *compiler*|*worker*|*service*|*database*|*db*|*sql*|*mongodb*|*postgres*|*sqlite*|*framework*|*core*|*controls*|*runtime*|*vm*|*clr*|*assembly*|*pl0*|*wave*) printf '%s\n' "30" ;;
    *ui*|*tui*|*ide*|*a11y*|*dokument*|*doc*|*l10n*|*didactic*|*comment*) printf '%s\n' "40" ;;
    *) printf '%s\n' "60" ;;
  esac
}

sdh_order_group() {
  case "$1" in
    10) printf '%s\n' "Governance/Baseline" ;;
    20) printf '%s\n' "Migration/Tooling" ;;
    30) printf '%s\n' "Kernlogik/Runtime" ;;
    40) printf '%s\n' "UI/A11Y/Dokumentation" ;;
    45) printf '%s\n' "RL-SE-/Checklist-Selbstpruefung" ;;
    48) printf '%s\n' "GSDB-Spec-Kit-Intensivpruefung" ;;
    50) printf '%s\n' "Secure-Development-Hardening" ;;
    *)  printf '%s\n' "Weitere Anforderungen" ;;
  esac
}

sdh_build_legacy_order_section() {
  local repo="$1"
  local tmp_items
  local file base rank group status count

  tmp_items="$(mktemp)"
  find "$repo" -maxdepth 1 -type f -name 'Lastenheft*.md' ! -name 'Lastenheft_Abarbeitungsreihenfolge.md' -print \
    | while IFS= read -r file; do
        base="$(basename "$file")"
        rank="$(sdh_order_rank "$base")"
        group="$(sdh_order_group "$rank")"
        status="aktiv / active"
        case "$base" in
          *.[0-9][0-9][0-9]*.md) status="archiviert oder abgeschlossen / archived or completed" ;;
        esac
        printf '%s|%s|%s|%s\n' "$rank" "$base" "$group" "$status"
      done | sort -t '|' -k1,1n -k2,2f > "$tmp_items"

  count="$(wc -l < "$tmp_items" | tr -d ' ')"

  cat <<'EOF'
<!-- secure-development-hardening-order:start -->
## Automatisch ermittelte Lastenheft-Reihenfolge / Automatically Detected Requirements Order

Diese Tabelle wird aus `Lastenheft*.md` im Repository-Root erzeugt. Sie ist eine Vorbereitung fuer spaetere Spec-Kit-Laeufe und startet selbst keinen Lauf. Manuelle Projektentscheidungen ausserhalb dieses markierten Abschnitts bleiben erhalten.

*This table is generated from `Lastenheft*.md` in the repository root. It prepares later Spec Kit runs and does not start a run. Manual project decisions outside this marked section remain preserved.*

| Rang | Lastenheft | Gruppe | Status |
|---:|---|---|---|
EOF

  if [ "$count" = "0" ]; then
    printf '| - | - | Keine Lastenhefte gefunden | - |\n'
  else
    awk -F'|' '{ printf "| %d | `%s` | %s | %s |\n", NR, $2, $3, $4 }' "$tmp_items"
  fi

  cat <<'EOF'
<!-- secure-development-hardening-order:end -->
EOF

  rm -f "$tmp_items"
}

sdh_find_intake_series_manifest() {
  local repo="$1"
  local explicit_manifest="${2:-}"
  local preferred="$repo/requirements/intakes/series/home-baseline-delivery/manifest.json"
  local matches

  if [ -n "$explicit_manifest" ]; then
    sdh_assert_safe_repository_path "$repo" "$explicit_manifest" file || return 1
    printf '%s\n' "$repo/$explicit_manifest"
    return 0
  fi

  if [ -f "$preferred" ]; then
    printf '%s\n' "$preferred"
    return 0
  fi

  matches="$(
    find "$repo/requirements/intakes/series" -mindepth 2 -maxdepth 2 -type f -name manifest.json -print 2>/dev/null || true
    find "$repo/specs/intake-series" -mindepth 2 -maxdepth 2 -type f -name manifest.json -print 2>/dev/null || true
  )"
  [ "$(printf '%s\n' "$matches" | sed '/^$/d' | wc -l | tr -d ' ')" = "1" ] || return 1
  printf '%s\n' "$matches"
}

sdh_assert_safe_repository_path() {
  local repo="$1"
  local relative="$2"
  local expected_type="$3"
  local target resolved_repo resolved_target unsafe_class=""

  case "$relative" in
    "") unsafe_class='empty' ;;
    /*|\\*|[A-Za-z]:*) unsafe_class='absolute' ;;
    ..|../*|*/../*|*/..) unsafe_class='traversal' ;;
    -*|*/-*) unsafe_class='option-component' ;;
    *'\'*) unsafe_class='backslash' ;;
    *$'\n'*|*$'\r'*|*$'\t'*) unsafe_class='control-byte' ;;
  esac
  if [ -n "$unsafe_class" ]; then
      # Rejected path bytes may themselves be credentials or control text, so
      # the public diagnostic preserves the code and remediation, not the data.
    sdh_log "LIE003: unsicherer Repositorypfad / unsafe repository path: [redacted] (class: $unsafe_class)" >&2
    return 1
  fi

  target="$repo/$relative"
  case "$expected_type" in
    file) [ -f "$target" ] || { sdh_log "LIE004: Datei fehlt / file is missing: $relative" >&2; return 1; } ;;
    directory) [ -d "$target" ] || { sdh_log "LIE004: Verzeichnis fehlt / directory is missing: $relative" >&2; return 1; } ;;
    *) return 1 ;;
  esac

  # Git Bash exposes the same Windows path through both an MSYS namespace and
  # a native drive namespace. Resolve both containment operands with the same
  # tool so an in-repository file cannot become a false escape on Windows.
  resolved_repo="$(realpath "$repo")"
  resolved_target="$(realpath "$target")"
  case "$resolved_target" in
    "$resolved_repo"|"$resolved_repo"/*) ;;
    *)
      sdh_log "LIE005: Pfad verlaesst das Repository / path escapes repository: $relative" >&2
      return 1
      ;;
  esac
}

sdh_assert_safe_output_path() {
  local repo="$1"
  local relative="$2"
  local target parent resolved_repo resolved_parent

  case "$relative" in
    ""|/*|\\*|[A-Za-z]:*|..|../*|*/../*|*/..|-*|*/-*|*'\'*|*$'\n'*|*$'\r'*|*$'\t'*)
      sdh_log 'LIE003: unsicherer Ausgabepfad / unsafe output path: [redacted]' >&2
      return 1
      ;;
  esac
  target="$repo/$relative"
  parent="$(dirname "$target")"
  [ -d "$parent" ] || { sdh_log "LIE004: Ausgabe-Elternverzeichnis fehlt / output parent is missing: $(dirname "$relative")" >&2; return 1; }
  [ ! -e "$target" ] || [ -f "$target" ] || { sdh_log "LIE004: Ausgabe hat den falschen Typ / output has the wrong type: $relative" >&2; return 1; }
  [ ! -L "$target" ] || { sdh_log "LIE005: Ausgabe darf kein symbolischer Link sein / output must not be a symbolic link: $relative" >&2; return 1; }
  # Keep repository and parent in one canonical namespace on Git Bash while
  # retaining realpath's physical symlink resolution on every platform.
  resolved_repo="$(realpath "$repo")"
  resolved_parent="$(realpath "$parent")"
  case "$resolved_parent" in
    "$resolved_repo"|"$resolved_repo"/*) ;;
    *) sdh_log "LIE005: Ausgabepfad verlaesst das Repository / output path escapes repository: $relative" >&2; return 1 ;;
  esac
}

sdh_repository_relative_from_absolute_path() {
  local repo="$1"
  local absolute="$2"
  local resolved_repo resolved_absolute relative

  # Discovered paths may use a different Git-Bash namespace than their input.
  # Canonicalize both before stripping the repository prefix; the returned
  # value is safe to pass through the ordinary relative-path validator.
  resolved_repo="$(realpath "$repo")" || return 1
  resolved_absolute="$(realpath "$absolute")" || return 1
  case "$resolved_absolute" in
    "$resolved_repo"/*) relative="${resolved_absolute#"$resolved_repo"/}" ;;
    *)
      sdh_log 'LIE005: ermittelter Pfad verlaesst das Repository / discovered path escapes repository: [redacted]' >&2
      return 1
      ;;
  esac
  # A native Windows realpath may retain backslashes after the common physical
  # prefix has been removed. Repository-relative contracts always use '/'.
  relative="${relative//\\//}"
  printf '%s\n' "$relative"
}

sdh_linked_intake_input_paths() {
  local repo="$1"
  local manifest_relative="$2"
  local intake_path archive_stamp proof_path
  local spec_file state_path

  printf '%s\n' "$manifest_relative"
  sdh_jq -r '.orderedTargets[].path' "$repo/$manifest_relative"
  for spec_file in "$repo"/specs/[0-9][0-9][0-9]-*/spec.md; do
    [ -f "$spec_file" ] || continue
    printf '%s\n' "${spec_file#"$repo/"}"
  done
  while IFS= read -r intake_path; do
    archive_stamp="$(basename "$intake_path" | sed -nE 's/^.*\.([0-9]{3}-[^/]+)\.md$/\1/p')"
    [ -n "$archive_stamp" ] || continue
    state_path="specs/$archive_stamp/autonomous-run-state.json"
    [ ! -f "$repo/$state_path" ] || printf '%s\n' "$state_path"
  done < <(sdh_jq -r '.orderedTargets[].path' "$repo/$manifest_relative")
  while IFS= read -r proof_path; do
    [ -z "$proof_path" ] || printf '%s\n' "$proof_path"
  done < <(sdh_jq -r '(.featureEvidence // [])[].featurePath' "$repo/$manifest_relative")
}

sdh_linked_intake_input_fingerprint() {
  local repo="$1"
  local manifest_relative="$2"
  local relative raw_hash

  while IFS= read -r relative; do
    if [ -f "$repo/$relative" ]; then
      raw_hash="$(sdh_sha256_file "$repo/$relative")"
      printf '%s\0file\0%s\n' "$relative" "$raw_hash"
    elif [ -d "$repo/$relative" ]; then
      printf '%s\0directory\n' "$relative"
    else
      printf '%s\0missing\n' "$relative"
    fi
  done < <(sdh_linked_intake_input_paths "$repo" "$manifest_relative" | LC_ALL=C sort -u) \
    | sdh_sha256_stream
}

sdh_assert_fixture_fault_scope() {
  local repo="$1"
  local resolved_repo resolved_tmp

  [ -f "$repo/.sdh-linked-intake-test-fixture" ] || return 1
  resolved_repo="$(cd "$repo" && pwd -P)"
  resolved_tmp="$(cd "${TMPDIR:-/tmp}" && pwd -P)"
  case "$resolved_repo" in
    "$resolved_tmp"/*) return 0 ;;
    *) return 1 ;;
  esac
}

sdh_assert_strict_utf8_file() {
  local file="$1"
  local subject="$2"

  if LC_ALL=C od -An -tx1 -v "$file" | tr -s ' ' '\n' | grep -Fqx '00'; then
    sdh_log "LIE001: NUL-Inhalt ist unzulaessig / NUL content is not allowed: $subject" >&2
    return 1
  fi
  if ! iconv -f UTF-8 -t UTF-8 "$file" >/dev/null 2>&1; then
    sdh_log "LIE001: ungueltiges UTF-8 / invalid UTF-8: $subject" >&2
    return 1
  fi
}

sdh_markdown_text() {
  # Entity-escape raw HTML in untrusted data. Renderer-owned <br> separators
  # are inserted only after this boundary and therefore remain functional.
  printf '%s' "$1" | sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/\\/\\\\/g; s/|/\\|/g; s/\[/\\[/g; s/\]/\\]/g; s/(/\\(/g; s/)/\\)/g; s/`/\\`/g'
}

sdh_validate_linked_intake_manifest() {
  local repo="$1"
  local manifest_relative="$2"
  local manifest="$repo/$manifest_relative"
  local path root duplicate_count position positions_file target_count index kind from to

  sdh_assert_safe_repository_path "$repo" "$manifest_relative" file || return 1
  sdh_assert_strict_utf8_file "$manifest" "$manifest_relative" || return 1
  sdh_jq -e '
    .schemaVersion == "1.0"
    and .documentType == "IntakeSeriesManifest"
    and (.seriesId | type == "string" and length > 0)
    and (.status | type == "string" and length > 0)
    and (.orderedTargets | type == "array" and length > 0)
    and (.roots | type == "array")
    and (.dependencies | type == "array")
    and all(.orderedTargets[];
      (type == "object")
      and (.path | type == "string" and length > 0)
      and (.role | type == "string" and length > 0)
      and (.status | type == "string" and length > 0))
    and all(.roots[]; type == "string" and length > 0)
    and all(.dependencies[];
      (type == "object")
      and (.from | type == "string" and length > 0)
      and (.to | type == "string" and length > 0)
      and (.kind | type == "string" and length > 0)
      and (.binding | type == "boolean"))
    and ((.featureEvidence // []) | type == "array")
    and all((.featureEvidence // [])[];
      (type == "object")
      and (.intakePath | type == "string" and length > 0)
      and (.featurePath | type == "string" and length > 0)
      and (.proofKind == "ReviewedLegacyMapping")
      and (.reviewed == true))
  ' "$manifest" >/dev/null 2>&1 || {
    sdh_log "LIE002: ungueltiges Series-Manifest / invalid series manifest: $manifest_relative" >&2
    return 1
  }

  duplicate_count="$(sdh_jq '[.orderedTargets[].path] | length - (unique | length)' "$manifest")"
  [ "$duplicate_count" = "0" ] || { sdh_log 'LIE006: doppelte Intake-Identitaet / duplicate intake identity' >&2; return 1; }
  duplicate_count="$(sdh_jq '[.roots[]] | length - (unique | length)' "$manifest")"
  [ "$duplicate_count" = "0" ] || { sdh_log 'LIE006: doppelte Root-Identitaet / duplicate root identity' >&2; return 1; }
  duplicate_count="$(sdh_jq '[.dependencies[] | [.from,.to,.kind,.binding]] | length - (unique | length)' "$manifest")"
  [ "$duplicate_count" = "0" ] || { sdh_log 'LIE007: doppeltes Dependency-Tupel / duplicate dependency tuple' >&2; return 1; }

  while IFS= read -r path; do
    sdh_assert_safe_repository_path "$repo" "$path" file || return 1
    sdh_assert_strict_utf8_file "$repo/$path" "$path" || return 1
  done < <(sdh_jq -r '.orderedTargets[].path' "$manifest")

  while IFS= read -r root; do
    sdh_jq -e --arg endpoint "$root" 'any(.orderedTargets[]; .path == $endpoint)' "$manifest" >/dev/null \
      || { sdh_log "LIE007: unbekannter Root-Endpoint / unknown root endpoint: $root" >&2; return 1; }
  done < <(sdh_jq -r '.roots[]' "$manifest")

  while IFS=$'\t' read -r from to kind; do
    sdh_jq -e --arg endpoint "$from" 'any(.orderedTargets[]; .path == $endpoint)' "$manifest" >/dev/null \
      || { sdh_log "LIE007: unbekannter Dependency-Endpoint / unknown dependency endpoint: $from" >&2; return 1; }
    sdh_jq -e --arg endpoint "$to" 'any(.orderedTargets[]; .path == $endpoint)' "$manifest" >/dev/null \
      || { sdh_log "LIE007: unbekannter Dependency-Endpoint / unknown dependency endpoint: $to" >&2; return 1; }
    case "$kind" in *$'\n'*|*$'\r'*|*$'\t'*) sdh_log 'LIE007: ungueltiger Dependency-Kind / invalid dependency kind' >&2; return 1 ;; esac
  done < <(sdh_jq -r '.dependencies[] | [.from,.to,.kind] | @tsv' "$manifest")

  while IFS=$'\t' read -r path to; do
    sdh_jq -e --arg endpoint "$path" 'any(.orderedTargets[]; .path == $endpoint)' "$manifest" >/dev/null \
      || { sdh_log "LIE008: Legacy-Proof referenziert unbekannten Intake / legacy proof references unknown intake: $path" >&2; return 1; }
    case "$to" in specs/[0-9][0-9][0-9]-*) ;; *) sdh_log "LIE008: ungueltiger Feature-Nachweis / invalid feature evidence: $path" >&2; return 1 ;; esac
    sdh_assert_safe_repository_path "$repo" "$to" directory >/dev/null 2>&1 \
      || { sdh_log "LIE008: Feature-Ziel fehlt oder ist unsicher / feature target is missing or unsafe: $path" >&2; return 1; }
  done < <(sdh_jq -r '(.featureEvidence // [])[] | [.intakePath,.featurePath] | @tsv' "$manifest")

  positions_file="$(mktemp)"
  target_count="$(sdh_jq '.orderedTargets | length' "$manifest")"
  for ((index = 1; index <= target_count; index++)); do
    path="$(sdh_jq -r --argjson index "$((index - 1))" '.orderedTargets[$index].path' "$manifest")"
    position="$(sdh_display_position "$repo/$path" "$index")"
    case "$position" in ''|*[!0-9]*|0) rm -f "$positions_file"; sdh_log "LIE006: ungueltige sichtbare Position / invalid display position: $path" >&2; return 1 ;; esac
    printf '%s\n' "$position" >> "$positions_file"
  done
  duplicate_count="$(sort "$positions_file" | uniq -d | wc -l | tr -d ' ')"
  rm -f "$positions_file"
  [ "$duplicate_count" = "0" ] || { sdh_log 'LIE006: doppelte sichtbare Position / duplicate display position' >&2; return 1; }
}

sdh_relative_repository_path() {
  local view_path="$1"
  local target_path="$2"
  local view_dir="."
  local common=0 index result=""
  local -a view_parts=() target_parts=()

  case "$view_path" in
    */*) view_dir="${view_path%/*}" ;;
  esac
  [ "$view_dir" = "." ] || IFS='/' read -r -a view_parts <<< "$view_dir"
  IFS='/' read -r -a target_parts <<< "$target_path"

  while [ "$common" -lt "${#view_parts[@]}" ] \
    && [ "$common" -lt "${#target_parts[@]}" ] \
    && [ "${view_parts[$common]}" = "${target_parts[$common]}" ]; do
    common=$((common + 1))
  done
  for ((index = common; index < ${#view_parts[@]}; index++)); do
    result="${result}../"
  done
  for ((index = common; index < ${#target_parts[@]}; index++)); do
    [ "$index" = "$common" ] || result="${result}/"
    result="${result}${target_parts[$index]}"
  done
  printf '%s\n' "$result"
}

sdh_url_encode_repository_path() {
  local path="$1"
  local suffix=""
  local component encoded result=""

  case "$path" in
    */) suffix="/"; path="${path%/}" ;;
  esac
  while IFS= read -r component; do
    if [ "$component" = ".." ] || [ "$component" = "." ]; then
      encoded="$component"
    else
      encoded="$(sdh_jq -nr --arg value "$component" '$value | @uri')"
    fi
    [ -z "$result" ] || result="$result/"
    result="$result$encoded"
  done < <(printf '%s\n' "$path" | tr '/' '\n')
  printf '%s%s\n' "$result" "$suffix"
}

sdh_markdown_label() {
  printf '%s' "$1" | sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/\\/\\\\/g; s/\[/\\[/g; s/\]/\\]/g; s/|/\\|/g'
}

sdh_markdown_link() {
  local repo="$1"
  local view_path="$2"
  local target_path="$3"
  local expected_type="$4"
  local label relative suffix=""

  sdh_assert_safe_repository_path "$repo" "$target_path" "$expected_type" || return 1
  label="$(sdh_markdown_label "$(basename "$target_path")")"
  relative="$(sdh_relative_repository_path "$view_path" "$target_path")"
  [ "$expected_type" != "directory" ] || suffix="/"
  relative="$(sdh_url_encode_repository_path "${relative}${suffix}")"
  printf '[%s](%s)' "$label" "$relative"
}

sdh_display_position() {
  local intake_file="$1"
  local manifest_index="$2"
  local explicit

  explicit="$(sed -nE '
    s/^\*\*Reihenfolge:\*\* *(sichtbare )?Position ([0-9]+).*/\2/p
    s/^\*\*Order:\*\* *(visible )?[Pp]osition ([0-9]+).*/\2/p
    s/^Dieser Intake .*Position ([0-9]+).*/\1/p
    s/^Position ([0-9]+) .*/\1/p
  ' "$intake_file" | head -n 1)"
  if [ -n "$explicit" ]; then
    printf '%s\n' "$explicit"
  else
    printf '%s\n' "$manifest_index"
  fi
}

sdh_feature_cell() {
  local repo="$1"
  local view_path="$2"
  local intake_path="$3"
  local status="$4"
  local manifest="${5:-}"
  local spec_file feature_dir state_file archive_stamp mapped_path
  local -a candidates=()

  if [ "$status" = "Completed" ] && [ -d "$repo/specs" ]; then
    while IFS= read -r spec_file; do
      if awk -v needle="\`$intake_path\`" '
        /^\*\*(Binding Input|Bindende Eingabe)( \/ (Binding Input|Bindende Eingabe))?\*\*:/ && index($0, needle) { found = 1 }
        END { exit(found ? 0 : 1) }
      ' "$spec_file"; then
        feature_dir="${spec_file%/spec.md}"
        mapped_path="$(sdh_repository_relative_from_absolute_path "$repo" "$feature_dir")" || return 1
        candidates+=("$mapped_path")
      fi
    done < <(find "$repo/specs" -mindepth 2 -maxdepth 2 -type f -name spec.md -print | sort)

    archive_stamp="$(basename "$intake_path" | sed -nE 's/^.*\.([0-9]{3}-[^/]+)\.md$/\1/p')"
    if [ -n "$archive_stamp" ] && [ -d "$repo/specs/$archive_stamp" ]; then
      state_file="$repo/specs/$archive_stamp/autonomous-run-state.json"
      if [ -f "$state_file" ]; then
        sdh_assert_strict_utf8_file "$state_file" "specs/$archive_stamp/autonomous-run-state.json" || return 1
        if sdh_jq -e --arg intake "$intake_path" 'any(.acceptedArtifacts[]?; .path == $intake)' "$state_file" >/dev/null 2>&1; then
          candidates+=("specs/$archive_stamp")
        fi
      fi
    fi

    if [ -n "$manifest" ]; then
      while IFS= read -r mapped_path; do
        [ -d "$repo/$mapped_path" ] || { sdh_log "LIE008: Feature-Ziel fehlt / feature target is missing: $intake_path" >&2; return 1; }
        candidates+=("$mapped_path")
      done < <(sdh_jq -r --arg intake "$intake_path" '(.featureEvidence // [])[] | select(.intakePath == $intake) | .featurePath' "$manifest")
    fi
  fi

  case "${#candidates[@]}" in
    0)
      printf '%s' '— (kein Spec-Kit-Feature / no Spec Kit feature)'
      ;;
    1)
      sdh_markdown_link "$repo" "$view_path" "${candidates[0]}" directory
      ;;
    *)
      sdh_log "LIE008: mehrdeutiger Feature-Nachweis / ambiguous feature evidence: $intake_path" >&2
      return 1
      ;;
  esac
}

sdh_build_linked_intake_order_section() {
  local repo="$1"
  local manifest="$2"
  local view_path="${3:-Lastenheft_Abarbeitungsreihenfolge.md}"
  local target_count manifest_index path role status intake_link display_position manifest_relative
  local dependency_count dependency_index from kind binding dependency_link dependencies feature_cell

  command -v jq >/dev/null 2>&1 || { sdh_log 'LIE002: jq fehlt / jq is missing' >&2; return 1; }
  manifest_relative="$(sdh_repository_relative_from_absolute_path "$repo" "$manifest")" || return 1
  sdh_validate_linked_intake_manifest "$repo" "$manifest_relative" || return 1

  target_count="$(sdh_jq '.orderedTargets | length' "$manifest")"
  cat <<'EOF'
<!-- secure-development-hardening-order:start -->
## Verlinkte Lastenheft-Reihenfolge / Linked Requirements Order

Diese Tabelle wird aus dem kanonischen Series-Manifest und ausdruecklicher Feature-Evidence erzeugt. Vollstaendige Dateinamen, direkte eingehende Kanten und sichtbare Positionen bleiben erhalten. Manuelle Abschnitte ausserhalb dieses Markers bleiben unberuehrt.

*This table is generated from the canonical series manifest and explicit feature evidence. Complete filenames, direct incoming edges, and visible positions are preserved. Manual sections outside this marker remain unchanged.*

| Position | Status | Lastenheft/Intake | Abhängigkeiten / Dependencies | Spec-Kit-Feature |
|---:|---|---|---|---|
EOF

  for ((manifest_index = 1; manifest_index <= target_count; manifest_index++)); do
    path="$(sdh_jq -r --argjson index "$((manifest_index - 1))" '.orderedTargets[$index].path' "$manifest")"
    role="$(sdh_jq -r --argjson index "$((manifest_index - 1))" '.orderedTargets[$index].role' "$manifest")"
    status="$(sdh_jq -r --argjson index "$((manifest_index - 1))" '.orderedTargets[$index].status' "$manifest")"
    [ -n "$role" ] || { sdh_log "LIE002: Rolle fehlt / role is missing: $path" >&2; return 1; }
    sdh_assert_safe_repository_path "$repo" "$path" file || return 1
    intake_link="$(sdh_markdown_link "$repo" "$view_path" "$path" file)" || return 1
    display_position="$(sdh_display_position "$repo/$path" "$manifest_index")"

    dependency_count="$(sdh_jq --arg target "$path" '[.dependencies[] | select(.to == $target)] | length' "$manifest")"
    dependencies=""
    for ((dependency_index = 0; dependency_index < dependency_count; dependency_index++)); do
      from="$(sdh_jq -r --arg target "$path" --argjson index "$dependency_index" '[.dependencies[] | select(.to == $target)][$index].from' "$manifest")"
      kind="$(sdh_jq -r --arg target "$path" --argjson index "$dependency_index" '[.dependencies[] | select(.to == $target)][$index].kind' "$manifest")"
      binding="$(sdh_jq -r --arg target "$path" --argjson index "$dependency_index" '[.dependencies[] | select(.to == $target)][$index].binding' "$manifest")"
      sdh_jq -e --arg endpoint "$from" 'any(.orderedTargets[]; .path == $endpoint)' "$manifest" >/dev/null \
        || { sdh_log "LIE007: unbekannter Dependency-Endpoint / unknown dependency endpoint: $from" >&2; return 1; }
      dependency_link="$(sdh_markdown_link "$repo" "$view_path" "$from" file)" || return 1
      [ -z "$dependencies" ] || dependencies="${dependencies}<br>"
      dependencies="${dependencies}${dependency_link} → current (\`$(sdh_markdown_text "$kind")\`, binding: ${binding})"
    done
    [ -n "$dependencies" ] || dependencies='— (Root / keine direkte Abhängigkeit)'
    feature_cell="$(sdh_feature_cell "$repo" "$view_path" "$path" "$status" "$manifest")" || return 1
    printf '| %s | %s | %s | %s | %s |\n' "$display_position" "$(sdh_markdown_text "$status")" "$intake_link" "$dependencies" "$feature_cell"
  done

  cat <<'EOF'
<!-- secure-development-hardening-order:end -->
EOF
}

sdh_build_order_section() {
  local repo="$1"
  local view_path="${2:-Lastenheft_Abarbeitungsreihenfolge.md}"
  local manifest

  manifest="$(sdh_find_intake_series_manifest "$repo" 2>/dev/null || true)"
  if [ -n "$manifest" ]; then
    sdh_build_linked_intake_order_section "$repo" "$manifest" "$view_path"
  else
    sdh_build_legacy_order_section "$repo"
  fi
}

sdh_build_order_file_candidate() {
  local repo="$1"
  local manifest="$2"
  local output_relative="$3"
  local destination="$4"
  local output="$repo/$output_relative"
  local section_file current_file

  section_file="$(mktemp)"
  current_file="$(mktemp)"
  sdh_build_linked_intake_order_section "$repo" "$manifest" "$output_relative" > "$section_file" || { rm -f "$section_file" "$current_file"; return 1; }

  if [ -f "$output" ]; then
    sdh_jq -Rrsj 'gsub("\r\n|\r"; "\n")' "$output" > "$current_file"
    if grep -q '<!-- secure-development-hardening-order:start -->' "$current_file" \
      && grep -q '<!-- secure-development-hardening-order:end -->' "$current_file"; then
      awk -v section_file="$section_file" '
        BEGIN { while ((getline line < section_file) > 0) section = section line "\n"; in_generated = 0 }
        /<!-- secure-development-hardening-order:start -->/ { printf "%s", section; in_generated = 1; next }
        /<!-- secure-development-hardening-order:end -->/ { in_generated = 0; next }
        in_generated == 0 { print }
      ' "$current_file" > "$destination"
    else
      { cat "$current_file"; printf '\n\n'; cat "$section_file"; } > "$destination"
    fi
  else
    {
      cat <<'EOF'
# Lastenheft-Abarbeitungsreihenfolge / Requirements Processing Order

Diese Datei haelt die sichtbare Abarbeitungsreihenfolge der vorhandenen Lastenhefte fest. Sie ist eine Vorbereitung fuer spaetere Spec-Kit-Laeufe und startet selbst keinen Lauf.

*This file records the visible processing order of existing requirements documents. It prepares later Spec Kit runs and does not start a run by itself.*

EOF
      cat "$section_file"
    } > "$destination"
  fi

  awk '{ lines[NR] = $0 } END { last = NR; while (last > 0 && lines[last] ~ /^[[:space:]]*$/) last--; for (i = 1; i <= last; i++) print lines[i] }' "$destination" > "$destination.normalized"
  mv "$destination.normalized" "$destination"
  rm -f "$section_file" "$current_file"
}

sdh_view_semantics() {
  local file="$1"
  awk '
    /^\| Position \| Status \| Lastenheft\/Intake \|/ { in_table = 1; next }
    in_table && /^\|---/ { next }
    in_table && /^\|/ { print; next }
    in_table { exit }
  ' "$file" | sed -E 's/\]\([^)]*\)/\]/g'
}

sdh_restore_linked_intake_outputs() {
  local repo="$1"
  local backup_dir="$2"
  shift 2
  local index=0 relative target restore_tmp

  for relative in "$@"; do
    target="$repo/$relative"
    restore_tmp="$(dirname "$target")/.sdh-restore-$$-$index.tmp"
    if [ -f "$backup_dir/$index.file" ]; then
      cp "$backup_dir/$index.file" "$restore_tmp" && mv "$restore_tmp" "$target"
    else
      rm -f -- "$target" "$restore_tmp"
    fi
    index=$((index + 1))
  done
}

sdh_render_linked_intake_views() {
  local repo="$1"
  local manifest_relative="$2"
  local mode="$3"
  shift 3
  local -a outputs=("$@") candidates=() rechecks=() publish_temps=()
  local work_dir backup_dir input_fingerprint_before input_fingerprint_after relative target candidate recheck outside_target
  local index=0 other_index stale_count=0 replaced=0 publish_tmp fault="${SDH_TEST_FAULT:-}" vanish_path="${SDH_TEST_VANISH_PATH:-}"

  SDH_RENDER_RESULT="Failed"
  SDH_RENDER_WRITE_COUNT=0
  SDH_RENDER_ATTEMPTED_WRITES=0
  case "$mode" in check|write) ;; *) sdh_log 'LIE002: Modus muss check oder write sein / mode must be check or write' >&2; return 2 ;; esac
  [ "${#outputs[@]}" -gt 0 ] || { sdh_log 'LIE002: mindestens eine Ausgabe ist erforderlich / at least one output is required' >&2; return 2; }
  [ -d "$repo/.git" ] || { sdh_log 'LIE004: explizites Ziel ist kein Git-Repository / explicit target is not a Git repository' >&2; return 4; }
  command -v jq >/dev/null 2>&1 || { sdh_log 'LIE002: jq fehlt / jq is missing' >&2; return 2; }

  sdh_validate_linked_intake_manifest "$repo" "$manifest_relative" || return $?
  for relative in "${outputs[@]}"; do
    sdh_assert_safe_output_path "$repo" "$relative" || return $?
    if sdh_linked_intake_input_paths "$repo" "$manifest_relative" | LC_ALL=C grep -Fx -- "$relative" >/dev/null; then
      sdh_log "LIE006: Ausgabe ueberlappt kanonische Eingabe / output overlaps canonical input: $relative" >&2
      return 6
    fi
  done
  for ((index = 0; index < ${#outputs[@]}; index++)); do
    for ((other_index = index + 1; other_index < ${#outputs[@]}; other_index++)); do
      [ "${outputs[$index]}" != "${outputs[$other_index]}" ] || { sdh_log 'LIE006: doppelter Ausgabepfad / duplicate output path' >&2; return 6; }
    done
  done

  work_dir="$(mktemp -d)"
  backup_dir="$work_dir/backups"
  mkdir -p "$backup_dir"
  input_fingerprint_before="$(sdh_linked_intake_input_fingerprint "$repo" "$manifest_relative")"
  for ((index = 0; index < ${#outputs[@]}; index++)); do
    candidate="$work_dir/candidate-$index.md"
    sdh_build_order_file_candidate "$repo" "$repo/$manifest_relative" "${outputs[$index]}" "$candidate" || { rm -rf -- "$work_dir"; return 1; }
    candidates+=("$candidate")
  done

  if [ "${#outputs[@]}" -gt 1 ]; then
    for ((index = 0; index < ${#outputs[@]}; index++)); do
      target="$repo/${outputs[$index]}"
      [ -f "$target" ] || continue
      for ((other_index = index + 1; other_index < ${#outputs[@]}; other_index++)); do
        [ -f "$repo/${outputs[$other_index]}" ] || continue
        if [ "$(sdh_view_semantics "$target")" != "$(sdh_view_semantics "$repo/${outputs[$other_index]}")" ]; then
          rm -rf -- "$work_dir"
          sdh_log 'LIE011: Root- und Series-Ansicht widersprechen sich / root and series views disagree' >&2
          return 11
        fi
      done
    done
  fi

  for ((index = 0; index < ${#outputs[@]}; index++)); do
    target="$repo/${outputs[$index]}"
    if [ ! -f "$target" ] || ! cmp -s "$target" "${candidates[$index]}"; then
      stale_count=$((stale_count + 1))
    fi
  done
  if [ "$stale_count" = "0" ]; then
    rm -rf -- "$work_dir"
    SDH_RENDER_RESULT="Current"
    return 0
  fi
  if [ "$mode" = "check" ]; then
    rm -rf -- "$work_dir"
    SDH_RENDER_RESULT="Stale"
    sdh_log 'LIE009: erzeugte Ausgabe ist veraltet; Write-Modus ausfuehren / generated output is stale; run write mode' >&2
    return 9
  fi

  if [ -n "$fault" ]; then
    sdh_assert_fixture_fault_scope "$repo" || { rm -rf -- "$work_dir"; sdh_log 'LIE010: Testfehlerinjektion ist nur in isolierten Temp-Fixtures erlaubt / test fault injection is limited to isolated temporary fixtures' >&2; return 10; }
    case "$fault" in
      source-drift) printf ' ' >> "$repo/$manifest_relative" ;;
      input-drift)
        [ -n "$vanish_path" ] || { rm -rf -- "$work_dir"; sdh_log 'LIE010: Testziel fehlt / test target is missing' >&2; return 10; }
        sdh_assert_safe_repository_path "$repo" "$vanish_path" file || { rm -rf -- "$work_dir"; return 4; }
        printf '\n' >> "$repo/$vanish_path"
        ;;
      vanish-target)
        [ -n "$vanish_path" ] || { rm -rf -- "$work_dir"; sdh_log 'LIE010: Testziel fehlt / test target is missing' >&2; return 10; }
        sdh_assert_safe_repository_path "$repo" "$vanish_path" file || { rm -rf -- "$work_dir"; return 4; }
        rm -f -- "$repo/$vanish_path"
        ;;
      containment-drift)
        [ -n "$vanish_path" ] || { rm -rf -- "$work_dir"; sdh_log 'LIE010: Testziel fehlt / test target is missing' >&2; return 10; }
        sdh_assert_safe_repository_path "$repo" "$vanish_path" file || { rm -rf -- "$work_dir"; return 4; }
        outside_target="$(dirname "$repo")/.sdh-outside-$$.md"
        printf '# outside\n' > "$outside_target"
        rm -f -- "$repo/$vanish_path"
        sdh_create_test_file_symlink "$outside_target" "$repo/$vanish_path"
        ;;
      after-first-replace) ;;
      *) rm -rf -- "$work_dir"; sdh_log 'LIE010: unbekannte Testfehlerinjektion / unknown test fault injection' >&2; return 10 ;;
    esac
  fi

  sdh_validate_linked_intake_manifest "$repo" "$manifest_relative" || { rm -rf -- "$work_dir"; return 1; }
  input_fingerprint_after="$(sdh_linked_intake_input_fingerprint "$repo" "$manifest_relative")"
  if [ "$input_fingerprint_before" != "$input_fingerprint_after" ]; then
    rm -rf -- "$work_dir"
    sdh_log 'LIE010: kanonische Eingabemenge hat sich vor Publication geaendert / canonical input set changed before publication' >&2
    return 10
  fi
  for ((index = 0; index < ${#outputs[@]}; index++)); do
    recheck="$work_dir/recheck-$index.md"
    sdh_assert_safe_output_path "$repo" "${outputs[$index]}" || { rm -rf -- "$work_dir"; return 1; }
    sdh_build_order_file_candidate "$repo" "$repo/$manifest_relative" "${outputs[$index]}" "$recheck" || { rm -rf -- "$work_dir"; return 1; }
    cmp -s "${candidates[$index]}" "$recheck" || { rm -rf -- "$work_dir"; sdh_log 'LIE010: Kandidat driftete vor Publication / candidate drifted before publication' >&2; return 10; }
    rechecks+=("$recheck")
  done

  for ((index = 0; index < ${#outputs[@]}; index++)); do
    target="$repo/${outputs[$index]}"
    [ ! -f "$target" ] || cp "$target" "$backup_dir/$index.file"
    publish_tmp="$(dirname "$target")/.sdh-publish-$$-$index.tmp"
    if ! cp "${candidates[$index]}" "$publish_tmp"; then
      for candidate in "${publish_temps[@]+"${publish_temps[@]}"}"; do rm -f -- "$candidate"; done
      rm -f -- "$publish_tmp"
      rm -rf -- "$work_dir"
      return 10
    fi
    publish_temps+=("$publish_tmp")
  done

  for ((index = 0; index < ${#outputs[@]}; index++)); do
    target="$repo/${outputs[$index]}"
    if [ -f "$target" ] && cmp -s "$target" "${candidates[$index]}"; then
      rm -f -- "${publish_temps[$index]}"
      continue
    fi
    if ! mv "${publish_temps[$index]}" "$target"; then
      sdh_restore_linked_intake_outputs "$repo" "$backup_dir" "${outputs[@]}"
      for candidate in "${publish_temps[@]}"; do rm -f -- "$candidate"; done
      rm -rf -- "$work_dir"
      sdh_log 'LIE010: atomare Publication fehlgeschlagen; Altzustand wiederhergestellt / atomic publication failed; prior state restored' >&2
      return 10
    fi
    replaced=$((replaced + 1))
    SDH_RENDER_ATTEMPTED_WRITES="$replaced"
    if [ "$fault" = "after-first-replace" ] && [ "$replaced" = "1" ]; then
      sdh_restore_linked_intake_outputs "$repo" "$backup_dir" "${outputs[@]}"
      for candidate in "${publish_temps[@]}"; do rm -f -- "$candidate"; done
      rm -rf -- "$work_dir"
      SDH_RENDER_WRITE_COUNT=0
      sdh_log 'LIE010: simulierte Publication fehlgeschlagen; vollstaendiger Rollback / simulated publication failed; complete rollback' >&2
      return 10
    fi
  done

  for ((index = 0; index < ${#outputs[@]}; index++)); do
    cmp -s "$repo/${outputs[$index]}" "${candidates[$index]}" || {
      sdh_restore_linked_intake_outputs "$repo" "$backup_dir" "${outputs[@]}"
      for candidate in "${publish_temps[@]}"; do rm -f -- "$candidate"; done
      rm -rf -- "$work_dir"
      SDH_RENDER_WRITE_COUNT=0
      sdh_log 'LIE010: Post-Write-Verifikation fehlgeschlagen; vollstaendiger Rollback / post-write verification failed; complete rollback' >&2
      return 10
    }
  done
  for candidate in "${publish_temps[@]}"; do rm -f -- "$candidate"; done
  rm -rf -- "$work_dir"
  SDH_RENDER_WRITE_COUNT="$replaced"
  SDH_RENDER_RESULT="Updated"
  return 0
}

sdh_update_order_file() {
  local repo="$1"
  local dry_run="$2"
  local order_file="$repo/Lastenheft_Abarbeitungsreihenfolge.md"
  local section_file tmp_file normalized_file

  section_file="$(mktemp)"
  tmp_file="$(mktemp)"
  normalized_file="$(mktemp)"
  sdh_build_order_section "$repo" > "$section_file"

  if [ -f "$order_file" ]; then
    if grep -q '<!-- secure-development-hardening-order:start -->' "$order_file" \
      && grep -q '<!-- secure-development-hardening-order:end -->' "$order_file"; then
      awk -v section_file="$section_file" '
        BEGIN {
          while ((getline line < section_file) > 0) section = section line "\n"
          in_generated = 0
        }
        /<!-- secure-development-hardening-order:start -->/ {
          printf "%s", section
          in_generated = 1
          next
        }
        /<!-- secure-development-hardening-order:end -->/ {
          in_generated = 0
          next
        }
        in_generated == 0 { print }
      ' "$order_file" > "$tmp_file"
    else
      {
        cat "$order_file"
        printf '\n\n'
        cat "$section_file"
      } > "$tmp_file"
    fi
  else
    cat > "$tmp_file" <<'EOF'
# Lastenheft-Abarbeitungsreihenfolge / Requirements Processing Order

Diese Datei haelt die sichtbare Abarbeitungsreihenfolge der vorhandenen Lastenhefte fest. Sie ist eine Vorbereitung fuer spaetere Spec-Kit-Laeufe und startet selbst keinen Lauf.

*This file records the visible processing order of existing requirements documents. It prepares later Spec Kit runs and does not start a run by itself.*

EOF
    cat "$section_file" >> "$tmp_file"
  fi

  awk '
    { lines[NR] = $0 }
    END {
      last = NR
      while (last > 0 && lines[last] ~ /^[[:space:]]*$/) last--
      for (i = 1; i <= last; i++) print lines[i]
    }
  ' "$tmp_file" > "$normalized_file"
  mv "$normalized_file" "$tmp_file"

  if [ -f "$order_file" ] && cmp -s "$order_file" "$tmp_file"; then
    rm -f "$section_file" "$tmp_file" "$normalized_file"
    return 1
  fi

  if [ "$dry_run" = "1" ]; then
    rm -f "$section_file" "$tmp_file" "$normalized_file"
    return 0
  fi

  mv "$tmp_file" "$order_file"
  rm -f "$section_file" "$normalized_file"
  return 0
}

sdh_prepare_repo() {
  local repo="$1"
  local project_name="$2"
  local explicit_language="${3:-}"
  local dry_run="${4:-0}"
  local force="${5:-0}"
  local script_dir="${6:-}"
  local language source_dir template_file target_docs intake_file

  SDH_PREPARE_RESULT="skipped"
  SDH_PREPARE_REASON=""
  SDH_DETECTED_LANGUAGE=""

  if [ ! -d "$repo/.git" ]; then
    SDH_PREPARE_REASON="kein Git-Repository"
    return 0
  fi

  language="$(sdh_detect_language "$repo" "$project_name" "$explicit_language" 2>/dev/null || true)"
  if [ -z "$language" ]; then
    SDH_PREPARE_REASON="Primaersprache unklar; nutze --primary-language fuer automatische Vorbereitung"
    return 0
  fi
  SDH_DETECTED_LANGUAGE="$language"

  if ! sdh_is_msl_language "$language"; then
    if sdh_is_known_non_msl_language "$language"; then
      SDH_PREPARE_REASON="nicht-MSL erkannt: $language"
    else
      SDH_PREPARE_REASON="Sprache nicht auf MSL-Allowlist: $language"
    fi
    return 0
  fi

  script_dir="${script_dir:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." 2>/dev/null && pwd)}"
  source_dir="$(sdh_find_source_dir "$script_dir" 2>/dev/null || true)"
  template_file="$(sdh_find_template_file "$script_dir" 2>/dev/null || true)"

  if [ -z "$source_dir" ]; then
    SDH_PREPARE_RESULT="error"
    SDH_PREPARE_REASON="docs/secure-development Quelle nicht gefunden"
    return 1
  fi
  if [ -z "$template_file" ]; then
    SDH_PREPARE_RESULT="error"
    SDH_PREPARE_REASON="Lastenheft-Template nicht gefunden"
    return 1
  fi

  target_docs="$repo/docs/secure-development"
  intake_file="$repo/Lastenheft_Secure-Development-Hardening.md"

  if [ "$dry_run" = "1" ]; then
    sdh_log "  [dry-run] docs/secure-development nach ${repo}/docs/secure-development synchronisieren"
  else
    sdh_sync_baseline "$source_dir" "$target_docs" 0
  fi

  if [ -f "$intake_file" ] && [ "$force" != "1" ]; then
    [ "$dry_run" = "1" ] && sdh_log "  [dry-run] Lastenheft vorhanden, wird nicht ueberschrieben: $(basename "$intake_file")"
  else
    if [ "$dry_run" = "1" ]; then
      sdh_log "  [dry-run] Lastenheft_Secure-Development-Hardening.md erzeugen"
    else
      sdh_render_template "$template_file" "$intake_file" "$project_name"
    fi
  fi

  if sdh_update_order_file "$repo" "$dry_run"; then
    [ "$dry_run" = "1" ] && sdh_log "  [dry-run] Lastenheft_Abarbeitungsreihenfolge.md aktualisieren"
  else
    [ "$dry_run" = "1" ] && sdh_log "  [dry-run] Lastenheft_Abarbeitungsreihenfolge.md unveraendert"
  fi

  SDH_PREPARE_RESULT="prepared"
  SDH_PREPARE_REASON="MSL erkannt: $language"
  return 0
}
