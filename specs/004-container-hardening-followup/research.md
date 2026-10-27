# Research: Härtungsnachlauf / Hardening Follow-Up

**Date**: 2026-10-26. **Basis**: [Spec](spec.md), sieben committed
Clarifications und aktuell validierte Intake-Quellen. / Seven committed
clarifications and current validated intake inputs.

DE: Recherche bedeutet hier Quellen-/Codelektüre, keine ausgeführten Tests.
Open-Entscheidungen sind benannte Folgearbeit, keine verschwiegenen technischen
Unbekannten. Keine Neuinstallation oder Versionsaktualisierung.
EN: Research here is source/code inspection, not test execution. Explicit
Open decisions remain follow-up work rather than hidden design uncertainty.
No installation or version upgrade is performed.

## R01: Bestehendes System weiterverwenden / Reuse Existing Boundaries

- **Decision**: DE: Wrapper-Paare und Python-Kern weiterverwenden; explizite
  Featureauswahl ergänzen statt Feature-003-Konstanten umzuschreiben.
  EN: Reuse paired wrappers/core with explicit feature selection, not changed
  historical defaults.
- **Rationale**: DE: `scripts/lib/secure_development_hardening.py` und dessen
  Tests binden historische Schema-/Evidencepfade. Der neue Auftrag erteilt
  keine rückwirkende Feature-003-Abnahme. EN: Existing validators/tests bind
  historical contracts; the new feature cannot reinterpret prior acceptance.
- **Alternatives considered**: DE: generisches neues Prüf-Framework oder
  blindes Kopieren aller Skripte; verworfen wegen Drift und unnötiger Fläche.
  EN: Reject a new framework or wholesale copies as unnecessary drift risk.

## R02: Retention als kleiner gemeinsamer Kern / Small Shared Retention Core

- **Decision**: DE: 30 Tage anhand eines einmaligen UTC-Tages, strikte
  ISO-Tagesdateien, nur reguläre direkte Dateien im verifizierten Audit-Mount;
  Export → Retention → Down. Fehler verhindern Down. Python-Standardbibliothek
  für Auswahl/Typ-/Pfadprüfung, je Wrapper identische Semantik und Dry-run.
  EN: Use one UTC date, strict direct regular ISO-day files, verified audit
  mount, export then retention then down, failing closed on error, with a
  small standard-library core and equivalent dry-run behavior.
- **Rationale**: DE: FR-006/SC-002 legen Frist und Exportvorbedingung fest.
  Shellabhängige Datumsarithmetik und ein pauschales Dateiglob würden
  Grenzfälle/Links unterschiedlich behandeln. EN: Clarified retention/export
  requirements need consistent calendar and containment rules.
- **Alternatives considered**: DE: mtime, rekursives Cleanup, DB-Abfrage,
  Container-Entrypoint als alleinige Garantie: verworfen. EN: Reject mtime,
  recursive cleanup, database queries and entrypoint-only guarantees.

## R03: Messwerte nicht verwechseln / Do Not Equate Different Coverage Metrics

- **Decision**: DE: Python-Zweige mit `coverage.py --branch` und
  `covered_branches / num_branches` pro Modul aus JSON messen, nicht die
  kombinierte Prozentzahl als reine Branchquote verwenden. Alle Inventar-
  Module behalten, auch unimportierte. Subprozesse ebenfalls instrumentieren
  oder deren fehlenden Umfang Open führen. Bash-/PowerShell-Zweigbelege aus
  vollständigem Entscheidungs-/Outcome-Register mit ausführbaren Fixtures
  und nachvollziehbarem Trace; Line-/Command-Coverage nur ergänzend.
  EN: Measure Python branch numerator/denominator from JSON per module,
  retaining unimported modules and child-process gaps. Use explicit complete
  decision/outcome catalogs with fixture execution evidence for shell/
  PowerShell; line/command coverage is supplementary, never equivalent.
