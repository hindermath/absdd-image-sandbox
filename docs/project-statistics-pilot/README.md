# Sandbox-Statistik-Feldtest / Sandbox statistics field test

## Stand / Status

Am 2026-09-18 nach menschlicher Sichtung genau den ersten Inhaltspatch
committet: `9f07e6795cb05ff7d3866972638349c8aded5b44`. Die reale UTC-Messung
darauf liefert 1306 Textdateien, 233454 Textzeilen und 70 Aktivtage.
Bash-/PowerShell-Status, 67 Fixture-Assertions, zwei unveraenderte
Wiederholungsupdates, acht Encoding-Statusfaelle und sechs Raw-Blob-Faelle
bestanden. [Pruefwerte](field-evidence.json) und
[Sitzungsnachweis](../security/agent-session-log/2026-09-18-1238.md).

Dies ist eine reproduzierbare Zwischenmessung. Neue Ausgaben und Dokumente
sind noch nicht committet; insbesondere das neue Sitzungsprotokoll muss nach
seinem gesichteten Commit in einen erneuten Statistik-Nachlauf eingehen.
Native CI, Windows-Nachweis und menschliche Feldabnahme bleiben offen.
Kein Push oder Merge in dieser Etappe.

The owner-reviewed first content patch is committed at the stated revision.
Its real UTC measurement gives 1306 text files, 233454 lines and 70 active
days. Local shell, fixture, repeatability, encoding and raw-blob checks passed.
This is intermediate evidence: new outputs and documentation await review,
and their content commit requires a fresh statistics pass. Native CI,
Windows evidence and human field acceptance remain open; no push or merge.

## Quelle und Bedienung / Source and operation

- Projekt: [Sandbox #70](https://github.com/hindermath/absdd-image-sandbox/issues/70).
- Gesamtpilot: [Preset #1](https://github.com/hindermath/spec-kit-preset-project-statistics-governance/issues/1).
- Installation: [Nachweis v0.1.0](../maintenance/project-statistics-installation-v010.md);
  geliefert ueber [PR #72](https://github.com/hindermath/absdd-image-sandbox/pull/72).
- Produkt: Project Statistics Governance v0.1.0, Prioritaet 90, unveraenderte
  14er-Matrix. Paketcommit `7e824ca8de11212aefdc5b05d7d05637f5343dab`.
- Paket-ZIP-SHA-256:
  `d8ad7d5eef920f50b629121b64ba8123c22ec4f6dadd14da5cd826d1c50f420a`.
- Pilotbasis: `457cc3b32872cadebefab613423e5542dc34760b`.
- Konfiguration: [config.json](config.json), UTC, 52 Wochen, keine
  Referenzmodellrechnungen. Bestehende Projektstatistik bleibt kanonisch.

The installation and issue links identify provenance and tracking. This
separate pilot uses UTC and 52 weeks, with reference estimates disabled.
Existing project statistics remain authoritative. The README records current
field-test progress; the earlier installation receipt remains historical.

Erst nach Sichtung und Konfigurationscommit auf sauberem Git-Stand:

Only after human review and the configuration commit, on a clean worktree:

```bash
bash .specify/presets/project-statistics-governance/scripts/project-statistics.sh update --repo . --config docs/project-statistics-pilot/config.json --dry-run --json
bash .specify/presets/project-statistics-governance/scripts/project-statistics.sh update --repo . --config docs/project-statistics-pilot/config.json --json
bash .specify/presets/project-statistics-governance/scripts/project-statistics.sh status --repo . --config docs/project-statistics-pilot/config.json --json
```

## Pruefvertrag und Grenzen / Test contract and boundaries

1. Quellenrevision, Stichtag, Konfigurations- und Payload-Hashes binden.
2. Update wiederholen; identische Eingaben muessen identische Daten erzeugen.
3. Bash und PowerShell vergleichen; Status darf weder gepruefte Dateien noch
   Git-Zustand aendern. Nachweisgrenze: Hashes und Git-Zustand, kein Voll-I/O-Trace.
4. LF/CRLF/BOM-Paritaet und negative Tests nur in isolierten Fixtures pruefen.
   Erfolg liefert 0, Drift 1, ungueltige Voraussetzungen 2.
5. Native CI prueft Linux und Windows, bindet den ausgefuehrten Commit und
   prueft den aktuellen Liefer-Snapshot separat. Die Windows-Suite enthaelt
   keine Bash-/Unix-spezifischen Faelle; fehlende Plattformbelege bleiben offen.
6. Bestehenden Statistik-Ledger nach Inhaltscommit fortschreiben; jeden neuen
   Diff vor Commit/Push sichten. Fachliche Abnahme bleibt menschlich.

Bind revisions, cutoff and hashes; verify repeatability, shell parity and
read-only status. Encoding and negative tests run only in isolated fixtures.
Native CI checks Linux and Windows and separately checks the current delivery
snapshot. Windows does not prove Bash/Unix-specific cases. Missing platform
evidence stays open. Review each new diff before commit/push and keep human
field acceptance separate from technical checks.

Arbeit nur als `adedev` im isolierten Podman-Piloten. Kein Image-Neubau,
keine Runtime-/Produkt-API-Aenderung, kein Home-Sync, keine globale Registry-
oder Git-Konfiguration. Der urspruengliche Sandbox-Checkout bleibt unberuehrt.
Keine Produktivitaets-, Qualitaets-, Personen-, Release- oder
Zertifizierungsbehauptung. Tracking bleibt bis zum zentralen Bericht offen.

Work only as non-root adedev in the isolated Podman pilot. No image rebuild,
runtime/API change, Home sync, global registry or Git configuration change.
Preserve the original checkout. These measurements do not prove productivity,
quality, individual performance, release acceptance or certification.

## Dokumentationsauswirkung / Documentation impact

`UpdateRequired`. Owner und fachlicher Reviewer: Thorsten Hindermann.
Zielgruppen: Lernende ab Lehrjahr 1, Maintainer und Reviewer.
Leserpfad: Installationsnachweis -> dieser Pilotkontext -> spaetere Messung
und Pruefevidence. Klasse: ActiveSemantic; Quelle: dieses Repository plus
unveraendertes eigenstaendiges Preset. DE zuerst/EN danach, textorientiert.
Distribution: Projektdokumentation und Projekt-CI, kein Home-Runtime-Sync.
Wiedervorlage bei Paket-, Profil-, Messkontext- oder Plattformwechsel.
Die bestehende Statistikmethodik und gemeinsame Guidance bleiben unveraendert.

UpdateRequired; the named owner reviews project documentation and CI evidence.
The standalone preset remains the product source. Reevaluate on package,
profile, measurement-context or platform changes. No shared guidance or
existing statistics-methodology change is introduced.
