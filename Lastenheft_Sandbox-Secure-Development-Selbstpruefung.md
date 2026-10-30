<!-- intake-authoring:begin -->
## Usability-Quellenabgleich 2026-10-27 / Usability Source Alignment

DE: Der Quellenabgleich in `docs/maintenance/usability-alignment-2026-10-27.md`
ordnet die drei bestehenden Lernendenpfade `docs/fuer-lernende/erste-schritte.md`,
`docs/fuer-lernende/troubleshooting.md` und `docs/fuer-lernende/alltag.md` ein.
Ein gewaehlter Einstieg ohne KI-Konto und sichere Recovery konkretisieren
den bestehenden Umfang. Fail-closed, Rootless/Non-root, Agentenregeln und
menschliche Gates bleiben verbindlich; keine Machine-Loeschung oder
Schutzumgehung als normale Hilfe. Der freiwillige betreute Pilot bleibt
nur geplant und Open. Quellenbindung beweist keine Usability oder Abnahme.
Ein neues unabhaengiges Vollreview ist erforderlich; alte Reviews sind ueberholt.

EN: The linked alignment binds the three existing learner paths for one
selected account-free start and safe recovery within the accepted scope.
Preserve fail-closed operation, rootless/non-root identity, agent rules and
human gates; no machine deletion or safeguard bypass as ordinary help.
The voluntary supervised pilot remains planned and Open. Source bindings
prove neither usability nor acceptance. A new independent full review is
required; previous reviews are superseded.

# Sandbox-Abnahme / Sandbox Acceptance Review

**Status:** ReadyForReview

**Zielgruppe / Audience:** Auszubildende, Lernbegleitung, Betrieb und unabhaengiges Review

**Lieferautoritaet / Delivery authority:** LocalImplementation

## Voraussetzungen und Begriffe / Prerequisites and Terms

**DE:** Ein Intake ist eine Anforderungsdatei vor einem Spec-Kit-Lauf; Spec Kit
ordnet Anforderungen, Planung und Aufgaben. Grundlegende Computer- und
Terminalbedienung genuegt; Container-, Sicherheits- oder Spec-Kit-Erfahrung
wird nicht vorausgesetzt. Die Zielgruppe ab dem ersten Ausbildungsjahr
umfasst Fachinformatiker*innen, IT-System-Elektroniker*innen und die beiden
kaufmaennischen IT-Ausbildungsberufe. LocalImplementation bedeutet lokale
Umsetzung ohne automatische Liefer- oder Plattformaenderungsautoritaet.

**EN:** An intake is a requirements file before a Spec Kit run; Spec Kit
organizes requirements, planning and tasks. Basic computer and terminal use
is sufficient; no container, security or Spec Kit experience is assumed.
The first-year audience includes IT specialists, IT systems electronics
technicians and both IT management training occupations. LocalImplementation
means local work without automatic delivery or platform-change authority.

**DE:** Podman betreibt Container (isolierte Arbeitsumgebungen); ein Image ist
deren Bauvorlage. Rootless bedeutet Betrieb ohne Administratorrechte;
Capabilities sind einzelne Linux-Rechte, Mounts eingebundene Verzeichnisse.
Eine CLI ist ein Kommandozeilenwerkzeug, eine Toolchain eine Gruppe von
Entwicklungswerkzeugen. LSP (Language Server Protocol) verbindet Editor und
Sprachwerkzeuge; SourceKit-LSP ist das entsprechende Swift-Werkzeug.
Ein Smoke-Test ist ein kleiner Funktionstest. Compose beschreibt und startet
Container gemeinsam; HTTP ist das Protokoll fuer Webzugriff. Eine SBOM
(Software Bill of Materials) listet Softwarebestandteile. DE-first/EN-second
bedeutet Deutsch vor Englisch, CEFR B2 bezeichnet eine mittlere sprachliche
Komplexitaet, WCAG 2.2 AA die anwendbare Barrierefreiheits-Pruefbasis.

**EN:** Podman runs containers (isolated work environments); an image is their
build template. Rootless operation needs no administrator privileges;
capabilities are individual Linux permissions and mounts connect directories.
A CLI is a command-line tool; a toolchain groups development tools. Language
Server Protocol (LSP) connects editors and language tools; SourceKit-LSP is
the Swift tool. A smoke test is a small functional check. Compose describes
and starts containers together; HTTP is the web access protocol. A Software
Bill of Materials (SBOM) lists software components. DE-first/EN-second means
German before English, CEFR B2 indicates moderate language complexity, and
WCAG 2.2 AA is the applicable accessibility review baseline.

## Dokumentations- und Versionsnachtrag 2026-10-25 / Documentation and Version Addendum

