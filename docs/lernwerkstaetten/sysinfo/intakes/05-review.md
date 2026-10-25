<!-- intake-authoring:begin -->
# SYS-05: Sicherheits- und Evidenzreview / Security and Evidence Review

## Deutsch

**Status:** ReadyForReview, Produktstufe Pending. Identität SYS-05; UUID im
Receipt. [basis.md](../basis.md) gilt; Vorbedingung SYS-04 abgenommen.
Ziel: seit Stufe 0 geltende Kontrollen nachweisen, keine nachträgliche Freigabe erfinden.

- FR-01: Gewählte generische Secure-Development-Basis und relevante Presets
  mit Version/Hash binden. AC-01: Projekt-Quelleninventar unterscheidet
  übernommene Quelle, lokale Anwendbarkeit, technische Evidenz und menschliches Urteil.
- FR-02: Kontroll-/Anforderungsmatrix mit stabilen IDs pflegen.
  AC-02: jede Anforderung aller sechs Stufen hat Evidenzpfad und aktuellen
  Status; Applicable, N/A und Open sind begründet, keine Installation gilt als Erfüllung.
- FR-03: Deltas von YAML, SQLite, REST und Dokumentation nachvollziehen.
  AC-03: Collector-Opt-in, Transaktion, REST-Grenze, Exportdaten und generierte
  Dokumentation sind mit realen Prüfungen oder offenen Maßnahmen verbunden.
- FR-04: Offene und menschliche Entscheidungen getrennt halten.
  AC-04: jeder Open/_TODO_-Punkt hat Owner, Follow-up und Trigger; formale
  Freigabe, Provider/Modell, Secrets, Plattformregeln und Register bleiben human-only.
- FR-05: Abschlussbericht und unabhängiges menschliches Review ermöglichen.
  AC-05: technische Regressionen und mindestens 80 % Coverage datiert belegt;
  nicht geprüfte Plattformen/A11Y bleiben Open. Kein pauschales compliant/approved.

**Artefakte:** Baseline, Matrix, Delta-Referenzen, Maßnahmenliste, Reviewbericht
und begrenzte Abschlussentscheidung. **Nicht-Ziele:** Sicherheitsmaßnahmen erst
jetzt implementieren, Zertifizierung, SBOM-/VEX-/SLSA-/AI-SBOM-Behauptung ohne
Nachweis, Produktivsetzung. Neue Produktlücken erfordern gesonderten Auftrag.
Lernfrage: Was unterscheidet Quellenübernahme, Prüfergebnis und Risikoakzeptanz?

## English

SYS-05 is ReadyForReview, Pending after SYS-04 acceptance. Review controls
that applied from stage 0; do not invent approval. FR/AC-01 binds generic
baseline/preset versions and separates source, applicability, evidence and
human judgement; 02 maps every stage's requirements to current evidence or
reasoned N/A/Open; 03 traces all feature deltas; 04 gives every open item an
owner/follow-up/trigger and preserves human-only decisions; 05 supplies dated
regressions, at least 80 % coverage and bounded independent human review.
Deliver baseline/matrix/deltas/actions/report. No certification, unsupported
supply-chain claims or production release. New remediation requires its own
authority. Explain source adoption versus verification versus risk acceptance.

<!-- intake-authoring:prompts -->
DE: Human-only-Punkte nicht schließen. EN: Never close human-only decisions.
<!-- spec-kit-command-id: speckit.specify -->
```text
$speckit-specify Nutze intakes/05-review.md und basis.md. Spezifiziere SYS-05 als projektspezifische Evidenzprüfung, nicht als formale Freigabe. Keine Implementierung, Risikoakzeptanz oder Remote-Schreibzugriffe.
```
<!-- spec-kit-command-id: speckit.autonomous -->
```text
$speckit-autonomous Nutze intakes/05-review.md und basis.md mit DeliveryMode LocalImplementation nach eigenem Auftrag und erfüllten Gates. Nur beauftragte Evidenzarbeit; kein Commit, Push, Container-Build, keine formale Freigabe oder Plattform-/Provideränderung.
```
<!-- intake-authoring:end -->
