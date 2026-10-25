#!/usr/bin/env python3
"""Bound the public-key exception using real, path-aware Gitleaks scans."""

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / ".gitleaks.toml"
FINGERPRINT = "52BB7E3DE28A71BE22EC05FFEF80A866B47A981F"
SNAPSHOT = ("specs/intake-authoring-operations/"
            "3caff22f-59d5-4142-b15b-955ee96a3037/source-snapshots/Dockerfile.txt")


def assignment(value):
    return '    swift_signing_key="' + value + '"; \\\n'


class SwiftFingerprintExceptionTests(unittest.TestCase):
    def scan(self, path, content, expected_exit):
        executable = shutil.which("gitleaks")
        if not executable:
            self.skipTest("real Gitleaks is required; no scanner success claimed")
        with tempfile.TemporaryDirectory(prefix="ade-gitleaks-scope-") as directory:
            root = Path(directory)
            payload = root / "payload"
            target = payload / path
            target.parent.mkdir(parents=True)
            target.write_text(content, encoding="utf-8")
            report = root / "redacted.json"
            result = subprocess.run(
                [executable, "dir", ".", "--config", str(CONFIG),
                 "--redact", "--no-banner", "--report-format", "json",
                 "--report-path", str(report)],
                cwd=payload, text=True, capture_output=True, timeout=15,
            )
            self.assertEqual(result.returncode, expected_exit, result.stderr)
            findings = json.loads(report.read_text()) if report.exists() else []
            if expected_exit:
                self.assertTrue(findings)
                self.assertIn("generic-api-key", {item["RuleID"] for item in findings})
            else:
                self.assertEqual(findings, [])

    def test_exception_requires_rule_path_and_complete_line(self):
        config = tomllib.loads(CONFIG.read_text())
        rule = next(item for item in config["allowlists"]
                    if item["description"].startswith("Public Swift release"))
        self.assertEqual(rule["targetRules"], ["generic-api-key"])
        self.assertEqual(rule["condition"], "AND")
        self.assertEqual(rule["regexTarget"], "line")
        self.assertEqual(len(rule["paths"]), 1)
        self.assertEqual(len(rule["regexes"]), 1)
        self.assertTrue(config["extend"]["useDefault"])

    def test_public_fingerprint_is_allowed_in_dockerfile(self):
        self.scan("Dockerfile", assignment(FINGERPRINT), 0)

    def test_public_fingerprint_is_allowed_in_exact_snapshot(self):
        self.scan(SNAPSHOT, assignment(FINGERPRINT), 0)

    def test_complete_multiline_sources_are_allowed(self):
        for path in ("Dockerfile", SNAPSHOT):
            with self.subTest(path=path):
                self.scan(path, (ROOT / path).read_text(), 0)

    def test_crlf_context_and_neighboring_secret_remain_bounded(self):
        synthetic = hashlib.sha256(b"ade-neighbor-noncredential-control").hexdigest()
        context = "RUN true; \\\n" + assignment(FINGERPRINT) + "    echo complete\n"
        self.scan("Dockerfile", context.replace("\n", "\r\n"), 0)
        self.scan("Dockerfile", context + 'service_token="' + synthetic + '"\n', 1)

    def test_other_value_is_detected_at_both_allowed_paths(self):
        synthetic = hashlib.sha1(b"ade-noncredential-negative-control").hexdigest().upper()
        for path in ("Dockerfile", SNAPSHOT):
            with self.subTest(path=path):
                self.scan(path, assignment(synthetic), 1)

    def test_public_fingerprint_is_detected_outside_allowed_paths(self):
        for path in ("unrelated.txt", "subdir/Dockerfile", SNAPSHOT.replace("3caff22f", "0caff22f")):
            with self.subTest(path=path):
                self.scan(path, assignment(FINGERPRINT), 1)

    def test_additional_assignment_on_same_line_is_not_allowed(self):
        synthetic = hashlib.sha256(b"ade-additional-noncredential-control").hexdigest()
        line = assignment(FINGERPRINT).rstrip("\\\n") + ' service_token="' + synthetic + '"\n'
        self.scan("Dockerfile", line, 1)

    def test_fingerprint_in_another_assignment_is_detected(self):
        self.scan("Dockerfile", assignment(FINGERPRINT).replace("swift_signing_key", "service_token"), 1)


if __name__ == "__main__":
    unittest.main()