- **Rationale**: DE: Die offizielle [coverage.py-Dokumentation](https://coverage.readthedocs.io/en/latest/branch.html)
  beschreibt Zielübergänge; [Pester](https://pester.dev/docs/usage/code-coverage)
  beschreibt ausgeführte Zeilen/Commands. Das belegt keine austauschbaren
  Branch-Nenner. EN: Official documentation distinguishes executed branch
  destinations from command/line coverage; these metrics are not interchangeable.
- **Alternatives considered**: DE: Testanzahl, 85 % Zeilenabdeckung oder
  erfolgreiche Tests als Quotenersatz: verworfen. Fehlende vertrauenswürdige
  Messung bleibt Open, keine neue Sprache nur für Instrumentierung.
  EN: Reject test counts, line percentages or pass totals as branch proxies.
  Missing credible measurement stays Open without introducing a new language.

## R04: Defaults erhalten, Variante gezielt prüfen / Preserve Defaults

- **Decision**: DE: freie Standard-Egress-Verbindungen und beschreibbare
  Root-Schicht erhalten; Portbindung lokal. Optionaler Read-only-Override,
  keine implizite Einführung bei Build/Start. EN: Preserve egress/writable
  defaults and loopback ports; read-only remains an explicit optional override.
- **Rationale**: DE: Die Clarifications entscheiden dies; `compose.yml`
  enthält bereits cap_drop ALL, no-new-privileges und getrennte Mounts.
  Beleg statt pauschaler Neuerstellung. EN: Clarifications and existing
  safeguards favor evidence-led changes rather than replacement.
- **Alternatives considered**: DE: Standard read_only, Egress-Allowlist,
  Kernel-Sonderrechte: nicht beauftragt. EN: Default read-only, egress allowlist
  and special kernel privileges are outside the chosen scope.

## R05: Plattformbeleg ist kein portabler Erfolgsstempel / Platform Proof Is Scoped

- **Decision**: DE: native ARM64-Mindestabnahme; Windows und WSL2 als eigene
  AMD64-Kontexte, gleiche Hardware zulässig, gleiche Evidence unzulässig.
  CI kann eng begrenzte Prüfungen beitragen, keinen Desktop-Attach beweisen.
  EN: Real ARM64 minimum, distinct Windows/WSL2 evidence, shared hardware but
  never shared results; bounded CI does not prove desktop attach.
- **Rationale**: DE: FR-013 und geklärtes SC-007; die frühere Feature-003-
  Scopeentscheidung ist historische Referenz, keine neue pauschale Ausnahme.
  EN: Current spec/clarifications govern, not an automatically extended old waiver.
- **Alternatives considered**: DE: Emulation/Rosetta, native Linux-Hardware
  verlangen oder Windows-Ergebnisse nach WSL2 kopieren: verworfen.
  EN: Reject emulation, unavailable native hardware requirements and copied proof.

## R06: Quellenfrische und Assurance getrennt / Provenance and Assurance

- **Decision**: DE: Intake und Review unverändert lassen; Planungsautorität
  erlaubt keine neue Bindung. Assurance 0.1.8 mit exaktem datierten Kontext,
  separaten Baseline/Delta/Closure/Image-Impact-Nachweisen. Markdown-Evidenz
  behält die Spec-Pfade; datierte JSON-Gates werden verlinkt.
  EN: Preserve intake/review bindings; use dated Assurance gates linked from
  the specified readable evidence paths.
- **Rationale**: DE: Aktueller Receipt-Validator bestätigt 67 Quellen; das
  Reihenreview ist Ready. Der installierte Assurance-Vertrag verlangt exakt
  gebundene aktive Metadaten und datierten Kontext. Integrität ist nicht
  fachliche/rechtliche Freigabe. EN: Current bindings pass; Assurance requires
  exact active metadata and context, without granting human authority.
- **Alternatives considered**: DE: historische JSON passend machen,
  Organisationstext im schemafesten ExternalComparison-Feld austauschen oder
  fehlende Human-Gates als Ready markieren: verworfen. EN: Reject rewritten
  historical records, altered contract constants or invented approvals.

## R07: Verwundbarkeit und Nutzung getrennt entscheiden / Separate Scan and Authority

- **Decision**: DE: geklärte Critical-/High-Schwelle unverändert, jedes VEX/
  Open mit konkreter CVE-/Komponentenbindung. Keine Agenten-Risikoannahme.
  Lokale SBOM und Scan auf genau dasselbe Image und Architektur beziehen.
  EN: Preserve clarified Critical/High policy with exact finding/VEX/Open
  links, no delegated human risk acceptance, and exact image/SBOM binding.
- **Rationale**: DE: Existierende `build-and-sbom.*` und `analyze-sbom.*`
  liefern wiederverwendbare Pfade; historische Ergebnisse sind keine aktuelle
  Abnahme. EN: Reuse existing tooling, not historical success as current proof.
- **Alternatives considered**: DE: neueste SBOM stillschweigend auswählen,
  pauschales VEX not_affected oder weitere Registryverteilung: verworfen.
  EN: Reject implicit newest-file selection, blanket VEX and registry rollout.

## Offene fachliche Nachweise / Open Domain Evidence

DE: Kein technischer Architekturpunkt bleibt als unaufgelöster Platzhalter.
O-344-HUMAN/CLOUD, UPD-AMD64/V2-LOOP/V2-AUDIT/SMOKE-WARN, DOC-A11Y und
UPD-APPROVAL sind konkrete Folgeprüfungen mit Owner/Trigger aus der Spec.
Coverage-Instrumentierung wird erst im autorisierten Implementierungslauf
bewiesen; bis dahin ist Erfüllung Not Assessed, nicht behauptet.
EN: No unresolved technical placeholder remains. Explicit human/cloud/platform/
agent/warning/accessibility items retain their spec owners/triggers.
Measurement itself needs later proof; implementation remains Not Assessed.
