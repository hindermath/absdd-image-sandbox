# Preset- und Assurance-Prüfung / Preset and assurance review

## Deutsch

**Stand 2026-10-31: teilweise geprüft, G004-11 Open.** Die Repository-Dateien enthalten genau 14 Verzeichnisse unter `.specify/presets/`. Für jede Zeile stimmen `preset.id` und `preset.version` in `preset.yml` mit dem Register `scripts/config/spec-kit-project-statistics-governance-presets.json` überein (Registerversion mit führendem `v`). Die Priorität stammt aus dem Register; das Vorhandensein einer Datei beweist weder die effektive Spec-Kit-Aktivierung noch das Ergebnis des Presets. `.specify/extensions.yml` enthält `installed: []` für Extensions, was kein Beleg für Preset-Deaktivierung oder -Aktivierung ist.

| Priorität | Preset | Version im Register und Manifest |
| ---: | --- | --- |
| 10 | security-governance | 0.7.4 |
| 15 | secure-development-assurance-governance | 0.1.8 |
| 20 | architecture-governance | 0.6.5 |
| 30 | isaqb-architecture-governance | 0.2.5 |
| 40 | a11y-governance | 0.4.6 |
| 50 | cross-platform-governance | 0.2.5 |
| 60 | agent-parity-governance | 0.4.5 |
| 61 | model-routing-governance | 0.1.7 |
| 64 | intake-authoring-governance | 0.3.10 |
| 65 | intake-review-governance | 0.2.7 |
| 66 | intake-sequencing-governance | 0.2.11 |
| 70 | autonomous-run-governance | 0.4.8 |
| 80 | parallel-autonomous-run-governance | 0.2.9 |
| 90 | project-statistics-governance | 0.1.3 |

Die Plan-Tabelle nannte zunächst für `autonomous-run-governance` **0.4.7**; Register und lokales Manifest nennen **0.4.8**. Die Tabelle wurde auf den geprüften lokalen Stand korrigiert. Der Quellhash des Plans und alle davon abhängigen Gate-Bindungen müssen nach dieser Änderung erneuert werden. Es wurde kein Preset installiert oder aktualisiert.

Das Assurance-Preset 0.1.8 verlangt getrennte Baseline-, Delta-, Closure- und Image-Impact-Gates. Der reservierte Kontext `docs/security/secure-development/2026-10-26-004-container-hardening-followup/` ist noch nicht als ausgeführte Assurance-Evidenz vorhanden; sein Pfaddatum darf nicht als Ausführungsdatum gelten. Die lokalen Bash-/PowerShell-Validatoren sind vorhanden. T051 muss ihre fachlichen Mutationsfälle gegen frisch berechnete Hashes prüfen; T067 erstellt später den echten Kontext. Bis dahin sind die Kontrollabdeckung und ein `Ready`-Urteil offen. Vorhandene Security-, Architektur-, A11Y-, Plattform- und Statistik-Presets liefern getrennte Beiträge; aus der Reihenfolge allein entsteht keine Abnahme.

Der installierte Validator-Selbsttest `pwsh -NoProfile -File .specify/presets/secure-development-assurance-governance/tests/test-secure-development-assurance.ps1` bestand am 2026-10-31. Er meldete 47 neu gebundene Metadaten-Negativfälle je Shell, eindeutige Kontext-/ID-Prüfung, Dateisnapshots, vier Gate-Reviews sowie Bash-/PowerShell-Parität. Das belegt die synthetische Preset-Testmatrix, nicht den noch fehlenden Feature-004-Assurance-Kontext. Ein projektspezifischer Mutationsfall gegen Preset-Version 0.1.8/0.1.7 besteht in `scripts/tests/test_hardening_followup.py`; weitere in T051 verlangte projektspezifische Semantikvarianten bleiben offen.

**Folgearbeit:** Maintainer prüft effektive Aktivierung und die erneuerte Plan-/Gate-Bindung; Security Review prüft T051/T067. Regelmäßiger Review vierteljährlich, bei Quellen-/Profilwechsel und am 3. Oktober; vor einer Feature-Freigabe ist der aktuelle Anlassreview fällig. Keine automatische Aktualisierung, keine menschliche Freigabe durch diesen Text.

## English

**Status 2026-10-31: partial review; G004-11 Open.** All 14 local `preset.yml` files match the IDs and versions in the registry, with the registry's `v` prefix ignored for comparison. Priorities come from that registry; file presence does not prove effective Spec Kit activation or passing behavior. The plan's stale autonomous-run-governance 0.4.7 row was corrected to the reviewed registry/manifest value 0.4.8; refresh dependent hashes before fulfillment. No preset was installed or upgraded.

Assurance 0.1.8 has four separate gates. The reserved dated context has no executed evidence yet and its path date is not an execution time. T051 must run semantic positive and mutation cases against the installed validators; T067 later creates real context. Maintainer owns effective activation and plan binding, with Security Review of the cases and evidence. Review quarterly, on source/profile change and on 3 October. No `Ready` status or human approval is claimed here.

The installed validator's synthetic suite passed on 2026-10-31, including 47 rebound metadata negative cases per shell, unique context/ID checks, unchanged file snapshots, four gate reviews and Bash/PowerShell parity. A project-specific preset-version mismatch case also passes. The remaining project-specific semantic mutations requested by T051 and the real Feature 004 Assurance context are still Open.
