#!/usr/bin/env python3
"""Exercise both stop wrappers using fake engines, never real Podman."""

import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
ENGINE = '''#!/bin/sh
printf '%s\\n' "$*" >> "$ADE_TEST_CALLS"
case "$*" in
  *"/usr/bin/test -f /audit/.audit-mount."*)
    [ "$ADE_TEST_MOUNT_VISIBLE" -eq 1 ] || exit 1
    marker="${ADE_TEST_AUDIT_DIR}/$(basename "$*")"
    test -f "$marker"
    exit $?
    ;;
  *"/usr/local/bin/audit-export"*)
    [ "$ADE_TEST_AUDIT_EXIT" -eq 0 ] || exit "$ADE_TEST_AUDIT_EXIT"
    [ "$ADE_TEST_WRITE_ARTIFACT" -eq 1 ] || exit 0
    day=''
    run=''
    for arg in "$@"; do
      case "$arg" in
        AUDIT_DATE=*) day="${arg#AUDIT_DATE=}" ;;
        AUDIT_RUN_ID=*) run="${arg#AUDIT_RUN_ID=}" ;;
      esac
    done
    case "$ADE_TEST_ARTIFACT_MODE" in
      empty) : > "$ADE_TEST_AUDIT_DIR/$day.jsonl" ;;
      stale) printf '{"record_type":"audit-export-run","run_id":"old-run","audit_date":"%s","session_coverage":"filesystem-metadata-only","session_metadata_count":0}\\n' "$day" > "$ADE_TEST_AUDIT_DIR/$day.jsonl" ;;
      link) printf 'foreign metadata\\n' > "$ADE_TEST_AUDIT_DIR/foreign.jsonl"; ln -s "$ADE_TEST_AUDIT_DIR/foreign.jsonl" "$ADE_TEST_AUDIT_DIR/$day.jsonl" ;;
      *) printf '{"record_type":"audit-export-run","run_id":"%s","audit_date":"%s","session_coverage":"filesystem-metadata-only","session_metadata_count":0}\\n' "$run" "$day" > "$ADE_TEST_AUDIT_DIR/$day.jsonl" ;;
    esac
    exit 0
    ;;
  *"/usr/local/bin/audit-retention verify"*)
    day=''
    run=''
    previous=''
    for arg in "$@"; do
      case "$previous" in
        --date) day="$arg" ;;
        --run-id) run="$arg" ;;
      esac
      previous="$arg"
    done
    python3 "$ADE_TEST_HELPER" verify --audit-dir "$ADE_TEST_AUDIT_DIR" --date "$day" --run-id "$run"
    exit $?
    ;;
  *"/usr/local/bin/audit-retention retain"*)
    if [ "$ADE_TEST_RETAIN_EXIT" -ne 0 ]; then
      printf 'audit retention deletion failed: 2026-01-01.jsonl; removed=1\\n' >&2
      exit "$ADE_TEST_RETAIN_EXIT"
    fi
    day=''
    previous=''
    for arg in "$@"; do
      [ "$previous" = "--date" ] && day="$arg"
      previous="$arg"
    done
    python3 "$ADE_TEST_HELPER" retain --audit-dir "$ADE_TEST_AUDIT_DIR" --date "$day"
    exit $?
    ;;
  down*|*" down"*)
    case "$*" in
      *" --unsupported"|*" --timeout") exit 2 ;;
    esac
    exit "$ADE_TEST_DOWN_EXIT"
    ;;
esac
exit 2
'''


