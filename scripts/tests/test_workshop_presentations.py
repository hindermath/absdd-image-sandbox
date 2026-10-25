#!/usr/bin/env python3
"""Source/package regression checks, not native-app or human A11Y acceptance."""

import json
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "docs/praesentationen"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
BANNED = re.compile(r"gwdg|gitlab-ce|it4science|\bzki\b|manage-spec-kit-presets|/Users/|/var/folders/", re.I)


class WorkshopPresentationTests(unittest.TestCase):
    def source(self, lang):
        return (DIRECTORY / f"workshop-spec-kit.{lang}.md").read_text()

    def test_languages_have_matching_ids_and_complete_notes(self):
        expected = [f"W{i:02}" for i in range(1, 40)]
        for lang in ("de", "en"):
            text = self.source(lang)
            self.assertEqual(re.findall(r"<!-- slide: (W\d+) -->", text), expected)
            self.assertEqual(len(re.findall(r"(?m)^::: notes$", text)), 39)
            self.assertEqual(len(re.findall(r"(?m)^<!-- slide: W\d+ -->\n# ", text)), 39)
            self.assertIn(f"lang: {'de-DE' if lang == 'de' else 'en-GB'}", text)

    def test_sources_are_neutral_and_use_current_sandbox_commands(self):
        for lang in ("de", "en"):
            text = self.source(lang)
            self.assertIsNone(BANNED.search(text))
            for required in ("1.2.3", "--dry-run", "--check-only", "--podman",
                             "linux/arm64", "Ubuntu/WSL2", "$speckit-implement"):
                self.assertIn(required, text)
            self.assertNotIn("v1.0.0", text)

    def test_pilot_matrix_matches_local_versioned_source(self):
        matrix = json.loads((ROOT / "scripts/config/spec-kit-project-statistics-governance-presets.json").read_text())
        self.assertEqual(len(matrix["presets"]), 14)
        for item in matrix["presets"]:
            row = f"| {item['id']} | {item['version']} | {item['priority']} |"
            for lang in ("de", "en"):
                self.assertIn(row, self.source(lang))

    def test_pptx_has_39_editable_slides_and_39_note_parts(self):
        for lang in ("de", "en"):
            with self.subTest(lang=lang), zipfile.ZipFile(DIRECTORY / "exports" / f"workshop-spec-kit.{lang}.pptx") as package:
                slides = [name for name in package.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)]
                notes = [name for name in package.namelist() if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", name)]
                self.assertEqual(len(slides), 39)
                self.assertEqual(len(notes), 39)
                for name in slides:
                    root = ET.fromstring(package.read(name))
                    self.assertGreaterEqual(len(root.findall(f".//{A}t")), 3, name)
                    self.assertNotIn(b"<p:pic", package.read(name), name)

    def test_package_text_notes_links_and_metadata_are_neutral(self):
        for lang in ("de", "en"):
            with zipfile.ZipFile(DIRECTORY / "exports" / f"workshop-spec-kit.{lang}.pptx") as package:
                for name in package.namelist():
                    if name.endswith((".xml", ".rels")):
                        text = package.read(name).decode("utf-8")
                        self.assertIsNone(BANNED.search(text), f"{lang}: {name}")

    def test_keynote_exports_are_native_39_slide_packages(self):
        for lang in ("de", "en"):
            path = DIRECTORY / "exports" / f"workshop-spec-kit.{lang}.key"
            with self.subTest(lang=lang), zipfile.ZipFile(path) as package:
                self.assertIsNone(package.testzip())
                names = package.namelist()
                self.assertIn("Index/Document.iwa", names)
                self.assertIn("Metadata/Properties.plist", names)
                self.assertIn("preview.jpg", names)
                slides = [name for name in names
                          if re.fullmatch(r"Index/Slide(?:-\d+-\d+)?\.iwa", name)]
                self.assertEqual(len(slides), 39)
                self.assertNotIn("[Content_Types].xml", names)

    def test_shell_flags_are_not_converted_to_typographic_dashes(self):
        for lang in ("de", "en"):
            with zipfile.ZipFile(DIRECTORY / "exports" / f"workshop-spec-kit.{lang}.pptx") as package:
                root = ET.fromstring(package.read("ppt/slides/slide17.xml"))
                text = " ".join(item.text or "" for item in root.findall(f".//{A}t"))
                self.assertIn("--dry-run", text)
                self.assertNotIn("\u2013dry-run", text)

    def test_exporter_and_index_record_nonclaims(self):
        script = (ROOT / "scripts/export-workshop-presentations.mjs").read_text()
        self.assertIn("markdown+fenced_divs-smart", script)
        index = (DIRECTORY / "README.md").read_text()
        for required in ("Open", "Learning/A11Y Review", "Keynote", ".key", "WCAG"):
            self.assertIn(required, index)
        for lang in ("de", "en"):
            self.assertIn(f"exports/workshop-spec-kit.{lang}.pptx", index)
            self.assertIn(f"exports/workshop-spec-kit.{lang}.key", index)
        self.assertIn("com.apple.Keynote", index)
        self.assertNotIn("Keynote derzeit nicht installiert", index)
        self.assertNotIn("Keynote\nis not currently installed", index)


if __name__ == "__main__":
    unittest.main()
