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
2. `platform-scope-decision.md` dokumentiert die ausdruecklich genehmigte
   Windows-Host-/Ubuntu-WSL2-Akzeptanzmatrix und ihre Evidenztrennung. / It
   records the explicitly approved acceptance matrix and evidence separation.
3. `verification-evidence.json` enthaelt nur beobachtete, nicht sensible
   Gate-Ergebnisse. / It records only observed, non-sensitive gate results.
4. `work-packages/` erklaert die zwoelf fachlichen Pruefgruppen und ihre
   RED-, AlreadySatisfied-, N/A- oder Open-Bewertung. / It explains the twelve
   review packages and their dispositions.
5. `human-only-handoffs.md` uebergibt exakt 49 offene Entscheidungen an die
   benannten menschlichen Rollen. / It hands exactly 49 open decisions to the
   named human roles.
6. Build-, SBOM-, Scan-, VEX-, Plattform-, A11Y- und Abschlussartefakte werden
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

Die aktuelle Ausfuehrungsplattform ist macOS. Der Windows-Host- und der
Ubuntu/WSL2-Gatepfad duerfen nach
[`DEC-XPLAT-WSL2-2026-09-04`](platform-scope-decision.md) dieselbe physische
Windows-Hardware nutzen, benoetigen aber passende getrennte Runner,
Podman-Laufzeiten und Evidenz. Fehlende Plattform- oder menschliche Evidenz
bleibt mit Owner, Folgeaktion und Trigger offen und blockiert die davon
abhaengige positive Abschlussaussage. / The current runner is macOS. The
Windows-host and Ubuntu/WSL2 gate paths may share physical Windows hardware
under the approved decision but require matching separate runners, Podman
runtimes, and evidence. Missing platform or human evidence stays open with
owner, follow-up, and trigger and blocks the dependent positive completion
claim.

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

T001 bis T065 sind mit zugehoeriger Evidenz abgeschlossen. Windows-Host,
Ubuntu/WSL2 und macOS besitzen getrennte aktuelle Build-, Runtime-,
Toolchain- und VS-Code-Nachweise. Der aktuelle macOS-Nachlauf erzeugte das
lokale arm64-Image `sha256:978cb724a3cf33be6891ad99c261a0bfe441a813d90a6be9eb029b10ce4e2a72`.
Die macOS-Podman-Machine meldet `Rootful=true`; der kanonische rootless Nachweis
und die dokumentweite Supply-Chain-Bindung bleiben beim Ubuntu/WSL2-Image
`sha256:bcdd1c8d4234ff8de8edbd1f3c52fe06c1a97d876d1c6a8996928bdff4376f2c`.
/ T001 through T065 are evidenced. Windows host, Ubuntu/WSL2, and macOS have
separate current build, runtime, toolchain, and VS Code evidence. The macOS
machine is rootful; canonical rootless and supply-chain evidence remains bound
to the WSL2 image.

Die aktuelle CycloneDX-SBOM umfasst 23.960 Komponenten. Der digest-gepinnte
Grype-Scan meldet 1.286 Matches in 390 Advisory-Gruppen: 14 Critical, 326 High,
787 Medium, 144 Low, 11 Negligible und 4 Unknown. Jede Advisory-Gruppe bleibt
sichtbar `Open`/`in_triage`; es wird kein `not affected` erfunden. Fuer die
source-only Machbarkeitsstudie besteht `GATE-SUPPLY-01` als Transparenzgate,
nicht als Aussage, das Image sei produktiv sicher oder distributionsbereit. /
The current SBOM contains 23,960 components. All 390 advisory groups remain
Open/in_triage. The supply gate proves transparency for the source-only study,
not production safety or distribution approval.

Der Repository Owner hat am 06.09.2026 die bis 31.12.2026 befristete
Ein-Personen-Machbarkeitsstudie festgelegt. Reale unabhaengige Learning-/A11Y-
und moderierte Lernendennachweise werden in diesem Studienlauf nicht erzeugt.
`feasibility-study-decision.json` dokumentiert `NotPerformed`;
`GATE-LEARNER-01` ist nur fuer diesen Abschluss `N/A`. Vor Lernenden-Rollout,
vorgebauter Image-Verteilung, produktiver Nutzung oder bei Ablauf wird der
reale Test wieder verpflichtend. / The owner limited this run to a
single-person feasibility study through 2026-12-31. Human learner evidence is
NotPerformed and N/A only for this closeout; it becomes mandatory before any
rollout, image distribution, production use, or expiry.

## Historischer Stopp an T065 / Historical Stop at T065

**DE:** Ein frueher T065-Versuch stoppte fail-closed nach Exit 2 von
`pre-commit`. Der spaetere redigierte Wiederholungslauf bestand sowohl
Pre-Commit als auch Secret-Scan; T065 ist abgeschlossen. Der damalige erste
T066-Kandidat schlug wegen vier noch fehlender Gate-Zeilen fehl und bleibt als
historische RED-Evidenz erhalten. Erst die explizite Wiederaufnahme nach
vollstaendiger Plattform- und Scope-Evidenz autorisiert genau einen neuen
T066-Kandidaten.

**EN:** An earlier T065 attempt stopped fail closed. The later redacted retry
passed pre-commit and secret scanning, completing T065. The first historical
T066 candidate failed because four gate rows were missing. It remains RED
evidence; only the explicit resume after complete platform and scope evidence
authorizes one new T066 candidate.
