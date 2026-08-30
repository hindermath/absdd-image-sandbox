# Container-Haertung: Leser- und Evidenzweg / Container Hardening: Reader and Evidence Route

## Zweck und Scope / Purpose and Scope

**DE:** Dieses Verzeichnis ist die projektspezifische Evidenz fuer Feature
`003-secure-development-container-hardening`. Eine **Evidenz** ist ein
nachvollziehbarer Beleg mit Pruefgegenstand, Befehl, Ergebnis, Plattform,
Zeitpunkt und bekannter Grenze. Die akzeptierte GSDB-Bewertung ist nur die
Arbeitsbasis: Sie schliesst keinen Gap und akzeptiert kein Restrisiko.

**EN:** This directory contains project-specific evidence for feature
`003-secure-development-container-hardening`. **Evidence** is a reviewable
record of subject, command, result, platform, time, and known limitation. The
accepted GSDB assessment is only the work baseline: it closes no gap and
accepts no residual risk.

Der Scope umfasst die lokale Podman-Entwicklungs-Sandbox, ihre Build- und
Laufzeitgrenzen, Toolchains, Agentenoberflaechen, Lieferkettenevidenz sowie
Lern- und Betriebsdokumentation. Registry-Verteilung, formale Freigaben,
Provider- oder Modellentscheidungen, echte Secrets, externe Register,
Plattformadministration und Risikoakzeptanz sind ausgeschlossen. / The scope
covers the local Podman development sandbox, build and runtime boundaries,
toolchains, agent surfaces, supply-chain evidence, and learner/operations
documentation. Registry distribution, formal approvals, provider/model
decisions, real secrets, external registers, platform administration, and risk
acceptance are excluded.

## Lesereihenfolge / Reading Order

1. `gap-dispositions.json` ordnet jeden Befund `GAP-001` bis `GAP-157` genau
   einmal zu. / It maps every finding exactly once.
2. `verification-evidence.json` enthaelt nur beobachtete, nicht sensible
   Gate-Ergebnisse. / It records only observed, non-sensitive gate results.
3. `work-packages/` erklaert die zwoelf fachlichen Pruefgruppen und ihre
   RED-, AlreadySatisfied-, N/A- oder Open-Bewertung. / It explains the twelve
   review packages and their dispositions.
4. `human-only-handoffs.md` uebergibt exakt 49 offene Entscheidungen an die
   benannten menschlichen Rollen. / It hands exactly 49 open decisions to the
   named human roles.
5. Build-, SBOM-, Scan-, VEX-, Plattform-, A11Y- und Abschlussartefakte werden
   erst nach ihrer realen Pruefung ergaenzt. / Build, SBOM, scan, VEX,
   platform, accessibility, and closeout artefacts are added only after actual
   observation.

Diese Reihenfolge ist vollstaendig als Text beschrieben. Dateinamen und
Tabellen sind Navigation, nicht die einzige Statusinformation. / This order is
fully described in text. File names and tables aid navigation but are not the
only status information.

## Statusregeln / Status Rules

- `Open` bedeutet: notwendige Evidenz oder eine menschliche Entscheidung
  fehlt. Der Umsetzungsstand bleibt `Not Assessed`. / Required evidence or a
  human decision is missing; implementation remains `Not Assessed`.
- `N/A` bedeutet: der Pruefpunkt wird durch die belegte System-, Produkt-,
  Daten- oder Distributionsgrenze nicht ausgeloest. Ein konkreter
  Neubewertungsausloeser bleibt Pflicht. / The control is not triggered by an
  evidenced boundary; a concrete re-evaluation trigger remains mandatory.
- `AlreadySatisfied` verlangt aktuelle, reproduzierbare Evidenz nach der
  letzten Aenderung des Pruefgegenstands. / It requires current reproducible
  evidence after the latest subject change.
- `FollowUp` bedeutet `Partly Fulfilled` oder `Not Fulfilled` mit Owner,
  Folgeaktion und Trigger. / It records partial or missing fulfilment with an
  owner, follow-up, and trigger.
