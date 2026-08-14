# Einzelne Agenten-Prompts ausfuehren / Run Single Agent Prompts

## Zweck / Purpose

**DE:** Mit `scripts/agent-prompt.sh` und `scripts/agent-prompt.ps1` kannst du
einen einzelnen Auftrag ohne textbasierte Benutzeroberflaeche (TUI) an eine
Agenten-CLI im laufenden Sandbox-Container uebergeben. Das ist praktisch fuer
Skripte, wiederholbare Reviews oder einen Aufruf aus einer Desktop-Anwendung.
Die Desktop-Anwendung steuert dabei nicht den Container selbst; das Skript ruft
die CLI im Container ueber Podman Compose auf.

**EN:** `scripts/agent-prompt.sh` and `scripts/agent-prompt.ps1` send one task
to an agent CLI in the running sandbox container without opening its text user
interface (TUI). This is useful for scripts, repeatable reviews, or calls made
from a desktop application. The desktop application does not control the
container directly; the script invokes the container CLI through Podman
Compose.

## Voraussetzungen / Prerequisites

**DE:** Starte zuerst den Service `ade`. Die ausgewaehlte Agenten-CLI muss
bereits auf die fuer dich zulaessige Weise angemeldet oder konfiguriert sein.
Das Skript erzeugt keine Zugangsdaten und nimmt keine Provider-, Modell- oder
Rechtsfreigabe vor.

**EN:** Start the `ade` service first. The selected agent CLI must already be
signed in or configured through an allowed method. The script creates no
credentials and does not grant provider, model, or legal approval.

```bash
podman compose up -d ade
podman compose ps
```

## Unterstuetzte Agenten / Supported Agents

| Name | Nicht-interaktiver Aufruf im Container / Non-interactive container call | Hinweis / Note |
|---|---|---|
| `codex` | `codex exec` | Verwendet die Codex-Sandbox- und Approval-Konfiguration. / Uses Codex sandbox and approval configuration. |
| `claude` | `claude -p` | Gibt die einzelne Antwort aus. / Prints the single response. |
| `opencode` | `opencode run` | Verwendet keinen durch das Image vorausgewaehlten Provider. / The image does not preselect a provider. |
| `copilot` | `copilot -p` | Berechtigungen muessen explizit durch die CLI-Konfiguration erlaubt sein. / Permissions must be allowed explicitly by CLI configuration. |
| `gemini` | `gemini -p` | Verwendet den persistenten Gemini-Zustand. / Uses persistent Gemini state. |
| `agy` | `agy -p` | Experimentell; Ausgabe und Berechtigungen kontrollieren. / Experimental; review output and permissions. |

## Vom Host aufrufen / Run from the Host

**DE:** Das Repo-Skript verwendet standardmaessig den laufenden Container. Ein
Pfad bei `--cwd` ist deshalb ein Containerpfad, zum Beispiel `/workspace`.

**EN:** The repository script targets the running container by default. A
`--cwd` value is therefore a container path such as `/workspace`.

```bash
scripts/agent-prompt.sh --cwd /workspace codex -- \
  "Pruefe die Markdown-Dateien auf widerspruechliche Aussagen."
```

```powershell
pwsh -NoProfile -File scripts/agent-prompt.ps1 --cwd /workspace codex -- `
  'Pruefe die Markdown-Dateien auf widerspruechliche Aussagen.'
```

**DE:** Auf einem System ohne funktionierendes `podman compose` kann mit
`--podman-compose` der dokumentierte Lifecycle-Fallback gewaehlt werden.

**EN:** On a system without working `podman compose`, select the documented
lifecycle fallback with `--podman-compose`.

## Prompt ueber stdin oder Datei / Prompt Through stdin or a File

**DE:** Ein Prompt als Shell-Argument kann in der Shell-Historie oder kurz in
der Prozessliste sichtbar sein. Fuer vertraulichen Inhalt ist die Uebergabe
ueber die Standardeingabe (stdin) oder eine geschuetzte Datei besser. Das
Host-Skript liest `--prompt-file` auf dem Host und uebergibt nur den Inhalt an
den Container.

**EN:** A prompt passed as a shell argument can appear in shell history or
briefly in the process list. For confidential content, use standard input
(stdin) or a protected file. The host script reads `--prompt-file` on the host
and sends only its content into the container.

```bash
printf '%s\n' 'Fasse die offenen Punkte zusammen.' | \
  scripts/agent-prompt.sh claude

scripts/agent-prompt.sh opencode --prompt-file ./auftrag.txt
```

```powershell
Get-Content -Raw .\auftrag.txt |
  pwsh -NoProfile -File scripts/agent-prompt.ps1 opencode
```

## Direkt im Container / Directly Inside the Container

**DE:** Das Image installiert beide Varianten. `ADE_AGENT_PROMPT_TARGET=local`
setzt dort die direkte Ausfuehrung als Standard.

**EN:** The image installs both variants. Inside the image,
`ADE_AGENT_PROMPT_TARGET=local` makes direct execution the default.

```bash
agent-prompt codex -- "Pruefe den aktuellen Git-Diff."
```

```powershell
pwsh -NoProfile -File /usr/local/bin/agent-prompt.ps1 claude -- \
  'Fasse den aktuellen Git-Diff zusammen.'
```

## Agentenoptionen und Grenzen / Agent Options and Boundaries

**DE:** Mit `--agent-arg` wird genau ein Argument an die Agenten-CLI
weitergereicht; die Option kann wiederholt werden. Nutze `--dry-run`, um die
Zuordnung ohne Prompt-Inhalt und ohne Agentenaufruf zu sehen. Der Dispatcher
aktiviert niemals automatisch Optionen, die Sandboxing, Freigaben oder
Berechtigungspruefungen umgehen. Pruefe die Hilfe der gewaehlten CLI, bevor du
solche Argumente weiterreichst.

**EN:** `--agent-arg` passes exactly one argument to the agent CLI and can be
repeated. Use `--dry-run` to inspect the mapping without prompt content and
without calling the agent. The dispatcher never enables options that bypass
sandboxing, approvals, or permission checks. Read the selected CLI help before
passing such arguments.

```bash
scripts/agent-prompt.sh --local --dry-run --agent-arg --json codex -- \
  "Dieser Text wird in der Vorschau nicht ausgegeben."
```

`--local` ist ausserhalb des Containers ein bewusster Sonderfall: Dann wird
eine Agenten-CLI des Hosts mit dem dortigen Zustand verwendet. Fuer die
Ausbildungs-Sandbox ist der Container-Standard vorzuziehen.

*Outside the container, `--local` is an explicit exception that uses a host
agent CLI and its host-side state. The container default is preferred for the
training sandbox.*
