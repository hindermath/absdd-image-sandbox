# Research: Sichere Entwicklungs-Container-Haertung / Secure Development Container Hardening

## Forschungsbasis / Research Basis

**DE:** Geprueft wurden die geklaerte Spezifikation, alle sechs akzeptierten
Artefakte und ihre aktuellen SHA-256-Werte, alle 157 Gap-Datensaetze, der
orchestratorverwaltete Run-State, Constitution v1.16.0, `Dockerfile`, beide
Compose-Dateien, Agentenkonfigurationen, Build-/SBOM-/Audit-/Smoke-Skripte,
vorhandene Tests, Workflows, VS-Code-Dev-Container, Security-, Betriebs-,
Lernenden- und Statistikdokumentation. Kein Produktzustand wurde geaendert.

**EN:** Research inspected the clarified specification, six accepted artefacts
and current hashes, all 157 gap records, orchestrator-owned run state,
constitution, Docker/Compose, agent configuration, scripts, tests, workflows,
VS Code configuration, and security, operations, learner, and statistics docs.
No product state was changed.

## Entscheidung 1: Eingangsbindung und Partition / Input Binding and Partition

**Decision:** Die sechs aktuellen Dateihashes stimmen exakt mit `spec.md` und
`autonomous-run-state.json` ueberein. `assessment-results.json` enthaelt exakt
157 offene Gaps, alle `P1`, mit 108 `humanOnly: false` und 49
`humanOnly: true`; die Human-only-Rollenliste aus `spec.md` ist bindend.

**Rationale:** Die AcceptedBaseline ist Arbeitsgrundlage, nicht Abschluss oder
Risikoakzeptanz. Jede spaetere positive Aussage braucht neue Evidenz.

**Alternatives considered:** Die vorhandenen 157 `Open`-Zeilen unmittelbar als
umsetzbare Aufgaben oder als erfuellt zu behandeln wurde verworfen; beides
vermischt Befund, Anwendbarkeit und Implementierungsstatus.

## Entscheidung 2: Kanonisches Gap-Register / Canonical Gap Register

**Decision:** Ein kanonisches `gap-dispositions.json` enthaelt genau einen
Eintrag je `GAP-001` bis `GAP-157`. JSON-Schema prueft Struktur; ein gemeinsamer
Python-Validator prueft exakte Menge, Reihenfolge, Eindeutigkeit, 108/49,
Human-only-Rollen, Statuskombinationen, Referenzen und Evidenzfrische.

**Rationale:** JSON Schema allein kann die fortlaufende ID-Menge und die
wechselseitige Bindung an die akzeptierte Baseline nicht vollstaendig pruefen.
Eine Markdown-Tabelle allein waere fuer deterministische Validierung zu fragil.

**Alternatives considered:** 157 lose Markdown-Dateien und eine einzige breite
Tabelle wurden wegen Drift-, Screenreader- und Duplikatrisiko verworfen.

## Entscheidung 3: Evidence-first RED/GREEN

**Decision:** Jeder Gap startet aus der akzeptierten Baseline als `Open` und
`Not Assessed`. Ein RED-Test zeigt zuerst fehlende, veraltete oder fehlerhafte
Evidenz. Danach ist genau eine dieser Antworten erlaubt: aktuelle Evidenz fuer
`AlreadySatisfied`, minimale Aenderung plus GREEN, begruendetes `N/A` plus
Trigger oder ehrliches `Open`/`FollowUp`.

**Rationale:** Das Repository besitzt bereits viele Kontrollen. Pauschale
Edits koennten Lernablaeufe brechen und waeren nicht finding-conditioned.

**Alternatives considered:** Dockerfile/Compose anhand einer Ideal-Checkliste
komplett neu zu schreiben wurde als nicht rueckverfolgbarer Umbau verworfen.

## Entscheidung 4: Bestehende Container-Kontrollen zuerst beweisen / Prove Existing Controls First

