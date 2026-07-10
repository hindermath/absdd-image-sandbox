#!/usr/bin/env python3
"""Validate the pinned home-baseline image-content dependency."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


LOCK_PATH = Path("home-baseline.lock.json")
EXPECTED_SOURCE = "https://github.com/hindermath/home-baseline.git"
EXPECTED_KEYS = {"schemaVersion", "source", "tag", "commit", "license"}


def main() -> int:
    try:
        data = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Invalid {LOCK_PATH}: {exc}", file=sys.stderr)
        return 1

    failures: list[str] = []
    if set(data) != EXPECTED_KEYS:
        failures.append(f"keys must be exactly: {', '.join(sorted(EXPECTED_KEYS))}")
    if data.get("schemaVersion") != 1:
        failures.append("schemaVersion must be 1")
    if data.get("source") != EXPECTED_SOURCE:
        failures.append(f"source must be {EXPECTED_SOURCE}")
    if not re.fullmatch(r"v\d+\.\d+\.\d+", str(data.get("tag", ""))):
        failures.append("tag must be a stable vMAJOR.MINOR.PATCH release")
    if not re.fullmatch(r"[0-9a-f]{40}", str(data.get("commit", ""))):
        failures.append("commit must be a lowercase 40-character Git SHA")
    if data.get("license") != "MIT":
        failures.append("license must be MIT")

    if failures:
        print("Home-baseline lock validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Home-baseline lock OK: {data['tag']} @ {data['commit']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
