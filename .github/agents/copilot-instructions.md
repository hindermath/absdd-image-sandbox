# Repository Guidelines

## Einstieg und Detailregeln / Entry point and detailed rules

DE: Lies die Projektkonstitution und vor der Arbeit die [Detailregeln](../../docs/agent-guidance.md)
für deine Aufgabe. Sie ergänzen die verbindlichen Arbeits-, Sicherheits-, Prüf- und Freigaberegeln.

EN: Read the project constitution and the relevant [detailed rules](../../docs/agent-guidance.md)
before working. They supplement the binding work, security, verification and approval rules.

DE: Das Standardprofil `all` enthält sechs erforderliche speichersichere
Toolchains (.NET/C#, Java, Go, Rust, Python und Swift). PowerShell 7 ist die
zweite Skriptgrundlage. Node.js/npm sind unterstützende Werkzeuge.

EN: The default `all` image includes six required memory-safe language
toolchains (.NET/C#, Java, Go, Rust, Python, and Swift). It includes
PowerShell 7 as a second scripting foundation and Node.js/npm as supporting tooling.

<!-- documentation-reader-contract:start -->
## Dokumentationspflege / Documentation Maintenance

DE: Bestehende Markdown-Leserpfade unter `docs/fuer-lernende/` und
`docs/betrieb/` erweitern, keine zweite Lernreihenquelle erzeugen.
Deutsch zuerst, gleichwertiges Englisch danach, etwa CEFR B2. Befehle mit
Ausfuehrungsort (Host, Ubuntu/WSL2 oder Container), Shell, Voraussetzungen,
erwartetem Ergebnis und Fehlerhilfe erklaeren. Destruktive Volume-Optionen
nicht als normalen Stopp empfehlen. Aktuelle Statusangaben an Datum, Image
und Evidenz binden; historische Zahlen nicht ungeprueft fortschreiben.
WCAG 2.2 AA ist Pruefziel, kein Ergebnis automatischer Markdown-Checks.
OpenCode-2-Datenbankmetadaten sind kein sitzungsbezogener Auditnachweis:
`session_coverage=not-exported`; keine Datenbankinhalte exportieren.

EN: Extend existing learner and operations Markdown paths; do not create a
second learning-series source. Use German first and equivalent English,
around CEFR B2. Explain command location, shell, prerequisites, expected
result and error help. Never recommend destructive volume options as normal
shutdown. Bind current status to date, image and evidence; do not repeat
historical counts without checking. WCAG 2.2 AA is a review target, not the
result of automated Markdown checks. OpenCode 2 storage metadata does not
prove session-level audit coverage; never export database contents.
<!-- documentation-reader-contract:end -->

## Active Compliance Work Queue

This repository maintains open sandbox-governance findings against the generic Secure Development Guideline and checklist `CL_12` ("Agentic AI in Sandbox Environments") from `docs/secure-development`. The complete work list with concrete tasks, acceptance criteria, verification steps, and escalation rules is in `COMPLIANCE-PLAN_RL-SE-001.md`.

**Read `COMPLIANCE-PLAN_RL-SE-001.md` at the start of every GitHub Copilot session.** That file is the single source of truth for:

- the priority order of open work (P0 must run first, then P1, P2, P3);
- the per-task commit and pull request conventions used for these changes;
- the items that must NOT be handled by an agent and have to be escalated to a human (API key rotation, formal sandbox approval, platform-side branch protection rules, external management-system register entries).

At the end of every GitHub Copilot session, append a short session log under `docs/security/agent-session-log/<YYYY-MM-DD-HHMM>.md` as required by the plan. The log records which plan IDs were completed, partially completed, or escalated.

The plan and these guidelines work together: this `.github/copilot-instructions.md` file describes the repository conventions; `COMPLIANCE-PLAN_RL-SE-001.md` describes the generic secure-development and sandbox-governance work that brings those conventions into provable conformance.

## Secure-Development Neutralitaet / Secure Development Neutrality

Treat `docs/secure-development/` as the generic Secure-Development-Basis for
training, review, and hardening work. Do not describe it as a company policy,
internal guideline, or concrete management-system requirement.

Generic roles and placeholders such as organization, project owner, security
review, CISO/ISB/KIB, document repository, risk register, RoPA, provider, or
platform are allowed when they remain generic. Concrete organizations, private
URLs, local host paths, provider portals, account-specific defaults, external
document-management or security-management systems, or platform rules must be
removed, generalized, or marked as example, context, `N/A`, `Open`, or
project-specific evidence.

Spec-Kit runs against this baseline must create project-specific evidence.
Human-only items such as formal approval, external registers, secret rotation,
provider/model approvals, and platform branch protection must not be claimed as
completed by an agent.

<!-- optional-template-profile:start -->
## Optionales Template-Profil / Optional Template Profile

Fork oder institutionelle Kopie mit gemeinsamer Historie bleibt Standard.
Das optionale GitHub-Template-Profil ist vorbereitet, nicht aktiviert.
Eine Template-Kopie hat eigene Historie; keine pauschalen Upstream-Merges
oder Verknuepfung mit --allow-unrelated-histories empfehlen.
Kopierte Compliance-Workqueues, Intakes, Run-States, Statistiken und Abnahmen
sind Referenzkontext, keine persoenlichen Auftraege oder Nachweise.
Keine kopierten Autonomous-Laeufe fortsetzen und keine Status zur scheinbaren
Neuinbetriebnahme umschreiben. Persoenliche Baseline, Review und Startautoritaet
muessen getrennt hergestellt werden. Sandbox-, Level-0- und Produkt-Repos
auseinanderhalten. MIT gilt nur fuer nachweislich eigene Inhalte;
Lizenz- und Aktivierungsgates bleiben erhalten. Siehe
docs/fuer-lernende/template-profil.md und docs/licensing.md.

*Fork/shared-history institutional copy remains the default. The optional
template profile is prepared, not enabled. Template copies have independent
history: do not recommend blind upstream or unrelated-history merges.
Copied workqueues, intakes, states, statistics and approvals are source
context, not personal authority/evidence. Never resume copied source runs
or reset their statuses. Establish a separate personal baseline, review and
start decision. Keep sandbox, Level-0 and product repos distinct. MIT covers
demonstrably original content only; rights and activation gates remain.*
<!-- optional-template-profile:end -->

## Git Hosting for Learners

Learner documentation must not require a GitHub account universally. The
learner's personal fork or institution-provided repository is `origin`; the
institution-maintained reference is `upstream`. GitHub is one profile alongside
GitLab, Codeberg, Forgejo, and other Git-capable institutional systems. Require
a GitHub account only for the direct GitHub route or optional GitHub Copilot
sign-in. Keep the public GitHub URL as provenance, not as the only clone path.

## Build, Test, and Development Commands

Run commands from the repository root:

```bash
podman-compose config
```

Validates the Compose file without printing values from `opencode.env` and
without requiring a running Podman machine.

```bash
podman compose up -d
```

Builds the image if needed and starts the `ade` container.

```bash
podman compose exec ade bash
```

Opens a shell inside the running container.

On macOS or Windows, initialize and start the Podman machine before running Compose commands:

```bash
podman machine init
podman machine start
podman compose build --pull
podman compose up -d
podman compose exec ade bash
```

Use `podman-compose config` for config-only validation. If `podman compose`
is not available for lifecycle actions on the local installation, use
`podman-compose` with the same arguments.

```bash
specify version
specify check
```

Verifies the Spec Kit CLI installation inside the container.

```bash
cd /rider-projects
```

Moves to the mounted Windows/Rider projects directory inside the container.

```bash
cd /home/adedev/home-baseline-source
```

Moves to the pinned read-only `home-baseline` reference included in the image.
Its source, release, commit, and license are locked in
`home-baseline.lock.json`; no script from the reference runs automatically.
For writable Level-0 work, public users create their personal fork or
institution-provided repository and set `HOME_BASELINE_DIR` locally. The
Compose override replaces `/opt/home-baseline` while preserving this user-facing
path. Only the direct GitHub profile requires a GitHub account.

The Level-0 source is used directly inside the container. Normal writing
`sync-home.*` runs targeting `/home/adedev` remain blocked. The explicit
`sync-home-baseline-runtime --apply` wrapper may synchronize only manifest-defined
`homeRuntime` content; `--dry-run` and `--check-only` are write-free, and no
mode means no write. The wrapper offers no force mode and runs no pull, push,
commit, Git initialization, Git configuration, or identity change. Selected
runtime content may enter persistent agent volumes, but credentials, provider
state, and local settings must remain untouched. No writing sync runs during
image build or container startup.

```bash
bash scripts/compose-down-with-audit.sh --podman
```

Stops the environment after successful metadata export and preserves volumes.
Volume deletion is a separate human-confirmed operation; never append `-v`
or `-Volumes` for normal shutdown. Use the PowerShell wrapper described below
on a PowerShell host. Do not bypass the wrapper or a failed audit export.

## Agentische Skriptausfuehrung / Agentic Script Execution

Vor lokaler Automation zuerst das Betriebssystem erkennen. Wenn `pwsh`
verfuegbar ist, vorhandene PowerShell-7-Skripte oder Cmdlets bevorzugen und
auf diesem macOS-Host wegen Profil-Nebenwirkungen `pwsh -NoProfile` nutzen.
Fuer strukturierte lokale Automation ist C# ueber `.NET` oder `mono` ein
zulaessiger zweiter Weg, wenn Typisierung, Dateiformate oder
Wiederverwendbarkeit davon profitieren. Erst wenn PowerShell oder C# nicht
sinnvoll passen, die OS-nahe vorhandene Repo-Variante nutzen, in diesem
Repository typischerweise Bash, Podman-Compose-Befehle oder vorhandene
`scripts/`-Wrapper. Keine neue Sprache nur aus Bequemlichkeit einfuehren, wenn
ein bestehendes Repo-Skript denselben Zweck erfuellt.

*Before local automation, detect the operating system. If `pwsh` is available,
prefer existing PowerShell 7 scripts or Cmdlets and use `pwsh -NoProfile` on
this macOS host because the profile has side effects. For structured local
automation, C# via `.NET` or `mono` is an acceptable second option when typing,
file formats, or reuse benefit from it. Only use the OS-native existing
repository variant when PowerShell or C# does not fit, typically Bash, Podman
Compose commands, or existing `scripts/` wrappers in this repository. Do not
introduce a new language for convenience when an existing repository script
already solves the task.*

<!-- agent-prompt-dispatcher-guidance:start -->
## Nicht-interaktive Agenten-Prompts / Non-Interactive Agent Prompts

Die Repo-Einstiege `scripts/agent-prompt.sh` und
`scripts/agent-prompt.ps1` zielen standardmaessig auf den laufenden
Compose-Service `ade`. Im Image sind beide als `agent-prompt` und
`/usr/local/bin/agent-prompt.ps1` installiert; dort setzt
`ADE_AGENT_PROMPT_TARGET=local` die direkte CLI-Ausfuehrung. Unterstuetzt
werden `codex`, `claude`, `opencode`, `copilot`, `gemini` und `agy`;
Antigravity-Printmodus bleibt experimentell.

Prompts mit vertraulichem Inhalt ueber stdin oder `--prompt-file` uebergeben.
Der Dispatcher darf keine Anmeldung, Provider- oder Modellwahl,
Berechtigungserweiterung oder Approval-Umgehung automatisieren. Gemeinsame
Aenderungen an Mapping und Argumentsemantik muessen atomar in beiden Skripten,
`scripts/tests/test_agent_prompt_dispatchers.py`, `README.md` und der
Lernenden-Anleitung gepflegt werden.

*The repository entrypoints target the running `ade` service by default. Both
variants are installed in the image and run agent CLIs directly there through
`ADE_AGENT_PROMPT_TARGET=local`. Use stdin or `--prompt-file` for
confidential prompts. The dispatcher must not automate sign-in, provider or
model selection, permission broadening, or approval bypasses. Keep both
scripts, their parity tests, and user documentation synchronized.*
<!-- agent-prompt-dispatcher-guidance:end -->

## Commit & Pull Request Guidelines

The current history uses short, imperative commit messages, for example `Update opencode podman setup` and `Add README table of contents`.

For pull requests, include:

- a short summary of the change
- any Podman Compose commands used for validation
- notes about configuration or secret handling
- screenshots only if documentation rendering or UI output is relevant

Repository governance lives partly in this repository and partly in the active
GitHub hosting platform. `.github/CODEOWNERS` and
`.github/pull_request_template.md` are repository-side guidance for reviews.
Platform-side enforcement such as repository rulesets, required checks, Code
Owner review, signed-commit policy, and admin bypass must be configured
separately by an Owner or Admin on GitHub. For the target public-readiness
ruleset and signed-commit notes, see `docs/security/branch-protection.md`.

## Security & Configuration Tips

Never commit `opencode.env`; it is ignored by `.gitignore` and may contain local provider secrets when a user adds their own OpenCode configuration. Keep local secret files restricted:

```bash
chmod 600 opencode.env
```

If copying credentials for a local OpenCode provider, only write the key into `opencode.env` and do not print it in logs or documentation.

Run the repository secret scan before committing:

```bash
pre-commit install
pre-commit run --all-files
```

If `pre-commit` is not installed in the current environment, install it first with `uv tool install pre-commit` or run it via `uvx pre-commit run --all-files`.

Audit text for P1-3: "Client-side Control; central secret push blocking
depends on the active hosting platform, edition, and admin-operated hooks."

Run the agent-session audit export at least once per workday and always before removing Compose volumes. The standard stop path is the wrapper, because it exports metadata before running `compose down`:

```bash
bash scripts/compose-down-with-audit.sh --podman
```

On Windows PowerShell with Podman:

```powershell
.\scripts\compose-down-with-audit.ps1 -Engine podman
```

Normal shutdown preserves volumes. Add `-v` or `-Volumes` only after explicit confirmation of data loss. Both wrappers abort before `down` if audit export fails. If a wrapper cannot be used, a human must confirm successful metadata export before any deliberate volume removal; do not bypass an export failure. The entrypoint hook is best effort and does not replace this check.

The export writes metadata only to `/audit/YYYY-MM-DD.jsonl`. Do not extend it to include prompt text, response text, raw session payloads, or secrets. The default host directory is `audit-logs/`; generated JSONL files stay untracked.

## Spec-Kit-Modell-Routing / Spec Kit Model Routing

- Modellwahl ist operative Agenten-Routing-Guidance, keine Feature-Anforderung. Modellnamen nicht in `spec.md`, `plan.md`, `tasks.md` oder einzelne Feature-Specs schreiben; diese Artefakte muessen reproduzierbar bleiben, auch wenn Modellnamen wechseln oder ein anderer KI-Agent verwendet wird.
- Der jeweilige Agent soll diese Empfehlungen auf seine aktuell verfuegbaren Modelle abbilden; keine feste Anbieter- oder Modellbindung ableiten.
- Fuer Spec-Kit-Spezifikation, Klaerung, Planung, Tasks und Analyse (`/speckit-specify`, `/speckit-clarify`, `/speckit-plan`, `/speckit-tasks`, `/speckit-analyze`; je nach Agent auch `/speckit.specify` usw.) das staerkste verfuegbare Frontier-Reasoning-/Coding-Modell bevorzugen.
- Fuer vollstaendige, lang laufende `/speckit-implement`-Laeufe das staerkste verfuegbare Long-Running-Agent-Modell bevorzugen; das Frontier-Modell nutzen, wenn maximale Urteilsguete wichtiger ist als Laufzeitstabilitaet.
- Fuer fokussierte Reviews oder CI-Fixes ein coding-optimiertes Modell bevorzugen.
- Fuer triviale Bereinigung, Formatierung oder risikoarme mechanische Edits ist ein schnelles kleines Coding-Modell akzeptabel.

*Model choice is operational agent-routing guidance, not a feature requirement. Do not pin model names in `spec.md`, `plan.md`, `tasks.md`, or individual feature specs; those artifacts must stay reproducible even when model names change or another AI agent is used. Each agent should map these recommendations to its currently available models; do not derive a fixed vendor or model requirement. For Spec-Kit specification, clarification, planning, task generation, and analysis (`/speckit-specify`, `/speckit-clarify`, `/speckit-plan`, `/speckit-tasks`, `/speckit-analyze`; or `/speckit.specify` etc. depending on the agent surface), prefer the strongest available frontier reasoning/coding model. For complete long-running `/speckit-implement` runs, prefer the strongest available long-running agent model; use the frontier model when maximum judgment quality is more important than runtime stability. For focused review or CI fixes, prefer a coding-optimized model. For trivial cleanup, formatting, or low-risk mechanical edits, a fast small coding model is acceptable.*

<!-- learner-a11y-baseline:start -->
## Hinweise zur Lernenden- und A11Y-Basis / Notes on the Learner and A11Y Baseline

- Verbindliche Zielgruppen ab dem ersten Ausbildungsjahr sind
  Fachinformatiker*innen, IT-System-Elektroniker*innen, Kaufleute für
  IT-System-Management und Kaufleute für Digitalisierungsmanagement.
- Lern-, Bedien-, Governance- und Spec-Kit-Inhalte stehen auf Deutsch zuerst
  und Englisch danach, verwenden ungefähr CEFR B2 und erklären Fachbegriffe
  beim ersten Auftreten.
- Spec-Kit-Erfahrung wird nicht vorausgesetzt. Befehle, Artefakte, Zustände und
  Übergänge werden beim ersten Gebrauch verständlich eingeführt.
- Abhängigkeiten, Zustände und Entscheidungen erhalten eine vollständige
  textorientierte Erklärung; eine ausschließlich visuelle Darstellung genügt
  nicht.
- `Programmierung #include<everyone>` und WCAG 2.2 Level AA gelten als
  verbindliche Prüfbasis, soweit die Kriterien auf das Artefakt anwendbar sind.

*The binding audience starts in the first training year and includes IT
specialist and IT systems electronics technician apprentices plus both IT
management occupations. Learner, usage,
governance, and Spec Kit content is German-first/English-second at about CEFR
B2, explains technical terms at first use, assumes no prior Spec Kit
experience, and never relies on visual-only dependency, state, or decision
information. `Programmierung #include<everyone>` and WCAG 2.2 Level AA are the
review baseline wherever applicable.*
<!-- learner-a11y-baseline:end -->

<!-- intake-mermaid-guidance:start -->
## Textorientierte Mermaid-Diagramme / Text-First Mermaid Diagrams

- Kommende Lastenhefte und Intake-Reihenfolgen sollen bei nicht trivialen
  Abhaengigkeiten, Ablaeufen oder Zustaenden ein Mermaid-Diagramm direkt im
  versionierten Markdown enthalten.
- Vor jedem Diagramm muss eine vollstaendige deutschsprachige und danach
  englischsprachige Textalternative als geordnete Liste oder Tabelle stehen.
  Sie nennt alle Knoten, Kanten, Status und Entscheidungen und bleibt die
  verstaendliche Grundlage, wenn Mermaid nicht gerendert wird.
- Mermaid ist eine ergaenzende Ansicht. Ein vorhandenes maschinenlesbares
  Manifest bleibt massgeblich; Diagramm und Text duerfen keinen davon
  unabhaengigen Zustand erfinden.
- Der Mermaid-Quelltext verwendet stabile, sprechende Knoten-IDs, einfache
  `flowchart TD`- oder `flowchart LR`-Strukturen und keine Information, die nur
  durch Farbe, Form oder Position vermittelt wird. Externe Bilder oder
  generierte Binaerdiagramme sind fuer diese Ergaenzung nicht erforderlich.
- Bei Aenderungen an Abhaengigkeiten oder Status werden Textalternative und
  Mermaid-Quelle gemeinsam aktualisiert.

*Future requirements documents and intake order views should embed Mermaid
for non-trivial dependencies, flows, or states. A complete German-first and
English-second ordered text or table alternative must precede every diagram
and carry every node, edge, status, and decision. Mermaid is supplementary;
the machine-readable manifest remains authoritative. Use stable descriptive
node IDs, simple flowcharts, and no color-, shape-, or position-only meaning.
Update the text alternative and Mermaid source together.*
<!-- intake-mermaid-guidance:end -->

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
<!-- SPECKIT END -->

<!-- statistics-profile-2-guidance:begin -->
## Statistikprofil 2 / Statistics Profile 2

- Verbindlich sind `docs/project-statistics.config.json` und der markierte Profil-2-Block in `docs/project-statistics.md`; aktualisieren mit `render-project-statistics.*`.
- Profil 2 zeigt exakte KPI, Artefaktmix, 52-Wochen-Aktivitaet, Wochen- und kumulatives Volumen, belastbare Phasen oder Monatsfallback sowie Speedup-Vergleiche.
- Nur ASCII verwenden: Heatmap `0..4`, `-` fuer noch nicht abgelaufene Tage und Gauges `#`/`.`; jedes Textdiagramm bleibt hoechstens 100 Zeichen breit.
- Jede Grafik braucht genaue Zahlen und eine bilinguale CEFR-B2-Textalternative, Deutsch zuerst und Englisch danach.
- Methodik v2 wertet Git-getrackten Text und Bruttoaenderungen aus Nicht-Merge-Commits aus; Ledger, `STATS.md` und Binaerdaten bleiben ausgeschlossen.
- Referenzen dieses Repositories: `80` Zeilen/Arbeitstag konservativ und `100` Zeilen/Arbeitstag Thorsten-Solo. Speedup bleibt Lieferdichte, keine Stoppuhr- oder Personenbewertung.
- Dieser Vertrag ersetzt aeltere Visualisierungsvorgaben; historische Ledger-Eintraege und archivierte Profil-1-Diagramme bleiben unveraendert.
- Gemeinsame Aenderungen werden synchron in `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` und `.github/agents/copilot-instructions.md` gepflegt.

*Profile 2 is governed by the JSON configuration and generated marker block. Use ASCII `0..4`, `-`, and `#`/`.`, exact values, German-first bilingual CEFR-B2 alternatives, and a 100-character chart limit. Methodology v2 excludes the ledger, `STATS.md`, and binaries. This repository uses manual references of `80` and `100` lines per workday. Speedup describes delivery density, not stopwatch or personal performance. This contract supersedes older visualization rules while retaining historical entries and archived Profile 1 charts.*
<!-- statistics-profile-2-guidance:end -->

## Secure Development Assurance – freigegebenes Projektprofil / Approved Project Profile

- Die unveraenderte Basis des optionalen 14er-Statistik-Piloten ist `secure-development-assurance-thirteen-governance-presets`: die bisherigen zwölf Presets plus `secure-development-assurance-governance` v0.1.10, aktiviert mit Priorität 15. Andere Profile und globale Defaults bleiben unverändert.
- Maßgebliche Produktquellen sind ausschließlich die veröffentlichten eigenständigen GitHub-Preset-Repositories. Lokale Installationen sind Integrationskopien, keine zusätzlichen Produktquellen; Änderungen entstehen im jeweiligen Preset-Repository, nicht in einem Home-Baseline-Scaffold.
- `speckit.secure-development-status` prüft Evidence strikt lesend. `speckit.secure-development-review` benötigt einen ausdrücklich beauftragten Gate-/Kontext-Review; die Installation startet keine Reviews und erteilt keine menschlichen Freigaben.
- Keine C5-Testat-, Zertifizierungs- oder vollständige Readiness-Prüfung; `Ready` gilt nur für den gebundenen Evidence-Kontext. Projektgeführte Baseline-Versionen werden nicht durch die Preset-Version ersetzt.
- Bedienung, Paketbindung, Erhaltungsnachweis und Grenzen: [Integrationsnachweis](../../docs/maintenance/secure-development-assurance-integration.md), relativ zur Repository-Wurzel.

*The optional fourteen-preset statistics pilot retains this thirteen-preset base: its existing twelve presets plus Secure Development Assurance v0.1.8, enabled at priority 15. Other profiles and global defaults stay unchanged. Published standalone GitHub repositories are the only product sources; installed copies are integrations, not competing sources. Status is read-only; a gate review requires explicit context-specific authority. Installation starts no reviews and grants no human approvals. This is not a C5 attestation, certification, or full readiness check; `Ready` is evidence-context-specific. The project baseline retains its own version. See the integration record relative to the repository root.*

<!-- BEGIN spec-kit-diagrams-completion -->
## Mermaid und Spec-Kit-Abschlussbericht / Mermaid and Spec Kit completion report

Neue Lastenhefte enthalten bei hilfreichen Abläufen, Zuständen oder Abhängigkeiten
lesbaren Mermaid-Quelltext im Markdown und eine gleichwertige Textalternative.
Bei einfachen Inhalten die Nichtanwendung kurz begründen. Diagramme bilden die
verbindlichen Text-/Manifestquellen ab; Farbe allein trägt keine Bedeutung.
Nach jedem vollständig abgeschlossenen Spec-Kit-Feature-Lauf den vollständigen
Ergebnisbericht im Chat anzeigen und im Feature-Verzeichnis als
`completion-report.md` versionieren. Einzelne Planungs-/Status-/Review-Kommandos
lösen keinen solchen Bericht aus; blockierte oder pausierte Läufe als
Zwischenbericht kennzeichnen. Vorlage: `.specify/templates/completion-report-template.md`;
Regel: `docs/spec-kit-diagrams-and-completion-reports.md`.
Ergebnis, Tests, Dokumentation, Git-gebundene Umfangszahlen, Verlauf und Restpunkte
belegen. Programmlogik von generierter Evidence, Git-Wandzeit von aktiver
Arbeitszeit und bestandene von ausgefallenen Prüfungen unterscheiden. Finale
Merge-/Sync-Evidence im Chat und bestehenden Closeout-Nachweis ergänzen; keine
zusätzlichen Commits allein für selbstreferenzielle Berichts-/Statistikwerte.
Diese Projektregel und lokale Vorlagen bei Spec-Kit-Updates erhalten.

*New intakes use readable Mermaid Markdown and equivalent text alternatives for
useful workflows, states or dependencies; justify omission for simple content.
Diagrams reflect authoritative text/manifests and never rely on color alone.
After each completed feature run, show the full outcome report in chat and
version completion-report.md in the feature directory using the shared template
and rule above. Individual planning/status/review commands do not trigger it;
paused/blocked runs receive interim reports. Evidence outcomes, tests, docs,
Git-bound counts, delivery history and remaining work. Distinguish code from
volume generated as evidence, elapsed from active time, and passed from failed
checks. Add final merge/sync proof in chat and existing closeout evidence, without
commits solely for self-referential counts or IDs. Preserve local rules/templates
across Spec Kit updates.*
<!-- END spec-kit-diagrams-completion -->

<!-- project-statistics-pilot:begin -->
## Optionaler Statistik-Pilot / Optional Statistics Pilot

Dieses Projekt verwendet im genehmigten Pilotbranch das Profil
`project-statistics-fourteen-governance-presets`: unveraenderte 13er-Basis plus
`project-statistics-governance` v0.1.4, aktiviert mit Prioritaet 90.
Das Preset dient reproduzierbarer Projekttransparenz, nicht der Bewertung von
Lernenden, Qualitaet oder KI-Zeitersparnis. Die bestehende Statistik bleibt
kanonisch. Der kuenftige getrennte Kontext ist `docs/project-statistics-pilot/`;
Referenz-Modellrechnungen bleiben ausgeschaltet. Installation startet weder
Messung noch Spec-Kit-Feature und erteilt keine Commit-/Push-/Mergefreigabe.
Integrationsnachweis: `docs/maintenance/project-statistics-installation-v010.md`
relativ zur Repository-Wurzel. Kein Home-Runtime-Sync und keine globale
Default-Aenderung. Operative Profilzuordnung erst nach gepruefter Lieferung.

This project's approved pilot branch opts into fourteen presets: the unchanged
thirteen-preset base plus Project Statistics Governance v0.1.3 at priority 90.
It provides reproducible project transparency, not learner ratings, quality
scores or AI time-savings measurements. Existing statistics remain canonical;
the future pilot context is separate and reference estimates remain off.
Installation starts no measurement or Spec Kit feature and grants no delivery
authority. See the integration record relative to the repository root.
No Home Runtime sync or global default change; operational assignment follows
reviewed delivery.
<!-- project-statistics-pilot:end -->

## macOS-CI-Runner / macOS CI runners

Bisherige macOS-14-Jobs verwenden explizit `macos-15`. Die bestehende
Repository-Auswahl fuer Linux-only-Wartungsjobs bleibt erhalten. Ein gruener
CI-Lauf beweist nur die ausgefuehrten Checks, keine Produkt-Plattformabnahme.
Bei Runnerwechseln auch verpflichtende Checknamen und Migrationsvorlagen
pruefen. Betrieb und Pruefgrenzen: `docs/maintenance/macos-runner-migration.md`.

Existing macOS 14 jobs explicitly use `macos-15`. Keep the existing repository
selection for Linux-only maintenance jobs. Successful CI proves the executed
checks, not product platform acceptance. Review required check names and
migration templates whenever runner labels change. See the linked guide.

## Governance-Zielstand 2026-10-24 / Governance target 2026-10-24

DE: Das explizit genehmigte 14er-Profil bindet Security 0.7.4, Architecture
0.6.5 und Intake Authoring 0.3.10 / Review 0.2.7 / Sequencing 0.2.11. Alle vierzehn
Presets werden aktualisiert; Prioritaeten bleiben erhalten. DS-GVO, KI-VO, CRA, NIS2
und DORA werden fuer Beispielprodukt, Entwicklungswerkzeuge und Organisation
getrennt auf Anwendbarkeit geprueft; Ausbildung ist keine pauschale Ausnahme.
Ungeklaerte Rollen bleiben Open. C5 Typ 1 und Typ 2 sind getrennte Nachweise,
keine Produktzertifizierung. Installation startet keinen Produktlauf, erneuert
keine Intake-Receipts und ersetzt keine menschliche Sandbox-/Risikofreigabe.
Vor einem Lauf Quellen-/Review-Frische, Serie, lokales Routing und aktuelle
Delivery-Autoritaet erneut pruefen. Nachweis: docs/maintenance/stable-preset-rollout-2026-10-24.md.

EN: The explicitly approved fourteen-preset profile binds Security 0.7.4,
Architecture 0.6.5 and Intake Authoring 0.3.10 / Review 0.2.7 / Sequencing 0.2.11.
Update all fourteen packages and preserve all priorities. Screen GDPR, AI Act, CRA,
NIS2 and DORA separately for example product, development tools and organization;
education is not a blanket exemption and unknown roles remain Open. Distinguish
C5 Type 1 from Type 2 evidence, without claiming product certification.
Installation starts no product run, refreshes no intake receipts and grants
no human sandbox/risk acceptance. Before a run recheck source/review freshness,
series, local routing and delivery authority; see the linked integration record.
