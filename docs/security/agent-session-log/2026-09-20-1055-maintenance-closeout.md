# Wartungsabschluss: Image-Pin / Maintenance closeout: image pin

## Deutsch

Der Owner hat MergeAndSync mit begrenztem Admin-Bypass fuer die zentralen
Wartungskorrekturen und alle 35 Flotten-Repositories ausdruecklich genehmigt.
Technische Gates bleiben verbindlich. Die bestehende Wartungsfreigabe endet
am 31.12.2026; keine Erweiterung von Provider-, Credential-, Mount- oder
CISO-/ISB-/KIB-Berechtigungen. Kein neuer Spec-Kit-Lauf.

Der Lock bindet den exakten veroeffentlichten PR-Commit
`3d07d6e467196fb8f34259aab4e3e56a024e4951` aus Home-Baseline PR #306.
Er korrigiert die Laufzeit-Eventphasen und die explizite Level-0-Profilwahl.
Die Aktivierung folgt erst nach bestandenen technischen Pruefungen.

P1-1: Audit-Metadaten exportiert; Sitzungsnachweis angelegt.
P1-4: bestehende begrenzte Owner-Freigabe, keine Rollenfreigabe behauptet.
P2-3: Build und finale CycloneDX-1.7-SBOM bestanden: 28.970 Komponenten.
Image: `7d9e45d0b042eeb082e299f7cbab95182bfb3ffcaf98b06b6f18b336bfec6444`.
SBOM: `sboms/2026-09-20-localhost-absdd-image-sandbox_ade-closeout-3d07d6e.cdx.json`,
SHA-256: `3dfca46d529e8a264506deb9a53803c8cdfc2d25c6458c7a5e349291e5ee8656`.
Die SBOM bleibt ein ignoriertes lokales Build-Artefakt. Zusaetzlich bestanden
22 Wrapper-Tests im netzwerklosen finalen Image. Der Wiederanlauf wird nach
der technischen PR-Abnahme im Lieferabschluss gesondert nachgewiesen.
Neun Pin-/Dokumentationstests, alle Pre-commit-Hooks, 22 netzwerklose
Container-Delegationstests sowie die vollstaendige Paket-Hashbindung und
der Schreibschutz der Image-Referenz bestanden. Die statische
Compose-Konfiguration blieb bytegleich. Bestehende Volumes bleiben erhalten.
Die lokale private Rueckfallsicherung
`localhost/absdd-image-sandbox-recovery:before-closeout-3d07d6e`
bewahrt die bisherige beschreibbare Container-Schicht und wird nicht publiziert.

Documentation Impact: UpdateRequired. Quellen: Lock, Freigabetabelle und
dieser historische Nachweis; Owner: Repository-Owner. Zielgruppe: Maintainer,
Einstieg ueber den vorhandenen README-Verweis zur Home-Baseline-Referenz.
Deutsch zuerst, Englisch danach; Source-/Image-Distribution. Der Pin selbst
benoetigt keinen Host-Home-Sync. Re-Evaluation bei Pin-/Freigabeaenderungen.
Der abschliessende Flottenlauf ist getrennt nachzuweisen.

### Nachtrag: Canary-Korrektur vor Aktivierung

Der erste Consumer-Canary fand einen vorzeitigen Bash-Engine-Preflight vor
UI-Abbruch und Home-Delegation. Home-Baseline PR #307 korrigiert die
Reihenfolge ohne Lockerung der Engine-Barrieren. Der finale Lock zeigt auf
`b96e6c861a448f01582855248a26250fdd76371c`; der obige erste Kandidat wurde
nicht aktiviert. Neues Image:
`f36c14322097f538019943923e3fa32018a0a48145f8cc28b0c36b7f1da50899`.
23 Wrapper-Tests, 22 zentrale Delegationstests und neun Pin-/Dokumentations-
tests bestanden; Pre-commit, komplette Paket-Hashbindung und Schreibschutz
ebenfalls. Die sieben source-abhaengigen Integrationsfaelle der 22er-Suite
werden zentral geprueft, nicht gegen absichtlich reduzierte Consumer-Pakete.
Finale CycloneDX-1.7-SBOM: 28.970 Komponenten,
`sboms/2026-09-20-localhost-absdd-image-sandbox_ade-closeout-b96e6c8.cdx.json`,
SHA-256 `a95969b28399a57befb174cdd03003b482bc6c3d7fd354c2184f5119a280edee`.
Aktivierung weiterhin erst nach technischer Abnahme; Freigabeumfang unveraendert.

## English

The Owner explicitly approved MergeAndSync with bounded admin bypass for
the central corrections and all 35 fleet repositories. Technical gates
remain mandatory. Existing maintenance authority expires on 2026-12-31;
provider, credential, mount and formal role authority are not expanded.
No Spec Kit run is started.

The lock binds the exact published commit above from Home-Baseline PR #306,
correcting runtime event phases and scoped Level-0 profile selection.
Activation requires successful technical checks.

P1-1: audit metadata exported and session recorded. P1-4: existing bounded
Owner authority, not formal role approval. P2-3: build and final CycloneDX
1.7 SBOM passed with 28,970 components. The exact image, local ignored SBOM
and hash are recorded above. Another 22 wrapper tests passed in the
network-disabled final image. Restart evidence follows technical PR
acceptance and is recorded separately in delivery closeout.
Nine pin/documentation tests, all pre-commit
hooks, 22 network-disabled delegation tests, complete package hash binding
and immutable source checks passed. Static Compose configuration is
byte-identical. Existing named volumes will be retained. The private local
recovery image above preserves the previous writable container layer and
must not be published.

Documentation Impact is UpdateRequired. The lock, approval table and this
historical evidence serve maintainers through the existing README path.
Repository Owner owns these bilingual source/image artifacts. Pin changes
alone need no host Home sync. Reevaluate on pin or approval changes;
final fleet maintenance needs separate evidence.

### Addendum: canary correction before activation

The first consumer canary found premature Bash engine preflight before UI
cancellation and Home delegation. Home-Baseline PR #307 fixes ordering without
weakening barriers. The final lock binds `b96e6c861a448f01582855248a26250fdd76371c`;
the first candidate above was not activated. The replacement image and final
SBOM path/hash are recorded above. Its 23 wrapper tests, 22 central delegation
tests, nine pin/documentation tests, pre-commit and immutable package bindings
passed. Seven source-dependent integration cases belong to the complete
central suite, not deliberately reduced consumer packages. The CycloneDX 1.7
inventory contains 28,970 components. Activation still requires technical
acceptance; existing authority remains unchanged.