**Decision:** Als vorhandene, aber noch aktuell zu belegende Kontrollen gelten:
digest-gepinntes MCR-Basisimage, `USER adedev`, `no-new-privileges:true`,
`cap_drop: ALL`, localhost-Portbereich, getrennte Agent-Volumes,
read-only-`ContainerBuild.props`, deaktivierte Agenten-Autoupdates,
Codex-Workspace-/Netzwerkgrenzen und OpenCode-Approval-/Secret-Regeln.

**Rationale:** Statische Existenz ist keine Wirksamkeitsevidenz. Praktische
Identity-, Capability-, Mount-, Allowed/Denied-Write- und State-Tests sind
noetig, bevor ein Gap positiv dispositioniert wird.

**Alternatives considered:** Diese Controls allein anhand der Dateiinhalte als
`Fulfilled` zu markieren wurde nach FR-002/FR-004a verworfen.

## Entscheidung 5: Reproduzierbare Quellen und Downloads / Reproducible Sources and Downloads

**Decision:** Ein statischer Pin-Audit erfasst Basis, apt-Quellen, Go, Rust,
Swift, uv, Syft, Spec Kit, Home Baseline und sechs Agentenoberflaechen. Jede
Quelle benoetigt unveraenderliche Identitaet oder verifizierbare Integritaet.
Die direkte Helper-Inspektion bestaetigt zwei RED-Befunde bereits vor Tasks:
`scripts/build-and-sbom.*` verwendet im Fallback
`docker.io/anchore/syft:latest`, und `scripts/analyze-sbom.*` sucht Grype oder
Trivy nur als ungepinnte Host-Installation. Go-Tarball ohne explizite
Checksumme, Node-Paket/Repository-Key, git-tag-basierte Spec-Kit-Installation
und Checksummen aus demselben Downloadkanal bleiben Pruefhypothesen, bis der
reproduzierbare Audit sie bestaetigt. Konkrete Produktedits erfolgen erst nach
der RED-Evidenz in der Implementierungsphase.

**Rationale:** Versions-ARGs sind wichtig, aber nicht fuer jede Quelle ein
vollstaendiger Herkunfts- oder Integritaetsnachweis.

**Alternatives considered:** Versionsnummern ohne Quellen-/Hashpruefung als
reproduzierbar anzunehmen und Netzwerkwerte im Plan zu erfinden wurden
verworfen. Neue Digests/Checksummen werden erst bei Implementierung aus
authentischer Quelle ermittelt und als Review-Evidenz festgehalten.

## Entscheidung 6: Mount-, Netzwerk- und Credential-Grenzen

**Decision:** Mounts werden mit Zweck, Hostquelle, Containerziel,
read/write-Modus, Datenklasse, Agentenzugriff und Test inventarisiert. Breite
RW-Mounts, `read_only`, PID-/Ressourcenlimits und Rootless-Hostbetrieb werden
praktisch beurteilt. Freier Egress bleibt ohne formale Owner-Entscheidung
`Open`; das bestehende Dokument darf keine Risikoakzeptanz behaupten. Reale
Credentials und Providerzustand sind aus Tests/Evidenz ausgeschlossen.

**Rationale:** Compose allein kann ohne Proxy/DNS-/Plattformkontrolle keine
belastbare Ziel-Allowlist erzwingen. `GAP-155` ist Human-only. Eine technische
Dokumentation darf diese Entscheidung nicht vorwegnehmen.

**Alternatives considered:** `network_mode: none` wurde verworfen, weil es die
verbindlichen Lern-/Paket-/Agentenablaeufe blockiert. Unbeschraenkten Egress als
akzeptiertes Risiko zu deklarieren wurde wegen fehlender Autoritaet verworfen.

## Entscheidung 7: Paired Validator statt redundanter Vollsuiten / Paired Validator Instead of Repeated Full Suites

