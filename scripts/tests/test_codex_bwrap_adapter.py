"""Argument contracts for rootless masks; no real mount operations."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


@unittest.skipUnless(os.name == "posix", "Linux adapter uses POSIX ownership semantics")
class BwrapAdapterTests(unittest.TestCase):
    def run_adapter(self, args, unsafe=False, target_state=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            real = root / "real"
            real.write_text('#!/usr/bin/env python3\nimport json,sys\nprint(json.dumps(sys.argv[1:]))\n')
            real.chmod(0o755)
            empty = root / "empty"
            empty.mkdir(mode=0o555)
            target = root / 'project' / '.aws'
            target.parent.mkdir()
            if target_state == 'empty':
                target.mkdir()
            elif target_state == 'nonempty':
                target.mkdir()
                (target / 'user-data').write_text('preserve')
            elif target_state == 'symlink':
                target.symlink_to(root, target_is_directory=True)
            args = [arg.replace('@target@', str(target)) for arg in args]
            if unsafe:
                empty.rmdir()
                empty.symlink_to(root, target_is_directory=True)
            stat = root / "stat"
            stat.write_text('#!/bin/sh\necho 0\n')
            stat.chmod(0o755)
            source = (ROOT / "scripts/codex-bwrap-wrapper.sh").read_text()
            source = source.replace('/usr/libexec/codex-bwrap.real', str(real))
            source = source.replace('/usr/libexec/codex-empty-readonly', str(empty))
            wrapper = root / "wrapper"
            wrapper.write_text(source)
            result = subprocess.run(["bash", str(wrapper), *args], text=True,
                capture_output=True, env={**os.environ,
                    "PATH": str(root) + os.pathsep + os.environ["PATH"]})
            return result

    def test_current_uid_daemon_remains_empty_and_inaccessible(self):
        path = f"/tmp/codex-daemon-{os.getuid()}"
        result = self.run_adapter(["--perms", "000", "--tmpfs", path,
                                   "--remount-ro", path, "--", "true"])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout),
                         ["--perms", "000", "--tmpfs", path, "--", "true"])

    def test_unrecognized_path_and_mode_are_not_rewritten(self):
        for path, mode in (("/tmp/unrelated", "000"),
                           (f"/tmp/codex-daemon-{os.getuid()}", "555")):
            args = ["--perms", mode, "--tmpfs", path, "--remount-ro", path]
            self.assertEqual(json.loads(self.run_adapter(args).stdout), args)

    def test_missing_metadata_uses_readonly_empty_bind(self):
        args = ["--perms", "555", "--tmpfs", "/ade-fixture-absent/.aws",
                "--remount-ro", "/ade-fixture-absent/.aws"]
        result = self.run_adapter(args)
        self.assertEqual(result.returncode, 0, result.stderr)
        actual = json.loads(result.stdout)
        self.assertEqual(actual[0], "--ro-bind")
        self.assertEqual(actual[2], "/ade-fixture-absent/.aws")
        self.assertNotIn("--bind", actual)

    def test_unsafe_placeholder_blocks(self):
        result = self.run_adapter(["--perms", "555", "--tmpfs", "/ade-fixture-absent/.aws",
                                  "--remount-ro", "/ade-fixture-absent/.aws"], unsafe=True)
        self.assertEqual(result.returncode, 126)

    def test_only_empty_existing_targets_are_replaced(self):
        args = ["--perms", "555", "--tmpfs", "@target@", "--remount-ro", "@target@"]
        self.assertEqual(json.loads(self.run_adapter(args, target_state='empty').stdout)[0], '--ro-bind')
        for state in ('nonempty', 'symlink'):
            result = self.run_adapter(args, target_state=state)
            self.assertEqual(json.loads(result.stdout)[0:3], ['--perms', '555', '--tmpfs'])
