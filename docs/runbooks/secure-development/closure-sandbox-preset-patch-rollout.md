# closure: technische Rollout-Nachpruefung / Technical rollout revalidation

Owner: @hindermath. Kontext / Context: sandbox-preset-patch-rollout. Mode: training.

DE: Pruefe genau dieses Gate nach der ausdruecklich autorisierten Installation.
Richtlinie und kontrollierte Quellen bleiben unveraendert. Der Baseline-Nachweis
bindet Dokumentidentitaet und Integritaet, nicht die Umsetzung aller Kontrollen.
Vergleiche alle Kontextdateien einschliesslich versteckter Dateien vor/nach dem
Aufruf ordinal nach relativem Pfad mit rohen SHA-256. Bei Drift oder Nonzero-Exit
stoppen. Keine Entscheidung oder Evidence durch den Review aendern.

EN: Review only this gate after the authorized installation. Preserve controlled
sources. Baseline proof establishes document identity/integrity, not complete
control implementation. Compare ordinal relative paths and raw SHA-256 for all
context files, including hidden files, before/after. Stop on drift/nonzero exit.
Review changes no evidence or human decision.

~~~bash
bash .specify/presets/secure-development-assurance-governance/scripts/validate-secure-development-assurance.sh review closure sandbox-preset-patch-rollout training
~~~

~~~powershell
pwsh -NoProfile -File .specify/presets/secure-development-assurance-governance/scripts/validate-secure-development-assurance.ps1 -Action Review -Gate closure -ContextId sandbox-preset-patch-rollout -Mode training
~~~

Erwartet / Expected: exit 0; negative fixture cases only in temporary copies: 2.
No new pilot, project, general-release, risk or certification authorization.
