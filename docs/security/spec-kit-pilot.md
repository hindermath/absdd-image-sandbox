# Spec-Kit-Pilotinitialisierung

Stand: 2026-05-16

## Deutsch

P2-1 wurde mit einem Pilotprojekt unter `/rider-projects/specify-pilot/`
validiert. Das Projekt liegt im gemounteten Host-Pfad fuer Rider-Projekte und
ist kein Bestandteil dieses Docker-Setup-Repositories.

Durchgefuehrter Ablauf:

1. ASP.NET-Core-Razor-Pages-Projekt mit dem .NET-SDK-Template erzeugt.
2. Projekt mit `dotnet restore` und `dotnet build --no-restore` gebaut.
3. Opencode mit `/init` initialisiert; dabei wurde `AGENTS.md` im Pilotprojekt
   angelegt.
4. Spec Kit mit `specify init . --integration opencode --script sh --force`
   initialisiert.
5. Die sechs Governance-Presets installiert:
   `security-governance`, `architecture-governance`,
   `isaqb-architecture-governance`, `a11y-governance`,
   `cross-platform-governance` und `agent-parity-governance`.
6. Opencode mit `/speckit.constitution` ausgefuehrt und die Projekt-Constitution
   unter `.specify/memory/constitution.md` erzeugt.

Evidenz im Container:

- `/workspace/audit-evidence/specify-preset-list.txt`
- `/workspace/audit-evidence/specify-init.txt`
- `/workspace/audit-evidence/opencode-init.jsonl`
- `/workspace/audit-evidence/opencode-speckit-constitution.jsonl`
- `/workspace/audit-evidence/specify-pilot-dotnet-build.txt`
- `/workspace/audit-evidence/specify-pilot-files.txt`
- `/workspace/audit-evidence/specify-pilot-AGENTS.md`
- `/workspace/audit-evidence/specify-pilot-constitution.md`

Bewertung:

- Das Pilotprojekt ist initialisiert.
- Alle sechs Presets sind in `specify preset list` sichtbar.
- Die Spec-Kit- und Opencode-Artefakte liegen im Pilotprojekt vor.
- Die Evidenzdateien liegen bewusst unter `/workspace/audit-evidence/` und
  werden nicht in diesem Repository versioniert.

Hinweis zum Lauf:

Beim Installieren der Presets auf dem Windows-/Podman-Bind-Mount trat ein
Metadatenfehler von Python `shutil.copytree` auf. Der bestehende Spec-Kit-Patch
wurde deshalb erweitert, damit nicht nur Datei-, sondern auch
Verzeichnis-Metadatenoperationen auf Bind-Mounts unterbleiben.

## English

P2-1 was validated with a pilot project under `/rider-projects/specify-pilot/`.
The project is located in the mounted host path for Rider projects and is not
part of this Docker setup repository.

Executed flow:

1. Created an ASP.NET Core Razor Pages project from the .NET SDK template.
2. Built the project with `dotnet restore` and `dotnet build --no-restore`.
3. Initialized Opencode with `/init`; this created `AGENTS.md` in the pilot
   project.
4. Initialized Spec Kit with
   `specify init . --integration opencode --script sh --force`.
5. Installed the six governance presets:
   `security-governance`, `architecture-governance`,
   `isaqb-architecture-governance`, `a11y-governance`,
   `cross-platform-governance`, and `agent-parity-governance`.
6. Ran Opencode with `/speckit.constitution` and created the project
   constitution under `.specify/memory/constitution.md`.

Evidence inside the container:

- `/workspace/audit-evidence/specify-preset-list.txt`
- `/workspace/audit-evidence/specify-init.txt`
- `/workspace/audit-evidence/opencode-init.jsonl`
- `/workspace/audit-evidence/opencode-speckit-constitution.jsonl`
- `/workspace/audit-evidence/specify-pilot-dotnet-build.txt`
- `/workspace/audit-evidence/specify-pilot-files.txt`
- `/workspace/audit-evidence/specify-pilot-AGENTS.md`
- `/workspace/audit-evidence/specify-pilot-constitution.md`

Assessment:

- The pilot project is initialized.
- All six presets are visible in `specify preset list`.
- The Spec Kit and Opencode artifacts exist in the pilot project.
- The evidence files intentionally live under `/workspace/audit-evidence/` and
  are not versioned in this repository.

Run note:

During preset installation on the Windows/Podman bind mount, Python
`shutil.copytree` hit a metadata error. The existing Spec Kit patch was extended
so both file and directory metadata operations are skipped on bind mounts.