- `Applicable` mit `Not Assessed` kennzeichnet bewusst noch nicht bewerteten,
  anwendbaren Scope. / It marks applicable scope deliberately not yet assessed.

Ein fehlgeschlagener oder uebersprungener Test ist `Open`, niemals `N/A` oder
`Pass`. Ein Dokument allein ist keine Wirksamkeitsevidenz. / A failed or
skipped test is `Open`, never `N/A` or `Pass`. A document alone is not
effectiveness evidence.

## Owner, Review und Human-only-Grenze / Ownership, Review, and Human-Only Boundary

Fuer die 108 agentisch bearbeitbaren Gaps ist `Repository Maintainer` der
Umsetzungs- und Follow-up-Owner; `Security Review` prueft die Evidenz. Das
erteilt keine Risikoakzeptanz. / For the 108 agent-actionable gaps,
`Repository Maintainer` owns implementation and follow-up and `Security
Review` reviews evidence. This grants no risk-acceptance authority.

Die exakt 49 Human-only-Gaps bleiben ohne datierten Rollenbeleg `Open`,
`Not Assessed` und `Unassessed`. Zustaendig sind je Gap `Privacy/Legal
Review`, `Platform Owner/Admin`, `CISO/ISB/KIB` oder `Project Owner`. Der
Agent darf Fakten und Vorlagen vorbereiten, aber keine formale Entscheidung,
Secret-Aktion, externe Registeraktion, Provider-/Modellfreigabe,
Plattformregel oder Risikoakzeptanz ausfuehren oder behaupten. / Exactly 49
human-only gaps remain open and unassessed without dated role evidence. The
agent may prepare facts and templates but may not perform or claim formal,
secret, external-register, provider/model, platform-rule, or risk-acceptance
actions.

Der moderierte Erstnutzungstest aus SC-009 wird ebenfalls nur durch
`Learning/A11Y Review` ausgefuehrt. Er ist ein Feature-Gate und aendert die
49-Gap-Partition nicht. / The SC-009 moderated first-use test is likewise
performed only by `Learning/A11Y Review`. It is a feature gate and does not
change the 49-gap partition.

## Changed-Path-Mapping / Changed-Path Mapping

Jeder geaenderte Produkt-, Konfigurations-, Skript- oder Dokumentationspfad
muss in mindestens einer Gap-Disposition mit Gap- und Requirement-ID
erscheinen. Zwingende Phasen- und Gate-Evidenz wird mit der jeweiligen
Gate-ID gemappt. Unabhaengige Refactorings sind nicht Teil dieses Features. /
Every changed product, configuration, script, or documentation path must map
to at least one gap disposition with gap and requirement IDs. Mandatory phase
and gate evidence maps to its gate ID. Unrelated refactors are out of scope.

## Eingangspruefung / Input Check

Am 2026-08-30 wurde T001 auf Branch
`003-secure-development-container-hardening` read-only geprueft: Run-ID
`8330f54b-97d1-424c-ad1a-842a3fad7be3`, laufende Implementierungsphase,
abgeschlossenes `analyze`-Ergebnis, sechs unveraenderte SHA-256-Bindungen,
Tasks-Hash und `65/65` Checklistenpunkte stimmen ueberein. Der autonome
Run-State wurde nicht bearbeitet. / On 2026-08-30, T001 was checked read-only:
branch, run ID, running implementation phase, completed analyze result, six
input hashes, tasks hash, and all 65 checklist items match. The autonomous run
state was not edited.

## RED vor GREEN / RED Before GREEN

