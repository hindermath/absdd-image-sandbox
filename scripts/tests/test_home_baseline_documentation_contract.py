#!/usr/bin/env python3
"""Validate the documentation boundary between Home Baseline and the image."""

from __future__ import annotations

from pathlib import Path
import re
import unittest


REPOSITORY = Path(__file__).resolve().parents[2]
HOME_ARCHITECTURE_URL = (
    "https://github.com/hindermath/home-baseline/blob/main/"
    "docs/architecture/source-and-home-runtime.md"
)
GUIDANCE_FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".github/copilot-instructions.md",
    ".github/agents/copilot-instructions.md",
)
BOUNDARY_FILES = (
    "README.md",
    "docs/fuer-lernende/README.md",
    "docs/betrieb/README.md",
    "docs/betrieb/image-aufbau.md",
)
REQUIRED_MSL = (".NET/C#", "Java", "Go", "Rust", "Python", "Swift")
SECURE_MOUNT_TARGETS = {
    "/secure-case-tracker-projects",
    "/secure-service-harvester-projects",
    "/secure-order-desk-projects",
}


def read_text(relative_path: str) -> str:
    return (REPOSITORY / relative_path).read_text(encoding="utf-8")


def normalize_whitespace(content: str) -> str:
    return re.sub(r"\s+", " ", content)


class HomeBaselineDocumentationContractTests(unittest.TestCase):
    def test_binding_audience_is_synchronized(self) -> None:
        for relative_path in ("README.md", *GUIDANCE_FILES):
            with self.subTest(path=relative_path):
                content = read_text(relative_path)
                self.assertIn("IT-System-Elektroniker*innen", content)
                self.assertIn(
                    "IT systems electronics technician apprentices",
                    normalize_whitespace(content),
                )

    def test_required_language_paths_are_unambiguous(self) -> None:
        shared_contract = (
            "six required memory-safe language toolchains "
            "(.NET/C#, Java, Go, Rust, Python, and Swift)"
        )
        for relative_path in GUIDANCE_FILES:
            with self.subTest(path=relative_path):
                content = read_text(relative_path)
                normalized = normalize_whitespace(content)
                self.assertIn(shared_contract, normalized)
                self.assertIn("PowerShell 7 as a second scripting foundation", content)
                self.assertIn("Node.js/npm as supporting tooling", content)
                self.assertNotIn(
                    "six memory-safe language toolchains, Python and PowerShell",
                    content,
                )

        learner_toolchains = read_text("docs/fuer-lernende/toolchains/README.md")
        for language in REQUIRED_MSL:
            self.assertIn(language, learner_toolchains)
        self.assertIn("not a seventh required MSL learning path", learner_toolchains)

        sandbox_profile = normalize_whitespace(
            read_text("docs/fuer-lernende/sandbox-profil.md")
        )
        self.assertIn("Python is one of the six required MSL paths", sandbox_profile)
        self.assertIn("PowerShell 7 as the second scripting foundation", sandbox_profile)

    def test_pinned_image_and_current_upstream_are_distinguished(self) -> None:
        for relative_path in BOUNDARY_FILES:
            with self.subTest(path=relative_path):
                content = read_text(relative_path)
                self.assertIn("home-baseline.lock.json", content)
                self.assertIn(HOME_ARCHITECTURE_URL, content)
                self.assertIn("may be newer", normalize_whitespace(content))

    def test_image_mount_scope_is_exactly_the_documented_subset(self) -> None:
        compose = read_text("compose.yml")
        targets = set(
            re.findall(r"^\s*target:\s*(/secure-[a-z-]+-projects)\s*$", compose, re.MULTILINE)
        )
        self.assertEqual(targets, SECURE_MOUNT_TARGETS)
        self.assertNotIn("inventory-hub", compose.lower())

        for relative_path in ("README.md", "docs/betrieb/README.md"):
            with self.subTest(path=relative_path):
                content = read_text(relative_path)
                self.assertIn("CaseTracker", content)
                self.assertIn("ServiceHarvester", content)
                self.assertIn("OrderDesk", content)
                self.assertIn("Home Baseline catalog", content)


if __name__ == "__main__":
    unittest.main()
