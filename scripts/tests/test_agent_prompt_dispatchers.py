#!/usr/bin/env python3
"""Contract tests for the Bash and PowerShell agent prompt dispatchers."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[2]
BASH_DISPATCHER = REPOSITORY / "scripts" / "agent-prompt.sh"
POWERSHELL_DISPATCHER = REPOSITORY / "scripts" / "agent-prompt.ps1"
SECRET_PROMPT = "prompt text that must stay redacted"


def clean_environment() -> dict[str, str]:
    environment = os.environ.copy()
    environment.pop("ADE_AGENT_PROMPT_TARGET", None)
    return environment


class AgentPromptDispatcherTests(unittest.TestCase):
    def run_bash(self, *arguments: str, stdin: str | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["bash", str(BASH_DISPATCHER), *arguments],
            input=stdin,
            text=True,
            capture_output=True,
            env=clean_environment(),
            check=False,
        )

    def run_powershell(
        self, *arguments: str, stdin: str | None = None
    ) -> subprocess.CompletedProcess[str]:
        if not shutil.which("pwsh"):
            self.skipTest("PowerShell 7 is unavailable")
        return subprocess.run(
            [
                "pwsh",
                "-NoLogo",
                "-NoProfile",
                "-File",
                str(POWERSHELL_DISPATCHER),
                *arguments,
            ],
            input=stdin,
            text=True,
            capture_output=True,
            env=clean_environment(),
            check=False,
        )

    def assert_redacted(self, result: subprocess.CompletedProcess[str]) -> None:
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("<prompt:redacted>", result.stdout)
        self.assertNotIn(SECRET_PROMPT, result.stdout)
        self.assertNotIn(SECRET_PROMPT, result.stderr)

    def test_agent_command_mappings_match(self) -> None:
        expected_commands = {
            "codex": "codex exec",
            "claude": "claude -p",
            "opencode": "opencode run",
            "copilot": "copilot -p",
            "gemini": "gemini -p",
            "agy": "agy -p",
        }
        for agent, expected in expected_commands.items():
            with self.subTest(agent=agent):
                bash_result = self.run_bash("--local", "--dry-run", agent, "--", SECRET_PROMPT)
                powershell_result = self.run_powershell(
                    "--local", "--dry-run", agent, "--", SECRET_PROMPT
                )
                self.assert_redacted(bash_result)
                self.assert_redacted(powershell_result)
                self.assertIn(f"Agent command: {expected}", bash_result.stdout)
                self.assertIn(f"Agent command: {expected}", powershell_result.stdout)

    def test_standard_input_and_prompt_file_are_supported(self) -> None:
        for runner in (self.run_bash, self.run_powershell):
            with self.subTest(runner=runner.__name__):
                stdin_result = runner("--local", "--dry-run", "codex", stdin=SECRET_PROMPT)
                self.assert_redacted(stdin_result)
                self.assertIn("Prompt source: stdin", stdin_result.stdout)

                with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8") as prompt_file:
                    prompt_file.write(SECRET_PROMPT)
                    prompt_file.flush()
                    file_result = runner(
                        "--local",
                        "--dry-run",
                        "codex",
                        "--prompt-file",
                        prompt_file.name,
                    )
                self.assert_redacted(file_result)
                self.assertIn("Prompt source: file", file_result.stdout)

    def test_repository_entrypoints_default_to_container_target(self) -> None:
        for runner in (self.run_bash, self.run_powershell):
            with self.subTest(runner=runner.__name__):
                result = runner("--dry-run", "codex", "--", SECRET_PROMPT)
                self.assert_redacted(result)
                self.assertIn("Target: container", result.stdout)

    def test_unknown_agent_is_rejected(self) -> None:
        for runner in (self.run_bash, self.run_powershell):
            with self.subTest(runner=runner.__name__):
                result = runner("--local", "--dry-run", "unknown", "--", SECRET_PROMPT)
                self.assertEqual(result.returncode, 2)
                self.assertIn("unsupported agent", result.stderr)


if __name__ == "__main__":
    unittest.main()
