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
    "CODEX_VERSION": (
        "@openai/codex",
        '"@openai/codex@${CODEX_VERSION}"',
        "codex --version",
    ),
    "CLAUDE_CODE_VERSION": (
        "@anthropic-ai/claude-code",
        '"@anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}"',
        "claude --version",
    ),
    "ANTIGRAVITY_CLI_VERSION": (
        "google-antigravity/antigravity-cli",
        "releases/download/${ANTIGRAVITY_CLI_VERSION}",
        "agy --version",
    ),
    "COPILOT_CLI_VERSION": (
        "@github/copilot",
        '"@github/copilot@${COPILOT_CLI_VERSION}"',
        "copilot --version",
    ),
}

REQUIRED_OPERATIONAL_TOOLS = {
    "ACTIONLINT_VERSION": ("rhysd/actionlint", "actionlint_${ACTIONLINT_VERSION}", "actionlint -version"),
    "DOTNET_COMPAT_SDK_VERSION": ("dotnet-sdk", "dotnet-sdk-${DOTNET_COMPAT_SDK_VERSION}", "dotnet --version"),
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
    for arg_name, (package, install_marker, version_command) in REQUIRED_AGENT_CLIS.items():
        if not re.search(rf"^ARG {re.escape(arg_name)}=\S+$", dockerfile_text, re.MULTILINE):
            failures.append(f"required agent ARG missing: {arg_name}")
        if install_marker not in dockerfile_text:
            failures.append(f"Dockerfile does not install {package} from {arg_name}")
        if package not in renovate_packages:
            failures.append(f"Renovate agent CLI group is missing {package}")
        if version_command not in smoke_text:
            failures.append(f"smoke test is missing: {version_command}")

    for arg_name, (package, install_marker, version_command) in REQUIRED_OPERATIONAL_TOOLS.items():
        if not re.search(rf"^ARG {re.escape(arg_name)}=\S+$", dockerfile_text, re.MULTILINE):
            failures.append(f"required operational ARG missing: {arg_name}")
        if install_marker not in dockerfile_text:
            failures.append(f"Dockerfile does not install {package} from {arg_name}")
        if version_command not in smoke_text:
            failures.append(f"smoke test is missing: {version_command}")

    # Actionlint release assets use Go's "amd64" name, not "x86_64".
    architecture_contracts = {
        "actionlint": (
            r'amd64\) actionlint_arch="amd64"; actionlint_sha256="[0-9a-f]{64}"',
            r'arm64\) actionlint_arch="arm64"; actionlint_sha256="[0-9a-f]{64}"',
        ),
        ".NET compatibility SDK": (
            r'amd64\) dotnet_rid="linux-x64"; dotnet_sha512="[0-9a-f]{128}"',
            r'arm64\) dotnet_rid="linux-arm64"; dotnet_sha512="[0-9a-f]{128}"',
        ),
    }
    for label, patterns in architecture_contracts.items():
        if not all(re.search(pattern, dockerfile_text) for pattern in patterns):
            failures.append(f"Dockerfile is missing complete amd64/arm64 hashes for {label}")

    codex_config = Path("codex/config.toml").read_text(encoding="utf-8")
    codex_requirements = Path("codex/requirements.toml").read_text(encoding="utf-8")
    codex_contracts = {
        "Codex rootless adapter is not installed": "scripts/codex-bwrap-wrapper.sh",
        "Codex transaction workspace is not prepared": "/home/adedev/codex-workspace/.git",
    }
    for message, marker in codex_contracts.items():
        if marker not in dockerfile_text:
            failures.append(message)
    if "/etc/codex/managed_config.toml" in dockerfile_text:
        failures.append("legacy Codex managed_config would collapse allowed policy sets")
    if 'approval_policy = "untrusted"' not in codex_config:
        failures.append("Codex interactive default must remain untrusted")
    if not re.search(
        r'allowed_approval_policies\s*=\s*\[[^\]]*"untrusted"[^\]]*"on-request"[^\]]*"never"',
        codex_requirements,
    ):
        failures.append("Codex requirements must support interactive and headless approval modes")

    if not re.search(r"^ARG SYFT_VERSION=\S+$", dockerfile_text, re.MULTILINE):
        failures.append("required SBOM tool ARG missing: SYFT_VERSION")
    if "anchore/syft" not in renovate_packages:
        failures.append("Renovate supply-chain group is missing anchore/syft")
    if "syft version" not in smoke_text:
        failures.append("smoke test is missing: syft version")
    if "syft_${SYFT_VERSION}_checksums.txt" not in dockerfile_text:
        failures.append("Syft installation does not retrieve its checksum manifest")

    if not re.search(r"^ARG POWERSHELL_VERSION=\S+$", dockerfile_text, re.MULTILINE):
        failures.append("required scripting tool ARG missing: POWERSHELL_VERSION")
    if "PowerShell/PowerShell" not in renovate_packages:
        failures.append("Renovate scripting tool group is missing PowerShell/PowerShell")
    if 'pwsh -NoLogo -NoProfile' not in dockerfile_text:
        failures.append("Dockerfile does not verify the bundled PowerShell version")
    if "pwsh --version" not in smoke_text:
        failures.append("smoke test is missing: pwsh --version")

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
