#!/usr/bin/env python3
"""Require Renovate metadata for every Dockerfile ARG."""

from pathlib import Path
import json
import re
import sys


ARG_RE = re.compile(r"^\s*ARG\s+([A-Z][A-Z0-9_]*)\s*=")
RENOVATE_RE = re.compile(
    r"^\s*#\s+renovate(?:-dotnet)?:\s+.*\bargName=([A-Z][A-Z0-9_]*)\b"
)

REQUIRED_AGENT_CLIS = {
    "CODEX_VERSION": ("@openai/codex", "codex --version"),
    "CLAUDE_CODE_VERSION": ("@anthropic-ai/claude-code", "claude --version"),
    "GEMINI_CLI_VERSION": ("@google/gemini-cli", "agy --version"),
    "COPILOT_CLI_VERSION": ("@github/copilot", "copilot --version"),
}


def main() -> int:
    dockerfile = Path("Dockerfile")
    lines = dockerfile.read_text(encoding="utf-8").splitlines()
    dockerfile_text = "\n".join(lines)
    smoke_text = Path("scripts/smoke-test-toolchains.sh").read_text(encoding="utf-8")
    renovate = json.loads(Path("renovate.json").read_text(encoding="utf-8"))
    failures: list[str] = []

    for index, line in enumerate(lines):
        match = ARG_RE.match(line)
        if not match:
            continue

        arg_name = match.group(1)
        if index == 0:
            failures.append(f"line {index + 1}: ARG {arg_name} has no metadata line")
            continue

        metadata = RENOVATE_RE.match(lines[index - 1])
        if metadata is None:
            failures.append(
                f"line {index + 1}: ARG {arg_name} is missing an immediately "
                "preceding # renovate metadata line"
            )
            continue

        metadata_arg = metadata.group(1)
        if metadata_arg != arg_name:
            failures.append(
                f"line {index + 1}: ARG {arg_name} metadata uses argName={metadata_arg}"
            )

    renovate_packages = {
        package
        for rule in renovate.get("packageRules", [])
        for package in rule.get("matchPackageNames", [])
    }
    for arg_name, (package, version_command) in REQUIRED_AGENT_CLIS.items():
        if not re.search(rf"^ARG {re.escape(arg_name)}=\S+$", dockerfile_text, re.MULTILINE):
            failures.append(f"required agent ARG missing: {arg_name}")
        if f'"{package}@${{{arg_name}}}"' not in dockerfile_text:
            failures.append(f"Dockerfile does not install {package} from {arg_name}")
        if package not in renovate_packages:
            failures.append(f"Renovate agent CLI group is missing {package}")
        if version_command not in smoke_text:
            failures.append(f"smoke test is missing: {version_command}")

    if not re.search(r"^ARG SYFT_VERSION=\S+$", dockerfile_text, re.MULTILINE):
        failures.append("required SBOM tool ARG missing: SYFT_VERSION")
    if "anchore/syft" not in renovate_packages:
        failures.append("Renovate supply-chain group is missing anchore/syft")
    if "syft version" not in smoke_text:
        failures.append("smoke test is missing: syft version")
    if "syft_${SYFT_VERSION}_checksums.txt" not in dockerfile_text:
        failures.append("Syft installation does not retrieve its checksum manifest")

    if failures:
        print("Every Dockerfile ARG must have matching Renovate metadata.")
        print("Use this form directly above the ARG:")
        print(
            "# renovate: datasource=<datasource> depName=<dependency> "
            "versioning=<versioning> argName=<ARG_NAME>"
        )
        print()
        print("\n".join(failures))
        return 1

    print("Dockerfile ARG Renovate metadata OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
