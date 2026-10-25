#!/usr/bin/env python3
"""Focused CI wiring and fail-closed installed-payload regressions."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.tests.test_spec_kit_agent_surface_parity import (  # noqa: E402
    normalized_hash, payload_binding, validate_installed_lock,
)


class CloseoutCiContractTests(unittest.TestCase):
    def test_statistics_workflow_uses_current_integrity_gate_in_both_worktrees(self):
        text = (ROOT / ".github/workflows/project-statistics-pilot-native-proof.yml").read_text(encoding="utf-8")
        self.assertNotIn("project-statistics-installation-v010.json", text)
        self.assertIn("foreach ($root in @($source,$pilot))", text)
        self.assertIn("test_gsdb_rollout_installed_payload_and_release_bindings", text)
        self.assertIn("if ($LASTEXITCODE -ne 0)", text)
        historical = json.loads((ROOT / "docs/maintenance/project-statistics-installation-v010.json").read_text())
        self.assertEqual(historical["preset"]["version"], "0.1.0")

    def test_maintenance_sdk_uses_verified_ga_not_floating_endpoint(self):
        text = (ROOT / ".github/workflows/maintenance-tui.yml").read_text(encoding="utf-8")
        self.assertIn("dotnet-version: 10.0.402", text)
        self.assertNotIn("dotnet-version: 10.0.x", text)
        self.assertIn("--locked-mode", text)
        self.assertIn("unittest discover", text)

    def test_current_lock_gate_rejects_payload_and_manifest_tampering(self):
        with tempfile.TemporaryDirectory(prefix="ade-ci-lock-") as directory:
            root = Path(directory)
            preset = root / "project-statistics-governance"
            preset.mkdir()
            manifest = preset / "preset.yml"
            manifest.write_text('metadata:\n  version: "0.1.3"\n', encoding="utf-8")
            payload = preset / "command.md"
            payload.write_text("Approved payload\n", encoding="utf-8")
            entry = {"version": "0.1.3", "priority": 90, "enabled": True,
                     "manifest_hash": "sha256:" + normalized_hash(manifest)}
            (root / ".registry").write_text(json.dumps({"presets": {preset.name: entry}}), encoding="utf-8")
            lock = {"schemaVersion": 1, "hashContract": "sha256-utf8-lf-bom-or-raw-v1",
                    "baselineCommit": "a" * 40, "registrySha256": normalized_hash(root / ".registry"),
                    "presets": [{"id": preset.name, **entry, **payload_binding(preset)}]}
            validate_installed_lock(root, lock)
            payload.write_text("Changed payload\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "installed payload drift"):
                validate_installed_lock(root, lock)
            payload.write_text("Approved payload\n", encoding="utf-8")
            manifest.write_text('metadata:\n  version: "0.1.4"\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "installed manifest hash drift"):
                validate_installed_lock(root, lock)


if __name__ == "__main__":
    unittest.main()
