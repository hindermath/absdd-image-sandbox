# GSDB-Bestandspruefung / GSDB Baseline Assessment

## Leserpfad und Zweck / Reader Path and Purpose

**DE:** Diese datierte Ablage ist die vollstaendige, assessment-only Bestandspruefung der Sandbox gegen die Generische Secure-Development-Basis (GSDB). Die GSDB ist eine organisationsneutrale Ausbildungs- und Pruefgrundlage. Beginne mit dieser README, oeffne danach die Evidenzmatrix, die priorisierte Lueckenliste und den Inventarabgleich. ssessment-results.json ist die kanonische, maschinenlesbare Quelle; alidation-results.json dokumentiert die ausgefuehrten Pruefungen.

**EN:** This dated directory is the complete assessment-only review of the sandbox against the Generic Secure Development Baseline (GSDB), an organisation-neutral training and review basis. Start here, then read the evidence matrix, prioritised gap list, and inventory reconciliation. ssessment-results.json is canonical; alidation-results.json records the executed checks.

## Ausgaben / Outputs

- [Kanonische Bewertung / Canonical assessment](assessment-results.json)
- [Evidenzmatrix / Evidence matrix](evidence-matrix.md)
- [Priorisierte Luecken / Prioritised gaps](prioritized-gap-list.md)
- [Inventarabgleich / Inventory reconciliation](inventory-reconciliation.md)
- [Dokumentationsauswirkung / Documentation impact](documentation-impact.json)
- [Validierungsbundle / Validation bundle](validation-results.json)

## Begriffe und Zustaende / Terms and States

**DE:** Draft bedeutet unvollstaendige Bewertung. ReviewPending bedeutet, dass 37 Quellen, 12 Checklisten, 157 Zeilen, Gaps, Inventar und lokale technische Gates vollstaendig dokumentiert sind, aber keine menschliche Baseline-Akzeptanz vorliegt. AcceptedBaseline darf nur nach dokumentierter Mitwirkung von Project Owner und Security Review gesetzt werden. Drift an Eingaben, Quellen, Scope oder Evidenz setzt den Stand wieder auf Draft.

**EN:** Draft means incomplete. ReviewPending means that 37 sources, 12 checklists, 157 rows, gaps, inventory, and local technical gates are complete, but human baseline acceptance is absent. AcceptedBaseline requires documented participation by the Project Owner and Security Review. Input, source, scope, or evidence drift returns the state to Draft.

**DE:** Open ist kein Pass. Es zeigt fehlende, widerspruechliche, nicht reproduzierbare, plattformbegrenzte oder Human-only-Evidenz. Jeder offene Punkt besitzt genau einen Gap mit Owner, Zieltermin und Trigger. Ein Gap erteilt keine Implementierungs-, Git-, Remote-, Bypass- oder Risikoakzeptanz-Autoritaet.

**EN:** Open is not a pass. It identifies missing, conflicting, non-reproducible, platform-limited, or human-only evidence. Every open item has exactly one gap with owner, target date, and trigger. A gap grants no implementation, Git, remote, bypass, or risk-acceptance authority.

## Exakte Zusammenfassung / Exact Summary

**DE:** Erfasst sind 37 Quellen, 12 Checklisten und 157 eindeutige CL-Zeilen. Alle 157 Zeilen bleiben konservativ Open; 157 reziproke P1-Gaps sind dokumentiert. Human-only-Zeilen: 49; nicht Human-only: 108. Quellen- und ID-Integritaet bestehen, zugleich bleiben Manifestdrift bei Richtlinie, Sammelband, CL-09 und CL-12 sowie der fehlende dokumentierte GSDB-Generator sichtbar offen. Alle Fehlerzaehler der strukturellen und semantischen Projektion sind 0.

**EN:** The assessment covers 37 sources, 12 checklists, and 157 unique CL rows. All 157 rows conservatively remain Open, with 157 reciprocal P1 gaps. Human-only rows: 49; not human-only: 108. Source and ID integrity pass, while manifest drift for the guideline, compendium, CL-09, and CL-12 and the documented but missing GSDB generator remain visibly open. All structural and semantic projection error counters are zero.

## Plattform- und Authority-Grenzen / Platform and Authority Boundaries

**DE:** macOS- und repository-lokale Pruefungen wurden ausgefuehrt. Der praktische Podman-Containercheck bleibt wegen des in dieser Sandbox nicht erreichbaren Maschinen-Locks und Endpunkts Open. Linux, Windows/WSL2, Provider, Hosting und externe Plattformdienste wurden nicht erfunden. Formale Freigaben, Secret-Aktionen, Plattformregeln, externe Register, Risikoakzeptanz und AcceptedBaseline bleiben Human-only.

**EN:** macOS and repository-local checks were executed. The practical Podman container check remains Open because this sandbox cannot access the machine lock and endpoint. Linux, Windows/WSL2, providers, hosting, and external platform services are not invented. Formal approvals, secret actions, platform rules, external registers, risk acceptance, and AcceptedBaseline remain human-only.

## Verifikation und Folgeabhaengigkeit / Verification and Follow-Up Dependency

**DE:** Die Befehle Q01 bis Q25 stehen unveraendert im [Feature-Quickstart](../../../../specs/002-gsdb-baseline-assessment/quickstart.md). Das Hardening-Lastenheft ist nur ein bedingter spaeterer Kandidat. Die erlaubte Zukunftskette lautet: dokumentierte AcceptedBaseline -> separat autorisiertes Intake-Series-Update -> Series-Statuspruefung -> read-only Anzeige des naechsten Kandidaten. Dieser Lauf hat keinen dieser Fortschrittsschritte ausgefuehrt.

**EN:** Commands Q01 through Q25 remain unchanged in the [feature quickstart](../../../../specs/002-gsdb-baseline-assessment/quickstart.md). The hardening requirements document is only a conditional later candidate. The permitted future chain is documented AcceptedBaseline, separately authorized series update, series-status validation, then read-only next-candidate listing. This run performed none of those advancement steps.
