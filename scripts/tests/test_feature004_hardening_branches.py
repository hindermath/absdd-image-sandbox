"""DE: Synthetische Evidenzzweige. EN: Synthetic evidence branch fixtures.

No approval, actual runtime, provider, installer or real process is exercised.
"""
import copy
from datetime import datetime, timezone
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


LIB = Path(__file__).resolve().parents[1] / "lib/secure_development_hardening.py"
SPEC = importlib.util.spec_from_file_location("hardening_branch_fixtures", LIB)
core = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(core)


class HardeningBranchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ade004-hardening-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name).resolve()
        self.enterContext(patch("sys.stdout", new_callable=io.StringIO))
        self.enterContext(patch("sys.stderr", new_callable=io.StringIO))
        self.spawn = self.enterContext(patch.object(core.subprocess, "run",
            side_effect=AssertionError("No real process allowed")))
        self.write("source.txt", "synthetic\r\n")
        self.requirements = {
            "schemaVersion": "1.0", "feature": core.FEATURE_004_ID, "gitHead": "fixture-head",
            "gateCount": 18, "quickstartCheckIds": [f"Q{n}" for n in range(1, 9)],
            "gates": [{"gateId": f"G004-{n:02d}", "quickstartChecks": ["Q1"]} for n in range(1, 19)],
            "sourceBindings": [{"path": "source.txt", "hashKind": "text/raw-and-utf8-lf",
                "rawSha256": core._sha256_raw(self.repo / "source.txt"),
                "normalizedSha256": core.normalized_sha256(self.repo / "source.txt")}],
            "executedEvidenceRequiredFields": ["evidenceId", "gateId", "gitHead", "commandArgv",
                "inputHashes", "payloadSha256", "decisionSha256", "runner", "observedAt", "exitCode"],
        }
        self.document = {
            "schemaVersion": "1.0", "feature": core.FEATURE_004_ID,
            "gateRequirementsSha256": "a" * 64, "gitHead": "fixture-head", "evidenceRecords": [],
            "checkpoints": [{"gateId": f"G004-{n:02d}", "applicability": "Open",
                "implementation": "Not Assessed", "evidenceIds": [],
                **{key: "synthetic" for key in ("reason", "owner", "reviewer", "residualRisk",
                    "nextAction", "dueAt", "reevaluationTrigger")}} for n in range(1, 19)],
        }

    def write(self, relative, value):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value if isinstance(value, str) else json.dumps(value), encoding="utf-8")
        return path

    def validate(self, document=None, requirements=None):
        return core.validate_feature_004_evidence(
            self.document if document is None else document,
            self.requirements if requirements is None else requirements, self.repo, "a" * 64)

    def record(self):
        return {"evidenceId": "synthetic-E1", "gateId": "G004-01", "gitHead": "fixture-head",
            "outcome": "Passed", "commandArgv": ["synthetic-only"], "inputHashes": {},
            "payloadSha256": "b" * 64, "decisionSha256": "c" * 64, "runner": "synthetic",
            "observedAt": "2026-11-02T00:00:00Z", "exitCode": 0}

    def test_paths_normalization_timestamps_and_duplicate_helpers(self):
        for value in (None, "", "../escape", "/outside", "C:\\outside"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                core.safe_repo_path(self.repo, value)
        (self.repo / "outside").symlink_to(self.repo.parent)
        with self.assertRaises(ValueError):
            core.safe_repo_path(self.repo, "outside/escape")
        self.write("nul.txt", "\x00")
        with self.assertRaises(ValueError):
            core.normalized_bytes(self.repo / "nul.txt")
        with self.assertRaises(ValueError):
            core.load_json(self.write("not-object.json", []))
        for value in (None, "badZ", "2026-11-02T00:00:00"):
            errors = []
            self.assertIsNone(core.parse_utc(value, "fixture", errors))
            self.assertTrue(errors)
        self.assertEqual(core.duplicates(["a", "b", "a"]), ["a"])

    def test_feature_requirements_mutations_are_rejected(self):
        mutations = [("schemaVersion", "invalid"), ("feature", "other"), ("gateCount", 17),
            ("gates", None), ("gates", [None] * 18),
            ("gates", [{"gateId": 1}] * 18), ("quickstartCheckIds", None),
            ("quickstartCheckIds", [1]), ("sourceBindings", None),
            ("sourceBindings", [None]), ("sourceBindings", [{"path": None}]),
            ("sourceBindings", self.requirements["sourceBindings"] * 2)]
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                requirements = copy.deepcopy(self.requirements)
                requirements[key] = value
                self.assertTrue(self.validate(requirements=requirements))
        for changes in ({"hashKind": "wrong"}, {"normalizedSha256": "0" * 64},
                        {"path": "missing"}):
            requirements = copy.deepcopy(self.requirements)
            requirements["sourceBindings"][0].update(changes)
            self.assertTrue(self.validate(requirements=requirements))

    def test_records_reject_malformed_ids_outcomes_and_execution_fields(self):
        for records in (None, [None], [{}], [self.record(), self.record()]):
            candidate = copy.deepcopy(self.document)
            candidate["evidenceRecords"] = records
            self.assertTrue(self.validate(candidate))
        changes = [{"gateId": "unknown"}, {"gitHead": "other"}, {"outcome": "invented"},
            {"exitCode": True}, {"exitCode": "0"}, {"commandArgv": []},
            {"commandArgv": [None]}, {"inputHashes": []}, {"runner": ""},
            {"payloadSha256": "bad"}, {"decisionSha256": "bad"}, {"observedAt": "badZ"}]
        for mutation in changes:
            with self.subTest(mutation=mutation):
                candidate = copy.deepcopy(self.document)
                candidate["evidenceRecords"] = [{**self.record(), **mutation}]
                self.assertTrue(self.validate(candidate))
        candidate = copy.deepcopy(self.document)
        candidate["evidenceRecords"] = [{"evidenceId": "notrun", "gateId": "G004-01",
            "gitHead": "fixture-head", "outcome": "NotRun"}]
        self.assertIn("missing owner", " | ".join(self.validate(candidate)))

    def test_record_hash_records_verify_raw_normalized_kind_and_containment(self):
        for kind, digest, errors in (("rawSha256", core._sha256_raw(self.repo / "source.txt"), False),
                ("normalizedSha256", core.normalized_sha256(self.repo / "source.txt"), False),
                ("rawSha256", "0" * 64, True), ("unknown", "0" * 64, True)):
            candidate = copy.deepcopy(self.document)
            record = self.record()
            record["inputHashes"] = {"source.txt": {"kind": kind, "digest": digest}}
            candidate["evidenceRecords"] = [record]
            self.assertEqual(bool(self.validate(candidate)), errors)
        for value in (None, {"kind": "rawSha256", "digest": "0" * 64}):
            candidate = copy.deepcopy(self.document)
            record = self.record()
            record["inputHashes"] = {"../outside": value}
            candidate["evidenceRecords"] = [record]
            self.assertTrue(self.validate(candidate))

    def test_checkpoints_invalid_sets_references_and_authority(self):
        for checkpoints in (None, [None], [self.document["checkpoints"][0]] * 18):
            candidate = copy.deepcopy(self.document)
            candidate["checkpoints"] = checkpoints
            self.assertTrue(self.validate(candidate))
        for changes in ({"applicability": "unknown"}, {"implementation": "unknown"},
                {"evidenceIds": None}, {"evidenceIds": [None]}, {"evidenceIds": ["missing"]},
                {"evidenceIds": ["x", "x"]}, {"owner": ""},
                {"applicability": "Applicable", "implementation": "Fulfilled"}):
            candidate = copy.deepcopy(self.document)
            candidate["checkpoints"][0].update(changes)
            self.assertTrue(self.validate(candidate))
        for authority, expect_error in ((None, True), ("missing", True), ("authority.txt", False)):
            self.write("authority.txt", "Synthetic authority fixture, not a real decision")
            candidate = copy.deepcopy(self.document)
            record = {**self.record(), "gateId": "G004-09"}
            candidate["evidenceRecords"] = [record]
            candidate["checkpoints"][8].update(applicability="Applicable", implementation="Fulfilled",
                evidenceIds=[record["evidenceId"]], authorityEvidence=authority)
            self.assertEqual(bool(self.validate(candidate)), expect_error)
        self.assertEqual(self.validate(), [])

    def profile(self):
        entries = [{"id": f"synthetic-{n}", "version": "v1.0.0", "priority": n} for n in range(13)]
        entries.append({"id": "secure-development-assurance-governance", "version": "v0.1.8", "priority": 15})
        for entry in entries:
            self.write(f".specify/presets/{entry['id']}/preset.yml",
                f"preset:\n  id: \"{entry['id']}\"\n  version: \"{entry['version'][1:]}\"\n")
        path = "scripts/config/spec-kit-project-statistics-governance-presets.json"
        self.write(path, {"presets": entries})
        return path, entries

    def test_profile_manifest_registry_semantics_and_exact_installed_set(self):
        path, entries = self.profile()
        self.assertEqual(core.validate_feature_004_assurance_profile(self.repo), [])
        for values in ([], [None] * 14, entries[:13] + [entries[0]],
                [{**e, "version": "invalid"} for e in entries],
                [{**e, "priority": True} for e in entries]):
            self.write(path, {"presets": values})
            self.assertTrue(core.validate_feature_004_assurance_profile(self.repo))
        self.write(path, {"presets": [{**e, "version": "v0.0.1"} if e["priority"] == 15 else e
                                     for e in entries]})
        self.assertTrue(core.validate_feature_004_assurance_profile(self.repo))
        self.write(path, {"presets": entries})
        self.write(".specify/presets/synthetic-0/preset.yml", "wrong manifest")
        (self.repo / ".specify/presets/unexpected").mkdir()
        errors = " | ".join(core.validate_feature_004_assurance_profile(self.repo))
        self.assertIn("manifest differs", errors)
        self.assertIn("directory set", errors)

    def test_feature_execution_explicit_context_and_status_dispatch(self):
        feature = f"specs/{core.FEATURE_004_ID}"
        self.write(f"{feature}/gate-requirements.json", self.requirements)
        for value in (".", "source.txt"):
            with self.assertRaises(ValueError):
                core.execute_feature_004_mode(self.repo, "Input", None, True, value)
        self.assertEqual(core.execute_feature_004_mode(self.repo, "Input", None, True, feature), 0)
        with patch.object(core, "validate_feature_004_assurance_profile", return_value=["synthetic missing"]):
            self.assertEqual(core.execute_feature_004_mode(self.repo, "Input", None, False, feature), 1)
        self.profile()
        with self.assertRaises(ValueError):
            core.execute_feature_004_mode(self.repo, "Input", None, False, feature)
        document = copy.deepcopy(self.document)
        requirements_path = self.repo / feature / "gate-requirements.json"
        document["gateRequirementsSha256"] = core._sha256_raw(requirements_path)
        for applicability, implementation, expected in (("Open", "Not Assessed", 3),
                ("Applicable", "Not Fulfilled", 1), ("N/A", "Not Assessed", 0)):
            document["checkpoints"][0].update(applicability=applicability, implementation=implementation)
            for cp in document["checkpoints"][1:]:
                cp.update(applicability="N/A", implementation="Not Assessed")
            self.write("evidence.json", document)
            self.assertEqual(core.execute_feature_004_mode(self.repo, "Input", "evidence.json", False, feature), expected)
        self.write("evidence.json", {})
        self.assertEqual(core.execute_feature_004_mode(self.repo, "Input", "evidence.json", False, feature), 1)

    def test_legacy_evidence_rejects_root_gate_record_and_execution_mutations(self):
        gate = {"gateId": "synthetic-gate", "applicability": "Applicable",
            "requiredCommandTokens": ["check"], "requiredRunnerOrPlatformTokens": ["fixture"]}
        record = {key: "synthetic" for key in core.EXPECTED_EVIDENCE_FIELDS}
        record.update(evidenceId="synthetic", gateId=gate["gateId"], applicability="Applicable",
            command="check", runnerOrPlatform="fixture", subjectPaths=["source.txt", "N/A", "local-image:fixture"],
            startedAt="2026-11-02T00:00:00Z", finishedAt="2026-11-02T00:00:01Z", exitCode=0,
            result="Pass", freshness="Current", artifactSha256="a" * 64, containsSensitiveContent=False)
        baseline = {"schemaVersion": "1.0", "sourceRevision": "WORKTREE", "imageIdentity": "synthetic",
                    "gateResults": [record], "overallResult": "Pass"}
        self.assertEqual(core.validate_evidence_document(baseline, {"gates": [gate]}, self.repo), [])
        for key, value in (("schemaVersion", "bad"), ("sourceRevision", None), ("imageIdentity", ""),
                ("overallResult", "bad"), ("gateResults", []), ("gateResults", [None]),
                ("gateResults", [record, record])):
            candidate = {**baseline, key: value}
            self.assertTrue(core.validate_evidence_document(candidate, {"gates": [gate]}, self.repo))
        mutations = [{"gateId": "unknown"}, {"subjectPaths": []}, {"subjectPaths": [None, "../outside"]},
            {"finishedAt": "2026-11-01T00:00:00Z"}, {"expectedResult": ""}, {"containsSensitiveContent": True},
            {"command": ""}, {"runnerOrPlatform": ""}, {"exitCode": -1}, {"result": "bad"},
            {"freshness": "bad"}, {"artifactSha256": "bad"}, {"exitCode": 1}, {"freshness": "Stale"}]
        for mutation in mutations:
            candidate = {**baseline, "gateResults": [{**record, **mutation}]}
            self.assertTrue(core.validate_evidence_document(candidate, {"gates": [gate]}, self.repo))
        self.assertTrue(core.validate_evidence_document({}, {"gates": None}, self.repo, require_all_gates=True))
        na_gate = {**gate, "applicability": "N/A", "rationale": "not applicable", "reevaluationTrigger": "change"}
        self.assertTrue(core.validate_evidence_document(baseline, {"gates": [na_gate]}, self.repo))
        na = {**record, "applicability": "N/A", "command": "N/A", "runnerOrPlatform": "N/A",
            "exitCode": None, "result": "N/A", "freshness": "N/A", "artifactSha256": "N/A",
            "rationale": "not applicable", "reevaluationTrigger": "change"}
        self.assertEqual(core.validate_evidence_document({**baseline, "gateResults": [na]},
                         {"gates": [na_gate]}, self.repo), [])
        na["exitCode"] = 0
        na["rationale"] = "wrong"
        na["reevaluationTrigger"] = "wrong"
        self.assertTrue(core.validate_evidence_document({**baseline, "gateResults": [na]},
                        {"gates": [na_gate]}, self.repo))

    def test_learner_and_feasibility_fixtures_never_supply_real_approval(self):
        self.assertTrue(core.validate_feasibility_study_decision(self.repo))
        path = core.FEASIBILITY_DECISION_PATH
        self.write(path, "invalid json")
        self.assertTrue(core.validate_feasibility_study_decision(self.repo))
        self.assertTrue(core.validate_feasibility_study_decision_document({},
            today=datetime(2099, 1, 1, tzinfo=timezone.utc)))
        self.assertTrue(core.validate_learner_result(self.repo))
        learner = "docs/security/secure-development/2026-08-30-container-hardening/learner-first-use-results.json"
        self.write(learner, "invalid json")
        self.assertTrue(core.validate_learner_result(self.repo))
        self.write(learner, {})
        errors = " | ".join(core.validate_learner_result(self.repo))
        for fragment in ("owner", "prior Spec Kit", "timeLimitMinutes", "successRatePercent",
                         "all four", "containsSensitiveContent"):
            self.assertIn(fragment, errors)

    def test_legacy_mode_process_results_are_intercepted(self):
        self.write("docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json", {})
        self.write(core.GATE_REQUIREMENTS_PATH, {"gates": [{"gateId": "GATE-LEARNER-01", "applicability": "N/A"}]})
        with patch.object(core, "validate_gap_document", return_value=[]), \
                patch.object(core, "command_plan", return_value=[["synthetic", "literal arg"]]):
            with patch.object(core.shutil, "which", return_value=None):
                self.assertEqual(core.execute_mode(self.repo, "Input", None, False), 3)
            with patch.object(core.shutil, "which", return_value="synthetic"):
                self.spawn.side_effect = None
                self.spawn.return_value = subprocess.CompletedProcess([], 2)
                self.assertEqual(core.execute_mode(self.repo, "Input", None, False), 1)
                self.spawn.return_value = subprocess.CompletedProcess([], 0)
                self.assertEqual(core.execute_mode(self.repo, "Input", None, False), 0)
            self.spawn.reset_mock()
            self.assertEqual(core.execute_mode(self.repo, "Input", None, True), 0)
            self.spawn.assert_not_called()
            for mode in ("SupplyChain", "Documentation", "Accessibility"):
                self.assertNotEqual(core.execute_mode(self.repo, mode, None, False), 0)
        with patch.object(core, "validate_gap_document", return_value=["synthetic invalid"]):
            self.assertEqual(core.execute_mode(self.repo, "Input", None, True), 1)

    def test_cli_hash_and_usage_failure_without_spawning(self):
        self.assertEqual(core.main(["hash", "--repo", str(self.repo), "--path", "source.txt"]), 0)
        self.assertEqual(core.main(["hash", "--repo", str(self.repo), "--path", "missing"]), 2)
        self.assertEqual(core.main(["hash", "--repo", str(self.repo / "missing"), "--path", "x"]), 2)
        self.spawn.assert_not_called()


if __name__ == "__main__":
    unittest.main()
