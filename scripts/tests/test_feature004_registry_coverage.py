"""Synthetic Linux registry/result branches; no installation or maintenance.

DE: Nur temporaere Dateien. EN: Temporary files and explicitly blocked spawning.
"""
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch


PATH = Path(__file__).resolve().parents[1] / "lib/linux-maintenance-hardening.py"
SPEC = importlib.util.spec_from_file_location("registry_coverage", PATH)
helper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(helper)


class RegistryCoverageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="ade004-registry-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.data = self.root / "data.json"
        self.rows = self.root / "rows.tsv"
        self.output = self.root / "result.json"
        self.enterContext(patch.object(helper.subprocess, "Popen",
            side_effect=AssertionError("No real probe/installer in registry fixtures")))
        self.enterContext(patch("sys.stdout", new_callable=io.StringIO))

    def write(self, value):
        self.data.write_text(json.dumps(value), encoding="utf-8")
        return self.data

    def test_os_release_and_json_reject_invalid_missing_and_non_objects(self):
        for text in ("ID=ubuntu\nVERSION_ID=24.04", "# ignored\n\nID='Ubuntu'\nVERSION_ID=\"24.04\"\nignored"):
            self.data.write_text(text)
            self.assertEqual(helper.parse_os_release(self.data), ("ubuntu", "24.04"))
        for text in ("ID=bad value\nVERSION_ID=24.04", "ID=ubuntu\nVERSION_ID=24", "ID=ubuntu"):
            self.data.write_text(text)
            with self.assertRaises(helper.ContractError):
                helper.parse_os_release(self.data)
        for value in ([], None, "text"):
            with self.subTest(value=value), self.assertRaises(helper.ContractError):
                helper.load_json(self.write(value))
        self.data.write_bytes(b"\xff")
        for function in (helper.load_json, helper.parse_os_release):
            with self.assertRaises(helper.ContractError):
                function(self.data)
        self.data.unlink()
        with self.assertRaises(helper.ContractError):
            helper.load_json(self.data)

    def test_result_classification_nonfile_read_error_malformed_and_schema(self):
        self.assertEqual(helper.classify_toolchain_result(self.root)[1], "ResultNotFile")
        self.data.write_text("{}")
        with patch.object(Path, "read_bytes", side_effect=PermissionError):
            self.assertEqual(helper.classify_toolchain_result(self.data)[1], "ResultUnreadable")
        for payload, expected in ((b"{broken}", "ResultMalformed"), (b"[]", "ResultSchemaMismatch")):
            self.data.write_bytes(payload)
            self.assertEqual(helper.classify_toolchain_result(self.data)[1], expected)
        valid = {"schemaVersion": "1.0", "platform": "Linux", "mode": "dry-run",
            "overallStatus": "SUCCESS", "exitCode": 0, "items": [],
            "remainingRequired": [], "optionalDrift": [], "nextAction": "N/A"}
        for status, code in (("SUCCESS", 0), ("SUCCESS_WITH_WARNINGS", 0), ("PARTIAL", 1), ("FAILED", 2)):
            value = {**valid, "overallStatus": status, "exitCode": code}
            self.assertEqual(helper.inspect_toolchain_result(self.write(value)), 0)
            value["exitCode"] = 99
            self.assertEqual(helper.inspect_toolchain_result(self.write(value)), 2)
        for update in ({"remainingRequired": [1]}, {"optionalDrift": [False]}, {"platform": "Other"}):
            self.assertEqual(helper.classify_toolchain_result(self.write({**valid, **update}))[1],
                             "ResultSchemaMismatch")

    def test_failure_result_rejects_invalid_class_platform_and_mode(self):
        for platform, mode, category in (("Other", "update", "ProducerFailed"),
                ("Linux", "unknown", "ProducerFailed"), ("Linux", "update", "arbitrary/path")):
            with self.subTest(category=category), self.assertRaises(helper.ContractError):
                helper.toolchain_result_failure(self.output, platform, mode, category)
            self.assertFalse(self.output.exists())

    def test_swift_contract_mutations_and_exact_artifact_integrity(self):
        os_release = self.root / "os-release"
        os_release.write_text("ID=ubuntu\nVERSION_ID=24.04\n")
        linux = {"swiftlyVersion": "1.1.0", "swiftVersion": "6.4.1",
            "profiles": {"ubuntu:24.04": "ubuntu2404"},
            "artifacts": {"aarch64": {"url": "https://download.swift.org/fixture.tar.gz",
                                      "sha256": "a" * 64}}}
        valid = {"tools": [{"id": "swift", "install": {"manager": "swiftly", "linux": linux}}]}
        mutations = [{}, {"tools": []}, {"tools": valid["tools"] * 2},
            {"tools": [{"id": "swift"}]},
            {"tools": [{"id": "swift", "install": {"manager": "apt"}}]},
            {"tools": [{"id": "swift", "install": {"manager": "swiftly"}}]}]
        for field, value in (("swiftlyVersion", "latest"), ("swiftVersion", "6.4-beta"),
                ("artifacts", {"aarch64": {"url": "http://other.invalid", "sha256": "a" * 64}})):
            altered = copy.deepcopy(valid)
            altered["tools"][0]["install"]["linux"][field] = value
            mutations.append(altered)
        for value in mutations:
            with self.subTest(value=value), self.assertRaises(helper.ContractError):
                helper.resolve_swift_contract(self.write(value), os_release, "arm64")
        self.assertEqual(helper.resolve_swift_contract(self.write(valid), os_release, "arm64")[1], 0)
        self.assertEqual(helper.resolve_swift_contract(self.data, os_release, "unsupported")[1], 1)
        artifact = self.root / "artifact"
        artifact.write_bytes(b"synthetic binary")
        digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
        self.assertEqual(helper.verify_sha256(artifact, digest)[1], 0)
        self.assertEqual(helper.verify_sha256(artifact, "0" * 64)[1], 1)
        for path, expected in ((artifact, "invalid"), (self.root / "missing", digest)):
            with self.assertRaises(helper.ContractError):
                helper.verify_sha256(path, expected)

    def test_swiftly_archive_only_extracts_regular_binary_and_rejects_duplicates(self):
        archive = self.root / "fixture.tar.gz"
        for names, valid in ((["../swiftly"], True), (["swiftly", "nested/swiftly"], False),
                             (["unrelated"], False)):
            with tarfile.open(archive, "w:gz") as bundle:
                for name in names:
                    item = tarfile.TarInfo(name)
                    item.size = 3
                    bundle.addfile(item, io.BytesIO(b"bin"))
            if valid:
                self.assertEqual(helper.extract_swiftly(archive, self.output)[1], 0)
                self.assertEqual(self.output.read_bytes(), b"bin")
                self.assertEqual(self.output.stat().st_mode & 0o777, 0o755)
                self.assertEqual({p.name for p in self.root.iterdir()},
                                 {"fixture.tar.gz", "result.json"})
            else:
                with self.assertRaises(helper.ContractError):
                    helper.extract_swiftly(archive, self.output)
        archive.write_bytes(b"not gzip")
        with self.assertRaises(helper.ContractError):
            helper.extract_swiftly(archive, self.output)

    def test_result_rows_all_rejections_and_sorting(self):
        row = ["1", "cli", "fixture", "required", "true", "Installed", "Available", "safe", "N/A"]
        for index, value in ((0, "bad"), (0, "0"), (1, "bad kind"), (2, "bad id"),
                (3, "other"), (4, "yes"), (5, "bad"), (6, "bad")):
            fields = row.copy()
            fields[index] = value
            self.rows.write_text("\t".join(fields) + "\n")
            with self.subTest(index=index), self.assertRaises(helper.ContractError):
                helper.parse_result_rows(self.rows)
        text = "\t".join(row) + "\n"
        for value in ("short\n", text * 2, text.replace("1\t", "2\t", 1),
                      text + text.replace("1\t", "2\t", 1)):
            self.rows.write_text(value)
            with self.assertRaises(helper.ContractError):
                helper.parse_result_rows(self.rows)
        second = ["2", "cli", "other", "optional", "false", "Planned", "N/A", "safe", "N/A"]
        self.rows.write_text("\t".join(second) + "\n" + text)
        self.assertEqual([item["sequence"] for item in helper.parse_result_rows(self.rows)], [1, 2])
        self.rows.unlink()
        with self.assertRaises(helper.ContractError):
            helper.parse_result_rows(self.rows)

    def test_summary_required_optional_and_success_outputs(self):
        for scope, status, expected, code in (("required", "Failed", "PARTIAL", 1),
                ("optional", "StillMissing", "SUCCESS_WITH_WARNINGS", 0),
                ("required", "Present", "SUCCESS", 0)):
            self.rows.write_text(f"1\tcli\tfixture\t{scope}\tfalse\t{status}\tN/A\tsafe\tN/A\n")
            self.assertEqual(helper.summarize_results(self.rows, self.output, "Linux", "dry-run"), code)
            self.assertEqual(json.loads(self.output.read_text())["overallStatus"], expected)
        for platform, mode in (("Other", "dry-run"), ("Linux", "bad")):
            with self.assertRaises(helper.ContractError):
                helper.summarize_results(self.rows, self.output, platform, mode)

    def test_snapshot_fail_closed_fields_roots_records_and_install_metadata(self):
        paths = [self.root / name for name in ("brew.json", "cli.json", "npm.json")]
        for path in paths:
            path.write_text("{}")
        for index, value in ((0, []), (0, {"formulae": ["bad"]}),
                (0, {"aptFallback": []}), (0, {"formulae": [{"name": "bad\tfield"}]}),
                (1, {"tools": [{"id": "fixture", "platforms": ["Linux"], "install": []}]})):
            paths[index].write_text(json.dumps(value))
            with self.subTest(index=index, value=value), self.assertRaises(helper.ContractError):
                helper.snapshot_registries(self.root / "snapshot", *paths, "Linux", None)
            paths[index].write_text("{}")
        paths[0].write_bytes(b"\xff")
        with self.assertRaises(helper.ContractError):
            helper.snapshot_registries(self.root / "snapshot", *paths, "Linux", None)

    def test_small_validation_and_bounded_probe_rejections_do_not_spawn(self):
        for command, timeout, limit in (([], 1, 128), (["fixture"], .01, 128),
                                         (["fixture"], 1, 12)):
            with self.assertRaises(helper.ContractError):
                helper.bounded_probe("fixture", command, timeout, limit, [])
        self.assertEqual(helper.sanitize("abc" * 100, [], 10), "abcabcabca\u2026")
        self.assertEqual(helper.sanitize("\x00\r", []), "N/A")
        for exc, expected in ((FileNotFoundError(), "Missing"), (PermissionError("fixture"), "Unusable")):
            with patch.object(helper.subprocess, "Popen", side_effect=exc):
                result, code = helper.bounded_probe("fixture", ["fake"], 1, 128, [])
            self.assertEqual(result["status"], expected)
            self.assertEqual(code, 1)
        with self.assertRaises(SystemExit) as raised:
            helper.fail("synthetic invalid input")
        self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
