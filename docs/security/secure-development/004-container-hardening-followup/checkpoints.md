# Feature 004: Prüfregister / Review checkpoints

## Deutsch

**Angelegt:** 2026-10-31 nach T001/T002. Dieses Register beginnt mit geplanten Prüfungen. `Applicable` und `Open` bezeichnen Anwendbarkeit, `Not Assessed` die noch fehlende Wirksamkeitsbewertung. Eine Datei, ein grüner Hash oder ein Scan allein erzeugt keinen `Fulfilled`-Status. Alle Nachweise beziehen sich auf den jeweils aktuellen Git- und Eingabestand; Änderungen verlangen eine betroffene Neubewertung. Die vollständige 50-ID-Zuordnung steht in [control-matrix.md](control-matrix.md).

| Gate | Anwendbarkeit | Umsetzung | Erwarteter Nachweis | Owner; Reviewer | Nächste Aktion, Frist und Trigger |
| --- | --- | --- | --- | --- | --- |
| G004-01 | Applicable | Not Assessed | `control-matrix.md`, `input-bindings.md` | Maintainer; Security Review | 50er-Matrix nach finalen Änderungen reviewen; vor US3; bei Quellenwechsel. |
| G004-02 | Applicable | Not Assessed | `platform-parity.md`, `threat-model.md` | Maintainer; Security Review | Rechte, Mounts und Egress prüfen; vor Runtime; bei Compose-/Mountwechsel. |
| G004-03 | Applicable | Not Assessed | `platform-parity.md`, optionale Read-only-Konfiguration | Maintainer; Platform Review | Variante isoliert prüfen; vor Nutzung der Variante; bei neuem Schreibort. |
| G004-04 | Applicable | Not Assessed | `coverage-modules.json`, `interface-catalog.json`, `secure-coding-review.md`, `msl-applicability.md` | Maintainer; unabhängiger Security Review | Nenner, Zweige und Fälle messen; vor Code-Freeze; bei Quell-/Katalogwechsel. |
| G004-05 | Applicable | Not Assessed | `dependency-audit.md` | Maintainer; Security Review | Downloads, Pins und Herkunft prüfen; vor Image-Build; bei Abhängigkeitswechsel. |
| G004-06 | Applicable | Not Assessed | `agent-security-review.md` | Maintainer; Security Review | Sechs Clients und effektive Updates/Overrides prüfen; vor Agentennutzung; bei Versions-/Konfigwechsel. |
| G004-07 | Applicable | Not Assessed | `audit-retention-review.md`, `gdpr-applicability.md` | Maintainer; Security und Privacy Review | Export, 30-Tage-Auswahl und Stopp isoliert prüfen; vor auditpflichtigem Betrieb; bei Datenfluss-/Fristwechsel. |
| G004-08 | Applicable | Not Assessed | `supply-chain-evidence.md`, finale SBOM | Maintainer; Security und Rights Review | T063/T064 nach finalem Image; vor Weitergabe; bei Image-/Lizenzwechsel. Kein vorgezogener Abschluss. |
| G004-09 | Open | Not Assessed | `regulatory-applicability.md` und Rechtsdetaildateien | Repository Owner; qualifizierter Privacy/Legal Review | O-344-HUMAN: Land, Rolle und Pflicht entscheiden; vor betroffener Nutzung/Weitergabe, bei Rollenwechsel. Kalenderfrist durch Owner festlegen. |
| G004-10 | Applicable | Not Assessed | `crypto-tls-inventory.md` | Maintainer; Security Review | TLS/Signaturen und Migration prüfen; vor finalem Code-Freeze; bei Profilwechsel. Keine agentische Rotation. |
| G004-11 | Applicable | Not Assessed | `preset-assurance-review.md`, datierter Assurance-Kontext | Maintainer; unabhängiger Security Review | 14 Presets und Mutationsfälle prüfen; vor Review; quartalsweise, anlassbezogen und am 3. Oktober. |
| G004-12 | Open | Not Assessed | `cloud-autonomy-applicability.md`, `cloud-compliance-assurance.md` | Repository Owner; Architecture Review | O-344-CLOUD: C3A/C5 und Providerrolle entscheiden; vor Cloud-/Providererweiterung, bei Hosting-/Registrywechsel. Kalenderfrist durch Owner festlegen. |
| G004-13 | Applicable | Not Assessed | `agent-parity-review.md`, `documentation-review.md` | Maintainer; Learning/Security Review | Agentenflächen und DE/EN-Leserpfade prüfen; vor Übergabe; bei gemeinsamer Regel-/Textänderung. |
| G004-14 | Applicable | Not Assessed | `docs/accessibility/004-container-hardening-followup.md`, `learner-usability-review.md` | Learning/A11Y Review; unabhängiger Reviewer | Manuelle WCAG-/Erstnutzungsprüfung organisieren; vor A11Y-/unbegleitetem Erstnutzungsclaim; bei UI-/Dokumentationsänderung. |
| G004-15 | Applicable | Not Assessed | `platform-macos.md` | Maintainer; Platform Review | Nativen ARM64-Kandidaten getrennt prüfen; vor begrenzter technischer Übergabe; bei Head-/Imagewechsel. |
| G004-16 | Applicable | Not Assessed | `platform-windows.md` | Windows Platform Review; unabhängiger Reviewer | UPD-AMD64: echten Windows-Host/Podman-Lauf nachweisen; vor AMD64-Nutzungsclaim; bei Head-/Imagewechsel. Fehlender Runner bleibt Open/Blocked. |
| G004-17 | Applicable | Not Assessed | `platform-wsl2.md` | Ubuntu/WSL2 Platform Review; unabhängiger Reviewer | UPD-AMD64: getrennten rootless WSL2-Lauf nachweisen; vor AMD64-Nutzungsclaim; bei Head-/Imagewechsel. Fehlender Runner bleibt Open/Blocked. |
| G004-18 | Applicable | Not Assessed | `independent-review.md`, `handoff.md` | Repository Owner; unabhängiger Security Review | T068 und Übergabe nach eingefrorenem Paket; vor Handoff; nach jeder Korrektur neu prüfen. |