DE: Der [Dokumentationsabgleich](docs/maintenance/documentation-alignment-2026-10-25.md)
und die [Werkzeug-Nachpruefungen](docs/security/toolchain-followups-2026-10-25.md)
ergaenzen die vorhandene Pruefgrundlage. Sie binden die aktuelle Agent-Guidance,
nicht eine technische Gesamterledigung. AMD64-Abnahme, effektive OpenCode-2-
Kontrollen, sitzungsbezogene Auditabdeckung und Linux-Warnungsreproduktion
bleiben anhand der dort benannten Owner, Follow-ups und Trigger zu pruefen.
Reine Datenbank-Dateimetadaten ersetzen keinen Sitzungsnachweis. Der
[gemeinsame Lernweg](docs/fuer-lernende/lernwege.md) und die
[A11Y-Pruefgrenzen](docs/fuer-lernende/barrierefreiheit.md) konkretisieren
bestehende Zielgruppen- und Verstaendlichkeitsanforderungen. Die bisherigen
Kontroll-IDs, Akzeptanzbedingungen, Uebergaben und menschlichen Grenzen bleiben
erhalten; keine neue Freigabe und kein Produktstart.

EN: Documentation alignment and toolchain follow-ups supplement the existing
review basis. They bind current agent guidance, not overall technical
completion. AMD64 acceptance, effective OpenCode 2 controls, session-level
audit coverage and Linux warning reproduction remain subject to the listed
owners, follow-ups and triggers. Database file metadata is not session
evidence. The shared learning path and A11Y review boundaries clarify existing
audience and readability requirements. Preserve control IDs, acceptance
conditions, handoffs and human boundaries; no new approval or product start.

## Maven-Quellenabgleich 2026-10-25 / Maven Source Alignment

DE: Der [gezielte Quellenabgleich](docs/maintenance/maven-fallback-intake-alignment-2026-10-25.md) bindet den
offiziellen Apache-Archiv-Fallback und die historische Einordnung des
Impact-Registers. Maven-Version und feste SHA-512 bleiben unveraendert.
Isolierte Download-Fixtures sind keine Image- oder Plattformabnahme.
Anforderungen, Kontroll-IDs, Akzeptanzschwellen, Uebergaben und menschliche
Grenzen bleiben erhalten; Quellenpflege erteilt keine Startautoritaet.

EN: The targeted source alignment binds the official Apache archive fallback
and historical impact-register context. Maven version and committed SHA-512
remain unchanged. Isolated download fixtures grant no image or platform
acceptance. Preserve requirements, control IDs, acceptance thresholds,
handoffs and human boundaries; source maintenance grants no execution authority.

## Review-Korrektur 2026-10-25 / Review Correction

DE: Der [aktuelle Statusnachtrag](docs/maintenance/sandbox-current-state-2026-10-25.md)
ordnet REV-001 bis REV-003 zu. Fuer die spaetere unabhaengige Abnahme sind
Registry/Image-Versionskonsistenz, richtige Lernenden-Versionen und getrennte
historische/aktuelle Evidenz zu beachten. Alle vorhandenen Kontroll-IDs,
Akzeptanzschwellen, Uebergaben und menschlichen Grenzen bleiben unveraendert.
Ein lokaler ARM64-Erfolg ist keine AMD64-Abnahme oder Freigabe; korrigierte
Texte und Quellenbindungen ersetzen keine praktische Abnahme.

EN: The current status addendum maps REV-001 through REV-003. Later independent
acceptance must consider registry/image consistency, correct learner versions
and separate historical/current evidence. Existing control IDs, acceptance
thresholds, handoffs and human boundaries remain unchanged. Local ARM64
success grants no AMD64 acceptance or approval; corrected text/source bindings
do not replace practical acceptance.

## Zweck / Purpose

**DE:** Dieser Intake prueft die technisch gehaertete Sandbox unabhaengig auf
Sicherheit, Reproduzierbarkeit und praktische Arbeitsfaehigkeit. Eine
Abnahme bedeutet technische Evidenz, nicht die formale Freigabe durch eine
Organisation.

**EN:** This intake independently checks the technically hardened sandbox for
security, reproducibility, and practical usability. Acceptance means technical
evidence, not formal approval by an organization.

## Aktualisierte Pruefgrundlage / Updated Review Baseline

