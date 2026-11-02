# Mac-A-Coverage und Plattformuebergabe / Mac-A coverage and platform handoff

## Deutsch

### Status und Ausfuehrungsgrenze

Stand: 2026-11-02. Dies ist ein vorbereiteter Arbeitsauftrag fuer T041-T046
und T059-T061, **keine** abgeschlossene T069-Uebergabe oder Plattformabnahme.
Der inspizierte Ausgangscommit ist
`e115fa863e754a83eff212c72f130f6f8543a988`.
Neue lokale Artefakte sind uncommittet. Ein finaler, transportierbarer
Pruefstand nach T053 ist noch nicht benannt. Diesen Ausgangscommit nicht
als finalen Code-Freeze oder als Nachweis der neuen Tests ausgeben.

Die Anforderungen bleiben unveraendert: mindestens 85 % Zweig-Outcomes
je sicherheitskritischem Modul, mindestens 80 % logische Interfaces mit
positiven und negativen Faellen fuer **alle** beanspruchten Varianten,
100 % der neuen/geaenderten Interfaces. Keine Mittelung verschiedener
Messverfahren und keine Verkleinerung des Nenners wegen fehlender Plattformen.
Eine Mac-Messung ist kein Windows-/WSL2- oder Runtime-Nachweis.

### Reihenfolge und Verantwortliche

1. Maintainer: erneuerte Intake-/Reviewbindungen und aktuelle Quellhashes
   pruefen. Nicht allein auf ein historisches Ready oder passende Zielhashes
   vertrauen; alle gebundenen Quellen muessen passen. Bei Drift stoppen.
2. Mac-A-Maintainer: isolierte Python-Messung und zulaessige native
   Bash-/PowerShell-Fixtures ausfuehren. Messluecken bei Inline-Code,
   isolierten Interpretern und Kindprozessen separat erfassen. Kein
   persoenliches HOME, keine globalen Wartungslaeufe, kein Containerzugriff.
3. Maintainer und unabhaengiger Reviewer: T045-Lueckenbericht auswerten,
   gezielte T046-Korrekturen pruefen und erst danach T053 abschliessen.
   Bis dahin bleiben Quoten und Freeze Open.
4. Repository Owner: den gleichen finalen Stand durch eine gesondert
   autorisierte Lieferung oder ein explizit geprueftes Patchpaket zugaenglich
   machen. Head plus Patchhash bindet uncommittierte Eingaben; ein Git-SHA
   allein bezeichnet sie nicht. Kein Commit/Push durch diesen Auftrag.
5. Windows Platform Review und Ubuntu/WSL2 Platform Review: getrennte
   Laufzeiten und eigene Nachweise fuer denselben finalen Stand erstellen.
   Ein physischer Windows-Rechner fuer beide Pfade ist erlaubt.
6. Unabhaengiger Gesamt-Review: erst T068 bewertet das vollstaendige Paket.
   Rechts-, Provider-, Lizenz-, Usability- und A11Y-Entscheidungen bleiben
   getrennte menschliche Aufgaben.

### Mac-A-Messung

Host: macOS/ARM64, Repository-Wurzel. Die Messumgebung ist ein eigener
Temp-Pfad; keine globale Paketinstallation. Die Toolversion, Python-Version,
Wheel-SHA-256, Messkonfiguration, zehn Python-Quellhashes und Testdateihashes
werden im Messbericht gebunden. Coverage-Patch fuer Subprozesse ist
eingeschaltet, macht aber einen isolierten fremden Interpreter ohne
Messmodul nicht automatisch messbar.

Die Konfiguration liegt in
`scripts/tests/fixtures/hardening-followup/coverage-mac-a.ini`.
Der Ergebnisbericht unterscheidet je Datei
`covered_branches / num_branches`, fehlende Module und nicht zuordenbare
eingebettete Programme. Shell-/PowerShell-Zeilen, erfolgreiche Unittests und
ein Datei-Inventar sind keine gemessene Entscheidungsabdeckung.
Das vollstaendige Inventar mit 106 Dateien bleibt erhalten.

Reproduktion: ein eigenes temporaeres venv mit der im Messbericht
gebundenen Version vorbereiten, den dort angegebenen vollstaendigen argv
verwenden und HOME, Caches, Coverage-Daten sowie Git-Konfiguration auf eigene
synthetische Testorte begrenzen. Keine vorhandene Coverage-Datei fremder
Revisionen kombinieren. Bei fehlenden Werkzeugen oder unerwartetem Timeout
stoppen und den Fehler dokumentieren; keine stillen Installationen,
zusaetzlichen Launcher oder hoeheren Timeouts.

### Windows-Host: T060

