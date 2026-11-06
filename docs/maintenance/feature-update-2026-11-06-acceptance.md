# Feature-Update #101/#102/#104: Abnahme / Acceptance

## Deutsch

Stand: 2026-11-06, unveröffentlichter Arbeitsbaum bei
8adfac3f46af603198340058ad3ce49583b4b45f.
Host macOS ARM64 (`Darwin 27.2.0`), Podman 5.8.2 auf Linux ARM64;
Pruefstand 2026-11-06 21:05 UTC. Die Image-IDs sind Kandidaten,
keine formale Freigabe. #98 bleibt geschlossen. Model Routing 0.2.6 und
Autonomous Run 0.4.10 werden nur auf Erhalt geprüft; kein autonomer Lauf.
Gemeinsame Versionen aller ARM64-Profile: Ubuntu 26.04, .NET-SDK 10.0.403
mit Kompatibilitaets-SDK 10.0.303, PowerShell 7.6.9, Node 24.22.2,
npm 12.2.2, OpenCode 2.1.4 und Syft 1.55.0. Die Sprachen stehen pro
Profilzeile; alle sieben finalen Builds verwendeten `--pull`.

| Nachweis | Ergebnis |
|---|---|
| Compose | podman-compose config Exit 0; ade-all als Standardziel, App-Ports 5100–5198 und OpenCode 5199 auf Loopback, Compose-Healthcheck vorhanden |
| Pins | Pin-Register Exit 0 und 75 Offline-Assertions; Basisdigest und Swift 6.4.2 für AMD64/ARM64 geprüft; finaler read-only PowerShell-Checker im ARM64-`all`-Image `Ready`, Exit 0, 28 Quellgruppen, siehe [Versionsnachweis](toolchain-version-audit-2026-11-06.md) |
| .NET-Ausgabe | isolierter MSBuild-Test Exit 0; verschiedene Mountpfade erzeugen verschiedene /dotnet-build-Pfade und importieren Projekt-Props |
| ARM64 ade-dotnet Vorabimage | Pull-Build Exit 0, ID sha256:365155fd70a96be353dd0e110df423cd1d638f5f1950c77776fd5b5da0fdfc66; vor Swift-6.4.2- und Healthcheck-Endstand gebaut |
| OpenCode 2.1.4 | Authentifizierte Bereitschaft 200, ohne/falsches Passwort 401; Webtest Exit 0 vor und nach Neustart; falscher Healthcheck Exit 1 ohne Ausgabe |
| TUI und Browser | opencode-tui und opencode-tui-mini interaktiv geöffnet, Exit 0, kein Modellaufruf; run --server-Syntax akzeptiert; Browser-Anmeldung erfolgreich, beschriftete Steuerelemente und Tab-Fokus beobachtet |
| Passwort und Port | Beispielpasswort Exit 1 ohne Secret-Ausgabe; zweiter Container auf Port 5199 Exit 126 wegen belegtem Port; synthetischer Wert nicht im Serverlog |
| Compose-Healthcheck | Isolierter Service zuerst starting, dann healthy; bei falschem Passwort Exit 1 ohne Ausgabe; ohne Volume-Löschung gestoppt |
| .NET-Probe | dotnet new console und dotnet run Exit 0, Hello, World!; java, go, rustc, python, swift fehlen im dotnet-Profil |
| Finale ARM64-`all`-Probe | Pull-Build Exit 0, ID `sha256:e683d7c22bcd8d11db3a1502deaf093ed40fac488fe503bbdc426ea3b92d431e`; Profil-Label und Manifest `all`, Docker-Healthcheck vorhanden; vollständiger Toolchain-, Projekt- und Dokumentations-Smoke Exit 0 |
| Finales ARM64-`all`-Web | synthetisches Passwort, OpenCode-2.1.4-Bereitschaft und 401/200-Probe Exit 0, Container `healthy`; `opencode-tui`, `opencode-tui-mini` und `run --server` vorhanden; isolierter Testcontainer ohne Volumes gestoppt und entfernt |
| Finale ARM64-`all`-SBOM | `sboms/2026-11-06-localhost-ade-feature-all-test-all-arm64-e683d7c22bcd.cdx.json`, CycloneDX 1.7, 34285 Komponenten, ungetrackt |
| Finale ARM64-`dotnet`-Probe | Pull-Build Exit 0, ID `sha256:f56a6e3d3433d8f54a0800d2d12722090ffff9d4b46eef58445de3eaa50a7729`; vollstaendige .NET-/Policy-/Dokumentationsprobe und Ausschlussbefehle Exit 0; CycloneDX 1.7 mit 31374 Komponenten ungetrackt |
| Compose-Profilwechsel | isoliertes Projekt `adefeatureswitch`: `all` → Audit-Wrapper-Stop → `dotnet` → Audit-Wrapper-Stop, alle Exit 0; Profilmanifest wechselte, synthetischer Marker im benannten `opencode_data`-Volume blieb, Webbereitschaft nach Wechsel Exit 0. Testvolume nicht geloescht |
| Direkter und Compose-Build | direkter `podman build --pull --format docker` ohne Ziel ergab ID `e683d7c22bcd`, Label `all`, Exit 0; isoliertes `podman-compose build --pull` mit `BUILDAH_FORMAT=docker` ergab fuer Standard `all` dieselbe ID und fuer `ADE_MSL_PROFILE=swift` ID `f14a47bac9ae`, Label `swift`, je Exit 0; `invalid` scheiterte vor dem Build mit Exit 125 (`target not found`) |
| Finale ARM64-`java`-Probe | Pull-Build Exit 0, ID `sha256:8a626cc7def1c2444f630f07153e932758867b51781f234cb6ad1212a1862724`; OpenJDK 25.0.4.1, Maven 3.10.0, Java-Projekt und Ausschlussbefehle Exit 0; Webbereitschaft Exit 0; CycloneDX 1.7 mit 31780 Komponenten ungetrackt |
| Finale ARM64-`go`-Probe | Pull-Build Exit 0, ID `sha256:f295d493210ceb2b46c983351a1c7ccb73c616c962a7d1b2cf85bc6e203259b9`; Go-1.27.3-Projekt, Analysewerkzeuge und Ausschlussbefehle Exit 0; Webbereitschaft Exit 0; CycloneDX 1.7 mit 32213 Komponenten ungetrackt |
| Finale ARM64-`rust`-Probe | Pull-Build Exit 0, ID `sha256:3b59ec43d3b8ec6c22f6f0e34a6c737d91d14d429ed4411d57f724dd369eb3dd`; Rust-1.99.1-Projekt, Clippy und Ausschlussbefehle Exit 0; Webbereitschaft Exit 0; CycloneDX 1.7 mit 32599 Komponenten ungetrackt |
| Finale ARM64-`python`-Probe | Pull-Build Exit 0, ID `sha256:84d0c5910b13954df0c2fab4f79b34bf315ba19e85771b501a5bf72ec9749126`; CPython 3.15.2 unter `/opt/cpython`, getrenntes Ubuntu-Python 3.14.4, Venv-Projekt und Ausschlussbefehle Exit 0; Webbereitschaft Exit 0; CycloneDX 1.7 mit 31815 Komponenten ungetrackt |
| Finale ARM64-`swift`-Probe | erster Versuch Exit 125 (`no space left on device` beim Layer-Schreiben), nach gezielter Entfernung eigener gepruefter Testimages erneuter Pull-Build Exit 0, ID `sha256:f14a47bac9ae9ec58e6ce4626cf9c4c69d019217513b4dd1e022759fe6e7a1b6`; GPG-Signatur/Fingerprint, Swift 6.4.2, Paketprojekt, SourceKit-LSP und Ausschlussbefehle Exit 0; Webbereitschaft Exit 0; CycloneDX 1.7 mit 31374 Komponenten ungetrackt |
| #98-Presets | Repo-Presets und Quellen-Lock weiterhin `model-routing-governance` 0.2.6 und `autonomous-run-governance` 0.4.10; `specify`-Version und `specify check` im finalen `all`-Smoke Exit 0; kein autonomer Lauf |
| Statische Abschlusspruefung | `pre-commit run --all-files` samt Secret-Scan Exit 0; `git diff --check`, Pin-Register und Dokumentationsbefehle Exit 0 |