**Decision:** `Test-AdeSandboxHardening` bildet einen gemeinsamen Modusvertrag
(`Input`, `Static`, `Runtime`, `SupplyChain`, `Documentation`,
`Accessibility`, `All`) ab.
Bash und PowerShell rufen denselben Python-Semantikkern auf, besitzen
`--dry-run`/`-WhatIf`, identische Exitcodes und schreiben strukturierte
Evidenz. Der Kern nutzt nur die Python-Standardbibliothek und erzwingt die
Strukturregeln der beiden gelieferten JSON-Schemas explizit; positive und
negative Fixtures verhindern Schema-/Semantikdrift ohne ungepinnte
Laufzeitabhaengigkeit. Full Build/Smoke laeuft einmal nach den finalen
technischen Aenderungen; waehrend RED/GREEN laufen gezielte Modi.

**Rationale:** Das erfuellt Cross-Platform-Paritaet und vermeidet mehrfachen
teuren Image-Build ohne Evidenzgewinn.

**Alternatives considered:** Zwei unabhaengige Implementierungen der gesamten
Semantik wurden wegen Drift verworfen. Nur ein Bash-Skript verletzt die
bindende Cross-Platform-Governance.

## Entscheidung 8: SBOM, Schwachstellen, VEX und Provenienz

**Decision:** Die finale lokale Image-ID wird an genau eine aktuelle
CycloneDX-SBOM gebunden. Ein gepinnter, reproduzierbarer Scannerpfad wird nur
bei bestaetigtem Fehlen ergaenzt. Relevante Funde erhalten CycloneDX-VEX-Status
`affected`, `not_affected`, `resolved`/`mitigated` oder
`under_investigation` mit Begruendung; der menschenlesbare Vertrag bildet die
Spec-Begriffe ab. Lokale Provenienz nennt Source-HEAD, Dockerfile-/Compose-
Hash, Basisdigest, Buildbefehl, Plattform, Image-ID und Zeitpunkt. Keine
Registry, Signatur- oder SLSA-Stufe wird erfunden.

**Rationale:** Historische Dateien in `sboms/` sind nicht automatisch aktuell
und eine SBOM allein ist kein Schwachstellennachweis.

**Alternatives considered:** Alte SBOMs wiederzuverwenden oder fehlende
Scanner-/Provenienz-Evidenz als `N/A` zu markieren wurde verworfen; fehlende
Evidenz ist `Open`.

## Entscheidung 9: Security- und Architekturartefakte

**Decision:** Fuer die Sandbox werden projektbezogen mindestens Threat Model
(STRIDE+CIA+CAPEC), arc42 Security Concepts, S-ADRs fuer Isolation/Egress/
Quellenintegritaet, Security Checklist, MSL-/Sprachregeln, Dependency Audit,
Supply Chain, Zero-Trust-N/A, SAMM, Cloud-Autonomy-N/A, Cloud-C5-N/A und
Regulatory-Handoff geplant. ASVS und AI-SBOM bleiben mit sachlichem Trigger
`N/A`.

**Rationale:** Das Feature veraendert Architektur- und Trust-Boundary-Evidenz,
auch wenn keine Anwendung entwickelt wird.

**Alternatives considered:** Nur `sandbox-isolation.md` zu aktualisieren wurde
wegen fehlendem Threat Model, ADR, Qualitaetsszenarien und Standardsabgleich
verworfen.

## Entscheidung 10: VS Code, Lernende und A11Y

**Decision:** Der vorhandene Attach-to-Container-Pfad bleibt Grundmodell: kein
permanenter VS-Code-Server und kein neuer Port, `remoteUser: adedev`, explizite
Workspace-Mappings und textlich erklaerte `code`-Shim-Grenze. Geaenderte
Lerntexte werden gegen vier Ausbildungsberufe, erstes Ausbildungsjahr,
DE-first/EN-second, CEFR B2, Erstbegriffserklaerung, keine Spec-Kit-Vorkenntnis,
Text-first und anwendbare WCAG-2.2-AA-Kriterien geprueft. Der moderierte
Erstnutzungstest aus SC-009 wird von `Learning/A11Y Review` mit datiertem,
nicht sensiblem Ergebnisdatensatz ausgefuehrt. Der Agent validiert nur dessen
Vollstaendigkeit und Schwellenwert; er simuliert weder Teilnehmende noch
menschliche Beobachtungen.

