# Ubuntu/WSL2-Linux-Plattformbeleg / Ubuntu/WSL2 Linux Platform Evidence

Status: `Pass` (05.09.2026). Owner: Repository Maintainer. Reviewer:
Security Review. Runner-Token: `Ubuntu-WSL2-Bash-rootless-Podman`.

## Scope

**DE:** Nach der genehmigten Entscheidung
`DEC-XPLAT-WSL2-2026-09-04` ist Ubuntu unter WSL2 die verbindliche
Linux-Akzeptanzumgebung fuer Feature 003. Windows-Host und Ubuntu/WSL2 duerfen
dieselbe physische Hardware nutzen. Dieser Nachweis verwendet jedoch eine
eigene rootless-Podman-Laufzeit innerhalb von Ubuntu und keine
Windows-Podman-Machine-Evidenz. Native Linux-Hardware ist kein Akzeptanzziel
dieses Features.

**EN:** Under approved decision `DEC-XPLAT-WSL2-2026-09-04`, Ubuntu under WSL2
is the binding Linux acceptance environment for Feature 003. The Windows host
and Ubuntu/WSL2 may share physical hardware, but this evidence uses its own
rootless Podman runtime inside Ubuntu and no Windows Podman-machine evidence.
Native Linux hardware is not an acceptance target for this feature.

## Ausfuehrungsumgebung / Execution Environment

- WSL `2.7.10.0`, Kernel `6.18.33.2-microsoft-standard-WSL2`, Ubuntu
  `24.04.4 LTS`.
- Checkout im Linux-Dateisystem / Checkout in the Linux file system:
  `/home/thinder/absdd-image-sandbox-issue52-wsl2`.
- Git-Head: `ad5cd8bc9a9a2c541416390aa4256bc1ffe1eee7`; Worktree vor der
  Artefakterzeugung sauber / clean before artifact generation.
- Benutzer / User: `thinder`, UID `1000`; Bash `5.2.21`; PowerShell `7.6.5`;
  Podman `4.9.3`, `rootless=true`; podman-compose `1.0.6`.
- Compose-Projekt / Compose project: `absdd-image-sandbox-issue52-wsl2`.
  Ein temporaeres, nicht versioniertes Override bildete die Containerports
  `5100-5199` auf die freien Hostports `127.0.0.1:5600-5699` ab. Die
  Repository-Vorgabe blieb unveraendert. / A temporary unversioned override
  mapped container ports 5100-5199 to free host ports 127.0.0.1:5600-5699; the
  repository default remained unchanged.

## Technischer Nachweis / Technical Evidence