## Finale Profilmatrix / Final profile matrix

Jedes finale Profil braucht nativen Build, Laufzeit, Sprach- und Ausschlussprobe
sowie eine frische, ungetrackte CycloneDX-SBOM.

| Ziel / Target | Probe UTC 2026-11-06 | ARM64 nativ / native | AMD64 nativ / native | finale SBOM |
|---|---|---|---|---|
| ade-dotnet | 19:43 | Pull-Build, .NET-/Policy-/Dokumentations- und Ausschlussprobe Exit 0; ID `f56a6e3d3433`; lokales Testimage spaeter aus Platzgruenden entfernt / passed, local test image later removed for space | nicht verfügbar / unavailable | CycloneDX 1.7 erzeugt / created |
| ade-java | 19:57 | Pull-Build, Java-Projekt, Ausschluss- und Webprobe Exit 0; ID `8a626cc7def1`; lokales Testimage danach aus Platzgruenden entfernt / passed, local test image removed for space | nicht verfügbar / unavailable | CycloneDX 1.7 erzeugt / created |
| ade-go | 20:10 | Pull-Build, Go-Projekt, Ausschluss- und Webprobe Exit 0; ID `f295d493210c`; lokales Testimage danach aus Platzgruenden entfernt / passed, local test image removed for space | nicht verfügbar / unavailable | CycloneDX 1.7 erzeugt / created |
| ade-rust | 20:22 | Pull-Build, Rust-Projekt, Clippy, Ausschluss- und Webprobe Exit 0; ID `3b59ec43d3b8`; lokales Testimage danach aus Platzgruenden entfernt / passed, local test image removed for space | nicht verfügbar / unavailable | CycloneDX 1.7 erzeugt / created |
| ade-python | 20:32 | Pull-Build, Python-Venv-Projekt, System-Python-, Ausschluss- und Webprobe Exit 0; ID `84d0c5910b13`; lokales Testimage spaeter aus Platzgruenden entfernt / passed, local test image later removed for space | nicht verfügbar / unavailable | CycloneDX 1.7 erzeugt / created |
| ade-swift | 20:55 | Pull-Build nach Speicherfreigabe, Swift-Projekt, Signatur-, Ausschluss- und Webprobe Exit 0; ID `f14a47bac9ae` / passed after freeing space | nicht verfügbar / unavailable | CycloneDX 1.7 erzeugt / created |
| ade-all | 19:30 | Pull-Build, Sprach-/Projekt-/Dokumentationsprobe und Webtest Exit 0; ID `e683d7c22bcd` / passed | nicht verfügbar / unavailable | CycloneDX 1.7 erzeugt / created |

