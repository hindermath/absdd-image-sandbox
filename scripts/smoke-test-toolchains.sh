#!/usr/bin/env bash
set -euo pipefail

json_mode=false
repository=""
while (($# > 0)); do
  case "$1" in
    --json) json_mode=true ;;
    --repo)
      (($# >= 2)) || { printf '%s\n' '--repo requires a path' >&2; exit 2; }
      repository="$2"
      shift
      ;;
    -h|--help)
      printf '%s\n' 'Usage: smoke-test-toolchains.sh [--json] [--repo PATH]'
      exit 0
      ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; exit 2 ;;
  esac
  shift
done

if $json_mode; then
  python3 - "$repository" <<'PY'
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

repository = Path(sys.argv[1]).resolve() if sys.argv[1] else None
commands = {
    "actionlint": ["actionlint", "-version"],
    "bash": ["bash", "--version"],
    "codex": ["codex", "--version"],
    "dotnet": ["dotnet", "--version"],
    "git": ["git", "--version"],
    "jq": ["jq", "--version"],
    "pwsh": ["pwsh", "--version"],
    "python": ["python3", "--version"],
    "yq": ["yq", "--version"],
}
results = []
for name, command in commands.items():
    executable = shutil.which(command[0])
    if executable is None:
        results.append({"tool": name, "status": "Missing", "version": None})
        continue
    completed = subprocess.run(command, text=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, check=False)
    version = completed.stdout.splitlines()[0].strip() if completed.stdout else ""
    results.append({"tool": name, "status": "Pass" if completed.returncode == 0 else "Fail",
                    "version": version})

# GitHub provider administration intentionally stays on the separate control plane.
results.append({"tool": "gh", "status": "ControlPlane", "version": None})
sdk = {"requested": None, "selected": None, "status": "NotApplicable"}
if repository and (repository / "global.json").is_file():
    try:
        sdk["requested"] = json.loads(
            (repository / "global.json").read_text(encoding="utf-8")
        )["sdk"]["version"]
        completed = subprocess.run(["dotnet", "--version"], cwd=repository, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
        sdk["selected"] = completed.stdout.strip().splitlines()[0] if completed.returncode == 0 else None
        sdk["status"] = (
            "Pass"
            if completed.returncode == 0 and sdk["selected"] == sdk["requested"]
            else "Fail"
        )
    except (KeyError, TypeError, json.JSONDecodeError, OSError, UnicodeError):
        sdk["status"] = "Fail"

document = {
    "schemaVersion": "1.0",
    "platform": platform.system().lower(),
    "architecture": platform.machine().lower(),
    "repository": str(repository) if repository else None,
    "tools": results,
    "dotnetSdk": sdk,
}
print(json.dumps(document, ensure_ascii=True, sort_keys=True))
if any(item["status"] in {"Missing", "Fail"} for item in results) or sdk["status"] == "Fail":
    raise SystemExit(1)
PY
  exit $?
fi

base_dir="${SMOKE_TEST_ROOT:-/home/adedev/smoke-tests}"
mkdir -p "${base_dir}"
work_dir="$(mktemp -d "${base_dir}/run.XXXXXX")"

cleanup() {
  rm -rf "${work_dir}"
}
trap cleanup EXIT

section() {
  printf '\n== %s ==\n' "$1"
}

section "identity"
whoami
pwd

section "tool versions"
dotnet --info
dotnet --version
java --version
javac --version
mvn --version
go version
gopls version
rustc --version
cargo --version
cargo clippy --version
python --version
pwsh --version
node --version
npm --version
swift --version
swiftc --version
command -v sourcekit-lsp
opencode --version
codex --version
claude --version
agy --version
copilot --version
syft version
actionlint -version
specify version
specify check

section ".NET"
dotnet_dir="${work_dir}/dotnet"
mkdir -p "${dotnet_dir}"
(
  cd "${dotnet_dir}"
  dotnet new console --framework net10.0 --no-restore
  dotnet run
)

section "Java"
java_dir="${work_dir}/java"
mkdir -p "${java_dir}"
cat >"${java_dir}/Main.java" <<'JAVA'
public final class Main {
  public static void main(String[] args) {
    System.out.println("hello from java");
  }
}
JAVA
javac "${java_dir}/Main.java"
java -cp "${java_dir}" Main

section "Go"
go_dir="${work_dir}/go"
mkdir -p "${go_dir}"
(
  cd "${go_dir}"
  go mod init example.com/ade-smoke
  cat >smoke_test.go <<'GO'
package smoke

import "testing"

func TestSmoke(t *testing.T) {
  if 2+2 != 4 {
    t.Fatal("unexpected arithmetic")
  }
}
GO
  go test ./...
)

section "Rust"
rust_dir="${work_dir}/rust"
cargo new "${rust_dir}" --bin
(
  cd "${rust_dir}"
  cargo test
  cargo clippy -- -D warnings
)

section "Python"
python_dir="${work_dir}/python"
python -m venv "${python_dir}/.venv"
"${python_dir}/.venv/bin/python" - <<'PY'
print("hello from python")
PY

section "PowerShell"
# PowerShell variables must remain literal until pwsh expands them.
# shellcheck disable=SC2016
pwsh -NoLogo -NoProfile -Command \
  '$result = 2 + 2; if ($result -ne 4) { throw "unexpected arithmetic" }; "hello from powershell"'
# shellcheck disable=SC2016
pwsh -NoLogo -NoProfile -Command \
  '$result = & pwsh -NoLogo -NoProfile -Command "2 + 2"; if ($LASTEXITCODE -ne 0 -or $result -ne 4) { throw "nested PowerShell failed" }; "hello from nested powershell"'

section "Node.js"
node -e 'console.log("hello from node")'
npm --version >/dev/null

section "Swift"
swift_dir="${work_dir}/swift"
mkdir -p "${swift_dir}"
(
  cd "${swift_dir}"
  swift package init --name SwiftSmoke --type executable
  swift build
  swift run SwiftSmoke
)

section "done"
printf 'Toolchain smoke tests passed.\n'
