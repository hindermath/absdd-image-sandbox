# Feature-Spezifikation: Sichere Entwicklungs-Container-Haertung / Feature Specification: Secure Development Container Hardening

**Feature-Branch / Feature Branch**: `003-secure-development-container-hardening`
**Erstellt / Created**: 2026-08-30
**Status**: Geklaert, bereit fuer die Checklistenphase / Clarified, ready for the checklist phase
**Eingabe / Input**: Technische und dokumentarische Haertung der Podman-basierten Entwicklungs-Sandbox auf Grundlage der sechs exakt akzeptierten Artefakte des autonomen Laufs. / Technical and documentary hardening of the Podman-based development sandbox based on the six exactly accepted artefacts of the autonomous run.

## Clarifications

### Session 2026-08-30

- **DE:** Keine Nutzerfrage ist erforderlich. Die sechs akzeptierten Artefakte
  und der getrennte autonome Run-State beantworten alle materiellen Punkte
  eindeutig. Die folgenden Anforderungen halten Gap-Disposition,
  Agent/Human-Grenze, Prioritaet, Evidenzfrische, `N/A`, Restrisiko und
  Lieferautoritaet testbar fest. **EN:** No user question is required. The six
  accepted artefacts and the separate autonomous run state answer every
  material point unambiguously. The requirements below make gap disposition,
  the agent/human boundary, priority, evidence freshness, `N/A`, residual risk,
  and delivery authority testable.

### Session 2026-09-04

- **DE:** `@hindermath` genehmigt in den Rollen `Repository Owner` und
  `Security Review` fuer Feature 003 die folgende Plattform-Scope-Aenderung:
  Der Windows-Hostpfad und der Linux-Ausfuehrungspfad werden auf derselben
  physischen Windows-Hardware geprueft. Der Linux-Ausfuehrungspfad ist Ubuntu
  unter WSL2 mit eigener rootless-Podman-Laufzeit. Beide Pfade benoetigen
  getrennte Befehls-, Zeit-, Runner-, Image- und VS-Code-Evidenz. Ein separater
  nativer Linux-Rechner ist fuer dieses Feature nicht erforderlich; native
  Linux-Kompatibilitaet wird damit weder getestet noch behauptet. Die
  Sicherheitsanforderungen und das Fail-closed-Verhalten bleiben unveraendert.
  **EN:** For Feature 003, `@hindermath`, acting as both `Repository Owner` and
  `Security Review`, approves the following platform-scope change: the Windows
  host path and the Linux execution path may be tested on the same physical
  Windows hardware. The Linux execution path is Ubuntu under WSL2 with its own
  rootless Podman runtime. Both paths require separate command, time, runner,
  image, and VS Code evidence. A separate native Linux machine is not required
  for this feature, and native Linux compatibility is neither tested nor
  claimed. Security requirements and fail-closed behaviour remain unchanged.
- **DE:** Die bindende Entscheidungsakte ist
  `docs/security/secure-development/2026-08-30-container-hardening/platform-scope-decision.md`
  mit ID `DEC-XPLAT-WSL2-2026-09-04`. **EN:** The binding decision record is
  the named evidence file with decision ID `DEC-XPLAT-WSL2-2026-09-04`.

## Nutzungsszenarien und Tests / User Scenarios & Testing *(mandatory)*

### User Story 1 - Jeden offenen Befund nachvollziehbar bearbeiten / Disposition Every Open Finding (Priority: P1)

**DE:** Eine Repository-Maintainerin oder ein Repository-Maintainer kann fuer
jeden der 157 offenen Befunde erkennen, ob er auf diese Sandbox anwendbar ist,
welche technische oder dokumentarische Aenderung erforderlich ist, welche
Evidenz den Zustand belegt und welche menschliche Entscheidung weiterhin
fehlt. Ein Befund darf nicht allein durch die Annahme der Baseline als erledigt
gelten.

**EN:** A repository maintainer can determine for each of the 157 open findings
whether it applies to this sandbox, which technical or documentary change is
required, which evidence supports the state, and which human decision is still
missing. A finding must not be treated as completed merely because the baseline
was accepted.

**Warum diese Prioritaet / Why this priority**: Die 157 offenen Befunde sind
die verbindliche Arbeitsbasis des Features. Ohne vollstaendige Zuordnung waere
keine belastbare Haertung oder Abnahme moeglich. / The 157 open findings are the
binding work baseline. Without complete mapping, no defensible hardening or
acceptance is possible.

**Unabhaengiger Test / Independent Test**: Die Gap-Evidenz wird gegen
`GAP-001` bis `GAP-157` abgeglichen. Der Test besteht nur, wenn jede ID genau
einmal vorkommt und Anwendbarkeit, Umsetzungsstand, Begruendung, Evidenzpfad,
Owner, Reviewer, Restrisiko, Folgeaktion und Neubewertungsausloeser enthaelt. /
Compare the gap evidence with `GAP-001` through `GAP-157`. The test passes only
when every ID occurs exactly once and includes applicability, implementation
state, rationale, evidence path, owner, reviewer, residual risk, follow-up, and
re-evaluation trigger.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Given / Gegeben** die unveraenderte `AcceptedBaseline` mit 157 offenen
   Gaps, **When / Wenn** die Haertungsevidenz geprueft wird, **Then / Dann** ist
   jeder Gap genau einmal auf eine Anforderung und eine aktuelle Evidenz oder
   einen klaren offenen Blocker abgebildet.
2. **Given / Gegeben** ein technisch nicht anwendbarer Pruefpunkt, **When /
   Wenn** er als `N/A` bewertet wird, **Then / Dann** bleibt sein
   Umsetzungsstand `Not Assessed` und die Bewertung enthaelt Begruendung sowie
   Neubewertungsausloeser.
3. **Given / Gegeben** ein fehlender Nachweis, **When / Wenn** kein
   reproduzierbarer Beleg vorliegt, **Then / Dann** bleibt der Gap `Open`; ein
   positiver Zustand wird nicht erfunden.

---

### User Story 2 - Eine minimal berechtigte Sandbox sicher nutzen / Use a Least-Privilege Sandbox Safely (Priority: P1)

**DE:** Lernende und Entwicklungspersonen koennen die Sandbox mit den
dokumentierten Projekt-Mappings verwenden, ohne dass Agentenzustaende,
Geheimnisse, Host-Dateien oder unnoetige Linux-Rechte in den Arbeitsbereich
gelangen. Die erforderlichen Lern- und Entwicklungsablaeufe bleiben nutzbar.

**EN:** Learners and developers can use the sandbox with the documented project
mappings without exposing agent state, secrets, host files, or unnecessary
Linux privileges to the workspace. Required learning and development workflows
remain usable.

**Warum diese Prioritaet / Why this priority**: Rootless-Laufzeit, begrenzte
Mounts, Schreibgrenzen und isolierte Agentenzustaende sind die zentrale
Vertrauensgrenze der Sandbox. / Rootless runtime, limited mounts, write
boundaries, and isolated agent state are the sandbox's central trust boundary.

**Unabhaengiger Test / Independent Test**: Eine frische lokale Instanz wird
gestartet. Tester pruefen Benutzeridentitaet, Berechtigungen, Mount-Liste,
Schreibgrenzen, Agenten-Volumes, Dateirechte, Port- und Netzwerkentscheidung
sowie einen zulaessigen und einen unzulaessigen Schreibversuch. / Start a fresh
local instance. Testers inspect user identity, privileges, mount list, write
boundaries, agent volumes, file permissions, port and network decision, and one
allowed plus one denied write attempt.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Given / Gegeben** eine frisch gebaute Sandbox, **When / Wenn** sie
   gestartet wird, **Then / Dann** laeuft der Entwicklungsprozess nicht als
   Root und besitzt nur begruendete Rechte und Schreibpfade.
2. **Given / Gegeben** getrennte Agenten- und Projektzustaende, **When / Wenn**
   ein Agent arbeitet, **Then / Dann** bleiben Anmeldedaten, Sitzungszustand
   und Providerkonfiguration ausserhalb des Repository-Inhalts.
3. **Given / Gegeben** eine Sicherheitsrestriktion, **When / Wenn** ein
   dokumentierter Lernablauf ausgefuehrt wird, **Then / Dann** funktioniert er
   oder ein konkreter, sicherheitsbezogener Blocker ist mit Owner und
   Folgeaktion dokumentiert.

---

### User Story 3 - Reproduzierbare Toolchains und Agenten pruefen / Verify Reproducible Toolchains and Agents (Priority: P1)

**DE:** Eine pruefende Person kann erkennen, welche Basis, Downloads,
Toolchains, Agenten und Hilfswerkzeuge erwartet werden, wie ihre Identitaet
festgelegt ist und ob sie im finalen lokalen Image praktisch funktionieren.

**EN:** A reviewer can determine which base, downloads, toolchains, agents, and
supporting tools are expected, how their identity is fixed, and whether they
work in practice in the final local image.

**Warum diese Prioritaet / Why this priority**: Versionsangaben ohne
reproduzierbare Herkunft und praktische Smoke-Tests sind keine ausreichende
Lieferketten- oder Laufzeitevidenz. / Version claims without reproducible
provenance and practical smoke tests are insufficient supply-chain or runtime
evidence.

**Unabhaengiger Test / Independent Test**: Ein kontrollierter Build und ein
Inventar-Smoke-Test pruefen die sechs speichersicheren Toolchain-Familien,
zwei Skriptgrundlagen, vier erforderlichen Agenten-CLIs, zwei zusaetzlichen
Agentenoberflaechen und die benoetigten Governance-/Build-Werkzeuge. / A
controlled build and inventory smoke test verify six memory-safe toolchain
families, two scripting foundations, four required agent CLIs, two additional
agent surfaces, and required governance/build tools.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Given / Gegeben** zwei Builds aus derselben freigegebenen Revision,
   **When / Wenn** ihre deklarierten Quellen und Versionen verglichen werden,
   **Then / Dann** stammen Basis und Downloads aus nachvollziehbaren,
   festgelegten Quellen; Abweichungen werden als Fehler gemeldet.
2. **Given / Gegeben** das finale lokale Image, **When / Wenn** der Smoke-Test
   laeuft, **Then / Dann** werden erwartete Identitaet, Version und ein
   minimales Projekt- oder Befehlsverhalten fuer jede verpflichtende
   Werkzeuggruppe belegt.
3. **Given / Gegeben** eine nicht verfuegbare Plattform oder Laufzeit,
   **When / Wenn** ein Test uebersprungen werden muss, **Then / Dann** wird er
   als `Open` mit Grund und Neubewertungsausloeser dokumentiert, nicht als
   bestanden.

---

### User Story 4 - Lieferketten- und Schwachstellenevidenz pruefen / Review Supply-Chain and Vulnerability Evidence (Priority: P2)

**DE:** Security Review kann fuer das finale lokale Image Komponenten,
bekannte Schwachstellen, Ausnutzbarkeitsstatus und Build-Herkunft pruefen,
ohne dass das Image in eine Registry verteilt wird.

**EN:** Security Review can inspect components, known vulnerabilities,
exploitability status, and build provenance for the final local image without
distributing that image to a registry.

**Warum diese Prioritaet / Why this priority**: SBOM, VEX-Entscheidungen und
Build-Evidenz machen technische Haertung nachvollziehbar, liegen aber hinter
den unmittelbaren Isolations- und Reproduzierbarkeitskontrollen. / SBOM, VEX
decisions, and build evidence make technical hardening reviewable but follow
the immediate isolation and reproducibility controls.