Windows/WSL2, native AMD64, vollständige WCAG-2.2-AA-Prüfung,
formale Sandbox- oder Plattformfreigaben sind offen. Echte Compose-Services werden regulär über
den Audit-Wrapper gestoppt; der isolierte Testservice hatte keine Bestandsvolumes.

## English

Status: 2026-11-06, unpublished working tree at the Git head above. The host
is macOS ARM64 (`Darwin 27.2.0`); Podman 5.8.2 runs on Linux ARM64. Evidence
was current at 2026-11-06 21:05 UTC. Candidate images are
not formal approval. #98 remains closed. Model Routing 0.2.6 and Autonomous
Run 0.4.10 are checked for retention without starting an autonomous run.
All seven ARM64 profiles share Ubuntu 26.04, .NET SDK 10.0.403 and
compatibility SDK 10.0.303, PowerShell 7.6.9, Node 24.22.2, npm 12.2.2,
OpenCode 2.1.4 and Syft 1.55.0. Each final build used `--pull`; selected
language versions appear in the profile evidence rows.

Compose config, the pin registry, 75 offline assertions and the isolated
MSBuild output-path test passed. The final read-only PowerShell pin checker
ran in the ARM64 `all` image with source access: 28 groups, overall `Ready`,
exit 0. The version record includes the verified archive hashes. The preliminary ade-dotnet ARM64 image built with pull and ran a .NET
10 console project. OpenCode 2.1.4 returned 401 without or with wrong
credentials and 200 after authenticated readiness, also after restart. Both
full-screen and mini TUIs opened and exited without a model call. A placeholder
password and a second listener on port 5199 failed. The isolated Compose
service became healthy; its check exited 1 without output on a wrong password.
Browser sign-in worked, controls were labelled and keyboard Tab reached the
home control. This is partial accessibility evidence.

The preliminary image predates final Swift and healthcheck changes. The matrix
records the seven completed native ARM64 profile builds, language and absence
checks, and fresh untracked SBOMs. Native AMD64, Windows/WSL2, complete WCAG 2.2 AA review,
and formal decisions remain open. Routine shutdown of a real Compose service
uses the audit wrapper.

