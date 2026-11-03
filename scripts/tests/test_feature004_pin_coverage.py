"""Measured pin-validator and patcher gaps; mutate owned copies only."""

import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PINS = load("feature004_pin_coverage", "scripts/check-toolchain-pins.py")
PATCHER = load("feature004_patch_coverage", "spec-kit/patch-specify-cli.py")


class PinValidationCoverageTests(unittest.TestCase):
    def check_mutation(self, relative, mutate, expected):
        with tempfile.TemporaryDirectory(prefix="ade004-pin-negative-") as directory:
            root = Path(directory)
            for path in ("Dockerfile", "scripts/config/toolchain-pins.json", "scripts/smoke-test-toolchains.sh",
                         "codex/config.toml", "codex/requirements.toml"):
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / path, target)
            target = root / relative
            before = target.read_text(encoding="utf-8")
            after = mutate(before)
            self.assertNotEqual(before, after, "Fixture mutation must change input")
            target.write_text(after, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/check-toolchain-pins.py")],
                cwd=root, capture_output=True, text=True, timeout=10,
            )
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn(expected, result.stdout)

    def remove_package(self, text, package):
        config = json.loads(text)
        config["pins"] = [pin for pin in config["pins"] if pin.get("package") != package]
        return json.dumps(config)

    def test_each_metadata_failure_is_rejected(self):
        cases = (
            (lambda text: "ARG FIXTURE_FIRST=1\n" + text, "ARG FIXTURE_FIRST has no metadata line"),
            (lambda text: text + "\nARG FIXTURE_NO_META=1\n", "ARG FIXTURE_NO_META is missing"),
            (lambda text: text + "\n# toolchain-pin: argName=OTHER\n"
             "ARG FIXTURE_WRONG=1\n", "ARG FIXTURE_WRONG metadata uses argName=OTHER"),
        )
        for mutate, expected in cases:
            with self.subTest(expected=expected):
                self.check_mutation("Dockerfile", mutate, expected)

    def test_each_required_agent_guard_is_rejected_independently(self):
        for arg, (package, marker, version) in PINS.REQUIRED_AGENT_CLIS.items():
            cases = (
                ("Dockerfile", lambda text, arg=arg: re.sub(rf"(?m)^ARG {arg}=.*\n", "", text),
                 f"required agent ARG missing: {arg}"),
                ("Dockerfile", lambda text, marker=marker: text.replace(marker, "fixture-removed"),
                 f"Dockerfile does not install {package}"),
                ("scripts/config/toolchain-pins.json", lambda text, package=package: self.remove_package(text, package),
                 f"Pin registry agent CLI group is missing {package}"),
                ("scripts/smoke-test-toolchains.sh",
                 lambda text, version=version: text.replace(version, "fixture-removed"),
                 f"smoke test is missing: {version}"),
            )
            for relative, mutate, expected in cases:
                with self.subTest(arg=arg, expected=expected):
                    self.check_mutation(relative, mutate, expected)

    def test_each_required_operational_guard_is_rejected_independently(self):
        for arg, (package, marker, version) in PINS.REQUIRED_OPERATIONAL_TOOLS.items():
            cases = (
                ("Dockerfile", lambda text, arg=arg: re.sub(rf"(?m)^ARG {arg}=.*\n", "", text),
                 f"required operational ARG missing: {arg}"),
                ("Dockerfile", lambda text, marker=marker: text.replace(marker, "fixture-removed"),
                 f"Dockerfile does not install {package}"),
                ("scripts/smoke-test-toolchains.sh",
                 lambda text, version=version: text.replace(version, "fixture-removed"),
                 f"smoke test is missing: {version}"),
            )
            for relative, mutate, expected in cases:
                with self.subTest(arg=arg, expected=expected):
                    self.check_mutation(relative, mutate, expected)

    def test_codex_and_supply_chain_guards_are_rejected_independently(self):
        cases = (
            ("Dockerfile", lambda text: text.replace("scripts/codex-bwrap-wrapper.sh", "fixture-removed"),
             "Codex rootless adapter is not installed"),
            ("Dockerfile", lambda text: text.replace("/home/adedev/codex-workspace/.git", "fixture-removed"),
             "Codex transaction workspace is not prepared"),
            ("Dockerfile", lambda text: text + "\n# /etc/codex/managed_config.toml\n", "legacy Codex managed_config"),
            ("codex/config.toml", lambda text: text.replace('approval_policy = "untrusted"', 'approval_policy = "never"'),
             "Codex interactive default must remain untrusted"),
            ("codex/requirements.toml", lambda text: text.replace('"untrusted"', '"fixture-removed"'),
             "Codex requirements must support interactive and headless approval modes"),
            ("Dockerfile", lambda text: re.sub(r"(?m)^ARG SYFT_VERSION=.*\n", "", text),
             "required SBOM tool ARG missing: SYFT_VERSION"),
            ("scripts/config/toolchain-pins.json", lambda text: self.remove_package(text, "anchore/syft"),
             "Pin registry supply-chain group is missing anchore/syft"),
            ("scripts/smoke-test-toolchains.sh", lambda text: text.replace("syft version", "fixture-removed"),
             "smoke test is missing: syft version"),
            ("Dockerfile", lambda text: re.sub(r"(?m)^ARG POWERSHELL_VERSION=.*\n", "", text),
             "required scripting tool ARG missing: POWERSHELL_VERSION"),
            ("scripts/config/toolchain-pins.json", lambda text: self.remove_package(text, "PowerShell/PowerShell"),
             "Pin registry scripting tool group is missing PowerShell/PowerShell"),
            ("Dockerfile", lambda text: text.replace("pwsh -NoLogo -NoProfile", "fixture-removed"),
             "Dockerfile does not verify the bundled PowerShell version"),
            ("scripts/smoke-test-toolchains.sh", lambda text: text.replace("pwsh --version", "fixture-removed"),
             "smoke test is missing: pwsh --version"),
        )
        for relative, mutate, expected in cases:
            with self.subTest(expected=expected):
                self.check_mutation(relative, mutate, expected)

    def test_architecture_hash_guards_reject_each_missing_digest(self):
        for variable, expected in (("actionlint_sha256", "hashes for actionlint"),
                                   ("dotnet_sha512", "hashes for .NET compatibility SDK")):
            with self.subTest(variable=variable):
                self.check_mutation("Dockerfile", lambda text, variable=variable:
                                    re.sub(rf'{variable}="[0-9a-f]+"', f'{variable}="0"', text), expected)


