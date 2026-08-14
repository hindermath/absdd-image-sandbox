$ErrorActionPreference = 'Stop'

function Show-Usage {
    @'
Usage:
  agent-prompt.ps1 [--local|--container] [options] <agent> [--] [prompt...]

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
ADE_AGENT_PROMPT_TARGET=local, so /usr/local/bin/agent-prompt.ps1 runs directly.

Examples:
  pwsh -NoProfile -File scripts/agent-prompt.ps1 codex -- 'Review the current changes.'
  'Summarize this repository.' | pwsh -NoProfile -File scripts/agent-prompt.ps1 claude
  pwsh -NoProfile -File scripts/agent-prompt.ps1 opencode --prompt-file ./task.txt
  pwsh -NoProfile -File /usr/local/bin/agent-prompt.ps1 --local gemini -- 'Explain the active project.'
'@
}

function Write-AgentPromptFailure {
    param([Parameter(Mandatory)][string] $Message)

    [Console]::Error.WriteLine("agent-prompt: ${Message}")
    exit 2
}

$target = if ($env:ADE_AGENT_PROMPT_TARGET) { $env:ADE_AGENT_PROMPT_TARGET } else { 'container' }
$composeMode = 'auto'
$agent = ''
$workDir = ''
$promptFile = ''
$dryRun = $false
$agentArguments = [System.Collections.Generic.List[string]]::new()
$promptParts = [System.Collections.Generic.List[string]]::new()
$inputArguments = @($args)

for ($index = 0; $index -lt $inputArguments.Count; $index++) {
    $current = $inputArguments[$index]
    switch ($current) {
        { $_ -in @('-h', '--help') } {
            Show-Usage
            exit 0
        }
        '--local' { $target = 'local'; continue }
        '--container' { $target = 'container'; continue }
        '--podman' { $composeMode = 'podman'; continue }
        '--podman-compose' { $composeMode = 'podman-compose'; continue }
        '--cwd' {
            if (++$index -ge $inputArguments.Count) { Write-AgentPromptFailure '--cwd requires a directory' }
            $workDir = $inputArguments[$index]
            continue
        }
        '--prompt-file' {
            if (++$index -ge $inputArguments.Count) { Write-AgentPromptFailure '--prompt-file requires a file path or -' }
            $promptFile = $inputArguments[$index]
            continue
        }
        '--agent-arg' {
            if (++$index -ge $inputArguments.Count) { Write-AgentPromptFailure '--agent-arg requires one argument' }
            $agentArguments.Add($inputArguments[$index])
            continue
        }
        '--dry-run' { $dryRun = $true; continue }
        '--' {
            for ($promptIndex = $index + 1; $promptIndex -lt $inputArguments.Count; $promptIndex++) {
                $promptParts.Add($inputArguments[$promptIndex])
            }
            $index = $inputArguments.Count
            continue
        }
        default {
            if ($current.StartsWith('-')) { Write-AgentPromptFailure "unknown option: ${current}" }
            if (-not $agent) {
                $agent = $current
            } else {
                $promptParts.Add($current)
            }
        }
    }
}

if (-not $agent) { Write-AgentPromptFailure 'an agent name is required' }
$supportedAgents = @('codex', 'claude', 'opencode', 'copilot', 'gemini', 'agy')
if ($agent -notin $supportedAgents) { Write-AgentPromptFailure "unsupported agent '${agent}'" }
if ($promptFile -and $promptParts.Count -gt 0) {
    Write-AgentPromptFailure 'use either --prompt-file or prompt arguments, not both'
}

$promptSource = 'stdin'
if ($promptFile) {
    $promptSource = 'file'
    if ($promptFile -eq '-') {
        $promptText = [Console]::In.ReadToEnd()
    } else {
        if (-not (Test-Path -LiteralPath $promptFile -PathType Leaf)) {
            Write-AgentPromptFailure "prompt file not found: ${promptFile}"
        }
        $promptText = Get-Content -LiteralPath $promptFile -Raw
    }
} elseif ($promptParts.Count -gt 0) {
    $promptSource = 'argument'
    $promptText = $promptParts -join ' '
} else {
    if (-not [Console]::IsInputRedirected) {
        Write-AgentPromptFailure 'provide a prompt argument, --prompt-file, or standard input'
    }
    $promptText = [Console]::In.ReadToEnd()
}

