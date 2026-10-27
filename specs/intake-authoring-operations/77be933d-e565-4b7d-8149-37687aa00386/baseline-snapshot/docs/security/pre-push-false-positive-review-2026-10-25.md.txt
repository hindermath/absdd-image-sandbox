# Pre-Push-Nachreview / Pre-Push Follow-Up Review

## Deutsch

### Ergebnis und Scope

**Ready fuer den begrenzten Hook-Delta**: keine offenen Findings; PP201 und
PP202 sind ResolvedAndVerified. Keine Risikoakzeptanz oder allgemeine
Security-/Produktfreigabe. Datum: 2026-10-25.

Geprueft: scripts/hooks/pre-push, scripts/tests/test_pre_push_secret_policy.py
und der eigene Deltaanteil in .git/hooks/pre-push. Der Reviewer verfasste
keine dieser Korrekturen und aendert ausschliesslich diesen Bericht.
Kein neues Intake-Review, keine Builds, Runtime-, Git- oder Journalmutation.
Die bisherige vollstaendige Intakepruefung wird nicht neu ausgefuehrt;
Parent bestaetigt deren 260 unveraenderte gebundene Inputs.

### PP201: ResolvedAndVerified

- Kategorie: SecretDetectionCorrectness; urspruengliche Severity: Medium.
- Location: beide Hooks, Zeile 13; Testmethode
  test_quoted_leading_whitespace_and_empty_assignments_fail_closed.
- Historischer Befund: Das wertparsende Feldmuster uebersah zitierte,
  nichtleere Werte mit fuehrendem Leerraum. Eigener minimaler Bash-/grep-
  Nachweis bestaetigte damals den fehlenden Treffer.
- Aufloesung: Die finale Regel erkennt Feldname plus Zuweisungsoperator,
  ohne den Wert zu parsen. Zitierter fuehrender Leerraum und leere
  Zuweisungen bleiben damit fail-closed. Leere Zuweisungen bewusst zu
  blockieren erhaelt frueheres Schutzverhalten, keine neue Produktanforderung.
- Eigener gezielter Nachreview: finale Regex in Bash geladen; 6/6 synthetische
  Zuweisungen erkannt, 4/4 unzugewiesene Regelwoerter erlaubt, Exit 0.
  Keine Dateien oder Git-Zustaende fuer diesen In-Memory-Probe veraendert.
  Diese Regex bleibt im aktuellen PP202-Stand unveraendert.
- Owner: Repository Maintainer / Hook Author.
- Follow-up: vereinfachte Regel und Regression erhalten; keine weitere
  PP201-Korrektur im aktuellen Stand erforderlich.
- Trigger: Aenderung an Feld-, Operator-, Quoting- oder Leerwert-Semantik.

### PP202: ResolvedAndVerified

- Kategorie: CommitHistoryCoverage; urspruengliche Severity: Medium.
- Location: beide Hooks, collect_regex_files_for_existing_ref, Zeilen 63-74;
  is_reviewed_keynote, Zeilen 20-35.
- Historischer Befund: Der Existing-Ref-Endpunktdiff liess einen in einem
  Zwischencommit manipulierten und spaeter auf den Remote-Inhalt
  zurueckgesetzten Pfad aus. Die neue Blobpruefung wurde dann nicht erreicht.
- Aufloesung: Der Existing-Ref-Collector iteriert jetzt jeden ausgehenden
  Commit, sammelt ihn fuer die Blobpruefung und fuegt dessen diff-tree-Pfade
  zur deduplizierten Kandidatenliste hinzu. Die Netto-Endpunktdiff-Auswahl
  ist entfernt. Somit bleibt der betroffene Pfad auch bei sauberem,
  identischem Remote-/Tip-Inhalt Kandidat. Beide Hooks enthalten diese Logik.
- Unabhaengiges Nachreview: Den korrigierten Kontrollfluss von Commitliste
  ueber Pfadsammlung zur Ausnahme gelesen und geprueft. Ein abweichender
  Zwischenblob erreicht nun die exakte Pinpruefung und verweigert die
  Dateinamen-Ausnahme, auch bei freigegebenem Working Tree und spaeterer
  Wiederherstellung. Kein zusaetzlicher Git-Fixture-/Suite-Lauf.
