# Requirements Quality Checklist: Sandbox-Härtungsnachlauf / Sandbox Hardening Follow-Up

**Purpose**: Klarheit, Vollständigkeit, Konsistenz und Messbarkeit der Anforderungen vor der Task-Erstellung / requirement quality before task generation.
**Created**: 2026-10-27
**Feature**: [spec.md](../spec.md)
**Context**: [plan.md](../plan.md), [research.md](../research.md), [data-model.md](../data-model.md), [coverage-scope.md](../coverage-scope.md), [quickstart.md](../quickstart.md), [CLI-Vertrag](../contracts/cli.md).
**Audience/Depth**: fachlicher Reviewer, risikoorientierte Standardtiefe / substantive reviewer, risk-focused standard depth.
**Reviewed**: 2026-10-27, 36/36 textuell erfüllt nach Korrekturen / text-quality pass after remediation; [Einzelbewertungen](requirements-quality-review.md).

DE: Zielgruppe ab dem ersten Ausbildungsjahr: Fachinformatiker*innen in den
vier Fachrichtungen Anwendungsentwicklung, Systemintegration, Daten- und
Prozessanalyse sowie Digitale Vernetzung; IT-System-Elektroniker*innen;
Kaufleute für IT-System-Management und Kaufleute für Digitalisierungsmanagement.
Auch Entwicklung ohne Spezialkenntnisse ist eingeschlossen. Die Fachrichtungen
sind mit ihren unterschiedlichen Lern- und Nutzungspfaden zu berücksichtigen,
nicht pauschal mit Softwareentwicklung gleichzusetzen.
EN: The audience starts in the first training year: IT specialists in all
four tracks—application development, systems integration, data and process
analysis, and digital networking—plus IT systems electronics technicians,
IT systems management clerks and digitalization management clerks.
Non-specialist developers are also included. Consider each track's learning
and usage needs rather than treating every track as software development.

DE: Diese Liste ist ein Satz Qualitätsfragen an die geschriebenen Anforderungen,
keine Implementierungs- oder Freigabeprüfung. Alle Punkte waren bei Erstellung
offen; der aktuelle Textreview ist separat protokolliert. Eine Durchführungsanweisung benennt die zu lesenden Stellen und das
Merkmal einer ausreichenden Anforderung; sie verlangt keine Shellbefehle,
Tests, Builds oder Containeraktionen. `[Gap]`, `[Ambiguity]` und `[Conflict]`
kennzeichnen den Prüffokus, nicht bereits bestätigte Findings.
EN: These questions assess written requirements, not implementation or release
acceptance. Items were initially unchecked; the current text review is recorded
separately. Each instruction identifies source text
and an adequacy criterion without requiring commands, tests or runtime actions.
Gap, Ambiguity and Conflict markers identify review focus, not confirmed findings.

DE: Zum Bearbeiten Quelle lesen, Frage anhand des Textes beantworten und bei
erfüllter Qualität abhaken. Bei einer Lücke den Punkt offen lassen und die
fehlende oder widersprüchliche Textstelle mit kurzer Begründung notieren.
Ein dokumentierter Open-Betriebspunkt darf klar spezifiziert sein; er ist
deshalb weder technisch erfüllt noch menschlich freigegeben. Vorhandene
Häkchen in `requirements.md` ersetzen diesen neuen Review nicht.
EN: Read the cited text and check the item only when its requirement-quality
criterion is met. Otherwise record the exact gap or conflicting passages.
A clearly specified operational Open item is neither a technical pass nor
human approval. Existing checklist ticks do not replace this review.

## Requirement Completeness / Vollständigkeit

- [X] CHK001 Sind Umfang und Abgrenzung des Nachlaufs gegenüber historischer Studie und späterer Selbstprüfung vollständig beschrieben? / Is follow-up scope fully distinguished from historical study and downstream self-review? [Completeness, Spec §FR-001, Spec §FR-015, Spec §Assumptions]
  - Durchführungsanweisung / Review instruction: Intake-Bezug, historische GAP-Liste und Plan §Delta-Zuordnung lesen. Ausreichend sind explizite In-/Out-of-Scope-Grenzen, erhaltene Feature-003-Historie und keine pauschale Wiederöffnung oder Schließung alter Befunde. / Read input, historic gap and delta references; require explicit scope and preservation of history without blanket reopening or closure.

