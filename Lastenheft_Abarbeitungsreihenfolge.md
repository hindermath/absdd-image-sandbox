# Lastenheft_Abarbeitungsreihenfolge

**Dokumenttyp:** Reihenfolge fuer spaetere Spec-Kit-Laeufe
**Status:** aktiv
**Stand:** 2026-06-29

## Zweck

Diese Datei merkt die aktive Reihenfolge fuer spaetere Spec-Kit-Laeufe. Sie
startet selbst keinen Lauf. Feature-Branch-spezifische Lastenhefte mit einem
Branch-Namen im Dateinamen, zum Beispiel `001-workspace-homogeneity-guardian`,
gelten als bereits einem Lauf zugeordnet und werden hier nicht erneut
einsortiert.

## Aktive Reihenfolge fuer spaetere Laeufe

1. `Lastenheft_Sandbox-Public-Readiness.md`
2. `Lastenheft_RL-SE-Checklist-Selbstpruefung.md`
3. `Lastenheft_Secure-Development-Container-Hardening.md`
4. `Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md`

## Hinweise fuer Agenten

- Nur Dateien nach dem Muster `Lastenheft*.md` pruefen.
- Bereits branch-spezifische Lastenhefte nicht erneut ausfuehren.
- Vor einem Lauf den aktuellen Repo-Stand, Branch und offene Diffs pruefen.
- Erst nach ausdruecklicher Freigabe einen Spec-Kit-Lauf starten.
- Public-Readiness, RL-SE-/Checklist-Selbstpruefung, Container-Hardening
  und Sandbox-Selbstpruefung sind getrennte Laeufe.


<!-- secure-development-hardening-order:start -->
## Automatisch ermittelte Lastenheft-Reihenfolge / Automatically Detected Requirements Order

Diese Tabelle wird aus `Lastenheft*.md` im Repository-Root erzeugt. Sie ist eine Vorbereitung fuer spaetere Spec-Kit-Laeufe und startet selbst keinen Lauf. Manuelle Projektentscheidungen ausserhalb dieses markierten Abschnitts bleiben erhalten.

*This table is generated from `Lastenheft*.md` in the repository root. It prepares later Spec Kit runs and does not start a run. Manual project decisions outside this marked section remain preserved.*

| Rang | Lastenheft | Gruppe | Status |
|---:|---|---|---|
| 1 | `Lastenheft_Sandbox-Public-Readiness.md` | Kernlogik/Runtime | aktiv / active |
| 2 | `Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md` | Kernlogik/Runtime | aktiv / active |
| 3 | `Lastenheft_RL-SE-Checklist-Selbstpruefung.md` | RL-SE-/Checklist-Selbstpruefung | aktiv / active |
| 4 | `Lastenheft_Secure-Development-Container-Hardening.md` | Weitere Anforderungen | aktiv / active |
<!-- secure-development-hardening-order:end -->
