"""Owned storage fixtures and intercepted providers; never global cleanup.

DE: Nur temporaere Testdaten. EN: Temporary test data, not host maintenance.
"""
import copy
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("storage_branch_fixtures",
    Path(__file__).resolve().parents[1] / "lib/workspace_storage_maintenance.py")
storage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(storage)


def result(code=0, stdout="", stderr=""):
    return subprocess.CompletedProcess([], code, stdout, stderr)


class StorageBranchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ade004-storage-")
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name).resolve()
        self.repo = self.home / "repo"
        (self.repo / ".git").mkdir(parents=True)
        self.enterContext(patch("sys.stdout", new_callable=io.StringIO))
        self.enterContext(patch("sys.stderr", new_callable=io.StringIO))
        self.spawn = self.enterContext(patch.object(storage.subprocess, "run",
            side_effect=AssertionError("Real storage/provider process forbidden")))
        self.policy = {"schemaVersion": 1, "retentionDays": 7, "pressureFreePercent": 10,
                       "nonMslAdapters": [], "genericBuildAdapters": []}

    def directory(self, name="build"):
        path = self.repo / name
        path.mkdir(exist_ok=True)
        (path / "output").write_text("synthetic")
        return path

    def test_contract_objects_paths_policy_and_registry(self):
        path = self.home / "input.json"
        for text in ("not json", "[]"):
            path.write_text(text)
            with self.assertRaises(storage.StorageContractError):
                storage.load_json_object(path, "fixture")
        for raw in (None, "", "/outside", "../escape"):
            with self.assertRaises(storage.StorageContractError):
                storage.validate_relative_path(raw, "fixture")
        for path in (self.home, self.home / ".."):
            with self.assertRaises(storage.StorageContractError):
                storage.contained_path(path, self.repo, "fixture")
        adapter = {"repositoryPath": "repo", "adapter": "cc65-make"}
        for value in (None, [None], [{**adapter, "adapter": "bad"}], [adapter, adapter]):
            with self.assertRaises(storage.StorageContractError):
                storage.policy_adapter_map({"nonMslAdapters": value})
        for key, value in (("schemaVersion", 2), ("retentionDays", 0),
                ("pressureFreePercent", 51), ("genericBuildAdapters", None)):
            with self.assertRaises(storage.StorageContractError):
                storage.validate_policy({**self.policy, key: value})
        with self.assertRaises(storage.StorageContractError):
            storage.registry_level2_entries({})
        entries = [{"path": "repo", "level": 2}, {"path": "REPO", "level": 2}]
        with self.assertRaises(storage.StorageContractError):
            storage.registry_level2_entries({"repositories": entries})
        self.assertEqual(storage.registry_level2_entries({"repositories": [None, {"level": 0}]}), [])

    def test_runtime_and_non_msl_justification(self):
        for entry, expected in (({"primaryLanguage": "Rust"}, "msl"),
                ({"primaryLanguage": "C++"}, "non-msl"), ({"mslStatus": "n/a"}, "n/a"),
                ({}, "unknown")):
            self.assertEqual(storage.classify_runtime(entry, None)[1], expected)
        self.assertFalse(storage.has_non_msl_justification(self.repo))
        (self.repo / "constitution.md").write_text("Non-MSL justification: synthetic adapter")
        self.assertTrue(storage.has_non_msl_justification(self.repo))
        with patch.object(Path, "read_text", side_effect=PermissionError):
            self.assertFalse(storage.has_non_msl_justification(self.repo))

    def test_process_parsers_and_unavailable_inventory_are_fail_closed(self):
        self.assertEqual(storage.parse_tasklist_processes('bad\n"tool.exe","bad"\n"own","5"\n"cmake.exe","6"', 5), {"cmake"})
        self.assertEqual(storage.parse_ps_processes("bad\nbad cmd\n5 own\n6 /bin/cmake\n7 node npm-cli.js install", 5),
                         {"cmake", "node", "npm"})
        with patch.object(storage, "run_command", return_value=result(2)):
            self.assertEqual(storage.process_inventory(), {storage.PROCESS_INVENTORY_UNAVAILABLE})
        self.assertTrue(storage.adapter_is_busy("x", {storage.PROCESS_INVENTORY_UNAVAILABLE}, {}))
        self.assertFalse(storage.provider_is_busy(set(), {"npm"}))
        self.assertTrue(storage.provider_is_busy({"npm"}, {"npm"}))

    def test_process_error_conversion_and_git_proofs(self):
        for error, code in ((PermissionError("fixture"), 127),
                            (subprocess.TimeoutExpired(["fixture"], 1), 124)):
            with patch.object(storage.subprocess, "run", side_effect=error):
                self.assertEqual(storage.run_command(["synthetic"], environment={"TEST": "1"}).returncode, code)
        with patch.object(storage, "git", return_value=result(2)):
            with self.assertRaises(storage.StorageContractError):
                storage.repository_is_dirty(self.repo)
        with patch.object(storage, "git", return_value=result(stdout=" M fixture")):
            self.assertTrue(storage.repository_is_dirty(self.repo))
        self.assertFalse(storage.git_file_is_tracked(self.repo, self.home / "outside"))
        self.assertFalse(storage.git_path_is_ignored_and_untracked(self.repo, self.home / "outside"))

    def test_metrics_skip_links_and_bind_candidate_layout(self):
        build = self.directory()
        (build / "nested").mkdir()
        (build / "linked-dir").symlink_to(self.home, target_is_directory=True)
        (build / "linked-file").symlink_to(build / "output")
        self.assertEqual(storage.directory_metrics(build)[1], 1)
        self.assertEqual(storage.directory_metrics(self.home / "missing"), (0, 0, 0))
        self.assertEqual(storage.age_days(0), 0)
        self.assertEqual(storage.age_days(100, now_epoch=50), 0)
        candidate = storage.candidate_record(self.repo, build, "synthetic", 7, True)
        self.assertTrue(candidate["eligible"])
        self.assertEqual(storage.cache_path_metrics([build, self.home / "missing"])[0], candidate["sizeBytes"])
        with patch.object(storage, "git_path_is_ignored_and_untracked", return_value=False), \
                self.assertRaisesRegex(storage.StorageContractError, "lost ignored"):
            storage.remove_candidate(self.repo, candidate)
        with patch.object(storage, "git_path_is_ignored_and_untracked", return_value=True), \
                patch.object(storage, "directory_metrics", return_value=(999, 1, 1)), \
                self.assertRaisesRegex(storage.StorageContractError, "contents changed"):
            storage.remove_candidate(self.repo, candidate)
        self.assertTrue((build / "output").is_file())

    def test_cc65_deep_preview_busy_and_curated_rejection(self):
        self.directory()
        adapter = {"safeGroups": [{"id": "fixture", "paths": ["build"]}], "protectedEvidencePatterns": []}
        for mode, dirty, expected in (("dry-run", False, "Passed"), ("update", True, "Warning")):
            with patch.object(storage, "git_path_is_ignored_and_untracked", return_value=True):
                progress = {}
                candidates, _, freed, status, _ = storage.handle_cc65(self.repo, adapter, mode=mode,
                    profile="deep", retention_days=7, pressure_mode=False, dirty=dirty, busy=False, progress=progress)
            self.assertEqual(status, expected)
            self.assertEqual(freed, 0)
            self.assertEqual(progress["candidates"], candidates)
        with patch.object(storage, "git_path_is_ignored_and_untracked", return_value=False), \
                self.assertRaisesRegex(storage.StorageContractError, "ignored"):
            storage.handle_cc65(self.repo, adapter, mode="update", profile="deep", retention_days=7,
                pressure_mode=False, dirty=False, busy=False)
        adapter["safeGroups"] = [{"paths": ["build", "BUILD"]}]
        with self.assertRaisesRegex(storage.StorageContractError, "duplicate"):
            storage.handle_cc65(self.repo, adapter, mode="dry-run", profile="deep", retention_days=7,
                pressure_mode=False, dirty=False, busy=False)

    def test_cmake_failure_dispatch_never_runs_cmake(self):
        build = self.directory()
        candidate = storage.candidate_record(self.repo, build, "cmake", 7, True)
        for mode, dirty, available, exit_code, expected in (("dry-run", False, True, 0, "Passed"),
                ("update", True, True, 0, "Warning"), ("update", False, False, 0, "Warning"),
                ("update", False, True, 2, "Warning"), ("update", False, True, 0, "Passed")):
            with patch.object(storage, "discover_cmake_candidates", return_value=[copy.deepcopy(candidate)]), \
                    patch.object(storage.shutil, "which", return_value="synthetic" if available else None), \
                    patch.object(storage, "run_command", return_value=result(exit_code)) as run, \
                    patch.object(storage, "remove_candidate", return_value=9) as remove:
                _, freed, status = storage.handle_cmake(self.repo, {}, mode=mode, retention_days=7,
                    pressure_mode=True, dirty=dirty, busy=False)
                self.assertEqual(status, expected)
                self.assertEqual(freed, 9 if mode == "update" and not dirty and available and not exit_code else 0)
                if mode != "update" or dirty or not available:
                    run.assert_not_called()
                    remove.assert_not_called()

    def test_cc65_owned_old_and_fresh_candidates_dispatch_without_real_removal(self):
        old = self.directory()
        self.directory("fresh")
        os.utime(old / "output", (1, 1))
        os.utime(old, (1, 1))
        adapter = {"safeGroups": [{"id": "fixture", "paths": ["build", "fresh"]}],
                   "protectedEvidencePatterns": []}
        for profile, dirty, progress in (("deep", False, {}), ("deep", False, None),
                ("safe", True, {}), ("safe", False, {})):
            with patch.object(storage, "git_path_is_ignored_and_untracked", return_value=True), \
                    patch.object(storage, "remove_candidate", return_value=9) as remove:
                candidates, _, freed, status, _ = storage.handle_cc65(self.repo, adapter,
                    mode="update", profile=profile, retention_days=7, pressure_mode=False,
                    dirty=dirty, busy=False, progress=progress)
                expected_calls = 0 if dirty else 2 if profile == "deep" else 1
                self.assertEqual(remove.call_count, expected_calls)
                self.assertEqual(freed, 9 * expected_calls)
                self.assertEqual(status, "Warning" if dirty else "Passed")
                if profile == "safe":
                    self.assertEqual([c["eligible"] for c in candidates], [True, False])
                if progress is not None and freed:
                    self.assertEqual(progress["freedBytes"], freed)
            self.assertTrue((old / "output").exists())
        with patch.object(storage, "git_path_is_ignored_and_untracked", return_value=False), \
                self.assertRaises(storage.StorageContractError):
            storage.handle_cc65(self.repo, adapter, mode="dry-run", profile="safe",
                retention_days=7, pressure_mode=False, dirty=False, busy=False)

    def test_cmake_discovery_requires_tracked_source_ignored_build_and_matching_home(self):
        build = self.directory()
        cache = build / "CMakeCache.txt"
        cache.write_text(f"CMAKE_HOME_DIRECTORY:INTERNAL={self.repo}\n")
        (self.repo / "CMakeLists.txt").write_text("synthetic")
        for tracked, ignored, count in ((True, True, 1), (False, True, 0), (True, False, 0)):
            with patch.object(storage, "git_file_is_tracked", return_value=tracked), \
                    patch.object(storage, "git_path_is_ignored_and_untracked", return_value=ignored):
                self.assertEqual(len(storage.discover_cmake_candidates(self.repo,
                    {"buildDirectoryPatterns": ["build"]}, 7, True)), count)
        cache.write_text(f"CMAKE_HOME_DIRECTORY:INTERNAL={self.home}\n")
        self.assertEqual(storage.discover_cmake_candidates(self.repo, {"buildDirectoryPatterns": ["build"]}, 7, True), [])
        cache.write_text("no home")
        self.assertIsNone(storage.read_cmake_home(cache))
        self.assertIsNone(storage.read_cmake_home(self.home / "missing"))

    def test_fake_cache_providers_keep_home_scope_and_busy_boundaries(self):
        for profile, mode, processes in (("safe", "dry-run", set()), ("deep", "update", set()),
                ("safe", "update", {"npm", "brew", "go", "dotnet"}),
                ("deep", "update", {storage.PROCESS_INVENTORY_UNAVAILABLE})):
            with patch.dict(os.environ, {"npm_config_cache": str(self.home / ".npm")}), \
                    patch.object(storage.shutil, "which", side_effect=lambda name: str(self.home / name)), \
                    patch.object(storage, "run_command",
                        return_value=result(stdout=f"{self.home / '.npm'}\n")), \
                    patch.object(storage, "cache_path_metrics", return_value=(100, 1)), \
                    patch.object(storage, "execute_provider") as execute:
                items = storage.handle_cache_providers(self.home, mode=mode, profile=profile,
                    pressure_mode=True, retention_days=7, processes=processes)
                self.assertTrue(items)
                if mode != "update" or processes:
                    execute.assert_not_called()
                else:
                    self.assertGreaterEqual(execute.call_count, 4)
        with patch.dict(os.environ, {"npm_config_cache": str(self.home.parent)}), \
                patch.object(storage.shutil, "which", side_effect=lambda name: "fake-npm" if name == "npm" else None), \
                patch.object(storage, "run_command",
                    return_value=result(stdout=f"{self.home.parent}\n")), \
                patch.object(storage, "cache_path_metrics", return_value=(0, 0)):
            items = storage.handle_cache_providers(self.home, mode="update", profile="safe",
                pressure_mode=False, retention_days=7, processes=set())
            self.assertEqual(items[0]["status"], "ProviderUnavailable")

    def test_provider_result_and_dangling_image_plan_only_against_stubs(self):
        for code, text in ((0, ""), (2, "fixture failure"), (2, "")):
            item = storage.provider_item("fixture", "cleanup", 0, "update")
            with patch.object(storage, "run_command", return_value=result(code, stderr=text)):
                storage.execute_provider(item, ["synthetic"])
            self.assertEqual(item["status"], "Warning" if code else "Completed")
        for present, pressure in (("podman", False), ("podman", True), ("docker", False)):
            with patch.object(storage.shutil, "which", side_effect=lambda name: "fake-" + name if name == present else None), \
                    patch.object(storage, "podman_socket_arguments", return_value=([], None)), \
                    patch.object(storage, "execute_provider") as execute:
                items = storage.handle_container_provider(mode="update", pressure_mode=pressure,
                    retention_days=7, processes=set())
                argv = execute.call_args.args[1]
                self.assertNotIn("--all", argv)
                self.assertEqual("--filter" in argv, not pressure)
                self.assertEqual(items[0]["provider"], present)
        with patch.object(storage.shutil, "which", return_value="fake"), \
                patch.object(storage, "podman_socket_arguments", return_value=([], "unavailable")), \
                patch.object(storage, "execute_provider") as execute:
            items = storage.handle_container_provider(mode="update", pressure_mode=False, retention_days=7, processes=set())
            self.assertEqual(items[0]["status"], "ProviderUnavailable")
            execute.assert_not_called()

    def test_socket_inspection_errors_and_verified_synthetic_socket(self):
        with patch.object(storage.sys, "platform", "darwin"):
            for response in (result(2), result(stdout="bad json"), result(stdout="{}"),
                    result(stdout='[null, {"State":"stopped"}, {"State":"running"}]')):
                with patch.object(storage, "run_command", return_value=response):
                    self.assertIsNotNone(storage.podman_socket_arguments()[1])
            payload = [{"State": "running", "ConnectionInfo": {"PodmanSocket": {"Path": str(self.home / "socket")}}}]
            with patch.object(storage, "run_command", return_value=result(stdout=json.dumps(payload))), \
                    patch.object(Path, "stat", return_value=SimpleNamespace(st_mode=stat.S_IFSOCK)):
                self.assertEqual(storage.podman_socket_arguments(), (["--url", f"unix://{self.home}/socket"], None))

    def args(self):
        policy = self.home / "policy.json"
        policy.write_text(json.dumps(self.policy))
        registry = self.home / "registry.json"
        registry.write_text(json.dumps({"repositories": []}))
        return SimpleNamespace(home_dir=self.home, policy=policy, registry=registry,
            report=self.home / "report.json", mode="dry-run", profile="safe",
            run_id="11111111-1111-4111-8111-111111111111", confirm_deep_cleanup=False, projects_only=True)

    def test_execute_failure_contracts_emit_failed_not_success(self):
        for changes in ({"run_id": "bad"}, {"profile": "bad"}, {"mode": "bad"},
                {"profile": "deep", "mode": "update"}):
            args = self.args()
            vars(args).update(changes)
            self.assertEqual(storage.execute(args), 2)
            self.assertEqual(json.loads(args.report.read_text())["overallStatus"], "FAILED")

    def test_atomic_report_failure_preserves_previous_and_cleans_temporary(self):
        report = self.home / "atomic.json"
        storage.atomic_write_json(report, {"previous": True})
        with patch.object(storage.os, "replace", side_effect=PermissionError("fixture")), \
                self.assertRaises(PermissionError):
            storage.atomic_write_json(report, {"candidate": True})
        self.assertEqual(json.loads(report.read_text()), {"previous": True})
        self.assertFalse(list(self.home.glob(".atomic.json.*.tmp")))
        with patch.object(storage.os, "chmod", side_effect=PermissionError("fixture")), \
                self.assertRaises(PermissionError):
            storage.atomic_write_json(report, {"publishedBeforeChmodFailure": True})
        self.assertEqual(json.loads(report.read_text()), {"publishedBeforeChmodFailure": True})

    def test_execute_non_msl_adapter_dispatch_and_warning_collection(self):
        for adapter_id in ("cc65-make", "cmake-out-of-source"):
            args = self.args()
            adapter = {"repositoryPath": "repo", "adapter": adapter_id,
                "runtimeClass": "synthetic-non-msl", "mslStatus": "non-msl", "id": "fixture"}
            args.policy.write_text(json.dumps({**self.policy, "nonMslAdapters": [adapter]}))
            args.registry.write_text(json.dumps({"repositories": [{"level": 2, "path": "repo"}]}))
            with patch.object(storage, "disk_snapshot", return_value={"freePercent": 50, "freeBytes": 100}), \
                    patch.object(storage, "process_inventory", return_value=set()), \
                    patch.object(storage, "repository_is_dirty", return_value=False), \
                    patch.object(storage, "has_non_msl_justification", return_value=True), \
                    patch.object(storage, "handle_cc65", return_value=([], [], 0, "Warning", ["synthetic warning"])) as cc65, \
                    patch.object(storage, "handle_cmake", return_value=([], 0, "Passed")) as cmake:
                self.assertEqual(storage.execute(args), 0)
                self.assertEqual(cc65.call_count, int(adapter_id == "cc65-make"))
                self.assertEqual(cmake.call_count, int(adapter_id == "cmake-out-of-source"))
            data = json.loads(args.report.read_text())
            self.assertEqual(data["repositories"][0]["status"], "Warning" if adapter_id == "cc65-make" else "Passed")
            self.assertEqual(bool(data["warnings"]), adapter_id == "cc65-make")

    def test_execute_synthetic_repository_skips_and_dispatch(self):
        for entry, justified, expected in (({"path": "missing", "level": 2}, False, "SkippedMissing"),
                ({"path": "repo", "level": 2, "primaryLanguage": "C++"}, False, "NonMslJustificationMissing"),
                ({"path": "repo", "level": 2, "primaryLanguage": "C++"}, True, "UnsupportedNonMslProfile"),
                ({"path": "repo", "level": 2, "primaryLanguage": "Rust"}, False, "Warning")):
            args = self.args()
            args.mode = "update"
            args.registry.write_text(json.dumps({"repositories": [entry]}))
            with patch.object(storage, "disk_snapshot", return_value={"freePercent": 50, "freeBytes": 100}), \
                    patch.object(storage, "process_inventory", return_value=set()), \
                    patch.object(storage, "repository_is_dirty", return_value=False), \
                    patch.object(storage, "has_non_msl_justification", return_value=justified), \
                    patch.object(storage, "handle_generic_repository", side_effect=storage.StorageContractError("synthetic failure")):
                self.assertEqual(storage.execute(args), 0)
            report = json.loads(args.report.read_text())
            self.assertEqual(report["repositories"][0]["status"], expected)
            self.assertEqual(report["providers"], [])
        args = self.args()
        args.projects_only = False
        with patch.object(storage, "disk_snapshot", return_value={"freePercent": 50, "freeBytes": 100}), \
                patch.object(storage, "process_inventory", return_value=set()), \
                patch.object(storage, "handle_cache_providers", return_value=[{"provider": "synthetic", "status": "Warning"}]), \
                patch.object(storage, "handle_container_provider", return_value=[]):
            self.assertEqual(storage.execute(args), 0)
        self.assertEqual(json.loads(args.report.read_text())["overallStatus"], "SUCCESS_WITH_WARNINGS")


if __name__ == "__main__":
    unittest.main()