| Beobachtung / Observation | UTC-Zeit / UTC time | Ergebnis / Result |
|---|---|---|
| Kanonischer Compose-Start mit freiem Portbereich / canonical Compose start with free published ports | `2026-09-05T16:22:12Z` bis `16:22:15Z` | Exit `0`; 100 Bindings von `127.0.0.1:5600 -> 5100` bis `127.0.0.1:5699 -> 5199`. Der Windows-Container blieb unberuehrt. / Exit 0; 100 bindings; the Windows container was left untouched. |
| Benutzer, Terminal, Workspace, Mounts und LSP-Binary / user, terminal, workspace, mounts, and LSP binary | `2026-09-05T16:22:20Z` bis `16:22:22Z` | Exit `0`; `whoami=adedev`, UID `1655`, `pwd=/rider-projects`, Repository-Mount von `/home/thinder/absdd-image-sandbox-issue52-wsl2` nach `/ade-dev-sandbox`, Workspace-Mount nach `/workspace`, `sourcekit-lsp=/usr/bin/sourcekit-lsp`. |
| Vollstaendiger Runtime-Modus / complete Runtime mode | `2026-09-05T16:22:22Z` bis `16:22:26Z` | Exit `0`, `GREEN [Runtime]`; `no-new-privileges`, `cap_drop: ALL`, Non-root-User, getrennte Agenten-Volumes und localhost-only Portbindung bestaetigt. / Isolation, non-root user, separate state volumes, and localhost-only bindings confirmed. |
| Audit-Shutdown / audit shutdown | `2026-09-05T16:22:26Z` bis `16:22:33Z` | Der erste Export in den Repository-Mount scheiterte ehrlich mit Exit `1` an den Schreibrechten. Der korrigierte Lauf mit temporaerem Audit-Ziel endete mit Exit `0`, exportierte 5 Metadatenzeilen ohne Prompt-/Antwortinhalt und entfernte Service sowie Netzwerk. / The first repository-mounted export failed honestly on permissions; the corrected temporary audit target passed, exported five metadata-only rows, and removed the service and network. |
| Erneuter Service-Start fuer Editorpruefung / service restart for editor validation | `2026-09-05T16:22:34Z` bis `16:22:36Z` | Exit `0`; laufender Container `a10ae0acbfb1c8a9d84d38b5e8c87955a5c01098ad5f11e0b57595722bd287c5`. |
| Vollstaendiger Static-Modus im Linux-nativen Checkout / complete Static mode in the Linux-native checkout | `2026-09-05T21:40:25Z` bis `21:43:43Z` | Finaler Nachlauf gegen den um die Editorbeobachtung ergaenzten Evidenz-Patch: Exit `0`, `GREEN [Static]`; 24 Hardening-Tests, 4 Dispatcher-Tests, 3 Paritaetstests, Dockerfile-/Lock-/Dokumentationspruefungen und `git diff --check` bestanden. Zwei erste Wiederholungen der 24er-Suite als Containerbenutzer scheiterten an fehlendem Schreibrecht fuer ein temporaeres Verzeichnis direkt im Linux-Host-Mount; die massgebliche Linux-native Wiederholung als Checkout-Eigentuemer bestand vollstaendig. / The final rerun passed. Two initial container-user invocations could not create a temporary directory in the Linux host mount; the binding Linux-native rerun as the checkout owner passed completely. |
| Bash-/PowerShell-Presets, pre-commit, Secret- und Diff-Lauf im kanonischen Container gegen den Linux-nativen Mount / paired presets, pre-commit, secret, and diff run | `2026-09-05T21:40:27Z` bis `21:40:56Z` | Exit `0`; beide 12-Preset-Pruefungen bestanden; `uvx pre-commit run --all-files` bestand alle 4 Hooks einschliesslich gitleaks; Log-Hash `7deaa7748868ca332194fd0a472d98452960b0e9f559bff182b1d5688e475cb4`; Agenten-Scan `high=0`, `medium=0`, `low=4`; `git diff --check` Exit `0`. Die vier Low-Treffer sind Klassifikationen fuer Prompt-/Template-Verzeichnisse, keine offengelegten Geheimnisse. / Both preset checks and all four pre-commit hooks passed; no high or medium secret candidate was found. |
| Aktuelle CycloneDX-SBOM / current CycloneDX SBOM | `2026-09-05T16:27:56Z` bis `16:29:03Z` | Exit `0`; Syft `1.46.0`, CycloneDX `1.7`, 23.960 Komponenten, SHA-256 `ae02cefda291a8e59826859c7427f9db96b4a1f76f7ae44ca538c89841a4de71`. |
| Digest-gepinnter Grype-Scan und VEX-Abgleich / digest-pinned Grype scan and VEX reconciliation | Scan `2026-09-05T16:29:04Z` bis `16:31:03Z`; finale Validierung `2026-09-05T21:40:56Z` bis `21:40:57Z` | Exit `0`; Grype `0.117.0`, Datenbank `2026-09-05T06:27:00Z`, Scan-Hash `6be0bef9713a403a9cde05ed88a8fdc2e7aab65b025d3725b8a4f69d06e7aa3f`, 1.286 Treffer und 390 eindeutige Advisories. Alle bleiben `Open`/`in_triage`; keine Risikoakzeptanz oder Nichtbetroffenheit wird behauptet. Der Supply-Chain-Modus meldete `GREEN`. / All advisories remain open and in triage; final SupplyChain validation returned GREEN. |
| VS Code Remote WSL | Installation `2026-09-05T16:37:02Z` bis `16:37:05Z`; Verbindung `16:38:33Z` bis `16:38:37Z` | Erweiterung `ms-vscode-remote.remote-wsl` `0.104.3` installiert, Installations-Exit `0`; `code --status` bestaetigte das Fenster `absdd-image-sandbox-issue52-wsl2 [WSL: Ubuntu-24.04]`, den Linux-Workspace und laufende VS-Code-Serverprozesse. / Installation and the Remote WSL workspace passed. |
| VS Code Dev Containers | Erster Startversuch `2026-09-05T16:39:41Z` bis `16:40:28Z`; erfolgreiche Wiederholung und Abschlusspruefung bis `2026-09-05T21:35:50Z` | Der erste verschachtelte CLI-Versuch scheiterte ehrlich mit `No remote extension installed to resolve wsl`. Nach Setzen von `dev.containers.dockerPath` auf `podman` im lokalen VS-Code-Benutzerkontext gelang der manuelle Anhang. Der Repository Owner bestaetigte im integrierten Terminal `whoami=adedev` und nach Oeffnen des Ordners `pwd=/rider-projects`. Der Remote-Indikator zeigte das Image `docker.io/library/absdd-image-sandbox-issue52-wsl2-ade:latest`. Die technische Abschlusspruefung `2026-09-05T21:35:34Z` bis `21:35:50Z`, Exit `0`, bestaetigte das Remote-Fenster, `Folder (rider-projects)`, den laufenden Container `absdd-image-sandbox-issue52-wsl2-ade-1`, VS-Code-Server, `ptyHost`, `extensionHost` und den aktiven LSP `rust-analyzer`, jeweils unter `adedev`. / The initial nested CLI attempt failed honestly. After selecting Podman as the Dev Containers engine, manual attachment passed; the human terminal and the final exit-0 status/process probe confirmed the remote indicator, workspace, integrated terminal backend, remote user, and active LSP. |

