# Dokumentationsabgleich / Documentation Alignment

## Auftrag Und Herkunft / Authority and Provenance

DE: Der Owner genehmigte den zuvor besprochenen Gesamtplan mit
"Ja, Plan umsetzen." Markdown ausbauen, kein Website-System; offene
technische Punkte als eigene Arbeitspakete untersuchen. Keine Commits,
Pushes, Plattformaenderungen, Produktlaeufe oder produktiven Neustarts.
Vorhandene lokale Aenderungen und historische Nachweise erhalten.

EN: The owner approved the discussed plan: expand Markdown, no website;
investigate technical follow-ups as separate work packages. No commit, push,
platform change, product run or production restart. Preserve existing local
changes and historical evidence.

DE: Didaktische Referenz: ADE-Dokumentation, am 2026-10-25 authentifiziert
gelesener Main-Commit `7de47d81780f949d0f41101227dbfed53de9ee10`. Geprueft
wurden README, Grundidee, Sprach-/Agenten-Gliederung, FAQ und A11Y-Seite.
Die Referenz ist privat. Keine Texte, privaten Anhange oder Konfigurationen
werden kopiert; oeffentliche Lernwege setzen keinen Zugang dorthin voraus.
Institutions-, Provider-, Docker- und Kontovorgaben werden nicht uebernommen.
Fachliche Quelle fuer die Berufszuordnung ist die
[BIBB-Uebersicht](https://www.bibb.de/de/pressemitteilung_121075.php).

EN: The teaching reference was read through authenticated access at the exact
main commit above: README, basics, language/agent outlines, FAQ and A11Y page.
It is private. No text, private attachments or configuration is copied, and
public learning paths do not require access. Institutional, provider, Docker
and account defaults are not adopted. BIBB is the occupational reference.

## Vergleich Und Massnahmen / Comparison and Actions

DE: Jede Zeile ordnet ein Vorbild-Thema einer hiesigen Seite und einem
konkret pruefbaren redaktionellen Ergebnis zu. Das ist kein bestandener
Lernenden- oder Plattformtest.

EN: Each row maps a reference topic to a local page and a checkable editorial
outcome. This is not a passed learner or platform test.

| ID | Thema / Topic | Ziel unter docs/ / Target under docs/ | Luecke und Ergebnis / Gap and outcome |
|---|---|---|---|
| DOC-01 | Orientierung / orientation | fuer-lernende/README.md, lernwege.md | gemeinsame Grundlage plus acht Zielgruppenpfade / shared foundation plus eight audience paths |
| DOC-02 | Entwickler-Einstieg / developer entry | fuer-lernende/entwickler-kurzpfad.md | kurzer Weg ohne Sicherheitsabkuerzung / short path without security shortcut |
| DOC-03 | Host und Container / host and container | fuer-lernende/container-grundlagen.md, erste-schritte.md | keine perfekte Isolation oder Plattformgleichheit behaupten / no perfect isolation or platform-equivalence claim |
| DOC-04 | Einrichtung / setup | fuer-lernende/installation.md | drei getrennte Plattformpfade, Bash/PowerShell, Env-Dateien ohne Ueberschreiben / three platform paths, shells and non-overwriting env setup |
| DOC-05 | Sprachen / languages | fuer-lernende/toolchains/README.md | bestehende sechs Sprachen plus Skriptbasis behalten / retain six languages plus scripting foundation |
| DOC-06 | Agenten und SDD / agents and SDD | fuer-lernende/agenten-und-spec-kit.md | Voraussetzungen, begrenzte Auftraege und V2-Grenzen / prerequisites, bounded tasks and V2 limits |
| DOC-07 | Betrieb und Daten / operations and data | fuer-lernende/alltag.md, faq.md | Stopp, Reset, Neubau und Neuerstellung unterscheiden / distinguish stop, reset, rebuild and recreation |
| DOC-08 | Hilfe / help | fuer-lernende/faq.md, troubleshooting.md | haeufige Fragen und datensparsame Fehlermeldung / common questions and data-minimal reports |
| DOC-09 | A11Y und Sprache / A11Y and language | fuer-lernende/barrierefreiheit.md | pruefbare Redaktion plus offene menschliche Rendering-Abnahme / editorial checks plus open human rendering acceptance |
| DOC-10 | Status / status | betrieb/README.md, validierung-und-wartung.md | historische Scanwerte von aktuellem Kandidaten trennen / distinguish historical scans from current candidate |
| DOC-11 | Nachpruefung / follow-up | security/toolchain-followups-2026-10-25.md | AMD64, V2 und Warnungen mit Owner/Trigger / AMD64, V2 and warnings with owner/trigger |
| DOC-12 | Quellenbindung / source binding | intake receipts and series | drei gezielte Updates, Archivtreue, unabhaengiges Vollreview / three targeted updates, faithful archives, independent full review |

## Reihenfolge Und Reviewgrenze / Sequence and Review Boundary

DE: Der vorangegangene Quellenabgleich ist ein erhaltener Snapshot.
Sein damaliger AGENTS-SHA-256 `30032f667790bf30e113b4c67ce64adc6a06412d7b6ddd44562f2ea08f55898f`
wurde durch die ausdruecklich beauftragten Version-/Dokumentationsaenderungen
zunaechst zu `3b43341933a5c77b8f7868b5e3b056a8b305ab43116cf11c2b752aa964d59659`.
Dieser Zwischenstand ist vor der synchronen Korrektur der normalen
Stopp-Beispiele ebenfalls archiviert. Die endgueltige aktuelle AGENTS-Bindung
steht in den drei neuen Receipts; keine Volume-Loeschung als Normalstopp.
Die neue Bindung erfolgt in Operation
`64d6ad91-2d6e-4e63-a340-0fdb4d3a6b1c`; die vorherigen Ziel-, Receipt- und
Review-Bytes sind archiviert. Im unabhaengigen Erstreview gefundene
Dokumentationsfehler werden innerhalb dieses Auftrags korrigiert und erneut
unabhaengig geprueft, nicht als akzeptierte Risiken geschlossen.

EN: The preceding alignment is a retained snapshot. Its earlier AGENTS hash
first changed to the intermediate value above through requested changes.
That intermediate is also archived before synchronising normal shutdown
guidance. The three new receipts bind final agent guidance, without treating
volume deletion as ordinary shutdown. The new operation archives previous target,
receipt and review bytes. Documentation findings from the independent first
review are corrected within this task and independently re-reviewed, never
closed through agent risk acceptance.

DE: Erst Dokumentation und technische Untersuchung abschliessen, dann Quellen
binden und unabhaengig vollstaendig reviewen. Die abgeschlossene GSDB bleibt
historischer Vorgaenger. Die Reihe bleibt Completed, Eligible, Blocked,
Blocked. Keine neue Feature-Spezifikation und kein impliziter Produktstart.
Inhaltliche Anforderungspruefung, technische Abnahme, menschliche A11Y-Pruefung
und formelle Freigabe bleiben getrennt.

EN: Finish documentation and technical investigation before binding sources
and independent full review. The completed GSDB remains the historical
predecessor; preserve Completed, Eligible, Blocked, Blocked. No new feature
specification or implicit product start. Requirements review, technical
acceptance, human A11Y testing and formal approval remain separate.
