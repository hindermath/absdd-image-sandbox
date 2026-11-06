"""Configuration loading must fail smoke even when version reporting works."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


class CodexConfigurationSmokeTests(unittest.TestCase):
    @unittest.skipUnless(os.name == "posix", "Native shell fixture targets the Linux image")
    def test_configuration_failure_is_not_hidden_by_version_success(self):
        source = (ROOT / "scripts/smoke-test-toolchains.sh").read_text()
        stage = source.split('section "Codex configuration"', 1)[1].split(
            'section "Codex session startup"', 1)[0]
        with tempfile.TemporaryDirectory() as directory:
            cli = Path(directory) / "codex"
            cli.write_text('#!/bin/sh\nif [ "$1" = "--version" ]; then echo codex-test; exit 0; fi\n'
                           '[ "$1 $2" = "features list" ] || exit 99\n'
                           'exit "$CONFIG_TEST_EXIT"\n')
            cli.chmod(0o755)
            for status in (0, 42):
                env = {**os.environ, "PATH": directory + os.pathsep + os.environ["PATH"],
                       "CONFIG_TEST_EXIT": str(status)}
                version = subprocess.run(["codex", "--version"], env=env, capture_output=True)
                self.assertEqual(version.returncode, 0)
                result = subprocess.run(["bash", "-c", "set -euo pipefail\n" + stage], env=env)
                self.assertEqual(result.returncode, status)

    def test_json_mode_loads_configuration_without_override(self):
        source = (ROOT / "scripts/smoke-test-toolchains.sh").read_text()
        self.assertIn('"codex-config": ["codex", "features", "list"]', source)
