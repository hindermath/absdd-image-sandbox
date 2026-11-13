# Projektstatistik / Project Statistics — absdd-image-sandbox

**Stand / Date:** 2026-10-30
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

> **DE:** Lebendiges Dokument — nach jedem abgeschlossenen Feature, jeder
> Spec-Kit-Phase und auf ausdrückliche Anfrage aktualisieren.
>
> **EN:** Living document — update after every completed feature, Spec-Kit
> phase, or on explicit request.

**DE:** Dieses Ledger wurde mit dem Feature „Anfänger-Onboarding für Lernende"
erstmals angelegt. Ältere Arbeit vor diesem Zeitpunkt ist als kumulierter
Basis-Snapshot verdichtet, nicht rückwirkend je Feature aufgeschlüsselt.

**EN:** This ledger was created together with the "beginner onboarding for
learners" feature. Earlier work before that point is condensed into a cumulative
baseline snapshot, not retroactively broken down per feature.

---

## Methodik / Methodology

**DE:** Die Beschleunigungsfaktoren sind ein *blended repository speedup*:
Lieferdichte (Zeilen je sichtbarem Git-Aktivtag) gegen eine manuelle Referenz,
keine Stoppuhrzeit. Dieses Repository ist eine Container-/Infrastruktur- und
Dokumentationsbasis (Dockerfile, Compose, Skripte, `docs/`), kein
C#/.NET-Anwendungscode. Daher gelten hier bewusst die Infrastruktur-Basiswerte
statt der C#/.NET-Standardbasis von 125 Zeilen/Arbeitstag:

**EN:** The acceleration factors are a *blended repository speedup*: delivery
density (lines per visible git active day) against a manual reference, not
stopwatch time. This repository is a container/infrastructure and documentation
base (Dockerfile, Compose, scripts, `docs/`), not C#/.NET application code.
Therefore the infrastructure baselines apply here deliberately instead of the
C#/.NET default of 125 lines/workday:

| Referenz / Reference | Wert / Value | Bedeutung / Meaning |
|---|---:|---|
| Konservativ / Conservative | 80 Z./AT | Vorsichtige manuelle Untergrenze / cautious manual lower bound |
| Thorsten-Solo (Infrastruktur) | 100 Z./AT | Skripting-/Infrastruktur-Referenz / scripting-infrastructure reference |
| TVöD-Arbeitstag / workday | 7,8 h | 21,5 Arbeitstage je Monat / 21.5 workdays per month |

**DE:** „Z./AT" = Zeilen je Arbeitstag. „AT" = Arbeitstag. Die Zeilenzahlen
zählen alle getrackten Dateien; sie sind ein Artefakt-Umfangsmaß, kein
Qualitätsmaß.

**EN:** "Z./AT" = lines per workday. "AT" = workday. Line counts cover all
tracked files; they are an artefact-volume measure, not a quality measure.

---

## Fortschreibungsprotokoll / Update Log

**DE:** Ältester Eintrag oben, neuester Eintrag unten.
**EN:** Oldest entry at top, newest entry at bottom.