Finales Ubuntu/WSL2-Image / Final Ubuntu/WSL2 image:

- Name: `docker.io/library/absdd-image-sandbox-issue52-wsl2-ade:latest`
- Image-ID:
  `bcdd1c8d4234ff8de8edbd1f3c52fe06c1a97d876d1c6a8996928bdff4376f2c`
- Plattform / Platform: `linux/amd64`
- Laufcontainer-ID / Runtime container ID:
  `a10ae0acbfb1c8a9d84d38b5e8c87955a5c01098ad5f11e0b57595722bd287c5`
- Der eingefrorene ADE-PoC-Container blieb vor und nach dem Lauf unveraendert
  `exited`, ID
  `f9989f112979ce8bbdb90f6576af1f71fededfdf6db158dfc2c7e10ead1a76e8`.
  / The frozen ADE PoC container remained exited and unchanged.

## Ergebnis / Result

**DE:** Build, freier publizierter Portbereich, Isolation, Runtime-Modus,
Audit-Shutdown, Benutzer, Workspace, Mounts, statische Pruefungen, pre-commit,
Secret-Scan, Diff, SBOM, Vulnerability-Scan, VEX/Provenienz und Remote WSL sind
aktuell belegt. Der erfolgreiche Dev-Containers-Anhang wurde durch die
menschlich beobachteten Terminalausgaben und den technischen VS-Code-/
Prozessnachweis fuer Remote-Indikator, `/rider-projects`, `adedev` und
`rust-analyzer` vervollstaendigt. `GATE-XPLAT-LINUX-01` ist deshalb `Pass`.
Der fruehere fehlgeschlagene CLI-Versuch und die nicht verfuegbare
Computer-Use-Schnittstelle bleiben als Grenzen sichtbar, aendern aber den
anschliessend erfolgreich beobachteten manuellen Anhang nicht.

**EN:** Build, the free published port range, isolation, Runtime mode, audit
shutdown, user, workspace, mounts, static checks, pre-commit, secret scan,
diff, SBOM, vulnerability scan, VEX/provenance, Remote WSL, and the Dev
Containers attachment are current. Human-observed terminal output and the
technical VS Code/process evidence complete the remote indicator,
`/rider-projects`, `adedev`, and `rust-analyzer` observations.
GATE-XPLAT-LINUX-01 therefore passes. The earlier failed CLI attempt and the
unavailable Computer Use interface remain documented limitations but do not
invalidate the subsequently observed manual attachment.

Neubewertungsausloeser / Re-evaluation trigger: Any WSL distribution, Podman
engine/socket, Compose mapping, image, mount, VS Code, Remote WSL, Dev
Containers, workspace, terminal, remote-user, or LSP change.
