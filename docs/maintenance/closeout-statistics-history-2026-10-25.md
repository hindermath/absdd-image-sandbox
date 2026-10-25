# Historische Statistik und Aktualität / Historical Statistics and Freshness

## Deutsch

**Entscheidung `DEC-STAT-HISTORY-2026-10-25`:** Der Repository Owner hat
ausdrücklich gewählt: Historie erhalten, Reproduzierbarkeit und aktuelle
Statistik getrennt prüfen. Diese Entscheidung betrifft die CI-Prüfsemantik
von PR #100, nicht eine Risikoannahme oder Produktfreigabe.

1. `docs/project-statistics-pilot/` bleibt byte-identisch erhalten. Jede
   Encoding-Variante muss die festgehaltene Messrevision und den Stichtag
   reproduzieren, ohne Dateien zu ändern. `reproducible=false`, unbekannte
   Zustände, falsche Revision/Stichtag, unpassende Exitcodes oder Schreibeffekte
   bleiben Fehler. `DRIFT` mit Exit 1 ist nur bei erfolgreicher Reproduktion
   und `current=false` zulässig; eine wirklich aktuelle Reproduktion müsste
   konsistent `CURRENT`, `current=true` und Exit 0 liefern.
2. Die aktive Profil-2-Statistik muss unabhängig davon `CURRENT`, Exit 0,
   Methodik 2 und `changed=false` melden. Beide vorhandenen Shell-Einstiege
   werden verwendet. Der historische Snapshot-Hash und der aktuelle Ledger-
   Hash erhalten getrennte Evidenzfelder. Reproduzierbarkeit ersetzt niemals
   Aktualität des aktiven Ledgers.
3. Bestehende Integritäts-, Encoding-, Raw-Blob-, Nichtschreib- und
   Abstammungsprüfungen bleiben bestehen. Kein allgemeines Akzeptieren von
   `DRIFT`, kein Überschreiben oder Neugenerieren des historischen Piloten.

Die Umsetzung erfolgt in einem temporären sauberen Git-Worktree. Parallel
geänderte lokale Keynote-Dateien werden weder verändert noch gestaged oder
in den PR aufgenommen. Workflow-/Test-Vorstände und gebundene Intake-Artefakte
werden archiviert, Quellenbindungen mit unveränderter Identität erneuert und
begrenzt unabhängig nachreviewt. Intake-Texte, sechs Folgeprompts, Lifecycle
und Startautorität bleiben unverändert. Kein Build, Neustart, globale Wartung,
Secret-/Providerkonfiguration oder Plattformregelwechsel.

## English

**Decision `DEC-STAT-HISTORY-2026-10-25`:** The repository owner explicitly
selected preservation of history with separate reproducibility and current
statistics checks. This changes PR #100 CI interpretation, not risk acceptance
or product approval.

1. Preserve the historical pilot byte-for-byte. Each encoding variant must
   reproduce its recorded revision and cutoff without writes. Reject failed
   reproduction, unknown states, wrong revision/cutoff, inconsistent exit codes
   or changed files. DRIFT/exit 1 is allowed only with reproducibility and
   current=false. A genuinely current replay must consistently return CURRENT,
   current=true and exit 0.
2. Independently require active Profile 2 statistics to report CURRENT, exit 0,
   methodology 2 and changed=false, using both existing shell entrypoints.
   Record historical snapshot and current ledger hashes separately.
   Reproducibility never substitutes for freshness of the active ledger.
3. Preserve installed integrity, encoding, raw-blob, write-free and ancestry
   checks. No blanket DRIFT allowance or regeneration of historical evidence.

Use a clean temporary worktree; leave parallel local Keynote edits unchanged
and outside the PR. Archive preimages and renew bound sources with preserved
intake identities and bounded independent follow-up. Intake texts, six prompts,
lifecycle and execution authority stay unchanged. No build/restart, global
maintenance, secret/provider configuration or platform-rule changes.
