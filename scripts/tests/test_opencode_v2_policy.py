#!/usr/bin/env python3
"""DE: OpenCode-2-Schutzregeln. EN: OpenCode 2 policy regression checks."""

import fnmatch
import json
from pathlib import Path
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


if __name__ == "__main__":
    unittest.main()
