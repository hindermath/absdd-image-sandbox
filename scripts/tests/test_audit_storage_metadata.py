#!/usr/bin/env python3
"""DE: Audit liest keine V2-Inhalte. EN: Audit never reads V2 contents."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]


class AuditStorageMetadataTests(unittest.TestCase):
    def run_export(self, runner, state):
        executable = shutil.which(runner)
        if not executable or not shutil.which("jq"):
            self.skipTest(f"{runner} and jq are required")
        with tempfile.TemporaryDirectory(prefix="ade-audit-metadata-") as directory:
            root = Path(directory)
            opencode = root / "opencode"
            opencode.mkdir()
            database = opencode / "opencode.db"
            content = b"PRIVATE-CONTENT-MUST-NOT-APPEAR\x00not-a-database"
            if state == "file":
                database.write_bytes(content)
            elif state == "symlink":
                secret = root / "unrelated.db"
                secret.write_bytes(content)
                database.symlink_to(secret)
            legacy = opencode / "storage/session_diff"
            legacy.mkdir(parents=True)
            (legacy / "ses_fixture.json").write_text("PRIVATE-LEGACY-CONTENT")
            bin_dir = root / "bin"
            bin_dir.mkdir()
            for name in ("opencode", "codex", "claude", "agy", "copilot"):
                command = bin_dir / name
                command.write_text("#!/bin/sh\nprintf 'fixture-version\\n'\n")
                command.chmod(0o755)
            env = dict(os.environ, PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
                       OPENCODE_DATA_DIR=str(opencode), AUDIT_DIR=str(root / "audit"),
                       AUDIT_PROJECT_PATH="/fixture", CODEX_DATA_DIR=str(root / "codex"),
                       CLAUDE_DATA_DIR=str(root / "claude"),
                       GEMINI_CLI_HOME=str(root / "gemini"),
                       COPILOT_HOME=str(root / "copilot"))
            env.pop("AUDIT_OUTPUT", None)
            if runner == "bash":
                command = [executable, str(ROOT / "scripts/audit-export.sh")]
            else:
                command = [executable, "-NoProfile", "-File",
                           str(ROOT / "scripts/audit-export.ps1")]
            result = subprocess.run(command, env=env, capture_output=True, text=True,
                                    check=True, timeout=40)
            lines = next((root / "audit").glob("*.jsonl")).read_text()
            self.assertNotIn("PRIVATE", lines + result.stdout + result.stderr)
            records = [json.loads(line) for line in lines.splitlines()]
            storage = [item for item in records
                       if item.get("record_type") == "storage-metadata"]
            self.assertEqual(len(storage), int(state == "file"))
            if storage:
                self.assertEqual(set(storage[0]), {
                    "record_type", "tool", "storage_format", "source_path",
                    "modified_at", "exported_at", "session_coverage",
                })
                self.assertEqual(storage[0]["session_coverage"], "not-exported")
                self.assertNotIn("session_id", storage[0])
                self.assertEqual(database.read_bytes(), content)
            self.assertEqual(sum(item.get("session_id") == "ses_fixture"
                                 for item in records), 1)

    def test_bash_database_metadata_only(self):
        self.run_export("bash", "file")

    def test_powershell_database_metadata_only(self):
        self.run_export("pwsh", "file")

    def test_bash_skips_symlink(self):
        self.run_export("bash", "symlink")

    def test_powershell_skips_symlink(self):
        self.run_export("pwsh", "symlink")

    def test_bash_absent_database(self):
        self.run_export("bash", "absent")

    def test_powershell_absent_database(self):
        self.run_export("pwsh", "absent")


if __name__ == "__main__":
    unittest.main()
