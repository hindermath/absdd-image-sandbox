# Lastenheft-Abarbeitungsreihenfolge / Requirements Processing Order

DE: Der [Maven-Quellenabgleich](../../../docs/maintenance/maven-fallback-intake-alignment-2026-10-25.md) erneuert ausschliesslich Quellenbindungen und Review; Reihenfolge, Status und Startautoritaet bleiben unveraendert.

EN: Maven source alignment refreshes source bindings and review only; order, lifecycle and execution authority remain unchanged.


Diese Datei haelt die sichtbare Abarbeitungsreihenfolge der vorhandenen Lastenhefte fest. Sie ist eine Vorbereitung fuer spaetere Spec-Kit-Laeufe und startet selbst keinen Lauf.

*This file records the visible processing order of existing requirements documents. It prepares later Spec Kit runs and does not start a run by itself.*

## Quellenabgleich 2026-10-25 / Source Alignment 2026-10-25

DE: Die [Review-Korrektur](../../../docs/maintenance/sandbox-current-state-2026-10-25.md)
erneuert Quellen und das separat gefuehrte Vollreview, nicht die Lifecycle-
Status oder Startautoritaet. Completed, Eligible, Blocked, Blocked bleibt erhalten.

EN: Review correction refreshes sources and the separately recorded full
review, not lifecycle or execution authority. Preserve Completed, Eligible,
Blocked, Blocked.

DE: Der [Dokumentationsabgleich](../../../docs/maintenance/documentation-alignment-2026-10-25.md)
bindet zusaetzlich aktuelle Guidance und offene Werkzeug-Nachpruefungen,
ohne Statusfortschritt oder Startfreigabe.

EN: Documentation alignment additionally binds current guidance and open
toolchain follow-ups without lifecycle advancement or execution authority.

DE: Die drei aktiven Intakes beziehen GSDB 3.4.4 und Assurance 0.1.8 ueber
den [Delta-Abgleich](../../../docs/maintenance/intake-gsdb344-delta-2026-10-21.md).
Der [aktuelle Quellenabgleich](../../../docs/maintenance/intake-sources-alignment-2026-10-25.md)
erneuert die Werkzeug-/Guidance-Bindung, nicht die Kontroll-Erfüllung.
Die abgeschlossene historische Root und die Statusfolge bleiben unveraendert.
Review-Bereitschaft ist keine Ausfuehrungsfreigabe.

EN: The three active intakes consume GSDB 3.4.4 and Assurance 0.1.8 through
the linked delta alignment. The completed historical root and lifecycle
statuses remain unchanged. Review readiness grants no execution authority.
The current source alignment refreshes tool/guidance bindings, not control
fulfillment.

<!-- secure-development-hardening-order:start -->
## Verlinkte Lastenheft-Reihenfolge / Linked Requirements Order

Diese Tabelle wird aus dem kanonischen Series-Manifest und ausdruecklicher Feature-Evidence erzeugt. Vollstaendige Dateinamen, direkte eingehende Kanten und sichtbare Positionen bleiben erhalten. Manuelle Abschnitte ausserhalb dieses Markers bleiben unberuehrt.

*This table is generated from the canonical series manifest and explicit feature evidence. Complete filenames, direct incoming edges, and visible positions are preserved. Manual sections outside this marker remain unchanged.*

| Position | Status | Lastenheft/Intake | Abhängigkeiten / Dependencies | Spec-Kit-Feature |
|---:|---|---|---|---|
| 1 | Completed | [Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md](../../intake-authoring-archive/ec50344b-6a7b-45bf-b67c-a67f24f56c01/9d9fce68-15cc-490c-afe0-16b98eda8a54/Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md) | — (Root / keine direkte Abhängigkeit) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 2 | Eligible | [Lastenheft_Secure-Development-Container-Hardening.md](../../../Lastenheft_Secure-Development-Container-Hardening.md) | [Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md](../../intake-authoring-archive/ec50344b-6a7b-45bf-b67c-a67f24f56c01/9d9fce68-15cc-490c-afe0-16b98eda8a54/Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md) → current (`AssessmentBaseline`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 3 | Blocked | [Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md](../../../Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md) | [Lastenheft_Secure-Development-Container-Hardening.md](../../../Lastenheft_Secure-Development-Container-Hardening.md) → current (`SandboxBaseline`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 4 | Blocked | [learner-fork-self-build-sandbox.md](../../../intakes/learner-fork-self-build-sandbox.md) | [Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md](../../../Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
<!-- secure-development-hardening-order:end -->