- [X] CHK002 Sind die zu schützenden Identitäten, Rechte und Datenorte vollständig als Anforderungen benannt? / Are protected identities, privileges and data locations fully identified? [Completeness, Spec §FR-002, Spec §FR-006]
  - Durchführungsanweisung / Review instruction: FR-002/006 und Plan §Source Code vergleichen. Erkennbar getrennt sein müssen Host-Mount, beschreibbare Container-Schicht, temporäre Orte und persistente Volumes sowie Rootless-/Non-root-Grenzen; keine Ebene darf stillschweigend als durch eine andere geschützt gelten. / Distinguish each storage/privilege layer without assuming one control protects another layer.

- [X] CHK003 Ist die Anforderungsabdeckung aller tatsächlich vorgesehenen Agenten einschließlich Konfiguration, Overrides und Selbstaktualisierung eindeutig? / Are all intended agents and their configuration, overrides and updates covered? [Completeness, Spec §FR-005, Plan §Agenten und Lieferkette]
  - Durchführungsanweisung / Review instruction: Die sechs benannten Clients und FR-005 abgleichen. Ausreichend sind vollständiger Inventarumfang, versionsbezogene Aussagen sowie klare Anforderungen für abschaltbare und nicht abschaltbare Auto-Updates, ohne Anmeldung oder Providerwahl als verdeckte Voraussetzung. / Require complete client scope and version-bound update rules without hidden sign-in or provider prerequisites.

- [X] CHK004 Sind Herkunft, Integrität, Lizenzen und bestehende Kryptografie getrennt und vollständig adressiert? / Are provenance, integrity, licences and existing cryptography covered separately? [Completeness, Spec §FR-004, Spec §FR-007, Spec §FR-009]
  - Durchführungsanweisung / Review instruction: Die drei FR samt zugeordneten Evidenzpflichten lesen. Eine ausreichende Beschreibung unterscheidet Downloadprüfung, Paket-/Lizenzherkunft, Imagebestandteile und TLS-/Signaturabhängigkeiten; sie erfindet weder Schlüsselrotation noch Freigabe aus einem Herkunftsnachweis. / Look for distinct obligations and no inferred key action or approval.

## Requirement Clarity / Eindeutigkeit

- [X] CHK005 Ist die 30-Tage-Regel mit Zeitbezug, Vergleichsgrenze und geschütztem aktuellem Export eindeutig beschrieben? / Does retention define time basis, cutoff boundary and current-export protection? [Clarity, Spec §FR-006, Spec §SC-002, Plan §Audit und Retention]
  - Durchführungsanweisung / Review instruction: Clarification zur Aufbewahrung, FR-006 und CLI-Vertrag lesen. Ausreichend sind ein festgelegter Tages-/Zeitzonenbezug, die Bedeutung von „älter“, die Behandlung genau 30 Tage alter und zukünftiger Dateien sowie die Abgrenzung von Dateidatum und Änderungszeit. / Require an explicit clock/cutoff and exact-boundary, future-date and timestamp treatment.

- [X] CHK006 Sind Löschumfang und ausgeschlossene Datei-/Pfadtypen präzise begrenzt? / Are deletion scope and excluded file/path types precisely bounded? [Clarity, Spec §FR-006, CLI §Audit-Stopp, Ambiguity]
  - Durchführungsanweisung / Review instruction: Auswahlregel in Plan §Audit und Retention und Vertrag gegenüberstellen. Der Text muss Tagesdateinamen, direkten regulären Dateityp, effektiven Audit-Mount und Schutz von Unterverzeichnissen, Links, sonstigen Dateien und Volumes unterscheiden. / Require precise filename/type/location limits and explicit exclusions, not an unrestricted glob.

