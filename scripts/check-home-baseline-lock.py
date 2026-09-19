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
    if not isinstance(data, dict):
        print("Home-baseline lock must be an object", file=sys.stderr)
        return 1
    schema = data.get("schemaVersion")
    expected_keys = EXPECTED_KEYS if schema == 1 else (EXPECTED_KEYS - {"tag"}) | {"refType"}
    if set(data) != expected_keys:
        failures.append(f"keys must be exactly: {', '.join(sorted(expected_keys))}")
    if type(schema) is not int or schema not in (1, 2):
        failures.append("schemaVersion must be 1 or 2")
    if schema == 2 and data.get("refType") != "commit":
        failures.append("schema 2 refType must be commit")
    if data.get("source") != EXPECTED_SOURCE:
        failures.append(f"source must be {EXPECTED_SOURCE}")
    if schema == 1 and not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", str(data.get("tag", ""))):
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

    print(f"Home-baseline lock OK: {data.get('tag', 'commit-pin')} @ {data['commit']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
