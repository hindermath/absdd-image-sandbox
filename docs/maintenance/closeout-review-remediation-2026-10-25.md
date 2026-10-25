# Abschlussreview: IR201 und IR202 / Closeout Review Remediation

**Datum / Date:** 2026-10-25

## DE

Der Owner hat die gezielte Korrektur von IR201 und IR202 sowie die Fortsetzung
des Tagesabschlussplans ausdrücklich beauftragt. Das vorherige unabhängige
Vollreview `5fa23447-e96c-403c-b7da-79c506a11586` bleibt als historischer
`NeedsRemediation`-Nachweis erhalten und wird nicht nachträglich aufgewertet.

- **IR201:** Beide Normalstopp-Zeilen im Lernendenprofil verwenden den
  Audit-Wrapper ohne Volume-Löschung. Absichtliche Löschung benötigt einen
  getrennten Auftrag, ausdrückliche menschliche Zustimmung und vorherigen
  Audit-Export. Metadaten sind kein Backup. Eine statische Regression prüft
  beide Zeilen und lehnt drei destruktive Flag-Varianten ab.
- **IR202:** Das Profil trennt eingebundene Host-Verzeichnisse, beschreibbare
  Container-Dateien, temporäre Pfade und persistente Volumes. Container-
  Entfernung ist nicht dasselbe wie Stopp. Codex-Regeln bleiben zusätzliche
  agentenspezifische Grenzen, einschließlich der nicht automatisch erlaubten
  temporären Schreibpfade. Ein bilingualer Quellvertrag prüft diese Trennung.
- Die drei betroffenen Intake-Identitäten bleiben erhalten. Neue Operations-,
  Receipt- und Review-IDs ersetzen keine Archivhistorie; Vorstände werden
  byte-identisch archiviert, Quellen neu gebunden und die gesamte viergliedrige
  Reihe unabhängig vollständig reviewt.
- `Completed → Eligible → Blocked → Blocked` bleibt unverändert. Kein
  Produktlauf, keine neue Startautorität, keine Risikoannahme und keine
  formale Sandbox-, Rechts-, Provider- oder A11Y-Freigabe entstehen.
- Keine Runtime-/Build-Eingabe wird geändert. Der bereits geprüfte separate
  ARM64-Kandidat darf nur bei identischen 14 Build-Eingabehashes wiederverwendet
  werden. Der laufende Lerncontainer und seine sechs Volumes bleiben erhalten.

## EN

The owner explicitly authorized bounded correction of IR201 and IR202 and
continuation of the daily closeout plan. The previous independent full review
`5fa23447-e96c-403c-b7da-79c506a11586` remains historical `NeedsRemediation`
evidence; it is not retroactively upgraded.

- **IR201:** Both routine shutdown rows in the learner profile use the audit
  wrapper without volume removal. Deliberate removal needs a separate request,
  explicit human authorization and a prior audit export. Metadata is not a
  backup. A static regression checks both rows and rejects three destructive
  flag variants.
- **IR202:** The profile distinguishes exposed host directories, writable
  container files, temporary paths and persistent volumes. Container removal
  is not the same as stopping. Codex rules remain additional agent-specific
  boundaries, including temporary paths that are not automatically writable
  for Codex. A bilingual source contract checks these distinctions.
- The three affected intake identities remain unchanged. New operation,
  receipt and review IDs preserve archive history; exact preimages are archived,
  sources rebound and the complete four-member series independently reviewed.
- `Completed → Eligible → Blocked → Blocked` remains unchanged. This grants no
  product run, execution authority, risk acceptance or formal sandbox, legal,
  provider or accessibility approval.
- No runtime/build input changes. The existing separate ARM64 candidate may
  only be reused with identical hashes for all 14 build inputs. The running
  learner container and its six volumes remain unchanged.
