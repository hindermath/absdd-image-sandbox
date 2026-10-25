#!/usr/bin/env python3
"""Exercise both stop wrappers using fake engines, never real Podman."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
ENGINE = '''#!/bin/sh
printf '%s\\n' "$*" >> "$ADE_TEST_CALLS"
case "$*" in
  *"exec -T ade audit-export"*) exit "$ADE_TEST_AUDIT_EXIT" ;;
esac
exit "$ADE_TEST_DOWN_EXIT"
'''


class AuditShutdownFailClosedTests(unittest.TestCase):
    def check_case(self, runner, engine, volume, audit_exit, down_exit):
        executable = shutil.which(runner)
        if not executable:
            self.skipTest(f"{runner} unavailable")
        with tempfile.TemporaryDirectory(prefix="ade-audit-stop-") as directory:
            root = Path(directory)
            fake = root / engine
            fake.write_text(ENGINE)
            fake.chmod(0o755)
            log = root / "calls.txt"
            env = dict(os.environ, PATH=f"{root}{os.pathsep}{os.environ['PATH']}",
                       ADE_TEST_CALLS=str(log), ADE_TEST_AUDIT_EXIT=str(audit_exit),
                       ADE_TEST_DOWN_EXIT=str(down_exit))
            if runner == "bash":
                command = [executable, str(ROOT / "scripts/compose-down-with-audit.sh"),
                           "--" + engine] + ([volume] if volume else [])
            else:
                script = str(ROOT / "scripts/compose-down-with-audit.ps1").replace("'", "''")
                extra = " -Volumes" if volume == "-v" else (
                    " -DownArgs @('--volumes')" if volume else "")
                command = [executable, "-NoProfile", "-Command",
                           f"& '{script}' -Engine {engine}{extra}; exit $LASTEXITCODE"]
            result = subprocess.run(command, env=env, text=True, capture_output=True,
                                    timeout=30)
            self.assertEqual(result.returncode, audit_exit or down_exit,
                             result.stdout + result.stderr)
            calls = log.read_text().splitlines()
            self.assertIn("exec -T ade audit-export", calls[0])
            self.assertEqual(len(calls), 1 if audit_exit else 2)
            if not audit_exit:
                self.assertIn("down", calls[1])
                if volume:
                    self.assertIn(volume, calls[1])

    def test_failed_export_blocks_every_down_variant(self):
        for runner in ("bash", "pwsh"):
            for engine in ("podman", "podman-compose"):
                for volume in ("", "-v", "--volumes"):
                    with self.subTest(runner=runner, engine=engine, volume=volume):
                        self.check_case(runner, engine, volume, 7, 0)

    def test_successful_export_precedes_down(self):
        for runner in ("bash", "pwsh"):
            for engine in ("podman", "podman-compose"):
                for volume in ("", "-v", "--volumes"):
                    with self.subTest(runner=runner, engine=engine, volume=volume):
                        self.check_case(runner, engine, volume, 0, 0)

    def test_down_exit_code_is_preserved(self):
        for runner in ("bash", "pwsh"):
            with self.subTest(runner=runner):
                self.check_case(runner, "podman", "", 0, 11)


if __name__ == "__main__":
    unittest.main()
