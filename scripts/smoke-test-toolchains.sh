#!/usr/bin/env bash
set -euo pipefail

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
java --version
javac --version
mvn --version
go version
gopls version
rustc --version
cargo --version
cargo clippy --version
python --version
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