| Datum / Date | Phase / Branch | Aktivtage ges. / Active days | Zeilen ges. / Lines | Commits ges. / Commits | Hauptarbeitspakete / Main Work Packages |
|---|---|---:|---:|---:|---|
| 2026-07-10 | docs/lernende-container-onboarding | 36 | 73.081 | 129 | Erst-Erfassung der Statistik. Anfänger-Onboarding: 5 neue Lernenden-Dokumente (`container-grundlagen`, `warum-sandbox`, `installation`, `erste-schritte`, `troubleshooting`), README-Hub-Umbau, Glossar-Erweiterung, Session-Log. Diff +1.136/−74. |
| 2026-07-10 | feat/four-agent-learner-environment | 36 | 73.975 | 132 | Vier Required-Agenten und Syft im Podman-Image; getrennte Agenten-Volumes, Audit-Metadaten, image-interne SBOM, Anfängerpfad mit persönlichem Fork und erstem kontrollierten Agentenlauf, Lychee-/Static-CI. Diff +830/−379. |
| 2026-07-10 | docs/provider-neutral-learner-hosting | 36 | 74.073 | 133 | GitHub-unabhaengiger Lernendenpfad fuer institutionelles GitLab, Codeberg, Forgejo und weitere Git-Systeme; oeffentliche GitHub-Referenzen bleiben Herkunftsnachweis. Agenten-Guidance und Session-Log synchronisiert. Diff +141/−43. |
| 2026-07-15 | docs/home-sync-container-boundary | 40 | — | — | Eingebettete und per Override gemountete Level-0-Referenz als direkte Container-Lesequelle bestaetigt; README und vier Agenten-Dateien stellen klar, dass schreibende `sync-home.*`-Laeufe nach `/home/adedev` gesperrt sind und auf dem Host laufen. Read-only Check-/Vorschaumodi bleiben fuer Diagnosen erhalten; Compose-Mountmodell unveraendert. |
| 2026-09-06 | Assurance-Profil v0.1.2 integriert / Assurance profile v0.1.2 integrated | Arbeitsfenster: eine sichtbare Agentensitzung am 2026-09-06; Branch `codex/assurance-preset-integration`. Nur freigegebene Repository-Integration, keine Produktcode- oder Produkttest-Aenderung. Wiederverwendetes Paket und Dokumentations-/Konfigurationsdelta vor Statistik-Selbstnachweis: +4285 / -0 Zeilen; importiertes Paket ist keine neu entwickelte Produktlogik. Zwoelf bestehende Presets, alte Profile, projektgefuehrte Baseline und menschliche Entscheidungen bleiben unveraendert. Paketbindung, exakte 13er-Matrix, Byte-Erhalt, isolierte Vertrags-/Oberflaechentests und lesender Status sind im Integrationsnachweis dokumentiert; Lieferung folgt per fokussiertem PR mit CI und MergeAndSync. Keine Home-Verteilung oder fachlichen Reviews. Referenzen bleiben im unveraenderten Statistikprofil konfiguriert. / One visible session integrates only the approved repository profile. Imported package content is reuse, not new product logic. Product code/tests and the original twelve presets remain unchanged; see the integration record for tests and boundaries. |
| 2026-09-07 | Assurance-Integration und Evidence-Navigation / Assurance integration and evidence navigation | Branch `codex/assurance-preset-integration`; sichtbare Sitzung 2026-09-07. Paket-, Profil- und Dokumentationsaenderungen: +493 / -38 Textzeilen vor Statistik-Selbstnachweis. Wiederverwendete Paketzeilen sind keine neu entwickelte Produktlogik; vorhandene Nachweise werden nur referenziert. Zwoelf Presets unveraendert, keine fachliche Freigabe, kein Home-Sync. Referenzen: 80 Zeilen/Arbeitstag konservativ, repo-spezifische Thorsten-Solo-Basis laut Profilkonfiguration; Speedup ist Lieferdichte. / One visible session; reused package and evidence-index volume, no new product logic or human approval. Twelve presets preserved; CI/review and MergeAndSync; no Home sync. Manual effort follows the repository statistics configuration. |
| 2026-09-07 | Assurance-Evidence-Vertrag / Assurance evidence contract | Branch `codex/assurance-evidence-migration`, sichtbare Sitzung 2026-09-07. 157 historische Kontrollen quellengebunden abgebildet, vier Gates Blocked, vier menschliche Entscheidungen Open; 4036 neue Evidence-/Dokumentationszeilen vor Ledger und Delivery-Metadaten, 0 neue Produkt-/Testlogikzeilen. Quellen- und Shell-Paritätsprüfung: docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assurance-validation.json. Presets und Altbewertungen unverändert. / Source-bound migration and read-only parity verification; no approval inferred, no Home sync. Manual reference: 80 lines/workday and the repository-specific configuration; speedup is delivery density, not stopwatch time. |
| 2026-09-08 | Assurance-Baseline und Gate-Revalidierung / Assurance baseline and gate revalidation | Branch `codex/assurance-evidence-ready`; sichtbare Sitzung 2026-09-08. Die verwaltete Baseline ist auf 3.2.0 synchronisiert, der fruehere blockierte Gate-Satz auditierbar archiviert und der aktive Evidence-Vertrag fuer Baseline, Delta, Closure und Image Impact in Bash und PowerShell mit Gesamtstatus `Ready` geprueft. Alle 157 fachlichen GSDB-Kontrollen und die menschlichen Freigaben bleiben `Open`; keine C5-, Konformitaets-, Betriebs- oder Risikoakzeptanz wird behauptet. Umfang vor Statistik- und Session-Log-Metadaten: `+2881 / -2270` Dokumentations-, Governance- und Evidence-Zeilen, `0` Produkt- und `0` Testcode-Zeilen. Dreizehn Presets bleiben unveraendert; keine Dockerfile-, Compose-, Image-, Netzwerk-, Secret- oder Home-Sync-Aenderung. / Synchronize baseline 3.2.0, archive the superseded blocked gate set, and validate the technical contract as `Ready` while all 157 GSDB controls and human approvals remain `Open`. No image, runtime, C5, conformity, or Home-sync claim; manual references remain defined by the repository statistics configuration. |
| 2026-09-08 | Assurance-v0.1.3-Feldtest abgeschlossen / Assurance v0.1.3 field test completed | Branch `codex/assurance-v013-field-test-closeout`; eine sichtbare Agentensitzung. Das unveraenderliche Preset-Paket wurde im exakten 13-Preset-Profil unter Bash und PowerShell, mit Vertrags-, Negativ-, Zeilenendungs-, BOM-, Oberflaechen-, Kompositions- und Read-only-Pruefungen validiert. Alle vier aktiven Gates und der Gesamtstatus sind `Ready`; `technicalValidation` ist `Fulfilled`. C5, CRA und formale Produktkonformitaet sind im aktuellen nichtkommerziellen Ausbildungs- und Beispielscope `N/A`; die technische Wiedervorlage ist `2027-09-08`, die regulatorische Scope-Wiedervorlage `2026-12-31`. Die Empfehlung `ReleaseAccepted` gilt nur fuer Preset v0.1.3; Pilotfreigabe, Projektabnahme und allgemeine Freigabe bleiben `Open`. Evidence-Umfang vor Statistik-Selbstnachweis: `+287 / -53` Dokumentations-, Governance- und Evidence-Zeilen, `0` Produkt-, Image- und Testcode-Zeilen. Keine Dockerfile-, Compose-, Runtime-, Paket-, Mount-, Netzwerk-, Secret- oder Home-Sync-Aenderung. / The immutable preset package passed the exact 13-preset profile and the complete cross-shell evidence suite. ReleaseAccepted applies only to preset v0.1.3; human approvals remain Open. No image, runtime, or Home-sync change. |

---

| 2026-09-13 | Intake-Lifecycle-Preset-Rollout / Intake lifecycle preset rollout | N/A | N/A | N/A | Vorhandene Authoring-/Review-/Sequencing-Presets auf 0.3.2/0.2.2/0.2.4 aktualisiert; optionale Profile und Dokumentation nachgefuehrt. Pruefnachweise in docs/maintenance/intake-lifecycle-fleet-rollout.json. / Update existing presets and profile references; preserve other presets and project extensions. |
| 2026-09-13 | Mermaid und Abschlussberichte | N/A | N/A | N/A | Neue textbasierte Diagrammregel, Berichtsvorlage, Agent-Paritaet und versionierte Governance; kein Produktcode. / Text-first diagram and completion-report governance; no product code. |

| 2026-09-14 | codex/sandbox-spec-kit-0128 | N/A | N/A | N/A | UpdateRequired: Spec Kit 0.12.8 auf Release-Commit gepinnt; vorhandenen Bind-Mount-Patch an modularisierte CLI angepasst; drei Regressionstests und lokale/CI-Einbindung. Image- und Laufzeitnachweise in docs/maintenance/spec-kit-0128-upgrade.md. Lieferung und Statistik-Rendering folgen erst nach menschlicher Diff-Pruefung. / Pinned CLI upgrade and compatibility tests; delivery and statistics rendering await human diff review. |

| 2026-09-14 | Statistik-Pilotinstallation / Statistics pilot installation | N/A | N/A | N/A | UpdateRequired: v0.1.0 als adedev im vorhandenen 0.12.8-Pilotcontainer installiert; 26 Paketdateien hashgleich, 15 generierte Command-Dateien, 13 alte Presets erhalten. Beide CheckOnly-Einstiege und Lifecycle-Fixtures bestanden. Keine Image-/Produktlogik geaendert; keine Messung, Freigabe oder Community-Einreichung. Menschliche Diff-Sichtung vor Commit/Push und danach Inhaltscommit/Statistik-Rendering bleiben offen. Nachweis: docs/maintenance/project-statistics-installation-v010.md. / Local non-root installation verified; no image build, human approval or remote delivery claimed. |

