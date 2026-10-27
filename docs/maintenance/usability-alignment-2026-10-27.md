# Usability-Abgleich / Usability Alignment

## Deutsch

**Auftrag:** Owner bestätigt am 2026-10-27: gesichtete Dokumente zuerst
gezielt committen, danach Usability-Ergänzungen und Quellenbindungen mit
unabhängigem Vollreview pflegen. Ausgangscommit `596b4ca`; kein weiterer Commit
oder Push. Kein Hardening-Code, Container-Build, Stopp, Start oder Neustart.

- Feature 004 präzisiert FR-012/SC-006 statt neue Anforderungen oder ein neues
  Feature zu erzeugen. Die 15 FR, acht SC, sieben Owner-Clarifications,
  Sicherheitsgrenzen und 85-/80-Prozent-Schwellen bleiben erhalten.
- `docs/fuer-lernende/erste-schritte.md`: eine gewählte Aufgabe, Python als
  Beispiel ohne KI-Konto, Vollabnahme bei Maintainer-Betrieb statt am ersten Tag.
- `docs/fuer-lernende/alltag.md`: speichern, auditgesichert stoppen und
  wieder öffnen; keine pauschale Datenerhaltungszusage für Container-Schreibschichten.
- `docs/fuer-lernende/troubleshooting.md`: Machine-Zustand erst diagnostizieren,
  keine pauschale Lösch-/Reset-Anleitung. Sichere Export-/Retention-/Sperrhilfe
  unterscheidet vorhandenes Verhalten von erst geplanter Feature-004-Funktion.
- Fail-closed, Rootless/Non-root, Agentenregeln, Datenminimierung und
  menschliche Freigaben bleiben verbindlich. Keine automatische Entsperrung,
  erweiterte Rechte oder Audit-Umgehung als Komfortfunktion.
- Bestehende gemeinsame Agentenregeln werden konkretisiert, nicht geändert;
  kein neues Agenten-Routing und keine zweite Lernreihenquelle.
- Der Pilot bleibt **Open**: Owner Learning/A11Y Review; Follow-up freiwilligen
  betreuten Pilot mit synthetischen Daten organisieren; Trigger vor Behauptung
  selbständiger Erstnutzung. Alle vier IT-Berufe einschließlich vier
  Fachinformatik-Fachrichtungen im Abdeckungsplan; unbesetzte Bezüge explizit offen.
  Normalablauf ohne Admin/Schutzumgehung, Fehlerfall mit sicherer Hilfe.

Die drei aktiven Intakes erhalten archivierte Vorstände und aktuelle Quellen;
Identitäten und `Completed → Eligible → Blocked → Blocked` bleiben erhalten.
Die abgeschlossene GSDB und Feature 003 bleiben unverändert. Erst ein
unabhängiger vollständiger Text-/Reihenreview darf den aktuellen Reviewstatus
feststellen. Gültige Hashes beweisen weder Usability noch technische Abnahme.

## English

**Authority:** On 2026-10-27 the owner authorizes one scoped commit of reviewed
documents, then usability text, provenance renewal and an independent full
review. Baseline commit 596b4ca; no further commit or push. No hardening code,
container build, stop, start or restart.

- Feature 004 refines FR-012/SC-006 rather than adding new requirements or a
  feature. Preserve 15 FRs, eight SCs, seven owner clarifications, security
  boundaries and 85/80 percent thresholds.
- First steps: one selected task, Python as an account-free example, with full
  acceptance assigned to operations maintainers rather than day-one learners.
- Daily workflow: save, audit-stop and reopen; no blanket persistence promise
  for files in the container writable layer.
- Troubleshooting: diagnose machine state first, without generic reset/removal
  recipes. Export/retention/lock guidance distinguishes installed behavior from
  planned Feature-004 functionality.
- Preserve fail-closed operation, rootless/non-root identity, agent rules,
  data minimization and human approvals. No automatic unlocking, extra
  privileges or audit bypass for convenience.
- Clarify existing shared agent rules without changing them; no new routing
  or duplicate learning-series source.
- Pilot remains **Open**, owned by Learning/A11Y Review. Organize voluntary
  supervised participation using synthetic data; reevaluate before claiming
  independent first use. Plan all four occupations and four IT specialist
  tracks, keeping unobserved coverage explicit. Ordinary flow needs no admin
  or bypass; failure recovery may need safe assistance.

Archive previous versions and renew sources for the three active intakes,
preserving identities and Completed → Eligible → Blocked → Blocked. Leave
completed GSDB and Feature 003 unchanged. Only independent full substantive
intake/series review establishes the current review result. Current hashes
prove neither usability nor technical acceptance.
