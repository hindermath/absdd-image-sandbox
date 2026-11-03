# Model Routing Governance 0.2.3: Installation

## Deutsch

Documentation Impact: **UpdateRequired**. Owner: Thorsten Hindermann.
Kanonische Quellen sind das veröffentlichte Preset, die projektgeführte
14er-Matrix und der maschinenlesbare [Installationsnachweis](model-routing-v023-installation.json).
Leserpfad: README → dieser Nachweis → installierter DE-/EN-Preset-Leitfaden
unter `.specify/presets/model-routing-governance/docs/automatic-discovery.md`
beziehungsweise `automatic-discovery.EN.md`. Zielgruppen sind Maintainer,
Lernende aller vier IHK-IT-Berufe und Entwickelnde ohne Spezialwissen.
Deutsch zuerst, gleichwertiges Englisch, CEFR B2 und anwendbare WCAG 2.2 AA;
statische Prüfungen sind keine vollständige A11Y-Abnahme.

Der Auftrag umfasst Release und Installation in Level 0, TinyCalc,
Show-CommandTui400 und absdd-image-sandbox. Nur Model Routing wird von 0.1.7
auf **0.2.3**, Priorität **61**, angehoben. Die anderen 13 Preset-Payloads und
Registry-Einträge bleiben erhalten; insbesondere bleibt eine bereits vorhandene
Autonomous-Version 0.4.8 im Sandbox-Repo bestehen. Andere Flottenziele,
Produktläufe, SDK-/Werkzeuginstallationen und Container-/Imagewechsel sind
nicht Teil dieses Auftrags.

Das Tag-Archiv ist vollständig gegen den geprüften Quellcommit gebunden:

- Tag: `v0.2.3`; Commit: `282a5d7c9df5587fabf4f2164d837a4f1003c8fc`.
- ZIP-SHA-256: `b04afda98c642147bc89fa5f6d11a5e34a8e6b0d47443e223753bba477cd72c6`.
- Archiv: 55 Dateien; 105007 Bytes; alle Git-Blobs entsprechen dem Quellcommit.
- [Veröffentlichung](https://github.com/hindermath/spec-kit-preset-model-routing-governance/releases/tag/v0.2.3).

Die bisherigen Top-Level-Resolver haben Vorrang vor Preset-Pfaden. Deshalb
werden diese Einstiegspunkte samt allen vier Adapter-Ressourcen aus genau
diesem Release übernommen. Vorhandene Pflege-Dateikataloge und Skriptreferenzen
werden um die vollständige Laufzeitabhängigkeit ergänzt. Sonst könnte trotz neuer
Preset-Version weiterhin alter Resolver-Code ausgeführt werden.

Die Installation erzeugt keine persönlichen Modellprofile, führt keinen
Refresh, keine Modellinferenz und keine SDK-Anmeldung aus. Codex-/agy-Verhalten
bleibt erhalten. Die neuen Adapter wählen bestätigte Fähigkeiten vor breiten
Modellpräferenzen; Mehrdeutigkeit bleibt sichtbar und kann mit einer exakten
gemeldeten ID aufgelöst werden. Hersteller-Planmodi sind keine OS-Sandbox und
die Installation erteilt keine formale Sandbox- oder Providerfreigabe.

Claude, Copilot und OpenCode leiten erfolgreiche reine JSON-Standardausgabe
über einen paketgebundenen Adapter an den exakten Ergebnisdateipfad des
autonomen Runners weiter. Lesende Rollen benötigen deshalb keine Dateischreib-
rechte im Harness. Leere, fehlgeschlagene oder unstrukturierte Ausgabe erzeugt
keine Ergebnisdatei und bleibt geschlossen blockiert.

Prüfungen: exakte projektgeführte 14er-Matrix, Release-/Ist-Payload-Bindung,
Erhalt der übrigen Presets, Agentenflächen-Parität, Root-/Preset-Resolver-Parität,
Bash-/PowerShell-Fixtures, vorhandene Skriptkataloge, Secrets und native PR-CI. Die 119
Tests zur breiten Auswahl nutzen ausschließlich synthetische Inventare.
Echte Konten, Quote, Inferenz sowie Produkt-/Plattform-/A11Y-Abnahmen bleiben
getrennte Nachweise. CI-Ergebnisse und Merge-SHAs stehen im zugehörigen PR.

Distributionsklasse: Projektintegration, versionierte Wartungsskripte und
Source-Dokumentation. Für Level 0 betreffen die geänderten Skripte/Gem.-Guidance
auch `homeRuntime`; nach der zentralen Lieferung sind Vorschau und begrenzter
Home-Sync erforderlich. Die Level-2-Installation erteilt keinen Home-Sync-Auftrag
für andere Rechner. Neu bewerten bei Release-, Archiv-, Matrix-, CLI-/SDK-
oder Manifest-Drift. Historische Release-/Installed-Locks bleiben zeitgebundene
Evidence; der aktuelle Installed-Lock wird separat fortgeschrieben.

## English

Documentation Impact: **UpdateRequired**, owner Thorsten Hindermann. Canonical
sources are the published preset, project-specific fourteen-preset matrix and
linked machine-readable installation evidence. Reader path: README → this
record → paired installed preset guides. Audiences include maintainers, all
four IHK IT occupations and non-specialist developers. German first,
equivalent English, B2 and applicable WCAG 2.2 AA; static checks are not full
accessibility acceptance.

The explicit scope is release and installation in Level 0, TinyCalc,
Show-CommandTui400 and absdd-image-sandbox. Only Model Routing changes from
0.1.7 to **0.2.3** at priority **61**. The other thirteen payloads and registry
entries are preserved, including the sandbox's existing Autonomous 0.4.8.
Other fleet targets, product runs, SDK/tool installation and container/image
replacement remain outside scope.

The tag/archive binding above covers all 55 files and the exact source commit.
Top-level resolvers take precedence over installed preset scripts, so their
complete four-resource adapter closure is copied from the same release. The
existing maintenance-file catalogs and script references cover these dependencies.
Installation starts no personal-profile refresh, inference or SDK login.
Codex/agy behavior remains unchanged. New adapters filter confirmed
capabilities before broad model preferences; ambiguity stays explicit and can
be resolved by an exact discovered ID. Vendor plan modes are not OS sandboxes.
No formal sandbox or provider approval is implied.

Claude, Copilot and OpenCode route successful JSON-only standard output through
a package-owned adapter to the autonomous runner's exact result-file path.
Read-only roles therefore need no harness file-write access. Empty, failed or
unstructured output creates no result file and remains fail-closed.

Checks cover the exact project matrix, source/installed payloads, preservation
of unrelated presets, agent surfaces, top-level/preset resolver parity, both
shell fixtures, existing script catalogs, secrets and native PR CI. The 119 broad-selection
assertions use synthetic inventories only. Live accounts, quota, inference and
product/platform/accessibility acceptance remain separate evidence. Actual CI
results and merge SHAs are recorded in the PR.

Distribution: project integration, versioned maintenance scripts and source
documentation. Level-0 script/shared-guidance changes also affect homeRuntime;
preview and bounded Home sync follow central delivery. Level-2 installation
does not authorize Home sync on other computers. Re-evaluate on release,
archive, matrix, CLI/SDK or manifest drift. Historical locks remain temporal
evidence; the current installed-state lock is updated separately.