| 2026-09-18 | Statistik-Pilot Zwischenmessung / Statistics pilot intermediate measurement | UTC 70 / Berlin 73 | 233454 | N/A | Nach Sichtung den ersten Fuenf-Dateien-Patch als 9f07e67 committet; reale getrennte Messung, 67 Fixture-Assertions, Shell-/Encoding-/Read-only-Pruefungen bestanden. Profil 2 aus sauberer Kopie derselben Revision fortgeschrieben. Neue Evidence und Session noch uncommittet; finaler Nachlauf nach gesichtetem Inhaltscommit erforderlich. Keine Fach-/Releasefreigabe, kein Push oder Merge. / Reviewed first content commit and reproducible intermediate evidence; final post-review refresh and acceptance remain open. |
| 2026-09-18 | Gesichteter Statistik-Nachlauf / Reviewed statistics refresh | UTC 70 / Berlin 73 | 233614 | N/A | Sechs gesichtete Dateien als 291d50e committet; beide Statistiken auf dieser sauberen Revision aktualisiert. Eine Datei und 160 Zeilen hinzugekommen. Shell-Status, 67 Assertions und isolierter Installationszyklus bestanden. Neue Sichtung vor weiterer Lieferung erforderlich. / Reviewed evidence committed; both statistics refreshed from the clean revision, adding one file and 160 lines. New review and remote delivery remain open. |
| 2026-09-20 | codex/update-sandbox-baseline-reference | N/A | N/A | N/A | UpdateRequired: exakter Home-Baseline-Commit-Pin mit Schema-1-Kompatibilitaet, acht Pin-/Dokumentationstests auf macOS und Linux sowie drei Preflight-Fixtures bestanden. Image gebaut und ohne Netzwerk mit neun Werkzeugpruefungen validiert. Wiederanlauf-/SBOM-Evidence im Sitzungsprotokoll 2026-09-20-0118-baseline-image-update.md; kein neuer Spec-Kit-Lauf. / Exact commit pin, compatibility and native/container tests; lifecycle evidence in the session log, no Spec Kit run. |
| 2026-09-20 | codex/pin-container-maintenance-delegation | N/A | N/A | N/A | UpdateRequired: gemergtes Level-0-Delegationspaket 110ac82e gepinnt; neun Pin-/Dokumentationstests, Pre-commit und 22 netzwerklose Image-Tests bestanden. Finale SBOM: 28.970 Komponenten. Service erneuert, 20 Mounts und sechs Volumes identisch; Evidence im Sitzungsprotokoll 2026-09-20-0910-container-delegation.md. Kein Spec-Kit-Lauf. / Pin merged Level-0 delegation, verify tests and image inventory, preserve mounts and volumes; no Spec Kit run. |

| 2026-09-20 | codex/maintenance-closeout-image-pin | N/A | N/A | N/A | UpdateRequired: finalen Wartungskorrektur-Commit 586c142 einschliesslich Consumer-Testgrenze und erzeugter Referenz gepinnt; neun Pin-/Dokumentationstests, Pre-commit, 22 zentrale Delegations- und 23 Wrapper-Tests im finalen Image bestanden. Hashbindung und Schreibschutz geprueft, SBOM mit 28.970 Komponenten erstellt. Aktivierung und abschliessender Flottenlauf folgen nach technischer PR-Abnahme; Details im Sitzungsprotokoll 2026-09-20-1055-maintenance-closeout.md. / Pin final maintenance corrections including consumer discovery, verify image tests and inventory; activation and fleet closeout remain separate evidence. |
| 2026-10-06 | macOS-15 CI runner migration | — | — | — | CI-Matrizen und gemeinsame Guidance auf macOS 15 umgestellt; Linux-/Windows-Auswahl erhalten, Required-Check-Migration und exakte PR-CI als Liefergates. / Migrated CI labels and guidance; preserved other platforms and required exact-head CI proof. |
| 2026-11-03 | Model Routing Governance 0.2.1 | N/A | N/A | N/A | UpdateRequired: hashgebundenes Release, ein Preset aktualisiert, andere 13 erhalten; vollständige Resolver-Ressourcen und Root-/Preset-Parität geprüft. Keine Modellaufrufe oder Profilmigration. / Hash-bound release, one preset updated, other 13 preserved; complete runtime closure and root/preset parity verified. No inference or profile migration. [Evidence](maintenance/model-routing-v021-installation.md). |
| 2026-11-03 | Model Routing Governance 0.2.3 | N/A | N/A | N/A | UpdateRequired: hashgebundenes Release mit strukturiertem Harness-Rückkanal und kanonischem Adapterpfad, ein Preset aktualisiert, andere 13 erhalten; vollständige Resolver-Ressourcen und Root-/Preset-Parität geprüft. Keine Modellaufrufe oder Profilmigration. / Hash-bound release with structured harness result transport and canonical adapter path, one preset updated, other 13 preserved; complete runtime closure and root/preset parity verified. No inference or profile migration. [Evidence](maintenance/model-routing-v023-installation.md). |
| 2026-11-05 | Model Routing 0.2.6 und Autonomous Run 0.4.10 | N/A | N/A | N/A | UpdateRequired: zwei hashgebundene Presets installiert, andere zwölf erhalten; Matrix, Payloads und lokale Verträge grün. Keine Modellaufrufe oder Profilmigration. / Two hash-bound presets installed, other twelve preserved; matrix, payload and local contracts passed. No model calls or profile migration. [Evidence](maintenance/model-routing-v026-installation.md). |

## Gesamtstand des Repositories / Repository Snapshot

**DE:** Stand: 2026-07-10. Dieses Repository enthält keinen klassischen
Produktionscode und kein Testframework; der Schwerpunkt liegt auf
Dokumentation, Konfiguration und Skripten.

**EN:** As of 2026-07-10. This repository contains no classic production code and
no test framework; the focus is documentation, configuration, and scripts.

