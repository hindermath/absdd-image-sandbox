#!/usr/bin/env python3
"""Template documentation and isolated Git contracts, not GitHub acceptance."""

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SURFACES = ("AGENTS.md", "CLAUDE.md", "GEMINI.md",
            ".github/copilot-instructions.md", ".github/agents/copilot-instructions.md")


class TemplateProfileTests(unittest.TestCase):
    def read(self, path):
        return (ROOT / path).read_text(encoding="utf-8")

    def test_shared_guidance_and_no_inherited_authority(self):
        blocks = []
        for path in SURFACES:
            text = self.read(path)
            block = text.split("<!-- optional-template-profile:start -->", 1)[1].split(
                "<!-- optional-template-profile:end -->", 1)[0]
            blocks.append(block)
            for required in ("nicht aktiviert", "Referenzkontext", "Keine kopierten", "Level-0"):
                self.assertIn(required, block)
        self.assertEqual(len(set(blocks)), 1)

    def test_license_scopes_and_unresolved_rights_gate(self):
        license_text = self.read("LICENSE")
        self.assertTrue(license_text.startswith("MIT License\n"))
        self.assertIn('THE SOFTWARE IS PROVIDED "AS IS"', license_text)
        rights = self.read("docs/licensing.md")
        for required in ("nachweislich eigenen", "LIC-01", "LIC-02", "Open", "Follow-up", "Trigger"):
            self.assertIn(required, rights)
        self.assertEqual(len(list((ROOT / ".specify/presets").glob("*/LICENSE"))), 14)
        for path in (ROOT / ".specify/presets").glob("*/LICENSE"):
            self.assertIn("MIT License", path.read_text())

    def test_profile_keeps_fork_self_build_and_separate_products(self):
        text = self.read("docs/fuer-lernende/template-profil.md")
        for required in ("nicht aktiviert", "nur `main`", "Podman", "Selbstbau", "Leeres",
                         "--allow-unrelated-histories", "Home-Baseline"):
            self.assertIn(required, text)
        handover = self.read("docs/betrieb/template-erstuebernahme.md")
        for required in ("kein ausführendes", "CODEOWNERS", "Statistik", "Referenzkontext", "Secrets", "Open"):
            self.assertIn(required, handover)

    def test_workflow_yaml_and_only_reference_specific_proof_is_scoped(self):
        if not shutil.which("ruby"):
            self.skipTest("Existing Ruby/Psych parser unavailable; no YAML-parser success claimed")
        def parse(name):
            result = subprocess.run(["ruby", "-r", "yaml", "-r", "json", "-e",
                                     "puts JSON.generate(YAML.load_file(ARGV[0]))",
                                     str(ROOT / ".github/workflows" / name)],
                                    capture_output=True, text=True, timeout=15)
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)
        workflow = parse("gsdb-pilot-contracts.yml")
        job = workflow["jobs"]["gsdb"]
        self.assertNotIn("if", job)
        scoped = [step for step in job["steps"] if "if" in step]
        self.assertEqual(len(scoped), 1)
        self.assertEqual(scoped[0]["if"], "github.repository == 'hindermath/absdd-image-sandbox'")
        self.assertIn("-Action Status", scoped[0]["run"])
        general = "\n".join(step.get("run", "") for step in job["steps"] if "if" not in step)
        for required in ("test_spec_kit_agent_surface_parity", "-CheckOnly", "test-gsdb-consolidation", "test-secure-development-assurance"):
            self.assertIn(required, general)
        pilot = parse("project-statistics-pilot-native-proof.yml")
        self.assertEqual(pilot["jobs"]["native-proof"]["if"], scoped[0]["if"])
        static = parse("documentation-and-sandbox.yml")
        for general_job in static["jobs"].values():
            self.assertNotIn("if", general_job)
        parse("homogeneity-check.yml")

    def test_new_requirement_pairs_preserve_blocked_lifecycle(self):
        text = self.read("intakes/learner-fork-self-build-sandbox.md")
        for prefix, start in (("L-FR", 20), ("L-AC", 17)):
            for i in range(start, start + 4):
                self.assertEqual(text.count(f"**{prefix}-{i:03}:**"), 2)
        manifest = json.loads(self.read("specs/intake-series/sandbox-development-lifecycle/manifest.json"))
        self.assertEqual([item["status"] for item in manifest["orderedTargets"]],
                         ["Completed", "Eligible", "Blocked", "Blocked", "Blocked"])
        self.assertEqual(manifest["orderedTargets"][2]["path"],
                         "Lastenheft_Sandbox-Feature-Update-Ubuntu2604-OpenCode-Web-MSL.md")
        edges = {(edge["from"], edge["to"]) for edge in manifest["dependencies"] if edge["binding"]}
        self.assertIn((manifest["orderedTargets"][1]["path"], manifest["orderedTargets"][2]["path"]), edges)
        self.assertIn((manifest["orderedTargets"][2]["path"], manifest["orderedTargets"][3]["path"]), edges)

    def test_link_exclusion_is_only_for_byte_identical_archived_order_views(self):
        workflow = self.read(".github/workflows/documentation-and-sandbox.yml")
        pattern = r"(^|/)specs/intake-series-archive/[^/]+/[^/]+/(order|requirements-order)\.md$"
        self.assertIn(pattern, workflow)
        self.assertIn("python3 scripts/tests/test_template_profile.py", workflow)
        for name in ("order", "requirements-order"):
            self.assertRegex(f"specs/intake-series-archive/series/operation/{name}.md", pattern)
        for path in ("specs/intake-series/series/order.md", "docs/fuer-lernende/template-profil.md",
                     "specs/intake-series-archive/series/operation/README.md"):
            self.assertIsNone(re.search(pattern, path))

    def fixture_git(self, root, *args, check=True):
        env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1",
                   GIT_AUTHOR_NAME="Fixture", GIT_AUTHOR_EMAIL="fixture@example.invalid",
                   GIT_COMMITTER_NAME="Fixture", GIT_COMMITTER_EMAIL="fixture@example.invalid")
        result = subprocess.run(["git", "-C", str(root), *args], env=env,
                                capture_output=True, text=True, timeout=15)
        if check:
            self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def init_fixture(self, directory, message):
        directory.mkdir()
        self.fixture_git(directory, "init", "-b", "main")
        (directory / "README.md").write_text("source version 1\n")
        (directory / "evidence.json").write_text('{"sourceStatus":"Completed","personalEvidence":false}\n')
        self.fixture_git(directory, "add", "README.md", "evidence.json")
        self.fixture_git(directory, "commit", "-m", message)

    def test_fork_fixture_has_shared_history_and_preserves_local_file(self):
        with tempfile.TemporaryDirectory(prefix="ade-template-fork-") as temp:
            source, fork = Path(temp) / "reference", Path(temp) / "fork"
            self.init_fixture(source, "reference initial")
            self.fixture_git(source, "clone", "--no-local", str(source), str(fork))
            (fork / "personal.env").write_text("noncredential fixture\n")
            (source / "README.md").write_text("source version 2\n")
            self.fixture_git(source, "add", "README.md")
            self.fixture_git(source, "commit", "-m", "reference update")
            self.fixture_git(fork, "fetch", "origin")
            self.fixture_git(fork, "merge", "--ff-only", "origin/main")
            self.assertEqual((fork / "personal.env").read_text(), "noncredential fixture\n")
            self.assertEqual((fork / "README.md").read_text(), "source version 2\n")

    def test_template_fixture_remains_unrelated_and_source_evidence_is_not_reset(self):
        with tempfile.TemporaryDirectory(prefix="ade-template-independent-") as temp:
            source, copy = Path(temp) / "reference", Path(temp) / "template"
            self.init_fixture(source, "reference history")
            self.init_fixture(copy, "independent template initial")
            original = (copy / "evidence.json").read_bytes()
            self.fixture_git(copy, "remote", "add", "upstream", str(source))
            self.fixture_git(copy, "fetch", "upstream")
            self.assertEqual(self.fixture_git(copy, "merge-base", "HEAD", "upstream/main", check=False).returncode, 1)
            self.assertNotEqual(self.fixture_git(copy, "merge", "--ff-only", "upstream/main", check=False).returncode, 0)
            self.assertEqual((copy / "evidence.json").read_bytes(), original)
            self.assertIs(json.loads(original)["personalEvidence"], False)


if __name__ == "__main__":
    unittest.main()
