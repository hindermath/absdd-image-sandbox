# Intake Sequencing Governance v0.2.13

## Deutsch

Nur Intake Sequencing Governance wurde von 0.2.12 auf 0.2.13 aktualisiert;
die anderen 13 Presets behalten Version, Prioritaet und installierten Inhalt.
Das Dokumentationspatch beschreibt die Sicherheitspruefungen aus 0.2.12
korrekt. Skripte, Commands und Templates sind unveraendert; der
Receipt-Generator bleibt 0.2.12. Keine neue Produkt- oder Ausfuehrungsfreigabe.

Quelle: Quell-PR hindermath/spec-kit-preset-intake-sequencing-governance#22,
Merge-/Tag-Commit 41ffb8fc93f857d1914e8be3693b7f6d021f5231.
ZIP SHA-256: 7dd29964d16bb8a8e0a107c2054ae8e0f69da99bdb7a6d5f320337d055fde3de.
Die 63 Archivdateien wurden bytegleich zum Tag geprueft. Eine isolierte
Installation und die Aufloesung aller 12 Templates und sechs Commands
bestanden. Alle sechs nativen Quell-CI-Checks bestanden. Der zentrale
Installer wurde mit einem Ein-Preset-Profil nach Vorschau ausgefuehrt;
danach binden die Source-/Installed-Locks den neuen Stand. Weitere lokale
und gehostete Rollout-Pruefergebnisse stehen am zugehoerigen Liefer-PR.

## English

Only Intake Sequencing Governance changes from 0.2.12 to 0.2.13. The other
thirteen packages retain their versions, priorities and installed payloads.
The documentation patch accurately describes the security checks introduced
in 0.2.12. Runtime scripts, commands and templates are unchanged; receipt
generator remains 0.2.12. This grants no product or execution authority.

The tag/archive binding above was verified byte-for-byte. Isolated
installation and all twelve template/six command resolutions passed, as did
all six native source CI checks. A preview preceded the focused one-preset
installer. Source and installed locks bind the resulting state; current
local/hosted delivery checks are recorded on the delivery PR.

Documentation Impact: UpdateRequired. Owner: Thorsten Hindermann. Audience:
workspace maintainers and reviewers. Canonical sources: preset release,
profile matrices and separate source/installed locks. Navigation: this record
and project-statistics ledger. DE/EN together; text-first Markdown.
Distribution: installed package/source evidence plus homeRuntime profile
matrices where assigned by the distribution manifest. Home sync is checked
after Level-0 merge; consumer repositories receive no Home sync.
Re-evaluate on source, matrix, installed payload or review drift.