Runner: `Windows-Host-PowerShell7-Podman`.
Voraussetzungen: eigener Checkout/Fork oder institutionelles Repo,
PowerShell 7, benoetigte native Testwerkzeuge, Windows-Podman-Machine,
VS Code Desktop und Dev Containers. Fehlende Werkzeuge nicht automatisch
installieren, keine Admin-Rechte oder Provider-Anmeldung voraussetzen.

Nach Quellenfreigabe auf dem **Windows-Host**, PowerShell 7,
aus der Repo-Wurzel, zuerst nur lesen:

```powershell
$PSVersionTable.PSVersion
git rev-parse HEAD
git status --porcelain=v1 --untracked-files=all
podman machine list --format json
podman info --format '{{.Host.Arch}} {{.Host.Security.Rootless}}'
```

Erwartung: vereinbarter finaler Head und exakt erklaerter Arbeitsbaum;
eigene Windows-Podman-Machine mit `amd64`, Rootless-Status pruefbar.
Kein laufender persoenlicher Container darf als Testfixture dienen.
Bei unerwartetem Head, fehlender Verbindung oder abweichender Architektur
stoppen; kein Machine-Reset oder automatischer Fallback.

Nur nach gesonderter Runtime-Autoritaet einen eigenen nativen
`linux/amd64`-Kandidaten bauen und Default/Read-only mit isolierten
Compose-Projekten pruefen. Die persoenliche `.env` und reale Mounts/Volumes
nicht wiederverwenden. Q5 im Feature-Quickstart beschreibt die Grenzen;
die dortigen ARM64-Beispiele sind keine unveraenderten Windows-Befehle.
Der Windows-Operator muss die native Befehlsfolge vor Ausfuehrung reviewen.
Beobachteten VS-Code-Attach und eine synthetische Dateioperation protokollieren;
installierte Erweiterungen allein genuegen nicht.

### Ubuntu unter WSL2: T061

Runner: `Ubuntu-WSL2-Bash-rootless-Podman`.
Voraussetzungen: eigener Checkout im Linux-Dateisystem, normaler Benutzer,
eigener direkt lokaler rootless Podman, Bash und PowerShell 7; VS Code ueber
Remote WSL und Dev Containers. Kein separater nativer Linux-Rechner gefordert.
Die Windows-Podman-Machine ist kein Ersatz fuer diesen eigenen Runtimepfad.

Nach Quellenfreigabe **in Ubuntu/WSL2**, Bash, aus der Repo-Wurzel lesen:

```bash
uname -a
id -u
pwd -P
git rev-parse HEAD
git status --porcelain=v1 --untracked-files=all
podman info --format '{{.Host.Arch}} {{.Host.Security.Rootless}}'
pwsh -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
```

Erwartung: gleicher finaler Git-Stand, Linux-Dateisystem statt `/mnt/c`,
UID ungleich 0, `amd64` und Rootless `true`. Zusaetzlich den tatsaechlich
verwendeten lokalen Podman-Endpunkt pruefen; ein Remote-Endpunkt zur
Windows-Machine erfuellt T061 nicht. Bei Abweichung stoppen und als
Open/Blocked dokumentieren, nicht auf rootful oder einen anderen Runner
ausweichen.

Auch hier erst nach Runtime-Autoritaet eigener Build, eigene Image-ID,
synthetische Compose-Daten und beobachteter Remote-WSL-/Dev-Containers-Attach.
Windows-Ergebnisse weder kopieren noch als WSL2-Ausfuehrung zaehlen.

### Nachweis je Fall und Fehlerhilfe

Pro Runner und Fall erfassen: finaler Head, optionaler Patchhash,
Eingabe-/Konfigurations-/Testhashes, echte UTC-Zeit, Shell/OS/Architektur,
argv und Ausfuehrungsort, Exitcode, erwartet/beobachtet, positive/negative
Fallart, Interface-ID/Variante, temporaerer Rohlog-Hash und Grenzen.
Runtimefaelle benoetigen zusaetzlich Image-ID, Build-Eingaben, Rootless-/
Non-root-/Capabilities-/Port-/Schreibgrenzen und beobachteten IDE-Zugriff.
Private Pfade redigieren; keine Tokens, Datenbank-, Prompt- oder Antwortinhalte.

Ergebnisort: `platform-windows.md` bzw. `platform-wsl2.md` in diesem
Verzeichnis. Coverage-Outcomes nur nach zuordenbarer echter Ausfuehrung
in den gemeinsamen Katalog uebernehmen. Skips und fehlende Varianten
bleiben im Nenner und werden mit Owner, Follow-up und Trigger gefuehrt.

- Open Q4: Owner Maintainer/Security Review; Follow-up Quellen und
  Messluecken schliessen; Trigger neuer Messlauf, Quell-/Test-/Katalogwechsel.
- Open Windows: Owner Windows Platform Review; Follow-up separater
  T060-Lauf; Trigger verfuegbarer Runner und finaler T053-Stand.
