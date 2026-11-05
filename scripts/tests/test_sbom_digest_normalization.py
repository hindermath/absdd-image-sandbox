"""Test the production digest normalization and rejection boundary."""
from pathlib import Path
import subprocess
import unittest


class DigestTests(unittest.TestCase):
    def test_bash_digest_boundary(self):
        source = (Path(__file__).resolve().parents[1] / "build-and-sbom.sh").read_text()
        boundary = source.split("# Podman versions", 1)[1].split(
            'bash "${script_dir}/check-container-architecture.sh"', 1)[0]
        for value, accepted in (("a" * 64, True), ("sha256:" + "b" * 64, True),
                                ("latest", False), ("a" * 63, False),
                                ("a" * 64 + "\n" + "b" * 64, False)):
            with self.subTest(value=value):
                result = subprocess.run(["bash", "-c",
                    'image_id="$1"; IMAGE_NAME=test; ' + boundary +
                    '\nprintf "%s" "$image_id"', "test", value],
                    text=True, capture_output=True)
                self.assertEqual(result.returncode == 0, accepted, result.stderr)
                if accepted:
                    self.assertTrue(result.stdout.startswith("sha256:"))
