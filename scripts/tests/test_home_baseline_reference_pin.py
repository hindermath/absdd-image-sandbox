"""Offline contract tests: never contact a provider or change system Git config."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "install-home-baseline-reference.sh"
COMMIT = "a" * 40


class ReferencePinTests(unittest.TestCase):
    def test_repository_validator_contracts(self):
        release = self.lock(schemaVersion=1, tag="v0.18.0")
        del release["refType"]
        cases = [(self.lock(), 0), (release, 0), ([], 1),
                 (self.lock(schemaVersion=True), 1),
                 (self.lock(schemaVersion=3), 1),
                 (self.lock(refType="branch"), 1),
                 (self.lock(commit="main"), 1),
                 (self.lock(tag="v0.18.0"), 1)]
        for lock, code in cases:
            with self.subTest(lock=lock), tempfile.TemporaryDirectory() as directory:
                (Path(directory) / "home-baseline.lock.json").write_text(json.dumps(lock))
                result = subprocess.run(
                    [sys.executable, str(SCRIPT.with_name("check-home-baseline-lock.py"))],
                    cwd=directory, capture_output=True, text=True)
                self.assertEqual(result.returncode, code, result.stderr)

    def run_install(self, lock, resolved=COMMIT):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binaries = root / "bin"
            binaries.mkdir()
            log = root / "git.log"
            fake_git = binaries / "git"
            fake_git.write_text(
                '#!/bin/sh\nprintf "%s\\n" "$*" >> "$PIN_TEST_LOG"\n'
                'case "$*" in\n'
                '  "init --quiet "*) mkdir -p "$3/docs/learning-units"; '
                'touch "$3/LICENSE" "$3/docs/learning-units/START-HERE-FUER-LERNENDE.md";;\n'
                '  *"rev-parse "*) printf "%s\\n" "$PIN_TEST_RESOLVED";;\n'
                'esac\n', encoding="utf-8")
            fake_git.chmod(0o755)
            for command in ("chown", "chmod"):
                stub = binaries / command
                stub.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
                stub.chmod(0o755)
            lockfile = root / "lock.json"
            lockfile.write_text(json.dumps(lock), encoding="utf-8")
            result = subprocess.run(
                ["bash", str(SCRIPT), str(lockfile), str(root / "reference")],
                env={**os.environ, "PATH": f"{binaries}{os.pathsep}{os.environ['PATH']}",
                     "PIN_TEST_LOG": str(log), "PIN_TEST_RESOLVED": resolved},
                text=True, capture_output=True)
            return result, log.read_text() if log.exists() else ""

    def lock(self, **overrides):
        return {"schemaVersion": 2, "refType": "commit",
                "source": "https://github.com/hindermath/home-baseline.git",
                "commit": COMMIT, "license": "MIT", **overrides}

    def test_commit_pin_fetches_exact_hash(self):
        result, log = self.run_install(self.lock())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"fetch --quiet --depth=1 --no-tags upstream {COMMIT}", log)

    def test_release_mode_remains_supported(self):
        lock = self.lock(schemaVersion=1, tag="v0.18.0")
        del lock["refType"]
        result, log = self.run_install(lock)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("upstream refs/tags/v0.18.0", log)

    def test_mismatch_does_not_install(self):
        result, log = self.run_install(self.lock(), resolved="b" * 40)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("config --system", log)

    def test_invalid_contracts_fail_before_git(self):
        for lock in (self.lock(schemaVersion=3), self.lock(tag="v0.18.0"),
                     self.lock(commit="main"), self.lock(refType="branch"),
                     self.lock(source="https://example.invalid/repo.git")):
            with self.subTest(lock=lock):
                result, log = self.run_install(lock)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(log, "")


if __name__ == "__main__":
    unittest.main()
