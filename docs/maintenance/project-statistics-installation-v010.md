# Statistik-Preset-Installation: ABS-DD Sandbox

## Stand / Status

Am 2026-09-14 lokal auf `codex/project-statistics-installation` installiert
und geprueft: Project Statistics Governance v0.1.0, aktiviert mit Prioritaet 90.
Das genehmigte Projektprofil ist `project-statistics-fourteen-governance-presets`.
Die vorhandenen 13 Presets bleiben unveraendert. Dies ist ein Installationsnachweis,
kein Messbericht und keine Feldtest-Abnahme. Commit, Push, PR und Merge sind
noch offen; die operative Registry-Zuordnung folgt erst nach Lieferung.

Installed and verified locally on the named pilot branch: v0.1.0 at priority 90
in the approved fourteen-preset profile. All thirteen existing presets remain
unchanged. This records installation only, not measurements or field acceptance.
Commit, push, PR and merge remain pending; operational assignment follows delivery.

## Quelle und Bindung / Source and binding

- [Projekttracking / Project tracking](https://github.com/hindermath/absdd-image-sandbox/issues/70)
- [Zentrales Feldtesttracking / Central tracking](https://github.com/hindermath/spec-kit-preset-project-statistics-governance/issues/1)
- [Zentrale Profilvorbereitung / Central profile PR #299](https://github.com/hindermath/home-baseline/pull/299)
- [Veroeffentlichtes Pre-Release / Published pre-release](https://github.com/hindermath/spec-kit-preset-project-statistics-governance/releases/tag/v0.1.0)
- Paketcommit / package commit: `7e824ca8de11212aefdc5b05d7d05637f5343dab`.
- ZIP-SHA-256: `d8ad7d5eef920f50b629121b64ba8123c22ec4f6dadd14da5cd826d1c50f420a`.
- Ausgangscommit / baseline commit: `1ec3e8e990c2bc59e72328619ff56a1df15a56d3`.
- [Dateiweise SHA-256-Bindungen und Pruefwerte / File hashes and check results](project-statistics-installation-v010.json).

Das Tag-ZIP wurde vor Installation gegen den SHA-256 und den aufgeloesten
Tag-Commit geprueft. Danach wurden alle 26 installierten Paketdateien erneut
bytegenau mit dem geprueften Archiv verglichen. Die Spec-Kit-Registry bezeichnet
den URL-Import als `source=local`; die externe Quellenbindung steht deshalb
explizit im Nachweis. Keine GitHub-Release-Immutability behauptet.

The archive was verified before installation; all 26 installed files then
matched it byte for byte. Spec Kit records the URL import as `source=local`;
the receipt provides explicit external provenance. No platform-enforced
release immutability is claimed.

## Ausgefuehrte Pruefungen / Executed checks

Umgebung / environment: Linux/aarch64 (Podman), PowerShell 7.6.4, Spec Kit 0.12.8.

| Pruefung / Check | Ergebnis / Result |
| --- | --- |
| Bash- und PowerShell-Installer mit expliziter 14er-Matrix, CheckOnly | Je Exit 0; exakt 14 aktive Presets mit richtigen Versionen und Prioritaeten |
| `specify preset list` und `preset info project-statistics-governance` | Exit 0 |
| Resolve: Statistik-/Assurance-Vertrag sowie Constitution-, Plan-, Tasks-Template | Exit 0; beide Vertraege und komponierte Template-Kette vorhanden |
| `specify check` | Exit 0; CLI einsatzbereit, optionale nicht installierte Agenten nicht als Pflichtfehler gewertet |
| Neue generierte Agenten-/Command-Dateien | 15 Dateien; Skriptpfade auf das installierte Preset gebunden |
| Erhaltungspruefung direkt nach Installation | 467 vorhandene Dateien und 13 Registry-Eintraege unveraendert |
| Installierter Lifecycle-Test in temporaerer Fixture | Exit 0: Install, Commands, Resolve, Disable/Enable, Remove/Reinstall; authored data erhalten |
| Reale Messung, Init, Update oder neues Spec-Kit-Feature | Nicht gestartet / not started |

Die Erhaltungspruefung liegt zeitlich vor den hier dokumentierten gezielten
Guidance-, Katalog-, Ausschluss- und Ledger-Ergaenzungen. Diese sind eigene
Integrationsaenderungen, keine Aenderungen am Paket oder an den alten Presets.
Die bisherigen Agenten-Commands wurden nicht migriert. Spec Kit meldete den
vorhandenen Legacy-Pfad `.opencode/command`; dessen Migration ist nicht Teil
dieses Auftrags.

Preservation was checked before the explicit integration documentation and
configuration changes. Existing presets and commands were not migrated.
The legacy OpenCode directory warning is documented, not silently repaired.

## Betriebsgrenzen und Folgeschritte / Boundaries and next steps

- Die bestehende `docs/project-statistics.md` bleibt kanonisch. Keine Migration,
  Personenbewertung, KI-Produktivitaets- oder Zeitersparnisbehauptung.
- Der spaetere Kontext ist `docs/project-statistics-pilot/`. Es wurde noch
  keine Konfiguration initialisiert; Referenz-Modellrechnungen bleiben aus.
- Globale Defaults bleiben unveraendert. Die lokale Level-2-Registry wird
  nicht vor Commit-/PR-/Merge-Lieferung umgestellt.
- Die allgemeine Level-0-Wartung verwendet derzeit `defaultPresetProfile`
  auch fuer Level 0. Ein unabhaengiger Level-0-Override fehlt. Deshalb im
  Pilot nur die explizite 14er-Matrix pruefen; keine Flottenreparatur mit
  `--force`. Vor regulaerer Wartungsintegration muss diese Grenze geklaert sein.
- Statistik-Rendering folgt dem Inhaltscommit; der erzeugte bisherige
  Profil-2-Block wird nicht mit dirty-tree-Bypass aktualisiert.
- Kein Home-Runtime-Sync, kein Image-Build, keine Community-Einreichung.
- Native Windows-Pruefung dieser konkreten Projektinstallation ist nicht
  ausgefuehrt. Die Drei-Plattform-Produkt-/Profil-CI aus PR #299 ersetzt keine
  projektspezifische Feldtest-Abnahme.
- Sandbox-Arbeit erfolgte als `adedev` im vorhandenen Pilotimage (ID `a33180f5cb18158d894792613479d5864e7a28c64d9308b6fbf7f724a36f4842`). Nur die freigegebene prozesslokale Git-Vertrauensausnahme fuer `/ade-dev-sandbox`; kein globales `safe.directory`. Die urspruengliche Host-Arbeitskopie bleibt unveraendert. Menschliche Sichtung vor Commit und Push ist ein eigenes Pflichtgate.

Existing statistics remain authoritative. No measurements, migration, people
ratings or AI savings claims. Global defaults stay unchanged; explicit pilot
matrix checks avoid the missing independent Level-0 maintenance override.
Resolve that integration limit before routine fleet repair. Render legacy
statistics only after the content commit. No Home sync, image build or community
submission. Native Windows project evidence and human field acceptance remain
open. Sandbox work used the non-root pilot container and only the approved process-local Git trust exception; human review is required before commit and push.

## Dokumentationsauswirkung / Documentation impact

`UpdateRequired`. Owner: Thorsten Hindermann. Zielgruppen: Lernende,
Maintainer und Reviewer; Leserpfad: README/Agent-Guidance -> dieses Dokument ->
Quellen/Pruefwerte -> spaeterer separater Messbericht. Kanonische Produktquelle
ist das eigenstaendige Preset-Repository; Profilquelle ist Home Baseline.
ActiveSemantic, DE zuerst/EN danach, textorientierte Tabellen.
Distribution: lokale Projektintegration; kein Home-Runtime-Sync.
Constitutions und Environment Registry wurden geprueft: keine Produkt-API,
Runtime oder bestehende Statistik-Referenz geaendert, daher keine dortige
Regelaenderung. Neue Addenda liegen als komponierbare Preset-Templates vor.
Wiedervorlage bei Paket-, Profil-, Quellen-, Runtime- oder Messkontextwechsel.

NIST SSDF und CWE Top 25 sind fuer die Integrations-/Lieferkettenpruefung
beruecksichtigt. ASVS ist fuer diesen nicht-Web/API-Installationsdelta N/A;
AI-SBOM fuer Modell-Runtime N/A (nur Entwicklungswerkzeug), Image-SBOM-Neubau
N/A (unveraendertes Image), VEX keine neue Disposition. SLSA/Provenance wird
durch konkrete Quellen-/Hashnachweise unterstuetzt, ohne Level-Behauptung.
Keine Architektur-/Zero-Trust-Aenderung und keine fachliche Freigabe.

UpdateRequired; the maintainer owns bilingual integration documentation.
The standalone preset owns package logic; Home Baseline owns profiles.
Existing runtime, APIs, statistics references and constitutions are unchanged.
Security review covers source provenance and preserved integration boundaries;
no new product, architecture, compliance or certification approval is inferred.
Reevaluate on package, profile, source, runtime or measurement-context change.
