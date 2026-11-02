"""Native shell adapter outcomes against a recording, non-executing core.

DE: Keine Kern-/Plattformabnahme. EN: Adapter tests, not core/platform acceptance.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[2]
MODES = ("Input", "Static", "Runtime", "SupplyChain", "Documentation", "Accessibility", "All")


class WrapperOutcomeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="ade004-wrapper-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        (self.root / "scripts").mkdir()
        for suffix in ("sh", "ps1"):
            shutil.copyfile(REPO / f"scripts/test-ade-sandbox-hardening.{suffix}",
                            self.root / f"scripts/test-ade-sandbox-hardening.{suffix}")
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self.log = self.root / "argv.json"
        fake = self.bin / "python3"
        fake.write_text(f"#!{sys.executable}\n" +
            "import json, os, pathlib, sys\n"
            "pathlib.Path(os.environ['ADE_WRAPPER_ARGV']).write_text(json.dumps(sys.argv[1:]))\n"
            "print('synthetic core: no checks executed')\n"
            "raise SystemExit(int(os.environ.get('ADE_WRAPPER_EXIT', '0')))\n")
        fake.chmod(0o755)
        self.env = {key: value for key, value in os.environ.items() if key in (
            "TMPDIR", "TMP", "TEMP", "LANG", "LC_ALL", "SYSTEMROOT", "SystemRoot")}
        self.env.update(HOME=str(self.root), USERPROFILE=str(self.root),
            PATH=f"{self.bin}:/usr/bin:/bin", ADE_WRAPPER_ARGV=str(self.log),
            PYTHONDONTWRITEBYTECODE="1", GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_NOSYSTEM="1")
        self.pwsh = shutil.which("pwsh")

    def run_wrapper(self, shell, arguments, code=0):
        self.log.unlink(missing_ok=True)
        if shell == "pwsh":
            if not self.pwsh:
                self.skipTest("Native PowerShell unavailable; no substitute acceptance")
            argv = [self.pwsh, "-NoLogo", "-NoProfile", "-NonInteractive", "-File",
                    str(self.root / "scripts/test-ade-sandbox-hardening.ps1")]
        else:
            argv = ["/bin/bash", str(self.root / "scripts/test-ade-sandbox-hardening.sh")]
        return subprocess.run([*argv, *arguments], env={**self.env, "ADE_WRAPPER_EXIT": str(code)},
            cwd=self.root, text=True, capture_output=True, timeout=15)

    def assert_routing(self, shell):
        # Option-shaped/spaced/metacharacter values must remain inert argv data.
        feature = "specs/feature with spaces;$(touch forbidden)"
        evidence = "-evidence with spaces.json"
        for mode in MODES:
            for code in (0, 2, 3):
                arguments = (["--mode", mode.lower(), "--evidence", evidence,
                    "--feature-directory", feature, "--dry-run"] if shell == "bash" else
                    ["-Mode", mode, "-EvidencePath", evidence, "-FeatureDirectory", feature, "-WhatIf"])
                with self.subTest(shell=shell, mode=mode, core_exit=code):
                    result = self.run_wrapper(shell, arguments, code)
                    self.assertEqual(result.returncode, code, result.stderr)
                    self.assertEqual(json.loads(self.log.read_text()), [
                        str(self.root / "scripts/lib/secure_development_hardening.py"),
                        "run-mode", "--repo", str(self.root), "--mode", mode,
                        "--evidence", evidence, "--feature-directory", feature, "--dry-run"])
                    self.assertFalse((self.root / "forbidden").exists())

    def test_bash_preview_argument_identity_and_core_exit_propagation(self):
        self.assert_routing("bash")

    def test_powershell_preview_argument_identity_and_core_exit_propagation(self):
        self.assert_routing("pwsh")

    def test_bash_parser_rejects_before_core_and_help_is_readonly(self):
        for arguments in ([], ["--mode"], ["--evidence"], ["--feature-directory"],
                ["--feature-directory", ""], ["--unknown"], ["--mode", "unsupported"]):
            with self.subTest(arguments=arguments):
                self.assertEqual(self.run_wrapper("bash", arguments).returncode, 2)
                self.assertFalse(self.log.exists())
        result = self.run_wrapper("bash", ["--help"])
        self.assertEqual(result.returncode, 0)
        self.assertIn("exit 0 is not a pass", result.stdout)
        self.assertFalse(self.log.exists())

    def test_powershell_parser_rejects_before_core(self):
        for arguments in (["-Mode", "unsupported"], ["-Mode", "Input", "-FeatureDirectory", ""]):
            with self.subTest(arguments=arguments):
                self.assertNotEqual(self.run_wrapper("pwsh", arguments).returncode, 0)
                self.assertFalse(self.log.exists())


if __name__ == "__main__":
    unittest.main()