**Offene Spec-IDs:** O-344-TECH bleibt beim Maintainer bis aktuelle G01–G10-Belege vorliegen. O-344-HUMAN betrifft formelle Sandboxfreigabe, Rollen, Rechte, Datenschutz sowie Provider/Modell; nur zuständige Menschen können entscheiden. O-344-CLOUD betrifft Provider-/Registry-/Cloud-Anwendbarkeit mit Architecture Review. UPD-V2-LOOP und UPD-V2-AUDIT verlangen versionsgebundene OpenCode-2-Wirkungsnachweise; `session_coverage=not-exported` bleibt. DOC-A11Y verlangt manuelle Prüfung. UPD-AMD64 verlangt zwei getrennte native Plattformpfade. Alle offenen Punkte behalten eine Nutzungsgrenze vor der betroffenen Verwendung; Kalenderfristen für menschliche Entscheidungen setzt der jeweilige Owner, nicht der Agent.

## US1-Zwischencheckpoint / US1 interim checkpoint

**2026-10-31, begrenzter technischer Kandidat:** Der Audit-Stopp und die
30-Tage-Auswahl sind mit künstlichen Dateien und Fake-Compose eigenständig
prüfbar; [Review und Grenzen](audit-retention-review.md) nennen die
Phasen-/Teilfehler. Default und optionaler Read-only-Override sind als
Konfiguration getrennt. Keine Admin-Aktion oder Schutzumgehung ist Teil des
Lernenden-Normalablaufs. G004-07 und G004-03 bleiben bis zur vollständigen
Abnahme `Not Assessed`; ein synthetischer Test ist keine globale Freigabe.
Native Plattformbelege, vollständige OpenCode-2-Sitzungsabdeckung und der
betreute Pilot sind Open. US2, T063 und T068 werden dadurch nicht abgeschlossen.

