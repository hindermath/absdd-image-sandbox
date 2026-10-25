# Aktueller lokaler Stand / Current Local State 2026-10-25

## Einordnung / Context

DE: Dieser Nachtrag trennt den spaeteren lokalen Image-Austausch von der
[ersten Versionspruefung](toolchain-version-audit-2026-10-25.md) und der
[damaligen Untersuchung](../security/toolchain-followups-2026-10-25.md).
Die Machine war bei jener Untersuchung gestoppt. Der nachfolgende
[Build- und Austausch-Log](../security/agent-session-log/2026-10-25-1047.md)
belegt Neubau, isolierte Tests, SBOM, Volumesicherung und kontrollierten Austausch.
Historische Session-Logs werden nicht umgeschrieben.

EN: This addendum separates later local image replacement from the first
version audit and investigation. The machine was stopped during that earlier
investigation. The subsequent build/replacement log records the build,
isolated tests, SBOM, volume backups and controlled replacement. Historical
session logs remain unchanged.

## Laufzeit Und Lieferkettenbindung / Runtime and Supply-Chain Binding

DE: Am 2026-10-25 erneut nur lesend ueber den dynamisch ermittelten
Podman-Socket bestaetigt. Keine Agenten gestartet, keine Anmeldung und kein
erneuter Build, Neustart oder Austausch fuer diese Korrektur.

EN: Reconfirmed read-only on October 25 through the discovered Podman socket.
This correction started no agents, sign-in, build, restart or replacement.

| Merkmal / Item | Nachweis / Evidence |
|---|---|
| Container | `9e5b3649ae911534ea5d4c579d9c99ab6b197635e82e7c51f2855d9991e4c2e9`, `running` |
| Image-ID | `9cbfe8a74a9437761193c404788dd0f2a57c55ec5685d0c4881272dbfabf0f47` |
| Architektur / architecture | `linux/arm64`, keine AMD64-Abnahme / no AMD64 acceptance |
| Benutzer / user | `adedev`; Build-Log belegt UID/GID 1655 / build log records UID/GID 1655 |
| SBOM-Datei / file | `sboms/2026-10-25-localhost-absdd-image-sandbox-rebuild-20261025.cdx.json`, ignoriertes Build-Artefakt / ignored build artifact |
| SBOM-Format / format | CycloneDX JSON, 29910 Komponenten / components |
| SBOM SHA-256 | `121066c8334374359884f6ec990ff0836590b8f384db8f74326365f9a09a970c` |

DE: Der Build-Log belegt Sprach-/Dokumentations-Smokes, JSON-Preflight,
sechs erhaltene Volumes und identische Mount-/Port-/Security-Bindungen beim
Austausch. SBOM und Funktionstests sind weder Vulnerabilitaetsfreigabe noch
PDF-Barrierefreiheitsnachweis. Der alte Kandidat `24139e60314c` und das
vorherige Service-Image `1ed9ce9a1a14` wurden danach gezielt entfernt; ihre
historischen Nachweise bleiben erhalten. Ein Git-HEAD allein bezeichnet
nicht den gebauten Inhalt: Der Build nutzte den dokumentierten dirty Worktree.

EN: The build log records language/documentation smokes, JSON preflight,
six retained volumes and unchanged mount, port and security bindings during
replacement. Neither SBOM nor functional tests grant vulnerability clearance
or PDF accessibility acceptance. The earlier audit candidate and service
image were removed afterwards; their historical evidence remains. Git HEAD
alone does not identify built content: the build used the documented dirty
worktree, which contains uncommitted changes.

## Drei Review-Korrekturen / Three Review Corrections

| ID | Korrektur / Correction | Abnahmegrenze / Acceptance boundary |
|---|---|---|
| REV-001 | Linux-Wartungsregistry auf Swift 6.4.1 ausrichten; mit Dockerfile vergleichen / align registry with Dockerfile | Swiftly 1.1.2 und Archiv-Hashes unveraendert; nur isolierte Tests / installer and hashes unchanged; isolated tests only |
| REV-002 | Lernenden-Tabelle: Go 1.27.3, Rust 1.99.1, Swift 6.4.1 / learner version table | bestehende Supported/Open-Werte nicht durch Versionsvergleich neu abnehmen / version comparison grants no new acceptance |
| REV-003 | aktuelle und historische Nachweise eindeutig verlinken / distinguish current and historical evidence | Review-Gueltigkeit separat validieren, keine Freigabe aus diesem Text / validate review separately; no approval from this text |

