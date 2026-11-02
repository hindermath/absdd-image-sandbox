"""Additional fail-closed audit cases using owned synthetic POSIX directories."""

from __future__ import annotations

import contextlib
from datetime import date
import importlib.util
import io
import json
import os
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "audit_retention_coverage", ROOT / "scripts/lib/audit_retention.py"
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)
DAY = date(2026, 11, 2)
RUN = "00000000-0000-4000-8000-000000000001"


def record(**changes):
    return {
        "record_type": "audit-export-run", "run_id": RUN,
        "audit_date": DAY.isoformat(),
        "session_coverage": "filesystem-metadata-only",
        "session_metadata_count": 0, **changes,
    }


class AuditInputCoverageTests(unittest.TestCase):
    def test_dates_are_valid_and_canonical(self):
        self.assertEqual(AUDIT.audit_day("2024-02-29"), date(2024, 2, 29))
        for value in ("20260230", "20261102", "not-a-day", "2026-W45-1"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                AUDIT.audit_day(value)

    def test_missing_directory_and_symlink_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with self.assertRaises(ValueError):
                AUDIT.open_audit_directory(root / "missing")
            link = root / "link"
            try:
                link.symlink_to(root, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("Native symlink creation unavailable")
            with self.assertRaises(ValueError):
                AUDIT.open_audit_directory(link)

    def test_missing_native_capability_is_fail_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            with mock.patch.object(AUDIT.os, "supports_dir_fd", set()):
                with self.assertRaisesRegex(ValueError, "native no-follow"):
                    AUDIT.open_audit_directory(Path(temporary))


@unittest.skipUnless(
    hasattr(os, "O_NOFOLLOW") and os.open in os.supports_dir_fd,
    "Native POSIX directory-descriptor operations required; no Windows claim",
)
class AuditNativeCoverageTests(unittest.TestCase):
    def test_dry_run_selects_without_deletion(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            old = root / "2026-09-01.jsonl"
            old.write_text("{}\n", encoding="utf-8")
            result = AUDIT.retain(root, DAY, dry_run=True)
            self.assertEqual((result["selected"], result["removed"]), (1, 0))
            self.assertTrue(old.is_file())

    def test_recheck_failure_preserves_the_selected_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            old = root / "2026-09-01.jsonl"
            old.write_text("{}\n", encoding="utf-8")
            with mock.patch.object(AUDIT, "direct_regular", side_effect=FileNotFoundError):
                with self.assertRaisesRegex(ValueError, "cannot be rechecked"):
                    AUDIT.retain(root, DAY)
            self.assertTrue(old.is_file())

    def test_changed_identity_is_not_deleted(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            old = root / "2026-09-01.jsonl"
            old.write_text("{}\n", encoding="utf-8")
            info = old.stat()
            changed = SimpleNamespace(st_dev=info.st_dev, st_ino=info.st_ino + 1)
            with mock.patch.object(AUDIT, "direct_regular", return_value=changed):
                with self.assertRaisesRegex(ValueError, "identity changed"):
                    AUDIT.retain(root, DAY)
            self.assertTrue(old.is_file())

    def test_export_run_id_is_required(self):
        for value in ("", "short", "g" * 36):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as temporary:
                with self.assertRaisesRegex(ValueError, "run id"):
                    AUDIT.verify_export(Path(temporary), DAY, value)

    def test_export_skips_blank_and_foreign_records(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            rows = ["", json.dumps({"record_type": "synthetic-other"}),
                    json.dumps(record()), ""]
            (root / f"{DAY}.jsonl").write_text("\n".join(rows), encoding="utf-8")
            result = AUDIT.verify_export(root, DAY, RUN)
            self.assertEqual(result["recordCount"], 2)
            self.assertEqual(result["sessionMetadataCount"], 0)

    def test_duplicate_run_and_wrong_scope_are_rejected(self):
        cases = [
            (json.dumps(record()) + "\n") * 2,
            json.dumps(record(session_coverage="unexpected")) + "\n",
            json.dumps(record(run_id="00000000-0000-4000-8000-000000000002")) + "\n",
        ]
        for payload in cases:
            with self.subTest(payload=payload), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                (root / f"{DAY}.jsonl").write_text(payload, encoding="utf-8")
                with self.assertRaises(ValueError):
                    AUDIT.verify_export(root, DAY, RUN)

    def test_oversized_malformed_and_non_utf8_records_are_rejected(self):
        cases = [b"x" * (1024 * 1024 + 2), b"{invalid}\n", b"\xff\n"]
        for payload in cases:
            with self.subTest(size=len(payload)), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                (root / f"{DAY}.jsonl").write_bytes(payload)
                with self.assertRaises((ValueError, UnicodeError)):
                    AUDIT.verify_export(root, DAY, RUN)

    def test_opened_export_identity_must_match_precheck(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / f"{DAY}.jsonl").write_text(json.dumps(record()) + "\n", encoding="utf-8")
            changed = SimpleNamespace(st_dev=-1, st_ino=-1)
            with mock.patch.object(AUDIT.os, "fstat", return_value=changed):
                with self.assertRaisesRegex(ValueError, "identity changed"):
                    AUDIT.verify_export(root, DAY, RUN)

    def test_main_retain_verify_and_validation_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / f"{DAY}.jsonl").write_text(json.dumps(record()) + "\n", encoding="utf-8")
            cases = [
                (["retain", "--date", str(DAY), "--dry-run"], 0),
                (["verify", "--date", str(DAY), "--run-id", RUN], 0),
                (["retain", "--date", "invalid"], 1),
                (["verify", "--date", str(DAY)], 1),
            ]
            for args, expected in cases:
                with self.subTest(args=args), mock.patch.object(
                    AUDIT.sys, "argv", ["audit", *args, "--audit-dir", str(root)]
                ), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(AUDIT.main(), expected)


if __name__ == "__main__":
    unittest.main()