- [X] CHK007 Sind Reihenfolge, Fehlerfolge und Erfolgsaussage des Audit-Stopp-Vorgangs eindeutig festgelegt? / Are phase order, error handling and success meaning unambiguous? [Clarity, Spec §FR-006, CLI §Audit-Stopp]
  - Durchführungsanweisung / Review instruction: Beschreibungen zu Export, Retention und Down lesen. Ausreichend sind eine eindeutige Reihenfolge, dokumentierte Folgen jedes Phasenfehlers und eine unverwechselbare Trennung von erfolgreichem Export, erfolgreicher Bereinigung und erfolgreichem Stopp. / Require explicit phase ordering and outcomes; one phase's success cannot imply another's.

- [X] CHK008 Sind Vorschau-, Argument- und Exitcode-Anforderungen in beiden CLI-Varianten fachlich eindeutig? / Are preview, argument and exit semantics clear across both CLI variants? [Clarity, Spec §Cross-Platform Applicability, CLI §Hardening-Prüfung]
  - Durchführungsanweisung / Review instruction: Nur den CLI-Text und die Paritätsanforderungen vergleichen. Erkennbar sein müssen wirkungsfreie Vorschau, Argumenterhalt, Fehlerklassen und die Aussage, dass ein Vorschau-Erfolg kein bestandener Test ist. / Read the contract for zero-action preview, preserved arguments and differentiated outcomes without executing commands.

## Requirement Consistency / Widerspruchsfreiheit

- [X] CHK009 Sind alle sieben Clarifications konsistent in Anforderungen und Erfolgskriterien übernommen? / Are all seven clarifications consistently reflected in requirements and outcomes? [Consistency, Spec §Clarifications, Spec §FR-002, Spec §FR-003, Spec §FR-005, Spec §FR-006, Spec §FR-007, Spec §SC-007]
  - Durchführungsanweisung / Review instruction: Jede Antwort ihrer FR-/SC-Passage und der zugehörigen Planentscheidung zuordnen. Ausreichend ist dieselbe Verbindlichkeit in DE/EN und in allen betroffenen Artefakten, ohne stillschweigend geänderte Schwellen oder zusätzliche Freigaben. / Map each answer to matching requirements/design; retain equivalent meaning and authority across both languages.

- [X] CHK010 Bleiben beschreibbarer Standardbetrieb und optionale Read-only-Variante widerspruchsfrei getrennt? / Are default writable operation and optional read-only mode consistently separated? [Consistency, Spec §FR-002, Plan §Read-only-Variante]
  - Durchführungsanweisung / Review instruction: Default-, Override- und Lernablauf-Beschreibungen lesen. Ausreichend sind ausdrückliche Optionalität, bekannte Einschränkungen und die Aussage, dass ein Read-only-Root-Dateisystem schreibbare Host-Mounts nicht automatisch schützt. / Require explicit optionality, supported-flow limits and no false host-mount protection claim.

- [X] CHK011 Sind Standard-Egress, lokale Portbindung und eine lediglich offene Allowlist-Folgearbeit konsistent beschrieben? / Are default egress, loopback publishing and deferred allowlisting consistent? [Consistency, Spec §FR-002, Plan §Technical Context]
  - Durchführungsanweisung / Review instruction: Netzwerk-Clarification, FR-002 und Sicherheitsdesign vergleichen. Ausreichend ist die Trennung ausgehender Ziele von veröffentlichten Ports; aus Portbindung oder Threat Model darf keine bestehende Egress-Sperre abgeleitet werden. / Distinguish outbound access from published ports without implying an implemented egress block.

- [X] CHK012 Sind begrenzter ARM64-Handoff, offene AMD64-Pfade und umfassende Abnahme widerspruchsfrei abgegrenzt? / Are bounded ARM64 handoff, AMD64 gaps and full acceptance distinguished consistently? [Consistency, Spec §FR-013, Spec §SC-007, Plan §Abschlussgrenzen und spätere Lieferung, Conflict]
  - Durchführungsanweisung / Review instruction: Abschluss-Clarification, SC-007 und Gesamtprüfungs-/Assurance-Aussagen nebeneinander lesen. Ausreichend ist ein klarer zulässiger Teilscope mit fortbestehenden Nutzungsgrenzen; „All erfolgreich“ oder „Ready“ darf fehlende Pflichtbelege nicht verdecken. / Require bounded completion without an implied all-platform or Assurance pass.