class SpecifyPatchCoverageTests(unittest.TestCase):
    def target(self, root, content):
        target = root / ".local/share/uv/tools/specify-cli/lib/python3.15/site-packages/specify_cli/__init__.py"
        target.parent.mkdir(parents=True)
        target.write_text(content, encoding="utf-8")
        return target

    def test_missing_target_and_unterminated_patch_fail_without_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with mock.patch.object(PATCHER.Path, "home", return_value=root):
                with self.assertRaisesRegex(SystemExit, "not found"):
                    PATCHER.main()
                target = self.target(root, "import shutil\n# Container patch: Windows/WSL bind mounts\nold = True\n")
                before = target.read_bytes()
                with self.assertRaisesRegex(SystemExit, "end not found"):
                    PATCHER.main()
                self.assertEqual(before, target.read_bytes())

    def test_old_patch_is_replaced_with_and_without_footer(self):
        for footer in ("# End container copy patch.\n", ""):
            with self.subTest(footer=bool(footer)), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                target = self.target(root, "import shutil\n# Container patch: Windows/WSL bind mounts\n"
                                     "old = True\n" + footer + "import json\n")
                with mock.patch.object(PATCHER.Path, "home", return_value=root):
                    PATCHER.main()
                    first = target.read_bytes()
                    PATCHER.main()
                self.assertEqual(first, target.read_bytes())
                self.assertNotIn("old = True", first.decode())
                compile(first, str(target), "exec")

    def test_duplicate_import_anchor_is_rejected_and_cli_uses_synthetic_home(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = "from .shared_infra import (\n)\n" * 2
            target = self.target(root, original)
            with mock.patch.object(PATCHER.Path, "home", return_value=root):
                with self.assertRaisesRegex(SystemExit, "anchor not found"):
                    PATCHER.main()
            self.assertEqual(target.read_text(), original)
            target.write_text("import shutil\nimport json\n", encoding="utf-8")
            # Windows Path.home prefers USERPROFILE; isolate both host variants.
            result = subprocess.run([sys.executable, str(ROOT / "spec-kit/patch-specify-cli.py")],
                                    env={**os.environ, "HOME": str(root), "USERPROFILE": str(root)}, capture_output=True,
                                    text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("_container_copytree_no_metadata", target.read_text())


if __name__ == "__main__":
    unittest.main()
