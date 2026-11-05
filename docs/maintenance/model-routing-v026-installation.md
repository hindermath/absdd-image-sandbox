# Model Routing 0.2.6 und Autonomous Run 0.4.10: Installation

## Deutsch

Documentation Impact: **UpdateRequired**. Owner: Thorsten Hindermann.
Kanonische Quellen sind die beiden veröffentlichten Presets, die projektgeführte
14er-Matrix und der maschinenlesbare
[Installationsnachweis](model-routing-v026-installation.json). Leserpfad:
README → dieser Nachweis → installierte DE-/EN-Preset-Dokumentation. Zielgruppen
sind Maintainer, Lernende und Entwickelnde. Deutsch steht zuerst; die englische
Fassung ist gleichwertig. Die Texte zielen auf CEFR B2 und anwendbare WCAG 2.2
AA. Statische Prüfungen ersetzen keine vollständige Barrierefreiheitsabnahme.

Der freigegebene Umfang aktualisiert genau vier Repositories: Level 0,
`Show-CommandTui400`, `TinyCalc` und `absdd-image-sandbox`. Model Routing steigt
von 0.2.5 auf **0.2.6** bei Priorität 61. Autonomous Run steigt in der
vereinheitlichten Matrix auf **0.4.10** bei Priorität 70. Die übrigen zwölf
Preset-Payloads, Versionen und Prioritäten bleiben erhalten. Andere
Flottenziele, Produktläufe, SDK-Installationen, Container-/Imagewechsel und
persönliche Modellprofile sind nicht Teil der Lieferung.

Die veröffentlichten Quellen sind unveränderlich gebunden:

- Model Routing `v0.2.6`: Commit
  `bf4509b364a89d276740470741e3a9d239b3eb72`, ZIP-SHA-256
  `ed2bf38dda728f9b8be4df7e539367b1a3eea56b74402c283587e0fca571f17f`,
  95 Dateien, 204941 Bytes.
- Autonomous Run `v0.4.10`: Commit
  `2de46fd1c1342bba195ab0487d82f0d1d4c22602`, ZIP-SHA-256
  `1e825c75bcf0c73b4a7c2065096ff4d4c015ba2fc67ca507b40170f0d3884765`,
  80 Dateien, 168607 Bytes.

Die installierten Payloads stimmen mit diesen Archiven überein. Level 0 führt
zusätzlich die weiterhin vorrangigen Resolver- und Adapter-Einstiege aus
demselben Model-Routing-Release. Autonomous Run 0.4.10 verwendet die installierte
Ausführungsrichtlinie aus Model Routing 0.2.6; damit gelangen die zuvor im
gekoppelten Smoke-/Integrationstest geprüften Rollenrechte in den normalen
Ausführungspfad. Codex- und `agy`-Auswahlsemantik bleibt unverändert.

Die Installation führt keine Modellinferenz, Anmeldung, Profilerneuerung oder
API-Key-Konfiguration aus. Mehrdeutige oder nicht mehr gültige Modelle bleiben
fail-closed. Home-Sync betrifft ausschließlich manifestgebundene Level-0-
`homeRuntime` und erfolgt nach zentraler Lieferung mit Check, Vorschau,
`--runtime-only --no-pull` und Abschlussprüfung. Die Level-2-Installationen
erteilen keine Home-Sync-Autorität für andere Rechner.

Abnahme: exakte 14er-Matrix, Release-/Installationshashes, Erhalt der übrigen
zwölf Presets, Root-/Preset-Parität, Model-Routing- und Autonomous-Tests,
Agentenflächenparität, PSScriptAnalyzer, Secrets-Prüfung und native PR-CI.
Live-Modellaufrufe sind bereits separate Release-Evidence und werden durch
diese Installation nicht erneut ausgelöst. Neu bewerten bei Release-, Archiv-,
Matrix-, CLI-/SDK-, Manifest- oder Plattformdrift.

Distributionsklasse: Projektintegration, versionierte Wartungsskripte,
Source-Dokumentation und begrenzte Level-0-Home-Runtime. Reine historische
Evidence bleibt unverändert.

## English

Documentation Impact: **UpdateRequired**, owner Thorsten Hindermann. Canonical
sources are the two published presets, the project-managed fourteen-preset
matrix and the linked machine-readable installation record. Reader path:
README → this record → installed paired preset documentation. Audiences are
maintainers, learners and developers. German comes first with equivalent
English. The text targets CEFR B2 and applicable WCAG 2.2 AA; static checks are
not a complete accessibility acceptance.

The approved scope updates exactly four repositories: Level 0,
`Show-CommandTui400`, `TinyCalc` and `absdd-image-sandbox`. Model Routing moves
from 0.2.5 to **0.2.6** at priority 61. Autonomous Run is aligned on **0.4.10** at
priority 70. The other twelve preset payloads, versions and priorities are
preserved. No other fleet targets, product runs, SDK installations,
container/image changes or personal model profiles are included.

The immutable source bindings, sizes and hashes are listed above. Installed
payloads match both archives. Level 0 also copies the still-precedent resolver
and adapter entry points from the same Model Routing release. Autonomous Run
0.4.10 consumes Model Routing 0.2.6's installed execution policy, carrying the
role permissions validated by the coupled smoke/integration test into the
normal execution path. Codex and `agy` selection semantics remain unchanged.

Installation performs no inference, login, profile refresh or API-key setup.
Ambiguous or stale models remain fail-closed. Home sync is restricted to
manifest-bound Level-0 `homeRuntime` after central delivery, using check,
preview, `--runtime-only --no-pull`, and a final verification. Level-2 installs
grant no Home-sync authority for other computers.

Acceptance covers the exact fourteen-preset matrix, source/installation hashes,
preservation of the other twelve presets, root/preset parity, Model Routing and
Autonomous tests, agent-surface parity, PSScriptAnalyzer, secret scanning and
native PR CI. Live model calls remain separate release evidence and are not
repeated by installation. Re-evaluate on release, archive, matrix, CLI/SDK,
manifest or platform drift.

Distribution: project integration, versioned maintenance scripts, source
documentation, and bounded Level-0 Home runtime. Historical evidence remains
unchanged.
