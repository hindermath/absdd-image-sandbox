#!/usr/bin/env python3
"""DE: Bind-Mount-Patch pruefen. EN: Verify the container copy patch."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SOURCE = Path(__file__).resolve().parents[2] / "spec-kit/patch-specify-cli.py"
SPEC = importlib.util.spec_from_file_location("container_patch", SOURCE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ContainerPatchTests(unittest.TestCase):
    def verify_layout(self, original: str) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / ".local/share/uv/tools/specify-cli/lib/python3.12/site-packages/specify_cli/__init__.py"
            target.parent.mkdir(parents=True)
            target.write_text(original, encoding="utf-8")
            with patch.object(MODULE.Path, "home", return_value=root):
                MODULE.main()
                first = target.read_bytes()
                MODULE.main()
                self.assertEqual(first, target.read_bytes(), "Patch must be idempotent")
            text = first.decode("utf-8")
            self.assertLess(text.index("# Container patch:"), text.index("import json"))
            compile(text, str(target), "exec")
            # DE: Globales shutil-Patching nur im Kindprozess pruefen.
            # EN: Isolate global shutil mutations in a disposable child process.
            probe = """
import pathlib, shutil, sys
root = pathlib.Path(sys.argv[1])
source = pathlib.Path(sys.argv[2]).read_text()
source = source.split('from .shared_infra import (')[0]
exec(compile(source, '<patched fixture>', 'exec'))
(root / 'input').mkdir()
(root / 'input/data.txt').write_text('bind mount contents')
shutil.copytree(root / 'input', root / 'output')
assert (root / 'output/data.txt').read_text() == 'bind mount contents'
shutil.copy2(root / 'input/data.txt', root / 'copied.txt')
assert (root / 'copied.txt').read_text() == 'bind mount contents'
"""
            result = subprocess.run(
                [sys.executable, "-c", probe, str(root), str(target)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_legacy_layout(self) -> None:
        self.verify_layout("import shutil\nimport json\n")

    def test_split_module_layout(self) -> None:
        self.verify_layout("import os\nimport sys\nimport json\nfrom .shared_infra import (\n    install_shared_infra,\n)\n")

    def test_unknown_layout_is_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / ".local/share/uv/tools/specify-cli/lib/python3.12/site-packages/specify_cli/__init__.py"
            target.parent.mkdir(parents=True)
            target.write_text("import json\n", encoding="utf-8")
            before = target.read_bytes()
            with patch.object(MODULE.Path, "home", return_value=root):
                with self.assertRaises(SystemExit):
                    MODULE.main()
            self.assertEqual(before, target.read_bytes())


if __name__ == "__main__":
    unittest.main()
