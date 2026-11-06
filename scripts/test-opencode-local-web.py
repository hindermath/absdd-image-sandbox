#!/usr/bin/env python3
"""Offline-safe HTTP check for the running local OpenCode server."""

import base64
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

URL = "http://127.0.0.1:5199/api/info"


def status(password: str | None) -> int:
    headers = {}
    if password is not None:
        token = base64.b64encode(f"opencode:{password}".encode()).decode("ascii")
        headers["Authorization"] = f"Basic {token}"
    request = urllib.request.Request(URL, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=2) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code


def main() -> int:
    password = os.environ.get("OPENCODE_PASSWORD", "")
    if len(password) < 16:
        print("Set a synthetic OPENCODE_PASSWORD of at least 16 characters.", file=sys.stderr)
        return 2
    deadline = time.monotonic() + 45
    while True:
        try:
            observed = status(password)
        except OSError:
            observed = 503
        if observed == 200:
            break
        if observed != 503 or time.monotonic() >= deadline:
            print(f"Authenticated readiness failed: HTTP {observed}.", file=sys.stderr)
            return 1
        time.sleep(1)
    if status(None) != 401 or status(password + "-wrong") != 401:
        print("Unauthenticated or incorrect credentials bypassed the gate.", file=sys.stderr)
        return 1
    health = subprocess.run(
        ["/usr/local/bin/healthcheck-opencode-web"],
        capture_output=True,
        check=False,
    )
    if health.returncode or health.stdout or health.stderr:
        print("Authenticated healthcheck failed or produced output.", file=sys.stderr)
        return 1
    print("OpenCode authentication and readiness passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
