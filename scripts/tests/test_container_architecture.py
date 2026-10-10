#!/usr/bin/env python3
"""Architecture guard and lifecycle parity without an engine or emulation."""

import os
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
PWSH = shutil.which("pwsh")
NATIVE = "arm64" if platform.machine().lower() in {"arm64", "aarch64"} else "amd64"


class ArchitectureTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self.log = self.root / "commands"
        self.env = os.environ.copy()
        for key in ("DOCKER_DEFAULT_PLATFORM", "CONTAINER_DEFAULT_PLATFORM"):
            self.env.pop(key, None)
        self.env.update(PATH=f"{self.bin}:{self.env['PATH']}", TEST_LOG=str(self.log),
                        TEST_ARCH=NATIVE, TEST_HOST_ARCH=NATIVE, TEST_OS="Linux",
                        TEST_ENGINE=f"linux/{NATIVE}", TEST_APPLE_ARM="1")
        self.stub("uname", 'if [ "$1" = -s ]; then echo "$TEST_OS"; else echo "$TEST_HOST_ARCH"; fi')
        self.stub("sysctl", 'echo "$TEST_APPLE_ARM"')
        self.stub("podman", r'''
printf '%s\n' "$*" >> "$TEST_LOG"
case "$1" in
  info) echo "$TEST_ENGINE" ;;
  image)
    case "$*" in
      *"{{.Id}}"*) echo fake-image-id ;;
      *) echo "linux/${TEST_IMAGE_ARCH:-$TEST_ARCH}" ;;
    esac ;;
  inspect) echo "${TEST_CONTAINER_IMAGE_ID:-fake-image-id}" ;;
  compose)
    case "$*" in
      *" build "*) exit "${TEST_BUILD_EXIT:-0}" ;;
      *" ps "*) echo fake-container ;;
    esac ;;
  *) exit 9 ;;
esac
''')

    def stub(self, name, body):
        path = self.bin / name
        path.write_text("#!/bin/sh\n" + body + "\n", encoding="utf-8")
        path.chmod(0o755)

    def run_script(self, name, *args, shell="bash"):
        extension = "ps1" if shell == "pwsh" else "sh"
        command = ([PWSH, "-NoLogo", "-NoProfile", "-File"] if shell == "pwsh"
                   else ["/bin/bash"])
        return subprocess.run(command + [str(ROOT / "scripts" / f"{name}.{extension}"), *args],
                              cwd=ROOT, env=self.env, text=True, capture_output=True, check=False,
                              timeout=30)

    def shells(self):
        return ("bash", "pwsh") if PWSH else ("bash",)

    @staticmethod
    def option(shell, bash, powershell):
        return powershell if shell == "pwsh" else bash

    def commands(self):
        return self.log.read_text() if self.log.exists() else ""

    def test_native_and_image_match(self):
        for shell in self.shells():
            with self.subTest(shell=shell):
                result = self.run_script("check-container-architecture",
                                         self.option(shell, "--image", "-ImageName"), "test", shell=shell)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.strip(), f"linux/{NATIVE}")

    def test_bash_normalizes_both_host_architectures(self):
        for architecture, normalized in (("aarch64", "arm64"), ("x86_64", "amd64")):
            self.env.update(TEST_HOST_ARCH=architecture, TEST_ENGINE=f"linux/{normalized}")
            result = self.run_script("check-container-architecture")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), f"linux/{normalized}")

    def test_translated_apple_shell_uses_hardware(self):
        self.env.update(TEST_OS="Darwin", TEST_HOST_ARCH="x86_64", TEST_ENGINE="linux/arm64")
        result = self.run_script("check-container-architecture")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "linux/arm64")

    def test_unknown_host_and_apple_hardware_fail_closed(self):
        self.env["TEST_HOST_ARCH"] = "riscv64"
        self.assertNotEqual(self.run_script("check-container-architecture").returncode, 0)
        self.env.update(TEST_OS="Darwin", TEST_APPLE_ARM="unknown")
        self.assertNotEqual(self.run_script("check-container-architecture").returncode, 0)

    def test_cross_requires_platform_and_approval(self):
        other = "amd64" if NATIVE == "arm64" else "arm64"
        for shell in self.shells():
            target = self.option(shell, "--platform", "-Platform")
            approval = self.option(shell, "--allow-cross-architecture", "-AllowCrossArchitecture")
            with self.subTest(shell=shell):
                self.assertNotEqual(self.run_script("check-container-architecture", target,
                                                    f"linux/{other}", shell=shell).returncode, 0)
                self.assertNotEqual(self.run_script("check-container-architecture", approval,
                                                    shell=shell).returncode, 0)
                result = self.run_script("check-container-architecture", target, f"linux/{other}",
                                         approval, shell=shell)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_engine_image_and_environment_mismatches(self):
        for shell in self.shells():
            for engine in ("linux/riscv64", "windows/amd64", "linux/" + ("amd64" if NATIVE == "arm64" else "arm64")):
                with self.subTest(shell=shell, engine=engine):
                    self.env["TEST_ENGINE"] = engine
                    self.assertNotEqual(self.run_script("check-container-architecture", shell=shell).returncode, 0)
            self.env["TEST_ENGINE"] = f"linux/{NATIVE}"
            self.env["TEST_IMAGE_ARCH"] = "unknown"
            self.assertNotEqual(self.run_script("check-container-architecture",
                                                self.option(shell, "--image", "-ImageName"), "test", shell=shell).returncode, 0)
            del self.env["TEST_IMAGE_ARCH"]
            self.env["DOCKER_DEFAULT_PLATFORM"] = "linux/invalid"
            self.assertNotEqual(self.run_script("check-container-architecture", shell=shell).returncode, 0)
            del self.env["DOCKER_DEFAULT_PLATFORM"]

    def test_failed_preflight_never_builds_or_starts(self):
        self.env["TEST_ENGINE"] = "linux/riscv64"
        for shell in self.shells():
            for action in ("build", "up", "recreate"):
                result = self.run_script("sandbox-lifecycle", action, shell=shell)
                self.assertNotEqual(result.returncode, 0)
            result = self.run_script("build-and-sbom", shell=shell)
            self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("compose", self.commands())
        self.assertNotIn("build --pull", self.commands())

    def test_post_build_mismatch_does_not_start(self):
        self.env["TEST_IMAGE_ARCH"] = "amd64" if NATIVE == "arm64" else "arm64"
        for shell in self.shells():
            with self.subTest(shell=shell):
                result = self.run_script("sandbox-lifecycle", "build", shell=shell)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("build --pull -- ade", self.commands())
                self.assertNotIn(" up ", self.commands())

    def test_failed_build_blocks_post_build_and_start(self):
        self.env["TEST_BUILD_EXIT"] = "7"
        for shell in self.shells():
            result = self.run_script("sandbox-lifecycle", "build", shell=shell)
            self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("image inspect", self.commands())
        self.assertNotIn(" up ", self.commands())

    def test_wrong_image_blocks_up_and_skip_build_sbom(self):
        self.env["TEST_IMAGE_ARCH"] = "amd64" if NATIVE == "arm64" else "arm64"
        for shell in self.shells():
            result = self.run_script("sandbox-lifecycle", "up", shell=shell)
            self.assertNotEqual(result.returncode, 0)
            result = self.run_script("build-and-sbom", self.option(shell, "--skip-build", "-SkipBuild"), shell=shell)
            self.assertNotEqual(result.returncode, 0)
        self.assertNotIn(" up ", self.commands())
        self.assertNotIn("run --rm", self.commands())

    def test_plain_up_retains_writable_layer(self):
        for shell in self.shells():
            with self.subTest(shell=shell):
                result = self.run_script("sandbox-lifecycle", "up", shell=shell)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("--no-recreate", self.commands())
                self.assertNotIn("--force-recreate", self.commands())
                self.assertNotIn("--renew-anon-volumes", self.commands())

    def test_outdated_container_does_not_start(self):
        self.env["TEST_CONTAINER_IMAGE_ID"] = "old-image-id"
        for shell in self.shells():
            result = self.run_script("sandbox-lifecycle", "up", shell=shell)
            self.assertNotEqual(result.returncode, 0)
        self.assertNotIn(" up ", self.commands())

    def test_dry_run_is_read_only(self):
        for shell in self.shells():
            result = self.run_script("build-and-sbom", self.option(shell, "--dry-run", "-WhatIf"), shell=shell)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("build --pull", self.commands())
        self.assertNotIn("run --rm", self.commands())


if __name__ == "__main__":
    unittest.main()