| Kategorie / Category | Dateien / Files | Zeilen / Lines | Anteil / Share |
|---|---:|---:|---:|
| Dokumentation (.md) / Documentation | 349 | 60.071 | 81,1 % |
| Sonstige / Other (LICENSE, man, dotfiles) | 24 | 5.471 | 7,4 % |
| Konfiguration / Configuration | 47 | 4.242 | 5,7 % |
| Skripte / Scripts (.sh, .ps1) | 26 | 4.289 | 5,8 % |
| **Gesamt / Total** | **446** | **74.073** | **100 %** |

---

## Statistikprofil-1-Archiv / Statistics Profile 1 Archive
| Kennzahl / Metric | Verdichteter Gesamtblick / Condensed Overview |
|---|---:|
| Artefaktbasis gesamt / Total artefact base | 446 Dateien / 74.073 Zeilen |
| Beobachtbarer Projektzeitraum / Observable period | 2026-04-29 – 2026-07-10 |
| Sichtbare Git-Aktivtage / Visible git active days | 36 |
| Commits gesamt / Total commits | 133 |
| Manuelle Äquivalenz (80 Z./AT) / Manual equiv. | ~925,9 AT (~7.222,1 h) |
| Manuelle Äquivalenz (100 Z./AT) / Manual equiv. | ~740,7 AT (~5.777,7 h) |
| Repo-weiter Speedup gg. 80-Zeilen-Referenz | ~25,7x |
| Repo-weiter Speedup gg. Thorsten-Referenz (100) | ~20,6x |

### Artefaktmix / Artefact Mix

```text
Doku (.md)      | ############################################  60071  (81%)
Sonstige/Other  | ####                                           5471  ( 7%)
Konfiguration   | ###                                            4242  ( 6%)
Skripte         | ###                                            4289  ( 6%)
```

**DE:** Das Diagramm zeigt, wie sich die Zeilen auf die Kategorien verteilen.
Über 80 % sind Dokumentation — passend zu einem öffentlichen Referenz- und
Ausbildungs-Repository.

**EN:** The diagram shows how the lines split across categories. More than 80 %
is documentation — fitting for a public reference and training repository.

### Phasenvolumen: Commits je Monat / Phase Volume: Commits per Month

```text
2026-04 | #                                         1
2026-05 | #######################################  87
2026-06 | ############                             27
2026-07 | #######                                  17
```

**DE:** Feste X-Slots je Monat. Der Aufbau-Schwerpunkt lag im Mai 2026 (87
Commits an 22 Aktivtagen); danach folgen kleinere Pflege- und Feature-Wellen.

**EN:** Fixed X slots per month. The build-up peak was May 2026 (87 commits on
22 active days); smaller maintenance and feature waves followed.

### Aufwandsvergleich repo-weit / Repo-Wide Effort Comparison

```text
Erfahren / 80 Z./AT   | ##########################################  926 AT
Thorsten-Solo / 100   | ##################################         741 AT
KI-sichtbar (real)    | ##                                          36 AT
```

**DE:** Der Balken vergleicht drei Sichtweisen auf denselben Umfang (74.073
Zeilen): erfahrene manuelle Referenz (80 Z./AT), Thorsten-Solo-Infrastruktur
(100 Z./AT) und die real sichtbaren Git-Aktivtage. Es ist ein Lieferdichte-
Vergleich, keine gemessene Arbeitszeit.

**EN:** The bars compare three views of the same volume (73,975 lines):
experienced manual reference (80 l/wd), Thorsten-Solo infrastructure (100 l/wd),
and the actually visible git active days. It is a delivery-density comparison,
not measured working time.

### Beschleunigungsfaktoren / Acceleration Factors

```text
gg. 80 Z./AT (konservativ)  | ##########################  25.7x
gg. 100 Z./AT (Thorsten)    | #####################       20.6x
```

**DE:** Der repo-weite Speedup ergibt sich aus manueller Äquivalenz geteilt
durch sichtbare Aktivtage. Höhere Werte bedeuten mehr Artefaktvolumen je
sichtbarem Tag, nicht automatisch höhere Qualität.

**EN:** The repo-wide speedup is manual equivalent divided by visible active
days. Higher values mean more artefact volume per visible day, not automatically
higher quality.

### Feature-Fokus: Anfänger-Onboarding / Feature Focus: Beginner Onboarding

```text
Erfahren / 80 Z./AT   | ##############  14.2 AT
Thorsten-Solo / 100   | ###########     11.4 AT
KI-sichtbar (real)    | #                1.0 AT
```

**DE:** Das aktuelle Feature lieferte 1.136 hinzugefügte Zeilen (netto +1.062)
über 8 Dateien an einem sichtbaren Aktivtag. Manuell entspräche das grob 14
Arbeitstagen (80 Z./AT) bzw. 11 Arbeitstagen (100 Z./AT).

**EN:** The current feature delivered 1,136 added lines (net +1,062) across 8
files on one visible active day. Manually this would roughly equal 14 workdays
(80 l/wd) or 11 workdays (100 l/wd).

### 2026-09-20 - Prozessgebundenes Wartungsvertrauen / Process-scoped maintenance trust

Home-Baseline-Pin auf `4459e744d126d51b832986b09ac1a73cf88c1607` für
exakte Git-Freigaben je Wartungsprozess aktualisiert. Keine neue globale
Git-Konfiguration, keine neuen Mounts oder Volumes. Documentation Impact:
UpdateRequired; Wartungsnavigation und Sitzungsnachweis aktualisiert.
Image-Build, SBOM und Aktivierung werden separat im Liefer-PR belegt.

Updated the Home Baseline pin for exact process-scoped maintenance Git trust.
No new global Git configuration, mounts or volumes. Documentation Impact:
UpdateRequired; maintenance navigation and session evidence updated. Record
image build, SBOM and activation separately in the delivery PR.

### 2026-09-20 - Portable Vertrauensfixture / Portable trust fixture

Image-Pin um die native Windows-Testfixture aus Level 0 ergänzt;
Wartungslogik unverändert. Documentation Impact: UpdateRequired;
Freigabeinventar und Sitzungsnachweis auf denselben Pin nachgeführt.

Updated the image pin for the native Windows test fixture; maintenance logic
is unchanged. Documentation Impact: UpdateRequired; approval inventory and
session evidence aligned to the same pin.

