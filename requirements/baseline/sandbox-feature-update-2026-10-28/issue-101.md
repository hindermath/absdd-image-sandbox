# Issue #101: Ubuntu 26.04 LTS: .NET-Basis, Swift und native AMD64-/ARM64-Validierung übernehmen

Source: https://github.com/hindermath/absdd-image-sandbox/issues/101
Retrieved through GitHub connector: 2026-10-28
Issue updatedAt: 2026-10-27T22:52:59Z
Proof boundary: immutable local requirements snapshot; no upstream implementation acceptance.

## Deutsch

### Gemeinsamer nächster Feature-Update-Block

Dieses Issue gehört zusammen mit den folgenden Issues zum **nächsten Feature-Update-Block dieses Repositories**:

- [#101 – Ubuntu 26.04 und Basisimage](https://github.com/hindermath/absdd-image-sandbox/issues/101)
- [#102 – OpenCode-Webinterface](https://github.com/hindermath/absdd-image-sandbox/issues/102)
- [#104 – MSL-Sprachauswahl](https://github.com/hindermath/absdd-image-sandbox/issues/104)

Gemeinsames Ziel: Ubuntu-26.04-Basis, OpenCode-Webbetrieb und wählbare MSL-Profile als zusammenhängendes Sandbox-Update bereitstellen. #101 bildet die technische Basis; #102 und #104 werden darauf abgestimmt. Die Umsetzung kann in getrennten Änderungen erfolgen. Vor Abschluss des Blocks die Kombination auf den finalen Images einschließlich Profil-, Web-, Audit- und Plattformprüfungen validieren. Der Block ist erst abgeschlossen, wenn alle drei Issues ihre Abnahmekriterien erfüllen.

### Aktualisierung nach Gesamtsichtung ab MR !64

Stand 2026-10-27: Quellkandidat `4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30`, [MR !64](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/merge_requests/64) weiterhin offen/Draft. Die Basisumstellung !70 und das Webfeature !71 sind implementiert; !74 ergänzt sieben Build-Profile, !76 schließt die Profil-Alpha. Die Quelländerungen sind technische Vorbilder für dieses offene Ziel-Issue.

- MR !65: OpenCode-2-Policies/Metadaten mit dem hier bereits vorhandenen V2-Vertrag abgleichen; Webübernahme in #102.
- MR !66 einschließlich !67: mountunabhängige .NET-Ausgabepfade und Dokumentationswerkzeuge. Lychee/Typst/Tinymist sind hier bereits vorhanden. Der konkrete .NET-Pfadfix fehlt noch: `ContainerBuild.props` gilt hier nur unter `/rider-projects/` und flacht Pfade mit Unterstrichen ab; die Quelle erhält die vollständige absolute Verzeichnishierarchie unter `/dotnet-build` und vermeidet Selbstimport. Als abgegrenzte Begleitkorrektur mit prüfen.
- MR !68 enthält quellprojektspezifisches Provider-/Modellrouting: nicht in dieses providerneutrale Repo übernehmen.
- MR !69: 14 Presets sind hier bereits installiert; vorhandene Pins prüfen, keine zweite Installation. !72/!73 und !75/!77 liefern freiwillige Testanleitung/Status, keine zusätzliche Implementierung.
- MR !74/!76: Profilimplementierung und Abschluss in #104. Dieses Basis-Issue erhält weiterhin alle sechs Toolchains im Standardprofil `all`; kleinere Profile erst über #104.

Zusätzliche Aufgaben:

- [ ] Mountunabhängigen .NET-Ausgabepfad aus !66 als eigene fokussierte Änderung prüfen: zwei unterschiedliche Mountwurzeln, Unterstrich-/Verzeichniskollision, Projekt-`Directory.Build.props`, Selbstimport sowie `bin`/`obj`/AppHost außerhalb der Bind-Mounts testen.
- [ ] Profilfähigen Quell-Dockerfile nicht komplett ersetzen: Ubuntu-Migration und MSL-Auswahl #104 getrennt halten, gemeinsame Basis und spätere Kombination abstimmen.
- [ ] Eigene SBOM-Sicherheitsverträge erhalten. Quellwrapper unterstützen Docker und einen externen Scanner-Fallback; hier gelten weiterhin Podman und imageintegriertes oder exakt gepinntes Host-Syft.

Die [AMD64-/ARM64-Quellnachweise](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/docs/security/base-image-migration-2026-10.md) und der [Profil-ARM64-Bericht](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/docs/security/mr74-macos-arm64-acceptance-2026-10-27.md) sind datiert und an ihre jeweiligen Testcommits gebunden. Nicht alle Plattformen/Compose-Pfade sind damit belegt; kein eigener Build wurde für dieses Issue ausgeführt.

### Ziel und geprüfter Ausgangspunkt

Die Containerbasis auf Ubuntu 26.04 LTS umstellen und die sechs vorhandenen Sprach-Toolchains auf nativen AMD64- und ARM64-Systemen erhalten.

Abgleich am 2026-10-27: Dieses Repository verwendet auf `main` die per Digest gebundene .NET-Basis `sdk:10.0` (Kommentar: SDK 10.0.402), Noble-/Ubuntu-24.04-spezifische Swift-Prüfung und GCC-13-Pakete. Architektur-Guards und Build-/SBOM-Wrapper sind bereits vorhanden.

Vorbild sind [MR !70](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/merge_requests/70), Commit [fe7ea5c](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/commit/fe7ea5c75064872f4d1064604308b56ce430c08d), einschließlich [SELinux-Korrektur 39f0415](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/commit/39f0415b9d296c496ff487c3e6d21b6e05db4f4f). Geprüfter Quellstand: `4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30` auf `chore/refresh-sandbox-image-2026-10`; MR !70 ist dort implementiert; der übergeordnete MR !64 bleibt offen/Draft. Quell-`main` enthält die neue Anleitung, aber noch nicht diese Implementierung.

Quellkandidat: `mcr.microsoft.com/dotnet/sdk:10.0.403-resolute@sha256:667f3cee6f24afb202d3e32c7941e3800bbac57dd70bb68f89e52a6245aff88f`. Tag, Manifest, Plattformen und Verfügbarkeit bei Umsetzung erneut prüfen. [Quell-Dockerfile](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/Dockerfile) und [Migrationsnachweis](https://gitlab-ce.gwdg.de/agentic-coding/ade-dev-sandbox/-/blob/4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30/docs/security/base-image-migration-2026-10.md).

### Arbeitspakete

- [ ] Basis mit explizitem Resolute-Tag und passendem Multiarch-Digest pinnen; Build-Prüfungen für .NET und PowerShell sowie Renovate-Metadaten und Dependency-Update-Dokumentation nachführen.
- [ ] Ubuntu-Pakete und Swift-Abhängigkeiten auf 26.04 abstimmen, insbesondere GCC-/C++-Bibliotheken. Swift für beide Architekturen aus zur Basis passenden Artefakten installieren und Integritätsprüfung erhalten. Noble-spezifische Sperren und Meldungen ersetzen.
- [ ] Java 25, gepinntes CPython 3.15 unter `/opt/cpython`, separates Ubuntu-System-Python, .NET-Kompatibilitäts-SDK und vorhandene Agenten-/Dokumentationswerkzeuge erhalten. Die Quelle verwendet Java 21 und System-Python: diese Unterschiede nicht ungeprüft übernehmen.
- [ ] Vorhandene Bash-/PowerShell-Architekturprüfungen erweitern, soweit erforderlich; keine zweite Guard-Implementierung schaffen. Cross-Builds separat kennzeichnen und nicht als native Laufzeitabnahme zählen.
- [ ] SELinux-/Bubblewrap-Verhalten beim Build und bei strikten Codex-Policy-Tests untersuchen. Die Quelle verwendet bei aktivem Podman-SELinux gezielt `label=type:container_engine_t`. Übernahme mit dokumentiertem Sicherheitsreview prüfen; keine pauschale Rechteerweiterung. Beide Build-/SBOM-Wrapper und Regressionstests synchron halten, unbekannten Engine-Status nicht stillschweigend akzeptieren.
- [ ] Bestehende Leserpfade in `docs/fuer-lernende/` und `docs/betrieb/`, README und betroffene Sicherheitsnachweise aktualisieren: Deutsch zuerst, gleichwertiges Englisch, Ausführungsort, Shell, Voraussetzungen, Ergebnis und Fehlerhilfe.

### Abnahme für die spätere Umsetzung

- [ ] Compose-Konfiguration ohne Secret-Ausgabe prüfen; `git diff --check`, vorhandene relevante Regressionstests, Pre-Commit und Secret-Scan bestehen.
- [ ] Vollständiger Neubau mit Pull; Host-, Engine-, Ziel- und Image-Architektur sowie `/etc/os-release`, Git-Head, Datum, Image-ID und Exitcodes belegen.
- [ ] Frische native AMD64- und ARM64-Laufzeittests aller sechs Sprach-Toolchains, PowerShell/C#, Dokumentationswerkzeuge, Agenten-CLIs ohne echte Modellaufrufe und vorhandener Policy-/Audit-Prüfungen. macOS, Windows-Host und Ubuntu/WSL2 getrennt ausweisen; fehlende Plattformen offen lassen.
- [ ] Non-root, `cap_drop: ALL`, `no-new-privileges`, Standard-Seccomp und persistente Daten erhalten. Frische CycloneDX-SBOM für jedes auszuliefernde finale Image erzeugen; Artefakte ungetrackt halten.
- [ ] Quellnachweise nur als Referenz verwenden; keine fremden Image-IDs, Testzahlen, Freigaben oder Sessionnachweise als eigene Ergebnisse übernehmen.

Planbezug: P0-2, P1-5, P2-3, P3-4. Dieses Issue plant ein Update; es startet keinen bestehenden autonomen Lauf und erteilt keine formelle Sandbox-, Provider- oder Plattformfreigabe.

## English

### Shared next feature update block

This issue and the following issues form the **next feature update block for this repository**:

- [#101 – Ubuntu 26.04 and base image](https://github.com/hindermath/absdd-image-sandbox/issues/101)
- [#102 – OpenCode web interface](https://github.com/hindermath/absdd-image-sandbox/issues/102)
- [#104 – MSL language selection](https://github.com/hindermath/absdd-image-sandbox/issues/104)

Shared goal: deliver the Ubuntu 26.04 base, OpenCode web operation and selectable MSL profiles as one coordinated sandbox update. #101 provides the technical foundation; align #102 and #104 with it. Implementation may use separate changes. Before closing the block, validate the combined final images with profile, web, audit and platform checks. The block is complete only when all three issues meet their acceptance criteria.

### Refresh after reviewing MR !64 onward

As of 2026-10-27, candidate `4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30` includes implemented base MR !70, web MR !71 and profile MR !74; !76 closes the profile alpha. Parent !64 remains open/Draft. These source changes are references for this still-open target issue.

MR !65 overlaps existing OpenCode V2 policy; web work belongs to #102. MR !66/!67 add mount-independent .NET output paths and documentation tools: Lychee/Typst/Tinymist already exist here, while the path fix is missing. Source preserves absolute directory hierarchy below /dotnet-build and prevents self-import; this repo currently restricts redirection to /rider-projects and flattens paths. MR !68's provider/model configuration stays source-specific. MR !69 overlaps the existing 14 presets: compare pins without duplicate installation. !72/!73 and !75/!77 add test/status guidance. !74/!76 profile implementation is tracked in #104; all six toolchains remain the default here.

- [ ] Assess the !66 output fix as a separate focused patch; test two mount roots, underscore/path collisions, repository props, self-import and bin/obj/AppHost outside bind mounts.
- [ ] Keep Ubuntu migration and #104 profile selection separate; coordinate their shared core and final combination.
- [ ] Preserve target SBOM restrictions: Podman and integrated/exactly pinned host Syft, without the source's Docker/moving-scanner fallback.

Linked source reports bind their own dates and tested revisions. They do not prove every platform/Compose path or this repository's acceptance; no build was run for this issue refresh.

### Goal and evidence

Migrate the container base to Ubuntu 26.04 LTS while preserving all six language toolchains on native AMD64 and ARM64. Verified on 2026-10-27 against source revision `4a9eb43a8a11f0f5b30e7ec1ffd97064e1dd1e30` on `chore/refresh-sandbox-image-2026-10`. MR !70 is implemented in that branch; parent MR !64 remains open/Draft. Source main contains guidance, not this implementation. The links above bind the exact candidate and migration evidence; recheck the tag, digest, platforms and availability before implementation.

### Work and acceptance

- [ ] Pin an explicit Resolute tag and multiarch digest; update .NET/PowerShell build checks, Renovate metadata and dependency documentation.
- [ ] Adapt Ubuntu packages, GCC/C++ dependencies and verified Swift downloads for both architectures; replace Noble-specific guards.
- [ ] Preserve this repository's Java 25, pinned CPython 3.15, separate system Python, compatibility SDK and existing agent/documentation tools. Do not copy the source's Java 21 or Python choices.
- [ ] Extend existing Bash/PowerShell architecture guards instead of duplicating them; report cross-builds separately.
- [ ] Review SELinux/Bubblewrap compatibility. Evaluate the source's narrowly scoped `container_engine_t` setting with security review; retain capability drops, no-new-privileges, standard Seccomp and inner policy. Keep both build/SBOM wrappers and regression tests aligned; fail on unknown engine status.
- [ ] Update existing learner and operations documentation in equivalent German and English, including command location, shell, prerequisites, expected results and troubleshooting.
- [ ] Pass secret-safe Compose validation, diff checks, relevant regressions, Pre-Commit and secret scanning.
- [ ] Rebuild and record fresh native AMD64/ARM64 runtime evidence for all six toolchains, PowerShell/C#, documentation tools, agent CLIs and policy/audit checks without real model calls. Record host/engine/image architecture, OS, date, Git revision, image ID and exit codes. Distinguish macOS, Windows and Ubuntu/WSL2; leave unavailable coverage open.
- [ ] Preserve non-root operation and persistent data; generate fresh untracked CycloneDX SBOMs for final delivery images. Source evidence is reference material, never this repository's acceptance.

Plan references: P0-2, P1-5, P2-3, P3-4. Scheduling this update does not resume an autonomous run or grant formal approval.

