"""Real isolated children and native previews; no actual runtime/provider calls.

DE: Nur eigene Fixtures. EN: Source-bound children with explicit proof limits.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("child_program_fixtures",
    ROOT / "scripts/lib/maintenance_execution_context.py")
context = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(context)


class ChildAndPreviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ade004-child-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self.log = self.root / "unexpected-command.json"
        fake_git = self.bin / "git"
        fake_git.write_text(f"#!{sys.executable}\nimport json,os,pathlib,sys\n"
            "pathlib.Path(os.environ['ADE_CHILD_LOG']).write_text(json.dumps(sys.argv[1:]))\n"
            "print('synthetic git')\n")
        fake_git.chmod(0o755)
        (self.bin / "python3").symlink_to(sys.executable)
        for name in ("bash", "pwsh", "podman", "docker"):
            fake = self.bin / name
            fake.write_text("#!/bin/sh\nexit 99\n")
            fake.chmod(0o755)
        self.env = {key: value for key, value in os.environ.items()
            if key in ("TMPDIR", "TMP", "TEMP", "LANG", "LC_ALL", "ADE_COVERAGE_REPO",
                       "COVERAGE_RCFILE", "COVERAGE_FILE") or key.startswith("COVERAGE_PROCESS_")}
        self.env.update(HOME=str(self.root), USERPROFILE=str(self.root), PATH=f"{self.bin}:/usr/bin:/bin",
            ADE_CHILD_LOG=str(self.log), PYTHONDONTWRITEBYTECODE="1", GIT_CONFIG_NOSYSTEM="1",
            GIT_CONFIG_GLOBAL="/dev/null")

    def child(self, program, payload):
        self.log.unlink(missing_ok=True)
        return subprocess.run([sys.executable, "-c", program], input=json.dumps(payload),
            env=self.env, cwd=self.root, text=True, capture_output=True, timeout=15)

    def test_remote_program_probe_allowed_git_and_rejected_mutations(self):
        repo = self.root / "repo with spaces"
        (repo / ".git").mkdir(parents=True)
        base = {"root": str(self.root), "repository": str(repo)}
        probe = self.child(context.REMOTE_PROGRAM, {**base, "action": "probe"})
        self.assertEqual(probe.returncode, 0, probe.stderr)
        self.assertEqual(json.loads(probe.stdout), {"exists": True, "directory": True, "git": True})
        self.assertFalse(self.log.exists())
        for args in (["status", "--", "space arg"], ["-c", "core.quotePath=false", "diff"],
                ["remote", "get-url", "origin"], ["symbolic-ref", "--quiet", "--short", "HEAD"],
                ["merge", "--ff-only", "a" * 40]):
            result = self.child(context.REMOTE_PROGRAM, {**base, "action": "git", "arguments": args})
            self.assertEqual(result.returncode, 0, result.stderr)
            argv = json.loads(self.log.read_text())
            self.assertEqual(argv[-len(args):], args)
            self.assertIn("safe.directory=" + str(repo), argv)
        for args in ([], ["push"], ["remote", "set-url", "origin", "other"],
                ["symbolic-ref", "HEAD", "refs/heads/main"], ["merge", "--ff-only", "main"]):
            result = self.child(context.REMOTE_PROGRAM, {**base, "action": "git", "arguments": args})
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(self.log.exists())
        self.assertNotEqual(self.child(context.REMOTE_PROGRAM, {**base, "action": "unknown"}).returncode, 0)

    def test_source_program_checks_real_temporary_readonly_and_hash_boundaries(self):
        source = self.root / "source"
        source.mkdir()
        member = source / "member.txt"
        member.write_bytes(b"synthetic\r\n")
        payload = {"source": str(source), "bindings": {
            "member.txt": hashlib.sha256(b"synthetic\n").hexdigest()}}
        self.assertNotEqual(self.child(context.SOURCE_PROGRAM, payload).returncode, 0)
        member.chmod(0o444)
        source.chmod(0o555)
        try:
            result = self.child(context.SOURCE_PROGRAM, payload)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), "ready")
            wrong = {**payload, "bindings": {"member.txt": "0" * 64}}
            self.assertNotEqual(self.child(context.SOURCE_PROGRAM, wrong).returncode, 0)
            missing = {**payload, "bindings": {"missing.txt": "0" * 64}}
            self.assertNotEqual(self.child(context.SOURCE_PROGRAM, missing).returncode, 0)
        finally:
            source.chmod(0o755)
            member.chmod(0o644)
        self.assertFalse(self.log.exists())

    def test_phase_program_rejects_real_source_drift_before_worker_import(self):
        source = self.root / "phase-source"
        (source / "scripts/lib").mkdir(parents=True)
        worker = source / "scripts/lib/maintenance_container_worker.py"
        worker.write_text("def execute(payload):\n    return {'status':'SyntheticOnly','records':[]}\n")
        bindings = {"scripts/lib/maintenance_container_worker.py": hashlib.sha256(worker.read_bytes()).hexdigest()}
        payload = {"source": str(source), "bindings": bindings}
        result = self.child(context.PHASE_PROGRAM, payload)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "SyntheticOnly")
        worker.write_text("raise RuntimeError('must not be imported after drift')\n")
        result = self.child(context.PHASE_PROGRAM, payload)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("binding mismatch", result.stderr)
        self.assertNotIn("RuntimeError", result.stderr)
        self.assertFalse(self.log.exists())

    def test_native_bash_and_powershell_preview_use_real_core_without_execution(self):
        scripts = self.root / "sandbox/scripts"
        (scripts / "lib").mkdir(parents=True)
        (scripts / "lib/secure_development_hardening.py").symlink_to(
            ROOT / "scripts/lib/secure_development_hardening.py")
        for suffix in ("sh", "ps1"):
            shutil.copyfile(ROOT / f"scripts/test-ade-sandbox-hardening.{suffix}",
                            scripts / f"test-ade-sandbox-hardening.{suffix}")
        repo = scripts.parent
        feature = "specs/004-container-hardening-followup"
        directory = repo / feature
        directory.mkdir(parents=True)
        (directory / "gate-requirements.json").write_text('{"synthetic":"preview only"}')
        before = sorted(str(p.relative_to(repo)) for p in repo.rglob("*"))
        pwsh = shutil.which("pwsh")
        self.assertIsNotNone(pwsh, "Mac-A PowerShell prerequisite, not Windows proof")
        for shell in ("bash", "pwsh"):
            for selected, expected in ((feature, 0), (".", 2)):
                argv = (["/bin/bash", str(scripts / "test-ade-sandbox-hardening.sh"), "--mode", "All",
                    "--feature-directory", selected, "--dry-run"] if shell == "bash" else
                    [pwsh, "-NoLogo", "-NoProfile", "-NonInteractive", "-File",
                    str(scripts / "test-ade-sandbox-hardening.ps1"), "-Mode", "All",
                    "-FeatureDirectory", selected, "-WhatIf"])
                result = subprocess.run(argv, env=self.env, cwd=repo, capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, expected, result.stderr)
                if expected == 0:
                    self.assertIn("no checks executed", result.stdout)
                self.assertEqual(before, sorted(str(p.relative_to(repo)) for p in repo.rglob("*")))
                self.assertFalse(self.log.exists())


if __name__ == "__main__":
    unittest.main()