**Rationale:** Die vorhandene Dokumentation ist eine gute Basis, aber der
praktische Plattformbeleg und die Synchronisation mit finalen Grenzen muessen
aktuell sein.

**Alternatives considered:** VS Code in das Image einzubauen oder einen IDE-
Port zu oeffnen wurde als unnoetige Angriffsflaeche verworfen.

## Entscheidung 11: Agentenparitaet

**Decision:** Projektspezifische Mount-/Build-Details bleiben lokal.
Gemeinsame Sicherheits-, Lernenden- oder Spec-Kit-Regeln werden nur atomar in
`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, bei
Bedarf `.github/agents/copilot-instructions.md`, passenden Templates und
`.specify/memory/constitution.md` geaendert. Bestehender Paritaetstest wird
erweitert statt eine zweite Quelle zu schaffen.

**Rationale:** So bleibt gemeinsame Guidance synchron, ohne projektlokale
Details unnoetig in Home-Baseline-Regeln zu heben.

**Alternatives considered:** Nur `AGENTS.md` zu aktualisieren wurde verworfen.

## Entscheidung 12: Human-only, Orchestrator und Statistik

**Decision:** Die 49 Human-only-Gaps behalten `Open`, `Not Assessed` und
`Unassessed`, bis die
jeweilige Rolle datierte Evidenz liefert. Modellaufgaben enden mit lokaler
Implementierung/Validierung. Commit, PR, Merge, Default-Branch-Sync und
PostMerge sind Orchestrator-only. Statistikprofil 2 wird nach dem Content-
Commit gerendert und als eigener Statistik-Commit geliefert; die Planphase
rendert nichts. Fehlende Linux- oder Windows/WSL2-Evidenz bleibt offen und
blockiert das jeweilige Applicable-Gate sowie `MergeAndSync`; sie wird weder
als `N/A` noch durch macOS ersetzt. PreMerge-Evidenz bleibt temporaer und
bindet den exakten reviewten Head. PostMerge bindet kausal deren normalisierten
Hash und den realen Merge-Commit mit leerer Aenderungsliste.

Fuer diesen Run ist `MergeAndSync` einschliesslich eines eng begrenzten
Admin-Bypass bereits ausdruecklich autorisiert. Der Bypass darf nur innerhalb
der Provider-Merge-Operation verwendet werden, wenn der exakte reviewte Head
alle technischen Checks gruen hat, kein handlungsrelevanter Review-Thread
offen ist, eine gueltige Schema-2.0-`PreMerge`-Evidenz vorliegt und
`REVIEW_REQUIRED` der einzige verbleibende Policy-Blocker ist. Er darf keine
fehlgeschlagene, ausstehende, fehlende, veraltete oder widerspruechliche
technische/Security-Pruefung und keine Repository-Regel umgehen; eine weitere
Autoritaetsanfrage ist fuer diesen Run nicht erforderlich. / This run already
has explicit `MergeAndSync` authority including narrowly bounded
Admin-Bypass. It may be used only inside the provider merge operation when the
exact reviewed head has all technical checks green, no actionable review
thread, valid schema-2.0 `PreMerge` evidence, and `REVIEW_REQUIRED` as the sole
remaining policy blocker. It may not bypass any failed, pending, missing,
stale, or contradictory technical/security check or change repository rules;
no further authority request is required for this run.

**Rationale:** Anforderungen und historische Folgeprompts erteilen keine
Lieferautoritaet. Statistik muss den finalen Content-Stand messen und getrennt
reviewbar bleiben.

**Alternatives considered:** Human-only-Vorlagen als Abschluss zu zaehlen,
Statistik im Content-Commit zu mischen oder PostMerge-Arbeit vor dem Merge zu
simulieren wurde verworfen.

## Offene Klaerungen / Open Clarifications

Keine. Technische RED-Befunde waehrend der Implementierung sind Ergebnisse,
keine offenen Planungsfragen, und werden fail-closed dispositioniert. / None.
Implementation RED findings are results, not planning ambiguities.