Negative Fixtures pruefen fehlende, doppelte oder zusaetzliche IDs, falsche
Human-only-Zuordnung, ungueltige Statuskombinationen, fehlende Trigger,
unbekannte Felder, widerspruechliche N/A-Laufdaten, veraltete Evidenz,
Hashdrift und nicht reziproke CL-/Evidence-Referenzen. Ein unerwarteter Erfolg
blockiert jede breite Haertung. Der erste End-to-End-Slice verwendet
`GAP-147`: fehlende Mount-Evidenz muss zuerst fehlschlagen; erst eine echte,
nicht sensible Mount-Pruefung darf GREEN erzeugen. / Negative fixtures cover
the stated contract failures. An unexpected success blocks broad hardening.
The first end-to-end slice uses `GAP-147`: missing mount evidence must fail
before a real non-sensitive mount check may produce GREEN.

Am 2026-08-30T13:16:13Z bestand
`python3 -m unittest scripts.tests.test_secure_development_container_hardening`
zunaechst mit 21 Tests; nach dem Vertical Slice und den Mapping-Erweiterungen
bestand die finale statische Ausfuehrung mit 24 Tests. Jede absichtlich
fehlerhafte Fixture wurde abgelehnt: fehlende,
doppelte und zusaetzliche Gap-ID; falsches Human-only-Flag oder Rolle; falsche
Binding-Rolle; ungueltige Statuskombination; fehlender Trigger; Zusatzfeld;
widerspruechliche N/A-Laufdaten; stale positive Evidenz; falscher akzeptierter
Hash sowie nicht reziproke CL- oder Evidence-Referenz. Bash-`--dry-run` und
PowerShell-`-WhatIf` lieferten denselben Plan ohne Schreibwirkung. / At the
stated time, all 21 tests passed and every deliberately invalid fixture was
rejected. Bash dry-run and PowerShell WhatIf produced the same write-free plan.

## Bekannte Grenzen / Known Limits

Die aktuelle Ausfuehrungsplattform ist macOS. Linux- und Windows/WSL2-Gates
duerfen nur durch echte passende Runner belegt werden. Fehlende Plattform- oder
menschliche Evidenz bleibt mit Owner, Folgeaktion und Trigger offen und
blockiert die davon abhaengige positive Abschlussaussage. / The current runner
is macOS. Linux and Windows/WSL2 gates require real matching runners. Missing
platform or human evidence stays open with owner, follow-up, and trigger and
blocks the dependent positive completion claim.

## Vertikaler Slice / Vertical Slice

Am 2026-08-30T13:18:00Z wurde die Fixture
`gap-147-missing-mount-evidence.json` gezielt validiert. Erwartet und
beobachtet war Exitcode 1: `GAP-147` darf ohne aktuelle Mount-Evidenz weder
`AlreadySatisfied` noch `Fulfilled` werden. Der nachfolgende reale
`podman-compose config`-Lauf bestand, und die nicht sensible Mount-Projektion
aus `compose.yml` ergab 20 deklarierte Mounts: 14 Bind-Mounts, sechs benannte
Volumes und genau einen read-only-Konfigurationsmount. Fuenf getrennte
Agenten-Volumes halten OpenCode-, Codex-, Claude-, Gemini- und Copilot-Zustand
vom Projektcode getrennt. / The targeted fixture returned the expected exit 1.
The subsequent real Compose check passed and the non-sensitive declaration
contains 20 mounts: 14 binds, six named volumes, and one read-only
configuration mount. Five separate agent volumes isolate agent state.

Der statische Slice-Lauf vom 2026-08-30T13:20:01Z bis
2026-08-30T13:20:22Z bestand mit Exitcode 0, einschliesslich 21
Hardening-Vertragstests, Dockerfile-/Renovate-Metadaten, Home-Baseline-Lock,
Agent-Prompt- und Spec-Kit-Agentenparitaet, Documentation Impact und
`git diff --check`. Die Inspektion fand zugleich den erwarteten RED-Befund:
beide vorhandenen SBOM-Einstiege enthielten den beweglichen
`docker.io/anchore/syft:latest`-Fallback. WP03/WP05 entfernten diesen spaeter
und ersetzten den ungepinnten Host-Scanner durch einen version- und
digest-gepinnten Grype-Pfad. / The static slice passed with exit code 0 and
confirmed the movable fallback. WP03/WP05 later removed it and introduced the
pinned Grype path.