**Unabhaengiger Test / Independent Test**: Aus dem finalen lokalen Image wird
eine maschinenlesbare SBOM erzeugt und gegen Image-Identitaet, Komponenten,
Scan-Ergebnisse und VEX-Status abgeglichen. / Generate a machine-readable SBOM
from the final local image and reconcile it with image identity, components,
scan results, and VEX status.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Given / Gegeben** das finale lokale Image, **When / Wenn** die SBOM
   erzeugt wird, **Then / Dann** ist sie maschinenlesbar, datiert und eindeutig
   diesem Image zugeordnet.
2. **Given / Gegeben** eine bekannte Schwachstelle, **When / Wenn** die
   Abschluss-Evidenz erstellt wird, **Then / Dann** lautet ihr Status
   `affected`, `not affected`, `mitigated` oder `under investigation` und ist
   begruendet.
3. **Given / Gegeben** fehlende Provenienz- oder Signaturmoeglichkeiten,
   **When / Wenn** sie bewertet werden, **Then / Dann** bleibt die Grenze
   sichtbar und wird nicht durch eine erfundene SLSA- oder Signaturstufe
   ersetzt.

---

### User Story 5 - Lern- und Betriebsdokumentation inklusiv verwenden / Use Inclusive Learning and Operations Documentation (Priority: P2)

**DE:** Auszubildende aller vier Zielberufe koennen Build, Start, Status,
Abhaengigkeiten, Entscheidungen, Sicherheitsgrenzen und naechste Schritte ohne
Spec-Kit-Vorerfahrung verstehen. Deutsche Inhalte stehen zuerst, englische
Inhalte folgen; visuelle Darstellungen sind nie die einzige Informationsquelle.

**EN:** Apprentices in all four target occupations can understand build,
startup, status, dependencies, decisions, security boundaries, and next steps
without prior Spec Kit experience. German content comes first, English follows,
and visual representations are never the only information source.

**Warum diese Prioritaet / Why this priority**: Die Sandbox ist eine
Lernumgebung. Sicherheitskontrollen sind nur wirksam, wenn die vorgesehenen
Nutzenden sie verstehen und korrekt anwenden koennen. / The sandbox is a
learning environment. Security controls are effective only when intended users
can understand and apply them correctly.

**Unabhaengiger Test / Independent Test**: Eine textorientierte
Dokumentationspruefung und ein moderierter Erstnutzungs-Smoke-Test kontrollieren
Sprache, Zielgruppenabdeckung, Begriffsdefinitionen, Tastatur-/Screenreader-
Tauglichkeit und vollstaendige Textalternativen. / A text-oriented documentation
review and moderated first-use smoke test check language, audience coverage,
term definitions, keyboard/screen-reader usability, and complete text
alternatives.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Given / Gegeben** eine lern- oder bedienbezogene Anleitung, **When / Wenn**
   sie gelesen wird, **Then / Dann** erscheint Deutsch zuerst und Englisch
   danach bei ungefaehr CEFR B2; ein Fachbegriff wird bei der ersten Nutzung
   kurz erklaert.
2. **Given / Gegeben** Status, Abhaengigkeit oder Entscheidung, **When / Wenn**
   Farben, Diagramme und Layout entfernt werden, **Then / Dann** bleibt die
   vollstaendige Bedeutung als Text erhalten.
3. **Given / Gegeben** eine Person ohne Spec-Kit-Erfahrung, **When / Wenn** sie
   dem dokumentierten Ablauf folgt, **Then / Dann** werden Befehl, Artefakt,
   Zustand und Zustandswechsel beim ersten Auftreten erklaert.

### Grenz- und Fehlerfaelle / Edge Cases

- **DE:** Ein Download-Pin ist vorhanden, aber das Artefakt ist nicht mehr
  erreichbar. Der Build muss sicher fehlschlagen und der Nachweis bleibt
  `Open`; es wird weder auf `latest` noch auf eine ungepruefte Quelle
  ausgewichen. **EN:** A download pin exists, but the artefact is no longer
  available. The build must fail safely and evidence remains `Open`; it must
  not fall back to `latest` or an unverified source.
- **DE:** Ein notwendiger Lernpfad kollidiert mit einer Mount-, Netzwerk- oder
  Schreibrestriktion. Die Restriktion wird nicht still gelockert. Der Konflikt
  wird mit minimaler benoetigter Ausnahme, Risiko, Owner und Test dokumentiert.
  **EN:** A required learning path conflicts with a mount, network, or write
  restriction. The restriction is not silently weakened. The conflict is
  documented with the minimum needed exception, risk, owner, and test.
- **DE:** Ein Plattformtest kann nur auf macOS ausgefuehrt werden. Dies ist
  lokale Plausibilitaet, keine Windows-Host- oder Ubuntu/WSL2-Abnahme. Fehlende
  Plattformpfade bleiben mit genauer Begruendung offen. **EN:** A platform
  test can be run only on macOS. This is local plausibility, not Windows-host
  or Ubuntu/WSL2 acceptance. Missing platform paths remain open with a precise
  rationale.
- **DE:** Ein Scan findet ein moegliches Geheimnis. Wert und Fundinhalt werden
  nicht in Protokolle oder Spezifikationsartefakte kopiert; die Arbeit stoppt
  an der Secret-Grenze und wird menschlich eskaliert. **EN:** A scan finds a
  possible secret. Its value and matching content are not copied into logs or
  specification artefacts; work stops at the secret boundary and is escalated
  to a human.
- **DE:** Ein Gap ist sowohl technisch vorbereitbar als auch formal
  Human-only. Repository-lokale Vorlagen oder Fakten duerfen erstellt werden,
  der Gap bleibt jedoch offen, bis die benannte menschliche Rolle den externen
  oder formalen Teil belegt. **EN:** A gap is technically preparable and also
  formally human-only. Repository-local templates or facts may be prepared,
  but the gap remains open until the named human role evidences the external or
  formal part.
- **DE:** SBOM oder Scan unterscheiden sich zwischen zwei ansonsten gleichen
  Builds. Die Abweichung wird als Reproduzierbarkeitsbefund behandelt und nicht
  durch manuelle Dateiaenderung kaschiert. **EN:** SBOM or scan output differs
  between two otherwise identical builds. The difference is treated as a
  reproducibility finding and is not hidden through manual file editing.
- **DE:** Eine Agenten-CLI veraendert Anmeldung, Telemetrie oder Modellwahl.
  Diese Werte werden nicht automatisiert uebernommen; der betroffene Nachweis
  bleibt bis zur menschlichen Entscheidung offen. **EN:** An agent CLI changes
  sign-in, telemetry, or model selection. These values are not adopted
  automatically; affected evidence remains open pending human decision.

## Anforderungen / Requirements *(mandatory)*

### Verbindliche Eingabe und Traceability / Binding Input and Traceability

Nur die folgenden sechs akzeptierten Artefakte sind fachlich bindende
Feature-Eingabe. Der autonome Run-State steuert ausschliesslich den Lauf und
erweitert den fachlichen Scope nicht. / Only the following six accepted
artefacts are binding feature input. The autonomous run state governs the run
only and does not expand feature scope.

| Nr. | Pfad / Path | Akzeptierter normalisierter SHA-256 / Accepted normalized SHA-256 |
|---:|---|---|
| 1 | `Lastenheft_Secure-Development-Container-Hardening.md` | `72c263db933ea5a10ca60f3a7cc41231b43e1aec5d0dd641129e1a523b3432dc` |
| 2 | `specs/intake-review-results/sandbox-development-lifecycle.json` | `0d08a1e90e25965c4b529d66be6996394b963abef4ddb3c3b75dd678f464004b` |
| 3 | `specs/intake-series/sandbox-development-lifecycle/manifest.json` | `8813d2135a092671ccb373cd9273f44fe8ec3ceabab3eaa35f44e617cf2d15c4` |
| 4 | `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json` | `81a7ab5c5d8c6de449289de1dbf143e14933a3678a1160a25ed8ba5d671c8b39` |
| 5 | `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/prioritized-gap-list.md` | `b7e631e9df5e37686ab1ff2c0a07552c5d59c23af28621c917e36d2a42f55542` |
| 6 | `docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/acceptance-decision.md` | `12fbac3263f31646e83e4d9b841a73c41d96dcc8ca259be68b40f356bd0354c7` |

**Baseline-Regel / Baseline rule:** `AcceptedBaseline` akzeptiert die
Bewertung als Arbeitsbasis. Sie schliesst keinen der 157 Gaps, akzeptiert kein
Restrisiko und erteilt keine formale Sandbox-, Provider-, Modell-, Rechts-,
Datenschutz- oder Plattformfreigabe. / `AcceptedBaseline` accepts the assessment
as a work baseline. It closes none of the 157 gaps, accepts no residual risk,
and grants no formal sandbox, provider, model, legal, privacy, or platform
approval.

| Gap-Bereich / Gap range | Themenbereich / Subject | Anzahl / Count | Davon Human-only / Human-only |
|---|---|---:|---:|
| `GAP-001`–`GAP-012` | Standards-Anwendbarkeit / Standards applicability | 12 | 2 |
| `GAP-013`–`GAP-025` | Sichere Softwarearchitektur / Secure software architecture | 13 | 0 |
| `GAP-026`–`GAP-040` | Krypto-Mindestvorgaben / Minimum cryptography requirements | 15 | 2 |
| `GAP-041`–`GAP-050` | Bedrohungsmodellierung / Threat modelling | 10 | 0 |
| `GAP-051`–`GAP-063` | Lieferkette und Build-Integritaet / Supply chain and build integrity | 13 | 0 |
| `GAP-064`–`GAP-074` | Schwachstellenoffenlegung / Vulnerability disclosure | 11 | 1 |
| `GAP-075`–`GAP-086` | CRA-Anwendbarkeit / CRA applicability | 12 | 12 |
| `GAP-087`–`GAP-099` | Sicherheits-Code-Review / Security code review | 13 | 0 |
| `GAP-100`–`GAP-116` | KI-Codeerzeugung / AI code generation | 17 | 9 |
| `GAP-117`–`GAP-133` | Sichere Entwicklungsumgebung / Secure development environment | 17 | 7 |
| `GAP-134`–`GAP-145` | Datenschutz-Folgenabschaetzung / Data protection impact assessment | 12 | 12 |
| `GAP-146`–`GAP-157` | Agentische KI-Sandbox / Agentic AI sandbox | 12 | 4 |
| **Gesamt / Total** |  | **157** | **49** |

### Funktionale Anforderungen / Functional Requirements

- **FR-001 Gap-Vollstaendigkeit und Disposition / Gap completeness and
  disposition**: Die Abschluss-Evidenz
  MUSS alle IDs `GAP-001` bis `GAP-157` ohne Luecke und ohne Duplikat abbilden.
  Jeder Eintrag MUSS mindestens Anwendbarkeit (`Applicable`, `N/A` oder
  `Open`), Umsetzungsstand (`Fulfilled`, `Partly Fulfilled`, `Not Fulfilled`
  oder `Not Assessed`) und genau einen konsolidierten Zustand enthalten:
  `N/A` ist nur mit `N/A` + `Not Assessed` zulaessig; `Open` ist nur mit
  `Open` + `Not Assessed` zulaessig;
  `AlreadySatisfied` ist nur mit `Applicable` + `Fulfilled` zulaessig;
  `FollowUp` ist nur mit `Applicable` + `Partly Fulfilled` oder `Applicable` +
  `Not Fulfilled` zulaessig; `Applicable` ist nur mit `Applicable` +
  `Not Assessed` fuer einen bewusst noch nicht bewerteten, aber anwendbaren
  Pruefpunkt zulaessig. Die Regeln werden in dieser Reihenfolge ausgewertet.
  Jeder Eintrag MUSS ausserdem Begruendung, Evidenzpfad, Owner, Reviewer,
  Restrisiko, Folgeaktion und Neubewertungsausloeser enthalten. Die
  Ausgangslage `157 x Open` und `157 x Not Assessed` darf nur durch eine dieser
  vollstaendig belegten Dispositionen ersetzt werden. / Final evidence MUST map
  all IDs `GAP-001` through `GAP-157` without gaps or duplicates. Each entry
  MUST include applicability, implementation state, and exactly one
  consolidated state: `N/A` is permitted only with `N/A` + `Not Assessed`;
  `Open` only with `Open` + `Not Assessed`;
  `AlreadySatisfied` only with `Applicable` + `Fulfilled`; `FollowUp` only with
  `Applicable` + `Partly Fulfilled` or `Applicable` + `Not Fulfilled`; and
  `Applicable` only with `Applicable` + `Not Assessed` for an applicable review
  item deliberately not yet assessed. Apply the rules in this order. Each
  entry MUST also include rationale, evidence path, owner, reviewer, residual
  risk, follow-up, and re-evaluation trigger. The starting state of `157 x
  Open` and `157 x Not Assessed` may be replaced only by one of these fully
  evidenced dispositions.
