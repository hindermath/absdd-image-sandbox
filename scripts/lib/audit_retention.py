#!/usr/bin/python3 -I
"""Verify one current audit export and retain exactly thirty UTC date buckets."""

from __future__ import annotations

import argparse
from datetime import date, timedelta
import json
import os
from pathlib import Path
import re
import stat
import sys


DAY_FILE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.jsonl$")


def audit_day(value: str) -> date:
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("UTC day must be a valid YYYY-MM-DD date") from exc
    if parsed.isoformat() != value:
        raise ValueError("UTC day must use canonical YYYY-MM-DD")
    return parsed


def open_audit_directory(path: Path) -> int:
    if path.is_symlink() or not path.is_dir():
        raise ValueError("audit root must be a direct directory, not a link")
    if not hasattr(os, "O_NOFOLLOW") or os.open not in os.supports_dir_fd:
        raise ValueError("native no-follow directory operations unavailable")
    flags = os.O_RDONLY | os.O_NOFOLLOW
    if hasattr(os, "O_DIRECTORY"):
        flags |= os.O_DIRECTORY
    return os.open(path, flags)


def direct_regular(directory_fd: int, name: str) -> os.stat_result:
    info = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
    if not stat.S_ISREG(info.st_mode):
        raise ValueError(f"audit entry is not a direct regular file: {name}")
    return info


def verify_export(root: Path, day: date, run_id: str) -> dict:
    if not run_id or not re.fullmatch(r"[0-9a-fA-F-]{36}", run_id):
        raise ValueError("run id must be a UUID")
    name = day.isoformat() + ".jsonl"
    directory_fd = open_audit_directory(root)
    try:
        before = direct_regular(directory_fd, name)
        if before.st_size == 0:
            raise ValueError("current audit export is empty")
        file_fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=directory_fd)
        try:
            opened = os.fstat(file_fd)
            if (opened.st_dev, opened.st_ino) != (before.st_dev, before.st_ino):
                raise ValueError("audit export identity changed")
            with os.fdopen(file_fd, "r", encoding="utf-8") as handle:
                file_fd = -1
                count = 0
                matching_count = 0
                run = None
                while True:
                    line = handle.readline(1024 * 1024 + 1)
                    if not line:
                        break
                    if len(line) > 1024 * 1024 or (
                        not line.endswith("\n") and len(line) == 1024 * 1024 + 1
                    ):
                        raise ValueError("audit JSONL record exceeds 1 MiB")
                    if not line.strip():
                        continue
                    count += 1
                    row = json.loads(line)
                    if (row.get("record_type") == "audit-export-run"
                            and row.get("run_id") == run_id
                            and row.get("audit_date") == day.isoformat()):
                        matching_count += 1
                        if matching_count > 1:
                            raise ValueError("current audit run record duplicated")
                        run = row
        finally:
            if file_fd >= 0:
                os.close(file_fd)
        if matching_count != 1:
            raise ValueError("current audit run record missing or duplicated")
        assert run is not None
        if run.get("session_coverage") != "filesystem-metadata-only":
            raise ValueError("audit run scope is invalid")
        return {
            "auditDate": day.isoformat(),
            "runId": run_id,
            "recordCount": count,
            "sessionMetadataCount": run.get("session_metadata_count"),
            "verified": True,
        }
    finally:
        os.close(directory_fd)


def retain(root: Path, day: date, *, dry_run: bool = False) -> dict:
    """Delete only direct regular day files before the thirty-day UTC window."""
    cutoff = day - timedelta(days=29)
    directory_fd = open_audit_directory(root)
    selected: list[tuple[str, int, int]] = []
    removed = 0
    skipped_unsafe = 0
    try:
        with os.scandir(root) as entries:
            for entry in entries:
                match = DAY_FILE.fullmatch(entry.name)
                if not match:
                    continue
                try:
                    file_day = audit_day(match.group(1))
                except ValueError:
                    continue
                if file_day >= cutoff:
                    continue
                info = os.stat(entry.name, dir_fd=directory_fd, follow_symlinks=False)
                if not stat.S_ISREG(info.st_mode):
                    skipped_unsafe += 1
                    continue
                selected.append((entry.name, info.st_dev, info.st_ino))
        for name, device, inode in sorted(selected):
            try:
                current = direct_regular(directory_fd, name)
            except (OSError, ValueError) as exc:
                raise ValueError(
                    f"audit entry cannot be rechecked: {name}; removed={removed}"
                ) from exc
            if (current.st_dev, current.st_ino) != (device, inode):
                raise ValueError(
                    f"audit entry identity changed: {name}; removed={removed}"
                )
            if not dry_run:
                try:
                    os.unlink(name, dir_fd=directory_fd)
                except OSError as exc:
                    raise OSError(
                        f"audit retention deletion failed: {name}; removed={removed}"
                    ) from exc
                removed += 1
        return {
            "frozenUtcDate": day.isoformat(),
            "retainedFrom": cutoff.isoformat(),
            "selected": len(selected),
            "removed": removed,
            "skippedUnsafe": skipped_unsafe,
            "dryRun": dry_run,
        }
    finally:
        os.close(directory_fd)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("verify", "retain"))
    parser.add_argument("--audit-dir", type=Path, required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--run-id")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        day = audit_day(args.date)
        if args.action == "verify":
            result = verify_export(args.audit_dir, day, args.run_id or "")
        else:
            result = retain(args.audit_dir, day, dry_run=args.dry_run)
    except (OSError, ValueError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"audit {args.action} failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
