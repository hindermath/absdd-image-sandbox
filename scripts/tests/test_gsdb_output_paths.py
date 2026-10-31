#!/usr/bin/env python3
"""Reject GSDB output aliases using disposable repositories only."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]


class GsdbOutputPathsTests(unittest.TestCase):
    def run_checker(self, shell: str, repository: Path) -> subprocess.CompletedProcess[str]:
        if shell == "bash":
            command = ["bash", str(ROOT / "scripts/check-gsdb-self-assessment.sh"),
                       "--repo", str(repository), "--preset-profile", "none"]
        else:
            command = ["pwsh", "-NoProfile", "-File",
                       str(ROOT / "scripts/check-gsdb-self-assessment.ps1"),
                       "-Repo", str(repository), "-PresetProfile", "none"]
        return subprocess.run(command, capture_output=True, text=True, timeout=40)

    def test_symlink_outputs_do_not_escape_repository(self):
        if not hasattr(os, "symlink"):
            self.skipTest("symlinks unavailable")
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            for output in ("docs", "docs/security", "docs/security/gsdb-self-assessment.md",
                           "Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md",
                           "Lastenheft_Abarbeitungsreihenfolge.md"):
                with self.subTest(shell=shell, output=output), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    repository = root / "repo"
                    repository.mkdir()
                    subprocess.run(["git", "init", "-q", str(repository)], check=True,
                                   capture_output=True, text=True)
                    external = root / "outside"
                    external.mkdir()
                    sentinel = external / "sentinel.txt"
                    sentinel.write_text("keep", encoding="utf-8")
                    link = repository / output
                    link.parent.mkdir(parents=True, exist_ok=True)
                    target = external if output in ("docs", "docs/security") else sentinel
                    link.symlink_to(target, target_is_directory=target.is_dir())

                    result = self.run_checker(shell, repository)

                    self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
                    self.assertEqual("keep", sentinel.read_text(encoding="utf-8"))
                    self.assertEqual(["sentinel.txt"], sorted(path.name for path in external.iterdir()))
                    self.assertFalse((repository / "Lastenheft_Abarbeitungsreihenfolge.md").is_file()
                                     if output != "Lastenheft_Abarbeitungsreihenfolge.md" else False)

    def test_normal_repository_writes_only_its_three_outputs(self):
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                repository = Path(temporary) / "repo"
                repository.mkdir()
                subprocess.run(["git", "init", "-q", str(repository)], check=True,
                               capture_output=True, text=True)
                result = self.run_checker(shell, repository)
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                for relative in ("docs/security/gsdb-self-assessment.md",
                                 "Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md",
                                 "Lastenheft_Abarbeitungsreihenfolge.md"):
                    self.assertTrue((repository / relative).is_file(), relative)

    def test_shared_bash_prepare_propagates_unsafe_order_path(self):
        if not shutil.which("bash"):
            self.skipTest("Bash unavailable")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repository = root / "repo"
            repository.mkdir()
            subprocess.run(["git", "init", "-q", str(repository)], check=True,
                           capture_output=True, text=True)
            sentinel = root / "outside.md"
            sentinel.write_text("keep", encoding="utf-8")
            (repository / "Lastenheft_Abarbeitungsreihenfolge.md").symlink_to(sentinel)
            library = ROOT / "scripts/lib/secure-development-hardening.sh"
            script = ('source "$1"; sdh_prepare_repo "$2" fixture Python 0 0 "$3"; '
                      'rc=$?; printf "result=%s\\n" "$SDH_PREPARE_RESULT"; exit "$rc"')
            result = subprocess.run(["bash", "-c", script, "bash", str(library),
                                     str(repository), str(ROOT / "scripts")],
                                    capture_output=True, text=True, timeout=20)
            self.assertNotEqual(0, result.returncode)
            self.assertIn("result=error", result.stdout)
            self.assertEqual("keep", sentinel.read_text(encoding="utf-8"))
            self.assertFalse((repository / "docs").exists())


if __name__ == "__main__":
    unittest.main()
