"""Isolated UTC retention and current-run verification tests."""

from __future__ import annotations

from datetime import date
import json
import os
from pathlib import Path
import tempfile
import unittest
import importlib.util
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "audit_retention", ROOT / "scripts/lib/audit_retention.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


@unittest.skipUnless(
    hasattr(os, "O_NOFOLLOW") and os.open in os.supports_dir_fd,
    "native no-follow dirfd operations unavailable",
)
class AuditRetentionTests(unittest.TestCase):
    def test_exact_thirty_day_utc_window_and_foreign_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in (
                "2026-09-29.jsonl", "2026-09-30.jsonl",
                "2026-10-01.jsonl", "2026-10-02.jsonl", "2026-10-30.jsonl",
                "2026-10-31.jsonl", "2026-11-01.jsonl",
                "2026-09-29.json", "2026-09-31.jsonl",
            ):
                (root / name).write_text("{}\n")
            (root / "2026-09-28.jsonl").mkdir()
            outside = root.parent / (root.name + "-outside")
            outside.write_text("untouched")
            (root / "historical-link").symlink_to(outside)
            result = MODULE.retain(root, date(2026, 10, 31))
            self.assertEqual(result["removed"], 3)
            self.assertFalse((root / "2026-09-29.jsonl").exists())
            self.assertFalse((root / "2026-09-30.jsonl").exists())
            self.assertFalse((root / "2026-10-01.jsonl").exists())
            self.assertTrue((root / "2026-10-02.jsonl").exists())
            self.assertTrue((root / "2026-11-01.jsonl").exists())
            self.assertEqual(outside.read_text(), "untouched")
            outside.unlink()

    def test_old_symlink_is_skipped_without_deleting_target(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            outside = root.parent / (root.name + "-outside")
            outside.write_text("untouched")
            (root / "2026-09-30.jsonl").symlink_to(outside)
            result = MODULE.retain(root, date(2026, 10, 31))
            self.assertEqual(result["skippedUnsafe"], 1)
            self.assertEqual(outside.read_text(), "untouched")
            outside.unlink()

    def test_leap_month_boundary_and_mtime_do_not_change_name_selection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            old = root / "2024-01-31.jsonl"
            first_kept = root / "2024-02-01.jsonl"
            leap_day = root / "2024-02-29.jsonl"
            for path in (old, first_kept, leap_day):
                path.write_text("{}\n")
            os.utime(old, (4102444800, 4102444800))
            os.utime(first_kept, (0, 0))

            result = MODULE.retain(root, date(2024, 3, 1))

            self.assertEqual(result["retainedFrom"], "2024-02-01")
            self.assertEqual(result["removed"], 1)
            self.assertFalse(old.exists())
            self.assertTrue(first_kept.exists())
            self.assertTrue(leap_day.exists())

    def test_current_export_requires_matching_run_record(self):
        run_id = "00000000-0000-4000-8000-000000000001"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "2026-10-31.jsonl"
            with self.assertRaises(FileNotFoundError):
                MODULE.verify_export(root, date(2026, 10, 31), run_id)
            path.write_text("")
            with self.assertRaises(ValueError):
                MODULE.verify_export(root, date(2026, 10, 31), run_id)
            path.write_text(json.dumps({
                "record_type": "audit-export-run",
                "run_id": run_id,
                "audit_date": "2026-10-31",
                "session_coverage": "filesystem-metadata-only",
                "session_metadata_count": 0,
            }) + "\n")
            self.assertTrue(
                MODULE.verify_export(root, date(2026, 10, 31), run_id)["verified"]
            )
            with self.assertRaises(ValueError):
                MODULE.verify_export(
                    root, date(2026, 10, 31),
                    "00000000-0000-4000-8000-000000000002",
                )

    def test_partial_retention_error_reports_already_removed_count(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "2026-09-29.jsonl").write_text("{}\n")
            (root / "2026-09-30.jsonl").write_text("{}\n")
            real_unlink = os.unlink

            def fail_second(name, *, dir_fd=None):
                if name == "2026-09-30.jsonl":
                    raise OSError("synthetic deletion failure")
                return real_unlink(name, dir_fd=dir_fd)

            with mock.patch.object(MODULE.os, "unlink", side_effect=fail_second):
                with self.assertRaisesRegex(OSError, "removed=1"):
                    MODULE.retain(root, date(2026, 10, 31))
            self.assertFalse((root / "2026-09-29.jsonl").exists())
            self.assertTrue((root / "2026-09-30.jsonl").exists())


if __name__ == "__main__":
    unittest.main()
