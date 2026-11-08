# Abarbeitungsreihenfolge der Sandbox-Intakes / Sandbox Intake Order

## Aktueller Stand / Current state — 2026-10-28

DE: Der Nutzer hat den gemeinsamen Feature-Update-Block #101/#102/#104
nach dem Container-Hardening und vor der Selbstprüfung aufgenommen.
Das Serienmanifest ist maßgeblich. Die fünf Statuswerte lauten
Completed, Eligible, Blocked, Blocked, Blocked. Eligible bedeutet nur
nächster Kandidat; keine Implementierung oder Lieferung wird gestartet.

EN: The user admitted the combined #101/#102/#104 update after container
hardening and before acceptance. The manifest is authoritative. The five
states are Completed, Eligible, Blocked, Blocked, Blocked. Eligible selects
a candidate only; it grants no implementation or delivery authority.

## Reviewstand / Review state — 2026-11-08

DE: IR901–IR903 sind behoben. Das vollständige fünfgliedrige Nachreview ist Ready.
Der [aktuelle vollständige Prüfbericht](../../intake-review-reports/sandbox-development-lifecycle.md) und das JSON-Ergebnis sind
maßgeblich; vorbereitete Aufträge und ältere Ready-Ergebnisse sind keine
aktuelle Abnahme. Review-ID: `796186b3-1508-4e81-8dd4-8cf8ac968bfa`. Status und Implementierungsautorität
bleiben getrennt. Alle bisherigen Reviewstände sind bytegleich archiviert.

EN: IR901–IR903 are resolved; the complete five-member re-review is Ready. The current full
report and JSON result govern; prepared requests and older Ready results do
not establish current acceptance. The review ID is shown above. Review status
and implementation authority remain separate; prior evidence is archived exactly.

<!-- secure-development-hardening-order:start -->
## Verlinkte Lastenheft-Reihenfolge / Linked Requirements Order

Diese Tabelle wird aus dem kanonischen Series-Manifest und ausdruecklicher Feature-Evidence erzeugt. Vollstaendige Dateinamen, direkte eingehende Kanten und sichtbare Positionen bleiben erhalten. Manuelle Abschnitte ausserhalb dieses Markers bleiben unberuehrt.

*This table is generated from the canonical series manifest and explicit feature evidence. Complete filenames, direct incoming edges, and visible positions are preserved. Manual sections outside this marker remain unchanged.*

| Position | Status | Lastenheft/Intake | Abhängigkeiten / Dependencies | Spec-Kit-Feature |
|---:|---|---|---|---|
| 1 | Completed | [Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md](../../intake-authoring-archive/ec50344b-6a7b-45bf-b67c-a67f24f56c01/9d9fce68-15cc-490c-afe0-16b98eda8a54/Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md) | — (Root / keine direkte Abhängigkeit) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 2 | Eligible | [Lastenheft_Secure-Development-Container-Hardening.md](../../../Lastenheft_Secure-Development-Container-Hardening.md) | [Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md](../../intake-authoring-archive/ec50344b-6a7b-45bf-b67c-a67f24f56c01/9d9fce68-15cc-490c-afe0-16b98eda8a54/Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md) → current (`AssessmentBaseline`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 3 | Blocked | [Lastenheft_Sandbox-Feature-Update-Ubuntu2604-OpenCode-Web-MSL.md](../../../Lastenheft_Sandbox-Feature-Update-Ubuntu2604-OpenCode-Web-MSL.md) | [Lastenheft_Secure-Development-Container-Hardening.md](../../../Lastenheft_Secure-Development-Container-Hardening.md) → current (`SandboxBaseline`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 4 | Blocked | [Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md](../../../Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md) | [Lastenheft_Secure-Development-Container-Hardening.md](../../../Lastenheft_Secure-Development-Container-Hardening.md) → current (`SandboxBaseline`, binding: true)<br>[Lastenheft_Sandbox-Feature-Update-Ubuntu2604-OpenCode-Web-MSL.md](../../../Lastenheft_Sandbox-Feature-Update-Ubuntu2604-OpenCode-Web-MSL.md) → current (`SandboxBaseline`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 5 | Blocked | [learner-fork-self-build-sandbox.md](../../../intakes/learner-fork-self-build-sandbox.md) | [Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md](../../../Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
<!-- secure-development-hardening-order:end -->

## Bindende Abhängigkeiten / Binding dependencies

1. Die abgeschlossene GSDB-Prüfung liefert die Baseline für das Hardening.
2. Das Feature-Update benötigt das abgeschlossene Hardening.
3. Die Selbstprüfung benötigt sowohl Hardening als auch den vollständigen
   Feature-Update-Block auf der finalen gehärteten Image-Baseline.
4. Die Selbstbau-Vorlage benötigt die erfolgreich abgeschlossene Selbstprüfung.

EN: The completed GSDB assessment supplies hardening's baseline. The update
requires completed hardening. Acceptance requires both hardening and the
complete update on the final hardened image baseline. Self-build requires
completed acceptance. All three previous binding edges are retained; the
two added edges are hardening → update and update → acceptance.

```mermaid
flowchart TD
  GSDB["1. GSDB / Completed"] --> HARDEN["2. Hardening / Eligible"]
  HARDEN --> UPDATE["3. Feature-Update / Blocked"]
  HARDEN --> REVIEW["4. Selbstprüfung / Acceptance / Blocked"]
  UPDATE --> REVIEW
  REVIEW --> SELF["5. Selbstbau / Self-build / Blocked"]
```

## Herkunft, Archive und Grenzen / Provenance, archives and limits

DE: Die [Aufnahmeoperation](../../../specs/intake-series-operations/1cadc99c-e344-4fc9-9fa0-78414f2d82cd.json)
bindet den Nutzerauftrag, die unveränderten Vorgänger und den neuen Graph.
Die vorherigen Manifest-/Receipt-/Reihenansichten sowie alte Reviewstände
sind archiviert. Historische Detailnachträge bleiben in diesen Archiven
erhalten; sie werden nicht als neue Ergebnisse ausgegeben.
Die frühere GSDB-Root bleibt abgeschlossen; alte Befunde und menschliche
Gates werden nicht geschlossen. Keine formelle, Produkt-, A11Y- oder
Plattformfreigabe und kein neuer autonomer Lauf.

EN: The admission operation binds user authority, exact prior artifacts and
the new graph. Prior manifest/receipt/order views and review evidence are
archived. Historical detail notes remain there; no new result is inferred.
The GSDB root stays completed, with all existing human gates retained.
No formal, product, accessibility or platform approval or autonomous run.

## Nächste fachliche Aktion / Next substantive action

DE: Das vollständige fünfgliedrige Nachreview ist Ready. Als Nächstes ist die
schreibfreie Serienstatusprüfung vorgesehen; keine Implementierung wird gestartet.

EN: The complete five-member re-review is Ready. Next inspect series status
read-only; no implementation is started.

```text
$speckit-intake-series-status specs/intake-series/sandbox-development-lifecycle/manifest.json
```

IR801-Reparatur / IR801 repair: [Vertrag / Contract](../../../docs/maintenance/ir801-repair-2026-10-30.md). Alle fünf Statuswerte und Kanten bleiben unverändert / All five statuses and edges remain unchanged.