- Neue Regression gelesen:
  test_existing_ref_checks_intermediate_key_even_when_tip_is_restored.
  Die Fixture speichert die freigegebene Remote-Basis, committet ungepruefte
  Zwischenbytes und stellt die freigegebenen Bytes im Tip wieder her. Sie
  uebergibt eine echte Remote-Basis-ID statt der Null-ID und erwartet Exit 2.
- Owner: Repository Maintainer / Hook Author.
- Follow-up: commitbasierte Pfadauswahl und Existing-Ref-Regression erhalten;
  keine weitere PP202-Korrektur im aktuellen Stand erforderlich.
- Trigger: Aenderungen an Ref-/Range-/Pfadsammlung oder Blob-Pin-Semantik.

### Bestaetigte Eigenschaften und Grenzen

- Ausnahme nur fuer die zwei exakten Workshop-Keynote-Pfade. Selbst gelesene
  Git-Blob-IDs mit hash-object --no-filters: DE
  79d80b6b5641e7f0452572ab934adc95f7b7199b, EN
  f412c5718e5d1983b67b77b25abdb484e172beea. Sie stimmen mit den Pins ueberein.
- Freigabe verlangt sowohl den passenden Working-Tree-Blob als auch den
  passenden vorhandenen Pfadblob in allen gesammelten ausgehenden
  Commitbaeumen und mindestens einen solchen Treffer. Falscher Pfad oder
  abweichende aktuelle/historische Bytes erhalten keine Ausnahme.
- Keine pauschale Erweiterungsfreigabe und keine neue Contentausnahme:
  die Keynote-Ausnahme betrifft nur Dateinamenbefunde. Der Primaerscan bleibt
  davor aktiv. Keine Behauptung zu rekursivem ZIP-/IWA-Parsing, nativer
  Folienzahl oder semantischer Secretfreiheit einer Praesentation.
- Bestehende Tokenfamilien und typisierte PEM-Header bleiben erhalten;
  Contentgrep fuer Repo/Gitconfig ist case-insensitive. Der generische
  untypisierte Private-Key-Header ist dadurch nicht neu als Contentregel
  abgedeckt; die Key-Fixture am gepinnten Pfad wird durch die abweichenden
  Bytes und den Dateinamenfilter blockiert.
- Jeder von null verschiedene echte Gitleaks-Exitcode bricht weiterhin vor
  den Ausnahmen mit Exit 2 ab. Fehlendes Gitleaks aktiviert unveraendert den
  Fallback und ist kein erfolgreich abgeschlossener Primaerscan.
- Vollstaendiger Installed-/Source-Diff: genau eine bestehende lokale
  allowed_secret_content_path_regex-Zeile mit zusaetzlichem hg-forgejo-/
  Secure-Development-Dokumentationsscope. Diese Abweichung wurde unveraendert
  erhalten. Vorher-Existenz ist Parent-Provenienz. Mitgeteilter privater
  Vorher-Backuphash:
  27fb41a793734e27b1ffa55daf9ca9a3680b630c90944a20ae0242cf42a27f29.
  Der Backupinhalt wurde nicht gelesen; keine neue Freigabe dieses Altscopes.

### Verifikation

Die neun Testmethoden beziehungsweise die gezielten Ergaenzungen wurden
fachlich gelesen. Temporaere Git-Fixtures fuehren den versionierten Hook mit
kontrolliertem Gitleaks-Stub aus; das isoliert den Fallback und prueft auch
Primaerscan-Fehler. Sie sind kein echter Gitleaks-Nachweis und testen nicht
unmittelbar den installierten Hook. Der Reviewer fuehrte nur den beschriebenen
kleinen PP201-Probe aus, keine zusaetzliche Suite oder Git-Fixtures.

Finale Parentmeldung zum stabilen aktuellen Stand: alle neun Tests bestanden
in 39.589 Sekunden; tatsaechlicher installierter Hook und echter Gitleaks-
Scan des ausgehenden Sieben-Commit-Ranges ebenfalls bestanden. Dies sind
explizit Parent-Nachweise, nicht als eigene Laeufe ausgegeben. Fruehere
Sechs-/Acht-Test-Ergebnisse und der wegen paralleler Quellenbearbeitung
fehlgeschlagene Zwischenlauf sind keine finalen aktuellen Testergebnisse.