## Acceptance Criteria Quality / Qualität der Abnahmekriterien

- [X] CHK013 Ist die 85-%-Branch-Anforderung mit vollständigem Modulnenner, Messbegriff und Umgang mit Messlücken objektiv bewertbar? / Is the 85% branch criterion objectively defined with scope, metric and missing-data treatment? [Measurability, Spec §FR-003, Spec §SC-003, Coverage §Messverfahren]
  - Durchführungsanweisung / Review instruction: Spec und Coverage-Scope lesen. Ausreichend sind Einbezug unveränderter Grenzhelfer, Umgang mit ungemessenen/inline/Subprozess-Anteilen und die ausdrückliche Nichtgleichsetzung von Branch-, Zeilen- und Command-Coverage. / Require complete scope and no substitution of line/command percentages for branch measurement.

- [X] CHK014 Ist die 80-%-Schnittstellenquote neben der 100-%-Pflicht für geänderte Interfaces klar definiert? / Are the 80% interface threshold and universal changed-interface obligation clear? [Measurability, Spec §FR-003, Spec §SC-002, Coverage §Schnittstellen-Nenner]
  - Durchführungsanweisung / Review instruction: Definition des öffentlichen Interface-/Flow-Katalogs sowie Zähler/Nenner vergleichen. Ausreichend sind festgelegte Zähleinheiten, Plattformvarianten, beide Fallarten und die Behandlung fehlender Beobachtung ohne verkleinerten Nenner. / Require stable counting units, variant and positive/negative obligations, and explicit missing evidence.

- [X] CHK015 Sind Critical-/High-Schwellen und zulässige VEX-/Open-Dispositionen messbar und ohne implizite Risikoakzeptanz formuliert? / Are vulnerability thresholds and exceptions measurable without implied risk acceptance? [Measurability, Spec §FR-007, Spec §SC-004]
  - Durchführungsanweisung / Review instruction: Schwellen-Clarification, FR-007 und SC-004 lesen. Ausreichend sind unbedingte Critical-Sperre, Unterscheidung High mit/ohne Fix sowie konkrete CVE-/Komponentenbezüge und die erforderlichen Owner-/Folgeaktions-/Triggerangaben für Open. / Require exact thresholds, finding-bound dispositions and retained human authority.

- [X] CHK016 Ist die Rückverfolgbarkeit von 15 FR, acht SC und 50 Delta-IDs ohne Doppelzählung spezifiziert? / Is traceability of all requirements, outcomes and delta IDs specified without double counting? [Traceability, Spec §FR-001, Spec §FR-014, Spec §SC-001, Plan §Anforderungsabdeckung]
  - Durchführungsanweisung / Review instruction: FR-/SC-Verweistabelle und Delta-Partition redaktionell vergleichen. Ausreichend ist je ID eine eindeutige Primärzuordnung mit Quellen-/Abnahmebezug; wiederverwendete Evidence darf mehrere Kontrollen stützen, aber nicht mehrfachen Erfolg erfinden. / Compare written mappings for unique primary links and honest shared evidence.

## Scenario Coverage / Abdeckung der Abläufe

- [X] CHK017 Sind Hauptabläufe, eigenständiger US1-MVP und sinnvolle Übergaben zwischen US1, US2 und US3 vollständig beschrieben? / Are main flows, independent US1 value and story handoffs complete? [Coverage, Spec §User Scenarios & Testing, Plan §Umsetzungsschnitte]
  - Durchführungsanweisung / Review instruction: Priorität, Independent Test und Acceptance Scenarios jeder Story lesen. Ausreichend sind eigener Nutzwert und klare Abhängigkeiten, ohne eine Human-Freigabe oder vollständiges US2 als verdeckte Bedingung für die isolierte US1-Prüfbarkeit. / Require independently reviewable value and explicit dependencies.

