# Abarbeitungsreihenfolge der Sandbox-Intakes / Sandbox Intake Order

**Status:** aktiv / active

**Verbindliche Quelle / Binding source:** `specs/intake-series/sandbox-development-lifecycle/manifest.json`

## Zweck / Purpose

**DE:** Diese Datei erklaert die verbindliche Reihenfolge der aktiven
Sandbox-Intakes. Ein Intake ist ein geprueftes Anforderungsdokument fuer einen
spaeteren Spec-Kit-Lauf. Die Datei startet keinen Lauf. Der maschinenlesbare
Graph im Serienmanifest ist bei Abweichungen massgeblich.

**EN:** This file explains the binding order of the active sandbox intakes. An
intake is a reviewed requirements document for a later Spec Kit run. This file
does not start a run. If information differs, the machine-readable graph in the
series manifest is authoritative.

## Aktive Reihenfolge / Active Order

| Rang | Intake | Aufgabe | Status |
|---:|---|---|---|
| 1 | `Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md` | GSDB-Bestand und Luecken pruefen | ausfuehrbar / eligible |
| 2 | `Lastenheft_Secure-Development-Container-Hardening.md` | priorisierte technische Haertung umsetzen | blockiert / blocked |
| 3 | `Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md` | gehaertete Sandbox unabhaengig abnehmen | blockiert / blocked |
| 4 | `intakes/learner-fork-self-build-sandbox.md` | forkbare Selbstbau-Vorlage bereitstellen | blockiert / blocked |

## Abhaengigkeiten / Dependencies

1. Die GSDB-Bestandspruefung liefert die priorisierte Lueckenliste.
2. Die technische Haertung verwendet diese Liste als verbindliche Baseline.
3. Die Sandbox-Abnahme beginnt erst nach abgeschlossener Haertung.
4. Die Selbstbau-Vorlage wird erst nach erfolgreicher Abnahme bearbeitet.

*The GSDB assessment produces the prioritized gap list. Technical hardening
uses it as its baseline. Acceptance starts only after hardening is complete,
and the self-build template follows successful acceptance.*

## Archivierte oder ersetzte Lastenhefte / Archived or Superseded Requirements

- `Lastenheft_Sandbox-Public-Readiness.001-public-readiness.md` ist als
  abgeschlossene Feature-Eingabe archiviert.
- Die frueheren getrennten RL-SE-/Checklist- und allgemeinen
  Secure-Development-Hardening-Intakes sind in die GSDB-Bestandspruefung
  eingeflossen. Archive und Tombstones liegen unter `specs/`.

## Naechste Aktion / Next Action

Den Serienstatus schreibfrei pruefen:

```text
$speckit-intake-series-status specs/intake-series/sandbox-development-lifecycle/manifest.json
```