- Open WSL2: Owner Ubuntu/WSL2 Platform Review; Follow-up eigener rootless
  T061-Lauf; Trigger verfuegbarer Runner und finaler T053-Stand.
- Open Transfer: Owner Repository Owner; Follow-up finalen Stand gesondert
  bereitstellen; Trigger autorisierte Lieferung oder geprueftes Patchpaket.

Frist aller Plattformnachweise: vor jeweiligem Plattform-/Unterstuetzungsclaim.
Keine Sperren fremd entsperren, keine Auditfehler umgehen, keine
Volume-Loeschoption als normalen Stopp verwenden. Bei unerwartetem Fehler
Rohbeleg sichern, den betroffenen Schritt stoppen und an den Owner geben.
Aufraeumen nur eindeutig eigener Testressourcen nach Befundsicherung,
ohne globales Prune oder Neustart der Lernumgebung.

## English

### Status and limits

Dated 2026-11-02. This prepares T041-T046 and T059-T061, not completed T069
handoff or platform acceptance. The inspected base commit is recorded above.
Local additions are uncommitted; no final transportable T053 revision is
designated. Do not label that base SHA as a final freeze or proof of new tests.

Keep at least 85% branch outcomes per critical module, 80% logical interfaces
with both case types for every claimed variant, and both case types for every
changed interface. Do not average unlike metrics or remove missing platforms
from the denominator. Mac execution proves neither Windows/WSL2 nor runtime.

### Order and owners

The maintainer first verifies current receipt, source and independent review
bindings, stopping on drift. The Mac-A maintainer then runs isolated Python
measurement and permitted native Bash/PowerShell fixtures, explicitly retaining
embedded/child/isolated-interpreter gaps. Never use personal HOME, global
maintenance or the live container as fixtures. Review T045 gaps, make targeted
T046 corrections and complete T053 only after final measurement.

The repository owner must separately authorize delivery of the final revision
or an explicitly reviewed patch package. A Git SHA alone does not identify
uncommitted changes. This request performs no commit/push. Windows and WSL2
reviewers use the same final inputs but distinct runtimes and evidence; one
physical Windows computer is sufficient. T068 and all human legal, provider,
rights, accessibility and usability decisions remain separate.

### Mac measurement

Use a disposable macOS ARM64 environment and bind Python/tool versions, wheel
SHA-256, measurement configuration and all ten Python/test source hashes.
The configuration path above is authoritative for this slice. Enabling
subprocess patching does not measure an unrelated isolated interpreter without
the tool. Report per-file covered/total branches, absent modules and unattributed
embedded code. Shell/PowerShell lines, passing tests and file inventories are
not decision coverage. Preserve the full 106-file scope.

Reproduce using an owned temporary venv and the report's complete argv, with
synthetic HOME, caches, coverage data and Git configuration. Never combine
different revisions. Missing tools/timeouts block; no silent installation,
extra launchers or larger timeout budgets.

### Windows and WSL2

Use the separate runner names and read-only command blocks above, in their
stated native shells and repository roots, only after input approval.
Windows requires PowerShell 7, its Podman Machine, native AMD64 tooling,
VS Code Desktop/Dev Containers and an owned checkout. WSL2 requires its own
Linux-filesystem checkout, nonzero UID, Bash/PowerShell 7 and direct local
rootless Podman on AMD64, not the Windows remote machine. Verify the actual
endpoint as well as the reported architecture/rootless status. Missing
prerequisites or wrong inputs stop the path without automatic installs,
elevation, resets or rootful fallback. Native Linux hardware is not required.

Only separately authorized runtime work may build candidates and exercise
default/read-only Compose with owned synthetic data/volumes and observed
editor attachment. Never reuse personal env files or the learner service.
Q5 describes safety limits, not a ready-to-run unchanged ARM64 command set for
Windows. The native operator must review its command sequence first.
An installed extension is not observed attachment. Windows results cannot be
copied as WSL2 results.

### Evidence, recovery and open work

For each runner/case record final head/patch, input/config/test hashes, UTC
time, OS/shell/architecture, argv/location, actual exit and expected/observed
result, positive/negative case, interface/variant, raw-log hash and limitations.
Runtime evidence additionally binds image/build inputs, rootless/non-root,
capabilities, ports, write boundaries and observed IDE access. Redact private
paths; never export confidential contents. Keep native evidence in the two
platform documents named above, adding catalog outcomes only after actual
attributable execution. Skips remain in the denominator.

Open Q4 belongs to Maintainer/Security Review and reopens on source/test/catalog
changes. Windows and WSL2 reviewers own separate T060/T061 runs after final
T053 inputs and runner availability. The repository owner separately owns
transfer authority. Platform evidence is due before the respective support
claim. Stop unexpected failures, retain raw evidence and contact the owner;
never unlock foreign locks or bypass audit failures. Preserve volumes on
normal shutdown and clean only inventoried own test resources, not global
storage or the learner service.