- [X] CHK018 Sind sichere synthetische Prüfkontexte und Grenzen nicht beobachtbarer Live-Eigenschaften als Anforderungen beschrieben? / Are safe synthetic assessment scope and unobserved live properties explicitly bounded? [Coverage, Spec §FR-005, Spec §FR-006, Spec §Edge Cases]
  - Durchführungsanweisung / Review instruction: Texte zu Zugangsdaten, Providerzugriff, Testdaten und OpenCode-2-Liveverhalten lesen. Ausreichend ist ein sicherer Weg ohne echte Anmeldung sowie eine klare Open-/Nutzungsgrenze für dadurch nicht belegte Eigenschaften. / Require synthetic-data paths without converting unobserved live properties into success.

- [X] CHK019 Ist der Schutz des laufenden Lernsystems gegenüber separaten Prüfkandidaten eindeutig gefordert? / Is protection of the live learning environment from candidate validation explicit? [Coverage, Spec §FR-002, Spec §FR-013, Plan §Read-only-Variante]
  - Durchführungsanweisung / Review instruction: Isolation, Volumes und künftige Runtime-Abnahme im Plan/Quickstart lesen. Ausreichend sind getrennte Ressourcen, keine persönlichen Zustände als Fixtures und eine begrenzte Aufräumverantwortung statt globaler Bereinigung. / Require separate resources and bounded ownership, not live personal data or global cleanup.

- [X] CHK020 Sind Revalidierung und Umgang mit Quellen-, Versions- oder Imagewechseln nachvollziehbar beschrieben? / Are revalidation requirements for changed inputs understandable? [Coverage, Spec §FR-014, Spec §Assumptions, Data Model §Invarianten]
  - Durchführungsanweisung / Review instruction: Frische-/Hash- und Evidenzregeln vergleichen. Ausreichend ist die Angabe, welche Änderung welche Aussage neu prüfpflichtig macht; historische Belege bleiben erhalten, aktuelle Freigaben werden daraus nicht ungeprüft abgeleitet. / Require causal revalidation and preserved historical records.

## Edge Case Coverage / Randfälle und Wiederanlauf

- [X] CHK021 Sind fehlender, leerer oder nicht eindeutig zuordenbarer Auditexport und Audit-Mount als Anforderungsfälle berücksichtigt? / Are absent, empty or ambiguous audit export/mount conditions specified? [Edge Cases, Spec §FR-006, Plan §Audit und Retention, Gap]
  - Durchführungsanweisung / Review instruction: Anforderungen an Exporterfolg und Mountbindung lesen. Ausreichend ist eine textliche Entscheidung über zulässigen Exportzustand, eindeutigen Zielort und Fehlerfolge; unklarer Ort darf keine Löschfreigabe bedeuten. / Require explicit valid-export/location criteria and failure consequences, not inferred deletion authority.

- [X] CHK022 Sind Teilfehler der Retention und der anschließende Wiederanlauf ausreichend beschrieben? / Are partial retention failure and subsequent recovery requirements sufficient? [Recovery, Spec §FR-006, CLI §Audit-Stopp, Gap]
  - Durchführungsanweisung / Review instruction: Texte zu Löschfehler, Down-Sperre und erneuter Ausführung lesen. Ausreichend ist die Unterscheidung schon entfernter Metadaten von erhaltenen Agentendaten sowie eine klare Fortsetzungs-/Fehleraussage ohne unbelegtes Rollback-Versprechen. / Require honest partial-state and retry behavior, not an invented rollback guarantee.

- [X] CHK023 Sind Datumsrandfälle, Pfad-/Typwechsel und konkurrierende Vorgänge als relevante Grenzen spezifiziert oder begründet ausgeschlossen? / Are date edges, path/type changes and concurrency covered or explicitly excluded? [Edge Cases, Spec §FR-003, Spec §FR-006, Ambiguity]
  - Durchführungsanweisung / Review instruction: Plan-Retention, CLI-Vertragsfälle und Datenmodell vergleichen. Ausreichend sind klare Schutzgrenzen für exakt 30 Tage, Zukunft, Links/Reparse-Points und einen möglichen Wechsel zwischen Auswahl und Löschung; Parallelität braucht ein beschriebenes Verhalten oder einen begründeten Scopeausschluss. / Require boundary and race/concurrency semantics, not assumptions of stability.

