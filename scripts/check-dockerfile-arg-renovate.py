#!/usr/bin/env python3
"""Require Renovate metadata for every Dockerfile ARG."""

from pathlib import Path
import re
import sys


ARG_RE = re.compile(r"^\s*ARG\s+([A-Z][A-Z0-9_]*)\s*=")
RENOVATE_RE = re.compile(
    r"^\s*#\s+renovate(?:-dotnet)?:\s+.*\bargName=([A-Z][A-Z0-9_]*)\b"
)


def main() -> int:
    dockerfile = Path("Dockerfile")
    lines = dockerfile.read_text(encoding="utf-8").splitlines()
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
