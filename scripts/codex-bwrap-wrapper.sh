#!/usr/bin/env bash
set -euo pipefail

readonly real_bwrap=/usr/libexec/codex-bwrap.real
[[ -x "$real_bwrap" ]] || {
  printf '%s\n' 'Codex Bubblewrap runtime is unavailable.' >&2
  exit 127
}

rewritten=()
while (($# > 0)); do
  if (($# >= 5)) \
    && [[ "$1" == --perms && "$2" == 000 && "$3" == --ro-bind-data ]] \
    && [[ "$5" == /home/adedev/.codex/auth.json \
      || "$5" == /home/adedev/.codex/config.toml ]]; then
    # Codex supplies an inaccessible in-memory replacement for denied files.
    # A writable bind-data mount is required only because rootless Podman
    # rejects the read-only remount; mode 000 and the Landlock deny rule remain.
    rewritten+=(--perms 000 --bind-data "$4" "$5")
    shift 5
    continue
  fi
  if (($# >= 6)) \
    && [[ "$1" == --perms && "$2" == 000 && "$3" == --tmpfs ]] \
    && [[ "$4" == /home/adedev/.codex/log \
      || "$4" == /home/adedev/.codex/sessions \
      || "$4" == /home/adedev/.local/share/opencode ]] \
    && [[ "$5" == --remount-ro && "$6" == "$4" ]]; then
    # The isolated replacement is empty and remains denied by Landlock. Avoid
    # only the unsupported remount operation in the nested user namespace.
    rewritten+=(--perms 000 --tmpfs "$4")
    shift 6
    continue
  fi
  if (($# >= 6)) \
    && [[ "$1" == --perms && "$2" == 555 && "$3" == --tmpfs ]] \
    && [[ "$4" == /tmp/.git || "$4" == /tmp/.agents || "$4" == /tmp/.codex ]] \
    && [[ "$5" == --remount-ro && "$6" == "$4" ]]; then
    # /tmp stays read-only in this container profile, so synthetic metadata
    # mounts below it are unnecessary and cannot be created rootlessly.
    shift 6
    continue
  fi
  if (($# >= 6)) \
    && [[ "$1" == --perms && "$2" == 555 && "$3" == --tmpfs ]] \
    && [[ "$4" == /home/adedev/codex-workspace/.git \
      || "$4" == /home/adedev/codex-workspace/.agents \
      || "$4" == /home/adedev/codex-workspace/.codex ]] \
    && [[ "$5" == --remount-ro && "$6" == "$4" ]]; then
    protected_path="$4"
    if [[ ! -d "$protected_path" || -L "$protected_path" ]] \
      || [[ "$(stat -c %u "$protected_path")" != 0 ]] \
      || find "$protected_path" -xdev \( ! -user root -o -perm /022 \) -print -quit | grep -q .; then
      printf 'Unsafe Codex transaction metadata path: %s\n' "$protected_path" >&2
      exit 126
    fi
    # Root-owned placeholders enforce the same write denial without a nested
    # tmpfs remount, which rootless Podman does not permit.
    rewritten+=(--ro-bind "$protected_path" "$protected_path")
    shift 6
    continue
  fi
  case "$1" in
    --bind)
      (($# >= 3)) || { printf '%s\n' 'Missing values for --bind.' >&2; exit 2; }
      if [[ "$2" == /tmp && "$3" == /tmp ]]; then
        # Drop Codex's legacy writable-/tmp overlay. The read-only root bind
        # remains effective and matches exclude_slash_tmp=true.
        shift 3
        continue
      fi
      ;;
    --dev)
      (($# >= 2)) || { printf '%s\n' 'Missing value for --dev.' >&2; exit 2; }
      if [[ "$2" == /dev ]]; then
        # Podman already supplies a minimal device tree. Rebinding that tree
        # avoids a nested devpts mount, which rootless containers cannot create.
        rewritten+=(--dev-bind /dev /dev)
        shift 2
        continue
      fi
      ;;
    --proc)
      (($# >= 2)) || { printf '%s\n' 'Missing value for --proc.' >&2; exit 2; }
      if [[ "$2" == /proc ]]; then
        # The outer container's procfs exposes only container processes. The
        # inner PID namespace and all remaining Bubblewrap arguments stay set.
        rewritten+=(--ro-bind /proc /proc)
        shift 2
        continue
      fi
      ;;
  esac
  rewritten+=("$1")
  shift
done

exec "$real_bwrap" "${rewritten[@]}"