Die beiden Korrekturen sind unabhaengig fachlich nachgeprueft. Dieses Ergebnis
akzeptiert keine Risiken und erteilt keine neue Start-, Merge-, Plattform-,
Rechts- oder menschliche Abnahmeautoritaet. Parent besitzt die gesonderte
Lieferautoritaet; keine weiteren Aenderungen oder Testschleifen durch Reviewer.

## English

**Ready for the bounded hook delta**: no open findings; PP201 and PP202 are
ResolvedAndVerified. No risk acceptance or general security/product approval.
Review covers only the tracked hook, its named test file and the owned
installed-hook delta. The reviewer authored none of the corrections and
changes only this report. No new intake review, build, runtime, Git or journal
mutation. Parent confirms the existing 260 intake bindings remain unchanged.

PP201, SecretDetectionCorrectness, originally Medium, both hooks line 13:
the old value-parsing expression missed quoted values with leading whitespace.
The corrected field-plus-assignment-operator rule does not parse the value;
it blocks leading whitespace and empty assignments deliberately, retaining
prior fail-closed behavior. The reviewer independently checked 6/6 assignment
cases matched and 4/4 bare words were allowed, exit 0, entirely in memory.
That expression is unchanged by PP202. Owner: Repository Maintainer / Hook
Author. Preserve the rule and focused regression; reopen on changes to
field/operator/quoting/empty-value semantics.

PP202, CommitHistoryCoverage, originally Medium, existing-ref collector lines
63-74 and guard lines 20-35: endpoint-only paths previously omitted a changed
intermediate file restored to its approved remote contents. The collector now
iterates each outgoing commit and adds its diff-tree paths as candidates as
well as collecting commit IDs. Consequently the path reaches the pin guard
even when remote and tip bytes agree; an unapproved intermediate blob rejects
the exception despite a clean working tree/later commit. This control flow
was independently reviewed in both hooks. The ninth regression creates the
approved remote base, unapproved intermediate commit and restored approved
tip, passes the actual nonzero remote base ID and expects exit 2. No duplicate
Git fixture or suite was executed by the reviewer. Owner: Repository Maintainer
/ Hook Author. Preserve commit-derived candidates and this regression; reopen
on ref/range/path-selection/blob-pin changes.

The exception is limited to two exact paths and the independently confirmed
no-filter Git IDs listed above. It requires matching current bytes and every
existing object at that path across collected outgoing trees, with at least
one seen object. Wrong paths or changed current/intermediate blobs do not
qualify. It bypasses filename findings only, not content or primary Gitleaks.
No extension-wide exception, ZIP/IWA parsing or presentation semantic-safety
claim. Existing token families/typed PEM headers remain; content grep ignores
case. Generic untyped private-key content is not newly covered by that typed
rule. Actual nonzero Gitleaks status still blocks with exit 2; missing Gitleaks
retains fallback behavior rather than proving primary-scan success.

Installed/source differences remain exactly the pre-existing local content-
allowregex line described above. Its prior existence and supplied private
backup hash are attributed to the parent; the backup was not read or newly
approved. The nine tests and focused additions were read; they execute the
tracked hook in temporary repositories using an intentional Gitleaks stub,
not the real scanner or installed hook. Parent reports final nine-test success
in 39.589 seconds and actual installed-hook/real-Gitleaks outgoing seven-commit
success on stable sources. These are parent evidence, not reviewer runs;
earlier or interrupted results are not presented as final. No further suite,
intake re-review, risk acceptance or new execution/delivery/acceptance authority.

## Quellenhashes / Source Hashes

Current raw SHA-256; no self-hash for this report.

| Path | SHA-256 |
|---|---|
| scripts/hooks/pre-push | bac2945b7125440e50312f4e1be2ef76b9a2f4582fbc174161eedbe3a6d42470 |
| scripts/tests/test_pre_push_secret_policy.py | 161cb716c128d8a32e1e1eca0e05d5d2b4762d09e8f519575fe2069fef862ae4 |
| .git/hooks/pre-push | 7488bb1c60787a09e2df44315bdef552606aa7ae1a3b2fa7c774226c9a3e8980 |
