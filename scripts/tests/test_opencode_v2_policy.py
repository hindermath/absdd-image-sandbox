#!/usr/bin/env python3
"""DE: OpenCode-2-Schutzregeln. EN: OpenCode 2 policy regression checks."""

import fnmatch
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]


def load_config():
    # This file deliberately uses only whole-line JSONC comments.
    text = "\n".join(
        line for line in (ROOT / "opencode.jsonc").read_text().splitlines()
        if not line.lstrip().startswith("//")
    )
    return json.loads(text)


class OpenCodePolicyTests(unittest.TestCase):
    def setUp(self):
        self.config = load_config()

    def test_every_previous_rule_is_preserved_in_order(self):
        previous = json.loads(
            (ROOT / "scripts/tests/fixtures/opencode-v1-policy.json").read_text()
        )
        expected = []
        for action, values in previous["permission"].items():
            if isinstance(values, str):
                values = {"*": values}
            for resource, effect in values.items():
                expected.append({
                    "action": {"bash": "shell", "task": "subagent"}.get(action, action),
                    "resource": resource,
                    "effect": effect,
                })
        self.assertEqual(self.config["permissions"], expected)

    def test_no_provider_or_automatic_update(self):
        self.assertEqual(self.config["share"], "disabled")
        self.assertEqual(self.config["update"], "disable")
        for field in ("permission", "autoupdate", "model", "provider", "providers"):
            self.assertNotIn(field, self.config)

    def test_effective_security_examples(self):
        cases = [
            ("shell", "git status --short", "allow"),
            ("shell", "git push origin main", "ask"),
            ("shell", "rm -rf /workspace", "deny"),
            ("shell", "curl https://example.org", "ask"),
            ("read", "nested/.env", "deny"),
            ("read", "nested/.env.example", "allow"),
            ("edit", "nested/.env.example", "deny"),
            ("edit", "src/main.cs", "ask"),
            ("external_directory", "/other/private/*", "ask"),
            ("subagent", "general", "ask"),
            ("new_tool", "unknown", "ask"),
        ]
        for action, resource, expected in cases:
            with self.subTest(action=action, resource=resource):
                result = "ask"
                for rule in self.config["permissions"]:
                    if (fnmatch.fnmatchcase(action, rule["action"])
                            and fnmatch.fnmatchcase(resource, rule["resource"])):
                        result = rule["effect"]
                self.assertEqual(result, expected)

    def test_package_and_renovate_follow_v2(self):
        dockerfile = (ROOT / "Dockerfile").read_text()
        self.assertIn('"@opencode/cli@${OPENCODE_VERSION}"', dockerfile)
        self.assertNotIn('"opencode-ai@${OPENCODE_VERSION}"', dockerfile)
        self.assertIn('"@opencode/cli"', (ROOT / "renovate.json").read_text())

    def test_sbom_fallback_matches_image_syft(self):
        dockerfile = (ROOT / "Dockerfile").read_text()
        version = next(
            line.split("=", 1)[1] for line in dockerfile.splitlines()
            if line.startswith("ARG SYFT_VERSION=")
        )
        self.assertIn(
            "${SYFT_VERSION:-" + version + "}",
            (ROOT / "scripts/build-and-sbom.sh").read_text(),
        )
        self.assertIn(
            "$SyftVersion = '" + version + "'",
            (ROOT / "scripts/build-and-sbom.ps1").read_text(),
        )

    def test_synthetic_global_agent_project_and_subagent_overrides(self):
        fixture = json.loads((ROOT / "scripts/tests/fixtures/hardening-followup/"
                              "opencode-v2-layer-cases.json").read_text())
        self.assertIn("synthetic", fixture["model"])
        kinds = set()
        for case in fixture["cases"]:
            rules = list(self.config["permissions"])
            for layer in case["layers"]:
                kinds.add(layer["kind"])
                rules.extend(layer["rules"])
            result = "ask"
            for rule in rules:
                if (fnmatch.fnmatchcase(case["action"], rule["action"])
                        and fnmatch.fnmatchcase(case["resource"], rule["resource"])):
                    result = rule["effect"]
            with self.subTest(case=case["id"]):
                self.assertEqual(result, case["expected"])
        self.assertEqual(kinds, {"agent", "project", "subagent"})

    def test_fake_updater_stays_idle_with_committed_controls(self):
        dockerfile = (ROOT / "Dockerfile").read_text()
        gemini = json.loads((ROOT / "gemini/system-settings.json").read_text())
        self.assertEqual(gemini["general"]["enableAutoUpdate"], False)
        self.assertIn('COPILOT_AUTO_UPDATE="false"', dockerfile)
        self.assertIn('AGY_CLI_DISABLE_AUTO_UPDATE="true"', dockerfile)
        self.assertIn('DISABLE_AUTOUPDATER="1"', dockerfile)
        self.assertIn('COPY ./gemini/system-settings.json /etc/gemini-cli/settings.json', dockerfile)
        with tempfile.TemporaryDirectory(prefix="ade-fake-updater-") as directory:
            marker = Path(directory) / "unexpected-update"
            # A disposable updater model tests control values, not agent runtime internals.
            probe = """import json, os, pathlib
root = pathlib.Path(os.environ['ADE_TEST_ROOT'])
config = json.loads((root / 'opencode.jsonc').read_text())
gemini = json.loads((root / 'gemini/system-settings.json').read_text())
enabled = (config['update'] != 'disable' or
           gemini['general']['enableAutoUpdate'] is not False or
           os.environ['DISABLE_AUTOUPDATER'] != '1' or
           os.environ['COPILOT_AUTO_UPDATE'] != 'false' or
           os.environ['AGY_CLI_DISABLE_AUTO_UPDATE'] != 'true')
if enabled:
    pathlib.Path(os.environ['ADE_TEST_MARKER']).write_text('update')
"""
            # The parsed source config is written as JSON for the isolated model.
            (Path(directory) / "opencode.jsonc").write_text(json.dumps(self.config))
            (Path(directory) / "gemini").mkdir()
            (Path(directory) / "gemini/system-settings.json").write_text(json.dumps(gemini))
            env = dict(os.environ, ADE_TEST_ROOT=directory, ADE_TEST_MARKER=str(marker),
                       DISABLE_AUTOUPDATER="1", COPILOT_AUTO_UPDATE="false",
                       AGY_CLI_DISABLE_AUTO_UPDATE="true")
            result = subprocess.run([sys.executable, "-c", probe], env=env,
                                    capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(marker.exists())
            (Path(directory) / "gemini/system-settings.json").write_text(
                json.dumps({"general": {"enableAutoUpdate": True}}))
            negative = subprocess.run([sys.executable, "-c", probe], env=env,
                                      capture_output=True, text=True, timeout=5)
            self.assertEqual(negative.returncode, 0, negative.stderr)
            self.assertTrue(marker.exists())


if __name__ == "__main__":
    unittest.main()
