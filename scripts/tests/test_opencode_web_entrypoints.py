#!/usr/bin/env python3
"""Check local web and TUI wrappers without provider access."""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import importlib.util
import io
import urllib.error
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"


class OpenCodeEntrypoints(unittest.TestCase):
    def run_wrapper(self, name: str, password: str | None, *args: str):
        with tempfile.TemporaryDirectory(prefix="ade-opencode-wrapper-") as directory:
            fake = Path(directory) / "opencode"
            fake.write_text("#!/bin/sh\nprintf '%s\\n' \"$@\"\n")
            fake.chmod(0o755)
            environment = dict(os.environ, PATH=f"{directory}:{os.environ['PATH']}")
            if password is None:
                environment.pop("OPENCODE_PASSWORD", None)
            else:
                environment["OPENCODE_PASSWORD"] = password
            return subprocess.run(
                ["bash", str(SCRIPTS / name), *args],
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )

    def test_password_gate(self):
        for password in (None, "", "short", " " * 20,
                         "changeme-this-is-long", "password-this-is-long",
                         "example-this-is-long", "<set-a-private-local-value>"):
            with self.subTest(password=password):
                result = self.run_wrapper("opencode-web.sh", password)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                if password:
                    self.assertNotIn(password, result.stderr)

    def test_server_arguments(self):
        result = self.run_wrapper("opencode-web.sh", "Synthetic-Only-9f4c2a")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(),
                         ["serve", "--hostname", "0.0.0.0", "--port", "5199"])

    def test_fullscreen_and_mini_clients(self):
        for name, expected in (
            ("opencode-tui.sh", ["--server", "http://127.0.0.1:5199"]),
            ("opencode-tui-mini.sh", ["mini", "--server", "http://127.0.0.1:5199"]),
        ):
            with self.subTest(name=name):
                result = self.run_wrapper(name, None, "--help")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.splitlines(), expected + ["--help"])

    def test_healthcheck_retries_only_temporary_503_and_stays_silent(self):
        path = SCRIPTS / "healthcheck-opencode-web.py"
        spec = importlib.util.spec_from_file_location("ade_healthcheck", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        class Response:
            status = 200

            def __enter__(self):
                return self

            def __exit__(self, *_):
                return False

        def failure(code):
            return urllib.error.HTTPError("http://127.0.0.1:5199/api/info",
                                          code, "synthetic", {}, None)

        cases = (
            ([failure(503), Response()], 0, True),
            ([failure(503)], 1, False),
            ([failure(401)], 1, False),
        )
        for responses, expected, retry in cases:
            with self.subTest(expected=expected, retry=retry):
                output, errors = io.StringIO(), io.StringIO()
                with patch.dict(os.environ, {"OPENCODE_PASSWORD": "Synthetic-Only-9f4c2a"}), \
                     patch.object(module.urllib.request, "urlopen",
                                  side_effect=responses), \
                     patch.object(module.time, "sleep") as sleep, \
                     patch.object(module.time, "monotonic",
                                  side_effect=[0, 1, 2, 3] if retry else [0, 1, 46]), \
                     redirect_stdout(output), redirect_stderr(errors):
                    self.assertEqual(module.main(), expected)
                self.assertEqual(output.getvalue() + errors.getvalue(), "")
                self.assertEqual(sleep.called, retry)


if __name__ == "__main__":
    unittest.main()
