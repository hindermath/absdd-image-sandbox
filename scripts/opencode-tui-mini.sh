#!/usr/bin/env bash
set -euo pipefail

exec opencode mini --server http://127.0.0.1:5199 "$@"
