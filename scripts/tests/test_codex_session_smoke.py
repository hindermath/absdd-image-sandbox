"""Exercise session startup success, server errors and bounded timeout offline."""
import importlib.util
import io
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "session_smoke", ROOT / "scripts/lib/codex_session_smoke.py")
smoke = importlib.util.module_from_spec(spec)
spec.loader.exec_module(smoke)


@unittest.skipUnless(os.name == "posix", "Image session cleanup uses POSIX process groups")
class SessionSmokeTests(unittest.TestCase):
    def run_probe(self, second, timeout=2):
        class FakeProcess:
            pid = 424242
            stdin = io.StringIO()
            stdout = io.StringIO(json.dumps({"id": 1, "result": {}}) + "\n" +
                                 json.dumps(second) + "\n")
            def wait(self, timeout):
                return 0
        process = FakeProcess()
        with patch.object(smoke.subprocess, "Popen", return_value=process) as launch, \
                patch.object(os, "killpg", create=True) as kill:
            try:
                smoke.start_session(Path("/fixture"), timeout=timeout)
            finally:
                self.assertIn("--strict-config", launch.call_args.args[0])
                self.assertGreaterEqual(kill.call_count, 2)
                self.assertTrue(process.stdout.closed)
                self.assertTrue(process.stdin.closed)

    def test_successful_thread(self):
        self.run_probe({"id": 2, "result": {"thread": {"id": "fixture"},
            "approvalPolicy": "on-request", "sandbox": {"type": "workspaceWrite",
            "networkAccess": False, "excludeSlashTmp": True}}})

    def test_weakened_sandbox_fails(self):
        with self.assertRaisesRegex(RuntimeError, "sandbox defaults"):
            self.run_probe({"id": 2, "result": {"thread": {"id": "fixture"},
                "approvalPolicy": "never", "sandbox": {"type": "dangerFullAccess"}}})

    def test_thread_error_fails_without_dumping_server_content(self):
        with self.assertRaisesRegex(RuntimeError, "thread/start failed"):
            self.run_probe({"id": 2, "error": {"message": "private fixture"}})

    def test_malformed_result_fails(self):
        with self.assertRaisesRegex(RuntimeError, "no result object"):
            self.run_probe({"id": 2, "result": None})

    def test_no_thread_fails(self):
        with self.assertRaisesRegex(RuntimeError, "no thread"):
            self.run_probe({"id": 2, "result": {}})

    def test_deadline_is_bounded(self):
        with self.assertRaisesRegex(RuntimeError, "timed out"):
            self.run_probe({"id": 99, "result": {}}, timeout=0)
