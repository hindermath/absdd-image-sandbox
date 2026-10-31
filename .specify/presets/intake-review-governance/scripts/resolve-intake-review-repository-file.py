#!/usr/bin/env python3
"""Resolve one existing intake-review file within the selected repository."""

import argparse
import json
from pathlib import Path, PurePosixPath, PureWindowsPath


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--repo", required=True)
parser.add_argument("--file", required=True)
args = parser.parse_args()

try:
    value = args.file
    relative = PurePosixPath(value)
    if (not value or "\\" in value or "\x00" in value or
            PureWindowsPath(value).drive or relative.is_absolute() or ".." in relative.parts):
        raise ValueError("invalid repository-relative path")
    root = Path(args.repo).resolve(strict=True)
    path = (root / value).resolve(strict=True)
    if not root.is_dir() or not path.is_relative_to(root) or not path.is_file():
        raise ValueError("outside repository")
    print(json.dumps({"path": str(path)}))
except (OSError, RuntimeError, ValueError):
    print(json.dumps({"errorClass": "IRG001", "message": "repository file containment failed"}))
    raise SystemExit(2) from None
