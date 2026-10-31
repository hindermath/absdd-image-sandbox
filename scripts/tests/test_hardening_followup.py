"""Feature 004 contract negatives using synthetic evidence only."""

from __future__ import annotations

import copy
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "secure_development_hardening",
    ROOT / "scripts/lib/secure_development_hardening.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
CONTRACT_HASH = "a" * 64


def checkpoint(number: int) -> dict:
    return {
        "gateId": f"G004-{number:02d}",
        "applicability": "Open",
        "implementation": "Not Assessed",
        "reason": "Synthetic unreviewed gate",
        "evidenceIds": [],
        "owner": "Repository Maintainer",
        "reviewer": "Security Review",
        "residualRisk": "Not yet measured",
        "nextAction": "Run isolated verification",
        "dueAt": "Before affected use",
        "reevaluationTrigger": "Source change",
    }


class Feature004EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name)
        self.source = self.repo / "context.txt"
        self.source.write_bytes(b"\xef\xbb\xbfline1\r\nline2\r\n")
        self.raw = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.normalized = MODULE.normalized_sha256(self.source)
        self.requirements = {
            "schemaVersion": "1.0",
            "feature": MODULE.FEATURE_004_ID,
            "gitHead": "synthetic-head",
            "gateCount": 18,
            "gates": [{"gateId": f"G004-{number:02d}"} for number in range(1, 19)],
            "quickstartCheckIds": [f"Q{number}" for number in range(1, 9)],
            "sourceBindings": [{
                "path": "context.txt",
                "hashKind": "text/raw-and-utf8-lf",
                "rawSha256": self.raw,
                "normalizedSha256": self.normalized,
            }],
            "executedEvidenceRequiredFields": [
                "evidenceId", "gateId", "commandArgv", "cwdClass", "gitHead",
                "inputHashes", "payloadSha256", "decisionSha256", "runner",
                "platform", "architecture", "observedAt", "exitCode",
                "outcome", "writeScope", "logPath", "limitations",
            ],
        }
        self.document = {
            "schemaVersion": "1.0",
            "feature": MODULE.FEATURE_004_ID,
            "gateRequirementsSha256": CONTRACT_HASH,
            "gitHead": "synthetic-head",
            "checkpoints": [checkpoint(number) for number in range(1, 19)],
            "evidenceRecords": [],
        }

    def validate(self, document=None, requirements=None):
        return MODULE.validate_feature_004_evidence(
            document or self.document,
            requirements or self.requirements,
            self.repo,
            CONTRACT_HASH,
        )

    def executed_record(self, *, kind="rawSha256", digest=None):
        return {
            "evidenceId": "E1", "gateId": "G004-01",
            "commandArgv": ["synthetic", "check"], "cwdClass": "temporary",
            "gitHead": "synthetic-head",
            "inputHashes": {
                "context.txt": {"kind": kind, "digest": digest or self.raw}
            },
            "payloadSha256": "b" * 64, "decisionSha256": "c" * 64,
            "runner": "synthetic", "platform": "macOS", "architecture": "arm64",
            "observedAt": "2026-10-31T15:00:00Z", "exitCode": 0,
            "outcome": "Passed", "writeScope": "temporary",
            "logPath": "synthetic.log", "limitations": "synthetic test only",
        }

    def test_open_baseline_is_valid_without_fabricated_execution(self):
        self.assertEqual([], self.validate())

    def test_status_and_evidence_require_real_fields(self):
        for mutation, marker in (
            (lambda item: item.update(implementation="Fulfilled"), "invalid applicability"),
            (lambda item: item.pop("owner"), "missing owner"),
            (lambda item: item.pop("reevaluationTrigger"), "missing reevaluationTrigger"),
            (lambda item: item.update(gateId="G004-99"), "checkpoint set is incomplete"),
        ):
            with self.subTest(marker=marker):
                candidate = copy.deepcopy(self.document)
                mutation(candidate["checkpoints"][0])
                self.assertIn(marker, " | ".join(self.validate(candidate)))

    def test_raw_and_normalized_hash_kinds_are_distinct(self):
        candidate = copy.deepcopy(self.document)
        candidate["evidenceRecords"] = [
            self.executed_record(kind="normalizedSha256", digest=self.normalized)
        ]
        candidate["checkpoints"][0]["evidenceIds"] = ["E1"]
        self.assertEqual([], self.validate(candidate))

        candidate["evidenceRecords"][0]["inputHashes"]["context.txt"]["digest"] = self.raw
        self.assertIn("wrong-kind input hash", " | ".join(self.validate(candidate)))

    def test_not_run_and_old_context_fail_closed(self):
        candidate = copy.deepcopy(self.document)
        candidate["evidenceRecords"] = [{
            "evidenceId": "E1", "gateId": "G004-01",
            "gitHead": "old-head", "outcome": "NotRun", "exitCode": 0,
            "owner": "Maintainer", "nextAction": "Retry", "trigger": "Source change",
            "limitations": "not run",
        }]
        candidate["gateRequirementsSha256"] = "d" * 64
        errors = " | ".join(self.validate(candidate))
        self.assertIn("requirements hash is stale", errors)
        self.assertIn("stale Git context", errors)
        self.assertIn("invents execution data", errors)

    def test_source_bindings_reject_old_raw_hash_even_with_current_normalized_hash(self):
        requirements = copy.deepcopy(self.requirements)
        requirements["sourceBindings"][0]["rawSha256"] = "0" * 64
        self.assertIn("raw hash is stale", " | ".join(self.validate(requirements=requirements)))

    def test_malformed_gate_and_q_metadata_fail_as_contract_errors(self):
        requirements = copy.deepcopy(self.requirements)
        requirements["gates"][0]["gateId"] = ["G004-01"]
        requirements["quickstartCheckIds"][0] = {"id": "Q1"}
        errors = " | ".join(self.validate(requirements=requirements))
        self.assertIn("requires exactly G004-01", errors)
        self.assertIn("Q1-Q8 binding is incomplete", errors)

    def test_feature_004_all_cannot_pass_with_open_gates_or_rewrite_evidence(self):
        feature = self.repo / "specs/004-container-hardening-followup"
        feature.mkdir(parents=True)
        requirements = copy.deepcopy(self.requirements)
        for gate in requirements["gates"]:
            gate["quickstartChecks"] = ["Q1"]
        requirements_path = feature / "gate-requirements.json"
        requirements_path.write_text(json.dumps(requirements), encoding="utf-8")
        document = copy.deepcopy(self.document)
        document["gateRequirementsSha256"] = hashlib.sha256(
            requirements_path.read_bytes()
        ).hexdigest()
        evidence_path = self.repo / "evidence.json"
        evidence_path.write_text(json.dumps(document), encoding="utf-8")
        before = evidence_path.read_bytes()
        with mock.patch.object(MODULE, "validate_feature_004_assurance_profile", return_value=[]), contextlib.redirect_stderr(io.StringIO()):
            result = MODULE.execute_feature_004_mode(
                self.repo, "All", "evidence.json", False,
                "specs/004-container-hardening-followup",
            )
        self.assertEqual(3, result)
        self.assertEqual(before, evidence_path.read_bytes())

        document["checkpoints"][0]["gateId"] = "G004-99"
        evidence_path.write_text(json.dumps(document), encoding="utf-8")
        before = evidence_path.read_bytes()
        with mock.patch.object(MODULE, "validate_feature_004_assurance_profile", return_value=[]), contextlib.redirect_stderr(io.StringIO()):
            result = MODULE.execute_feature_004_mode(
                self.repo, "All", "evidence.json", False,
                "specs/004-container-hardening-followup",
            )
        self.assertEqual(1, result)
        self.assertEqual(before, evidence_path.read_bytes())


