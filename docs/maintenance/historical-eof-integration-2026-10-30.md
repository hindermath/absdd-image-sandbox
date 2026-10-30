# Kanonischer EOF-Fix und begrenzte Integration / Canonical EOF fix and bounded integration

## Zusätzliche Freigabe / Additional authority

DE: Nach Meldung des exakt eingegrenzten EOF-Blockers erteilte der Owner
ausdrücklich die ergänzende Freigabe: „Bitte den kanonischen Validator samt
Regressionstests korrigieren, Archivbytes erhalten und anschließend
MergeAndSync mit Admin-Bypass abschließen. Wieder an den Agenten übergeben.“
Dies umfasst die formatneutrale EOF-Korrektur im aktiven Update-Lastenheft,
kontrollierte Archivierung/Erneuerung betroffener Bindungen und vollständiges
Nachreview. Keine historische Archiv-/Issue-Snapshotdatei wird umgeschrieben.

EN: After the exact EOF blocker was reported, the owner explicitly approved
the canonical validator correction and regression tests, preservation of
archive bytes and subsequent MergeAndSync with admin bypass, delegated to the
agent again. This includes neutral EOF normalization of the active update,
controlled preservation/rebinding and complete re-review. Never rewrite
historical archive or issue-snapshot bytes.

## Kanonische Quelle und Integration / Canonical source and integration

DE: Ausschließliche Produktquelle ist das eigenständige veröffentlichte Preset
`hindermath/spec-kit-preset-autonomous-run-governance`, Patch v0.4.8.
PR #28 bindet den Fix und native CI. Die begrenzte Verbraucherübernahme bindet
Release-Tag/Commit, extern heruntergeladenes ZIP und dessen Roh-SHA-256.
Nur dieses Preset wird aktualisiert. Die übrigen 13 installierten Payloads,
Prioritäten, registrierten Commands und Skills bleiben unverändert.
Lokale Profilmatrizen und aktive Installed-/Source-Locks werden konsistent
fortgeschrieben; frühere zeitgebundene Installationsnachweise bleiben erhalten.
Die beiden Constitution-Pins werden gemeinsam aktualisiert; Agent-Guidance
und Composition wurden auf Anpassungsbedarf geprüft, ohne neue Pflichten.

EN: The published standalone preset is the sole product source, patch v0.4.8.
PR #28 binds the fix and native CI. Bind consumer integration to exact release
tag/commit, independently downloaded ZIP and raw SHA-256. Update this preset
only; preserve the other thirteen payloads, priorities, registered commands
and skills. Keep local profiles and active installed/source locks consistent,
without rewriting dated historical installation records. Update both active
constitution pins together; review agent guidance/composition without adding
new obligations.

DE: Die bestehende exakte Pfad-/Rohhashausnahme erfasst jetzt zusätzlich
historische Leerzeilen am Dateiende. Neue Dateien im Index und unveränderte
Rohbytes bleiben Voraussetzung; andere EOF-Befunde, Konfliktmarker,
unvollständige Inventare und Hashdrift bleiben Fehler. Die ergänzten
LF-/CRLF-, Positiv-/Negativ- und Null-Schreibtests belegen dies. Keine Git-
Whitespace-Einstellung und keine pauschale Archivprüfung wird gelockert.

EN: The existing exact-path/raw-hash exception now includes historical EOF
blank lines. Newly added staged files and unchanged raw bytes remain required;
unapproved EOF, conflict markers, incomplete inventory and hash drift still
fail. Added LF/CRLF, positive/negative and zero-write tests cover these limits.
No Git whitespace setting or blanket archive exemption is relaxed.

## Reichweite / Boundaries

DE: Nur Source-/Preset-/Intake-Lieferung. Kein Home-Sync, Flottenrollout,
Image-Build, Containerstart oder Neuerzeugung. Feature 004 wird nicht
implementiert oder fortgesetzt. Fünf Ziele/fünf Kanten/eine Root und
Completed/Eligible/Blocked/Blocked/Blocked sowie alle Human-only-Gates bleiben.
Die zentrale Home-Baseline-/Flottenmatrix wird durch diesen bewusst lokalen
Verbraucherpatch nicht stillschweigend geändert.

EN: Source/preset/intake delivery only: no Home sync, fleet rollout, image
build, container start/recreation or Feature 004 execution. Preserve five
targets/edges, one root, lifecycle and human gates. Do not silently update the
central Home Baseline/fleet profile for this deliberately local consumer patch.

Documentation Impact: UpdateRequired; Owner Maintainer. Audiences maintainers
and intake reviewers. Canonical sources: explicit authority, published preset,
release/integration proof, current receipts and full review. Existing source
order, requirements, prompts, security/A11Y/privacy decisions remain intact.
German-first/equivalent English, sourceOnly, no Home sync. Reevaluate on
package, archive, source/hash, graph, review or authority drift.