- **FR-002 Kein impliziter Abschluss / No implicit closure**: Ein Gap DARF nur
  dann als `Fulfilled` gelten, wenn eine aktuelle reproduzierbare technische
  oder dokumentarische Evidenz sein Abnahmekriterium belegt. Baseline-Annahme,
  vorhandene Konfiguration oder ein nicht ausgefuehrter Test allein reichen
  nicht. / A gap MUST be `Fulfilled` only when current reproducible technical
  or documentary evidence proves its acceptance criterion. Baseline acceptance,
  existing configuration, or an unexecuted test alone is insufficient.
- **FR-003 Begruendetes N/A / Reasoned N/A**: Jede `N/A`-Entscheidung MUSS
  durch aktuelle Evidenz belegen, dass der Pruefpunkt wegen der beschriebenen
  System-, Produkt-, Daten- oder Distributionsgrenze sachlich nicht ausgeloest
  wird. Sie MUSS Projektkontext, Evidenzpfad, Owner, Reviewer und einen
  konkreten ereignisbezogenen Neubewertungsausloeser nennen; der
  Umsetzungsstand bleibt `Not Assessed`. Fehlende, veraltete,
  widerspruechliche oder nicht reproduzierbare Evidenz, ein fehlender
  Plattformzugang, ein uebersprungener oder fehlgeschlagener Test und eine
  ausstehende menschliche Entscheidung sind `Open`, niemals `N/A`. / Every
  `N/A` decision MUST use current evidence to prove that the review item is not
  triggered because of the stated system, product, data, or distribution
  boundary. It MUST name project context, evidence path, owner, reviewer, and a
  concrete event-based re-evaluation trigger; implementation state remains
  `Not Assessed`. Missing, stale, contradictory, or non-reproducible evidence,
  unavailable platform access, a skipped or failed test, and a pending human
  decision are `Open`, never `N/A`.
- **FR-004 Offene Punkte / Open items**: Jeder offene agentische oder
  Human-only-Punkt MUSS einen benannten Owner, die fehlende Evidenz, eine
  Folgeaktion und einen termin- oder ereignisbezogenen Neubewertungsausloeser
  enthalten. Kein offener Punkt darf als akzeptiertes Restrisiko bezeichnet
  werden, solange keine separate menschliche Entscheidung vorliegt. / Every
  open agent or human-only item MUST include a named owner, missing evidence,
  follow-up, and time- or event-based re-evaluation trigger. No open item may be
  called accepted residual risk without a separate human decision.
- **FR-004a Evidenzfrische / Evidence freshness**: Evidenz ist nur `Current`,
  wenn sie nach der letzten Aenderung ihres Pruefgegenstands erzeugt wurde und
  den aktuell bewerteten Repository-Stand beziehungsweise die finale lokale
  Image-Identitaet bindet. Der Nachweis MUSS Pruefzeitpunkt, exakten
  reproduzierbaren Befehl oder Pruefschritt, erwartetes und beobachtetes
  Ergebnis, Exitcode soweit anwendbar, Plattform, Quellversion oder Hash sowie
  bekannte Grenzen enthalten. Jede Aenderung an Quelle, Konfiguration,
  Abhaengigkeit, Toolversion, Image, Plattformergebnis oder erforderlicher
  menschlicher Entscheidung macht den Nachweis fuer den betroffenen Scope
  veraltet und loest eine erneute Pruefung aus. Ein nur vorhandenes Dokument,
  ein frueherer erfolgreicher Lauf oder ein uebersprungener Test ist keine
  aktuelle Wirksamkeitsevidenz. / Evidence is `Current` only when generated
  after the latest change to its subject and bound to the repository state
  under review or the final local image identity. It MUST record the check
  time, exact reproducible command or method, expected and observed result,
  exit code where applicable, platform, source version or hash, and known
  limitations. Any change to source, configuration, dependency, tool version,
  image, platform result, or required human decision makes the evidence stale
  for the affected scope and triggers re-verification. A document's mere
  existence, an earlier passing run, or a skipped test is not current
  effectiveness evidence.
- **FR-005 Reproduzierbare Quellen / Reproducible sources**: Basisimage,
  heruntergeladene Build-Artefakte, Paketquellen und installierte
  Werkzeugversionen MUESSEN durch unveraenderliche Identitaet, pruefbare
  Integritaet oder eine gleichwertige reproduzierbare Herkunft festgelegt
  sein. Bewegliche Versionen wie `latest` und ungepruefte Download-Fallbacks
  sind unzulaessig. / Base image, downloaded build artefacts, package sources,
  and installed tool versions MUST be fixed by immutable identity, verifiable
  integrity, or equivalent reproducible provenance. Moving versions such as
  `latest` and unverified download fallbacks are not allowed.
- **FR-006 Rootless und geringste Rechte / Rootless and least privilege**: Die
  laufende Sandbox MUSS als nicht privilegierte Person ausgefuehrt werden.
  Linux-Capabilities, Privilege-Escalation, Prozesse, Dateirechte und
  beschreibbare Pfade MUESSEN auf den nachweislich erforderlichen Umfang
  begrenzt oder mit konkreter technischer Begruendung offen dokumentiert sein.
  / The running sandbox MUST execute as a non-privileged user. Linux
  capabilities, privilege escalation, processes, file permissions, and
  writable paths MUST be limited to demonstrated need or remain openly
  documented with a concrete technical rationale.
- **FR-007 Mount- und Schreibgrenzen / Mount and write boundaries**: Jeder
  Host-Mount MUSS einen dokumentierten Lern-, Build- oder Projektzweck haben,
  mit minimaler Schreibberechtigung arbeiten und in einer pruefbaren
  Mount-Liste erscheinen. Agentische Schreibgrenzen MUESSEN mit diesen Mounts
  uebereinstimmen. / Every host mount MUST have a documented learning, build,
  or project purpose, use minimum write access, and appear in a reviewable mount
  list. Agent write boundaries MUST match these mounts.
- **FR-008 Zustands- und Geheimnistrennung / State and secret separation**:
  Agenten-, Provider- und Anmeldezustaende MUESSEN vom Repository und
  voneinander getrennt bleiben. Reale Geheimnisse, Prompt-/Antwortinhalte,
  Tokens, Provider-Endpunkte und lokale Anmeldedaten DUERFEN weder in Image,
  Commit, Testprotokoll, SBOM noch Projektevidenz aufgenommen werden. / Agent,
  provider, and sign-in state MUST remain separate from the repository and from
  each other. Real secrets, prompt/response content, tokens, provider endpoints,
  and local sign-in data MUST NOT enter the image, commits, test logs, SBOM, or
  project evidence.
- **FR-009 Netzwerkentscheidung / Network decision**: Build- und
  Laufzeit-Egress, veroeffentlichte Ports sowie agentische Netzwerkgrenzen
  MUESSEN explizit, textorientiert und testbar dokumentiert sein. Jede
  Erreichbarkeit MUSS einem erforderlichen Ablauf zugeordnet werden; freie oder
  ungetestete Erreichbarkeit bleibt `Open`. / Build and runtime egress,
  published ports, and agent network boundaries MUST be explicit, text-first,
  and testable. Every reachable path MUST map to a required workflow; open or
  untested reachability remains `Open`.
