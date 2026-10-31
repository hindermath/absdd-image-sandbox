# Plattform- und Schreibgrenzen / Platform and write boundaries

Stand: 2026-10-31. Quelle: `Dockerfile`, `compose.yml`,
`compose.home-baseline.yml`, `compose.read-only.yml`. Dies ist ein
Konfigurationsinventar; native Laufzeitbelege folgen getrennt.

## Default

Der Prozess läuft laut letztem `USER` im Dockerfile als `adedev`, nicht als
Root. Compose entfernt alle Linux-Capabilities, setzt `no-new-privileges`,
veröffentlicht 5100–5199 nur an `127.0.0.1` und nutzt den normalen
Compose-Netzwerkmodus. Das Image-Dateisystem bleibt im Default beschreibbar.
Dateirechte der Host-Bind-Mounts werden vom Host vorgegeben; ein Nicht-Root-
Container macht diese Mounts nicht automatisch schreibgeschützt.

Beschreibbare Projekt-Bind-Mounts sind `/workspace`, `/ade-dev-sandbox`,
`/rider-projects`, `/java-projects`, `/go-projects`, `/rust-projects`,
`/python-projects`, `/powershell-projects`, `/swift-projects` sowie die drei
Secure-*-Projektorte. `/audit` ist der Host-Auditbereich. Das
`dotnet/ContainerBuild.props`-Bind-Mount ist `ro`. Getrennte benannte Volumes
halten `dotnet_build` und die Zustände von OpenCode, Codex, Claude, Gemini
und Copilot. Das optionale Home-Baseline-Override bindet einen persönlichen
Checkout beschreibbar über `/opt/home-baseline`; ohne Override ist die
eingebettete Referenz schreibgeschützt. Temporäre Dateien liegen unter
`/tmp`; Agenten und Sprachwerkzeuge können zusätzliche Caches im Home
anlegen. Host-Dateirechte und konkrete UID-Zuordnung sind vor Nutzung
jeweils zu prüfen.

## Optionales Read-only-Profil

`compose.read-only.yml` setzt nur das Container-Root-Dateisystem auf
`read_only`. Drei tmpfs-Orte erlauben temporäre Dateien (`/tmp`),
Laufzeitdateien (`/run`) und einen nicht persistenten Benutzer-Cache
(`/home/adedev/.cache`). Fünf nur hier verwendete Volumes halten
OpenCode-, .NET- und PowerShell-Home-Zustand an eng begrenzten Pfaden
beschreibbar; Podmans `:U` ordnet ihren Inhalt der Container-UID zu.
Sie sind persistent und gehören zur optionalen Agenten-/Toolchain-Grenze.
Die Projekt-Bind-Mounts und übrigen benannten Volumes bleiben beschreibbar.
`USER`, Capability-Drops, `no-new-privileges` und
Loopback-Portbindung bleiben aus `compose.yml` erhalten. Andere
Home-Schreiborte einzelner Werkzeuge können mit diesem Profil scheitern;
der getrennte ARM64-Test belegt nur die unten genannten Smokes. Es ist eine ausdrückliche Wahl,
keine Änderung des Defaults und keine Behauptung über Host-Dateischutz.
Der native ARM64-Kandidat meldete für `adedev` UID/GID 1655. Podman 6.1.4
lehnte `uid=1655,gid=1655` als tmpfs-Mountoption ab. Der Cache nutzt daher
einen flüchtigen Sticky-Bit-Bereich wie `/tmp` (`mode=1777`); er ist kein
privater Credential-Speicher. Bei neuer Podman- oder Basisversion sind
Benutzerzuordnung und tmpfs-Semantik erneut zu prüfen.

Auf dem Host im Repository ausführen, mit Podman Compose Provider und
vorhandener `opencode.env`:

```sh
podman-compose -f compose.yml -f compose.read-only.yml config
```

Erwartet wird eine gültige Compose-Konfiguration mit `read_only: true`.
Bei einem Fehler zuerst die ausgegebene Pfad-/Compose-Meldung prüfen;
keine Volumes löschen und keinen laufenden Lerncontainer für diesen
Konfigurationstest ersetzen.

## T058: nativer macOS-ARM64-Vorlauf (31.10.2026)

**Autorität:** Der Repository Owner hat einen **separaten Test-Build** auf
macOS ARM64 erlaubt und anschließend einen **getrennten Test-Container mit
synthetischen Mounts/Volumes** freigegeben. Ein VS-Code-Attach muss weiterhin
als tatsächliche Beobachtung nachgewiesen werden.
Windows und Ubuntu/WSL2 stehen nicht bereit. Die bestehende Lernumgebung
blieb unangetastet. Die Tabelle dokumentiert den Vorlauf; die späteren
Build- und Runtime-Ergebnisse stehen im T059/T062-Abgleich darunter.

