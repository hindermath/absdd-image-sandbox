#!/usr/bin/env bash

set -o pipefail

/usr/bin/dotnet "$@" 2> >(
  grep -vF 'An issue was encountered verifying workloads. For more information, run "dotnet workload update".' >&2
)