- [X] CHK024 Sind fehlende Plattformen und Teilbelege klar von Nichtanwendbarkeit und voller Abnahme getrennt? / Are missing platforms and partial proofs distinguished from N/A and full acceptance? [Edge Cases, Spec §FR-013, Spec §SC-007, Plan §Governance- und Abnahme-Gates]
  - Durchführungsanweisung / Review instruction: Die drei Plattformpfade und Umgang mit CI-/Skip-Belegen lesen. Ausreichend sind konkrete offene Übergaben mit Owner/Trigger und dieselbe Hardware nur als erlaubte Ressourcenteilung, niemals als wiederverwendbarer Ergebnisbeleg. / Require platform-scoped gaps and no copied proof or missing-platform N/A.

## Non-Functional Requirements / Nichtfunktionale Anforderungen

- [X] CHK025 Sind speichersichere Helferwahl, Shell-Ausnahme und sprachbezogene Sicherheitsprüfung angemessen begründet? / Are language safety, shell exception and language-specific review justified? [Security, Spec §CR-005, Spec §FR-003, Plan §Constitution Check]
  - Durchführungsanweisung / Review instruction: MSL-/Security-Passagen lesen. Ausreichend ist eine begrenzte Begründung bestehender Shell-Grenzen mit expliziten Prüfpflichten; MSL-Status, Syntaxprüfung oder Testanzahl darf sichere Argument-/Pfadverarbeitung nicht ersetzen. / Require a bounded rationale and explicit secure-coding obligations rather than assumed safety.

- [X] CHK026 Sind Architekturgrenzen und die erwarteten Bedrohungs-/Entscheidungsnachweise konkret zugeordnet? / Are trust boundaries and architecture evidence obligations concretely mapped? [Security, Spec §Architecture Governance Applicability, Spec §FR-002, Plan §Governance- und Abnahme-Gates]
  - Durchführungsanweisung / Review instruction: Host/VM/Container-, Mount-, Build-/Runtime- und Providergrenzen lesen. Ausreichend sind Datenklassen und erwartete STRIDE/CIA/CAPEC-, Zero-Trust-, ADR-/arc42-/SAMM-Beiträge mit Pfaden, ohne erfundene Reife- oder Schutzwirkungsbehauptung. / Require concrete boundaries and attributable architecture records without unsupported maturity claims.

- [X] CHK027 Sind A11Y-Anforderungen artefaktbezogen, nachvollziehbar und von automatischen Text-/PDF-Prüfungen getrennt? / Are accessibility requirements artifact-specific and distinct from automated checks? [Accessibility, Spec §FR-012, Spec §SC-006, Spec §CR-002/CR-003]
  - Durchführungsanweisung / Review instruction: WCAG-Kriterien, CLI-/Dokumentarten, Textalternativen und Human-Review lesen. Ausreichend sind passende Kriterien/Reviewwege und klare Grenzen fehlender menschlicher Beobachtung, keine generelle WCAG- oder PDF-Abnahme aus Markdownqualität. / Require applicable criteria and human proof boundaries rather than automatic conformity.

- [X] CHK028 Sind alle vier IHK-IT-Berufe ab Jahr 1 einschließlich der vier Fachrichtungen des Fachinformatikers, Sprachgleichwertigkeit und verständliche Erstnutzung vollständig als Anforderungen beschrieben? / Are all four IHK IT occupations from year one, including all four IT specialist tracks, bilingual equivalence and novice use fully specified? [Readability, Spec §FR-012, Spec §SC-006, Spec §Einführung, Plan §Dokumentation und Parität]
  - Durchführungsanweisung / Review instruction: Zielgruppenabschnitt, DE/EN-Strategie und Leserpfadregeln lesen. Für Fachinformatiker*innen Anwendungsentwicklung, Systemintegration, Daten- und Prozessanalyse sowie Digitale Vernetzung einzeln berücksichtigen. Ausreichend ist eine erkennbare Anforderungsabdeckung ihrer unterschiedlichen Lern- und Nutzungspfade neben den drei weiteren IT-Berufen, ohne für jede Fachrichtung eine zweite Lernreihe zu verlangen. Keine vorausgesetzte Spec-Kit-Erfahrung, erklärte Begriffe und gleichwertige Fehlermeldungs-/Bedienhilfe auf etwa CEFR B2 bleiben erforderlich. / Review application development, systems integration, data and process analysis, and digital networking individually alongside the other three occupations. Require visible coverage of their different learning and usage needs, not a separate curriculum for each track. Retain novice access, first-use definitions and equivalent B2-level help in both languages.