if ([string]::IsNullOrWhiteSpace($promptText)) { Write-AgentPromptFailure 'the prompt must not be empty' }

switch ($agent) {
    'codex' { $agentCommand = 'codex'; $commandArguments = @('exec') + $agentArguments + @($promptText) }
    'claude' { $agentCommand = 'claude'; $commandArguments = @($agentArguments) + @('-p', $promptText) }
    'opencode' { $agentCommand = 'opencode'; $commandArguments = @('run') + $agentArguments + @($promptText) }
    'copilot' { $agentCommand = 'copilot'; $commandArguments = @($agentArguments) + @('-p', $promptText) }
    'gemini' { $agentCommand = 'gemini'; $commandArguments = @($agentArguments) + @('-p', $promptText) }
    'agy' { $agentCommand = 'agy'; $commandArguments = @($agentArguments) + @('-p', $promptText) }
}

if ($dryRun) {
    Write-Output "Target: ${target}"
    Write-Output "Agent: ${agent}"
    Write-Output "Working directory: $(if ($workDir) { $workDir } else { '<current>' })"
    Write-Output "Prompt source: ${promptSource}"
    $visibleArguments = @($commandArguments[0..([Math]::Max(0, $commandArguments.Count - 2))])
    Write-Output "Agent command: ${agentCommand} $($visibleArguments -join ' ') <prompt:redacted>"
    exit 0
}

if ($target -eq 'local') {
    if ($workDir -and -not (Test-Path -LiteralPath $workDir -PathType Container)) {
        Write-AgentPromptFailure "working directory not found: ${workDir}"
    }
    if (-not (Get-Command $agentCommand -ErrorAction SilentlyContinue)) {
        Write-AgentPromptFailure "agent CLI not found: ${agentCommand}"
    }
    if ($agent -eq 'agy') {
        [Console]::Error.WriteLine(
            'agent-prompt: Antigravity print mode is experimental; review its output and permissions.'
        )
    }
    if ($workDir) { Push-Location -LiteralPath $workDir }
    try {
        & $agentCommand @commandArguments
        exit $LASTEXITCODE
    } finally {
        if ($workDir) { Pop-Location }
    }
}

if ($target -ne 'container') {
    Write-AgentPromptFailure 'ADE_AGENT_PROMPT_TARGET must be local or container'
}

switch ($composeMode) {
    'podman' {
        if (-not (Get-Command podman -ErrorAction SilentlyContinue)) { Write-AgentPromptFailure 'podman was not found in PATH' }
        $composeCommand = 'podman'
        $composeArguments = @('compose')
    }
    'podman-compose' {
        if (-not (Get-Command podman-compose -ErrorAction SilentlyContinue)) {
            Write-AgentPromptFailure 'podman-compose was not found in PATH'
        }
        $composeCommand = 'podman-compose'
        $composeArguments = @()
    }
    default {
        if (Get-Command podman -ErrorAction SilentlyContinue) {
            $composeCommand = 'podman'
            $composeArguments = @('compose')
        } elseif (Get-Command podman-compose -ErrorAction SilentlyContinue) {
            $composeCommand = 'podman-compose'
            $composeArguments = @()
        } else {
            Write-AgentPromptFailure 'neither podman nor podman-compose was found in PATH'
        }
    }
}

$containerArguments = @('exec', '-T', 'ade', '/usr/local/bin/agent-prompt', '--local')
if ($workDir) { $containerArguments += @('--cwd', $workDir) }
foreach ($agentArgument in $agentArguments) {
    $containerArguments += @('--agent-arg', $agentArgument)
}
$containerArguments += $agent

$promptText | & $composeCommand @composeArguments @containerArguments
exit $LASTEXITCODE
