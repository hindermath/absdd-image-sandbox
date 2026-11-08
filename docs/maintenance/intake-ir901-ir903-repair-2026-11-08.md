# IR901–IR903: begrenzter Intake-Abgleich / Bounded Intake Repair

## Deutsch

Auftrag vom 2026-11-08: IR901–IR903 beheben und danach die vollständige
fünfgliedrige Reihe neu prüfen. Keine neue Sandbox-Implementierung,
Serienpromotion, Risikoannahme, Commit-, Push- oder Remote-Schreiboperation.
Alle Intake-IDs, fünf Mitglieder, fünf Kanten, die archivierte Root,
85-/80-Prozent-Schwellen und menschlichen Gates bleiben erhalten.

IR901: Die 17 Quellenänderungen seit dem gebundenen Stand wurden gegen
`e115fa863e754a83eff212c72f130f6f8543a988` und den aktuellen Head
`d165d49a1b206cc94cce3b640dd14dec88b8857f` fachlich abgeglichen:

| Quellen / Sources | Bewertung / Assessment |
|---|---|
| Assurance-Vertrag und beide User-Guides | Installierte Paketkennung 0.1.9 statt 0.1.8; scope/rationale, gültiges reviewDue und assessmentIds verbessern die Nachvollziehbarkeit menschlich akzeptierter Risiken. Keine Risikoannahme oder Schwellensenkung. / Installed 0.1.9 adds scoped, justified, unexpired, assessment-linked risk records without accepting risks or lowering thresholds. |
| AGENTS, CLAUDE, GEMINI und beide Copilot-Guidances | Pin-Register ersetzt Renovate; App-Ports 5100–5198, OpenCode 5199; Profil-/Versionskontext. / Pin-register replacement, port split and profile/version context. |
| Dockerfile | Bereits vorhandene Resolute-Basis, native Pins/Prüfsummen, Swift/Python und weitere Versionsupdates, sieben bedingte Profile, gemeinsamer Web-/Health-Kern, Codex-readonly-Verzeichnis und .NET-Runtime-Auswahl; keine erneute Umsetzung durch diesen Abgleich. / Existing base/pin/profile/web/hardening changes are source context, not a new implementation task. |
| CLI-Registry und Versionspin-Tests | Swift 6.4.2, Resolute, Prüfwerte, Pin-Vorschläge und Runtime-Testanpassung. / Registry and tests follow the current versions and pin evidence. |
| Sandbox-Profil, Troubleshooting und README | Beschreiben bereits vorhandenen Web-/Profilbetrieb und sichere Fehlerhilfe; finale Plattformabnahme bleibt offen. / Describe existing behavior and recovery while retaining open final platform acceptance. |
| Drei bestehende CI-Workflows | Actions-Pins, Pin-Checker und Shell-Syntaxprüfung aktualisiert; Runnername belegt keine native Zielabnahme. / Updated action pins/checkers; runner names are not target acceptance. |

Das aktuelle Pin-Register, Dependency-Policy und zugehörige Workflows werden
zusätzlich direkt gebunden. FU-018 und Selbstbau-Qualitätsregeln benennen nun
den genehmigten Mechanismus. Syft-Pinning, Podman, Integritätsnachweise,
manuelle Review-/Merge-Gates und Verbot beweglicher Fallbacks bleiben erhalten.

Historische 0.1.8-Verweise sind der frühere geprüfte Werkzeugstand; der aktuell
installierte Prüfer ist Assurance 0.1.9. Dieselben Kontroll-IDs und Prüfziele
gelten weiter. Dessen strengere Risikometadaten werden eingehalten, ohne
Risiken agentisch anzunehmen. Die GSDB 3.4.4 bleibt die Kontrollbaseline.
Der datierte Bericht `feature-update-2026-11-06-acceptance.md` ist lokale
ARM64-Kandidatenevidenz, keine vollständige native AMD64-/Windows-/WSL2-,
A11Y-, unabhängige oder formale Abnahme. Bestehende Umsetzung zuerst bewerten.

IR902: Der installierte kanonische Lifecycle-Test verlangt ausdrücklich eine
separate, bytegleiche Archivkopie des eingefrorenen Vorgänger-Receipt.
`predecessor-inputs` dokumentiert die tatsächlich konsumierte Eingabe dieser
Operation; `intake-authoring-archive` sichert sie als getrenntes Archiv.
Beide Pfade und Rohhashes werden aufgezeichnet und gegeneinander geprüft.
Kein neuer Beleg wird erfunden, keine historische Datei umgeschrieben und
kein Validator abgeschwächt. Identische Datei/Hardlink, abweichende Bytes,
falsche Identität und Alias des aktiven Targets müssen weiter scheitern.

Vorgängerziel ist stets die erste Quelle, dieser Abgleich die zweite;
danach folgen bisherige Quellen in derselben Reihenfolge mit aktuellen
Repository-Hashes, anschließend ausdrücklich hinzugefügte Kontextquellen.
Quellen, Text und Nachweise werden separat archiviert. Das alte
NeedsRemediation wird ausdrücklich durch ein neues Vollreview ersetzt;
die Vorbereitung selbst behauptet kein Ready. Keine Betriebsfreigabe.

## English

The user authorized bounded repair of IR901–IR903 and a complete five-member
re-review on 2026-11-08. Preserve identities, graph, lifecycle, 85%/80%
thresholds and human gates. No feature implementation, state promotion,
risk acceptance, commit, push or remote write is authorized.

The table records semantic comparison of all 17 changed sources between the
previous source baseline and current head. Existing Resolute, Web, profile,
toolchain, pin/CI and documentation changes are assessed before any later
work; they do not prove final acceptance. The current pin registry, dependency
policy and workflows are additionally bound. FU-018 and learner quality rules
now name this approved mechanism, preserving Podman, fixed Syft, integrity,
manual review gates and the ban on moving fallbacks.

Historical 0.1.8 references identify the former reviewed tool baseline;
installed Assurance 0.1.9 performs the same control checks with stricter risk
metadata. Retain GSDB 3.4.4, control IDs, acceptance thresholds and human risk
decisions. The 2026-11-06 ARM64 candidate report grants no complete native
AMD64/Windows/WSL2, accessibility, independent or formal acceptance.

The canonical lifecycle fixture requires a distinct byte-identical archive
of the frozen predecessor receipt. Operation predecessor-inputs records the
consumed source; the configured archive preserves a separate copy. Record
both paths and hashes. Do not weaken validators, invent evidence or alter
historical files. Same-file/hardlink aliases, changed archive bytes, foreign
identity and active-target aliases must remain rejected.

Each predecessor target is first source, this alignment second, followed by
the prior ordered source chain with current repository hashes and explicit
new context sources. Archive former targets/receipts and review evidence
exactly. Preparation does not adjudicate readiness; a complete review follows.
