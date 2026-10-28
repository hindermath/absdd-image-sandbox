# Lokale Image-Aktivierung / Local image activation

## Deutsch

Owner-Auftrag: das aktualisierte Sandbox-Repository lokal bauen und den
Service-Container neu aktivieren. Grundlage: Repository-Commit `7bb2ffd`;
Home-Baseline-Lock unveraendert `932a5eac8f853e916f03aa16b5b8591f76a27d9f`.
Der Image-Pin ist nicht automatisch der aktuelle Host-Level-0-Head.
Keine neue Rollenfreigabe, keine Pin-Aenderung, kein Commit oder Push.

Der vorherige Container `7a804ce61215` war bereits gestoppt. Seine
beschreibbare Schicht wurde vor dem Austausch lokal gesichert:
`localhost/absdd-image-sandbox-recovery:before-activation-20261028-7bb2ffd`
(`62dfd06703e5d64441e5867f1f53031ee54fba2e723ae8767c426c02a7de0216`).
Diese potenziell vertrauliche Sicherung wird nicht publiziert. Alte Binaries,
Caches und nicht persistente Einstellungen wurden nicht ueber das neue Image
kopiert; sie bleiben bei Bedarf aus dieser Sicherung wiederherstellbar.

Ein Podman-VM-Neustart unterbrach den ersten Build mit unexpected EOF.
Der zweite Build nutzte fertige Cache-Schichten und endete erfolgreich.
Build-/SBOM-Vorschau, Bash-Syntax, Compose-Konfiguration und 30 Tests fuer
Architektur, Home-Baseline-Pin und Toolchain-Pins bestanden. Die vollstaendige
Toolchain-Smoke-Suite bestand im separaten Kandidatencontainer, einschliesslich
.NET, Java, Go, Rust, Python, PowerShell, Node.js, Swift und Dokumentkonvertierung.
Die Dokumentations-Negativfixture meldete erwartungsgemaess einen fehlenden Link;
PDF-Barrierefreiheit wurde nicht als bestanden behauptet.

Aktiviertes ARM64-Image:
`2b8ac14fefcba062022e805d923ebfff5e638c349865c0f8af90a9574dce2e93`.
Laufender Container:
`ef58f5a00d4e845bd95d814c4d491bbae802e3b6198f5d88bc4c3fe6f4e5e4d3`.
Alle 20 Mounts sowie Namen und Erstellungszeiten der sechs Daten-Volumes
blieben gleich. `adedev` UID/GID 1655, no-new-privileges und Capability-Drops
blieben erhalten. Schreibzugriff auf Agenten- und Build-Volumes sowie
Codex, OpenCode, Claude, Antigravity und Copilot wurden nach Aktivierung geprueft.

P1-1 done fuer diesen Lauf: 10 Audit-Metadatensaetze vor Austausch exportiert.
P2-3 done fuer diesen Lauf: CycloneDX 1.7, 29.910 Komponenten.
SBOM: `sboms/2026-10-28-localhost-absdd-image-sandbox_ade-activation-20261028-7bb2ffd.cdx.json`.
SHA-256: `311cda965a186333786d471676a86e8032bd16d5c68199d733c471a2710a29d6`.
P1-4 bleibt partial: bestehende begrenzte Owner-Freigabe bis 31.12.2026,
keine zusaetzliche CISO-/ISB-/KIB-Freigabe. Weitere Compliance-Aufgaben,
Produktlaeufe und allgemeine Wartung waren nicht beauftragt.

Documentation Impact: UpdateRequired. Owner: Repository-Owner. Zielgruppe:
Maintainer; Leserpfad: Sitzungsnachweise. Kanonische Evidence: dieser
historische DE/EN-Nachweis und lokale SBOM. Source-only, kein Home-Sync.
Re-Evaluation bei Image-, Mount-, Pin- oder Freigabeaenderung.

## English

The Owner requested a local rebuild and activation from repository `7bb2ffd`.
The Home Baseline commit pin above was preserved; it is distinct from the
current host Level-0 head. No pin changes, commit, push or formal role approval.
The old container was already stopped. A private local recovery image preserves
its writable layer; no old binaries, caches or non-persistent settings were
copied over the new installation. They remain recoverable from that image.

