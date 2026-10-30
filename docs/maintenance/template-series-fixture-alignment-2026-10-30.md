# Begrenzter CI-Abgleich / Bounded CI alignment

DE: PR #106 zeigte zwei veraltete Regressionserwartungen: eine Viererreihe
trotz ausdrücklich genehmigter Fünferreihe und einen Vergleich des datierten
Workshopprofils vom 25.10.2026 gegen die heutige operative Preset-Matrix.
Der beauftragte Veröffentlichungsabschluss korrigiert ausschließlich diese
mechanische Konsistenz: fünf exakte Statuswerte und beide neuen bindenden
Update-Kanten prüfen; den historischen Workshop über seine erhaltene
Rohhash-Quelle prüfen, einschließlich manipulierter Hash-/Inhaltsfälle.
Die aktive 14er-Matrix bleibt unabhängig strikt an aktuelle Paket-/Quellen-
Locks gebunden. Keine Prüfung abschalten und keine Archiv-/Exportbytes ändern.

EN: PR #106 exposed two stale regression assumptions: four members despite
the explicitly approved five-member series, and comparison of the dated
2026-10-25 workshop profile to today's operational install matrix. Correct
only this mechanical consistency within authorized delivery: check five exact
states and both binding update edges; validate the preserved historical
workshop source by raw hash with tampered-hash/content negatives. Separately
retain strict current fourteen-preset payload/source checks. Disable no test
and rewrite no archive or presentation export.

DE: Nur H-/A-/L-Receipt-Metadaten werden erneuert, weil der korrigierte
Template-Test eine gebundene Quelle ist. Alle fünf Zieltexte, U-Receipt,
Serienmanifest/-Receipt und DAG/Lifecycle bleiben bytegleich. Alte Receipts,
Ziele, Testquelle und Reviewstände werden archiviert; vollständiges Nachreview.
Kein neuer Implementierungs-, Präsentations-, Image-, Runtime-, Home- oder
Flottenauftrag. MergeAndSync-/Admin-Grenzen bleiben unverändert.

EN: Renew H/A/L receipt metadata because the corrected template test is a
bound source. Preserve all five target texts, U receipt, series manifest/
receipt and graph/lifecycle byte for byte. Archive previous receipts, targets,
test and review evidence, then perform full re-review. No feature, presentation,
image, runtime, Home or fleet execution. Existing delivery/admin limits remain.

Documentation Impact: UpdateRequired. Owner Maintainer, audience reviewers
and workshop users. Canonical sources: approved five-member manifest, dated
workshop source and explicit bounded publication authority. Existing DE/EN
reader paths; sourceOnly, no Home sync. Reevaluate on source/profile/hash or
series drift. This source check is not product/human/A11Y acceptance.
