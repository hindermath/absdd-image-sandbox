# Renovate-Ablösung / Renovate Retirement

DE: Explizite Ownerentscheidung: Renovate vollstaendig durch Dependabot und
einen eigenen geprueften Pin-Workflow abloesen; Podman ist verbindlich.
29 ARGs sind in 28 Gruppen erfasst. Versionswerte und Archiv-Hashes bleiben
in dieser Einrichtung unveraendert. Der lokale read-only Herstellerabgleich
ist Ready; 81 Offline-Assertions und 61 fokussierte bestehende Python-Tests
sind erfolgreich. Dokumentationsentscheidung und Beweisgrenzen stehen in
docs/maintenance/toolchain-pin-migration-2026-11-03.json. PR110 enthaelt die
exakten Hosted-Checks. Kein Compliance-Task geschlossen, kein Containerwechsel,
kein Home-Sync und keine Aenderung menschlicher Review-/Branch-Schutzregeln.
Nach Merge erste Dependabot-/Pin-Laeufe pruefen; Paketupdates separat reviewen.

EN: Explicit owner choice: fully replace Renovate with Dependabot and a tested
custom pin workflow, retaining Podman. All29 ARGs are covered in28 groups.
This setup changes no version values or archive hashes. Read-only upstream
discovery is Ready; 81 offline assertions and 61 existing focused Python tests
pass. Documentation Impact and proof limits are in the migration record;
PR110 carries exact-head hosted checks. No compliance task is closed, no
container switched, no Home sync performed and no human review/branch rule
changed. Inspect first runs after merge; review package upgrades separately.