| 2026-10-10 | Fuenf Governance-Updates / Five governance updates | UpdateRequired: Security 0.7.1, Architecture 0.6.2 und Intake Authoring 0.3.7 / Review 0.2.4 / Sequencing 0.2.8 mit unveraenderlichen ZIP-Hashes, zentraler 14er-Matrix und aktuellen Guidance-Versionen. Neun andere Pakete, Prioritaeten, historische Evidence und menschliche Freigaben erhalten. Statistik-Nachlauf nach freigegebenem Quell-Commit; Methodik unveraendert. / Bounded integration, no product run or approval promotion; statistics follow the authorized source commit. [Nachweis / Evidence](maintenance/preset-alignment-2026-10-10.md). |

| 2026-10-18 | Vierzehn README-Patch-Pakete / Fourteen README patch packages | Begrenzte Integration aus Home Baseline #335 mit unveraenderlichen Quellenbindungen, kompletter Agentenkomposition und getrennten technischen Assurance-Gates. Keine Image-/Provider-/Netzwerkaenderung, Produkt- oder Zertifizierungsfreigabe. Statistik-Nachlauf erst nach gesichtetem Quell-Commit; Methodik bleibt unveraendert. / Bounded installation; generated measurement follows the approved clean source commit. [Nachweis / Evidence](maintenance/preset-readme-patch-rollout-2026-10-18.md). |

### 2026-10-20 - GSDB 3.4.4 / Assurance 0.1.5 Pilot

DE: Manifestgebundene GSDB-Übernahme aus Level 0 d9898356, 157 IDs erhalten;
Assurance 0.1.5 gezielt integriert, andere 13 Pakete und historische Evidence erhalten.
[Nachweis / Evidence](maintenance/gsdb-344-pilot-2026-10-20.md).
EN: Bounded source/preset adoption and new project evidence; no product or fleet acceptance.

### 2026-10-24 - Vierzehn stabile Preset-Patches / Fourteen stable preset patches

DE: Begrenzter Sandbox-Installationskandidat mit unveraenderten Prioritaeten,
native Agentenkomposition und neuer technischer Assurance-Delta-Kontext.
Keine Produkt-, Home-, Image- oder weitere Flottenaenderung. Lieferung erst
nach konkreter Diff-Sichtung und bestandenen Checks; keine KI-Zeitmessung.
EN: Bounded installation candidate, native command composition and separate
technical assurance evidence. No product, Home, image or wider fleet changes.
Delivery awaits explicit patch sighting and successful checks; no AI-time claim.

### 2026-10-30 - Sandbox-Intake-Serie und IR801 / Sandbox intake series and IR801

DE: Feature-Update als fünftes Ziel nach Hardening und vor Selbstprüfung
aufgenommen. IR801-Vertrag ergänzt finale H/U-Baseline, unabhängige Prüfungen
und keine Selbstabnahme. Vollständiges Nachreview Ready, null offene Findings;
fünf Ziele, eine archivierte Root, fünf bindende Kanten. Provenienz und
historische Vorstände erhalten. Keine Feature-Implementierung, Runtime-,
Home- oder Flottenänderung; Feature 004 bleibt ein gesonderter Arbeitsstand.
EN: Admit the feature update as the fifth target after hardening and before
acceptance. IR801 binds the final H/U baseline, independent checks and no
self-acceptance. Complete re-review Ready with no open findings; five targets,
one archived root and five binding edges. Preserve provenance and history.
No feature implementation, runtime, Home or fleet change; Feature 004 remains
a separate work context.

### 2026-10-30 - Kanonischer EOF-Fix / Canonical EOF fix

DE: Autonomous v0.4.8 aus dem veröffentlichten eigenständigen Preset mit
exaktem Tag-/ZIP-Nachweis lokal integriert. Die übrigen 13 Payloads bleiben
unverändert. Aktive Profile/Locks und zwei Constitution-Pins aktualisiert;
26 zusätzliche Vorstände bytegleich archiviert, vier aktive Receipts erneuert
und vollständiges Serienreview Ready. Historische EOF-Bytes werden nur über
exakte Rohhash-Ausnahmen erhalten, aktive U-Datei formatneutral normalisiert.
Keine Feature-004-Implementierung, globale Profilverteilung oder Runtimeaktion.
EN: Integrate published standalone Autonomous v0.4.8 with exact tag/ZIP proof,
preserving thirteen other payloads. Renew local profiles/locks, paired pins,
four receipts and complete Ready series review; preserve 26 preimages.
Historical EOF allowances bind exact raw bytes; normalize the active update
without semantic change. No Feature 004 execution, global rollout or runtime action.

### 2026-11-03 - Dependabot-Wartung / Dependabot maintenance

DE: Branch `codex/dependabot-maintenance-20261103`, Arbeitsfenster 2026-11-03.
Repository-spezifische Versions-/Sicherheitsgruppen und zweisprachige
Wartungshinweise ergaenzt. Kein Produktions- oder Testcode geaendert;
Konfigurations-/Dokumentationsumfang ist im PR-Diff belegt. Profil 2 wird
aus der committed Inhaltsrevision gerendert; bestehende Referenzen bleiben.
YAML/Schema, Manifestabdeckung, Policy, Dokumentation, Liefermenge und
Secret-Scan bestanden. Hosted-Checks werden am PR verfolgt. Keine Pakete
aktualisiert; Git-basierte Statistik misst keine KI-Zeitersparnis.

EN: Branch `codex/dependabot-maintenance-20261103`, work window 2026-11-03.
Adds repository-specific version/security groups and bilingual maintenance
guidance. No production or test code changed; the PR diff records the exact
configuration/documentation scope. Profile 2 is rendered from the committed
content revision with existing references. YAML/schema, manifest coverage,
policy, documentation, delivery scope and secret scan passed. Hosted checks
are tracked on the PR. No packages updated; Git statistics do not measure
AI time savings.

### 2026-11-03 - Verifizierte Pin-Updates / Verified pin updates

DE: Renovate durch Dependabot fuer den Basisimage-Digest und einen eigenen
PowerShell-7-Pin-Workflow ersetzt. Alle 29 ARGs besitzen Quellenabdeckung;
Architektur-Hashes werden gemeinsam mit Versionen vorgeschlagen. Podman-
Build, Smokes und SBOM sind Gates vor kuenftigen Update-PRs. 81 Offline-
Assertions und bestehende Pin-/Hardening-Pruefungen sichern Grenzen und
negative Faelle ab. Der read-only Herstellerabgleich ist Ready; Swift bleibt
bis zur koordinierten Level-0-Registry-Pflege zurueckgehalten. Keine Paket-
Upgrades und kein laufender Containerwechsel in dieser Einrichtung.

