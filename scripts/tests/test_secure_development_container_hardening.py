#!/usr/bin/env python3
"""Contract tests for secure-development container hardening evidence."""

from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[2]
LIBRARY_PATH = REPOSITORY / "scripts/lib/secure_development_hardening.py"
GAPS_PATH = REPOSITORY / "docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json"
GATE_PATH = REPOSITORY / "specs/003-secure-development-container-hardening/autonomous-run-gate-requirements.json"
FIXTURE_DIR = REPOSITORY / "scripts/tests/fixtures/secure-development-container-hardening"
CHANGED_PATH_MAPPING = REPOSITORY / "docs/security/secure-development/2026-08-30-container-hardening/changed-path-mapping.json"
ASSESSMENT_PATH_FOR_TESTS = "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json"

EXPECTED_HUMAN_ROLES = {
    "Privacy/Legal Review": {
        "GAP-011", "GAP-012", "GAP-070", *{f"GAP-{value:03d}" for value in range(75, 87)},
        "GAP-105", "GAP-106", "GAP-115", *{f"GAP-{value:03d}" for value in range(134, 146)},
    },
    "Platform Owner/Admin": {
        "GAP-034", "GAP-035", "GAP-120", "GAP-121", "GAP-124",
        *{f"GAP-{value:03d}" for value in range(128, 132)}, "GAP-155",
    },
    "CISO/ISB/KIB": {
        "GAP-100", "GAP-101", "GAP-102", "GAP-109", "GAP-110", "GAP-146", "GAP-150", "GAP-152",
    },
    "Project Owner": {"GAP-113"},
}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def normalized_tree_snapshot(repo: Path) -> tuple[str, str]:
    """Snapshot repository status and the canonical gap artefact only."""
    status = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=repo,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    canonical = (repo / "docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json").read_text(encoding="utf-8")
    return status, canonical