class ExplicitSbomSelectionTests(unittest.TestCase):
    def test_both_analyzers_require_an_explicit_sbom_even_in_preview(self):
        cases = [
            ("bash", ["bash", str(ROOT / "scripts/analyze-sbom.sh"), "--dry-run"]),
            ("pwsh", ["pwsh", "-NoProfile", "-File",
                      str(ROOT / "scripts/analyze-sbom.ps1"), "-WhatIf"]),
        ]
        for runner, command in cases:
            if not shutil.which(runner):
                continue
            with self.subTest(runner=runner):
                result = subprocess.run(command, capture_output=True, text=True, timeout=10)
                self.assertNotEqual(0, result.returncode)
                self.assertIn("required", result.stdout + result.stderr)

    def test_both_analyzers_use_the_selected_synthetic_sbom(self):
        with tempfile.TemporaryDirectory(prefix="ade004-sbom-") as directory:
            selected = Path(directory) / "selected.cdx.json"
            selected.write_text(json.dumps({
                "bomFormat": "CycloneDX", "specVersion": "1.7",
                "metadata": {"timestamp": "2026-10-31T00:00:00Z",
                             "component": {"name": "synthetic", "version": "1"}},
                "components": [],
            }), encoding="utf-8")
            cases = [
                ("bash", ["bash", str(ROOT / "scripts/analyze-sbom.sh"),
                          "--file", str(selected)]),
                ("pwsh", ["pwsh", "-NoProfile", "-File",
                          str(ROOT / "scripts/analyze-sbom.ps1"),
                          "-SbomPath", str(selected)]),
            ]
            for runner, command in cases:
                if not shutil.which(runner):
                    continue
                with self.subTest(runner=runner):
                    result = subprocess.run(command, capture_output=True, text=True,
                                            timeout=10, env=os.environ.copy())
                    self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                    self.assertIn("synthetic", result.stdout)

    def test_both_analyzers_reject_unpinned_scanner_override(self):
        with tempfile.TemporaryDirectory(prefix="ade004-sbom-") as directory:
            selected = Path(directory) / "selected.cdx.json"
            selected.write_text("{}", encoding="utf-8")
            cases = [
                ("bash", ["bash", str(ROOT / "scripts/analyze-sbom.sh"),
                          "--file", str(selected), "--scan", "--dry-run"],
                 {"GRYPE_IMAGE": "ghcr.io/anchore/grype:latest"}),
                ("pwsh", ["pwsh", "-NoProfile", "-File",
                          str(ROOT / "scripts/analyze-sbom.ps1"),
                          "-SbomPath", str(selected), "-Scan", "-WhatIf",
                          "-GrypeImage", "ghcr.io/anchore/grype:latest"], {}),
            ]
            for runner, command, extra_env in cases:
                if not shutil.which(runner):
                    continue
                with self.subTest(runner=runner):
                    result = subprocess.run(command, capture_output=True, text=True,
                                            timeout=10, env=dict(os.environ, **extra_env))
                    self.assertNotEqual(0, result.returncode)
                    self.assertIn("pinned", result.stdout + result.stderr)

    def test_both_analyzers_preserve_sbom_argument_and_fail_on_scanner_error(self):
        with tempfile.TemporaryDirectory(prefix="ade004-sbom-") as directory:
            root = Path(directory)
            selected = root / "selected with spaces.cdx.json"
            selected.write_text(json.dumps({
                "bomFormat": "CycloneDX", "specVersion": "1.7",
                "metadata": {"timestamp": "2026-10-31T00:00:00Z"},
                "components": [],
            }), encoding="utf-8")
            fake_bin = root / "bin"
            fake_bin.mkdir()
            fake_podman = fake_bin / "podman"
            fake_podman.write_text(
                '#!/bin/sh\nprintf "%s\\n" "$@" > "$ADE_TEST_ARGS"\nexit 7\n',
                encoding="utf-8",
            )
            fake_podman.chmod(0o755)
            cases = [
                ("bash", ["bash", str(ROOT / "scripts/analyze-sbom.sh"),
                          "--file", str(selected), "--scan"]),
                ("pwsh", ["pwsh", "-NoProfile", "-File",
                          str(ROOT / "scripts/analyze-sbom.ps1"),
                          "-SbomPath", str(selected), "-Scan"]),
            ]
            for runner, command in cases:
                if not shutil.which(runner):
                    continue
                with self.subTest(runner=runner):
                    args_file = root / f"{runner}-args.txt"
                    env = dict(os.environ, PATH=f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
                               ADE_TEST_ARGS=str(args_file))
                    result = subprocess.run(command, cwd=ROOT, capture_output=True,
                                            text=True, timeout=10, env=env)
                    self.assertNotEqual(0, result.returncode)
                    arguments = args_file.read_text().splitlines()
                    self.assertIn("sbom:/work/selected with spaces.cdx.json", arguments)
                    self.assertIn("/work:ro", " | ".join(arguments))


