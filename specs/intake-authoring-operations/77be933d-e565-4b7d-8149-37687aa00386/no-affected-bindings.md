# Kein betroffener Intake-Bezug / No Affected Intake Binding

## Deutsch

Die drei aktuellen Receipts enthalten je 71 Quellen. Weder
`scripts/hooks/pre-push` noch `scripts/tests/test_pre_push_secret_policy.py`,
Keynote-Binaerdateien oder das historische Security-Review vom 2026-10-25
sind direkte Quellen. Auch die aktuellen Serien-/Einzelreview-Requests und
-Ergebnisse sowie das Manifest enthalten keine zusaetzliche Bindung auf
diese Dateien. Der geplante neue Bericht
`docs/security/keynote-pin-review-2026-10-27.md` ist separate, ungebundene
Security-Evidenz und wird nicht still als neue Intake-Quelle aufgenommen.

21 Arbeitsbaum-Baseline-Dateien wurden byte-identisch gesichert. Das
Inventar mit Roh- und normalisierten SHA-256-Werten steht in `preflight.json`.
PowerShell pruefte alle 213 Quellenreferenzen, drei Intake-Ziele sowie
Manifest-/Review-Request-/Review-Zielbindungen. Sechs installierte
Bash-Validatoren bestaetigen die drei Receipts, Manifest, Serienreceipt
und das aktuelle Vier-Ziel-Review. Archivbytes und die untracked Logs
`2026-10-27-0747.md` und `2026-10-27-2219.md` bleiben unveraendert.

Nach dem gemeldeten Hook-/Test-Freeze umfasst der getrackte Diff nur diese
zwei Dateien. Deshalb: **kein Rebind, keine neuen Receipt-IDs, keine
Review-Supersession**. `Completed / Eligible / Blocked / Blocked` bleibt
erhalten. Dies ist nur eine Provenienz-Impactentscheidung: Die vom
Koordinator gemeldeten zehn erfolgreichen Code-Tests wurden hier nicht
wiederholt; unabhaengige Security-Pruefung, Liefergates und MergeAndSync
sind damit nicht abgeschlossen. Kein Commit, Push oder Runtime-Eingriff.

Zeitpraezision: Die Hook-/Test-Arbeitsbaumkopien entsprechen bereits den
finalen Dateien; sie belegen daher nicht deren Altbytes vor parallelen
Edits. Die echten Vorgaenger wurden gesondert aus dem anfangs sauberen,
aufgezeichneten HEAD `d48ce5f8bf0e5c3e612b4cc40fde0e5acf694240`
rekonstruiert und gegen exakte Git-Blob-IDs geprueft (`head-preimages/`).
Die urspruenglichen 21 Kopien wurden nicht ersetzt. Diese Abgrenzung
aendert die Entscheidung ohne betroffene Intake-Bindungen nicht.

## English

Each of the three current receipts binds 71 sources. The changed hook and
negative-test file, Keynote binaries, and historical security review are
not direct receipt sources. Current series/single review requests and
results and the manifest contain no additional binding to those files.
The planned new keynote-pin review is separate unbound security evidence,
not an implicitly added intake source.

Twenty-one working-tree baseline files were archived byte-for-byte; raw and
normalized SHA-256 values are in `preflight.json`. PowerShell verified all
213 source references, three intake targets, manifest, review request and
review targets. Six installed Bash validators passed for the receipts,
series and current four-target review. Archive bytes, historical security
review, and both protected untracked logs remain unchanged.

The frozen tracked diff contains only the hook and its negative tests.
Therefore no rebind, new receipt identities or review supersession is
needed. Preserve Completed / Eligible / Blocked / Blocked. This provenance
impact decision grants no security acceptance or delivery closure. The
coordinator reports ten passing code tests; this agent did not rerun them.
Independent security review and delivery gates remain separately owned.
No commit, push, runtime operation or MergeAndSync was performed here.

Timing precision: working-tree hook/test snapshots already match the final
files, so they do not prove old scanner/test bytes before concurrent edits.
Their actual predecessors were separately reconstructed from the recorded
initial clean HEAD and verified against exact Git blob IDs in
`head-preimages/`. Original snapshots were not replaced. This clarification
does not change the no-affected-intake-bindings decision.

## KEY-PIN-IR001: Begrenzter Nachtrag / Bounded Follow-Up

### Deutsch

Der unabhaengige Medium-Befund KEY-PIN-IR001 betrifft die Portabilitaet des
Tests: Alte Git-Blob-Objekte sind in flachen CI-Klonen nicht garantiert.
Der Koordinator meldet die Testkorrektur und das neue Reverse-Patch-Fixture
`scripts/tests/fixtures/keynote-previous-blobs.json`. Der korrigierte Test
prueft Eingabehash und rekonstruierten Vorgaenger-Blob. Diese Meldung ist
keine eigene Testausfuehrung oder Schliessung des Befunds durch die
Provenienzpflege; die unabhaengige Nachpruefung bleibt beim Reviewer.

Nur der Testhash und das neue Fixture wurden als Nachtrag aufgenommen.
Ihre exakten aktuellen SHA-256-Werte stehen in
`preflight.json` unter `boundedFollowUps[].currentFiles`.
Die begrenzte Pfadpruefung gegen drei Receipts sowie Manifest und
Review-Requests/-Ergebnisse findet weiterhin keine Bindung an Test oder
Fixture. **NoAffectedBindings** bleibt erhalten: kein neuer gebundener
Input, kein Rebind und keine Review-Supersession.

Die sechs Validatorresultate, die 213 Quellenpruefungen und die fruehere
Meldung von zehn erfolgreichen Code-Tests sind historische Evidenz des
initialen Preflights, keine frisch ausgefuehrten Pruefungen fuer den
korrigierten Test oder das Fixture. Keine Wiederholung dieser Kampagne,
keine neuen Archive und keine erneute rekursive Pruefung. Die bestehenden
21 Snapshots und HEAD-Vorgaenger wurden nicht veraendert; ihre bereits
dokumentierte Bytepruefung bleibt historische Evidenz.

### English

Independent Medium finding KEY-PIN-IR001 concerns test portability:
historical Git objects are not guaranteed in shallow CI clones. The
coordinator reports a corrected test and new reverse-patch fixture at
`scripts/tests/fixtures/keynote-previous-blobs.json`. The corrected test
checks the input hash and reconstructed predecessor blob. This provenance
follow-up neither executes those tests nor closes the finding; independent
verification and disposition remain with the reviewer.

Only the changed test hash and new fixture are recorded in the follow-up.
Exact current SHA-256 values are in
`preflight.json`, `boundedFollowUps[].currentFiles`.
Bounded path-membership inspection of three receipts, the manifest and
review requests/results finds no binding to either file. NoAffectedBindings
remains: no new bound intake input, rebind or review supersession.

The six validator results, 213 source checks and earlier ten-test report
are historical initial-preflight evidence, not fresh checks for the
corrected test or fixture. No repeated campaign, new archives or recursive
verification. Existing 21 snapshots and HEAD preimages remain untouched;
their previously recorded byte verification remains historical evidence.