class AuditShutdownFailClosedTests(unittest.TestCase):
    def check_case(self, runner, engine, volume, audit_exit, down_exit,
                   write_artifact=True, artifact_mode="current", mount_visible=True):
        executable = shutil.which(runner)
        if not executable:
            self.skipTest(f"{runner} unavailable")
        with tempfile.TemporaryDirectory(prefix="ade-audit-stop-") as directory:
            root = Path(directory)
            fake = root / engine
            fake.write_text(ENGINE)
            fake.chmod(0o755)
            log = root / "calls.txt"
            audit_dir = root / "audit"
            audit_dir.mkdir()
            env = dict(os.environ, PATH=f"{root}{os.pathsep}{os.environ['PATH']}",
                       ADE_TEST_CALLS=str(log), ADE_TEST_AUDIT_EXIT=str(audit_exit),
                       ADE_TEST_DOWN_EXIT=str(down_exit),
                       ADE_TEST_AUDIT_DIR=str(audit_dir), AUDIT_DIR=str(audit_dir),
                       ADE_TEST_HELPER=str(ROOT / "scripts/lib/audit_retention.py"),
                       ADE_TEST_WRITE_ARTIFACT="1" if write_artifact else "0",
                       ADE_TEST_ARTIFACT_MODE=artifact_mode,
                       ADE_TEST_MOUNT_VISIBLE="1" if mount_visible else "0",
                       ADE_TEST_RETAIN_EXIT="0")
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
            expected = 1 if not mount_visible else (
                audit_exit or (1 if not write_artifact or artifact_mode != "current"
                               else down_exit))
            self.assertEqual(result.returncode, expected,
                             result.stdout + result.stderr)
            calls = log.read_text().splitlines()
            self.assertIn("exec -T ade /usr/bin/test -f /audit/.audit-mount.", calls[0])
            if not mount_visible:
                self.assertEqual(len(calls), 1)
                return
            self.assertIn("/usr/local/bin/audit-export", calls[1])
            expected_calls = 2 if audit_exit or not write_artifact or artifact_mode in ("empty", "link") else (
                3 if artifact_mode == "stale" else 5)
            self.assertEqual(len(calls), expected_calls)
            if not audit_exit and write_artifact and artifact_mode not in ("empty", "link"):
                self.assertIn("audit-retention verify", calls[2])
            if not audit_exit and write_artifact and artifact_mode == "current":
                self.assertIn("audit-retention retain", calls[3])
                self.assertIn("down", calls[4])
                if volume:
                    self.assertIn(volume, calls[4])

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

    def test_exit_zero_without_current_artifact_blocks_down(self):
        for runner in ("bash", "pwsh"):
            with self.subTest(runner=runner):
                self.check_case(runner, "podman", "", 0, 0,
                                write_artifact=False)

    def test_empty_stale_and_wrong_mount_block_down(self):
        for runner in ("bash", "pwsh"):
            for mode in ("empty", "stale", "link"):
                with self.subTest(runner=runner, mode=mode):
                    self.check_case(runner, "podman", "", 0, 0,
                                    artifact_mode=mode)
            with self.subTest(runner=runner, mode="wrong-mount"):
                self.check_case(runner, "podman", "", 0, 0,
                                mount_visible=False)

    def test_preview_is_write_free_and_never_calls_compose(self):
        for runner in ("bash", "pwsh"):
            executable = shutil.which(runner)
            if not executable:
                continue
            with self.subTest(runner=runner), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                audit_dir = root / "Prüfung mit Leerzeichen"
                calls = root / "calls.txt"
                env = dict(os.environ, AUDIT_DIR=str(audit_dir),
                           ADE_TEST_CALLS=str(calls))
                if runner == "bash":
                    command = [executable, str(ROOT / "scripts/compose-down-with-audit.sh"),
                               "--podman", "--dry-run"]
                else:
                    command = [executable, "-NoProfile", "-File",
                               str(ROOT / "scripts/compose-down-with-audit.ps1"),
                               "-Engine", "podman", "-WhatIf"]
                result = subprocess.run(command, env=env, capture_output=True,
                                        text=True, timeout=20)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("DRY-RUN", result.stdout)
                self.assertFalse(audit_dir.exists())
                self.assertFalse(calls.exists())

    def test_foreign_lock_blocks_without_export_or_down(self):
        for runner, lock_kind in (("bash", "directory"), ("pwsh", "file")):
            executable = shutil.which(runner)
            if not executable:
                continue
            with self.subTest(runner=runner), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                audit_dir = root / "Prüfung mit Leerzeichen"
                audit_dir.mkdir()
                lock = audit_dir / ".audit-stop.lock"
                if lock_kind == "directory":
                    lock.mkdir()
                    (lock / "owner").write_text("foreign-run")
                else:
                    lock.write_text("foreign-run")
                calls = root / "calls.txt"
                env = dict(os.environ, AUDIT_DIR=str(audit_dir),
                           ADE_TEST_CALLS=str(calls))
                if runner == "bash":
                    command = [executable, str(ROOT / "scripts/compose-down-with-audit.sh"),
                               "--podman"]
                else:
                    command = [executable, "-NoProfile", "-File",
                               str(ROOT / "scripts/compose-down-with-audit.ps1"),
                               "-Engine", "podman"]
                result = subprocess.run(command, env=env, capture_output=True,
                                        text=True, timeout=20)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(calls.exists())
                self.assertEqual((lock / "owner").read_text() if lock_kind == "directory"
                                 else lock.read_text(), "foreign-run")

    def test_partial_retention_failure_reports_count_and_allows_retry(self):
        for runner in ("bash", "pwsh"):
            executable = shutil.which(runner)
            if not executable:
                continue
            with self.subTest(runner=runner), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                fake = root / "podman"
                fake.write_text(ENGINE)
                fake.chmod(0o755)
                audit_dir = root / "Prüfung mit Leerzeichen"
                audit_dir.mkdir()
                calls = root / "calls.txt"
                env = dict(os.environ, PATH=f"{root}{os.pathsep}{os.environ['PATH']}",
                           AUDIT_DIR=str(audit_dir), ADE_TEST_AUDIT_DIR=str(audit_dir),
                           ADE_TEST_CALLS=str(calls), ADE_TEST_AUDIT_EXIT="0",
                           ADE_TEST_DOWN_EXIT="0", ADE_TEST_WRITE_ARTIFACT="1",
                           ADE_TEST_ARTIFACT_MODE="current", ADE_TEST_MOUNT_VISIBLE="1",
                           ADE_TEST_RETAIN_EXIT="9", ADE_TEST_HELPER=str(
                               ROOT / "scripts/lib/audit_retention.py"))
                if runner == "bash":
                    command = [executable, str(ROOT / "scripts/compose-down-with-audit.sh"),
                               "--podman"]
                else:
                    command = [executable, "-NoProfile", "-File",
                               str(ROOT / "scripts/compose-down-with-audit.ps1"),
                               "-Engine", "podman"]
                failed = subprocess.run(command, env=env, capture_output=True,
                                        text=True, timeout=30)
                self.assertNotEqual(failed.returncode, 0)
                self.assertIn("removed=1", failed.stderr)
                self.assertEqual(len(calls.read_text().splitlines()), 4)
                self.assertFalse((audit_dir / ".audit-stop.lock").exists())
                env["ADE_TEST_RETAIN_EXIT"] = "0"
                retried = subprocess.run(command, env=env, capture_output=True,
                                         text=True, timeout=30)
                self.assertEqual(retried.returncode, 0, retried.stderr)
                self.assertIn("down", calls.read_text().splitlines()[-1])

    def test_vertical_stop_keeps_project_and_agent_state(self):
        for runner in ("bash", "pwsh"):
            executable = shutil.which(runner)
            if not executable:
                continue
            with self.subTest(runner=runner), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                fake = root / "podman"
                fake.write_text(ENGINE)
                fake.chmod(0o755)
                audit_dir = root / "audit"
                audit_dir.mkdir()
                today = datetime.now(timezone.utc).date()
                old = audit_dir / f"{today - timedelta(days=30)}.jsonl"
                recent = audit_dir / f"{today - timedelta(days=29)}.jsonl"
                old.write_text("old metadata\n")
                recent.write_text("recent metadata\n")
                project = root / "project" / "lesson.txt"
                project.parent.mkdir()
                project.write_text("synthetic lesson")
                agent = root / "agent-state" / "session.txt"
                agent.parent.mkdir()
                agent.write_text("synthetic state")
                calls = root / "calls.txt"
                env = dict(os.environ, PATH=f"{root}{os.pathsep}{os.environ['PATH']}",
                           AUDIT_DIR=str(audit_dir), ADE_TEST_AUDIT_DIR=str(audit_dir),
                           ADE_TEST_CALLS=str(calls), ADE_TEST_AUDIT_EXIT="0",
                           ADE_TEST_DOWN_EXIT="0", ADE_TEST_WRITE_ARTIFACT="1",
                           ADE_TEST_ARTIFACT_MODE="current", ADE_TEST_MOUNT_VISIBLE="1",
                           ADE_TEST_RETAIN_EXIT="0", ADE_TEST_HELPER=str(
                               ROOT / "scripts/lib/audit_retention.py"))
                if runner == "bash":
                    command = [executable, str(ROOT / "scripts/compose-down-with-audit.sh"),
                               "--podman"]
                else:
                    command = [executable, "-NoProfile", "-File",
                               str(ROOT / "scripts/compose-down-with-audit.ps1"),
                               "-Engine", "podman"]
                result = subprocess.run(command, env=env, capture_output=True,
                                        text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertFalse(old.exists())
                self.assertTrue(recent.exists())
                self.assertEqual(project.read_text(), "synthetic lesson")
                self.assertEqual(agent.read_text(), "synthetic state")
                self.assertEqual(calls.read_text().splitlines()[-1], "compose down")

    def test_ordered_down_options_are_forwarded_without_volume_removal(self):
        for runner in ("bash", "pwsh"):
            executable = shutil.which(runner)
            if not executable:
                continue
            with self.subTest(runner=runner), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                fake = root / "podman"
                fake.write_text(ENGINE)
                fake.chmod(0o755)
                audit_dir = root / "audit"
                audit_dir.mkdir()
                calls = root / "calls.txt"
                env = dict(os.environ, PATH=f"{root}{os.pathsep}{os.environ['PATH']}",
                           AUDIT_DIR=str(audit_dir), ADE_TEST_AUDIT_DIR=str(audit_dir),
                           ADE_TEST_CALLS=str(calls), ADE_TEST_AUDIT_EXIT="0",
                           ADE_TEST_DOWN_EXIT="0", ADE_TEST_WRITE_ARTIFACT="1",
                           ADE_TEST_ARTIFACT_MODE="current", ADE_TEST_MOUNT_VISIBLE="1",
                           ADE_TEST_RETAIN_EXIT="0", ADE_TEST_HELPER=str(
                               ROOT / "scripts/lib/audit_retention.py"))
                if runner == "bash":
                    command = [executable, str(ROOT / "scripts/compose-down-with-audit.sh"),
                               "--podman", "--remove-orphans", "--timeout", "5"]
                else:
                    script = str(ROOT / "scripts/compose-down-with-audit.ps1").replace("'", "''")
                    command = [executable, "-NoProfile", "-Command",
                               f"& '{script}' -Engine podman -RemoveOrphans -DownArgs @('--timeout','5')"]
                result = subprocess.run(command, env=env, capture_output=True,
                                        text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(calls.read_text().splitlines()[-1],
                                 "compose down --remove-orphans --timeout 5")

    def test_unknown_or_missing_down_argument_preserves_compose_error(self):
        for runner in ("bash", "pwsh"):
            executable = shutil.which(runner)
            if not executable:
                continue
            for invalid in ("--unsupported", "--timeout"):
                with self.subTest(runner=runner, invalid=invalid), tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    fake = root / "podman"
                    fake.write_text(ENGINE)
                    fake.chmod(0o755)
                    audit_dir = root / "audit"
                    audit_dir.mkdir()
                    calls = root / "calls.txt"
                    env = dict(os.environ, PATH=f"{root}{os.pathsep}{os.environ['PATH']}",
                               AUDIT_DIR=str(audit_dir), ADE_TEST_AUDIT_DIR=str(audit_dir),
                               ADE_TEST_CALLS=str(calls), ADE_TEST_AUDIT_EXIT="0",
                               ADE_TEST_DOWN_EXIT="0", ADE_TEST_WRITE_ARTIFACT="1",
                               ADE_TEST_ARTIFACT_MODE="current", ADE_TEST_MOUNT_VISIBLE="1",
                               ADE_TEST_RETAIN_EXIT="0", ADE_TEST_HELPER=str(
                                   ROOT / "scripts/lib/audit_retention.py"))
                    if runner == "bash":
                        command = [executable,
                                   str(ROOT / "scripts/compose-down-with-audit.sh"),
                                   "--podman", invalid]
                    else:
                        script = str(ROOT / "scripts/compose-down-with-audit.ps1").replace("'", "''")
                        command = [executable, "-NoProfile", "-Command",
                                   f"& '{script}' -Engine podman -DownArgs @('{invalid}'); exit $LASTEXITCODE"]
                    result = subprocess.run(command, env=env, capture_output=True,
                                            text=True, timeout=30)
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertEqual(calls.read_text().splitlines()[-1],
                                     f"compose down {invalid}")


if __name__ == "__main__":
    unittest.main()
