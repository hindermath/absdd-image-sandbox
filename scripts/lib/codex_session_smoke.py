#!/usr/bin/env python3
"""Start one local Codex session, without starting a turn or model request."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import queue
import subprocess
import tempfile
import threading
import time


def start_session(cwd: Path, timeout: float = 45) -> None:
    """Require initialize and thread/start success; always reap the server."""
    with tempfile.TemporaryFile(mode="w+") as errors:
        process = subprocess.Popen(
            ["codex", "app-server", "--strict-config"], stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=errors, text=True, start_new_session=True)
        rows: queue.Queue = queue.Queue()
        def read_rows():
            for line in process.stdout:
                try:
                    rows.put(json.loads(line))
                except ValueError:
                    rows.put({"error": "Invalid app-server JSON"})
            rows.put(None)
        reader = threading.Thread(target=read_rows, daemon=True)
        reader.start()
        deadline = time.monotonic() + timeout
        def send(message):
            process.stdin.write(json.dumps(message) + "\n")
            process.stdin.flush()
        def request(identifier, method, params):
            send({"id": identifier, "method": method, "params": params})
            while True:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise RuntimeError("Codex session startup timed out")
                try:
                    row = rows.get(timeout=remaining)
                except queue.Empty as exc:
                    raise RuntimeError("Codex session startup timed out") from exc
                if row is None:
                    raise RuntimeError("Codex app server ended during startup")
                if row.get("id") != identifier:
                    continue
                if "error" in row:
                    # Do not dump session content or server stderr into smoke output.
                    raise RuntimeError(f"Codex {method} failed")
                if not isinstance(row.get("result"), dict):
                    raise RuntimeError(f"Codex {method} returned no result object")
                return row["result"]
        try:
            request(1, "initialize", {"clientInfo": {
                "name": "ade-offline-smoke", "version": "1.0"}})
            send({"method": "initialized"})
            result = request(2, "thread/start", {"cwd": str(cwd), "ephemeral": True})
            if not isinstance(result.get("thread"), dict) or not result["thread"].get("id"):
                raise RuntimeError("Codex thread/start returned no thread")
            sandbox = result.get("sandbox", {})
            if (sandbox.get("type") != "workspaceWrite" or sandbox.get("networkAccess") is not False
                    or sandbox.get("excludeSlashTmp") is not True
                    or result.get("approvalPolicy") != "on-request"):
                raise RuntimeError("Codex session does not retain the image sandbox defaults")
            instructions = cwd / "AGENTS.md"
            if instructions.is_file() and str(instructions) not in json.dumps(result.get("instructionSources", [])):
                raise RuntimeError("Codex session did not report the AGENTS.md fixture")
        finally:
            # A separate process group also covers local daemon/helper children.
            import signal
            try:
                os.killpg(process.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait(timeout=5)
            # The parent can exit before a helper; reap the remaining group too.
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.stdin.close()
            reader.join(timeout=2)
            process.stdout.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cwd", type=Path)
    args = parser.parse_args()
    try:
        if args.cwd:
            start_session(args.cwd.resolve(strict=True))
        else:
            root = Path.home() / "smoke-tests"
            root.mkdir(exist_ok=True)
            with tempfile.TemporaryDirectory(prefix="codex-session-", dir=root) as directory:
                cwd = Path(directory)
                (cwd / "AGENTS.md").write_text(
                    "# Offline startup fixture\nRead local instructions. Do not call a model.\n")
                start_session(cwd)
        print("PASS: Codex local session and AGENTS.md sandbox startup; no model turn.")
        return 0
    except (OSError, RuntimeError) as exc:
        print(f"FAIL: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