EN: Replaces Renovate with Dependabot for the base digest and a PowerShell7
pin workflow. All29 ARGs have explicit sources; versions and architecture
hashes move together. Podman build, smokes and SBOM gate future update PRs.
81 offline assertions and existing pin/hardening checks cover boundaries and
negative cases. Read-only upstream discovery is Ready; Swift remains held
pending coordinated Level-0 registry maintenance. This setup performs no
package upgrade or running-container switch.

## Image-Refresh vom 05.11.2026 / Image refresh

Der separate ARM64-Kandidat enthaelt Model Routing 0.2.6 und Autonomous Run
0.4.10. Build, SBOM, isolierter Runtime-Sync, 48 Routing-Assertions und der
vollstaendige Toolchain-Smoke sind erfolgreich; der bestehende Container wurde
nicht ersetzt. Nachweis: [Image-Refresh](maintenance/image-refresh-routing-v026.md).
Documentation Impact: `GeneratedUpdate` fuer den folgenden Statistikblock;
kanonische Quelle sind die Git-Historie und `docs/project-statistics.config.json`.

The separate ARM64 candidate passed build, SBOM generation, isolated runtime
sync, routing assertions and full toolchain smoke. The existing container is
preserved. Git history and the statistics configuration generate the block below.

## Bundle-Transport-Image-Pin vom 08.11.2026 / Bundle transport image pin

Die unveraenderliche Home-Baseline-Referenz pinnt den gelieferten Bundle-
Transport auf `b232d5881f1d75092ddd9ecb345d210b4213732a`. Nach einem
Speicherabbruch und separat genehmigter Bereinigung bestanden nativer ARM64-
Build, CycloneDX-SBOM, Non-root-/Paketnachweis und der isolierte vollstaendige
Toolchain-/Dokumentations-Smoke. Die konkrete Owner-Freigabe bleibt ausstehend;
Bestandscontainer und sechs Volumes sind erhalten. Kein Home-Sync und kein
21-Repo-Wartungslauf. Nachweis: [Sitzungsprotokoll](security/agent-session-log/2026-11-08-1726.md).
Documentation Impact: `UpdateRequired`; der Profil-2-Nachlauf ist `GeneratedUpdate`.

The immutable Home Baseline reference embeds the delivered bundle transport.
After the initial storage failure and separately authorized cleanup, native
ARM64 build, SBOM, immutable package proof and isolated full smoke passed.
Concrete owner approval remains pending; the old container and six volumes
are preserved. No Home sync or 21-repository maintenance was performed.

### 2026-11-09 - OpenCode-Pin-PR #129 / OpenCode pin PR #129

DE: Vorhandenen Vorschlag fuer OpenCode 2.2.6 gegen Herstellerquelle und
npm-Metadaten geprueft; main-Historie integriert und den reinen Statistik-
Konflikt zur Neugenerierung aufgeloest. Sitzungsnachweis: agent-session-log
2026-11-09-pr129-pin-review.md. NoUpdateRequired fuer bestehende Anleitungen,
GeneratedUpdate fuer Profil 2; Source-only, kein Home-Sync. Exakte gruene
PR-Checks bleiben Merge-Gate. Native ARM64- und Runtime-Abnahme bleiben separat.
EN: Reviewed the existing OpenCode 2.2.6 proposal against official release and
npm metadata; integrated main history and resolved generated statistics for
regeneration. Session evidence: agent-session-log 2026-11-09-pr129-pin-review.md.
NoUpdateRequired for reader guidance, GeneratedUpdate for Profile 2;
source-only, no Home sync. Exact green PR checks remain the merge gate.
Native ARM64 and runtime acceptance remain separate.

### 2026-11-10 - Statistik-Drift nach Datumswechsel / Statistics date rollover

DE: Profil 2 nach dem Merge von PR #131 am 10.11.2026 aus committierten
Quellen neu erzeugt. Der Stand vom 09.11. war durch den Datumswechsel
veraltet; Konfiguration und Methodik bleiben erhalten. GeneratedUpdate;
Owner: Repository-Maintainer; Source-only, kein Home-Sync. Lokale Vorschau
und Driftkontrolle sowie exakte Head-Checks bilden den technischen Nachweis.
EN: Regenerated Profile 2 from committed sources after PR #131 merged on
10 November 2026. The previous day's snapshot became stale at date rollover;
retain configuration and methodology. GeneratedUpdate; repository-maintainer
owner; source-only, no Home sync. Preview, drift validation and exact-head
checks provide technical evidence.

### 2026-11-12 - Intake Sequencing Governance v0.2.13

DE: Ausschliesslich Intake Sequencing Governance auf das gepruefte
Dokumentationspatch 0.2.13 aktualisiert. Die anderen 13 Presets und alle
Runtime-Vertraege bleiben erhalten. Matrizen und Hash-Locks fortgeschrieben;
Nachweis: [Rollout](maintenance/intake-sequencing-v0213-rollout-2026-11-12.md).
Documentation Impact: UpdateRequired; Statistikblock: GeneratedUpdate.
Owner: Thorsten Hindermann. Git-Aktivitaet ist keine Stoppuhrmessung.

EN: Updated only Intake Sequencing Governance to documentation patch 0.2.13,
retaining the other thirteen packages and runtime contracts. Updated matrices
and source/installed bindings; see the linked rollout record. Statistics are
generated from the existing methodology, not measured working time.

### 2026-11-12 — Sicherheitsrichtlinie / Security policy

DE: Genehmigte Sicherheitsrichtlinie DE zuerst/EN danach auf CEFR-B2-Niveau
harmonisiert, projektspezifische Grenzen und bestehende Reaktionsziele erhalten.
Private Advisory-Links und Sprach-/Überschriftenstruktur geprüft.
Documentation Impact: UpdateRequired; Nachweis unter
`docs/documentation-impact/security-policy-2026-11-12.json`.
Keine Produktlogik geändert; CodeQL unter Tools wird nach Lieferung separat
eingerichtet. Keine AI-Scan-Aktivierung oder neue praktische A11Y-Abnahme.

EN: Harmonised the approved German-first/English-second security policy at
CEFR B2, preserving project boundaries and existing response targets. Checked
private advisory links, language boundaries and heading structure.
Documentation Impact: UpdateRequired; see the evidence path above.
No product logic changed; CodeQL under Tools is configured separately after
delivery. No AI Scan activation or new practical accessibility acceptance.