- **FR-010 Werkzeug-Inventar / Tool inventory**: Das finale lokale Image MUSS
  die sechs geforderten speichersicheren Toolchain-Familien (.NET/C#, Java,
  Go, Rust, Python und Swift), PowerShell 7 und Node.js/npm als zwei getrennte
  Skriptgrundlagen, die vier erforderlichen Agenten-CLIs (Codex, Claude Code,
  Antigravity CLI und GitHub Copilot CLI) sowie OpenCode und Gemini CLI als
  zusaetzliche Agentenoberflaechen eindeutig inventarisieren. / The final local
  image MUST unambiguously inventory the six required memory-safe toolchain
  families (.NET/C#, Java, Go, Rust, Python, and Swift), PowerShell 7 and
  Node.js/npm as two separate scripting foundations, the four required agent
  CLIs (Codex, Claude Code, Antigravity CLI, and GitHub Copilot CLI), and
  OpenCode plus Gemini CLI as additional agent surfaces.
- **FR-011 Praktische Smoke-Tests / Practical smoke tests**: Jede in FR-010
  geforderte Toolchain und Agentenoberflaeche MUSS im finalen lokalen Image
  durch Versionsidentitaet und einen angemessenen minimalen Funktions- oder
  Projekt-Smoke-Test belegt werden. Ein reiner statischer Installationshinweis
  ist keine Laufzeitevidenz. / Every toolchain and agent surface required by
  FR-010 MUST be evidenced in the final local image by version identity and an
  appropriate minimal functional or project smoke test. A static installation
  declaration alone is not runtime evidence.
- **FR-012 Agenten-Sicherheitsgrenzen / Agent safety boundaries**: Agenten-CLIs
  MUESSEN mit dokumentierten Datei-, Netzwerk-, Genehmigungs- und
  Zustandsgrenzen arbeiten. Das Feature DARF keine Anmeldung, Provider- oder
  Modellwahl, Telemetrieentscheidung, Umgehung einer Agenten-/Runtime-
  Genehmigung oder Berechtigungserweiterung automatisieren. Die eng begrenzte
  Orchestrator-Delivery-Ausnahme aus AU-002 ist keine Agenten-CLI-
  Konfigurationsaenderung und erweitert keine Repository-Regel. / Agent CLIs MUST operate with
  documented file, network, approval, and state boundaries. The feature MUST
  NOT automate sign-in, provider or model selection, telemetry decisions,
  bypass of an agent/runtime approval, or permission broadening. The narrowly
  bounded orchestrator-delivery exception in AU-002 is not an agent-CLI
  configuration change and does not broaden repository rules.
- **FR-013 Build- und Konfigurationspruefung / Build and configuration
  validation**: Die finale lokale Compose-Konfiguration MUSS statisch
  validieren; das finale Image MUSS kontrolliert bauen und starten. Fehler
  MUESSEN mit unveraendertem Exitcode und ohne Geheimnisoffenlegung sichtbar
  bleiben. / The final local Compose configuration MUST validate statically;
  the final image MUST build and start in a controlled manner. Failures MUST
  remain visible with their original exit code and without exposing secrets.
- **FR-014 SBOM / SBOM**: Fuer das finale lokale Image MUSS eine
  maschinenlesbare CycloneDX-SBOM oder eine fachlich gleichwertige
  maschinenlesbare Komponentenliste erzeugt, datiert und eindeutig der
  Image-Identitaet zugeordnet werden. Die Erzeugung ist lokal; eine
  Registry-Verteilung ist ausgeschlossen. / A machine-readable CycloneDX SBOM
  or professionally equivalent machine-readable component inventory MUST be
  generated for the final local image, dated, and linked unambiguously to image
  identity. Generation is local; registry distribution is excluded.
- **FR-015 Schwachstellen und VEX / Vulnerabilities and VEX**: Bekannte
  Schwachstellen im finalen Image MUESSEN bewertet werden. Fuer jeden relevanten
  Fund MUSS ein begruendeter VEX-Status (`affected`, `not affected`,
  `mitigated`, `under investigation`) oder ein offener Blocker dokumentiert
  sein. / Known vulnerabilities in the final image MUST be assessed. Every
  relevant finding MUST have a reasoned VEX status or an open blocker.
- **FR-016 Build-Herkunft und Integritaet / Build provenance and integrity**:
  Lokal erreichbare Build-Herkunfts-, Reproduzierbarkeits-, Signatur- und
  SLSA-Evidenz MUSS dokumentiert werden. Nicht erreichbare externe
  Provenienz- oder Signaturstufen bleiben mit genauer Grenze `Open` oder
  begruendet `N/A`; sie werden nicht erfunden. / Locally achievable build
  provenance, reproducibility, signature, and SLSA evidence MUST be documented.
  Unavailable external provenance or signature levels remain precisely bounded
  as `Open` or reasoned `N/A`; they are not invented.
- **FR-017 Abhaengigkeiten und Updates / Dependencies and updates**:
  Abhaengigkeiten MUESSEN aus verifizierbaren Quellen stammen, festgelegt und
  auf bekannte kritische Schwachstellen sowie Lizenzhinweise geprueft werden.
  Automatisierte Update-Hinweise duerfen vorbereitet werden, aber keine
  Plattformadministration oder automatische Freigabe ausloesen. /
  Dependencies MUST come from verifiable sources, be fixed, and be checked for
  known critical vulnerabilities and licence notices. Automated update
  notifications may be prepared but must not trigger platform administration
  or automatic approval.
- **FR-018 Sicherheits- und Audit-Evidenz / Security and audit evidence**:
  Repository-lokale Evidenz unter `docs/security/` MUSS Fakten, Befehle,
  Zeitpunkte, Plattformen, Limitierungen und Ergebnisse enthalten, jedoch keine
  Prompt-/Antwortinhalte oder Geheimnisse. / Repository-local evidence under
  `docs/security/` MUST contain facts, commands, timestamps, platforms,
  limitations, and results, but no prompt/response content or secrets.
- **FR-019 Dokumentation / Documentation**: Lern-, Bedien-, Sicherheits- und
  Governance-Dokumentation MUSS Build, Start, Stop, Mounts, Ports, Netzwerk,
  Agentenzustand, Toolchains, Smoke-Tests, SBOM, bekannte Grenzen und sichere
  Fehlerbehebung abdecken. / Learning, operations, security, and governance
  documentation MUST cover build, startup, shutdown, mounts, ports, network,
  agent state, toolchains, smoke tests, SBOM, known boundaries, and safe
  troubleshooting.
- **FR-020 Keine unbegruendete Funktionsminderung / No unjustified loss of
  function**: Eine Haertung darf dokumentierte Lern- und Entwicklungsablaeufe
  nur blockieren, wenn die Restriktion sicherheitsnotwendig, minimal und durch
  Test plus Begruendung belegt ist. / Hardening may block documented learning
  and development workflows only when the restriction is security-required,
  minimal, and supported by a test plus rationale.
- **FR-021 Scope-Schutz / Scope protection**: Aenderungen MUESSEN auf einen
  oder mehrere der 157 Gaps und eine Anforderung dieser Spezifikation
  rueckverfolgbar sein. Unabhaengige Refactorings und Komfortaenderungen sind
  ausgeschlossen. / Changes MUST trace to one or more of the 157 gaps and a
  requirement in this specification. Unrelated refactors and convenience
  changes are excluded.
- **FR-022 Priorisierte Reihenfolge / Prioritised order**: Alle 157
  Baseline-Gaps behalten `P1`. Innerhalb des Features kommen die P1-Arbeitsziele
  Traceability, geringste Rechte und Reproduzierbarkeit vor den
  P2-Arbeitszielen Lieferkettenevidenz und inklusive Dokumentation. Fuer ihre
  Bearbeitung gilt die folgende bindende Abhaengigkeitsreihenfolge: (1) sechs
  Eingabehashes und die vollstaendige
  157/108/49-Zuordnung sichern; (2) die 108 agentisch bearbeitbaren Gaps fuer
  Rootless-/Rechte-, Mount-/Schreib-, Secret-/Zustands-, Netzwerk- und
  reproduzierbare Quellen-/Toolchain-Grenzen bearbeiten; (3) Konfiguration,
  Build, Laufzeit und Smoke-Tests dieser P1-Grenzen belegen; (4) erst fuer das
  dadurch bestimmte finale lokale Image SBOM-, Schwachstellen-, VEX- und
  Provenienz-Evidenz erzeugen; (5) Lern-, Betriebs-, A11Y- und
  Cross-Platform-Dokumentation gegen den belegten Zustand abschliessen; (6)
  alle 157 Dispositionen erneut abgleichen und die 49 Human-only-Uebergaben
  offen an die benannten Rollen uebergeben. Spaetere Gruppen duerfen parallel
  vorbereitet werden, aber kein Gate einer frueheren Gruppe ueberschreiben
  oder als bestanden voraussetzen. / Because all 157 baseline gaps are `P1`,
  the following dependency order is binding: (1) preserve the six input hashes
  and complete 157/108/49 mapping; (2) address the 108 agent-actionable gaps
  for rootless/privilege, mount/write, secret/state, network, and reproducible
  source/toolchain boundaries; (3) evidence configuration, build, runtime, and
  smoke tests for those P1 boundaries; (4) only then generate SBOM,
  vulnerability, VEX, and provenance evidence for the resulting final local
  image; (5) complete learning, operations, accessibility, and cross-platform
  documentation against the evidenced state; and (6) reconcile all 157
  dispositions again and hand the 49 human-only items, still open, to their
  named roles. Later groups may be prepared in parallel but MUST NOT override
  or assume a passing gate from an earlier group. All 157 baseline gaps retain
  `P1`. Within the feature, the P1 outcomes for traceability, least privilege,
  and reproducibility precede the P2 outcomes for supply-chain evidence and
  inclusive documentation.

### Governance-Anforderungen / Governance Requirements *(mandatory)*

- **GR-001 Zielgruppen / Audiences**: Verbindliche Zielgruppen ab dem ersten
  Ausbildungsjahr sind Fachinformatikerinnen und Fachinformatiker,
  IT-System-Elektronikerinnen und IT-System-Elektroniker, Kaufleute fuer
  IT-System-Management sowie Kaufleute fuer Digitalisierungsmanagement. /
  Binding audiences from the first training year are IT specialists, IT
  systems electronics technicians, management assistants for IT systems
  management, and management assistants for digitalisation management.
- **GR-002 Sprach- und Lernniveau / Language and learner level**:
  Nutzerbezogene Inhalte MUESSEN Deutsch zuerst und Englisch direkt danach bei
  ungefaehr CEFR B2 liefern, Fachbegriffe bei der ersten Verwendung erklaeren
  und keine Spec-Kit-Erfahrung voraussetzen. Ueberschriften folgen `DE / EN`,
  sofern kein synchrones `.EN.md`-Partnerdokument begruendet wird. /
  User-facing content MUST provide German first and English directly after it
  at about CEFR B2, explain technical terms on first use, and assume no Spec
  Kit experience. Headings follow `DE / EN` unless a synchronized `.EN.md`
  companion is justified.
- **GR-003 Text zuerst / Text first**: Status, Abhaengigkeiten, Entscheidungen,
  naechste Schritte und Risiken MUESSEN vollstaendig textorientiert erklaert
  sein. Diagramm, Farbe, Symbol und raeumliche Position duerfen nur ergaenzen.
  / Status, dependencies, decisions, next steps, and risks MUST have complete
  text-first explanations. Diagrams, colour, symbols, and spatial position may
  only supplement them.
- **GR-004 WCAG 2.2 AA**: Fuer anwendbare Nutzeroberflaechen, CLI-Ausgaben,
  Markdown-/HTML-Dokumentation und erzeugte Vorlagen gilt WCAG 2.2 Level AA.
  Relevante Pfade umfassen insbesondere 1.1.1, 1.3.1, 1.4.1, 1.4.3, 1.4.10,
  2.1.1, 2.1.2, 2.4.6, 2.4.7, 2.4.11, 3.1.1, 3.1.2, 3.2.3, 3.3.1 und
  4.1.2, soweit der Artefakttyp das Kriterium ausloest. / WCAG 2.2 Level AA
  applies to relevant user interfaces, CLI output, Markdown/HTML documentation,
  and generated templates. Applicable paths include the listed criteria where
  the artefact type triggers them.
- **GR-005 Didaktische Kommentare / Didactic comments**: Wenn das Feature
  nichttriviale Skript- oder Helper-Logik aendert, MUESSEN kurze didaktische
  Kommentare Sicherheitsgrenzen und nicht offensichtliche Entscheidungen fuer
  Lernende erklaeren. Fuer reine Konfigurations- oder Dokumentaenderungen ist
  dies `N/A`; Neubewertung erfolgt, sobald nichttriviale Logik in den Plan
  aufgenommen wird. / If the feature changes non-trivial script or helper
  logic, concise didactic comments MUST explain security boundaries and
  non-obvious decisions for learners. This is `N/A` for configuration-only or
  documentation-only changes and is re-evaluated when non-trivial logic enters
  the plan.
- **GR-006 Dokumentationsentscheidung / Documentation decision**:
  `UpdateRequired`. Betroffen sind alle in GR-001 genannten Lernenden,
  Lernbegleitung, Entwicklung, Repository Maintenance und Security Review.
  Weitere Pflichtfelder stehen unter „Dokumentationswirkung“. /
  `UpdateRequired`. Affected audiences are all learners in GR-001, learning
  support, development, repository maintenance, and Security Review. Further
  mandatory fields are recorded under “Documentation impact”.
- **GR-007 Statistiken / Statistics**: In der Spezifikationsphase ist eine
  Statistikaktualisierung `N/A`, weil weder Implementierung noch Merge
  abgeschlossen wird. Sie MUSS am Abschluss der spaeteren Implementierung oder
  nach Merge gemaess Repository-Regel neu bewertet werden. / A statistics
  update is `N/A` during specification because neither implementation nor merge
  is complete. It MUST be re-evaluated after later implementation completion or
  merge under repository rules.

### Human-only-Grenzen / Human-Only Boundaries

Die akzeptierte Baseline teilt die 157 Gaps vollstaendig und ohne Ueberlappung
in exakt 108 agentisch bearbeitbare und 49 Human-only-Gaps. Fuer die 108 ist
`Repository Maintainer` Umsetzungs- und Follow-up-Owner und `Security Review`
Reviewer; diese Zuordnung erlaubt repository-lokale Aenderungen und Evidenz,
aber keine Risikoakzeptanz. Fuer die 49 duerfen technische Vorbereitung und
Faktenaufbereitung im Repository erfolgen; Abschluss, formale Entscheidung und
Restrisikoakzeptanz bleiben ausschliesslich der je Gap genannten menschlichen
Rolle vorbehalten. Ohne deren datierten Rollenbeleg bleibt der Gap `Open`, das
Restrisiko `Unassessed` und eine vorbereitete Vorlage ist kein Abschluss. / The
accepted baseline partitions the 157 gaps completely and without overlap into
exactly 108 agent-actionable and 49 human-only gaps. For the 108, `Repository
Maintainer` is implementation and follow-up owner and `Security Review` is the
reviewer; this assignment permits repository-local changes and evidence but
does not permit risk acceptance. For the 49, technical preparation and fact
collection may occur in the repository; closure, formal decision, and residual
risk acceptance remain solely with the human role named for each gap. Without
dated evidence from that role, the gap remains `Open`, residual risk remains
`Unassessed`, and a prepared template is not closure.

| Rolle / Role | Exakte Gap-IDs / Exact gap IDs | Zulaessige agentische Grenze / Permitted agent boundary |
|---|---|---|
| Privacy/Legal Review | `GAP-011`, `GAP-012`, `GAP-070`, `GAP-075`–`GAP-086`, `GAP-105`, `GAP-106`, `GAP-115`, `GAP-134`–`GAP-145` | Fakten, Vorlagen und offene Fragen vorbereiten; keine Rechts-, Datenschutz-, CRA-, DPIA- oder Registerentscheidung treffen. / Prepare facts, templates, and open questions; make no legal, privacy, CRA, DPIA, or register decision. |
| Platform Owner/Admin | `GAP-034`, `GAP-035`, `GAP-120`, `GAP-121`, `GAP-124`, `GAP-128`–`GAP-131`, `GAP-155` | Repository-Evidenz und Anleitungen vorbereiten; keine Schluesselaktion, Branch-Regel, Plattformkonfiguration, zentrale Audit-, Endpoint-, Backup- oder Netzwerkfreigabe ausfuehren. / Prepare repository evidence and guidance; perform no key action, branch rule, platform configuration, central audit, endpoint, backup, or network approval. |
| CISO/ISB/KIB | `GAP-100`–`GAP-102`, `GAP-109`, `GAP-110`, `GAP-146`, `GAP-150`, `GAP-152` | Inventar und technische Grenzen dokumentieren; keine Werkzeug-, Modell-, Telemetrie-, Sandbox- oder Review-Freigabe behaupten. / Document inventory and technical boundaries; claim no tool, model, telemetry, sandbox, or review approval. |
| Project Owner | `GAP-113` | Ausnahme und Risiko beschreiben; keine Risikoakzeptanz stellvertretend erklaeren. / Describe exception and risk; do not accept risk on the owner's behalf. |

Zusaetzlich ausgeschlossen sind Registry-Verteilung, formale Freigaben, reale
Secret- oder Schluesselaktionen, Eintraege in externe Register oder
Managementsysteme und nicht rueckverfolgbare Refactorings. / Also excluded are
registry distribution, formal approvals, real secret or key actions, entries in
external registers or management systems, and untraceable refactors.

### Security-Governance-Anwendbarkeit / Security Governance Applicability

| Checkpoint | Anwendbarkeit / Applicability | Anforderung, Evidenz und Neubewertung / Requirement, evidence, and re-evaluation |
|---|---|---|
| Primaersprache und Memory Safety / Primary language and memory safety | Applicable | Das Repository hat keine einzelne Anwendungssprache. Fuer wiederverwendbare Helper-Logik gilt Python als primaere speichersichere Sprache; Bash und PowerShell bleiben notwendige plattformbezogene Schnittstellen. Keine neue nicht speichersichere Sprache ohne dokumentierte Hardware-/Legacy-Begruendung. Evidenz: `docs/security/` und Sprach-/Skript-Reviews. Neubewertung bei Sprach- oder Runtime-Aenderung. / The repository has no single application language. Python is the primary memory-safe language for reusable helper logic; Bash and PowerShell remain required platform interfaces. No new non-memory-safe language without documented hardware/legacy rationale. Re-evaluate on language or runtime change. |
| NIST SSDF | Applicable | Die Haertung MUSS Vorbereitung, Schutz, sichere Erzeugung und Reaktion/Verbesserung abdecken. Evidenz: Gap-Matrix und Sicherheitsartefakte. Neubewertung bei Scope-Aenderung. / Hardening MUST cover preparation, protection, secure production, and response/improvement. |
| CWE Top 25 | Applicable | Architektur-, Skript-, Datei-, Eingabe-, Abhaengigkeits- und Geheimnisgrenzen MUESSEN relevante CWE-Ursachen pruefen. Evidenz: Security Checklist und Review. Neubewertung bei Code-/Skript-Aenderung. / Architecture, script, file, input, dependency, and secret boundaries MUST check relevant CWE root causes. |
| OWASP ASVS | N/A | Die Sandbox ist kein Web-, API-, HTTP- oder Authentifizierungsdienst. Re-Evaluation, sobald ein eigener solcher Dienst oder eine eigene Authentifizierung in Scope kommt. / The sandbox is not a web, API, HTTP, or authentication service. Re-evaluate if such a service or authentication enters scope. |
| SBOM | Applicable | FR-014; Evidenz in `docs/security/` plus lokales Build-Artefakt. Neubewertung fuer jedes finale Image. / FR-014; evidence under `docs/security/` plus local build artefact. Re-evaluate for every final image. |
| VEX | Applicable | FR-015; anwendbar fuer bekannte Schwachstellen im finalen Image. Neubewertung nach jedem Scan oder Komponentenwechsel. / FR-015; applies to known vulnerabilities in the final image. Re-evaluate after each scan or component change. |
| AI-SBOM | N/A | Agenten und Modelle werden nur als Entwicklungswerkzeuge verwendet; kein Modell, Datensatz, Inferenzdienst oder KI-Produktbestandteil wird als Runtime-Komponente des Sandbox-Images freigegeben. CLI-Inventar und Anbietertransparenz bleiben getrennte Governance-Evidenz. Neubewertung, sobald eine KI-Runtime oder ein Modell Bestandteil des ausgelieferten oder betriebenen Systems wird. / Agents and models are development tools only; no model, dataset, inference service, or AI product component is released as a runtime component of the sandbox image. Re-evaluate when an AI runtime or model becomes part of the delivered or operated system. |
| SLSA | Applicable target | Lokale Provenienz und reproduzierbare Build-Evidenz nach FR-016; keine veroeffentlichte SLSA-Stufe ohne externe Pipeline-Evidenz. Neubewertung bei CI/CD- oder Veroeffentlichungs-Scope. / Local provenance and reproducible build evidence under FR-016; no published SLSA level without external pipeline evidence. Re-evaluate when CI/CD or publication enters scope. |
| OpenSSF Scorecard | Applicable | Repository- und hochwirksame Abhaengigkeits-Evidenz wird dokumentiert; keine Plattformregel wird veraendert. Neubewertung bei neuen hochwirksamen Quellen oder Veroeffentlichung. / Repository and high-impact dependency evidence is documented; no platform rule is changed. Re-evaluate for new high-impact sources or publication. |
| NIS2, CRA, EU AI Act, DORA | Open, Human-only | Technische Fakten duerfen vorbereitet werden; formale Anwendbarkeit und Pflichten entscheidet Privacy/Legal Review. Owner: Privacy/Legal Review. Evidenz: `docs/security/regulatory-applicability.md` oder begruendetes Aequivalent. Trigger: Marktbereitstellung, Kundenuebergabe, KI-Runtime, Finanzsektorbezug oder Rechtsaenderung. / Technical facts may be prepared; Privacy/Legal Review decides formal applicability and duties. Trigger: market placement, customer handover, AI runtime, financial-sector context, or legal change. |
| Krypto-Mindestvorgaben / Minimum cryptography | Applicable in part | SHA-256-Integritaet, Signaturpruefung und TLS-Quellen duerfen technisch bewertet werden. Produktkryptografie ist `N/A`, solange keine eigene Krypto-Funktion hinzukommt. Schluesselverwaltung und Rotation sind Human-only. Neubewertung bei eigener Krypto-, Secret- oder Signaturfunktion. / SHA-256 integrity, signature verification, and TLS sources may be assessed technically. Product cryptography is `N/A` unless a cryptographic function is added. Key management and rotation are human-only. |

Erwartete Security-Evidenz / Expected security evidence:

- `docs/security/msl-applicability.md`
- `docs/security/security-checklist.md`
- `docs/security/secure-coding-language-rules.md`
- `docs/security/dependency-audit.md`
- `docs/security/supply-chain-evidence.md`
- `docs/security/regulatory-applicability.md`
- `docs/security/zero-trust-applicability.md`
- `docs/security/samm-assessment.md`
- `docs/security/cloud-autonomy-applicability.md`
- `docs/security/cloud-compliance-assurance.md`
- projektspezifische Gap-, SBOM-, VEX-, Scan-, Isolations- und Audit-Evidenz
  unter `docs/security/secure-development/` / project-specific gap, SBOM, VEX,
  scan, isolation, and audit evidence under `docs/security/secure-development/`

`docs/security/asvs-verification.md` ist `N/A` aufgrund der oben begruendeten
ASVS-Nichtanwendbarkeit; es wird neu bewertet, sobald ein eigener HTTP-, API-
oder Authentifizierungsdienst in Scope kommt. / `docs/security/asvs-verification.md`
is `N/A` due to the ASVS rationale above; re-evaluate when a first-party HTTP,
API, or authentication service enters scope.

### Architektur- und Trust-Boundary-Anwendbarkeit / Architecture and Trust-Boundary Applicability

- **AR-001 Architekturwirkung / Architecture impact**: Das Feature betrifft
  Systemkontext, Build- und Laufzeit-Bausteine, externe Paket-/Providergrenzen,
  Dateisystem- und Agentenschnittstellen, Laufzeitverhalten, Deployment,
  Sicherheits-, Wartbarkeits-, Portabilitaets- und Reproduzierbarkeitsziele
  sowie technischen Schuldenstand. / The feature affects system context, build
  and runtime building blocks, external package/provider boundaries, file
  system and agent interfaces, runtime behaviour, deployment, security,
  maintainability, portability, reproducibility goals, and technical debt.
- **AR-002 Trust Boundaries**: Mindestens Host↔Container,
  Repository↔Agentenzustand, Projekt-Mount↔Toolchain, Container↔Paketquelle,
  Agenten-CLI↔Provider, lokales Image↔SBOM/Scan und Lernende↔privilegierte
  Wartungsablaeufe MUESSEN textorientiert modelliert werden. Datenklassen sind
  `public`, `internal`, `confidential` und `restricted`; reale Secrets bleiben
  ausserhalb der Evidenz. / At minimum host↔container, repository↔agent state,
  project mount↔toolchain, container↔package source, agent CLI↔provider, local
  image↔SBOM/scan, and learner↔privileged maintenance workflows MUST be modelled
  text-first. Data classes are `public`, `internal`, `confidential`, and
  `restricted`; real secrets remain outside evidence.
- **AR-003 Threat Model**: Ein STRIDE+CIA-Bedrohungsmodell mit Assets,
  Datenfluessen, Vertrauensgrenzen, Massnahmen, Restrisiken und CAPEC-Bezug fuer
  hoechstriskante Pfade ist `Applicable`. Evidenz:
  `docs/security/threat-model.md`. Neubewertung bei Mount-, Netzwerk-,
  Privileg-, Agenten-, Provider- oder Deployment-Aenderung. / A STRIDE+CIA
  threat model with assets, flows, trust boundaries, mitigations, residual
  risks, and CAPEC references for highest-risk paths is `Applicable`.
- **AR-004 ADR und arc42**: Sicherheitsrelevante Architekturentscheidungen
  zu Isolation, Privilegien, Egress, Quellenintegritaet und Zustandsgrenzen
  erfordern ADR/S-ADR-Evidenz. `docs/architecture/` MUSS Kontext-, Baustein-,
  Laufzeit-, Deployment-, Qualitaetsszenario-, Architekturentscheidungs- und
  Architekturrisiko-Evidenz enthalten oder auf ein begruendetes
  projektspezifisches Aequivalent verweisen. `docs/security/arc42-security.md`
  MUSS die Security-Cross-Cutting-Concepts abdecken. / Security-relevant
  architecture decisions on isolation, privileges, egress, source integrity,
  and state boundaries require ADR/S-ADR evidence. `docs/architecture/` MUST
  contain or link an equivalent context, building-block, runtime, deployment,
  quality-scenario, architecture-decision, and architecture-risk record.
- **AR-005 Qualitaetsszenarien / Quality scenarios**: Mindestens sichere
  Ablehnung eines unzulaessigen Schreibzugriffs, reproduzierbarer Build,
  erfolgreicher Toolchain-Smoke-Test, nachvollziehbare Egress-Entscheidung und
  Wiederherstellung nach fehlgeschlagenem Build MUESSEN als messbare
  Szenarien dokumentiert werden. / At minimum safe rejection of an unauthorized
  write, reproducible build, successful toolchain smoke test, reviewable egress
  decision, and recovery after failed build MUST be documented as measurable
  scenarios.
- **AR-006 Zero Trust**: `N/A` fuer eine rein lokale Einzel-Container-
  Lernumgebung ohne verteilten oder remote verwalteten Dienst. Die
  Providergrenze bleibt dennoch Trust Boundary. Neubewertung, sobald Remote-
  Management, Multi-Device, Cloud- oder Service-Architektur hinzukommt. /
  `N/A` for a local single-container learning environment without distributed
  or remotely managed service. The provider edge remains a trust boundary.
- **AR-007 BSI C3A und C5 / BSI C3A and C5**: `N/A`, weil Registry-Verteilung,
  Cloud-Service-Auswahl, SaaS/PaaS/IaaS und Provider-Deployment ausgeschlossen
  sind. Neubewertung bei Cloud-, Hosting- oder Managed-Service-Scope. / `N/A`
  because registry distribution, cloud-service selection, SaaS/PaaS/IaaS, and
  provider deployment are excluded. Re-evaluate for cloud, hosting, or managed
  service scope.
- **AR-008 OWASP SAMM**: `Applicable` als dokumentarische
  Verbesserungsbewertung fuer den langlebigen Sandbox-Workspace; keine
  formale Reifegradfreigabe wird behauptet. Evidenz:
  `docs/security/samm-assessment.md`. Neubewertung am Feature-Abschluss. /
  `Applicable` as a documentary improvement assessment for the long-lived
  sandbox workspace; no formal maturity approval is claimed.

### Cross-Platform-Anwendbarkeit / Cross-Platform Applicability

- **CP-001**: Das Feature aendert voraussichtlich skriptfoermige Build-,
  Smoke-, Audit- oder SBOM-Ablaufe und ist daher fuer macOS, den Windows-Host
  und Ubuntu unter WSL2 als Linux-Ausfuehrungsumgebung `Applicable`. Der
  Windows-Host- und der Ubuntu/WSL2-Pfad duerfen dieselbe physische Hardware
  verwenden, MUESSEN aber getrennte Laufzeiten und Evidenz besitzen. Native
  Linux-Hardware ist fuer Feature 003 nicht Teil der Akzeptanzmatrix. Jede neue
  oder geaenderte kritische
  Skriptschnittstelle MUSS gleichwertige Bash- (`*.sh`) und PowerShell-7-
  Varianten (`*.ps1`) besitzen. / The feature is expected to change
  script-shaped build, smoke, audit, or SBOM workflows and is therefore
  `Applicable` to macOS, the Windows host, and Ubuntu under WSL2 as the Linux
  execution environment. The Windows-host and Ubuntu/WSL2 paths may use the
  same physical hardware but MUST use separate runtimes and evidence. Native
  Linux hardware is outside the Feature 003 acceptance matrix. Every new or
  changed critical script interface MUST have equivalent Bash and PowerShell 7
  variants.
- **CP-002**: Bash bietet `--dry-run`; PowerShell bietet `-WhatIf`. Beide Modi
  MUESSEN dieselben geplanten Aenderungen ohne Schreibwirkung berichten.
  Exitcodes und fachliche Ergebnisse MUESSEN gleichwertig sein. / Bash provides
  `--dry-run`; PowerShell provides `-WhatIf`. Both modes MUST report equivalent
  intended changes without writes. Exit codes and functional results MUST be
  equivalent.
- **CP-003**: Fuer einen neuen einheitlichen Haertungs-Pruefeinstieg ist der
  geplante Cmdlet-Name `Test-AdeSandboxHardening` und die Manpage
  `docs/man/test-ade-sandbox-hardening.1`. Fuer eine neue einheitliche
  SBOM-Erzeugung sind `New-AdeSandboxSbom` und
  `docs/man/new-ade-sandbox-sbom.1` vorgesehen. Wenn die Planung stattdessen
  bestehende Schnittstellen beibehält, MUSS sie vor der Task-Erzeugung deren
  konkrete genehmigte `Verb-Noun`-Namen und Manpages dokumentieren. / For a new
  unified hardening validation entry point, the planned Cmdlet name is
  `Test-AdeSandboxHardening` with man page
  `docs/man/test-ade-sandbox-hardening.1`. For new unified SBOM generation,
  use `New-AdeSandboxSbom` and `docs/man/new-ade-sandbox-sbom.1`. If planning
  retains existing interfaces instead, it MUST document their approved
  `Verb-Noun` names and man pages before task generation.
- **CP-004**: Jede PowerShell-Variante MUSS vollstaendige kommentarbasierte
  Hilfe in Deutsch zuerst und Englisch danach enthalten. Jede Bash-Manpage und
  `--help`-Ausgabe MUSS fachlich synchron sein. / Every PowerShell variant MUST
  include complete comment-based help in German first and English second.
  Every Bash man page and `--help` output MUST remain functionally synchronized.
- **CP-005**: Nicht verfuegbare Plattformtests werden mit Plattformpfad, Grund,
  Owner und Wiederholungsausloeser als `Open` dokumentiert. Ein Erfolg in nur
  einem Ausfuehrungspfad ist keine plattformuebergreifende Abnahme. Ergebnisse
  der Windows-Podman-Machine duerfen nicht als Ubuntu/WSL2-rootless-Podman-
  Evidenz wiederverwendet werden. / Unavailable platform tests are recorded as
  `Open` with platform path, reason, owner, and retry trigger. Success in only
  one execution path is not cross-platform acceptance. Windows Podman-machine
  results must not be reused as Ubuntu/WSL2 rootless-Podman evidence.

### Agent-Paritaet / Agent Parity Applicability

- **AP-001**: Aenderungen an gemeinsamem Betriebs-, Sicherheits-, Lernenden-
  oder Spec-Kit-Verhalten MUESSEN synchron in `AGENTS.md`, `CLAUDE.md`,
  `GEMINI.md` und `.github/copilot-instructions.md` gepflegt werden. Wenn die
  betroffene Regel auch die Copilot-Agentenoberflaeche spiegelt, gehoert
  `.github/agents/copilot-instructions.md` in denselben Aenderungssatz. /
  Changes to shared operations, security, learner, or Spec Kit behaviour MUST
  be synchronized across `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and
  `.github/copilot-instructions.md`. When the affected rule is mirrored in the
  Copilot agent surface, `.github/agents/copilot-instructions.md` belongs to
  the same change set.
- **AP-002**: Aenderungen an gemeinsamen Regeln MUESSEN auch die passenden
  Projektvorlagen unter `.specify/templates/` und
  `.specify/memory/constitution.md` pruefen und synchron aktualisieren. Reine
  projektspezifische Betriebsdetails duerfen mit Begruendung ohne
  Baseline-Synchronisation bleiben. / Shared rule changes MUST also inspect and
  synchronize matching project templates under `.specify/templates/` and
  `.specify/memory/constitution.md`. Project-specific operational details may
  remain local with rationale.
- **AP-003**: Provider- oder modellspezifische Namen sind keine
  Feature-Anforderung. Modell-Routing bleibt agentenneutrale operative
  Guidance. / Provider- or model-specific names are not feature requirements.
  Model routing remains agent-neutral operational guidance.
- **AP-004**: Absichtliche Abweichungen sind derzeit `N/A`; Trigger ist eine
  spaetere Anforderung, die auf einer Agentenoberflaeche technisch nicht
  abbildbar ist. Dann sind Grund, Auswirkung, Owner und Neubewertungspfad zu
  dokumentieren. / Intentional deviations are currently `N/A`; the trigger is
  a later requirement that cannot technically be represented on one agent
  surface. Then rationale, impact, owner, and re-evaluation path are required.

### Autonomous-Run-Anwendbarkeit / Autonomous-Run Applicability

- **AU-001 Run-Identitaet / Run identity**: Feature-lokaler Zustand:
  `specs/003-secure-development-container-hardening/autonomous-run-state.json`;
  Run-ID `8330f54b-97d1-424c-ad1a-842a3fad7be3`; Feature-Identitaet
  `003-secure-development-container-hardening`. Die akzeptierten Eingaben sind
  die sechs Hash-Bindungen oben. / Feature-local state, run ID, feature
  identity, and accepted inputs are fixed as stated.
- **AU-002 Delivery Mode und Autoritaet / Delivery mode and authority**: Der
  kopierbare `LocalImplementation`-Folgeprompt im historischen Intake ist eine
  Anforderungsnotiz und erteilt selbst keine Lieferrechte. Anforderungen
  duerfen weder Lieferautoritaet erteilen noch eine spaetere, separat
  validierte Autoritaet ersetzen. Fuer diesen konkreten Run nennt der aktuelle
  orchestratorverwaltete Zustand ausdruecklich `MergeAndSync`; diese separate
  Run-Autoritaet ist fuer spaetere zulaessige Phasen bindend, solange sie am
  jeweiligen Phasenrand unveraendert gueltig ist und alle Gates erfuellt sind.
  Fuer diesen Run ist zusaetzlich `Admin-Bypass` bereits ausdruecklich
  autorisiert, aber ausschliesslich innerhalb der Merge-Operation des
  Providers: Der exakte reviewte Head MUSS alle technischen Checks gruen
  haben, es darf keinen handlungsrelevanten Review-Thread geben, eine gueltige
  Schema-2.0-`PreMerge`-Evidenz MUSS vorliegen und `REVIEW_REQUIRED` MUSS der
  einzige verbleibende Policy-Blocker sein. Admin-Bypass DARF niemals ein
  fehlgeschlagenes, ausstehendes, fehlendes, veraltetes oder
  widerspruechliches technisches beziehungsweise Security-Gate umgehen und
  DARF keine Repository-Regel aendern. Dafuer ist in diesem Run keine weitere
  Autoritaetsanfrage erforderlich. Die Autoritaet erweitert weder den
  Feature-Scope noch Registry-, Secret-, formale Freigabe-,
  Plattformadministrations- oder Risikoakzeptanz-Autoritaet. Der
  Clarify-Auftrag erlaubt ungeachtet des
  spaeteren Delivery-Modus nur Spec-/Checklistenpflege und das Phasenergebnis,
  nicht Commit, Remote-Aktion oder Implementierung. / The copy-ready
  `LocalImplementation` follow-up prompt in the historical intake is a
  requirements note and grants no delivery rights by itself. Requirements may
  neither grant delivery authority nor replace later, separately validated
  authority. For this specific run, the current orchestrator-managed state
  explicitly declares `MergeAndSync`; that separate run authority is binding
  for later permitted phases while it remains valid at each phase boundary and
  every gate is satisfied. `Admin-Bypass` is also already explicitly
  authorized for this run, but only inside the provider merge operation: the
  exact reviewed head must have every technical check green, no actionable
  review thread, valid schema-2.0 `PreMerge` evidence, and `REVIEW_REQUIRED`
  as the sole remaining policy blocker. Admin-Bypass must never bypass a
  failed, pending, missing, stale, or contradictory technical/security gate
  and must not change repository rules. No further authority request is
  required for this run. This authority does not expand feature scope or grant
  registry, secret, formal-approval, platform-administration, or
  risk-acceptance authority. Regardless of the later delivery mode, the Clarify instruction
  permits only specification/checklist maintenance and the phase result, not a
  commit, remote action, or implementation.
- **AU-003 Stop und Wiederaufnahme / Stop and resume**: Ein bewusster Stop
  setzt einen sicheren Phasenrand und darf nicht durch implizite Fortsetzung
  umgangen werden. Nach unerwarteter Unterbrechung, Hash-, Branch-, Preset-,
  Governance- oder Scope-Drift ist eine vollstaendige Revalidierung und bei
  Bedarf ein ausdruecklicher Resume-Lauf erforderlich. / A deliberate stop sets
  a safe phase boundary and must not be bypassed by implicit continuation.
  Unexpected interruption or hash, branch, preset, governance, or scope drift
  requires full revalidation and, where needed, explicit resume.
- **AU-004 Mutable Tokens**: Feature-definierte veraenderliche
  Validierungstokens sind `N/A`; die akzeptierten Eingabehashes und spaeteren
  normalisierten Phasen-/Payload-Hashes sind unveraenderliche Evidenz. Trigger:
  Ein spaeterer Plan fuehrt zeit-, provider- oder plattformgebundene Tokens ein.
  / Feature-defined mutable validation tokens are `N/A`; accepted input hashes
  and later normalized phase/payload hashes are immutable evidence. Trigger: a
  later plan introduces time-, provider-, or platform-bound tokens.
- **AU-005 Causal Closeout**: `Applicable`, weil technische Haertung,
  Nutzerablauf, Sicherheitsstatus, A11Y, Plattformabdeckung und historische
  Gap-Evidenz veraendert werden. Der Abschluss MUSS Ursache, Aenderung,
  Verifikation, verbleibende offene Punkte und Folgeaktion verbinden. /
  `Applicable` because technical hardening, user workflow, security status,
  accessibility, platform coverage, and historical gap evidence change. The
  closeout MUST connect cause, change, verification, remaining open items, and
  follow-up.
- **AU-006 Retrospektive / Retrospective**: Wiederverwendbare Erkenntnisse
  duerfen erst nach validiertem Abschluss als Retrospektive vorgeschlagen
  werden. Provider-/Accountdetails, Geheimnisse und projektspezifische
  Risikofreigaben bleiben ausgeschlossen. / Reusable learning may be proposed
  only after validated completion. Provider/account details, secrets, and
  project-specific risk approvals remain excluded.

#### Stabile Akzeptanz-Gates / Stable Acceptance Gates

| Gate-ID | Zustand / State | Pflicht-Scope und Command-Token / Required scope and command token | Begruendung und Neubewertung / Rationale and re-evaluation |
|---|---|---|---|
| `GATE-SPEC-01` | Applicable | Sechs akzeptierte SHA-256-Bindungen erneut pruefen; Spec-Qualitaetscheck ohne offene Marker. / Re-check six accepted SHA-256 bindings; specification quality check with no open markers. | Verhindert Input-Drift. Erneut bei jeder Phase. / Prevents input drift. Repeat at each phase. |
| `GATE-GAP-01` | Applicable | `GAP-001`–`GAP-157` exakt einmal; Counts 157/108/49; Schema-/Gap-Validator aus dem spaeteren Plan. / Exact one-to-one gap coverage; later plan's schema/gap validator. | Kern der Baseline. Erneut nach jeder Gap-Evidenzaenderung. / Core baseline gate. Repeat after every gap evidence change. |
| `GATE-CONFIG-01` | Applicable | `podman-compose config`; optional zusaetzlich `podman compose config`, wenn der lokale Socket gesund ist. / `podman-compose config`; optionally also `podman compose config` when the local socket is healthy. | Statische Compose-Plausibilitaet. Bei jeder Compose-Aenderung. / Static Compose plausibility. Repeat for every Compose change. |
| `GATE-BUILD-01` | Applicable | `podman compose build --pull` oder die auf der Plattform verfuegbare gleichwertige Podman-Compose-Form. / Controlled final image build with the platform's available Podman Compose form. | Belegt reproduzierbare Buildbarkeit. Nach Dockerfile-/Abhaengigkeitsaenderung. / Proves reproducible buildability. Repeat after Dockerfile/dependency change. |
| `GATE-RUNTIME-01` | Applicable | Container starten; Rootless-, Rechte-, Mount-, Schreib-, Port-, Netzwerk- und Agentenzustandspruefung; danach geordnet stoppen. / Start container; verify rootless, privileges, mounts, writes, ports, network, and agent state; then stop cleanly. | Belegt Isolationswirkung. Bei Laufzeit-/Compose-Aenderung. / Proves isolation effect. Repeat on runtime/Compose change. |
| `GATE-SMOKE-01` | Applicable | Toolchain-/Agenten-Smoke-Test, einschliesslich des akzeptierten Tokens `podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh` oder eines spaeter dokumentierten gleichwertigen Paars. / Toolchain/agent smoke test including the accepted command token or a later documented equivalent pair. | Belegt Inventar in der Laufzeit. Bei Toolversion-/Installationsaenderung. / Proves runtime inventory. Repeat on tool version/install changes. |
| `GATE-SUPPLY-01` | Applicable | Finale lokale SBOM, Schwachstellenscan, VEX-Abgleich und lokale Provenienzpruefung; kein Registry-Push. / Final local SBOM, vulnerability scan, VEX reconciliation, and local provenance check; no registry push. | Belegt Lieferkettentransparenz. Fuer jedes finale Image. / Proves supply-chain transparency. Repeat for each final image. |
| `GATE-SECRET-01` | Applicable | `uvx pre-commit run --all-files` oder gepinnte gleichwertige lokale Secret-/Qualitaetspruefung; Trefferinhalte nicht protokollieren. / Pinned local secret/quality scan; do not log match contents. | Verhindert Secret-Leakage. Vor jedem Commit-/Delivery-Gate. / Prevents secret leakage. Repeat before each commit/delivery gate. |
| `GATE-XPLAT-01` | Applicable | Bash-/PowerShell-Paritaet, `--dry-run`/`-WhatIf`, Manpage, Hilfe sowie getrennte macOS-, Windows-Host- und Ubuntu/WSL2-Evidenz pruefen. / Verify Bash/PowerShell parity, dry-run/WhatIf, man page, help, and separate macOS, Windows-host, and Ubuntu/WSL2 evidence. | Ein Evidenzpfad allein reicht nicht. Windows-Host und Ubuntu/WSL2 duerfen dieselbe Hardware mit getrennten Laufzeiten nutzen. Bei jeder Skript- oder Scope-Aenderung neu pruefen. / One evidence path is insufficient. Windows host and Ubuntu/WSL2 may share hardware when runtimes are separate. Repeat for every script or scope change. |
| `GATE-A11Y-01` | Applicable | Bilinguale, CEFR-B2-, Text-first- und WCAG-2.2-AA-Pruefung der betroffenen Artefakte. / Bilingual, CEFR B2, text-first, and WCAG 2.2 AA review of affected artefacts. | Bindende Lernendenbasis. Bei jeder nutzerbezogenen Aenderung. / Binding learner baseline. Repeat for every user-facing change. |
| `GATE-HUMAN-01` | Applicable | 49 Human-only-Gaps bleiben offen, bis Rollenbeleg vorliegt; keine formale oder externe Aktion durch den Agenten. / 49 human-only gaps remain open until role evidence exists; no formal or external action by the agent. | Verhindert erfundene Freigaben. Erneut an jedem Phasenrand. / Prevents invented approvals. Repeat at every phase boundary. |
| `GATE-DIFF-01` | Applicable | `git diff --check`; geaenderte Pfade muessen Scope und Gap-ID zugeordnet sein. / `git diff --check`; changed paths must map to scope and gap ID. | Verhindert Nebenrefactorings und Whitespace-Fehler. Vor Delivery. / Prevents unrelated refactors and whitespace errors. Repeat before delivery. |

### Dokumentationswirkung / Documentation Impact

| Feld / Field | Entscheidung / Decision |
|---|---|
| Entscheidung / Decision | `UpdateRequired` |
| Zielgruppen / Audiences | Vier Ausbildungsberufe aus GR-001, Lernbegleitung, Entwicklung, Repository Maintenance, Security Review. / Four training occupations from GR-001, learning support, development, repository maintenance, Security Review. |
| Dokumentfamilien / Documentation families | README-/Bedienpfade, Build-/Compose-/Toolchain-Anleitungen, Security-/Architektur-/A11Y-Evidenz, Agenten-Guidance, Manpages, PowerShell-Hilfe, Troubleshooting und Abschlussnachweis. / README/operations paths, build/Compose/toolchain guidance, security/architecture/accessibility evidence, agent guidance, man pages, PowerShell help, troubleshooting, and closeout evidence. |
| Leserpfade / Reader paths | Einstieg→Voraussetzungen→Build→Start→Projekt-Mapping→Agenten/Toolchains→Sicherheitsgrenzen→Smoke-Test→SBOM/Scan→Fehlerbehebung→offene Human-only-Schritte. / Entry→prerequisites→build→start→project mapping→agents/toolchains→security boundaries→smoke test→SBOM/scan→troubleshooting→open human-only steps. |
| Kanonische Quelle und Owner / Canonical source and owner | Technische Wahrheit: versionierte Repository-Konfiguration; Feature-Wahrheit: diese Spec und 157-Gap-Evidenz; Owner: Repository Maintainer, Review: Security Review. / Technical truth: versioned repository configuration; feature truth: this spec and 157-gap evidence; owner: Repository Maintainer, reviewer: Security Review. |
| Navigation / Navigation impact | Bestehende Einstiegspfade MUESSEN neue oder aktualisierte Evidenz verlinken; keine verwaisten Sicherheitsdokumente. / Existing entry paths MUST link new or updated evidence; no orphaned security documents. |
| Dokumentklasse / Document class | Lern-, Bedien-, Governance-, Sicherheits-, Architektur- und Auditdokumentation. / Learning, operations, governance, security, architecture, and audit documentation. |
| Sprachstrategie und Partner / Language strategy and partner | Deutsch zuerst, Englisch danach inline; ein `.EN.md`-Partner nur bei begruendeter Lesbarkeitsverbesserung und synchroner Pflege. / German first, English second inline; `.EN.md` companion only with justified readability benefit and synchronized maintenance. |
| Plattform-/Beispielnachweis / Platform/example proof | Praktische Nachweise fuer macOS, den Windows-Host und Ubuntu/WSL2 mit eigener rootless-Podman-Laufzeit; fehlende Pfade als `Open`, niemals implizit bestanden. Native Linux-Hardware ist kein Akzeptanzziel dieses Features. / Practical evidence for macOS, the Windows host, and Ubuntu/WSL2 with its own rootless Podman runtime; missing paths remain `Open`, never implicitly passed. Native Linux hardware is not an acceptance target for this feature. |
| Distributionsklasse / Distribution class | Repository-lokale Dokumentation und lokales Image-Artefakt; keine Registry-, Paket- oder Hosting-Verteilung. / Repository-local documentation and local image artefact; no registry, package, or hosting distribution. |
| Home-Sync / Home sync need | `NoUpdateRequired` fuer rein projektspezifische Haertungsdetails; `UpdateRequired` nur, wenn eine gemeinsame Baseline-Regel geaendert wird. Owner: Repository Maintainer. Trigger: Aenderung an geteilter Guidance oder Vorlage. / `NoUpdateRequired` for project-specific hardening details; `UpdateRequired` only for a shared baseline-rule change. |
| Evidenz / Evidence | `docs/accessibility/`, `docs/architecture/`, `docs/security/`, betroffene Hilfe-/Manpage-Dateien und Abschluss-Gap-Matrix. / Accessibility, architecture, security, help/man-page files, and final gap matrix. |
| Neubewertung / Re-evaluation trigger | Jede Aenderung an Nutzerablauf, Plattformabdeckung, Mount/Port/Netzwerk, Agenten-/Toolchain-Inventar, Sicherheitsstatus, geteilter Guidance oder Distributionsscope. / Any change to user flow, platform coverage, mounts/ports/network, agent/toolchain inventory, security state, shared guidance, or distribution scope. |

### Schluesselentitaeten / Key Entities *(include if feature involves data)*

- **Akzeptiertes Artefakt / Accepted Artefact**: Unveraenderliche bindende
  Eingabe mit Repository-relativem Pfad und normalisiertem SHA-256. Eine
  Hash-Aenderung ist Input-Drift und blockiert die Fortsetzung. / Immutable
  binding input with repository-relative path and normalized SHA-256. A hash
  change is input drift and blocks continuation.
- **Gap-Disposition / Gap Disposition**: Aktueller Zustand genau eines der 157
  Gaps mit CL-ID, Anwendbarkeit, Umsetzungsstand, Begruendung, Evidenz, Owner,
  Reviewer, Restrisiko, Folgeaktion und Trigger. / Current state of exactly one
  of 157 gaps with CL ID, applicability, implementation state, rationale,
  evidence, owner, reviewer, residual risk, follow-up, and trigger.
- **Sandbox-Grenze / Sandbox Boundary**: Gepruefte Grenze fuer Host,
  Container, Mount, Schreibrecht, Netzwerk, Port, Agentenzustand oder
  Providerinteraktion mit Datenklasse und Kontrollziel. / Reviewed boundary for
  host, container, mount, write access, network, port, agent state, or provider
  interaction with data class and control objective.
- **Werkzeug-Inventareintrag / Tool Inventory Entry**: Erwartete und
  beobachtete Identitaet eines Toolchains, einer Skriptgrundlage, eines Agenten
  oder Hilfswerkzeugs samt Version, Herkunft, Smoke-Test und Limitierung. /
  Expected and observed identity of a toolchain, scripting foundation, agent,
  or supporting tool with version, provenance, smoke test, and limitation.
- **Verifikationsnachweis / Verification Evidence**: Datiertes Ergebnis eines
  reproduzierbaren Checks mit Befehl, Plattform, Scope, Exitcode, Ergebnis und
  bekannter Grenze, jedoch ohne Geheimnisse oder Sitzungsinhalte. / Dated result
  of a reproducible check with command, platform, scope, exit code, outcome, and
  known limitation, without secrets or session content.
- **Plattform-Scope-Entscheidung / Platform Scope Decision**: Datiertes,
  rollengebundenes Artefakt, das Akzeptanzumgebungen, getrennte Evidenzpfade,
  ausgeschlossene Aussagen und Neubewertungsausloeser festlegt. / Dated,
  role-bound artefact defining acceptance environments, separate evidence
  paths, excluded claims, and re-evaluation triggers.
- **Human-only-Uebergabe / Human-Only Handoff**: Offener Punkt mit Rolle,
  vorbereiteten Fakten, fehlender Entscheidung, Folgeaktion und
  Neubewertungsausloeser; niemals stellvertretende Freigabe. / Open item with
  role, prepared facts, missing decision, follow-up, and re-evaluation trigger;
  never proxy approval.

## Erfolgskriterien / Success Criteria *(mandatory)*

### Messbare Ergebnisse / Measurable Outcomes

- **SC-001**: `157/157` Gaps sind genau einmal dispositioniert; automatische
  Pruefung meldet `0` fehlende, `0` doppelte und `0` verwaiste Gap-IDs. /
  `157/157` gaps are dispositioned exactly once; automated verification reports
  `0` missing, `0` duplicate, and `0` orphan gap IDs.
- **SC-002**: Alle `108` nicht Human-only-Gaps haben aktuelle Evidenz fuer
  ihren ehrlichen Zustand. Jeder verbleibende offene Punkt besitzt Owner,
  fehlenden Nachweis, Folgeaktion und Trigger; `0` Restrisiken sind durch den
  Agenten als akzeptiert markiert. / All `108` non-human-only gaps have current
  evidence for their honest state. Every remaining open item has owner, missing
  evidence, follow-up, and trigger; `0` residual risks are marked accepted by
  the agent.
- **SC-003**: Alle `49` Human-only-Gaps bleiben ohne Rollenbeleg offen; die
  Abschlusspruefung findet `0` erfundene formale Freigaben, Secret-Aktionen,
  externe Registereintraege oder Plattformentscheidungen. / All `49`
  human-only gaps remain open without role evidence; closeout finds `0`
  invented approvals, secret actions, external register entries, or platform
  decisions.
- **SC-004**: Die finale lokale Compose-Konfiguration validiert ohne Fehler;
  das finale lokale Image baut und startet erfolgreich auf jeder fuer die
  Abnahme verfuegbaren Referenzplattform. Nicht verfuegbare Plattformen sind zu
  `100%` als offene Limitierung mit Trigger erfasst. / Final local Compose
  configuration validates without error; the final local image builds and
  starts successfully on every available reference platform. Unavailable
  platforms are recorded `100%` as open limitations with triggers.
- **SC-005**: `6/6` speichersichere Toolchain-Familien, `2/2`
  Skriptgrundlagen, `4/4` erforderliche Agenten-CLIs und `2/2` zusaetzliche
  Agentenoberflaechen bestehen Identitaets-/Versionspruefung sowie den
  vorgesehenen minimalen Smoke-Test im finalen lokalen Image. / All required
  toolchain, scripting, and agent groups pass identity/version and intended
  minimal smoke tests in the final local image.
- **SC-006**: Fuer das finale lokale Image existiert genau eine aktuelle,
  maschinenlesbare und der Image-Identitaet zugeordnete SBOM. `100%` der
  relevanten Scan-Funde besitzen VEX-Status oder einen expliziten offenen
  Blocker. / Exactly one current machine-readable SBOM linked to final image
  identity exists. `100%` of relevant scan findings have a VEX status or an
  explicit open blocker.
- **SC-007**: Secret- und Inhaltspruefungen finden `0` reale Geheimnisse,
  Provider-Anmeldedaten, Prompt-/Antworttexte oder private Endpunkte in allen
  geaenderten beziehungsweise erzeugten Repository-Artefakten. / Secret and
  content checks find `0` real secrets, provider credentials, prompt/response
  text, or private endpoints in all changed or generated repository artefacts.
- **SC-008**: `100%` der geaenderten nutzerbezogenen Dokumentationsabschnitte
  besitzen Deutsch-zuerst-/Englisch-danach-Inhalte, CEFR-B2-orientierte Sprache,
  erklaerte Erstbegriffe und vollstaendige textliche Status-, Abhaengigkeits-
  und Entscheidungsinformationen. / `100%` of changed user-facing documentation
  sections provide German-first/English-second content, CEFR-B2-oriented prose,
  first-use term explanations, and complete textual status, dependency, and
  decision information.
- **SC-009**: In einem moderierten Erstnutzungs-Test koennen mindestens `90%`
  der Teilnehmenden aus den vier Zielberufen ohne Spec-Kit-Vorerfahrung binnen
  `30 Minuten` den sicheren Startpfad, den aktuellen Verifikationsstatus und
  den naechsten offenen Human-only-Schritt korrekt bestimmen. / In a moderated
  first-use test, at least `90%` of participants from the four target
  occupations without prior Spec Kit experience can identify the safe startup
  path, current verification state, and next open human-only step within
  `30 minutes`.
- **SC-010**: Jede geaenderte Datei ist mindestens einer Anforderung und einer
  Gap-ID oder einer zwingenden Phasen-Evidenz zugeordnet; die Abschlusspruefung
  meldet `0` unabhaengige Refactorings und `0` Registry-/Hosting-Aktionen. /
  Every changed file maps to at least one requirement and gap ID or mandatory
  phase evidence; closeout reports `0` unrelated refactors and `0`
  registry/hosting actions.

## Annahmen / Assumptions

- Podman bleibt die Referenzlaufzeit; Docker-kompatible Endpunkte dienen nur
  Podman-gestuetzter lokaler Werkzeugkompatibilitaet. / Podman remains the
  reference runtime; Docker-compatible endpoints serve only Podman-backed local
  tool compatibility.
- Dieses Repository ist eine Entwicklungs- und Lern-Sandbox, keine
  produktive Cloud-, Web-, Mehrmandanten- oder Authentifizierungsplattform. /
  This repository is a development and learning sandbox, not a production
  cloud, web, multi-tenant, or authentication platform.
- Die 157-Gap-Liste ist vollstaendig fuer diese Feature-Baseline, aber sie
  bestimmt nicht vorab, welche Punkte technisch `Applicable` oder begruendet
  `N/A` sind. / The 157-gap list is complete for this feature baseline but does
  not pre-decide which items are technically `Applicable` or reasoned `N/A`.
- Eine dokumentierte offene Limitierung ist keine Risikoakzeptanz. Nur die
  benannte menschliche Rolle darf eine formale Freigabe oder Risikoakzeptanz
  erteilen. / A documented open limitation is not risk acceptance. Only the
  named human role may grant formal approval or accept risk.
- Plattformverfuegbarkeit kann waehrend der Implementierung variieren. Fuer
  Feature 003 ist Ubuntu unter WSL2 die Linux-Akzeptanzumgebung; ein separater
  nativer Linux-Rechner ist nicht erforderlich. Ein uebersprungener Check
  bleibt offen und wird niemals als bestanden gezaehlt. / Platform availability
  may vary during implementation. For Feature 003, Ubuntu under WSL2 is the
  Linux acceptance environment; a separate native Linux machine is not
  required. A skipped check remains open and is never counted as passed.
- Bestehende dokumentierte Lern- und Entwicklungsablaeufe bilden die
  Funktionsuntergrenze. Sicherheitskontrollen duerfen sie nur gemaess FR-020
  einschraenken. / Existing documented learning and development workflows form
  the functional minimum. Security controls may restrict them only under
  FR-020.
- Die Spezifikationsphase aendert weder Laufzeit, Image, Compose,
  Providerzustand noch externe Systeme. Sie plant oder implementiert keine
  Haertung. / The specification phase changes neither runtime, image, Compose,
  provider state, nor external systems. It does not plan or implement
  hardening.

## Nicht-Ziele / Non-Goals

- Kein Push oder keine Verteilung eines Images nach GHCR oder in eine andere
  Registry. / No image push or distribution to GHCR or another registry.
- Keine produktive Cloud-, Hosting-, SaaS-, PaaS-, IaaS- oder
  Mehrmandantenplattform. / No production cloud, hosting, SaaS, PaaS, IaaS, or
  multi-tenant platform.
- Keine formale Sandbox-, Provider-, Modell-, Rechts-, Datenschutz-,
  Telemetrie-, Netzwerk- oder Plattformfreigabe. / No formal sandbox,
  provider, model, legal, privacy, telemetry, network, or platform approval.
- Keine Rotation, Erzeugung, Offenlegung, Uebertragung oder operative Nutzung
  realer Secrets oder Schluessel. / No rotation, creation, disclosure,
  transfer, or operational use of real secrets or keys.
- Keine Eintraege in externe Risiko-, Datenschutz-, Dokumentenmanagement-,
  Softwarefreigabe- oder andere Managementsystem-Register. / No entries in
  external risk, privacy, document-management, software-approval, or other
  management-system registers.
- Keine nicht auf Gap, Anforderung oder zwingende Evidenz rueckverfolgbare
  Refactorings. / No refactors untraceable to a gap, requirement, or mandatory
  evidence.

## Naechste Phase / Next Phase

Nach erfolgreicher Validierung dieses Clarify-Ergebnisses ist die naechste
separate Phase `/speckit.checklist`. Diese Spezifikation plant oder
implementiert weiterhin nichts. / After successful validation of this Clarify
result, the next separate phase is `/speckit.checklist`. This specification
still performs neither planning nor implementation.
