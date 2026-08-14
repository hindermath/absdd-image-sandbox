#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  agent-prompt [--local|--container] [options] <agent> [--] [prompt...]

Agents:
  codex | claude | opencode | copilot | gemini | agy

Options:
  --cwd DIR             Working directory seen by the agent.
  --prompt-file FILE    Read the prompt from FILE; use - for standard input.
  --agent-arg ARG       Pass one option to the selected agent; repeat as needed.
  --dry-run             Show the command without printing the prompt.
  --podman              Use podman compose for host-to-container execution.
  --podman-compose      Use podman-compose for host-to-container execution.
  --local               Run the installed agent CLI directly.
  --container           Run the image-installed dispatcher in service ade.
  -h, --help            Show this help.

Without prompt arguments or --prompt-file, the prompt is read from standard
input. The repository script defaults to --container. The image sets
ADE_AGENT_PROMPT_TARGET=local, so /usr/local/bin/agent-prompt runs directly.

Examples:
  scripts/agent-prompt.sh codex -- "Review the current changes."
  printf '%s\n' 'Summarize this repository.' | scripts/agent-prompt.sh claude
  scripts/agent-prompt.sh opencode --prompt-file /tmp/task.txt
  agent-prompt --local gemini -- "Explain the active project."
USAGE
}

fail() {
  printf 'agent-prompt: %s\n' "$1" >&2
  exit 2
}

target="${ADE_AGENT_PROMPT_TARGET:-container}"
compose_mode="auto"
agent=""
work_dir=""
prompt_file=""
dry_run=false
agent_args=()
prompt_parts=()

while (($# > 0)); do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    --local)
      target="local"
      ;;
    --container)
      target="container"
      ;;
    --podman)
      compose_mode="podman"
      ;;
    --podman-compose)
      compose_mode="podman-compose"
      ;;
    --cwd)
      (($# >= 2)) || fail "--cwd requires a directory"
      work_dir="$2"
      shift
      ;;
    --prompt-file)
      (($# >= 2)) || fail "--prompt-file requires a file path or -"
      prompt_file="$2"
      shift
      ;;
    --agent-arg)
      (($# >= 2)) || fail "--agent-arg requires one argument"
      agent_args+=("$2")
      shift
      ;;
    --dry-run)
      dry_run=true
      ;;
    --)
      shift
      prompt_parts+=("$@")
      break
      ;;
    -*)
      fail "unknown option: $1"
      ;;
    *)
      if [[ -z "${agent}" ]]; then
        agent="$1"
      else
        prompt_parts+=("$1")
      fi
      ;;
  esac
  shift
done

[[ -n "${agent}" ]] || fail "an agent name is required"
case "${agent}" in
  codex|claude|opencode|copilot|gemini|agy) ;;
  *) fail "unsupported agent '${agent}'" ;;
esac

if [[ -n "${prompt_file}" && ${#prompt_parts[@]} -gt 0 ]]; then
  fail "use either --prompt-file or prompt arguments, not both"
fi

prompt_source="stdin"
if [[ -n "${prompt_file}" ]]; then
  prompt_source="file"
  if [[ "${prompt_file}" == "-" ]]; then
    prompt="$(cat)"
  else
    [[ -f "${prompt_file}" ]] || fail "prompt file not found: ${prompt_file}"
    prompt="$(<"${prompt_file}")"
  fi
elif ((${#prompt_parts[@]} > 0)); then
  prompt_source="argument"
  prompt="${prompt_parts[*]}"
else
  [[ ! -t 0 ]] || fail "provide a prompt argument, --prompt-file, or standard input"
  prompt="$(cat)"
fi

[[ "${prompt}" =~ [^[:space:]] ]] || fail "the prompt must not be empty"

command_args=()
case "${agent}" in
  codex)
    command_args=(codex exec)
    ;;
  claude)
    command_args=(claude)
    ;;
  opencode)
    command_args=(opencode run)
    ;;
  copilot)
    command_args=(copilot)
    ;;
  gemini)
    command_args=(gemini)
    ;;
  agy)
    command_args=(agy)
    ;;
esac
if ((${#agent_args[@]} > 0)); then
  command_args+=("${agent_args[@]}")
fi
case "${agent}" in
  claude|copilot|gemini|agy)
    command_args+=(-p)
    ;;
esac
command_args+=("${prompt}")

print_dry_run() {
  printf 'Target: %s\n' "${target}"
  printf 'Agent: %s\n' "${agent}"
  printf 'Working directory: %s\n' "${work_dir:-<current>}"
  printf 'Prompt source: %s\n' "${prompt_source}"
  printf 'Agent command:'
  local index
  for ((index = 0; index < ${#command_args[@]} - 1; index++)); do
    printf ' %q' "${command_args[index]}"
  done
  printf ' %s\n' '<prompt:redacted>'
}

if [[ "${dry_run}" == true ]]; then
  print_dry_run
  exit 0
fi

if [[ "${target}" == "local" ]]; then
  [[ -z "${work_dir}" || -d "${work_dir}" ]] || fail "working directory not found: ${work_dir}"
  command -v "${command_args[0]}" >/dev/null 2>&1 || fail "agent CLI not found: ${command_args[0]}"
  if [[ "${agent}" == "agy" ]]; then
    printf '%s\n' 'agent-prompt: Antigravity print mode is experimental; review its output and permissions.' >&2
  fi
  if [[ -n "${work_dir}" ]]; then
    cd "${work_dir}"
  fi
  exec "${command_args[@]}"
fi

[[ "${target}" == "container" ]] || fail "ADE_AGENT_PROMPT_TARGET must be local or container"

compose_cmd=()
case "${compose_mode}" in
  podman)
    command -v podman >/dev/null 2>&1 || fail "podman was not found in PATH"
    compose_cmd=(podman compose)
    ;;
  podman-compose)
    command -v podman-compose >/dev/null 2>&1 || fail "podman-compose was not found in PATH"
    compose_cmd=(podman-compose)
    ;;
  auto)
    if command -v podman >/dev/null 2>&1; then
      compose_cmd=(podman compose)
    elif command -v podman-compose >/dev/null 2>&1; then
      compose_cmd=(podman-compose)
    else
      fail "neither podman nor podman-compose was found in PATH"
    fi
    ;;
esac

container_args=(--local)
if [[ -n "${work_dir}" ]]; then
  container_args+=(--cwd "${work_dir}")
fi
if ((${#agent_args[@]} > 0)); then
  for agent_arg in "${agent_args[@]}"; do
    container_args+=(--agent-arg "${agent_arg}")
  done
fi
container_args+=("${agent}")

printf '%s' "${prompt}" | "${compose_cmd[@]}" exec -T ade \
  /usr/local/bin/agent-prompt "${container_args[@]}"