class OptionalReadOnlyAndLifecycleTests(unittest.TestCase):
    def test_default_and_optional_compose_keep_existing_isolation(self):
        compose = shutil.which("podman-compose")
        if not compose:
            self.skipTest("podman-compose unavailable for config-only validation")
        outputs = []
        for files in (("compose.yml",), ("compose.yml", "compose.read-only.yml")):
            command = [compose]
            for name in files:
                command += ["-f", name]
            result = subprocess.run(command + ["config"], cwd=ROOT,
                                    capture_output=True, text=True, timeout=15)
            self.assertEqual(0, result.returncode, result.stderr)
            outputs.append(result.stdout)
            for token in ("cap_drop:", "- ALL", "no-new-privileges:true",
                          "127.0.0.1:5100-5199:5100-5199", "codex_data:",
                          "claude_data:", "gemini_data:", "copilot_data:",
                          "opencode_data:", "dotnet_build:"):
                self.assertIn(token, result.stdout)
        self.assertNotIn("read_only: true", outputs[0])
        self.assertIn("read_only: true", outputs[1])
        self.assertIn("/tmp:rw,nosuid,nodev", outputs[1])
        self.assertIn("/home/adedev/.cache:rw,nosuid,nodev", outputs[1])
        self.assertIn("USER adedev", (ROOT / "Dockerfile").read_text())

    def test_lifecycle_entrypoints_reject_down_before_runtime_action(self):
        cases = [
            ("bash", ["bash", str(ROOT / "scripts/sandbox-lifecycle.sh"), "down"]),
            ("pwsh", ["pwsh", "-NoProfile", "-File",
                      str(ROOT / "scripts/sandbox-lifecycle.ps1"), "-Action", "down"]),
        ]
        for runner, command in cases:
            if not shutil.which(runner):
                continue
            with self.subTest(runner=runner):
                result = subprocess.run(command, cwd=ROOT, capture_output=True,
                                        text=True, timeout=10)
                self.assertNotEqual(0, result.returncode)
                self.assertTrue(
                    "build|up|recreate" in result.stdout + result.stderr
                    or "ValidateSet" in result.stdout + result.stderr
                    or "does not belong to the set" in result.stdout + result.stderr,
                    result.stdout + result.stderr,
                )