**English:** The synthetic audit-stop and 30-day selection can be checked
independently with fake Compose and artificial files. The default and optional
read-only configuration are distinct. This is limited technical candidate
evidence, not administrative approval or a global release. Native platform
proof, OpenCode 2 session coverage and the supervised learner pilot remain
Open; US2, T063 and T068 are separate.

## Ergänzende Standards / Additional standards

| Standard oder Entscheidung | Anwendbarkeit und aktueller Stand | Owner, Aktion und Trigger |
| --- | --- | --- |
| NIST SSDF, CWE Top 25, OWASP Cheat Sheets/Proactive Controls | Applicable; Not Assessed | Maintainer und Security Review: Fassung und relevante Prozess-/Pfad-/Rechtefälle dokumentieren; vor Schlussreview, bei Standard-/Quellwechsel. |
| STRIDE, CIA, CAPEC und Zero Trust | Applicable; Not Assessed | Maintainer und Architecture/Security Review: Trust Boundaries und Angriffswege in T009 prüfen; vor Implementierungsdesign, bei Datenflusswechsel. |
| OWASP SAMM | Applicable als begrenzte Ist-/Zielanalyse; Not Assessed | Maintainer und Security Review: keine erfundene Organisationsreife; vor Schlussreview, bei Prozessänderung. |
| OWASP ASVS für neue eigene Web-/API-/Login-Dienste | N/A; Not Assessed | Maintainer: kein solcher eigener Dienst in diesem Sandbox-Feature; bei Aufnahme eines eigenen Dienstes neu bewerten. Bestehende externe HTTP-/CLI-Flüsse bleiben prüfpflichtig. |
| SBOM, Dependency Audit und OpenSSF Scorecard | Applicable; Not Assessed | Maintainer und Security Review: konkrete Quellen und finale Imagebindung prüfen; vor Weitergabe, bei Abhängigkeitswechsel. |
| VEX, SLSA und Signaturen | Applicable als Prüfung; Not Assessed | Maintainer und Security Review: konkrete Nachweise/fehlende Level offen führen; vor Image-/Releaseclaim, bei Build- oder Signaturwechsel. |
| Dependency-Track-Ingestion | Open; Not Assessed | Maintainer: vorhandenen zentralen Dienst und Zuständigkeit vor Weitergabe prüfen; bei neuem CVE-Dienst neu bewerten, keinen Dienst automatisch installieren. |
| Eigene Modell-/Trainings-AI-SBOM | N/A; Not Assessed | Maintainer und Provider/Rights Review: kein eingebettetes/eigenes Modell oder Training belegt; bei Modell-, Dienst- oder Inferenzintegration alle sieben Cluster neu prüfen. |
| DSGVO, KI-VO, CRA, NIS2/BSIG, DORA | Open; Not Assessed | Repository Owner und qualifizierter Privacy/Legal Review: pro Rolle/Land und Datum prüfen; vor betroffener Nutzung/Weitergabe, bei Rollen-/Rechtsänderung. Keine Rechtsfreigabe durch technische Prüfung. |
| C3A und C5 | Open; Not Assessed | Repository Owner und Architecture Review: Cloud-/Lieferantenscope, 30 C3A-Gruppen bei Anwendbarkeit, C5-Typ/Zeitraum prüfen; vor Cloud-/Provideränderung. |

## English

This is an initial work register, not an acceptance record. Applicability and implementation remain separate; every gate starts `Not Assessed`. Human decisions, missing native runners and manual accessibility evidence stay open with named owners and triggers. The due boundary for each human decision is before affected use or distribution; the responsible owner must set its calendar date. Later source, catalog, image or role changes require revalidation of affected records. No scan, file presence or hash alone marks a control fulfilled.