A Podman VM restart interrupted the first build; the cached retry succeeded.
Preview, syntax, Compose validation, 30 architecture/pin tests and the full
toolchain smoke suite passed. The negative link fixture failed as intended;
PDF accessibility was not assessed. The activated ARM64 image and running
container are identified above. All 20 mounts, six volume identities and
creation times, UID/GID 1655 and security settings were preserved. Post-start
agent CLI and volume write-access checks passed.

P1-1 and P2-3 are complete for this operational run: ten audit metadata records
and a CycloneDX 1.7 SBOM with 29,910 components. P1-4 remains partial under the
existing bounded Owner authority through 2026-12-31, without separate formal
security-role approval. Other compliance tasks and product runs were out of
scope. Documentation impact is UpdateRequired, owned by the Repository Owner:
this bilingual historical session evidence and local SBOM are canonical for
maintainers; source-only, no Home sync, reevaluate on image/mount/pin/approval
changes. The evidence remains local and uncommitted.

## Gezielte Ressourcenbereinigung / Targeted resource cleanup

Auf ausdruecklichen Owner-Auftrag wurden nach erneuter Bestands- und
Prozesspruefung 43 externe Buildah-Arbeitscontainer des unterbrochenen Builds
anhand ihrer eindeutigen IDs entfernt. Alle waren im Zustand `storage`, mit
PID 0; kein Build lief. Keine pauschale Container-Bereinigung.

Nach Pruefung des Image-Elterngraphen wurden ausschliesslich diese drei
unreferenzierten Images mit `podman rmi --no-prune` entfernt:

- Grype: `97bb6b58633688f1924656e2d801e36d4d73dd9c6ab9cedda1d2f3e42f0094a0`
- Syft: `b611a272afd4b085b3f0cee6a160c79bd5cb2ad2aeef32f3d37335d60b090772`
- Alter .NET-SDK-Unterbau: `a3c9e022cfe0fa95d9a19ac4a136c88c34f9d04b5029c8aedfb2098979067fcf`

166 eindeutige Images einschliesslich aktiver und Rueckfall-Elternschichten
blieben geschuetzt. Abschliessend keine dangling Images vorhanden. Kein
`system prune`, kein erzwungenes Entfernen und keine Volume-Loeschung.

Gemessene VM-Dateisystembelegung (`df -B1 /`): vorher 31.587.135.488 Bytes,
nachher 27.948.228.608 Bytes. Netto freigegeben: 3.638.906.880 Bytes
(3,64 GB beziehungsweise 3,39 GiB), nicht aufsummierte Image-Groessen.
Eine Verkleinerung der VM-Datei auf macOS wurde weder gemessen noch zugesichert.

Abschlusspruefung: Container-ID und aktives Image wie oben, Container weiterhin
`running`; alle 20 Mounts identisch. Namen und Erstellungszeiten aller sechs
Volumes sowie beide Netzwerk-IDs unveraendert. Rueckfall-Image
`62dfd06703e5d64441e5867f1f53031ee54fba2e723ae8767c426c02a7de0216`
mit Tag `localhost/absdd-image-sandbox-recovery:before-activation-20261028-7bb2ffd`
erhalten; keine spaetere automatische Loeschung eingerichtet. Entfernte
Hilfsimages koennen erneut geladen, Build-Zwischenergebnisse neu gebaut werden.
Nur dieser lokale Betriebsnachweis wurde ergaenzt; kein Commit oder Push.

On explicit Owner authority, 43 abandoned external Buildah working containers
were identified individually and removed after confirming storage state, PID 0
and no running build. Parent-graph inspection protected 166 unique images,
including the active and recovery image ancestry. Only the three unreferenced
helper/base image IDs listed above were removed with `podman rmi --no-prune`.
No dangling images remained. No system prune, force removal or volume deletion.

Measured VM filesystem usage fell from 31,587,135,488 to 27,948,228,608 bytes:
a net gain of 3,638,906,880 bytes (3.64 GB / 3.39 GiB), not summed image sizes.
Host VM-file shrinkage was not measured or promised. The running container,
active image, all 20 mounts, six volume identities and timestamps, both network
IDs and the recovery image/tag were preserved. No automatic recovery-image
deletion was scheduled. Helper images can be pulled again; build intermediates
can be rebuilt. Only this local operational evidence changed; no commit/push.
The existing UpdateRequired documentation decision also covers this addendum.
