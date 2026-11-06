#!/usr/bin/env python3
"""Silent authenticated readiness check for the local OpenCode server."""

import base64
import os
import sys
import time
import urllib.error
import urllib.request


def main() -> int:
    password = os.environ.get("OPENCODE_PASSWORD", "")
    if not password:
        return 1
    token = base64.b64encode(f"opencode:{password}".encode()).decode("ascii")
    request = urllib.request.Request(
        "http://127.0.0.1:5199/api/info",
        headers={"Authorization": f"Basic {token}"},
    )
    deadline = time.monotonic() + 45
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return 1
        try:
            with urllib.request.urlopen(request, timeout=min(2, remaining)) as response:
                return 0 if response.status == 200 else 1
        except urllib.error.HTTPError as error:
            if error.code != 503:
                return 1
        except OSError:
            return 1
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return 1
        time.sleep(min(1, remaining))


if __name__ == "__main__":
    sys.exit(main())