**DE:** GSDB (generische Secure-Development-Basis) 3.4.4 mit 157 stabilen
Kontroll-IDs und Assurance 0.1.8 aus dem Preset-Abgleich vom 2026-10-24
(PR #99) sind die aktuelle Grundlage; die GSDB selbst ist unveraendert.
Assurance ist ein versioniertes Spec-Kit-Regel-/Werkzeugpaket fuer
Kontrollnachweise. Die historische GSDB-Pruefung bleibt unveraendert;
der [Delta-Abgleich](docs/maintenance/intake-gsdb344-delta-2026-10-21.md)
ergaenzt ihre 50 geaenderten Kontrolltexte durch die Gruppen G01-G10.
H bezeichnet das vorgelagerte Hardening, A diese unabhaengige Abnahme und L
den spaeteren Lernenden-Selbstbau. Ein erfolgreicher Quellenrollout und die
historische Feature-003-Studie sind keine aktuelle Sandbox-Abnahme.

**EN:** GSDB (generic Secure Development Baseline) 3.4.4 with 157 stable
control IDs and Assurance 0.1.8 from the 2026-10-24 preset alignment
(PR #99) are the current baseline; GSDB itself is unchanged.
Assurance is a versioned Spec Kit rule/tool package for control evidence.
The historical assessment remains unchanged; the linked delta alignment
maps 50 changed control texts to groups G01-G10. H is preceding hardening,
A this independent acceptance and L later learner self-build. Successful
source rollout and the historical Feature 003 study do not establish current
sandbox acceptance.

**DE:** Zusätzlich gilt der [Quellenabgleich vom 2026-10-25](docs/maintenance/intake-sources-alignment-2026-10-25.md).
Er erneuert die Werkzeug-/Guidance-Bindung, nicht die 50 Kontrollentscheidungen
oder deren Erfüllung. Ältere Assurance-Versionen im Delta-Bericht bleiben
historisch; für A-344-02 ist 0.1.8 maßgeblich. Neue Leserhilfen sind kein
bestandener Test. A-344-01 bis A-344-04 und ihre Grenzwerte bleiben erhalten.

**EN:** The linked 2026-10-25 source alignment also applies. It refreshes tool
and guidance bindings, not the 50 control decisions or their fulfillment.
Older Assurance versions in the delta report remain historical; A-344-02
uses 0.1.8. New reader help is not passed test evidence. A-344-01 through
A-344-04 and their thresholds remain unchanged.

## Ausgangslage und Zielbild / Current and Target State

**DE:** Zum Start dieser Abnahme müssen sowohl die technische Härtung als auch
der gemeinsame Feature-Update-Block aus
`Lastenheft_Sandbox-Feature-Update-Ubuntu2604-OpenCode-Web-MSL.md` abgeschlossen
sein. Beide Übergaben müssen auf dieselbe finale Quellrevision und das daraus
erzeugte lokale Update-Image mit genauer Image-ID bezogen sein. Nachweise
anderer Profile oder Architekturen dürfen nicht stillschweigend übertragen
werden. Die Abnahme wiederholt statische
und praktische Pruefungen aus Sicht von Lernenden und Reviewenden.

**EN:** Before this acceptance starts, both technical hardening and the combined
feature-update block named above must be complete. Both handoffs must bind the
same final source revision and resulting local update image with its exact
image ID. Do not silently transfer evidence across profiles or architectures.
Acceptance repeats static and practical checks from learner
and reviewer perspectives.

## Scope

- Rootless-Isolation, Capabilities, Mounts, Schreib- und Netzwerkgrenzen.
- OpenCode, Codex, Claude Code, Antigravity CLI und GitHub Copilot CLI.
- Die im Dockerfile und Smoke-Test tatsaechlich installierten
  Toolchain-Familien, einschliesslich Swift.
- VS-Code-Verbindung, SourceKit-LSP und dokumentierte Projekt-Mappings.
- Image-Build, Compose-Start, praktische Projekt-Smoke-Tests und HTTP-Zugriff.
- SBOM-Erzeugung sowie Konsistenz der Security-Evidenz.
- Lernbarkeit, DE-first/EN-second, CEFR B2 und WCAG 2.2 AA.

**EN:**
- Rootless isolation, capabilities, mounts, write and network boundaries.
- OpenCode, Codex, Claude Code, Antigravity CLI and GitHub Copilot CLI.
- Toolchain families actually installed by the Dockerfile and smoke test, including Swift.
- VS Code connection, SourceKit-LSP and documented project mappings.
- Image build, Compose startup, small project functional checks and HTTP access.
- SBOM generation and consistency of security evidence.
- Learnability, German-first/English-second, CEFR B2 and WCAG 2.2 AA.

## Nicht-Ziele / Non-Goals

- Keine weitere Haertung waehrend der unabhaengigen Abnahme.
- Keine Ausweitung auf nur geplante oder nicht installierte Sprachen.
- Keine Anmeldung mit echten Provider-Secrets als Abnahmevoraussetzung.
- Keine formale Sandbox-, Rechts-, Provider- oder Modellfreigabe.

**EN:**
- No further hardening during independent acceptance.
- No extension to planned but uninstalled languages.
- No sign-in with actual provider credentials as an acceptance prerequisite.
- No formal sandbox, legal, provider or model approval.

## Anforderungen / Requirements

1. Jede Pruefung nennt Befehl, erwartetes Ergebnis und Evidenzpfad.
2. Toolchain- und Agentenstatus werden aus Build- und Laufzeitquellen abgeleitet.
3. Fehler werden als Befund an die technische Haertung zurueckgegeben.
4. Plattformabdeckung wird ehrlich als geprueft, uebersprungen oder offen
   dokumentiert.
5. Sicherheitsrestriktionen und Lernablauf werden gemeinsam bewertet.
6. Keine positive Bewertung darf allein auf Dokumentation ohne praktischen
   Nachweis beruhen, wenn ein lokaler Check moeglich ist.

**EN:**
1. Every check names its command, expected result and evidence path.
2. Toolchain and agent status derive from build and runtime sources.
3. Failures return to technical hardening as findings.
4. Platform coverage is honestly recorded as checked, skipped or Open.
5. Security controls and learning flow are evaluated together.
6. Documentation alone cannot justify a positive result when a practical local check is possible.

## Delta-Anforderungen und Abnahme / Delta Requirements and Acceptance

- **A-344-01:** Die vollstaendige H-Uebergabe gegen historische Befunde und
  alle 50 Delta-IDs unabhaengig pruefen: H-344-01 bis H-344-10 und
  AC-H-344-01 bis AC-H-344-10, Quellenfassung, Anwendbarkeit, Erfuellung,
  Evidenzpfad und offene Punkte. / Independently review the complete H
  handoff against historical findings and all 50 delta IDs, including all
  ten H requirements/acceptance criteria, source version, applicability,
  implementation, evidence paths and Open items.
- **A-344-02:** Assurance 0.1.8 mit Bash und PowerShell auf exakte eindeutige
  aktive Versionen, Checklisten-Dokument-IDs und Sammelband-Baseline pruefen,
  einschliesslich deutscher und englischer Richtlinienmetadaten. Ein korrekt
  gehashter falscher aktiver Wert muss scheitern; eingebettete Checklisten
  behalten ihre eigene Baseline. / Check exact unique active metadata with
  both Assurance shells, including both guideline languages. A wrong active
  value must fail even with a valid hash; embedded checklists retain their
  own baseline.
- **A-344-03:** Anwendbarkeit und technische Umsetzung getrennt bewerten;
  N/A braucht Begruendung und Not Assessed, Unsicherheit bleibt Open mit
  Owner, Follow-up und Trigger. Pass/Fail ist nur das Ergebnis eines
  einzelnen Checks, keine formale Freigabe. Menschliche Rechts-, Datenschutz-,
  Provider-/Modell- oder Betriebsentscheidungen nur als reale Evidenz oder
  Open referenzieren; weder Scan noch SBOM ersetzen sie. / Separate
  applicability from implementation. N/A requires a reason and Not Assessed;
  uncertainty stays Open with owner, follow-up and trigger. Pass/Fail is a
  check result, not formal approval. Reference human legal, privacy,
  provider/model or operational decisions as real evidence or Open; scans
  and SBOMs do not replace them.
- **A-344-04:** Prüfende dürfen die jeweils abzunehmenden Hardening- oder
  Feature-Update-Anteile nicht selbst implementiert haben. Die
  Verantwortungszuordnung muss diese Unabhängigkeit je geprüftem Anteil
  nachvollziehbar belegen. Ergebnisse an konkreten Git-Stand, Plattform, Architektur,
  Image-ID, Zeitpunkt und Pruefbefehle binden. Fehler an H zurueckgeben;
  L bleibt bis erfolgreicher technischer Abnahme blockiert. / Reviewers must
  not accept hardening or feature-update portions they implemented themselves.
  Record reviewer responsibility and independence for each accepted portion.
  Bind results to exact Git
  revision, platform, architecture, image ID, time and commands. Return
  defects to H; L stays blocked until successful technical acceptance.

- **AC-A-344-01:** Ein Abnahmebericht enthaelt 50 eindeutige Delta-Zeilen
  samt H-Verweis und beurteilt auch AlreadyCovered-/N/A-Begruendungen.
  Fehlende oder unbrauchbare Evidenz ergibt kein Pass. / Acceptance report
  contains 50 unique delta rows linked to H and reviews AlreadyCovered/N/A
  rationales. Missing or unusable evidence cannot receive Pass.
- **AC-A-344-02:** Beide Shells akzeptieren den aktuellen Metadatenbestand;
  temporaere manipulierte Fixtures (Pruefdateien) mit erneuerten Hashes
  werden mit Exit 2 und Pfad/Feld-Diagnose abgelehnt. Produktivquellen und
  historische Nachweise bleiben bytegleich. / Both shells accept current
  metadata and reject temporary tampered fixtures with refreshed hashes,
  exit 2 and path/field diagnostics. Real sources and historical evidence
  remain byte-identical.
- **AC-A-344-03:** Bericht trennt Quellenvalidierung, technische Bewertung
  und menschliche Entscheidungen. Offene oder fehlgeschlagene anwendbare
  Abnahmekontrollen verhindern einen positiven Gesamtabschluss; menschliche
  Entscheidungen werden nicht automatisch geschlossen. / Report separates
  source validation, technical assessment and human decisions. Open or
  failed applicable acceptance controls prevent positive overall closure;
  human decisions are not closed automatically.
- **AC-A-344-04:** Reviewer-Identitaet und genaue Testumgebung sind
  dokumentiert; eine textorientierte Uebergabe nennt Befunde, gesperrte
  Nutzung/Weitergabe und den naechsten erlaubten Schritt fuer L oder H.
  Ein ARM64-Erfolg belegt keinen AMD64-Test. / Reviewer identity and exact
  environment are recorded; text-first handoff identifies defects, blocked
  usage/distribution and the next permitted L or H action. ARM64 success
  does not establish AMD64 testing.

**DE:** Offene Uebergaben O-344-TECH, O-344-HUMAN und O-344-CLOUD aus dem
Delta-Abgleich bleiben mit Owner, Follow-up und Trigger verbindlich. Die
Plattformabdeckung wird nicht durch CI-Runner oder diese Intake-Pflege
erweitert; fehlende Zielsysteme bleiben Open/Skipped mit Grund.

**EN:** Open handoffs O-344-TECH, O-344-HUMAN and O-344-CLOUD retain their
owners, follow-up and triggers. CI runners and intake maintenance do not
expand platform acceptance; missing target systems stay Open/Skipped with
a reason.

## IR801: Verbindliche Update-Übergabe / Binding Update Handoff

**DE:** Dieser Zusatz setzt ausschließlich den am 30.10.2026 ausdrücklich
bestätigten Reparaturvertrag um. Die bisherigen A-344- und AC-A-344-Kriterien
bleiben erhalten. H bezeichnet das Container-Hardening, U den gemeinsamen
Ubuntu-/OpenCode-Web-/MSL-Update-Block, A diese unabhängige Abnahme und L den
nachfolgenden Lernenden-Selbstbau. Der folgende Vertrag übernimmt die
vorhandenen FU-001–023 und FA-001–012 aus U, ohne neue Produktfunktionen,
Grenzwerte, Risikofreigaben oder Ausführungsrechte zu erfinden.

**EN:** This addition implements only the repair contract explicitly approved
on 2026-10-30. Existing A-344 and AC-A-344 criteria remain binding. H means
container hardening, U the combined Ubuntu/OpenCode Web/MSL update, A this
independent acceptance and L subsequent learner self-build. Consume U's
existing FU-001–023 and FA-001–012 without inventing new features, thresholds,
risk acceptance or execution authority.

- **A-FU-01:** Beide abgeschlossenen Vorgängerübergaben, die finale gemeinsame
  Quellrevision und die Image-ID pro geprüftem Profil und Architektur MÜSSEN
  im Abnahmebericht ausdrücklich gebunden sein. Historische Build-/H-Nachweise
  sind Ausgangsquellen, kein automatischer Nachweis für das neue U-Image. /
  Explicitly bind both completed predecessor handoffs, the common final source
  revision and image ID for each reviewed profile/architecture. Historical
  build/hardening evidence is input, not automatic acceptance of U's new image.
- **A-FU-02:** Eine vollständige Zuordnung aller FU-/FA-IDs zu Prüfzuständigkeit
  und Evidence MUSS bestehen. Die unabhängige Gegenprüfung umfasst
  risikobasiert die folgende Matrix. Jede übernommene U-Evidence braucht
  Prüfumfang, Herkunft, passende Image-/Quellbindung und nachvollziehbare
  Begründung; eigene Wiederholungen und Übernahmen bleiben unterscheidbar.
  Keine automatische Verdopplung aller Tests. / Map every FU/FA ID to review
  responsibility and evidence. Use the risk-based independent checks below.
  Evidence reuse needs scope, provenance, matching image/source identity and
  a reason; distinguish reuse from independently repeated checks. Do not
  mechanically duplicate every test.

| Prüfgruppe / Check group | Verbindlicher unabhängiger Prüfauftrag / Binding independent check | U-Vertrag / U contract |
|---|---|---|
| Basis und Ausgaben / Base and outputs | Finale OS-/Versions-/Architekturidentität und .NET-Ausgabepfade gegen U-Nachweise prüfen; positive/negative Kollisions- und Guardfälle bewerten. / Check final OS/version/architecture and .NET outputs against U evidence; assess positive/negative collision and guard cases. | FU-001–006, FA-001–002/009 |
| Web und Readiness / Web and readiness | Authentifizierten Zugriff und Ablehnung ungültiger Anmeldung unabhängig gegenprüfen; Passwort-Negativfälle, frühen 401, begrenzte 503-/Verbindungsfehler-Wiederholung, Fristfehler, Secretfreiheit und Loopback-Portgrenze anhand der U-Kriterien prüfen. / Independently countercheck authenticated access and invalid-login rejection; check password negatives, early 401, bounded 503/connection retries, timeout failure, secret safety and loopback boundary against U criteria. | FU-007–009/011, FA-005 |
| Gemeinsame Clients / Shared clients | Browser-Anmeldung sowie TUI-/CLI-Zuordnung zum selben Server und Testprojekt unabhängig prüfen; Sitzungen/Forks und Parallelitätsgrenzen belegen, ohne echte Provider-Secrets oder Inferenz. / Independently verify browser login and TUI/CLI mapping to the same server/project; evidence session/fork/concurrency limits without real provider secrets or inference. | FU-010, FA-006 |
| Profile und Plattformen / Profiles and platforms | Alle sieben Profil-/Architekturbelege für native AMD64/ARM64-Prüfungen bewerten; positive/negative Werkzeugauswahl, ungültige Profile, Wrapper-Parität und SkipBuild-Abweichungen prüfen. Keine Plattform aus Emulation oder CI-Runnernamen ableiten. / Assess all seven profiles' native AMD64/ARM64 evidence; check positive/negative tool selection, invalid profiles, wrapper parity and SkipBuild mismatches. Infer no platform proof from emulation or runner names. | FU-012–018, FA-003–004/009–010 |
| Sicherheit, Audit und Daten / Security, audit and data | Fortbestehende H-Kontrollen auf dem finalen U-Image prüfen; Non-root, CapEff=0, NoNewPrivs=1, Seccomp/innere Policies, Datenpersistenz und auditgesicherten Stop einschließlich Exportfehler-Sperre gegenprüfen. / Check retained H controls on the final U image; countercheck non-root, CapEff=0, NoNewPrivs=1, Seccomp/inner policies, persistence and audited stop including export-failure blocking. | FU-019–020, FA-007–008 |
| Lernendenpfade und Gesamtbindung / Learner paths and integrated binding | DE/EN, sichere Fehlerhilfe, anwendbare A11Y- und Regressionsnachweise sowie gemeinsamen finalen Quellstand aller drei Issues prüfen. / Review DE/EN, safe recovery, applicable accessibility/regression evidence and the shared final revision for all three issues. | FU-021–023, FA-011–012 |

- **AC-A-FU-01:** Der Bericht enthält eine vollständige FU-/FA-Zuordnung mit
  Check-ID, Ergebnis, Reviewer, Anteil/Unabhängigkeit, Datum, Profil,
  Host-/Engine-/Ziel-/Image-Architektur, Image-ID, Quellrevision und Evidencepfad.
  Eigenprüfungen nennen Befehl und erwartetes/tatsächliches Ergebnis; Übernahmen
  nennen Quelle und Begründung. / Record full FU/FA coverage, check ID, result,
  reviewer/portion/independence, date, profile, host/engine/target/image
  architecture, image ID, source revision and evidence. Repeated checks name
  commands and expected/actual outcomes; reuse names source and reason.
- **AC-A-FU-02:** Offene, fehlgeschlagene oder nicht passend gebundene
  anwendbare Prüfungen verhindern einen positiven Gesamtabschluss. Fehlende
  native oder menschliche Nachweise bleiben Open/Blocked mit Owner,
  Folgeaktion und Trigger. Bestehende Grenzwerte und Human-only-Gates werden
  nicht ersetzt. L bleibt bis erfolgreicher unabhängiger Abnahme blockiert. /
  Open, failed or incorrectly bound applicable checks block positive overall
  closure. Missing native/human evidence stays Open/Blocked with owner,
  follow-up and trigger. Preserve existing thresholds and human-only gates;
  L remains blocked until successful independent acceptance.

## Abhaengigkeiten und Risiken / Dependencies and Risks

**DE:** Technisches Sandbox-Hardening und der vollständige Feature-Update-Block
müssen abgeschlossen und nach A-FU-01 gemeinsam gebunden sein. Lokale
Podman-, Netzwerk- oder Plattformausfaelle werden von Repository-Fehlern
getrennt dokumentiert. Nur auf macOS ausgefuehrte Checks belegen keine
vollstaendige Windows- oder Linux-Abdeckung.

**EN:** Both technical hardening and the full feature-update block must be
complete and jointly bound under A-FU-01. Local Podman, network, or
platform failures are recorded separately from repository failures. Checks run
only on macOS do not prove full Windows or Linux coverage.

## Erwartete Artefakte und Evidenz / Expected Artefacts and Evidence

- Abnahmeprotokoll mit Pass, Fail, Open oder N/A je Pruefung.
- Toolchain-, Agenten-, Mount- und VS-Code-Matrix.
- Finale lokale SBOM und reproduzierbare Pruefbefehle.
- Rueckgabe konkreter Befunde an die Haertungsstufe.

**EN:**
- Acceptance record with Pass, Fail, Open or N/A (not applicable) for each check.
- Toolchain, agent, mount and VS Code matrix.
- Final local SBOM and reproducible check commands.
- Concrete findings returned to the hardening stage.

## Akzeptanzkriterien / Acceptance Criteria

- Compose-Konfiguration, Image-Build und Containerstart sind nachweisbar.
- Alle installierten Agenten und Toolchain-Familien bestehen die vorgesehenen
  Versions- und Projekt-Smoke-Tests.
- VS Code kann gemaess Dokumentation an den Container anbinden.
- Mounts zeigen auf die dokumentierten Containerpfade.
- SBOM-Erzeugung ist erfolgreich oder ein konkreter externer Blocker ist
  dokumentiert.
- Die Selbstbau-Vorlage wird erst nach erfolgreicher technischer Abnahme
  freigegeben.

**EN:**
- Compose configuration, image build and container startup are evidenced.
- All installed agents and toolchain families pass the planned version and project smoke tests.
- VS Code can attach to the container as documented.
- Mounts point to the documented container paths.
- SBOM generation succeeds or a concrete external blocker is documented.
- The self-build template is released only after successful technical acceptance.

## Annahmen und offene Fragen / Assumptions and Open Questions

- Provider-Anmeldungen sind fuer Versions- und Konfigurationschecks nicht
  erforderlich.
- Es bestehen keine offenen Intake-Authoring-Fragen.

**EN:**
- Provider sign-in is not required for version and configuration checks.
- No intake-authoring questions remain Open.

## Template-Quellenabgleich 2026-10-25 / Template Source Alignment

DE: Der [Tagesabschluss-Rechteabgleich](docs/maintenance/closeout-rights-alignment-2026-10-25.md)
bindet die ausdrückliche Ownerbestätigung nur für die benannte neue Workshop-/
Lernmaterial-Lieferung. LIC-01 und andere LIC-02-Betroffenheiten bleiben offen.
Keine Änderung von Kontrollanforderungen, Akzeptanzschwellen, Lifecycle oder
Startautorität; insbesondere keine Template- oder Sandboxfreigabe.

EN: The linked closeout rights alignment binds explicit owner confirmation
only for the named new workshop/learning delivery. LIC-01 and other LIC-02
concerns remain Open. Controls, acceptance thresholds, lifecycle and start
authority are unchanged; no template or sandbox approval is granted.

**DE:** [Template-Abgleich](docs/maintenance/template-profile-alignment-2026-10-25.md)
bindet das optionale Profil, Lizenzgrenzen und die CI-Trennung historischer
Referenzevidenz. Fork bleibt Standard; Template ist vorbereitet, nicht aktiviert.
Keine kopierten Run-States, Statistiken oder Freigaben als persönliche Nachweise
verwenden. Hardening-/Abnahme-Gates und bestehende Akzeptanzschwellen bleiben
unverändert. Diese Quellenpflege startet weder Produktarbeit noch die blockierte
Selbstbau-Stufe und führt keine Hosting-Einstellung aus.

**EN:** The template alignment binds the optional profile, rights boundaries
and source-only historical CI evidence. Fork remains default; template use is
prepared, not enabled. Copied states/statistics/approvals are not personal
evidence. Preserve hardening/acceptance gates and thresholds. Source maintenance
starts no product or blocked self-build work and changes no hosting setting.

<!-- intake-authoring:prompts -->
## Kopierbare Folgekommandos / Copy-Ready Follow-Up Commands

<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Erstelle eine Spezifikation auf Grundlage von Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md, docs/maintenance/intake-gsdb344-delta-2026-10-21.md und der vollstaendigen Hardening-Uebergabe. Beruecksichtige A-344-01 bis A-344-04 und deren Akzeptanzkriterien sowie GSDB 3.4.4 und Assurance 0.1.8. Plane unabhaengige technische Abnahme ohne weitere Haertung oder formale Freigabe; keine Implementierung starten. Beruecksichtige den Dokumentations- und Versionsnachtrag vom 2026-10-25 sowie docs/maintenance/documentation-alignment-2026-10-25.md und docs/security/toolchain-followups-2026-10-25.md; offene Nachweise nicht als erledigt behandeln. Aktuellen Statusnachtrag docs/maintenance/sandbox-current-state-2026-10-25.md mit REV-001 bis REV-003 beruecksichtigen; technische und menschliche Nachweise nicht vorwegnehmen. Beruecksichtige docs/maintenance/maven-fallback-intake-alignment-2026-10-25.md; isolierte Downloadtests sind kein Image-Build oder neue Abnahme. Beruecksichtige docs/maintenance/template-profile-alignment-2026-10-25.md und die neuen Rechte-/Historiengrenzen; Fork bleibt Standard, Template ist nicht aktiviert, bestehende Lifecycle- und Startgates bleiben erhalten. Beruecksichtige docs/maintenance/closeout-rights-alignment-2026-10-25.md: Ownerrechte nur fuer die benannte Lernmaterial-Lieferung bestaetigt; LIC-01 und andere LIC-02-Betroffenheiten sowie saemtliche Startgates bleiben offen. Beruecksichtige docs/maintenance/closeout-review-remediation-2026-10-25.md: IR201/IR202 nur als nachreviewte Quellenkorrektur behandeln; Lifecycle und Startautoritaet bleiben unveraendert. Beruecksichtige docs/maintenance/usability-alignment-2026-10-27.md und die dort benannten drei Lernendenpfade: begrenzte Usability-Konkretisierung ohne Scope-Ausweitung, Schutzlockerung, Pilot-Ausfuehrung oder neue Startautoritaet; unabhaengiges Vollreview erforderlich.
Zusätzliche verbindliche Eingabe ist Lastenheft_Sandbox-Feature-Update-Ubuntu2604-OpenCode-Web-MSL.md mit FU-001–023 und FA-001–012. Übernimm beide abgeschlossenen Vorgänger und dieselbe finale Quellrevision/Image-ID nach A-FU-01/02 und AC-A-FU-01/02; plane risikobasierte unabhängige positive/negative Gegenprüfungen und begründete Evidenceübernahmen statt pauschaler Testverdopplung. Niemand darf die jeweils selbst implementierten Hardening- oder Update-Anteile abnehmen. Bestehende Schwellen, Graph- und Human-only-Gates bleiben erhalten; dieser Specify-Auftrag startet keine technische Abnahme oder Implementierung.
```

<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Fuehre erst nach abgeschlossener Haertung, aktuellem Review und gesonderter Startautoritaet den vollstaendigen Spec-Kit-Lauf fuer Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md mit Delivery Authority LocalImplementation aus. Pruefe den GSDB-3.4.4-Delta-Abgleich und Assurance 0.1.8 unabhaengig, dokumentiere Plattformgrenzen und offene menschliche Entscheidungen und stoppe vor Commit, Push, Pull Request, Merge oder Hosting-Aenderungen. Beruecksichtige den Dokumentations- und Versionsnachtrag vom 2026-10-25 sowie docs/maintenance/documentation-alignment-2026-10-25.md und docs/security/toolchain-followups-2026-10-25.md; offene Nachweise nicht als erledigt behandeln. Aktuellen Statusnachtrag docs/maintenance/sandbox-current-state-2026-10-25.md mit REV-001 bis REV-003 beruecksichtigen; technische und menschliche Nachweise nicht vorwegnehmen. Beruecksichtige docs/maintenance/maven-fallback-intake-alignment-2026-10-25.md; isolierte Downloadtests sind kein Image-Build oder neue Abnahme. Beruecksichtige docs/maintenance/template-profile-alignment-2026-10-25.md und die neuen Rechte-/Historiengrenzen; Fork bleibt Standard, Template ist nicht aktiviert, bestehende Lifecycle- und Startgates bleiben erhalten. Beruecksichtige docs/maintenance/closeout-rights-alignment-2026-10-25.md: Ownerrechte nur fuer die benannte Lernmaterial-Lieferung bestaetigt; LIC-01 und andere LIC-02-Betroffenheiten sowie saemtliche Startgates bleiben offen. Beruecksichtige docs/maintenance/closeout-review-remediation-2026-10-25.md: IR201/IR202 nur als nachreviewte Quellenkorrektur behandeln; Lifecycle und Startautoritaet bleiben unveraendert. Beruecksichtige docs/maintenance/usability-alignment-2026-10-27.md und die dort benannten drei Lernendenpfade: begrenzte Usability-Konkretisierung ohne Scope-Ausweitung, Schutzlockerung, Pilot-Ausfuehrung oder neue Startautoritaet; unabhaengiges Vollreview erforderlich.
Zusätzlich vor jedem Start müssen Hardening UND Lastenheft_Sandbox-Feature-Update-Ubuntu2604-OpenCode-Web-MSL.md abgeschlossen und auf dieselbe finale Quellrevision/Image-ID gebunden sein. Prüfe FU-001–023/FA-001–012 nach A-FU-01/02 und AC-A-FU-01/02 risikobasiert unabhängig, einschließlich Web-Anmeldung/Readiness, Clients, Profilen und erhaltener Security-/Auditkontrollen. Übernommene Evidence begründen; keine pauschale Testverdopplung. Keine Selbstabnahme eigener Hardening-/Update-Anteile, keine Änderung bestehender Schwellen oder Human-only-Gates. Dieser Prompt ist keine Startfreigabe.
```
<!-- intake-authoring:end -->
