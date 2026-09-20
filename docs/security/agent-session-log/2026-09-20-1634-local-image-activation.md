# Lokale Image-Aktivierung / Local image activation

## Deutsch

Der Owner beauftragte ausdrücklich die Aktualisierung und Neuaktivierung
der lokalen Sandbox für die bereits gelieferte Wartungsdelegation. Der
vorhandene Lock blieb unverändert: `19dc97ceb0c413c12284077a7249d726f7bcc1c7`.
Keine neue Provider-, Mount- oder formelle Rollenfreigabe wurde erteilt.

- P1-1 done: Audit-Metadaten vor dem Wiederanlauf exportiert; dieser Nachweis.
- P1-4 partial: bestehende Owner-Freigabe bis 31.12.2026 geprüft;
  gesonderte CISO-/ISB-/KIB-Freigabe weiterhin nicht behauptet.
- P2-3 done: Build und CycloneDX-1.7-SBOM mit 28.970 Komponenten bestanden.
- Sonstige Compliance-Aufgaben nicht erneut bearbeitet: reiner Betriebsauftrag.

Image: `018de6b9a16269f06cbc3ec40d08e8359fe6cf0ff91f08eac1fa923f716f5d94`.
Neuer Container: `8a5d59f89d784502bdc91b835f59102b19e915bc25a782e10a24e2ac419685e2`.
Privates lokales Rückfall-Image:
`localhost/absdd-image-sandbox-recovery:before-activation-20260920-19dc97ce`.
Es bewahrt die alte beschreibbare Container-Schicht und wird nicht publiziert.

Nach Syntaxcheck, statischer Compose-Prüfung und Vorschau wurde das vorhandene
Build-/SBOM-Skript ausgeführt. Neun Pin-/Dokumentationstests auf macOS und
25 Delegationstests im netzwerklosen Linux-Kandidaten bestanden. Alle 156
Paketbindungen und der Schreibschutz wurden gegen die lokale Level-0-Quelle
geprüft. Nur der Service-Container wurde ohne Neubau oder Volume-Löschung
neu erzeugt. Alle 20 Mounts, Namen und Erstellungszeiten der sechs benannten
Volumes, Benutzer `adedev` (UID 1655) und Sicherheitseinstellungen blieben gleich.

Der echte Preflight mit Owner-Evidence, Mount- und Quellbindung bestand im
neuen Container. Delegierte Status- und Ahead/Behind-Abfragen bestanden für
21/21 Secure-Trader-Repositories: sauber, `main`, jeweils 0/0 gegenüber dem
zuletzt gefetchten `origin/main`. Kein neuer Fetch, Pull, vollständiger
Wartungslauf, Runtime-Sync, Commit oder Push wurde ausgeführt. Dies ist eine
lokale macOS/Podman-Betriebsprüfung, keine Windows-Abnahme oder neue
Sicherheitszertifizierung.

SBOM: `sboms/2026-09-20-localhost-absdd-image-sandbox_ade-activation-19dc97ce.cdx.json`.
SHA-256: `444b3c646b5dc278744bc228ec9a9c397defef388bb67bc42d428d42d91a85f4`.
Die SBOM bleibt ein ignoriertes lokales Artefakt.

Documentation Impact: UpdateRequired. Owner: Repository-Owner. Zielgruppe:
Maintainer; Leserpfad: Sitzungsprotokolle und Chat-Abschluss. Kanonische Quellen:
unveränderter Lock und diese lokale Betriebsevidence. Dokumentklasse:
historischer Nachweis, DE/EN in einer Datei, textorientiert. Source-only;
kein Home-Sync. Re-Evaluation bei Image-, Pin-, Mount- oder Freigabeänderung.
Nächster Schritt bei Bedarf: separat beauftragter regulärer Wartungslauf.

## English

The Owner explicitly requested local image update and activation using the
existing unchanged commit pin above. Audit metadata was exported; a private
local recovery image preserves the old writable container layer. No volumes
were removed and no image was published. P1-1 and P2-3 are done for this
activation; P1-4 remains partial with bounded Owner authority expiring on
2026-12-31, not additional formal security-role approval. Other compliance
tasks were outside this operational request.

Build, CycloneDX inventory, nine native macOS pin/documentation tests,
25 network-disabled Linux delegation tests, all 156 package bindings and
reference immutability passed. All twenty mounts, six named volume identities
and creation times, user and security settings were retained. The real
post-activation preflight and delegated read-only Git checks passed for all
21 Secure Trader repositories: clean main branches, zero ahead/behind against
the previously fetched origin/main. No fetch, pull, full maintenance, runtime
sync, commit or push was performed. This is local macOS/Podman operational
evidence, not Windows acceptance or security certification.

Documentation impact is UpdateRequired, owned by the Repository Owner for
maintainers through session logs and chat closeout. The unchanged lock and
this bilingual source-only historical record are canonical for this local
activation. No Home sync is needed. Reevaluate on image, pin, mount or approval
changes; routine maintenance remains a separately requested next action.
