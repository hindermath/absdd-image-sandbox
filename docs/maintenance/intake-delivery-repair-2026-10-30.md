# Begrenzte Lieferreparatur / Bounded delivery repair

## Bestätigter Vertrag / Approved contract

DE: Der Owner hat den konkret vorgelegten Reparaturvertrag ausdrücklich mit
„Reparaturfreigabe erteilt“ bestätigt: ausschließlich drei Markdown-Hardbreak-
Stellen im aktiven Feature-Update formatneutral korrigieren; Vorstände
bytegleich archivieren; betroffene Intake-/Serien-/Reviewbindungen erneuern
und vollständig nachreviewen. Die neun durch Archivverschiebung betroffenen
Links in drei exakt benannten unveränderlichen Archivdateien erhalten eine
eng begrenzte hashgebundene CI-Prüfung im ursprünglichen Dokumentkontext.
Keine Archivbytes ändern, keine pauschale Linkprüfung deaktivieren.
Danach den bereits beauftragten MergeAndSync-Abschluss mit Admin-Bypass
fortsetzen. Technische Fehler oder umsetzbare Reviewbefunde nicht umgehen.

EN: The owner explicitly approved the quoted bounded repair contract: correct
only three Markdown hardbreak locations without changing the active update's
meaning; preserve preimages, renew affected intake/series/review bindings and
perform the complete re-review. Check nine relocation-relative links in
exactly three immutable archive files through hash-bound CI validation in
their original document contexts. Do not rewrite archives or broadly disable
link checks. Then continue previously authorized MergeAndSync with admin
bypass, without bypassing technical errors or actionable review findings.

## Umfang und Nachweisgrenzen / Scope and proof boundaries

DE: Nur das Update-Lastenheft ändert sechs Leerzeichen an drei Stellen;
alle Anforderungen, Abnahmen, Prompts und fünf Lifecycle-Werte bleiben.
Die drei anderen aktiven Receipts binden zusätzlich den geänderten
Dokumentationsworkflow und werden deshalb ebenfalls kontrolliert erneuert;
ihre Zieltexte bleiben bytegleich. Ursprüngliche Quellenreihenfolgen bleiben
nach archiviertem Vorgänger und diesem Vertrag erhalten, betroffene aktuelle
Dateiquellen bekommen ihren neuen Hash. Frühere Ready-Ergebnisse bleiben
historisch, bis ein neues vollständiges Fünferreview alle Ziele beurteilt.

EN: Only the update intake changes six spaces at three locations. Preserve
all requirements, acceptance, prompts and five lifecycle states. Three other
active receipts also bind the changed documentation workflow, so renew them
under the same bounded contract without changing their targets. Keep prior
source order after the archived predecessor and this contract; update hashes
only for affected current file sources. Preserve previous Ready as history
until a new complete five-member review evaluates every target.

## Archiv-Linkprüfung / Archive link checks

DE: Kanonisches Manifest: `scripts/config/archived-markdown-links.json`.
Prüfer: `scripts/check-archived-markdown-links.ps1`, mit vollständiger
PowerShell-Hilfe; isolierte Regressionen unter `scripts/tests/`.
Host/CI mit PowerShell 7, Repository-Wurzel:

```powershell
pwsh -NoProfile -File scripts/tests/test-archived-markdown-links.ps1
pwsh -NoProfile -File scripts/check-archived-markdown-links.ps1 -Repo .
```

DE: Erwartet wird Pass für drei Originalhashes und neun vorhandene Zielpfade.
Hashänderung, falscher Quellkontext, fehlendes Ziel, Pfadausbruch und ungenaue
Ausnahmen sind Fehler; nicht durch Neu-Pinnen ungeprüfter Bytes „beheben“.
Die normalen Lychee-Prüfungen bleiben für alle anderen Dokumente aktiv.
Diese Prüfung belegt Dateilinks, nicht historische technische Abnahme oder
Aktualität des referenzierten Inhalts; keine Netzwerk-/Runtimeoperation.

EN: From the repository root on a host/CI with PowerShell 7, run the commands
above. Expect three original hashes and nine existing local target paths.
Changed bytes/context, missing destinations, path escape and non-exact
exclusions fail. Never re-pin unreviewed bytes to obtain a pass. Lychee
continues checking all other documents. This proves file destinations, not
historical technical acceptance or current linked content; no network/runtime
operation is involved.

Documentation Impact: UpdateRequired. Owner: Maintainer. Audiences: maintainers
and intake reviewers. Canonical sources: approved contract, hash manifest,
current receipts and complete review result. Existing order/review reader
paths remain canonical. German-first/equivalent English, text-oriented;
sourceOnly, no Home sync. Reevaluate after archive/context/workflow/source
changes. Feature 004 implementation and all human gates remain separate.