DE: Dies sind Quellen- und Dokumentationskorrekturen, keine erneute
Installation. Die Wartungsregistry wird ueber den Repository-Mount gelesen;
die Korrektur fuehrt das globale Wartungsskript nicht aus und beansprucht
keine bereits durchgefuehrte globale Swift-Umstellung auf anderen Hosts.
Fiktive Test-Fixtures mit alten Versionen bleiben absichtlich erhalten.

EN: These are source/documentation corrections, not another installation.
The repository mount exposes the registry change; it does not run global
maintenance or claim a Swift upgrade on other hosts. Old versions in
synthetic test fixtures remain intentional.

## Intake-Bindung Und Offene Grenzen / Intake Binding and Open Boundaries

DE: Der vorige Quellenabgleich und dessen Review wurden durchgefuehrt.
Diese Korrekturen benoetigen eine neue nachvollziehbare Quellenbindung und
ersetzen das alte Review ausdruecklich. Die gueltige Entscheidung steht nur
im [separaten Reihenreview](../../specs/intake-review-reports/sandbox-development-lifecycle.md)
mit aktuellen Quellenvalidatoren. Keine pauschale Ready-Behauptung in einem
statischen Statusabschnitt. Die Reihe bleibt Completed, Eligible, Blocked,
Blocked; Eligible ist keine Startautoritaet.

EN: Previous source alignment and review were performed. These corrections
need a fresh traceable binding and explicitly supersede the former review.
Only the separate series review and current source validators establish
validity; this static section does not assert Ready. Preserve Completed,
Eligible, Blocked, Blocked. Eligibility grants no execution authority.

DE: `UPD-AMD64`, `UPD-V2-LOOP`, `UPD-V2-AUDIT`, `UPD-SMOKE-WARN`,
`DOC-A11Y` und `UPD-APPROVAL` bleiben Open mit den Ownern, Follow-ups und
Re-Evaluation-Triggern im [Nachpruefungsregister](../security/toolchain-followups-2026-10-25.md).
Die Registry- und Textkorrekturen schliessen keinen dieser Punkte. Die
Windows-Host- und Ubuntu/WSL2-Nachweise bleiben getrennt; keine native
Linux-Hardware-Abnahme wird behauptet.

EN: AMD64 acceptance, effective OpenCode 2 loop/override controls, session
audit coverage, Swift/Poppler warnings, human accessibility and approval
remain Open with owners, follow-up and triggers in the follow-up register.
Registry/text corrections close none of them. Windows-host and Ubuntu/WSL2
evidence remain separate, with no native Linux hardware acceptance claimed.

## Spaetere Commit-Gruppen / Later Commit Groups

1. Toolchains: Pins, Installations-/Spec-Kit-Patches, Registry und passende Tests.
   / Pins, installation and Spec Kit patches, registry and related tests.
2. Audit/Stop: Exporter, Fail-closed-Wrapper und Sicherheitsregressionen.
   / Exporters, fail-closed wrappers and safety regressions.
3. Dokumentation: Leserpfade, Agent-Paritaet und Statusklarheit.
   / Reader paths, agent parity and explicit status boundaries.
4. Intake: Texte, Quellenbindungen, Archive, Reihenansichten und Vollreview zusammen.
   / Keep texts, bindings, archives, series views and full review together.
5. Betriebsnachweise: Build-, Austausch- und Korrektur-Session-Logs.
   / Build, replacement and correction session logs.

DE: Nur Zuordnung fuer einen spaeteren Auftrag; kein Commit, Push oder PR
hierdurch beauftragt. Geteilte Hook-Dateien nach zugehoeriger Aufgabe aufteilen.

EN: This groups future work only; it authorises no commit, push or PR. Split
shared hook changes with their corresponding task.
