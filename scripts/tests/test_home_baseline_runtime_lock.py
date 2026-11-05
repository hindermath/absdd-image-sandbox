"""Exercise the runtime wrapper's actual jq lock predicate offline."""
import json
from pathlib import Path
import subprocess
import unittest


class RuntimeLockTests(unittest.TestCase):
    def test_supported_and_invalid_locks(self):
        source = (Path(__file__).resolve().parents[1] /
                  "sync-home-baseline-runtime.sh").read_text()
        predicate = source.split("jq -e '", 1)[1].split("'", 1)[0]
        for schema, ref, commit, accepted in (
            (1, None, "a" * 40, True),
            (2, "commit", "a" * 40, True),
            (2, "branch", "a" * 40, False),
            (3, "commit", "a" * 40, False),
            (2, "commit", "main", False),
            (2, "commit", 123, False),
        ):
            with self.subTest(schema=schema, ref=ref, commit=commit):
                result = subprocess.run(
                    ["jq", "-e", predicate], input=json.dumps({
                        "schemaVersion": schema, "refType": ref,
                        "commit": commit}), text=True, capture_output=True)
                self.assertEqual(result.returncode == 0, accepted, result.stderr)
