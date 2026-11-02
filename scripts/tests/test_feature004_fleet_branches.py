"""Synthetic fleet contracts; no fleet run, provider calls or Git writes.

DE: Reine Vertrags-/Transport-Fixtures. EN: Contract and intercepted transport tests.
"""
import copy
import importlib.util
import io
import json
from pathlib import Path, PurePosixPath
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("fleet_branch_fixtures",
    Path(__file__).resolve().parents[1] / "lib/agentic_workspace_fleet.py")
fleet = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fleet)
RUN = "11111111-1111-4111-8111-111111111111"
HASH = "a" * 64
HEAD = "b" * 40
# Keep the inert redaction sample recognizable without a credential assignment.
SYNTHETIC_REDACTION_SAMPLE = "=".join(("password", "x"))


class FleetBranchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ade004-fleet-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.spawn = self.enterContext(patch.object(fleet.subprocess, "run",
            side_effect=AssertionError("External fleet process forbidden")))
        self.enterContext(patch("sys.stdout", new_callable=io.StringIO))
        self.enterContext(patch("sys.stderr", new_callable=io.StringIO))

    def test_git_transports_preserve_argv_and_fail_without_host_fallback(self):
        self.spawn.side_effect = None
        self.spawn.return_value = subprocess.CompletedProcess([], 0, "ok", "")
        fleet.run_git(self.root, "status", "--", "space arg")
        self.assertEqual(self.spawn.call_args.args[0], ["git", "-C", str(self.root), "status", "--", "space arg"])
        fleet.run_git(None, "--version")
        self.assertEqual(self.spawn.call_args.args[0], ["git", "--version"])
        for message in ("synthetic error", ""):
            self.spawn.return_value = subprocess.CompletedProcess([], 2, "", message)
            with self.assertRaises(RuntimeError):
                fleet.run_git(self.root, "status")
            self.assertEqual(fleet.run_git(self.root, "status", check=False).returncode, 2)
        router = SimpleNamespace(mapping=lambda path: True,
            git=lambda path, args: subprocess.CompletedProcess([], 1, "", "synthetic"))
        with patch.object(fleet, "EXECUTION_CONTEXTS", router), self.assertRaises(fleet.ContractError):
            fleet.run_git(self.root, "status")

    def test_transaction_identity_is_scoped_and_invalid_values_rejected(self):
        for name, email in (("", "fixture@example.invalid"), ("bad\nname", "fixture@example.invalid"),
                            ("fixture", "invalid")):
            with self.assertRaises(fleet.ContractError):
                fleet.run_git_transaction(self.root, "status", author_name=name, author_email=email)
        self.spawn.assert_not_called()
        self.spawn.side_effect = None
        self.spawn.return_value = subprocess.CompletedProcess([], 0, "", "")
        fleet.run_git_transaction(self.root, "status", author_name="fixture", author_email="fixture@example.invalid")
        self.assertIn("user.name=fixture", self.spawn.call_args.args[0])
        for message in ("failed", ""):
            self.spawn.return_value = subprocess.CompletedProcess([], 1, "", message)
            with self.assertRaises(RuntimeError):
                fleet.run_git_transaction(self.root, "status", author_name="fixture", author_email="fixture@example.invalid")

    def test_network_retry_is_mocked_and_auth_failure_is_not_retried(self):
        for detail, transient in (("connection reset", True), ("HTTP 503", True),
                                  ("authentication failed", False), ("dirty worktree", False), ("other", False)):
            self.assertEqual(fleet.is_transient_git_failure(detail), transient)
        self.spawn.side_effect = [subprocess.TimeoutExpired(["fake"], 300),
            subprocess.CompletedProcess([], 0, "ok", "")]
        with patch.object(fleet.time, "sleep") as sleep, patch.object(fleet.random, "uniform", return_value=0):
            result, attempts, _ = fleet.run_git_network(self.root, "fetch", "origin")
        self.assertEqual((result.returncode, attempts), (0, 2))
        self.assertEqual(self.spawn.call_args.kwargs["timeout"], 300)
        sleep.assert_called_once()
        self.spawn.side_effect = None
        self.spawn.return_value = subprocess.CompletedProcess([], 1, "", "permission denied")
        self.assertEqual(fleet.run_git_network(None, "fetch")[1], 1)
        evidence = fleet.network_attempt("fetch", subprocess.CompletedProcess([], 1, "", SYNTHETIC_REDACTION_SAMPLE), 1, 1)
        self.assertNotIn(SYNTHETIC_REDACTION_SAMPLE, evidence["sanitizedEvidence"])
        self.assertEqual(fleet.network_attempt("fetch", subprocess.CompletedProcess([], 124, "", ""), 1, 1)["status"], "TimedOut")
        self.assertEqual(fleet.network_attempt("fetch", subprocess.CompletedProcess([], 0, "", ""), 1, 1)["status"], "Succeeded")

    def test_path_remote_and_exact_closed_world_contracts(self):
        for value in (None, "", "/outside", "../outside", "bad\\path"):
            with self.assertRaises(fleet.ContractError):
                fleet.validate_relative_path(value)
        self.assertEqual(fleet.normalize_remote("HTTPS://EXAMPLE.INVALID/Repo.git"), "https://example.invalid/repo")
        with self.assertRaises(fleet.ContractError):
            fleet.normalize_remote("https://fixture:x@example.invalid/repo")
        for value in (None, "", "--flag", "../escape", "bad\nline", "Upper"):
            with self.assertRaises(fleet.ContractError):
                fleet.validate_ci_input_component(value)
        self.assertEqual(fleet.validate_ci_input_component("fixture-repo"), "fixture-repo")
        for value in (None, {}, {"unexpected": True}):
            with self.assertRaises(fleet.ContractError):
                fleet.validate_stage_b_closed_world(value, {"required"}, "fixture")
        fleet.validate_stage_b_document_set(fleet.STAGE_B_SCHEMA_VERSIONS)
        with self.assertRaises(fleet.ContractError):
            fleet.validate_stage_b_document_set({key: "wrong" for key in fleet.STAGE_B_SCHEMA_VERSIONS})
        for value in (None, {"status": "Delivering"}):
            with self.assertRaises(fleet.ContractError):
                fleet.validate_stage_b_plan_state_separation(value)
        fleet.validate_stage_b_plan_state_separation({"immutable": True})

    def test_schema_reference_and_branch_type_validation(self):
        schema = {"$defs": {"name": {"type": "string", "minLength": 1}}, "$ref": "#/$defs/name"}
        fleet.validate_stage_b_schema_instance("ok", schema)
        for reference in ("https://example.invalid/schema", "#/missing", "#/$defs/value"):
            with self.assertRaises(fleet.ContractError):
                fleet.validate_stage_b_schema_instance("x", {"$defs": {"value": 1}, "$ref": reference})
        fleet.validate_stage_b_schema_instance(1, {"oneOf": [{"type": "integer"}, {"type": "string"}]})
        for value in (None, True):
            with self.assertRaises(fleet.ContractError):
                fleet.validate_stage_b_schema_instance(value, {"oneOf": [{"type": "integer"}, {"type": "string"}]})
        for value, schema in ((1, {"const": 2}), (1, {"enum": [2]}),
                ({}, {"required": ["name"]}), ({"unknown": 1}, {"additionalProperties": False}),
                ([], {"type": "array", "minItems": 1}), ([1, 1], {"uniqueItems": True}),
                ([1, 2], {"maxItems": 1}), ("", {"minLength": 1}),
                ("too long", {"maxLength": 2}), ("bad", {"pattern": "[0-9]+"}),
                ("bad", {"format": "uuid"}), ("00000000-0000-0000-0000-000000000000", {"format": "uuid"}),
                ("bad", {"format": "date-time"})):
            with self.subTest(schema=schema), self.assertRaises(fleet.ContractError):
                fleet.validate_stage_b_schema_instance(value, schema)
        for value, schema in (({"name": "ok"}, {"properties": {"name": {"type": "string"}}}),
                ([1], {"items": {"type": "integer"}}), (RUN, {"format": "uuid"}),
                ("2026-11-02T00:00:00Z", {"format": "date-time"}), (True, {"type": "boolean"}),
                (1.5, {"type": "number"}), (None, {"type": "null"})):
            fleet.validate_stage_b_schema_instance(value, schema)

    def test_schema_bindings_require_exact_raw_bytes_and_source_presence(self):
        first, second = self.root / "first", self.root / "second"
        first.write_text("fixture\n")
        second.write_text("fixture\n")
        fleet.require_stage_b_schema_match(first, second)
        second.write_bytes(b"fixture\r\n")
        with self.assertRaises(fleet.ContractError):
            fleet.require_stage_b_schema_match(first, second)
        second.write_bytes(b"\x00")
        with self.assertRaises(fleet.ContractError):
            fleet.normalized_file_bytes(second)
        with self.assertRaises(fleet.ContractError):
            fleet.load_stage_b_schema_contracts(self.root)
        for key in fleet.STAGE_B_SCHEMA_VERSIONS:
            for prefix in ("specs/030-stage-b-rollout/contracts", "scripts/config"):
                path = self.root / prefix / (key + ".schema.json")
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("{}")
        self.assertEqual(fleet.load_stage_b_schema_contracts(self.root)["drift"], [])

    def test_plan_run_and_gate_bindings_are_exact(self):
        fleet.require_stage_b_plan_binding({"planSha256": HASH}, HASH)
        for value in (None, {}, {"planSha256": "bad"}):
            with self.assertRaises(fleet.ContractError):
                fleet.require_stage_b_plan_binding(value, HASH)
        path = f".specify/runtime/autonomous-routing/{RUN}/stage-b/evidence.json"
        fleet.require_stage_b_run_path_binding({"runId": RUN, "path": path}, RUN)
        for value in ({}, {"runId": RUN, "path": "../escape"}, {"runId": RUN, "path": "other"}):
            with self.assertRaises(fleet.ContractError):
                fleet.require_stage_b_run_path_binding(value, RUN)
        record = {"gateId": "fixture", "headSha": HEAD, "result": "Passed",
            "workflow": "fixture", "job": "fixture", "runnerOrPlatform": "synthetic", "executedCommand": "not-run-fixture"}
        self.assertEqual(fleet.validate_stage_b_gate_result(record, HEAD, "fixture"), record)
        for changes in ({"headSha": "other"}, {"result": "Failed"}, {"workflow": ""}):
            with self.assertRaises(fleet.ContractError):
                fleet.validate_stage_b_gate_result({**record, **changes}, HEAD, "fixture")
        self.assertTrue(fleet.stage_b_branch_name(RUN, "fixture").startswith("codex/"))

    def test_noop_needs_semantic_and_provider_convergence(self):
        case = {"caseId": "fixture", "expected": "NoOpConverged", "treeEqual": True,
            "profileEqual": True, "workflowEqual": True, "gateEqual": True,
            "rulesetEqual": True, "providerFresh": True}
        self.assertEqual(fleet.evaluate_stage_b_noop(case)["branchWrites"], 0)
        for field in ("providerFresh", "treeEqual", "profileEqual", "workflowEqual", "gateEqual"):
            with self.assertRaises(fleet.ContractError):
                fleet.evaluate_stage_b_noop({**case, field: False})
        self.assertEqual(fleet.evaluate_stage_b_noop({**case, "rulesetEqual": False})["outcome"], "RulesetTransaction")
        fixture_transaction = SimpleNamespace(execute=lambda: {"synthetic": True})
        self.assertEqual(fleet.evaluate_stage_b_noop({**case, "rulesetEqual": False},
            ruleset_transaction=fixture_transaction)["ruleset"], {"synthetic": True})

    def state(self):
        return {"status": "Preflighted", "rolloutPlanBinding": {"planSha256": HASH},
                "fleetSnapshotHash": "fixture", "authorityBinding": {"authorityHash": HASH, "externalWriteGate": "Closed"}}

    def test_state_transitions_are_copied_and_resume_rechecks_all_inputs(self):
        state = self.state()
        self.assertEqual(fleet.transition_stage_b_state(state, "Delivering")["status"], "Delivering")
        self.assertEqual(state["status"], "Preflighted")
        for value, next_state, changes in (({"status": "Completed"}, "Delivering", {}),
                (state, "Delivering", {"unexpected": True}), ({"status": "Preflighted"}, "Delivering", {})):
            with self.assertRaises(fleet.ContractError):
                fleet.transition_stage_b_state(value, next_state, **changes)
        with self.assertRaises(fleet.ContractError):
            fleet.complete_all_noop_stage_b_state(state, [])
        self.assertEqual(fleet.complete_all_noop_stage_b_state(state, [{"outcome": "NoOpConverged"}])["status"], "Completed")
        args = dict(plan_sha256=HASH, fleet_snapshot_hash="fixture", authority_hash=HASH,
            provider_hash=HASH, budget_hash=HASH)
        with self.assertRaises(fleet.ContractError):
            fleet.resume_stage_b_state(state, **args)
        state["status"] = "Stopped"
        for key in args:
            with self.subTest(key=key), self.assertRaises(fleet.ContractError):
                fleet.resume_stage_b_state(state, **{**args, key: "changed"})
        self.assertEqual(fleet.resume_stage_b_state(state, **args)["resumeCount"], 1)
        for key, value in (("baseline_head", "bad"), ("candidate_head", "bad"), ("plan_sha256", "bad")):
            kwargs = dict(run_id=RUN, repository_id="fixture", action="fixture", baseline_head=HEAD,
                          candidate_head=HEAD, plan_sha256=HASH)
            with self.assertRaises(fleet.ContractError):
                fleet.stage_b_idempotency_key(**{**kwargs, key: value})

    def test_budget_model_has_exclusive_limit_and_exact_categories(self):
        args = dict(wave_id=fleet.STAGE_B_WAVES[0], plan_sha256=HASH, fleet_snapshot_hash=HASH,
            wave_result_sha256=HASH, predecessor_result_sha256="N/A", expected_predecessor_sha256="N/A",
            minutes_per_week="1", provider_fresh=True, provider_observed_at="2026-11-02T00:00:00Z",
            copilot_categories={"review-runner-time": "0", "premium-requests": "0", "seat-consumption": "0"})
        projector = fleet.StageBBudgetProjector()
        self.assertEqual(projector.project(**args)["result"], "Pass")
        self.assertEqual(projector.project(**{**args, "minutes_per_week": "120"})["result"], "Blocked")
        for changes in ({"wave_id": "bad"}, {"plan_sha256": "bad"}, {"provider_fresh": False},
                {"predecessor_result_sha256": "bad"}, {"minutes_per_week": "bad"},
                {"minutes_per_week": "-1"}, {"copilot_categories": {}}):
            with self.assertRaises(fleet.ContractError):
                projector.project(**{**args, **changes})

    def test_workflow_normalization_and_inventory_drift(self):
        workflow = {"workflowId": "fixture", "jobId": "check", "triggers": ["push"],
            "runners": ["synthetic"], "averageDurationSeconds": "1.5", "plannedRuns": None}
        self.assertEqual(fleet._normalize_ci_workflows([workflow], "fixture")[0]["averageDurationSeconds"], "1.5")
        for value in (None, [None], [workflow, workflow], [{**workflow, "triggers": []}],
                [{**workflow, "averageDurationSeconds": "bad"}], [{**workflow, "plannedRuns": "-1"}]):
            with self.assertRaises(fleet.ContractError):
                fleet._normalize_ci_workflows(value, "fixture")
        authority = [{"repositoryId": "fixture", "remoteIdentity": "https://example.invalid/fixture"}]
        profiles = {"profiles": [{"profileId": "fixture", "requiredVisibility": "private"}],
            "assignments": [{"repositoryId": "fixture", "profileId": "fixture"}]}
        row = {"repositoryId": "fixture", "remoteIdentity": authority[0]["remoteIdentity"],
               "visibility": "private", "defaultBranch": "main", "workflows": [workflow]}
        kwargs = dict(authoritative=authority, profile_registry=profiles,
                      source_revision="synthetic", observed_at="2026-11-02T00:00:00Z")
        self.assertEqual(fleet.validate_ci_inventory([row], **kwargs)[0]["profileId"], "fixture")
        for changes in ({"profileId": "bad"}, {"visibility": "public"}, {"remoteIdentity": "other"},
                        {"defaultBranch": ""}, {"unknown": True}):
            with self.assertRaises((fleet.ContractError, fleet.CIGateBlocked)):
                fleet.validate_ci_inventory([{**row, **changes}], **kwargs)
        for rows in (None, [], [row, row]):
            with self.assertRaises((fleet.ContractError, fleet.CIGateBlocked)):
                fleet.validate_ci_inventory(rows, **kwargs)

    def test_redaction_isolation_and_causal_binding_requirements(self):
        self.assertEqual(fleet.validate_stage_b_redaction({"synthetic": True})["secretFindings"], 0)
        for value in (SYNTHETIC_REDACTION_SAMPLE, "rawProviderResponse", str(Path.home())):
            with self.assertRaises(fleet.ContractError):
                fleet.validate_stage_b_redaction({"fixture": value})
        isolation = {key: HASH for key in ("g4", "intakeSeries", "copilot", "account", "subscription")}
        self.assertEqual(fleet.build_stage_b_g4_isolation(baseline_hashes=isolation, current_hashes=isolation)["executedActions"], [])
        with self.assertRaises(fleet.ContractError):
            fleet.build_stage_b_g4_isolation(baseline_hashes=isolation, current_hashes={**isolation, "g4": "changed"})
        args = dict(plan_sha256=HASH, candidate_head=HEAD, premerge_sha256=HASH,
                    merge_commit=HEAD, default_head=HEAD, provider_hash=HASH)
        self.assertEqual(fleet.build_stage_b_causal_evidence(**args)["productDelta"], False)
        for key in ("default_head", "candidate_head", "provider_hash"):
            with self.assertRaises(fleet.ContractError):
                fleet.build_stage_b_causal_evidence(**{**args, key: "bad"})

    def test_result_readers_malformed_and_valid_synthetic_reports(self):
        path = self.root / "result.json"
        for read in (fleet.read_toolchain_result, fleet.read_storage_result):
            path.unlink(missing_ok=True)
            self.assertEqual(read(path)[1], "ResultMissing")
            self.assertEqual(read(self.root)[1], "ResultNotFile")
            for payload, failure in ((b"", "ResultEmpty"), (b"\xff", "ResultInvalidUtf8"),
                    (b"{", "ResultTruncated"), (b"{broken}", "ResultMalformed"), (b"[]", "ResultSchemaMismatch")):
                path.write_bytes(payload)
                self.assertEqual(read(path)[1], failure)
            with patch.object(Path, "read_bytes", side_effect=PermissionError):
                self.assertEqual(read(path)[1], "ResultUnreadable")
        tool = {"schemaVersion": "1.0", "platform": "Linux", "mode": "dry-run", "overallStatus": "SUCCESS",
            "exitCode": 0, "items": [], "remainingRequired": [], "optionalDrift": [], "nextAction": "N/A"}
        path.write_text(json.dumps(tool))
        self.assertIsNone(fleet.read_toolchain_result(path)[1])
        report = {"schemaVersion": "1.0", "runId": RUN, "platform": "darwin", "mode": "dry-run",
            "profile": "safe", "overallStatus": "SUCCESS", "exitCode": 0, "repositories": [],
            "providers": [], "warnings": [], "nextAction": "N/A"}
        path.write_text(json.dumps(report))
        self.assertIsNone(fleet.read_storage_result(path)[1])
        for value in ("bad", "00000000-0000-0000-0000-000000000000X"):
            path.write_text(json.dumps({**report, "runId": value}))
            self.assertEqual(fleet.read_storage_result(path)[1], "ResultSchemaMismatch")
        for state, expected in (("Failed", "PARTIAL"), ("Blocked", "DRIFT"), ("Warning", "DRIFT"), ("Passed", "SUCCESS")):
            self.assertEqual(fleet.derive_status([{"result": state}], "check-only")[0], expected)


if __name__ == "__main__":
    unittest.main()