### 2026-11-13 — Gemeinsame Preset-Sicherheitswartung / Shared preset security maintenance

Vierzehn veroeffentlichte Patch-Releases sind ueber echte Quellen- und Installationsbindungen uebernommen. Gemeinsame Workflow-Rechte sind explizit begrenzt; Produktlogik und Lifecycle bleiben unveraendert. Offene CodeQL-Belegluecken bleiben offen, ohne automatische Alert-Verwerfung.

Fourteen published patches are recorded through real source and installed bindings. Shared workflow permissions are explicitly restricted; product logic and lifecycle remain unchanged. Open CodeQL evidence gaps remain open without automatic alert dismissal.

Documentation Impact: UpdateRequired; [Wartungsnachweis / maintenance evidence](maintenance/shared-security-rollout-2026-11-13.md).

### 2026-11-13 — Intake Authoring 0.3.14 / Intake-Authoring-Folgekorrektur

DE: Die geprüfte Patch-Version 0.3.14 ergänzt den Sicherheitsrollout; Quellen- und Installationsbindungen sowie kompatible Nachweise bleiben getrennt nachvollziehbar. Keine neue Produktfunktion oder menschliche Sicherheitsabnahme.

EN: Verified patch 0.3.14 supplements the security rollout; source, installation and compatible evidence remain separately traceable. No new product feature or human security acceptance.

Documentation Impact: UpdateRequired; [Nachweis / evidence](maintenance/shared-security-rollout-2026-11-13.md).

### 2026-11-13 — npm-Agent-Proben begrenzt / Bound npm agent probes

DE: Die verteilten Wartungsskripte begrenzen npm-Agent-Proben vor der Ausfuehrung. TinyPl0 behaelt seine ausdrueckliche Freigabe fuer alternative Registries. Es wird kein Spec-Kit-Lauf hinzugezaehlt.

EN: Distributed maintenance scripts bound npm agent probes before execution. TinyPl0 retains its explicit opt-in for alternate registries. No Spec Kit run is added.

Documentation Impact: UpdateRequired; [Nachweis / evidence](maintenance/shared-security-rollout-2026-11-13.md).

### 2026-11-13 — Nativer CI-Vertrag / Native CI contract

DE: Der Ereignisstrom-Test prueft die vorhandenen Callback- und Ergebnis-Signale ohne ein hier nicht vorhandenes Level-0-Feld. Kein neuer Spec-Kit-Lauf.

EN: The event-stream test checks the existing callback and result signals without a Level-0-only field. No new Spec Kit run.

Documentation Impact: UpdateRequired; [Nachweis / evidence](maintenance/shared-security-rollout-2026-11-13.md).

### 2026-11-13 — Projektgebundene Wartung erhalten / Preserved project maintenance

DE: Die Sandbox behält ihre schreibfreie Registry-Vorschau und ihren Snapshot-Vertrag. npm-/CLI-Proben sind nun codegebunden; Swiftly-Archive sind größenbegrenzt. Gemeinsame MSL-Modultests bleiben aktiv, nicht vorhandene Elternadapterfälle werden ausdrücklich ausgenommen. Kein Spec-Kit-Lauf wird ergänzt.

EN: The sandbox retains its read-only registry preview and snapshot contract. npm and CLI probes are now code-bound; Swiftly archives have size limits. Shared MSL module tests remain active, and absent parent-adapter cases are explicitly excluded. No Spec Kit run is added.

Documentation Impact: UpdateRequired; [Nachweis / evidence](maintenance/shared-security-rollout-2026-11-13.md).

## Gesamtstatistik / Overall Statistics

<!-- project-statistics-v2:begin -->

Profil 2 verwendet Git-getrackte Textdateien und sichtbare Git-Aktivitaet. Die Werte beschreiben Lieferdichte, keine persoenliche Arbeitszeit.

*Profile 2 uses Git-tracked text files and visible Git activity. The values describe delivery density, not personal working time.*

| Kennzahl / Metric | Wert / Value |
|---|---:|
| Textbasis / Text base | 584834 lines |
| Textdateien / Text files | 2696 |
| Beobachtbarer Zeitraum / Observable period | 2025-11-16..2026-11-13 |
| Aktivtage / Active days | 98 |
| Relevante Commits / Relevant commits | 353 |
| Zeilen je Aktivtag / Lines per active day | 5967.7 |
| Peak-Tag im Fenster / Peak day in window | 2026-10-25 / 101840 |
| Peak-Woche im Fenster / Peak week in window | 2026-10-25 / 266277 |
| Laengste Serie / Longest streak | 8 days |
| Speedup vs. 80 lines/day | 74.6x |
| Speedup vs. 100 lines/day | 59.7x |
| Methodik / Methodology | v2; source `23ec4230c0c1` |

### Artefaktmix / Artifact Mix

```text
Produktiv / Production          [#...................]   0.0% | 97
Tests                           [#...................]   3.1% | 18226
Dokumentation / Documentation   [############........]  61.5% | 359939
Skripte / Scripts               [##..................]   7.8% | 45648
Konfiguration / Configuration   [####................]  18.9% | 110261
Daten und Medien / Data and media [....................]   0.0% | 0
Sonstiger Text / Other text     [##..................]   8.7% | 50663
```

Die Balken teilen die aktuelle getrackte Textbasis in stabile Kategorien. Prozent und Zeilenwert sind die genaue, textorientierte Aussage.

*The bars split the current tracked text base into stable categories. Percentages and line counts provide the exact text-first result.*

### Tagesaktivitaet / Daily Activity

```text
Wochen / Weeks 01..26 | 2025-11-16..2026-05-16
So/Su  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0
Mo/Mo  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 3
Di/Tu  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 3
Mi/We  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 3 0
Do/Th  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 3
Fr/Fr  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4 0 2
Sa/Sa  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0
```