The final native ARM64 `all` image has ID
`sha256:e683d7c22bcd8d11db3a1502deaf093ed40fac488fe503bbdc426ea3b92d431e`.
Its full toolchain, project and documentation smoke passed. The profile label,
manifest and image healthcheck match. Synthetic-password web readiness,
401/200 authentication and container health passed; the isolated web test
container was stopped and removed without volumes. An untracked CycloneDX 1.7
SBOM with 34,285 components was created for this exact image. The full
pre-commit run, including secret scan, and the static pin and documentation
checks passed.

The final ARM64 `dotnet` image has ID
`sha256:f56a6e3d3433d8f54a0800d2d12722090ffff9d4b46eef58445de3eaa50a7729`.
Its full .NET, policy and documentation smoke passed, including absent
commands for excluded development toolchains. Its untracked CycloneDX 1.7
SBOM contains 31,374 components.
The checked local `dotnet` image was later removed to free VM space for the
Swift solo build; its SBOM and recorded image ID remain as evidence.

An isolated Compose project switched from `all` to `dotnet`. Both shutdowns
used the audit wrapper and exported seven metadata lines each. The profile
manifest changed as requested, a synthetic marker persisted in the named
OpenCode volume, excluded commands were absent, and authenticated web
readiness passed after recreation. The test volume was preserved.

A direct build with pull and no target produced the same `all` image ID and
label. An isolated Compose build with `BUILDAH_FORMAT=docker` selected `all`
by default and the final Swift image for `ADE_MSL_PROFILE=swift`; both exited
0. An invalid value failed before building with exit 125 because the target
did not exist. The isolated Compose fixture used its own image tag.

The final ARM64 `java` image has ID
`sha256:8a626cc7def1c2444f630f07153e932758867b51781f234cb6ad1212a1862724`.
OpenJDK 25.0.4.1, Maven 3.10.0, the Java project, excluded commands and
authenticated web readiness passed. Its untracked CycloneDX 1.7 SBOM has
31,780 components.
The checked local Java image was then removed to free VM space; its SBOM and
recorded image ID remain as evidence.

The final ARM64 `go` image has ID
`sha256:f295d493210ceb2b46c983351a1c7ccb73c616c962a7d1b2cf85bc6e203259b9`.
Go 1.27.3, the project test, analysis tools, excluded commands and
authenticated web readiness passed. Its untracked CycloneDX 1.7 SBOM has
32,213 components.
The checked local Go image was then removed to free VM space; its SBOM and
recorded image ID remain as evidence.

The final ARM64 `rust` image has ID
`sha256:3b59ec43d3b8ec6c22f6f0e34a6c737d91d14d429ed4411d57f724dd369eb3dd`.
Rust 1.99.1, the project test, Clippy, excluded commands and authenticated
web readiness passed. Its untracked CycloneDX 1.7 SBOM has 32,599
components.
The checked local Rust image was then removed to free VM space; its SBOM and
recorded image ID remain as evidence.

The final ARM64 `python` image has ID
`sha256:84d0c5910b13954df0c2fab4f79b34bf315ba19e85771b501a5bf72ec9749126`.
Pinned CPython 3.15.2 under `/opt/cpython` and separate Ubuntu Python 3.14.4,
the virtual-environment project, excluded commands and authenticated web
readiness passed. Its untracked CycloneDX 1.7 SBOM has 31,815 components.
The checked local Python image was later removed for the same storage reason;
its SBOM and recorded image ID remain as evidence.

The first Swift solo build failed with exit 125 while writing a large layer
because the Podman VM ran out of space. After removing only checked local test
images, the retry built with pull and passed. The final ARM64 `swift` image has
ID `sha256:f14a47bac9ae9ec58e6ce4626cf9c4c69d019217513b4dd1e022759fe6e7a1b6`.
The GPG signature and expected Swift 6.x fingerprint, Swift 6.4.2 package
project, SourceKit-LSP, excluded commands and authenticated web readiness
passed. Its untracked CycloneDX 1.7 SBOM has 31,374 components.

The repository still contains Model Routing 0.2.6 and Autonomous Run 0.4.10
with matching source locks. `specify --version` and `specify check` passed in
the final `all` image. No autonomous run was started for issue #98.