class Feature004CliSelectionTests(unittest.TestCase):
    def test_installed_assurance_semantic_mutation_matrix(self):
        matrix_path = (ROOT / "scripts/tests/fixtures/hardening-followup/"
                       "assurance-mutation-matrix.json")
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
        self.assertEqual("004-container-hardening-followup", matrix["feature"])
        manifest = ROOT / ".specify/presets" / matrix["installedPreset"] / "preset.yml"
        self.assertIn(f'version: "{matrix["installedVersion"]}"',
                      manifest.read_text(encoding="utf-8"))
        script = ROOT / matrix["matrixScript"]
        source = script.read_text(encoding="utf-8")
        for token in matrix["requiredMutationTokens"]:
            self.assertIn(token, source)
        if os.environ.get("ADE_RUN_ASSURANCE_MUTATION_MATRIX") != "1":
            self.skipTest("full installed Assurance matrix is opt-in; executed separately")
        for executable in ("pwsh", "bash", "jq"):
            if not shutil.which(executable):
                self.skipTest(f"{executable} unavailable")
        result = subprocess.run(
            ["pwsh", "-NoProfile", "-File", str(script)],
            cwd=ROOT, capture_output=True, text=True, timeout=300,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        for marker in matrix["expectedExecutionMarkers"]:
            self.assertIn(marker, result.stdout)

    def test_assurance_profile_matches_and_rejects_version_drift(self):
        self.assertEqual([], MODULE.validate_feature_004_assurance_profile(ROOT))
        with tempfile.TemporaryDirectory(prefix="ade004-presets-") as directory:
            fixture = Path(directory)
            registry = ROOT / "scripts/config/spec-kit-project-statistics-governance-presets.json"
            target = fixture / "scripts/config"
            target.mkdir(parents=True)
            shutil.copy2(registry, target / registry.name)
            data = json.loads(registry.read_text(encoding="utf-8"))
            for preset in data["presets"]:
                source = ROOT / ".specify/presets" / preset["id"] / "preset.yml"
                destination = fixture / ".specify/presets" / preset["id"]
                destination.mkdir(parents=True)
                shutil.copy2(source, destination / "preset.yml")
            manifest = fixture / ".specify/presets/secure-development-assurance-governance/preset.yml"
            manifest.write_text(manifest.read_text().replace('version: "0.1.8"',
                                                           'version: "0.1.7"'),
                                encoding="utf-8")
            errors = MODULE.validate_feature_004_assurance_profile(fixture)
            self.assertIn("installed preset manifest differs", " | ".join(errors))

    def test_both_wrappers_preview_feature_004_without_green(self):
        cases = [
            ("bash", ["bash", str(ROOT / "scripts/test-ade-sandbox-hardening.sh"),
                      "--mode", "All", "--feature-directory",
                      "specs/004-container-hardening-followup", "--dry-run"]),
            ("pwsh", ["pwsh", "-NoProfile", "-File",
                      str(ROOT / "scripts/test-ade-sandbox-hardening.ps1"),
                      "-Mode", "All", "-FeatureDirectory",
                      "specs/004-container-hardening-followup", "-WhatIf"]),
        ]
        for runner, command in cases:
            if not shutil.which(runner):
                continue
            with self.subTest(runner=runner):
                result = subprocess.run(command, cwd=ROOT, capture_output=True,
                                        text=True, timeout=10)
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                self.assertIn("no checks executed", result.stdout)
                self.assertNotIn("GREEN", result.stdout)

    def test_explicit_feature_004_does_not_fallback_to_historical_evidence(self):
        for directory in ("specs/004-container-hardening-followup",
                          "specs/does-not-exist"):
            cases = [
                ("bash", ["bash", str(ROOT / "scripts/test-ade-sandbox-hardening.sh"),
                          "--mode", "All", "--feature-directory", directory]),
                ("pwsh", ["pwsh", "-NoProfile", "-File",
                          str(ROOT / "scripts/test-ade-sandbox-hardening.ps1"),
                          "-Mode", "All", "-FeatureDirectory", directory]),
            ]
            for runner, command in cases:
                if not shutil.which(runner):
                    continue
                with self.subTest(runner=runner, directory=directory):
                    result = subprocess.run(command, cwd=ROOT, capture_output=True,
                                            text=True, timeout=10)
                    self.assertEqual(2, result.returncode, result.stdout + result.stderr)
                    self.assertNotIn("GREEN", result.stdout)


if __name__ == "__main__":
    unittest.main()