## Dependencies & Assumptions / Abhängigkeiten und Annahmen

- [X] CHK029 Sind verbindliche Quellen, ihre Aktualität und die Autorität für spätere Quellenänderungen klar festgelegt? / Are binding inputs, freshness and later change authority clearly defined? [Dependencies, Spec §Assumptions, Plan §Dokumentation und Parität]
  - Durchführungsanweisung / Review instruction: Intake-/Receipt-/Review-/Spec-Bezüge lesen. Ausreichend ist die Unterscheidung geordneter Quellenbindung, unabhängiger fachlicher Prüfung und späterer Änderungsautorität; neue Hashes allein dürfen keinen ersetzten Vollreview vortäuschen. / Require distinct provenance, substantive review and update authority.

- [X] CHK030 Sind lesbare Evidenzpfade und datierter Assurance-Kontext widerspruchsfrei verknüpft? / Are readable evidence paths and the dated Assurance context consistently linked? [Dependencies, Spec §Security Evidence Expectations, Plan §Governance- und Abnahme-Gates, Data Model §Speicherung und Grenzen]
  - Durchführungsanweisung / Review instruction: E-/A-Definition, Baseline/Delta/Closure/Image-Impact und Metadatenregeln vergleichen. Ausreichend sind ein eindeutiger Kontext, klare Pfadverantwortung und eine Trennung geplanter Dateien von realer Evidence; kein historischer Beleg darf passend umgeschrieben werden. / Require unique context and honest planned/current/historical distinctions.

- [X] CHK031 Sind alle 14 Presets samt Version, Priorität und wiederkehrender Reviewpflicht nachvollziehbar gebunden? / Are all 14 presets, their versions/priorities and review cadence traceable? [Dependencies, Spec §FR-010, Spec §SC-005, Plan §Governance- und Abnahme-Gates]
  - Durchführungsanweisung / Review instruction: Profilmatrix und H-344-08-/Assurance-Verweise lesen. Ausreichend sind Quelle der Sollmatrix, aktive DE/EN-Metadatenregeln und quartals-/anlassbezogene sowie zusätzliche 3.-Oktober-Reviewpflicht mit Owner, ohne Installationsnachweis aus einer Tabelle abzuleiten. / Require exact profile obligations and cadence, not inferred installation success.

- [X] CHK032 Sind regulatorische, Cloud-, Lizenz- und Providerentscheidungen rollenbezogen und ohne pauschales Ausbildungs-N/A abgegrenzt? / Are regulatory, cloud, rights and provider decisions scoped by role without blanket educational exemptions? [Assumption, Spec §FR-007, Spec §FR-008, Spec §FR-011]
  - Durchführungsanweisung / Review instruction: Human-/Cloud-Register und regulatorische Abschnitte lesen. Ausreichend ist die Trennung Produkt, Werkzeugbetrieb und Organisation mit datierter Quellen-/Rollenprüfung; AI-SBOM-N/A oder C5 darf andere Pflichten und offene Rechte nicht automatisch erledigen. / Require independent applicability and authority decisions across scopes.

## Ambiguities & Conflicts / Unklarheiten und Konflikte