## Aktueller Implementierungsstatus / Current Implementation Status

T001 bis T055 sind mit zugehoeriger Evidenz abgeschlossen. Der exakt einmal
ausgefuehrte finale Build erzeugte die lokale Image-ID
`sha256:5bec1910211e61f60d140907a75689f9f6e31c2ec5baceaac7ff10b99d846eaf`.
Die anschliessende Ausfuehrung auf dem nativen rootless-Podman-Host unter
macOS bestand Runtime, 6/6 Sprachfamilien, 2/2 Skriptgrundlagen, sechs
Agenten-CLIs, Dispatcher-Dry-run, Audit-Export und geordneten Stop. Das Image
wurde nicht erneut gebaut. / T001 through T055 are evidenced. The one final
build produced the stated image; native macOS rootless Podman then passed
runtime, six language families, two scripting foundations, six agent CLIs,
dispatcher dry-run, audit export, and ordered stop. The image was not rebuilt.

Genau eine aktuelle CycloneDX-SBOM mit 23.967 Komponenten wurde durch Syft
1.46.0 erzeugt und mit dem digest-gepinnten Grype 0.117.0 gescannt. Der Scan
meldete 1.346 Matches in 426 Advisory-Gruppen. Jede Gruppe besitzt einen
offenen `in_triage`-Blocker; 14 Critical- und 360 High-Matches bleiben auf
Match-Ebene offen. Kein Risiko wurde akzeptiert und kein `not affected`
erfunden. / One current CycloneDX SBOM with 23,967 components was scanned by
digest-pinned Grype. All 426 advisory groups remain in triage; 14 Critical and
360 High matches are open. No risk was accepted and no not-affected result was
invented.

Offen bleiben echte Linux- und Windows/WSL2-Hostevidenz, VS-Code-Attach,
`GATE-LEARNER-01` durch `Learning/A11Y Review` und die technische oder
reviewte Disposition der Critical-/High-Treffer. Die Datei
`learner-first-use-results.json` existiert absichtlich nicht. Ein Linux-
Container auf macOS oder der macOS-Lauf ersetzt keine fehlende Hostplattform.
/ Real Linux and Windows/WSL2 host evidence, VS Code attachment, the human
learner gate, and reviewed Critical/High dispositions remain open. The learner
result file intentionally does not exist, and no substitute platform evidence
is used.

## Stopp an T065 / Stop at T065

**DE:** T056 bis T064 wurden mit ehrlicher Pass-, Fail-, Open- oder
Blocked-Evidenz abgeschlossen. T065 stoppte fail-closed: Der vollstaendig
redigierte Aufruf `uvx pre-commit run --all-files` endete mit Exit 2. Weil ein
moeglicher echter Fund ohne Einsicht in Trefferinhalte nicht sicher
ausgeschlossen werden konnte, wurde `scan-agent-secrets` nicht mehr gestartet.
T065 bleibt unchecked. T066 wurde wegen der unerfuellten Abhaengigkeit keinmal
ausgefuehrt; T066 bis T085 bleiben unchecked.

**EN:** T056 through T064 completed with honest pass, fail, open, or blocked
evidence. T065 stopped fail-closed when the fully redacted pre-commit command
returned exit 2. Because a possible real finding could not be safely excluded
without inspecting match content, scan-agent-secrets was not started. T065
remains unchecked, T066 was not run, and T066 through T085 remain unchecked.

Retry-Trigger: Eine autorisierte menschliche Security Review klassifiziert den
redigierten Pre-commit-Fehler ohne Offenlegung von Secret-Inhalten; danach
beide T065-Befehle erneut ausfuehren. / An authorized human Security Review
classifies the redacted pre-commit failure without disclosing secret content;
then rerun both T065 commands.
