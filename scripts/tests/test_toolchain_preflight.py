#!/usr/bin/env python3
"""Regression tests for the machine-readable sandbox toolchain preflight."""

import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "smoke-test-toolchains.sh"
TOOLS = ("actionlint", "codex", "dotnet", "git", "jq", "pwsh", "yq")


class ToolchainPreflightTests(unittest.TestCase):
    def make_path(self, root: Path, *, omit: str | None = None) -> Path:
        bin_dir = root / "bin"
        bin_dir.mkdir()
        for tool in TOOLS:
            if tool == omit:
                continue
            body = "#!/bin/sh\n"
            if tool == "dotnet":
                body += "printf '%s\\n' '10.0.301'\n"
            else:
                body += f"printf '%s\\n' '{tool} test-version'\n"
            path = bin_dir / tool
            path.write_text(body, encoding="utf-8")
            path.chmod(0o755)
        return bin_dir

    def run_preflight(self, fake_path: Path, repository: Path | None = None) -> subprocess.CompletedProcess[str]:
        command = ["/bin/bash", str(SCRIPT), "--json"]
        if repository:
            command.extend(["--repo", str(repository)])
        environment = os.environ.copy()
        environment["PATH"] = f"{fake_path}:/usr/bin:/bin"
        return subprocess.run(command, cwd=ROOT, env=environment, text=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)

    def test_reports_control_plane_and_matching_sdk(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fake_path = self.make_path(root)
            repository = root / "repo"
            repository.mkdir()
            (repository / "global.json").write_text(
                '{"sdk":{"version":"10.0.301","rollForward":"latestPatch"}}\n', encoding="utf-8"
            )
            result = self.run_preflight(fake_path, repository)
            self.assertEqual(result.returncode, 0, result.stderr)
            document = json.loads(result.stdout)
            self.assertEqual(document["schemaVersion"], "1.0")
            self.assertEqual(document["dotnetSdk"]["selected"], "10.0.301")
            self.assertEqual(document["dotnetSdk"]["status"], "Pass")
            gh = next(item for item in document["tools"] if item["tool"] == "gh")
            self.assertEqual(gh["status"], "ControlPlane")

    def test_missing_required_tool_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fake_path = self.make_path(Path(directory), omit="actionlint")
            result = self.run_preflight(fake_path)
            self.assertEqual(result.returncode, 1)
            document = json.loads(result.stdout)
            actionlint = next(item for item in document["tools"] if item["tool"] == "actionlint")
            self.assertEqual(actionlint["status"], "Missing")

    def test_different_selected_sdk_fails_exact_repository_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fake_path = self.make_path(root)
            repository = root / "repo"
            repository.mkdir()
            (repository / "global.json").write_text(
                '{"sdk":{"version":"10.0.302"}}\n', encoding="utf-8"
            )
            result = self.run_preflight(fake_path, repository)
            self.assertEqual(result.returncode, 1)
            document = json.loads(result.stdout)
            self.assertEqual(document["dotnetSdk"]["requested"], "10.0.302")
            self.assertEqual(document["dotnetSdk"]["selected"], "10.0.301")
            self.assertEqual(document["dotnetSdk"]["status"], "Fail")


if __name__ == "__main__":
    unittest.main()