- [X] CHK033 Ist das Verhältnis neuer Featureauswahl zu historischen CLI-Defaults ohne stillen Evidence-Fallback beschrieben? / Is new feature selection distinguished from historical CLI defaults without silent evidence fallback? [Ambiguity, Spec §FR-014, CLI §Hardening-Prüfung]
  - Durchführungsanweisung / Review instruction: Parameter-/Default-/Fehlerbeschreibungen im Vertrag lesen. Ausreichend sind unmissverständliche Bindung an Feature 004 bei expliziter Auswahl und sichere Behandlung fehlender neuer Gate-Dateien; historische Standardprüfung darf nicht als aktueller Erfolg erscheinen. / Require explicit context identity and failure on missing inputs rather than reused historical success.

- [X] CHK034 Sind effektive OpenCode-2-Schutzwirkung und tatsächlich exportierte Auditkategorie widerspruchsfrei getrennt? / Are effective OpenCode 2 safeguards and exported metadata categories consistently separated? [Conflict, Spec §FR-005, Spec §FR-006, Spec §SC-008]
  - Durchführungsanweisung / Review instruction: Aussagen zu Loop-/Override-/Subagent-Schutz und Sitzungsaudit lesen. Ausreichend ist ausdrücklich `session_coverage=not-exported`, getrennte Open-Punkte und kein Datenbank-/WAL-/SHM-/Prompt-/Antwortexport als Ersatz; Konfigurationsregeln allein sind keine Wirksamkeitsbehauptung. / Require explicit metadata-only limits and no configuration-only effectiveness inference.

- [X] CHK035 Sind Statusfelder, offene Folgearbeit und Risikoannahme sprachlich und fachlich eindeutig getrennt? / Are applicability, fulfillment, follow-up and risk acceptance unambiguously separated? [Consistency, Spec §FR-014, Spec §SC-005, Data Model §Invarianten]
  - Durchführungsanweisung / Review instruction: Enumdefinitionen und Open-/N/A-/Ready-Aussagen vergleichen. Ausreichend sind N/A plus Not Assessed und Begründung/Trigger, Open mit Owner/Folgeaktion/Frist sowie menschlich zuordenbare Risikoannahme; ein klar formulierter offener Punkt ist kein erfüllter Kontrollpunkt. / Require exact independent statuses and human authority, not renamed uncertainty.

- [X] CHK036 Ist die Grenze zwischen Checklistenqualität, begrenztem Handoff, Folge-Intake und Ausführungsfreigabe eindeutig? / Are checklist quality, bounded handoff, downstream work and execution authority clearly separated? [Clarity, Spec §FR-015, Spec §SC-008, Plan §Abschlussgrenzen und spätere Lieferung]
  - Durchführungsanweisung / Review instruction: Abschluss-/Autoritätsabschnitte und bestehende Reihenstatus lesen. Ausreichend ist die ausdrückliche Aussage, dass grüne Requirements-Checks weder Implementierung noch Build, Lieferung, Human-Freigabe oder automatischen Start blockierter Intakes autorisieren. / Require explicit separation of text quality from every operational and human decision.

## Notes / Hinweise

DE: 36 Punkte mit Quellenbezug und eigener Durchführungsanweisung am
2026-10-27 anhand der Texte bearbeitet. Sieben Textbefunde korrigiert und
betroffene Fragen erneut gelesen; Einzelbegründungen im verlinkten Review.
Häkchen bedeuten ausreichende Anforderungsqualität, keine technische Erfüllung
oder menschliche Freigabe. Spec und Plan sowie betroffene Begleittexte wurden
im gesondert autorisierten Review korrigiert; Quellenbindungen, historische
Evidenz und Reihenstatus bleiben unverändert. `tasks.md` liegt noch nicht vor;
Aufgabenabdeckung ist nicht Gegenstand dieses Reviews. Kein unabhängiges
Vollreview der Umsetzung und kein ersetzter Analyze-Lauf.
EN: Reviewed all 36 questions against text on October 27, corrected seven
textual findings and reread affected questions. The linked review records
each rationale. Ticks mean adequate requirements, not technical fulfillment
or human approval. Spec/plan and affected companion text were corrected under
separate review authority, preserving input bindings, history and lifecycle.
No task coverage, independent implementation acceptance or Analyze is claimed.
