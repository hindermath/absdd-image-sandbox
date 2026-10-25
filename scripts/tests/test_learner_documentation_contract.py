#!/usr/bin/env python3
"""Structural checks only, not human readability or WCAG acceptance."""

from pathlib import Path
import os
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
GUIDES = ("lernwege.md", "alltag.md", "faq.md", "entwickler-kurzpfad.md",
          "barrierefreiheit.md")
SURFACES = ("AGENTS.md", "CLAUDE.md", "GEMINI.md",
            ".github/copilot-instructions.md", ".github/agents/copilot-instructions.md")


class LearnerDocumentationContractTests(unittest.TestCase):
    def test_reader_entrypoints_exist_and_have_both_languages(self):
        entry = (ROOT / "docs/fuer-lernende/README.md").read_text()
        for guide in GUIDES:
            with self.subTest(guide=guide):
                text = (ROOT / "docs/fuer-lernende" / guide).read_text()
                self.assertEqual(len(re.findall(r"^# ", text, re.M)), 1)
                self.assertIn("**DE:**", text)
                self.assertIn("**EN:**", text)
                self.assertLess(text.index("**DE:**"), text.index("**EN:**"))
                self.assertIn(f"]({guide})", entry)

    def test_shared_agent_documentation_block_is_identical(self):
        blocks = []
        for surface in SURFACES:
            content = (ROOT / surface).read_text()
            blocks.append(content.split("<!-- documentation-reader-contract:start -->")[1]
                          .split("<!-- documentation-reader-contract:end -->")[0])
        self.assertTrue(all(block == blocks[0] for block in blocks))

    def test_installation_has_safe_env_and_distinct_platforms(self):
        text = (ROOT / "docs/fuer-lernende/installation.md").read_text()
        self.assertIn("if [ ! -e .env ]", text)
        self.assertIn("Test-Path -LiteralPath .env", text)
        for required in ("linux/arm64", "linux/amd64", "rootless", "PowerShell 7"):
            self.assertIn(required, text)
        self.assertNotIn("winget install podman-compose", text)
        self.assertNotIn("pip install podman-compose", text)

    def test_active_entrypoints_do_not_repeat_historical_scan_counts(self):
        for path in ("docs/fuer-lernende/README.md", "docs/betrieb/README.md",
                     "docs/fuer-lernende/erste-schritte.md"):
            text = (ROOT / path).read_text()
            self.assertNotIn("360 High", text)
            self.assertIn("toolchain-followups-2026-10-25.md", text)

    def test_a11y_boundary_is_not_automatic_conformance(self):
        text = (ROOT / "docs/fuer-lernende/barrierefreiheit.md").read_text()
        for required in ("Open", "Learning/A11Y Review", "Screenreader",
                         "3.1.5", "4.1.1", "Trigger"):
            self.assertIn(required, text)

    def test_daily_restart_handles_down_without_rebuild_or_replacement(self):
        text = (ROOT / "docs/fuer-lernende/alltag.md").read_text()
        self.assertIn("up -d --no-build --no-recreate --pull never ade", text)
        self.assertNotIn("podman compose start ade", text)
        for surface in SURFACES:
            content = (ROOT / surface).read_text()
            self.assertNotIn("bash scripts/compose-down-with-audit.sh --podman -v\n", content)
            self.assertNotIn(".\\scripts\\compose-down-with-audit.ps1 -Engine podman -Volumes\n", content)
            self.assertNotIn("\npodman compose down\n", content)
            self.assertNotIn("\npodman compose down -v\n", content)

    def test_profile_routine_stop_preserves_volumes_in_both_languages(self):
        text = (ROOT / "docs/fuer-lernende/sandbox-profil.md").read_text()

        def check_rows(content):
            rows = re.findall(r"^\| (?:Stoppen / Stop|Stop) \| (.*?) \|$",
                              content, re.M)
            self.assertEqual(len(rows), 2)
            for row in rows:
                self.assertEqual(re.findall(r"`([^`]+)`", row),
                                 ["bash scripts/compose-down-with-audit.sh --podman"])

        check_rows(text)
        for flag in ("-v", "--volumes", "-Volumes"):
            with self.subTest(flag=flag), self.assertRaises(AssertionError):
                check_rows(text.replace("--podman`", f"--podman {flag}`", 1))
        for warning in ("ausdrücklicher menschlicher Zustimmung", "vorherigem Audit-Export",
                        "kein Backup", "explicit human", "prior audit export",
                        "not a backup"):
            self.assertIn(warning, text)

    def test_profile_distinguishes_host_container_and_agent_boundaries(self):
        text = (ROOT / "docs/fuer-lernende/sandbox-profil.md").read_text()
        section = text.split("## 3 Schreibgrenzen / Write Boundaries", 1)[1].split("\n---", 1)[0]
        german = section.split("**DE:**", 1)[1].split("**EN:**", 1)[0]
        english = section.split("**EN:**", 1)[1]
        for phrase in ("Host-Mounts", "Container-Schreibschicht", "persistente Volumes",
                       "Benutzerrechte", "Container-Entfernung", "Stopp löscht",
                       "agentenspezifische", "keine allgemeine Betriebssystem-Sperre",
                       "nicht automatisch Schreibzugriff"):
            self.assertIn(phrase, german)
        for phrase in ("Host mounts", "container writable layer", "persistent volumes",
                       "user permissions", "container removal", "stopping alone",
                       "agent-specific", "not a general OS restriction",
                       "do not automatically permit Codex"):
            self.assertIn(phrase, english)
        for overclaim in ("Anything not listed here is unreachable",
                          "The container cannot write to anything outside",
                          "Alles, was nicht in dieser Liste steht"):
            self.assertNotIn(overclaim, text)
        config = (ROOT / "codex/config.toml").read_text()
        for setting in ("exclude_slash_tmp = true", "exclude_tmpdir_env_var = true"):
            self.assertIn(setting, german)
            self.assertIn(setting, english)
            self.assertIn(setting, config)

    def check_env_example(self, shell, existing):
        executable = shutil.which(shell)
        if not executable:
            self.skipTest(f"{shell} is unavailable")
        guide = (ROOT / "docs/fuer-lernende/installation.md").read_text()
        language = "bash" if shell == "bash" else "powershell"
        blocks = re.findall(r"```" + language + r"\n(.*?)```", guide, re.S)
        snippet = next(block for block in blocks
                       if ("if [ ! -e .env ]" if shell == "bash" else
                           "Test-Path -LiteralPath .env") in block)
        with tempfile.TemporaryDirectory(prefix="ade-env-example-") as directory:
            root = Path(directory)
            for filename in (".env.example", "opencode.env.example"):
                shutil.copyfile(ROOT / filename, root / filename)
            if existing:
                for filename in (".env", "opencode.env"):
                    (root / filename).write_text("KEEP-LOCAL-SETTINGS\n")
            command = [executable, "-c", snippet] if shell == "bash" else [
                executable, "-NoProfile", "-Command", "$ErrorActionPreference='Stop';\n" + snippet]
            subprocess.run(command, cwd=root, env=os.environ.copy(), check=True,
                           capture_output=True, text=True, timeout=30)
            for filename in (".env", "opencode.env"):
                expected = b"KEEP-LOCAL-SETTINGS\n" if existing else (root / (filename + ".example")).read_bytes()
                self.assertEqual((root / filename).read_bytes(), expected)

    def test_bash_env_creation_example(self):
        self.check_env_example("bash", False)

    def test_bash_env_existing_example(self):
        self.check_env_example("bash", True)

    def test_powershell_env_creation_example(self):
        self.check_env_example("pwsh", False)

    def test_powershell_env_existing_example(self):
        self.check_env_example("pwsh", True)


if __name__ == "__main__":
    unittest.main()