```text
Wochen / Weeks 27..52 | 2026-05-17..2026-11-14
So/Su  3 2 1 0 4 0 0 4 2 4 4 1 4 4 0 4 4 4 4 0 3 0 0 4 0 4
Mo/Mo  0 3 2 0 0 0 0 0 4 4 0 0 0 2 0 0 4 2 0 0 0 0 4 0 4 3
Di/Tu  3 2 3 0 0 0 0 0 3 4 4 0 0 0 0 0 4 4 0 0 4 0 4 4 4 2
Mi/We  0 2 4 0 0 0 0 2 1 2 4 0 0 2 0 0 0 0 0 0 0 0 4 0 0 0
Do/Th  3 0 4 3 0 0 0 0 1 3 0 0 4 0 0 0 0 0 0 0 0 0 0 2 4 3
Fr/Fr  1 3 0 0 0 2 4 4 4 4 1 0 4 0 0 3 0 3 0 0 0 0 0 4 3 4
Sa/Sa  2 0 0 0 2 0 4 4 0 4 2 0 2 0 0 0 4 1 3 0 4 0 4 4 3 -
```

DE: 0 = keine Aenderung; 1 = 1..79; 2 = 80..399; 3 = 400..1599; 4 = 1600+ geaenderte Textzeilen; - = noch nicht abgelaufen.

*EN: 0 = no change; 1 = 1..79; 2 = 80..399; 3 = 400..1599; 4 = 1600+ changed text lines; - = not elapsed.*

### Wochenvolumen / Weekly Volume

```text
Wochen / Weeks 01..26 | 2025-11-16..2026-05-16
    cap 5000 | . . . . . . . . . . . . . . . . . . . . . . . . . .
        4167 | . . . . . . . . . . . . . . . . . . . . . . . . . .
        3333 | . . . . . . . . . . . . . . . . . . . . . . . . . .
        2500 | . . . . . . . . . . . . . . . . . . . . . . . . . #
        1667 | . . . . . . . . . . . . . . . . . . . . . . . # . #
         833 | . . . . . . . . . . . . . . . . . . . . . . . # # #
           0 +-----------------------------------------------------
```

```text
Wochen / Weeks 27..52 | 2026-05-17..2026-11-14
  cap 500000 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      416667 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      333333 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      250000 | . . . . . . . . . . . . . . . . . . . . . . . # . .
      166667 | . . . . . . . . . . . . . . . . . . . . . . . # . .
       83333 | . . . . . . . . . . . . . . . . . . . . . . . # . .
           0 +-----------------------------------------------------
```

Das Wochenvolumen zeigt Additionen plus Loeschungen. Es ist Aenderungsaktivitaet, nicht die aktuelle Groesse des Repositories.

*Weekly volume shows additions plus deletions. It represents change activity, not the current repository size.*

### Kumulative Entwicklung / Cumulative Development

```text
Wochen / Weeks 01..26 | 2025-11-16..2026-05-16
   cap 10000 | . . . . . . . . . . . . . . . . . . . . . . . . . .
        8333 | . . . . . . . . . . . . . . . . . . . . . . . . . .
        6667 | . . . . . . . . . . . . . . . . . . . . . . . . . #
        5000 | . . . . . . . . . . . . . . . . . . . . . . . . . #
        3333 | . . . . . . . . . . . . . . . . . . . . . . . . # #
        1667 | . . . . . . . . . . . . . . . . . . . . . . . # # #
           0 +-----------------------------------------------------
```

```text
Wochen / Weeks 27..52 | 2026-05-17..2026-11-14
 cap 1000000 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      833333 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      666667 | . . . . . . . . . . . . . . . . . . . . . . . . # #
      500000 | . . . . . . . . . . . . . . . . . . . . . . . # # #
      333333 | . . . . . . . . . . . . . . . . . . . . . . # # # #
      166667 | . . . . . . . . . . . . # # # # # # # # # # # # # #
           0 +-----------------------------------------------------
```

Die kumulative Kurve summiert nur das Brutto-Aenderungsvolumen im Fenster. Sie darf nicht als aktuelle Codebasis gelesen werden.

*The cumulative curve sums gross change volume within the window only. It must not be read as the current code base.*

### Phasenvolumen / Phase Volume

```text
Slots 0..0
    cap 5000 | .
        4167 | #
        3333 | #
        2500 | #
        1667 | #
         833 | #
           0 +---
             00
```

| Slot | Phase | Nettozeilen / Net lines |
|---:|---|---:|
| 0 | Verlinkte Intake-Nachweise / Linked intake evidence | 4562 |

Die festen Slots halten den Phasenvergleich auch bei fehlenden oder spaeter ergaenzten Werten stabil.

*Stable slots keep the phase comparison consistent when values are missing or added later.*

### Beschleunigungsfaktoren / Acceleration Factors

```text
Scale: 0..100x
80 lines/day       [###############.....] 74.6x
100 lines/day      [############........] 59.7x
```

Die Faktoren vergleichen sichtbare Lieferdichte mit den dokumentierten manuellen Referenzen. Sie messen keine Arbeitszeit.

*The factors compare visible delivery density with documented manual references. They do not measure working time.*

### Durchsatzvergleich / Throughput Comparison

```text
Scale: 0..10000 lines/day
Experienced manual [#...................] 80
Thorsten solo      [#...................] 100
Visible repository [############........] 5967.7
```

Die gemeinsame Skala vergleicht Referenzen und sichtbare Lieferdichte. Sie schreibt die Git-Aktivitaet keiner Person oder KI pauschal zu.

*The common scale compares references with visible delivery density. It does not attribute Git activity to a person or AI by default.*

### Textalternative / Text Alternative

DE: Das Fenster beginnt am 2025-11-16 und endet am 2026-11-13. Es enthaelt 98 aktive und 265 inaktive vergangene Tage. Peak-Tag: 2026-10-25 / 101840. Peak-Woche: 2026-10-25 / 266277. Laengste Serie: 8 Tage (2026-07-10..2026-07-17).

*EN: The window starts on 2025-11-16 and ends on 2026-11-13. It contains 98 active and 265 inactive elapsed days. Peak day: 2026-10-25 / 101840. Peak week: 2026-10-25 / 266277. Longest streak: 8 days (2026-07-10..2026-07-17).*

| Monat / Month | Geaenderte Textzeilen / Changed text lines |
|---|---:|
| 2025-12 | 0 |
| 2026-01 | 0 |
| 2026-02 | 0 |
| 2026-03 | 0 |
| 2026-04 | 67 |
| 2026-05 | 12969 |
| 2026-06 | 37448 |
| 2026-07 | 110442 |
| 2026-08 | 96264 |
| 2026-09 | 61410 |
| 2026-10 | 325107 |
| 2026-11 | 78445 |

<!-- project-statistics-v2:end -->
