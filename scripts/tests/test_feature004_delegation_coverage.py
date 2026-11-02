"""DE: Isolierte Delegationszweige. EN: Synthetic delegation branch fixtures.

All transport/storage calls are replaced: no Podman, maintenance or host repair.
Real-process/platform evidence remains a separate requirement.
"""
import copy
import datetime
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


LIB = Path(__file__).resolve().parents[1] / "lib"


def load(name):
    spec = importlib.util.spec_from_file_location(name, LIB / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


context = load("maintenance_execution_context")
worker = load("maintenance_container_worker")


def completed(code=0, out="", err=""):
    return subprocess.CompletedProcess([], code, out, err)


class DelegationCoverageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="ade004-delegation-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.repo = self.root / "Projects" / "repo with spaces"
        (self.repo / ".git").mkdir(parents=True)
        self.contract = {
            "schemaVersion": 1, "container": "synthetic", "user": "tester",
            "source": "/opt/reference", "approvalPath": "approval.md",
            "expiresOn": "2099-12-31",
            "mounts": [{"host": "Projects", "container": "/projects"}],
        }
        self.contract_path = self.root / "contract.json"
        self.contract_path.write_text(json.dumps(self.contract), encoding="utf-8")
        self.manifest = self.root / "manifest.json"
        self.manifest.write_text(json.dumps({"targets": [
            {"id": "fixture", "path": "Projects/repo with spaces", "active": True,
             "kind": "git-repository"}]}), encoding="utf-8")
        self.registry = self.root / "registry.json"
        self.registry.write_text(json.dumps({"repositories": [
            {"path": "Projects/repo with spaces", "level": 2}]}), encoding="utf-8")
        self.evidence = dict(containerId="container-fixture", image="image-fixture",
                             approvalSha256="a" * 64, sourceSha256="b" * 64)
        self.report = self.root / "report.json"
        self.report.write_text(json.dumps({"runId": "fixture", "executionContexts": [
            {"context": "container", **self.evidence}],
            "mutationBarrier": {"domainMutationAllowed": True}}), encoding="utf-8")
        self.args = SimpleNamespace(contract=self.contract_path, manifest=self.manifest,
            home_dir=self.root, source=self.root, registry=self.registry, report=self.report,
            phase="propagation", mode="check-only", repair_drift=False,
            cleanup_profile="safe", confirm_deep_cleanup=False, output=self.root / "host.json")
        # Never inherit or execute a real transport, including on unexpected paths.
        self.transport = self.enterContext(patch.object(context.subprocess, "run",
            side_effect=AssertionError("Unexpected external process")))

    def router(self):
        targets = json.loads(self.manifest.read_text())["targets"]
        return context.ExecutionContexts(self.contract_path, self.root, targets)

    def payload(self, phase="propagation", mode="update"):
        return {"source": str(self.root), "mode": mode, "phase": phase,
            "runId": "fixture", "repairDrift": True, "cleanupProfile": "safe",
            "defaultPresetProfile": "none", "entries": [{"containerRoot": str(self.root),
            "containerPath": str(self.repo), "targetId": "fixture",
            "registry": {"path": "Projects/repo with spaces", "level": 2}}]}

    def info(self):
        return {"Id": "container-fixture", "Image": "image-fixture", "State": {"Running": True},
            "Config": {"User": "tester"}, "Mounts": [{"Destination": "/projects",
            "Source": str(self.root / "Projects"), "Type": "bind", "RW": True}]}

    def phase(self, output=None, preflight=None):
        output = output or {"status": "Passed", "records": [], "repaired": False}
        with patch.object(context.ExecutionContexts, "preflight", return_value=preflight or self.evidence), \
                patch.object(context, "source_bindings", return_value={}), \
                patch.dict(sys.modules, {"agentic_workspace_fleet": SimpleNamespace(
                    write_report=lambda path, data: path.write_text(json.dumps(data)))}):
            self.transport.side_effect = None
            self.transport.return_value = completed(out=json.dumps(output))
            with patch("sys.stdout", new_callable=io.StringIO):
                return context.run_phase(self.args)

    def test_contract_invalid_fields_and_date_boundaries(self):
        invalid = [None, {}, {**self.contract, "user": "root;id"},
            *({**self.contract, "expiresOn": value} for value in (None, "x", "2099-02-30")),
            *({**self.contract, "mounts": value} for value in ([], None, [None],
                [{"host": "Projects", "container": "relative"}],
                [{"host": "Projects/sub", "container": "/projects"}],
                [{"host": "Projects", "container": "/projects/sub"}],
                self.contract["mounts"] * 2)),
            {**self.contract, "source": "relative"}]
        for data in invalid:
            with self.subTest(data=data), self.assertRaises(context.ExecutionContextError):
                context.validate_contract(data)
        self.assertEqual(context.validate_contract(self.contract,
            today=datetime.date(2099, 12, 31)), self.contract)

    def test_mapping_external_and_registry_filter_keep_host_entries(self):
        router = self.router()
        self.assertIsNone(router.mapping(self.root.parent / "unrelated"))
        registry = {"marker": "keep", "repositories": [
            {"path": "Projects/repo with spaces"}, {"path": "Other/repo"}]}
        result = context.filter_registry(router, registry)
        self.assertEqual(result, {"marker": "keep", "repositories": [{"path": "Other/repo"}]})
        self.assertEqual(len(registry["repositories"]), 2)

    def test_inspect_ambiguous_readonly_wrong_source_and_valid(self):
        router = self.router()
        bad_mounts = [{**self.info()["Mounts"][0], "Source": str(self.root / "Other")},
                      {**self.info()["Mounts"][0], "RW": False},
                      {**self.info()["Mounts"][0], "Type": "volume"}]
        rows = [[], [self.info(), self.info()]] + [
            [{**self.info(), "Mounts": [mount]}] for mount in bad_mounts]
        self.transport.side_effect = None
        for value in rows:
            self.transport.return_value = completed(out=json.dumps(value))
            with self.subTest(value=value), self.assertRaises(context.ExecutionContextError):
                router.inspect()
        self.transport.return_value = completed(out=json.dumps([self.info()]))
        self.assertEqual(router.inspect(), self.info())

    def test_preflight_missing_mismatched_and_failed_source_then_success(self):
        router = self.router()
        approval = self.root / "approval.md"
        with self.assertRaisesRegex(context.ExecutionContextError, "missing"):
            router.preflight()
        approval.write_text("not an approval")
        with self.assertRaisesRegex(context.ExecutionContextError, "does not match"):
            router.preflight()
        approval.write_text("Owner 31.12.2099", encoding="utf-8")
        self.transport.side_effect = None
        with patch.object(router, "inspect", return_value=self.info()), \
                patch.object(context, "source_bindings", return_value={"fixture": "hash"}):
            self.transport.return_value = completed(2)
            with self.assertRaisesRegex(context.ExecutionContextError, "source binding"):
                router.preflight(self.root)
            self.transport.return_value = completed(out="ready")
            result = router.preflight(self.root)
        self.assertEqual(result["containerId"], "container-fixture")
        self.assertEqual(result["approvalSha256"], hashlib.sha256(approval.read_bytes()).hexdigest())
        self.assertEqual(self.transport.call_args.kwargs["timeout"], 60)

    def test_request_fail_closed_and_argument_identity(self):
        router = self.router()
        with self.assertRaisesRegex(context.ExecutionContextError, "not delegated"):
            router.request(self.root / "Other", "git")
        with self.assertRaisesRegex(context.ExecutionContextError, "preflight"):
            router.request(self.repo, "git")
        router.container_id = "container-fixture"
        self.transport.side_effect = None
        with patch.object(router, "inspect", return_value=self.info()):
            for response, message in ((completed(2), "no host fallback"),
                                      (completed(out="not-json"), "Malformed")):
                self.transport.return_value = response
                with self.assertRaisesRegex(context.ExecutionContextError, message):
                    router.request(self.repo, "git")
            self.transport.return_value = completed(out=json.dumps(
                {"returncode": 7, "stdout": "output", "stderr": "error"}))
            args = ("status", "--", "space and umlaut-ae", "-leading")
            result = router.git(self.repo, args)
            sent = json.loads(self.transport.call_args.kwargs["input"])
        self.assertEqual(sent["arguments"], list(args))
        self.assertEqual(result.returncode, 7)
        self.assertEqual(result.stderr, "error")
        self.assertEqual(self.transport.call_args.kwargs["timeout"], 120)

    def test_phase_prior_binding_registry_symlink_and_barrier(self):
        with self.assertRaisesRegex(context.ExecutionContextError, "preflight"):
            self.phase(preflight={**self.evidence, "image": "different"})
        original = self.registry.read_bytes()
        self.registry.unlink()
        target = self.root / "target.json"
        target.write_bytes(original)
        self.registry.symlink_to(target)
        with self.assertRaisesRegex(context.ExecutionContextError, "symlink"):
            self.phase()
        self.registry.unlink()
        self.registry.write_bytes(original)
        self.args.mode = "update"
        report = json.loads(self.report.read_text())
        report["mutationBarrier"]["domainMutationAllowed"] = False
        self.report.write_text(json.dumps(report))
        with self.assertRaisesRegex(context.ExecutionContextError, "barrier"):
            self.phase()
        self.transport.assert_not_called()

    def test_phase_host_filter_missing_target_and_transport_failure(self):
        self.args.phase = "host-registry"
        self.assertEqual(self.phase(), 0)
        self.assertEqual(json.loads(self.args.output.read_text())["repositories"], [])
        self.transport.assert_not_called()
        self.args.phase = "propagation"
        self.registry.write_text('{"repositories": []}')
        with self.assertRaisesRegex(context.ExecutionContextError, "every delegated"):
            self.phase()
        self.transport.assert_not_called()

    def test_phase_status_mapping_and_registry_translation_preserve_permissions(self):
        for status, code, repaired in (("Passed", 0, False), ("Blocked", 1, False),
                                       ("Failed", 2, False), ("Passed", 3, True)):
            with self.subTest(status=status, repaired=repaired):
                self.assertEqual(self.phase({"status": status, "records": [{
                    "targetId": "fixture", "status": status}], "repaired": repaired}), code)
        self.args.phase, self.args.mode = "registry", "update"
        self.registry.chmod(0o600)
        out = {"status": "Passed", "records": [], "registry": [
            {"path": "/projects/repo with spaces", "level": 2, "marker": "kept"}]}
        self.assertEqual(self.phase(out), 0)
        data = json.loads(self.registry.read_text())
        self.assertEqual(data["repositories"][0]["path"], "Projects/repo with spaces")
        self.assertEqual(data["repositories"][0]["marker"], "kept")
        self.assertEqual(self.registry.stat().st_mode & 0o777, 0o600)
        out["registry"] = []
        with self.assertRaisesRegex(context.ExecutionContextError, "unexpected registry"):
            self.phase(out)

    def test_source_bindings_synthetic_complete_package_and_symlink(self):
        paths = ["scripts/config/agentic-toolchain-maintenance-files.json",
            "scripts/lib/maintenance_execution_context.py", "scripts/lib/maintenance_container_worker.py",
            "scripts/config/maintenance-execution-contexts.json", "scripts/fixture.sh"]
        for relative in paths:
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"fixture\r\n")
        (self.root / paths[0]).write_text(json.dumps({"files": [{"path": paths[-1]}]}))
        result = context.source_bindings(self.root)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[paths[-1]], hashlib.sha256(b"fixture\n").hexdigest())
        (self.root / paths[-1]).unlink()
        (self.root / paths[-1]).symlink_to(self.root / paths[1])
        with self.assertRaisesRegex(context.ExecutionContextError, "Unsafe"):
            context.source_bindings(self.root)

    def test_context_main_reports_invalid_contract_without_transport(self):
        argv = ["context", "--contract", str(self.contract_path), "--manifest", str(self.manifest),
            "--home-dir", str(self.root), "--source", str(self.root), "--registry", str(self.registry),
            "--report", str(self.report), "--phase", "registry", "--mode", "check-only"]
        with patch.object(sys, "argv", argv), patch.object(context, "run_phase",
                side_effect=context.ExecutionContextError("synthetic rejection")), \
                patch("sys.stderr", new_callable=io.StringIO) as err:
            self.assertEqual(context.main(), 2)
        self.assertIn("BLOCKED", err.getvalue())
        self.transport.assert_not_called()

    def test_worker_clean_repair_success_and_each_failure_stage(self):
        payload = self.payload()
        for preview, applied, checked, expected, calls in (
                (2, 0, 0, "Failed", 3), (0, 2, 0, "Failed", 4),
                (0, 0, 1, "Failed", 5), (0, 0, 0, "Passed", 5)):
            results = [completed(1, "drift"), completed(), completed(preview),
                       completed(applied), completed(checked)]
            with self.subTest(preview=preview, applied=applied, checked=checked):
                self.transport.side_effect = results
                self.transport.reset_mock()
                result = worker.execute(payload)
                self.assertEqual(result["status"], expected)
                self.assertEqual(self.transport.call_count, calls)
                self.assertEqual(self.transport.call_args_list[2].args[0][-1], "--dry-run")
                self.assertTrue(all(call.kwargs["timeout"] in (30, 600)
                                    for call in self.transport.call_args_list))
                self.assertEqual(result["repaired"], expected == "Passed")

    def test_worker_profile_skip_reject_config_drift_and_bounded_repair(self):
        payload = self.payload("preset-profiles")
        self.assertEqual(worker.execute(payload)["records"][0]["status"], "Skipped")
        config = self.root / "scripts/config/spec-kit-preset-profiles.json"
        config.parent.mkdir(parents=True)
        payload["defaultPresetProfile"] = "fixture"
        for value in (None, "/absolute", "../escape"):
            config.write_text(json.dumps({"profiles": {"fixture": {"configPath": value}}}))
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "matrix path"):
                worker.execute(payload)
        self.transport.assert_not_called()
        config.write_text(json.dumps({"profiles": {"fixture": {"presetConfig": "safe.json"}}}))
        self.transport.side_effect = [completed(out="local"), completed(out="remote")]
        result = worker.execute(payload)
        self.assertEqual(result["records"][0]["reason"], "CanonicalPresetWorktreeRequired")
        self.transport.reset_mock()
        self.transport.side_effect = [completed(out="same"), completed(out="same"),
            completed(1), completed(), completed(), completed(), completed()]
        result = worker.execute(payload)
        self.assertEqual(result["status"], "Passed")
        self.assertEqual(self.transport.call_args_list[5].args[0][-1], "--force")

    def test_worker_registry_exit_statuses_and_readonly_preview(self):
        for mode, code, output, expected in (("update", 0, "updated: fixture", "Passed"),
                ("check-only", 0, "added: fixture", "Blocked"),
                ("dry-run", 0, "unchanged", "Passed"), ("update", 2, "failed", "Failed")):
            self.transport.side_effect = None
            self.transport.return_value = completed(code, output)
            with self.subTest(mode=mode, code=code):
                result = worker.execute(self.payload("registry", mode))
                self.assertEqual(result["status"], expected)
                self.assertEqual(result["registry"][0]["level"], 2)

    def test_worker_storage_is_fake_and_preview_blocks_mutation(self):
        for mode, preview_code, overall, code, warnings, expected, calls in (
                ("check-only", 0, "SUCCESS", 0, [], "Passed", 1),
                ("check-only", 0, "SUCCESS", 0, ["fixture"], "Blocked", 1),
                ("check-only", 0, "SUCCESS", 2, [], "Failed", 1),
                ("update", 1, "SUCCESS", 0, [], "Blocked", 1),
                ("update", 0, "FAILED", 0, [], "Blocked", 1),
                ("update", 0, "SUCCESS", 0, [], "Passed", 2)):
            observed = []
            def parse(argv):
                parsed = SimpleNamespace(report=Path(argv[argv.index("--report") + 1]),
                    mode=argv[argv.index("--mode") + 1])
                self.assertIn("--projects-only", argv)
                return parsed
            def execute(args):
                observed.append(args.mode)
                args.report.write_text(json.dumps({"overallStatus": overall, "warnings": warnings}))
                return preview_code if args.mode == "dry-run" else code
            storage = SimpleNamespace(build_parser=lambda: SimpleNamespace(parse_args=parse), execute=execute)
            with self.subTest(mode=mode, expected=expected), \
                    patch.dict(sys.modules, {"workspace_storage_maintenance": storage}):
                result = worker.execute(self.payload("storage-cleanup", mode))
            self.assertEqual(result["status"], expected)
            self.assertEqual(len(observed), calls)
            if mode == "update":
                self.assertEqual(observed[0], "dry-run")
        self.transport.assert_not_called()

    def test_worker_direct_boundary_rechecks_and_trust_environment_restoration(self):
        payload = self.payload()
        gitdir = self.repo / ".git"
        gitdir.rmdir()
        with self.assertRaisesRegex(ValueError, "Missing"):
            worker._execute(payload)
        gitdir.mkdir()
        alias = self.root / "alias"
        alias.symlink_to(self.repo, target_is_directory=True)
        bad = copy.deepcopy(payload)
        bad["entries"][0]["containerPath"] = str(alias)
        with self.assertRaisesRegex(ValueError, "symlink"):
            worker._execute(bad)
        with patch.dict(os.environ, {"GIT_CONFIG_PARAMETERS": "synthetic", "GIT_CONFIG_VALUE_9": "old"}):
            before = dict(os.environ)
            with worker.repository_trust(payload["entries"]):
                self.assertNotIn("GIT_CONFIG_PARAMETERS", os.environ)
                self.assertNotIn("GIT_CONFIG_VALUE_9", os.environ)
                self.assertEqual(os.environ["GIT_CONFIG_VALUE_1"], str(self.repo))
            self.assertEqual(dict(os.environ), before)
        self.transport.assert_not_called()


if __name__ == "__main__":
    unittest.main()
