# Feature 004: Architekturkontext und Entscheidungen / Architecture context and decisions

## Deutsch

**Stand:** 2026-10-31, Quellstand `51757c98f6a872419be6b9ae4d33685fe0782b67`. Dies ist der Entwurf vor Feature-004-Codeänderungen. Die aktuelle Spezifikation und [Kontrollmatrix](../../security/secure-development/004-container-hardening-followup/control-matrix.md) binden spätere Ergebnisse; frühere Architekturbelege sind Ausgangsquellen, keine neue Runtime-Abnahme.

### Kontext, Bausteine und Deployment

Ein Host betreibt rootless Podman und dessen Linux-VM, wo die Plattform sie benötigt. `Dockerfile` baut ein lokales Image mit sechs Sprachtoolchains, PowerShell, Agenten-CLIs und Helfern. `compose.yml` startet `ade` als `adedev`, bindet explizite Projekt- und Repository-Verzeichnisse ein und hält Build- und Agentenzustände in getrennten Volumes. Die Ports 5100–5199 sind an Host-Loopback gebunden. Der Build läuft zeitweise mit Root-Rechten im Image; der normale Containerprozess läuft ohne Root. `compose.home-baseline.yml` kann die eingebaute, schreibgeschützte Referenz durch einen gewählten beschreibbaren Fork ersetzen. Ein späterer optionaler Read-only-Override ist eine getrennte Variante, kein stiller Standardwechsel.

Textfolge: geprüfte Quellen und Pins → Image-Build → lokales Image → Compose-Start mit ausgewählten Bind-Mounts → Agenten-/Werkzeugnutzung → Audit-Metadatenexport → sichere 30-Tage-Auswahl → Stopp. Der Export-/Retention-/Down-Pfad muss bei unklaren oder fehlenden Belegen vor `down` abbrechen. Test- und Build-Kandidaten nutzen eigene Ressourcen, nicht die laufende Lernumgebung. Registry-Publikation ist nicht Teil von Feature 004.

| Baustein | Verantwortung | Vertrauensgrenze |
| --- | --- | --- |
| Host und Podman-VM | Image, Socket, Ressourcen und Mount-Quellen | Hostrechte und Podman-Endpunkt sind nicht durch Compose-Dateien allein bewiesen. |
| Image-Build | Toolchains, Downloads, Pins und Signaturen | Öffentliche Paketquellen und Buildskripte gelangen in das später privilegierte Image. |
| `ade`-Container | Lern- und Agentenprozesse als `adedev` | Non-root, `cap_drop: ALL`, `no-new-privileges`, aber beschreibbare Projekt-Mounts und freier Default-Egress. |
| Agentenzustand | Getrennte benannte Volumes | Zugangsdaten/Providerzustand bleiben vertraulich und außerhalb versionierter Belege. |
| Audit-Ziel | Metadaten unter `/audit` | Erfolg benötigt aktuellen, zugeordneten regulären Export; keine DB- oder Promptinhalte. |
| Host-Wartung | explizit ausgewählte Repositories und Werkzeuge | Vorschau und Check dürfen keine fremden Make-/Registry-Kommandos ausführen. |
| Projekt-Evidenz | Quellen, Tests, Plattform- und Reviewprotokolle | Hash und Existenz sind keine Wirksamkeit, Freigabe oder Rechtsentscheidung. |

### Qualitätsziele und Szenarien

1. **Geringste Rechte bei nutzbarem Standard:** Lernende können in deklarierten Projekt-Mounts arbeiten; unerlaubte Host- oder Agentenzustandszugriffe werden konkret geprüft. Default-Egress bleibt für das Lernprofil frei und wird als offene Schutzgrenze dokumentiert, nicht als nachgewiesene Allowlist.
2. **Reproduzierbare Herkunft:** Ein falscher Digest, Signierer oder unzulässiger Download bricht den Build beziehungsweise den isolierten Integritätstest ab. Ein passender Hash aus derselben kompromittierten Quelle ist kein unabhängiger Nachweis.
3. **Erhaltener Zustand:** Exportfehler, leere/fremde Auditdatei oder unsichere Pfadidentität verhindern Retention und `down`; normale Stopps erhalten alle Agentenvolumes. Ein Teilfehler berichtet tatsächlich entfernte alte Metadaten, ohne Rollback zu behaupten.
4. **Nachvollziehbare Bedienung:** Deutsche Hilfe steht zuerst, gleichwertiges Englisch folgt. Vorschau, Fehlerphase, tatsächlich erfolgte Aktionen und sicherer nächster Schritt sind textlich zugänglich; Farbe oder TUI sind Zusatzdarstellung.
5. **Plattformtreue:** Ein aktueller ARM64-Lauf auf macOS ist eigenständig. Windows/PowerShell/Podman und Ubuntu/WSL2/rootless Podman benötigen getrennte AMD64-Belege; fehlende Systeme bleiben Open/Blocked.

