# Home-Baseline-Image-Update / Home Baseline image update

## Deutsch

Owner-Auftrag vom 20.09.2026: Sandbox-Image-Update als ausdruecklich genehmigte
Erweiterung der Container-Delegation. Alle Volumes und bestehenden Mounts
bleiben erhalten. Keine Provider-, Modell-, Secret- oder Rollenfreigabe.

P1-1: Sitzungsnachweis; P1-4: bestehende Owner-Freigabe bis 31.12.2026,
gesonderte Rollenfreigabe weiterhin offen. Andere Compliance-Aufgaben werden
nicht als neu erledigt markiert.

Die Remote-Abfrage bestaetigt `v0.18.0` als letztes veroeffentlichtes Release.
Der neuere Wartungsstand `5b3096c244a6b08266916d2cb4ba5981ebafbd67`
ist deshalb ausdruecklich ein Commit-Pin, kein Release. Lock-Schema 2
unterstuetzt diesen Modus; Schema 1 prueft weiterhin Tag und Commit zusammen.
Unbekannte Felder, ungueltige Modi und Hash-Abweichungen werden abgewiesen.

Validierung: Bash-Syntaxcheck, acht gezielte Offline-/Dokumentationstests auf
macOS und Linux, drei Toolchain-Preflight-Fixtures und statische
Compose-Konfiguration bestanden. Image-Build erfolgreich; neuer Commit und
Schreibschutz sowie neun Werkzeuge im netzwerklosen Smoke-Test bestaetigt.
CycloneDX-SBOM erzeugt und JSON-validiert: 28.970 Komponenten.
Image `a0e780337daa34e45b3914b7be02791cfc770de6635b4f574907cc081290c90f`.
Container `10dde332c2a7` ueber Compose ohne Build und ohne Volume-Loeschung
neu erzeugt: running, Neustartzaehler 0, UID 1655. Alle 20 Mounts samt
Quellen und Schreibrechten sind identisch; Name und Erstellungszeit aller
sechs Volumes unveraendert. Referenz-Commit und die SHA-256-Werte von
Wartungswrapper und Flotten-Engine stimmen mit der Host-Quelle ueberein.
Audit-Metadaten exportiert und lokale private Container-Rueckfallsicherung
`localhost/absdd-image-sandbox-recovery:before-baseline-5b3096c` erstellt
(nicht veroeffentlichen). Die alte beschreibbare Container-Schicht bleibt
darin gesichert; sie wurde nicht ungeprueft ins neue Image uebernommen.
SBOM: `sboms/2026-09-20-localhost-absdd-image-sandbox_ade-baseline-5b3096c.cdx.json`
(lokales, ignoriertes Build-Artefakt). Dies ist eine kurze Wiederanlaufpruefung,
kein Langzeitstabilitaetsnachweis und kein erfolgreicher Flottenwartungslauf.
Statistik-Check meldet Drift. Der Renderer sperrt das Schreiben im dirty
Arbeitsbaum; Aktualisierung nach gesichtetem Inhaltscommit erforderlich.
Kein Commit oder Push. Die uebergeordnete Wartungsdelegation ist noch offen.

Documentation Impact: UpdateRequired. Kanonische Quelle ist der Lock mit dem
Installer; README und Sandbox-Freigabe erklaeren die Bindung. Owner ist der
Repository-Owner. Zielgruppen: Maintainer und Lernende; Leserpfad ueber den
bestehenden README-Abschnitt zur Home-Baseline-Referenz. Deutsch/Englisch
stehen im selben Dokument. Distribution: Sandbox-Image/Source-only, kein
Host-Home-Sync. Native macOS-/Linux-Container-Pruefung; Windows nicht lokal
verfuegbar. Re-Evaluation bei jedem Pin-/Installer-Update.

## English

The owner explicitly approved the sandbox image update on 2026-09-20 as an
extension of container delegation. Preserve all volumes and mounts; no new
provider, model, secret or role authority. The bounded maintenance approval
still expires on 2026-12-31; formal role approval remains open.

The latest published release is still v0.18.0. Schema 2 therefore pins the
newer maintenance commit explicitly, without inventing a release. Schema 1
retains exact tag/commit verification. Invalid contracts and hash mismatches
fail closed. Bash syntax, eight focused tests and static Compose validation
passed on macOS and Linux; three toolchain fixtures passed. Image build and
network-disabled smoke checks confirm the exact commit, read-only reference
and nine tools. A valid CycloneDX SBOM contains 28,970 components. Compose
recreated only the service container without rebuilding or deleting volumes.
Container 10dde332c2a7 runs as UID 1655 with restart count zero. All twenty
mounts including sources/access and all six volume identities/creation times
are unchanged. Reference commit and both maintenance script hashes match the
host source. Audit metadata exported; private local recovery image retained,
not published. The old writable layer is backed up there, not blindly copied
into the new image. This is bounded restart evidence, not long-term stability
or a completed fleet maintenance run.
Statistics drift remains: the renderer requires a clean tree after a reviewed
content commit. No commit/push; overarching delegation remains open.

Documentation Impact is UpdateRequired: lock/installer are canonical; README
and approval documentation explain the contract to maintainers and learners
in German and English. Image/source distribution only, no host Home sync.
macOS and Linux-container checks; Windows is unavailable locally.