| Vorbedingung | Beobachtung am 31.10.2026 | Konsequenz |
| --- | --- | --- |
| Host und Werkzeuge | `Darwin arm64`; `pwsh`, `podman` und `podman-compose` vorhanden; Host-Dateisystem ca. 45 GiB frei. | Native ARM64-Kandidatenplanung möglich; Platz vor dem tatsächlichen Build erneut messen. |
| Podman-Machine | `podman-machine-default` läuft mit AppleHV, 6 CPUs, 73-GiB-Disk und ca. 46 GiB frei im VM-Dateisystem `/var`; Rosetta aus. | Keine neue Machine starten oder bestehende umkonfigurieren. Größe/Platz bleiben eine aktuelle Beobachtung, keine Build-Garantie. |
| Dynamischer Endpunkt | `podman machine inspect` lieferte `.ConnectionInfo.PodmanSocket.Path`; Datei wurde als Socket verifiziert. Der konkrete Hostpfad und der dynamische SSH-Port werden nicht gespeichert. | Endpunkt für spätere Befehle jeweils neu ermitteln. Die Machine-Standardverbindung ist derzeit **rootful**; `podman --connection podman-machine-default info` bestätigte für die ausdrücklich gewählte Verbindung `Rootless=true`. Den Standardendpunkt nicht für einen als rootless behaupteten Test verwenden. |
| Geschützte Runtime | In der rootful Verbindung existiert der gestoppte Lerncontainer `absdd-image-sandbox_ade_1`. Bestehendes Lern-Image `localhost/absdd-image-sandbox_ade:latest`, Aktivierungs- und Recovery-Tag sowie sechs benannte Projektvolumes (`opencode_data`, `codex_data`, `dotnet_build`, `claude_data`, `gemini_data`, `copilot_data`) und zwei unbenannte Volumes wurden nur gelesen. Die rootless Verbindung hatte zum Abfragezeitpunkt keine Container, Images oder Volumes. | Keine vorhandenen Container, Tags oder Volumes ersetzen, löschen, starten oder mit Testdaten verbinden. Rootless Kandidat nur mit eigenem Namen und eigener Verbindung. |
| Getrennte Testnamen | Image-Tag `localhost/absdd-feature004-arm64:20261031-candidate`; Compose-Projekt `absdd-feature004-arm64-20261031`; synthetische Testpfade unter `/private/tmp/feature004-arm64-20261031-test`. | Nur die rootless Verbindung und synthetische Projekt-/Agentendaten wurden verwendet. Kein echter Credential- oder Lern-Volume-Mount. |

**T059/T062-Abgleich:** Der separate rootless ARM64-Kandidat wurde mit
`--pull` gebaut. Default und optionales Read-only liefen mit synthetischen
Mounts; beide vollständigen Toolchain-Smokes, JSON- und Dokumentationsmodi
endeten nach der engen Read-only-Korrektur mit Exit 0. Aktuelle Audit-Runs
wurden vor dem jeweiligen `down` verifiziert; Volumes blieben erhalten.
Image-ID, Eingaben, erste Fehler und Korrekturen stehen in
`platform-macos.md`. Ein tatsächlicher VS-Code-Attach fehlt; T059/G004-15
bleiben teilweise Open. Das Read-only-Profil hat fünf zusätzliche
persistente Zustandsvolumes und Swift-Cache-Warnungen. T060/T061 bleiben
mangels Windows-/WSL2-Runner als `UPD-AMD64` Open/Blocked.

**UPD-SMOKE-WARN:** Swift 6.4.1 startete direkt als Binary und über
`swift run` mit gleicher Ausgabe. Nur der Runner meldete `safeExec`
`signal(32/33)`; im Read-only-Lauf warnte Swift zudem über seine nicht
beschreibbaren `.swiftpm`-Caches. Poppler `24.02.0-1ubuntu9.11` meldete
`Suspects object is wrong type (boolean)` bei sonst erfolgreichem
PDF-Funktionstest. Keine Warnung wurde gefiltert. Owner: Platform Review;
Trigger: Podman-/Swift-/Poppler-Update oder Plattformnachtest. Daraus
folgt keine Aussage zur PDF-Barrierefreiheit.

## English

The final Dockerfile user is `adedev`. Compose drops all Linux capabilities,
sets `no-new-privileges`, and publishes ports 5100–5199 on loopback only.
The default image filesystem, project bind mounts, audit mount, and separate
agent/build volumes are writable. The host controls bind-mount permissions.
The optional Home Baseline override mounts a writable personal checkout;
the embedded reference is read-only without it.

The optional `compose.read-only.yml` makes the container root filesystem
read-only and supplies temporary `/tmp`, `/run`, and user cache paths. Five
separate named volumes keep required OpenCode, .NET and PowerShell home
state writable; Podman's `:U` maps ownership to the container user. Project
mounts and other named volumes remain writable. The separate ARM64 tests
passed the named smokes after narrow profile corrections, but other tools
may need different home paths. Run the configuration
command above on the host with a Compose provider and `opencode.env` present.
It should show `read_only: true`. If it fails, inspect the reported path or
Compose error. Do not remove volumes or replace the live learner container.
The tested ARM64 image reports UID/GID 1655 for `adedev`. Podman 6.1.4
rejected `uid/gid` as tmpfs options, so the transient cache uses a sticky
`mode=1777` area like `/tmp`; it is no private credential store. Recheck user
and tmpfs behavior after a Podman or base-image change.

**T058–T062, 31 October 2026:** The Owner authorised a separate macOS
ARM64 test build and, in a later reply, a separate test container with
synthetic mounts and volumes. Both isolated Compose profiles passed the
full language, JSON, documentation and current-audit checks after the
profile correction. A real VS Code attach was not observed.
The AppleHV Podman machine is running with Rosetta off;
approximately 45 GiB was free on the host and 46 GiB in its VM `/var` at the
check. Its dynamically reported socket is a real socket, but the default
machine connection is rootful. The explicitly selected
`podman-machine-default` connection reports `Rootless=true` and had no
containers, images or volumes. The rootful connection holds the stopped
learner container, existing image tags and six named plus two anonymous
volumes, all protected from candidate work. The candidate tag and temporary
test names above were used only in the rootless connection. Swift 6.4.1
and Poppler 24.02.0-1ubuntu9.11 produced the warnings documented above;
none was suppressed or interpreted as PDF accessibility proof. Windows
and Ubuntu/WSL2 native evidence remain `UPD-AMD64` Open/Blocked.
