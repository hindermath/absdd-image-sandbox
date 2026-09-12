#!/usr/bin/env python3
"""Ensure canonical sandbox workflows do not duplicate feature-branch CI."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]


class WorkflowConcurrencyTests(unittest.TestCase):
    def test_feature_branches_run_only_through_pull_request_trigger(self) -> None:
        workflows = (
            "documentation-and-sandbox.yml",
            "homogeneity-check.yml",
            "maintenance-tui.yml",
            "powershell-analysis.yml",
        )
        for name in workflows:
            with self.subTest(workflow=name):
                text = (ROOT / ".github/workflows" / name).read_text(encoding="utf-8")
                self.assertIn("  push:\n    branches:\n      - main\n", text)
                self.assertIn("  pull_request:\n", text)
                self.assertIn(
                    "group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}",
                    text,
                )
                self.assertIn("cancel-in-progress: true", text)


if __name__ == "__main__":
    unittest.main()