def load_library():
    spec = importlib.util.spec_from_file_location("secure_development_hardening", LIBRARY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {LIBRARY_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class GapContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = load_library()
        cls.canonical = load_json(GAPS_PATH)

    def assert_rejected(self, document: dict, expected_fragment: str) -> None:
        errors = self.library.validate_gap_document(document, REPOSITORY)
        self.assertTrue(errors, "invalid document was unexpectedly accepted")
        self.assertTrue(
            any(expected_fragment in error for error in errors),
            f"expected {expected_fragment!r} in {errors!r}",
        )

    def test_canonical_initial_register_is_valid(self) -> None:
        self.assertEqual(self.library.validate_gap_document(self.canonical, REPOSITORY), [])

    def test_mutation_fixtures_are_all_declared(self) -> None:
        fixture_names = {
            path.stem for path in FIXTURE_DIR.glob("*.json") if path.name != "gap-147-missing-mount-evidence.json"
        }
        self.assertEqual(
            fixture_names,
            {
                "duplicate-gap-id",
                "extra-gap-id",
                "invalid-input-role",
                "invalid-status-combination",
                "missing-gap-id",
                "missing-trigger",
                "nonreciprocal-cl-reference",
                "stale-evidence",
                "unexpected-field",
                "wrong-accepted-hash",
                "wrong-human-only",
                "wrong-human-only-role",
                "contradictory-na-runtime-data",
                "nonreciprocal-evidence-reference",
            },
        )

    def test_missing_gap_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        document["dispositions"].pop(20)
        self.assert_rejected(document, "exactly 157")

    def test_duplicate_gap_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        document["dispositions"][-1] = deepcopy(document["dispositions"][-2])
        self.assert_rejected(document, "duplicate gap IDs")

    def test_extra_gap_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        extra = deepcopy(document["dispositions"][-1])
        extra["gapId"] = "GAP-158"
        document["dispositions"].append(extra)
        self.assert_rejected(document, "exactly 157")

    def test_wrong_human_only_flag_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        document["dispositions"][0]["humanOnly"] = True
        document["dispositions"][0]["humanOnlyRole"] = "CISO/ISB/KIB"
        self.assert_rejected(document, "baseline projection")

    def test_wrong_human_only_role_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        target = next(item for item in document["dispositions"] if item["gapId"] == "GAP-011")
        target["humanOnlyRole"] = "Project Owner"
        target["owner"] = "Project Owner"
        self.assert_rejected(document, "baseline projection")

    def test_invalid_input_binding_role_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        document["acceptedInputBindings"][0]["role"] = "AssessmentResults"
        self.assert_rejected(document, "binding roles")

    def test_invalid_status_combination_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        target = document["dispositions"][0]
        target["applicability"] = "Applicable"
        target["implementationStatus"] = "Fulfilled"
        target["consolidatedState"] = "Open"
        self.assert_rejected(document, "status combination")

    def test_missing_trigger_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        document["dispositions"][0]["reevaluationTrigger"] = ""
        self.assert_rejected(document, "reevaluationTrigger")

    def test_unexpected_field_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        document["dispositions"][0]["approval"] = "invented"
        self.assert_rejected(document, "unexpected fields")

    def test_wrong_accepted_hash_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        document["acceptedInputBindings"][0]["sha256"] = "0" * 64
        self.assert_rejected(document, "hash mismatch")

    def test_nonreciprocal_cl_reference_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        document["dispositions"][0]["affectedClIds"] = ["CL-01-02"]
        self.assert_rejected(document, "baseline projection")

    def test_nonreciprocal_evidence_reference_is_rejected(self) -> None:
        document = deepcopy(self.canonical)
        document["dispositions"][0]["evidenceIds"] = ["EVD-NOT-DECLARED"]
        errors = self.library.validate_gap_document(
            document,
            REPOSITORY,
            known_evidence_ids={"EVD-OTHER"},
        )
        self.assertTrue(any("unknown evidence" in error for error in errors), errors)

    def test_exact_human_only_role_lists_and_range_sums(self) -> None:
        actual: dict[str, set[str]] = {role: set() for role in EXPECTED_HUMAN_ROLES}
        for item in self.canonical["dispositions"]:
            if item["humanOnly"]:
                actual[item["humanOnlyRole"]].add(item["gapId"])
        self.assertEqual(actual, EXPECTED_HUMAN_ROLES)
        self.assertEqual(sum(len(values) for values in actual.values()), 49)
        expected_ranges = [12, 13, 15, 10, 13, 11, 12, 13, 17, 17, 12, 12]
        actual_ranges = []
        starts = [1, 13, 26, 41, 51, 64, 75, 87, 100, 117, 134, 146]
        ends = [12, 25, 40, 50, 63, 74, 86, 99, 116, 133, 145, 157]
        for start, end in zip(starts, ends, strict=True):
            actual_ranges.append(sum(1 for item in self.canonical["dispositions"] if start <= int(item["gapId"][-3:]) <= end))
        self.assertEqual(actual_ranges, expected_ranges)

    def test_cl_projection_and_evidence_ids_are_reciprocal_and_unique(self) -> None:
        baseline = load_json(REPOSITORY / ASSESSMENT_PATH_FOR_TESTS)
        expected = {item["gapId"]: item["affectedClIds"] for item in baseline["gaps"]}
        actual = {item["gapId"]: item["affectedClIds"] for item in self.canonical["dispositions"]}
        self.assertEqual(actual, expected)
        evidence = load_json(REPOSITORY / "docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json")
        evidence_ids = [item["evidenceId"] for item in evidence["gateResults"]]
        self.assertEqual(len(evidence_ids), len(set(evidence_ids)))
        known = set(evidence_ids)
        referenced = {value for item in self.canonical["dispositions"] for value in item["evidenceIds"]}
        self.assertEqual(referenced - known, set())

    def test_changed_path_mapping_is_unique_and_traceable(self) -> None:
        mapping = load_json(CHANGED_PATH_MAPPING)
        self.assertEqual(mapping["schemaVersion"], "1.0")
        paths = [item["path"] for item in mapping["mappings"]]
        self.assertEqual(len(paths), len(set(paths)))
        self.assertTrue(paths)
        for item in mapping["mappings"]:
            self.assertTrue(item["gapIds"] or item["requirementIds"])
            self.assertTrue(item["requirementIds"])
            self.assertTrue(item["reason"].strip())


class EvidenceContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = load_library()
        cls.requirements = load_json(GATE_PATH)

    def na_record(self) -> dict:
        gate = next(item for item in self.requirements["gates"] if item["gateId"] == "GATE-ASVS-NA-01")
        return {
            "schemaVersion": "1.0",
            "sourceRevision": "WORKTREE",
            "imageIdentity": "N/A",
            "gateResults": [
                {
                    "evidenceId": "EVD-ASVS-NA-001",
                    "gateId": gate["gateId"],
                    "applicability": "N/A",
                    "subjectPaths": ["specs/003-secure-development-container-hardening/spec.md"],
                    "command": "N/A",
                    "runnerOrPlatform": "N/A",
                    "startedAt": "2026-08-30T13:12:00Z",
                    "finishedAt": "2026-08-30T13:12:00Z",
                    "exitCode": None,
                    "expectedResult": "A reasoned applicability decision with no invented execution.",
                    "observedResult": gate["rationale"],
                    "result": "N/A",
                    "freshness": "N/A",
                    "limitations": "Re-evaluate when the declared trigger occurs.",
                    "artifactSha256": "N/A",
                    "containsSensitiveContent": False,
                    "rationale": gate["rationale"],
                    "reevaluationTrigger": gate["reevaluationTrigger"],
                }
            ],
            "overallResult": "Blocked",
        }

    def test_reasoned_na_without_execution_is_valid(self) -> None:
        self.assertEqual(
            self.library.validate_evidence_document(self.na_record(), self.requirements, REPOSITORY),
            [],
        )

    def test_na_with_runtime_data_is_rejected(self) -> None:
        document = self.na_record()
        record = document["gateResults"][0]
        record["command"] = "a command that was not run"
        record["runnerOrPlatform"] = "invented runner"
        record["exitCode"] = 0
        record["result"] = "Pass"
        record["freshness"] = "Current"
        errors = self.library.validate_evidence_document(document, self.requirements, REPOSITORY)
        self.assertTrue(any("N/A execution fields" in error for error in errors), errors)

    def test_stale_evidence_cannot_pass(self) -> None:
        document = self.na_record()
        record = document["gateResults"][0]
        record.update(
            {
                "gateId": "GATE-GAP-01",
                "applicability": "Applicable",
                "command": "bash scripts/test-ade-sandbox-hardening.sh --mode input --evidence docs/security/secure-development/2026-08-30-container-hardening/verification-evidence.json",
                "runnerOrPlatform": "repository-local",
                "exitCode": 0,
                "result": "Pass",
                "freshness": "Stale",
                "artifactSha256": "0" * 64,
            }
        )
        errors = self.library.validate_evidence_document(document, self.requirements, REPOSITORY)
        self.assertTrue(any("stale evidence cannot pass" in error for error in errors), errors)


class CommandLineContractTests(unittest.TestCase):
    def run_entry(self, kind: str, *arguments: str) -> subprocess.CompletedProcess[str]:
        if kind == "bash":
            command = ["bash", str(REPOSITORY / "scripts/test-ade-sandbox-hardening.sh")]
        else:
            command = [
                "pwsh",
                "-NoLogo",
                "-NoProfile",
                "-File",
                str(REPOSITORY / "scripts/test-ade-sandbox-hardening.ps1"),
            ]
        return subprocess.run(
            [*command, *arguments],
            cwd=REPOSITORY,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_help_and_mode_contract_are_documented(self) -> None:
        bash_help = self.run_entry("bash", "--help")
        powershell_source = (REPOSITORY / "scripts/test-ade-sandbox-hardening.ps1").read_text(encoding="utf-8")
        man_page = (REPOSITORY / "docs/man/test-ade-sandbox-hardening.1").read_text(encoding="utf-8")
        self.assertEqual(bash_help.returncode, 0, bash_help.stderr)
        for mode in ("Input", "Static", "Runtime", "SupplyChain", "Documentation", "Accessibility", "All"):
            self.assertIn(mode, bash_help.stdout)
            self.assertIn(mode, powershell_source)
            self.assertIn(mode, man_page)
        self.assertIn("Test-AdeSandboxHardening", powershell_source)
        self.assertIn("Set-StrictMode -Version Latest", powershell_source)

    def test_bash_dry_run_and_powershell_whatif_are_write_free_and_equivalent(self) -> None:
        before = normalized_tree_snapshot(REPOSITORY)
        bash_result = self.run_entry("bash", "--mode", "Static", "--dry-run")
        if not shutil.which("pwsh"):
            self.skipTest("PowerShell 7 is unavailable")
        powershell_result = self.run_entry("powershell", "-Mode", "Static", "-WhatIf")
        after = normalized_tree_snapshot(REPOSITORY)
        self.assertEqual(bash_result.returncode, 0, bash_result.stderr)
        self.assertEqual(powershell_result.returncode, 0, powershell_result.stderr)
        self.assertEqual(before, after)
        for token in ("unittest", "check-dockerfile-arg-renovate.py", "git diff --check"):
            self.assertIn(token, bash_result.stdout)
            self.assertIn(token, powershell_result.stdout)

    def test_usage_errors_preserve_exit_two(self) -> None:
        self.assertEqual(self.run_entry("bash", "--mode", "Unknown").returncode, 2)
        if shutil.which("pwsh"):
            self.assertNotEqual(self.run_entry("powershell", "-Mode", "Unknown").returncode, 0)

    def test_cli_rejects_invalid_document_with_exit_one(self) -> None:
        document = load_json(GAPS_PATH)
        document["dispositions"].pop()
        # The CLI intentionally rejects paths outside the repository.  Keep
        # this short-lived fixture inside the boundary and remove it on exit.
        with tempfile.TemporaryDirectory(dir=REPOSITORY) as temporary:
            path = Path(temporary) / "invalid.json"
            path.write_text(json.dumps(document), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(LIBRARY_PATH),
                    "validate-gaps",
                    "--repo",
                    str(REPOSITORY),
                    "--gaps",
                    path.relative_to(REPOSITORY).as_posix(),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
