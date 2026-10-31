# macOS ARM64: getrennter Kandidat / separate candidate

**Stand:** 2026-10-31. T059 ist teilweise belegt und bleibt Open.
Host: macOS `arm64`, AppleHV, Rosetta aus, Podman 6.1.4. Alle
Containeraktionen nutzten ausdrücklich die Verbindung
`podman-machine-default` mit `Rootless=true` und `arm64`. Die rootful
Lernumgebung wurde nicht gestartet, ersetzt oder gemountet.

## Build und Eingaben

Der getrennte Kandidat wurde aus dem uncommitteten Feature-004-Arbeitsbaum
auf Git-Head `51757c98f6a872419be6b9ae4d33685fe0782b67` gebaut:

```sh
podman --connection podman-machine-default build --pull --platform linux/arm64 -t localhost/absdd-feature004-arm64:20261031-candidate .
```

Die Basis blieb `mcr.microsoft.com/dotnet/sdk:10.0@sha256:747cbade5bfd918a175ac32f8f1d931edec2c7d0d5397a3de72eaef1ac1f66d2`.
Der erste Build scheiterte bei `dotnet tool update` trotz korrekter
PowerShell-Nupkg-Prüfsumme mit `Invalid cross-device link` im rootless
Overlay. Die Korrektur installiert das geprüfte Paket separat nach
`/opt/powershell-pinned`, bindet `/usr/bin/pwsh` darauf und verifiziert
die Version. Der zweite Build endete mit Exit 0. Die Image-ID ist
`b0cdf23d43df34458040743a3f0abd09c26b8619f5a1c9b93f89f07ad30f830d`
(Linux ARM64; erstellt 2026-10-31 15:56:43 UTC). Das ist ein
Testkandidat, nicht das finale Image aus T063.

## Getrennte Compose-Läufe

Der Compose-Test verwendete das eigene Projekt
`absdd-feature004-arm64-20261031`, synthetische Projekt-, Audit- und
Agentenorte unter `/private/tmp/feature004-arm64-20261031-test`, eine
leere `opencode.env` und eigene benannte Volumes. Es gab keine echten
Projekt- oder Credential-Mounts. Der Default-Lauf mit `--no-build`
endete erfolgreich: `adedev` UID/GID 1655, `no-new-privileges`, alle
üblichen elf Linux-Capabilities entfernt, Port 5199 nur auf
`127.0.0.1`. Der vollständige vorhandene Toolchain-Smoke baute und
startete alle sechs Sprachbeispiele mit Exit 0; der JSON-Modus und
Dokumentations-Smoke endeten ebenfalls mit Exit 0. Der aktuelle
Audit-Export und sein Run-Record wurden vor `down` mit dem
Retention-Verifier geprüft (`sessionMetadataCount=0`). `down` erfolgte
ohne `-v`.

Das optionale `compose.read-only.yml` ergab zur Laufzeit
`ReadonlyRootfs=true`; ein Schreibversuch nach `/home/adedev` scheiterte
mit `EROFS`, während `/home/adedev/.cache` flüchtig beschreibbar war.
Podman 6.1.4 akzeptierte für tmpfs keine `uid/gid`-Option; deshalb
verwendet der Cache `mode=1777`. OpenCode benötigte zusätzlich ein
eigenes `opencode_state`-Volume für `/home/adedev/.local/state`; nach
dieser Korrektur liefen `opencode --version`, der JSON-Modus, der
Dokumentations-Smoke sowie der aktuelle Audit-Export und dessen
Run-Record-Verifikation erfolgreich. Der letzte geprüfte Read-only-
Audit-Run war `6ee2b81b-068a-416f-9eba-6e3bd583e475` mit sechs
Records und null Session-Metadaten. Auch dieser Container wurde ohne
Volumelöschung gestoppt.

Der erste vollständige Read-only-Toolchain-Smoke endete mit Exit 1:
.NET benötigte `/home/adedev/.dotnet` und später `.templateengine`;
PowerShell benötigte `/home/adedev/.local/share/powershell`. Ein
Zwischenversuch mit `DOTNET_CLI_HOME=/dotnet-build` traf auf einen
`NuGet-Migrations`-Mutex-Fehler. Eng begrenzte, eigene Volumes für diese
Pfade und `.nuget` wurden ergänzt. Der anschließende vollständige
Toolchain-Smoke endete mit Exit 0 und baute/startete die sechs
Sprachbeispiele. Swift meldete im Read-only-Profil zusätzlich, dass
`/home/adedev/.swiftpm/configuration` und `security` für seinen
Benutzercache nicht beschreibbar sind; der Build und Start gelangen.
Der letzte aktuelle Audit-Run `02657395-4041-4fa2-a6b3-4c292b844ebf`
war vor `down` verifiziert (sechs Records, null Session-Metadaten).

**Offene Grenze G004-15:** Ein tatsächlicher VS-Code-Dev-Containers-
Attach wurde nicht beobachtet; die installierte Extension allein belegt
ihn nicht. T059 bleibt daher teilweise offen. Die fünf zusätzlichen
Read-only-Zustandsvolumes müssen für reale Nutzung und Retention noch
bewertet werden.

Swift startete als direktes Binary und per `swift run` mit gleicher
`Hello, world!`-Ausgabe. Nur `swift run` meldete vier Zeilen auf stderr,
darunter `safeExec signal(32/33)`. Poppler `24.02.0-1ubuntu9.11` meldete
bei sonst erfolgreichem Dokumentations-Smoke `Syntax Error: Suspects
object is wrong type (boolean)`. Beide Warnungen bleiben
`UPD-SMOKE-WARN`; sie wurden weder gefiltert noch als PDF-A11Y-Beleg
interpretiert.

## English

On 31 October 2026, a separate rootless Linux ARM64 image built
successfully from the uncommitted Feature 004 tree at the Git head above.
The first build exposed an overlay cross-device failure during the in-place
PowerShell update; a separate verified installation fixed the build. The
candidate image ID is recorded above and is not the final T063 image.

An isolated Compose project used synthetic mounts, empty provider settings,
and its own volumes. The default profile passed all six language examples,
JSON and documentation smokes, UID/capability/loopback checks and current
audit-run verification. The optional read-only profile passed root-filesystem,
OpenCode, JSON, documentation and audit checks after adding a separate
OpenCode state volume. An initial full language smoke failed on .NET and
PowerShell home writes; dedicated state volumes for those paths,
`.templateengine` and `.nuget` allowed the next full smoke to pass. Swift
still warned about its unavailable user cache. A real VS Code attach was
not observed. T059 and G004-15 therefore remain partially open. Swift
`swift run` and Poppler emitted the
specific warnings recorded above; they were not filtered or treated as
accessibility evidence. Both test containers were stopped without deleting
volumes, and the learner environment was untouched.
