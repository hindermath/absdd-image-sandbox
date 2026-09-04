# Plattform-Scope-Entscheidung / Platform Scope Decision

## Entscheidung / Decision

| Feld / Field | Wert / Value |
|---|---|
| Decision-ID | `DEC-XPLAT-WSL2-2026-09-04` |
| Datum / Date | `2026-09-04` |
| Feature | `003-secure-development-container-hardening` |
| Genehmigt durch / Approved by | `@hindermath` |
| Genehmigungsrollen / Approval roles | `Repository Owner`, `Security Review` |
| Status | `Approved` |

**DE:** Fuer Feature 003 werden der Windows-Hostpfad und der
Linux-Ausfuehrungspfad auf derselben physischen Windows-Hardware geprueft. Der
Linux-Ausfuehrungspfad ist Ubuntu unter WSL2 mit einer eigenen
rootless-Podman-Laufzeit. Ein separater nativer Linux-Rechner ist fuer die
Abnahme dieses Features nicht erforderlich.

**EN:** For Feature 003, the Windows host path and the Linux execution path
are tested on the same physical Windows hardware. The Linux execution path is
Ubuntu under WSL2 with its own rootless Podman runtime. A separate native Linux
machine is not required for this feature's acceptance.

## Begruendung / Rationale

**DE:** Fuer den Ausbildungsbetrieb steht keine separate native
Linux-/Ubuntu-Hardware zur Verfuegung. Die fruehere Forderung nach einem
zusaetzlichen physischen oder unabhaengigen Linux-System war deshalb hoeher als
der praktisch verfuegbare Abnahmerahmen. Ubuntu unter WSL2 liefert eine reale
Linux-Benutzerumgebung fuer Bash, PowerShell 7 und rootless Podman. Die
Entscheidung reduziert nur die Hardwarematrix, nicht die Sicherheits- oder
Evidenzanforderungen.

**EN:** No separate native Linux/Ubuntu hardware is available for the training
operation. The former requirement for an additional physical or independent
Linux system therefore exceeded the practical acceptance environment. Ubuntu
under WSL2 provides a real Linux user environment for Bash, PowerShell 7, and
rootless Podman. This decision reduces only the hardware matrix, not the
security or evidence requirements.

## Verbindliche Evidenztrennung / Binding Evidence Separation

1. `GATE-XPLAT-WIN-01` verwendet den Runner-Token
   `Windows-Host-PowerShell7-Podman`. Der Nachweis umfasst Windows PowerShell 7,
   Windows-Podman-Machine, Build/Runtime und den beobachteten VS-Code-Desktop-
   Attach.
2. `GATE-XPLAT-LINUX-01` verwendet den Runner-Token
   `Ubuntu-WSL2-Bash-rootless-Podman`. Der Nachweis umfasst einen normalen
   Linux-Benutzer, einen Checkout im Linux-Dateisystem, eine eigene
   rootless-Podman-Laufzeit in Ubuntu, Bash, PowerShell 7, Build/Runtime und
   den beobachteten VS-Code-Pfad ueber Remote WSL und Dev Containers.
3. Beide Nachweise duerfen dieselbe physische Hardware und denselben geprueften
   Git-Head verwenden. Befehle, Start-/Endzeiten, Runner, Podman-Laufzeiten,
   Image-IDs, Exitcodes und VS-Code-Beobachtungen werden getrennt erfasst.
4. Ein Ergebnis der Windows-Podman-Machine darf nicht als Ergebnis des
   rootless Podman innerhalb von Ubuntu/WSL2 wiederverwendet werden. Ein
   Linux-Container auf macOS oder Windows ist ebenfalls kein Ersatz fuer den
   Ubuntu/WSL2-Ausfuehrungspfad.

*The two gates may share physical hardware and the reviewed Git head. They
must not share or duplicate commands, timing, runner identity, Podman runtime,
image identity, exit codes, or VS Code observations.*

## Unveraenderte Sicherheitsgrenzen / Unchanged Security Boundaries

- Der Ubuntu/WSL2-Lauf erfolgt als normaler Benutzer und muss rootless Podman
  nachweisen. / The Ubuntu/WSL2 run uses a normal user and must prove rootless
  Podman.
- Fehlende, fehlgeschlagene oder nur teilweise beobachtete Nachweise bleiben
  `Open` oder `Blocked`, nie `Pass` oder `N/A`. / Missing, failed, or partial
  evidence remains `Open` or `Blocked`, never `Pass` or `N/A`.
- Secrets, Providerdaten und lokale Kontodaten werden nicht protokolliert. /
  Secrets, provider data, and local account data are not recorded.
- Die Entscheidung schliesst kein anderes Gate, startet T066 nicht und erteilt
  keine formale Produkt-, Risiko- oder Plattformfreigabe. / This decision
  closes no other gate, does not start T066, and grants no product, risk, or
  platform approval.

## Ausgeschlossene Aussage / Excluded Claim

**DE:** Diese Entscheidung ist keine Abnahme auf nativer Linux-Hardware und
keine allgemeine Behauptung, dass sich WSL2 in allen Kernel-, systemd-,
Netzwerk-, Dateisystem- oder Runtime-Eigenschaften wie ein eigenstaendiger
Linux-Rechner verhaelt.

**EN:** This decision is not acceptance on native Linux hardware and does not
claim that WSL2 is equivalent to a standalone Linux machine for every kernel,
systemd, network, file-system, or runtime property.

## Neubewertungsausloeser / Re-evaluation Trigger

Neu bewerten, sobald native Linux-Hardware ein ausdrueckliches Zielsystem wird,
eine kernel-, systemd-, Netzwerk-, Dateisystem- oder Runtime-Abweichung
sicherheitsrelevant wird oder der Projekt-Scope native Linux-Kompatibilitaet
behauptet. / Re-evaluate when native Linux hardware becomes an explicit target,
a kernel, systemd, network, file-system, or runtime difference becomes
security-relevant, or project scope claims native Linux compatibility.

## Technische Referenzen / Technical References

- Microsoft WSL overview: <https://learn.microsoft.com/windows/wsl/about>
- Microsoft WSL systemd: <https://learn.microsoft.com/windows/wsl/systemd>
- Podman installation: <https://podman.io/docs/installation>
- VS Code Dev Containers: <https://code.visualstudio.com/docs/devcontainers/containers>