### arc42 §8: Sicherheitskonzepte

**Identität und Rechte:** Der Runtime-Benutzer ist `adedev`; `cap_drop: ALL`, `no-new-privileges` und Loopback-Ports sind deklarierte Mindestgrenzen. Der Host bestimmt die tatsächlichen Bind-Quellen und Rechte. Agentenkonfigurationen sind zusätzliche, versionsgebundene Kontrollen, keine Host-Sandboxgarantie. Persönliche Provideranmeldung, Modellwahl, formelle Freigabe und externe Register bleiben menschlich.

**Daten und Zustand:** Projektdateien und Agentenvolumes können vertraulich sein. Teste nur synthetische Daten. Audit exportiert Metadaten und behauptet für OpenCode 2 keine sitzungsbezogene Vollabdeckung (`session_coverage=not-exported`). Ein von Dateien oder Umgebungsvariablen umgelenkter Export muss dem beabsichtigten Mount und Tag zugeordnet werden; die Retention darf keine Links/Reparse-Points verfolgen.

**Kommunikation und Herkunft:** Default-Bridge und freier Egress sind eine bewusste Funktionsgrenze, keine akzeptierte allgemeine Risikoausnahme. Paketregister, Git-Quellen und optionale Anbieter sind getrennte Ziele. Versionen, Digests, Signatur- und TLS-Annahmen werden konkret geprüft. Ein neuer Egress-Zwang oder eine zentrale Allowlist ist hier nicht automatisch beschlossen.

**Nachweis und Fehler:** Tests erhalten exakte Revision, argv, Exitstatus, Runner, Architektur, Image-ID falls anwendbar und Hashes. Ein fehlender Test hat keinen Exit 0. Sicherheitsfehler stoppen vor destruktiven Aktionen; Logs und Berichte enthalten weder Secrets noch Prompt-/Antworttext. Die finale Image-SBOM, unabhängiger Review, Rechts-/Privacy-/A11Y-Bewertung und formelle Nutzungserlaubnis bleiben unterschiedliche Entscheidungen.

### Entscheidungen, Risiken und Schulden

- [S-ADR-003](../../security/adr/003-container-isolation.md) bleibt technische Richtung für rootless Podman und Runtime-Minimalrechte. Seine formelle Schutzstufenfreigabe bleibt Open. Feature 004 ergänzt einen optionalen Read-only-Override erst nach Schreibinventar.
- [S-ADR-004](../../security/adr/004-container-threat-boundaries.md) trennt Host, Build, Container, Mounts, Zustand, Audit und Provider. Freier Egress wird für den Standardbetrieb beibehalten und als offenes Risiko mit Owner geführt; er wird nicht als kontrolliert ausgegeben.
- [Vorherige Architektur](../container-hardening.md), [Qualitätsszenarien](../container-hardening-quality-scenarios.md) und [Wartungs-TUI](../maintenance-tui.md) sind historische bzw. angrenzende Belege. Veraltete T053- oder unbeschränkte-Egress-Aussagen darin werden nicht als Feature-004-Abnahme übernommen.
- Neue Sicherheitsbefunde aus Scan `4af7bffe-c319-4f8a-86b1-3a3623e50c5e` betreffen Make-Vorschau, Prompt-Argumente, Audit-Gate, Symlink-Pfade, Signatur-/Prüfsummenbindung und Wartungsressourcen. Sie werden vor dem finalen Code-Freeze einzeln geprüft und behoben oder offen disponiert.
- Technische Schulden: fehlende unabhängige Outcome-/Interface-Nenner, unbewiesene Windows-/WSL2-Pfade, optionale Provider-/Cloud-/Rechtsentscheidungen und fehlende echte OpenCode-2-Loop-/Sitzungswirkung. Keines dieser Themen ist durch dieses Dokument geschlossen.

## English

Feature 004 hardens a local rootless Podman learning sandbox. The host and VM own runtime and mount permissions; the image supplies toolchains and agent CLIs; Compose starts `ade` as `adedev` with explicit project mounts, separate state volumes, dropped capabilities, no-new-privileges and loopback ports. The default keeps writable paths and free egress for learning, with an optional restrictive profile reviewed separately. Build/download sources, host maintenance, agent state, audit metadata and external providers are distinct trust boundaries. The text sequence above covers source checks, build, start, use, export, retention and stop. Tests need synthetic state and exact source, runner and outcome evidence. Existing security ADRs remain technical design sources, while formal approval, legal/privacy/A11Y decisions and missing native platforms stay open. A hash, scan or successful local test is not a general release or usage approval.
