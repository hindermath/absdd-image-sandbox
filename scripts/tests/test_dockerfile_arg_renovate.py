"""Source-bound checks for the Dockerfile ARG and fixed archive-hash policy."""

from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "scripts/check-dockerfile-arg-renovate.py"


class DockerfileArgRenovateTests(unittest.TestCase):
    def run_fixture(self, mutation=None):
        with tempfile.TemporaryDirectory(prefix="ade004-dockerfile-contract-") as directory:
            fixture = Path(directory)
            for relative in (
                "Dockerfile", "renovate.json", "scripts/smoke-test-toolchains.sh",
                "codex/config.toml", "codex/requirements.toml",
            ):
                destination = fixture / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / relative, destination)
            if mutation:
                dockerfile = fixture / "Dockerfile"
                source = dockerfile.read_text(encoding="utf-8")
                pattern, replacement = mutation
                changed, count = re.subn(pattern, replacement, source, count=1)
                self.assertEqual(1, count)
                dockerfile.write_text(changed, encoding="utf-8")
            return subprocess.run(
                ["python3", str(VALIDATOR)], cwd=fixture, capture_output=True,
                text=True, timeout=10,
            )

    def test_current_fixed_hash_contract_passes(self):
        result = self.run_fixture()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_missing_syft_arm64_hash_fails(self):
        result = self.run_fixture((
            r'(arm64\) syft_arch="arm64"; syft_sha256=")[0-9a-f]{64}(")',
            r'\g<1>0\g<2>',
        ))
        self.assertEqual(1, result.returncode)
        self.assertIn("fixed amd64/arm64 SHA-256 verification for Syft", result.stdout)

    def test_missing_uv_amd64_hash_fails(self):
        result = self.run_fixture((
            r'(amd64\) uv_target="x86_64-unknown-linux-gnu"; uv_sha256=")[0-9a-f]{64}(")',
            r'\g<1>0\g<2>',
        ))
        self.assertEqual(1, result.returncode)
        self.assertIn("fixed amd64/arm64 SHA-256 verification for uv", result.stdout)


if __name__ == "__main__":
    unittest.main()
