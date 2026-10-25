#!/usr/bin/env python3
"""Portable learning-package contracts; not product, platform or human acceptance."""

import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
PACKAGES = ROOT / "docs/lernwerkstaetten"
PRESETS = ROOT / ".specify/presets"
SIZES = {"sysinfo": 6, "web-mvc": 4, "web-rest": 4}
MANIFEST = Path("specs/intake-series/learning/manifest.json")
RECEIPT = Path("specs/intake-series/learning/receipt.json")
REQUEST = Path("specs/intake-review-requests/learning.json")
BANNED = re.compile(r"gwdg|gitlab-ce|it4science|(?<![A-Za-z0-9])/(?:Users|var/folders)/|127\.0\.0\.1:60363", re.I)


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(text.encode()).hexdigest()


class LearningWorkshopTests(unittest.TestCase):
    def run_validator(self, kind, path, package, shell):
        if kind == "operation":
            script = PRESETS / "intake-authoring-governance/scripts/validate-intake-authoring-artifact"
        elif kind == "authoring":
            script = PRESETS / "intake-authoring-governance/scripts/validate-intake-authoring-receipt"
        else:
            script = PRESETS / f"intake-sequencing-governance/scripts/validate-intake-series-{kind}"
        if shell == "bash":
            args = ["bash", str(script) + ".sh",
                    {"authoring": "--receipt", "operation": "--artifact"}.get(kind, "--file"), str(path), "--repo", str(package)]
        else:
            args = ["pwsh", "-NoLogo", "-NoProfile", "-File", str(script) + ".ps1",
                    {"authoring": "-Receipt", "operation": "-Artifact"}.get(kind, "-File"), str(path), "-Repo", str(package)]
        result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=90)
        self.assertEqual(result.returncode, 0, f"{shell} {path}: {result.stdout}\n{result.stderr}")
        self.assertIn("PASS", result.stdout)

    def test_all_authoring_and_series_artifacts_in_both_shells(self):
        for executable in ("bash", "pwsh"):
            if not shutil.which(executable):
                self.skipTest(f"{executable} unavailable; no cross-shell success claimed")
        for slug in SIZES:
            package = PACKAGES / slug
            for shell in ("bash", "pwsh"):
                with self.subTest(package=slug, shell=shell):
                    self.run_validator("manifest", package / MANIFEST, package, shell)
                    self.run_validator("receipt", package / RECEIPT, package, shell)
                    for path in sorted((package / "specs/intake-authoring-receipts").glob("*.json")):
                        self.run_validator("authoring", path, package, shell)

    def test_packages_relocate_without_private_or_parent_paths(self):
        with tempfile.TemporaryDirectory(prefix="ade-learning-relocation-") as directory:
            for slug in SIZES:
                moved = Path(directory) / slug
                shutil.copytree(PACKAGES / slug, moved)
                self.run_validator("manifest", moved / MANIFEST, moved, "bash")
                self.run_validator("receipt", moved / RECEIPT, moved, "bash")
                first = sorted((moved / "specs/intake-authoring-receipts").glob("*.json"))[0]
                self.run_validator("authoring", first, moved, "bash")

    def test_authoring_journals_describe_only_draft_artifact_publication(self):
        for slug, count in SIZES.items():
            package = PACKAGES / slug
            operations = list((package / "specs/intake-authoring-operations").glob("*/operation.json"))
            self.assertEqual(len(operations), 1)
            operation = load(operations[0])
            self.assertEqual(operation["status"], "Completed")
            self.assertEqual(operation["publicationScope"], "ReusableDraftPackageOnly")
            self.assertEqual(len(operation["validatedTargets"]), count)
            self.assertEqual(operation["intendedTargets"], operation["publishedTargets"])
            for shell in ("bash", "pwsh"):
                self.run_validator("operation", operations[0], package, shell)

    def test_exact_stage_order_pending_draft_and_review_handoff(self):
        all_ids = set()
        for slug, count in SIZES.items():
            package = PACKAGES / slug
            manifest = load(package / MANIFEST)
            request = load(package / REQUEST)
            self.assertEqual(manifest["status"], "Draft")
            self.assertEqual(len(manifest["orderedTargets"]), count)
            paths = [target["path"] for target in manifest["orderedTargets"]]
            self.assertEqual(paths, sorted(paths))
            self.assertEqual(manifest["roots"], paths[:1])
            self.assertEqual(len(manifest["dependencies"]), count - 1)
            self.assertTrue(all(t["status"] == "Pending" for t in manifest["orderedTargets"]))
            for i, edge in enumerate(manifest["dependencies"]):
                self.assertEqual((edge["from"], edge["to"]), (paths[i], paths[i + 1]))
                self.assertEqual(edge["kind"], "HardCompletionGate")
                self.assertIs(edge["binding"], True)
            self.assertEqual(request["mode"], "Series")
            self.assertEqual(request["series"]["orderedTargetPaths"], paths)
            self.assertEqual(request["series"]["roots"], manifest["roots"])
            self.assertEqual(request["series"]["dependencies"], manifest["dependencies"])
            self.assertEqual([t["path"] for t in request["targets"]], paths)
            for receipt in (package / "specs/intake-authoring-receipts").glob("*.json"):
                item = load(receipt)
                self.assertNotIn(item["intakeId"], all_ids)
                all_ids.add(item["intakeId"])
                self.assertEqual(item["provenanceMode"], "New")
                self.assertEqual(item["deliveryAuthority"], "LocalImplementation")
                self.assertEqual(item["status"], "ReadyForReview")
                self.assertEqual(item["target"]["normalizedSha256"], digest(package / item["target"]["path"]))
        self.assertEqual(len(all_ids), 14)

    def test_intakes_have_bilingual_product_acceptance_and_bounded_prompts(self):
        for slug, count in SIZES.items():
            files = sorted((PACKAGES / slug / "intakes").glob("*.md"))
            self.assertEqual(len(files), count)
            for path in files:
                with self.subTest(path=path):
                    text = path.read_text()
                    self.assertLess(text.index("## Deutsch"), text.index("## English"))
                    requirements = set(re.findall(r"FR-(\d+)", text))
                    acceptance = set(re.findall(r"AC-(\d+)", text))
                    self.assertGreaterEqual(len(requirements), 4)
                    self.assertEqual(requirements, acceptance)
                    self.assertIn("LocalImplementation", text)
                    self.assertIn(f"intakes/{path.name}", text)
                    for marker in ("begin", "prompts", "end"):
                        self.assertEqual(text.count(f"<!-- intake-authoring:{marker} -->"), 1)
                    self.assertIn("$speckit-specify", text)
                    self.assertIn("$speckit-autonomous", text)
                    self.assertIn("Pending", text)

    def test_four_decks_have_paired_ids_and_notes(self):
        for topic, prefix in (("sysinfo", "S"), ("web", "B")):
            for lang, locale in (("de", "de-DE"), ("en", "en-GB")):
                path = ROOT / f"docs/praesentationen/werkstatt-{topic}.{lang}.md"
                text = path.read_text()
                self.assertEqual(re.findall(r"<!-- slide: (\w+) -->", text),
                                 [f"{prefix}{i:02}" for i in range(1, 17)])
                self.assertEqual(text.count("::: notes"), 16)
                self.assertIn(f"lang: {locale}", text)
                self.assertIn("Pending", text)

    def test_sources_are_neutral_and_no_reference_approval_is_inherited(self):
        for path in PACKAGES.rglob("*"):
            if path.suffix not in (".json", ".md"):
                continue
            self.assertIsNone(BANNED.search(path.read_text()), str(path))
        for slug in SIZES:
            catalog = load(PACKAGES / slug / "sources.json")
            self.assertIn("no source approval", catalog["proofBoundary"])
            self.assertTrue(catalog["adaptations"])
            for reference in catalog["references"]:
                self.assertRegex(reference["commit"], r"^[0-9a-f]{40}$")
                self.assertRegex(reference["rawSha256"], r"^[0-9a-f]{64}$")
                self.assertRegex(reference["normalizedSha256"], r"^[0-9a-f]{64}$")
        for path in (ROOT / "docs/praesentationen").glob("werkstatt-*.md"):
            self.assertIsNone(BANNED.search(path.read_text()), str(path))

    def test_safety_and_route_boundaries_are_explicit(self):
        sysinfo = (PACKAGES / "sysinfo/basis.md").read_text()
        for value in ("--collect container", "--include-sensitive", "80 %", "kein persistentes", "unavailable"):
            self.assertIn(value.lower(), sysinfo.lower())
        for slug in ("web-mvc", "web-rest"):
            text = (PACKAGES / slug / "basis.md").read_text()
            for value in ("70 %", "HTTPS", "SQLite", "64 KiB", "5111", "Loopback"):
                self.assertIn(value.lower(), text.lower())
            self.assertTrue((PACKAGES / slug / "decision.md").is_file())
        rest = (PACKAGES / "web-rest/basis.md").read_text()
        self.assertIn("5112", rest)
        self.assertIn("serverseitiger", rest)
        self.assertIn("keine zusätzliche CORS", rest)

    def test_order_tables_and_mermaid_match_manifest(self):
        for slug in SIZES:
            package = PACKAGES / slug
            text = (package / "order.md").read_text()
            self.assertLess(text.index("**DE:**"), text.index("```mermaid"))
            self.assertLess(text.index("**EN:**"), text.index("```mermaid"))
            manifest = load(package / MANIFEST)
            for target in manifest["orderedTargets"]:
                self.assertIn(f']({target["path"]}) | Pending', text)
            prefix = {"sysinfo": "SYS", "web-mvc": "MVC", "web-rest": "REST"}[slug]
            diagram = text.split("```mermaid", 1)[1].split("```", 1)[0]
            edges = re.findall(r"(?m)^\s+([A-Z]+\d+)(?:\[[^\]\n]+\])?\s+-->\s+([A-Z]+\d+)", diagram)
            self.assertEqual(edges, [(f"{prefix}{i:02}", f"{prefix}{i+1:02}")
                                     for i in range(SIZES[slug] - 1)])
            for i in range(SIZES[slug]):
                self.assertIn(f"{prefix}{i:02}[{prefix}-{i:02} Pending]", diagram)


if __name__ == "__main__":
    unittest.main()
