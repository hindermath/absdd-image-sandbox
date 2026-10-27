#!/usr/bin/env python3
"""Real hook execution in isolated repos; Gitleaks behavior is tested separately."""

from pathlib import Path
import base64
import hashlib
import json
import os
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
HOOK = ROOT / "scripts/hooks/pre-push"
DECK = "docs/praesentationen/exports/workshop-spec-kit.de.key"


class PrePushSecretPolicyTests(unittest.TestCase):
    def run_hook(self, files, gitleaks_exit=0, after_commit=None, followup_commit=False,
                 existing_ref=False, intermediate_commit=None):
        with tempfile.TemporaryDirectory(prefix="ade-pre-push-") as directory:
            root = Path(directory)
            env = os.environ.copy()
            env.update(HOME=str(root), XDG_CONFIG_HOME=str(root / "config"),
                       GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
            for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
                env.pop(key, None)
            binaries = root / "tools"
            binaries.mkdir()
            stub = binaries / "gitleaks"
            stub.write_text(f"#!/bin/sh\nexit {gitleaks_exit}\n", encoding="utf-8")
            stub.chmod(0o755)
            env["PATH"] = str(binaries) + os.pathsep + env["PATH"]

            def git(*args):
                return subprocess.run(["git", *args], cwd=root, env=env, check=True,
                                      capture_output=True, text=True, timeout=15).stdout.strip()

            git("init", "-q")
            git("config", "user.name", "Fixture")
            git("config", "user.email", "fixture@example.invalid")
            for name, value in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(value if isinstance(value, bytes) else value.encode())
            git("add", "--", *files)
            git("commit", "-qm", "fixture")
            remote_sha = git("rev-parse", "HEAD") if existing_ref else "0" * 40
            for name, value in (intermediate_commit or {}).items():
                (root / name).write_bytes(value)
            if intermediate_commit:
                git("add", "--", *intermediate_commit)
                git("commit", "-qm", "intermediate")
            for name, value in (after_commit or {}).items():
                (root / name).write_bytes(value)
            if followup_commit:
                git("add", "--", *after_commit)
                git("commit", "-qm", "followup")
            sha = git("rev-parse", "HEAD")
            return subprocess.run(["bash", str(HOOK)], cwd=root, env=env,
                                  input=f"refs/heads/main {sha} refs/heads/main {remote_sha}\n",
                                  capture_output=True, text=True, timeout=20)

    def test_rule_names_and_unassigned_words_are_not_credentials(self):
        result = self.run_hook({"review.md": "generic-api-key\naccess_token\nclient_secret\npassword\n"})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_assigned_fields_remain_blocked_in_shell_and_json(self):
        for field in ("api_key", "access_token", "refresh_token", "id_token", "client_secret", "password",
                      "API_KEY", "apiKey", "PASSWORD"):
            for value in (f"{field}=fixture-value", f'"{field}": "fixture-value"'):
                with self.subTest(field=field, value=value):
                    result = self.run_hook({"settings.txt": value + "\n"})
                    self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_reviewed_decks_are_allowed_only_at_exact_paths(self):
        files = {f"docs/praesentationen/exports/workshop-spec-kit.{lang}.key":
                 (ROOT / f"docs/praesentationen/exports/workshop-spec-kit.{lang}.key").read_bytes()
                 for lang in ("de", "en")}
        result = self.run_hook(files)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = self.run_hook({"other.key": files[DECK]})
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_quoted_leading_whitespace_and_empty_assignments_fail_closed(self):
        for field in ("password", "api_key"):
            for suffix in ('=" fixture-value"', '": " fixture-value"', '=""'):
                with self.subTest(field=field, syntax=suffix):
                    result = self.run_hook({"settings.txt": field + suffix + "\n"})
                    self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_reviewed_deck_history_allows_only_language_specific_pins(self):
        fixture = json.loads((ROOT / "scripts/tests/fixtures/keynote-previous-blobs.json")
                             .read_text(encoding="utf-8"))
        old, current = {}, {}
        # Reverse byte patches keep reviewed history reproducible in shallow clones.
        for lang in ("de", "en"):
            path = f"docs/praesentationen/exports/workshop-spec-kit.{lang}.key"
            data = current[path] = (ROOT / path).read_bytes()
            entry = fixture[lang]
            self.assertEqual(hashlib.sha256(data).hexdigest(), entry["inputSha256"])
            limit = len(data)
            for start, end, encoded in reversed(entry["patches"]):
                self.assertTrue(0 <= start <= end <= limit)
                data = data[:start] + base64.b64decode(encoded, validate=True) + data[end:]
                limit = start
            blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
            self.assertEqual(blob, entry["previousBlob"])
            old[path] = data
        for existing_ref in (False, True):
            with self.subTest(existing_ref=existing_ref):
                result = self.run_hook(old, after_commit=current, followup_commit=True,
                                       existing_ref=existing_ref)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for files in (old, current):
            paths = list(files)
            with self.subTest(swapped_version="old" if files is old else "current"):
                result = self.run_hook({paths[0]: files[paths[1]], paths[1]: files[paths[0]]})
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_modified_deck_and_real_key_at_allowed_path_remain_blocked(self):
        original = (ROOT / DECK).read_bytes()
        for payload in (original + b"changed", b"-----BEGIN " + b"PRIVATE KEY-----\nfixture\n"):
            with self.subTest(size=len(payload)):
                result = self.run_hook({DECK: payload})
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_private_keys_and_recognizable_tokens_remain_blocked(self):
        values = ("-----BEGIN " + "RSA PRIVATE KEY-----\nfixture\n",
                  "ghp_" + "A" * 30, "sk-" + "B" * 30)
        for value in values:
            with self.subTest(prefix=value[:5]):
                result = self.run_hook({"notes.txt": value})
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        result = self.run_hook({"private.pem": "opaque private material"})
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_gitleaks_failure_is_never_bypassed(self):
        result = self.run_hook({"clean.md": "Clean documentation\n"}, gitleaks_exit=2)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_worktree_or_later_commit_cannot_hide_unapproved_key_blob(self):
        approved = (ROOT / DECK).read_bytes()
        for committed in (False, True):
            with self.subTest(followup_commit=committed):
                result = self.run_hook({DECK: b"unapproved opaque key material"},
                                       after_commit={DECK: approved}, followup_commit=committed)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_existing_ref_checks_intermediate_key_even_when_tip_is_restored(self):
        approved = (ROOT / DECK).read_bytes()
        result = self.run_hook({DECK: approved}, existing_ref=True,
                               intermediate_commit={DECK: b"unapproved opaque material"},
                               after_commit={DECK: approved}, followup_commit=True)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
