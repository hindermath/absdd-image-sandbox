# Keynote-Pin-Review / Keynote Pin Review

## Deutsch

**Datum:** 2026-10-27. **Reviewer:** Huygens, unabhaengig von Hook-/Testautor, koordinierendem Hauptagenten und Provenienz-Autor Lorentz. Reviewer-UUID `01a17e80-c3dc-75d1-9e04-3f55115ab79d` wurde vom koordinierenden Hauptagenten aus dem Agenten-Toolergebnis mitgeteilt, nicht durch eine menschliche Bestaetigung erzeugt.
**Gepruefter HEAD:** `d48ce5f8bf0e5c3e612b4cc40fde0e5acf694240`, mit noch nicht committiertem Hook-/Test-Diff.
**Aktuelles Ergebnis nach begrenztem Nachreview:** **Ready**. KEY-PIN-IR001 (Medium) ist **ResolvedAndVerified**; null offene Findings, keine Risikoannahme. Der historische Erstbefund bleibt unten erhalten. Kein MergeAndSync, keine Runtime oder formale Abnahme durch diesen Reviewer.

### Historischer Erstbefund KEY-PIN-IR001

**Medium: Neuer Test setzt nicht garantiert vorhandene historische Git-Blobs voraus.**
Quelle: `scripts/tests/test_pre_push_secret_policy.py`, Methode `test_reviewed_deck_history_allows_only_language_specific_pins`, insbesondere der direkte `git cat-file blob`-Aufruf mit `check=True`.
Betroffener Ausfuehrungsweg: `.github/workflows/maintenance-tui.yml:31` verwendet Checkout ohne `fetch-depth`-Override; Zeilen71/76 entdecken alle `test_*.py` und damit diesen Test.

Das exakt gepinnte Checkout-Action-Manifest setzt [fetch-depth standardmaessig auf1](https://raw.githubusercontent.com/actions/checkout/9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0/action.yml). Der aktuelle HEAD enthaelt an den beiden Deckpfaden die neuen Blobs, nicht die vom Test angeforderten alten. Im lokalen nicht-flachen Repository sind beide alten Objekte vorhanden; das erklaert einen gruenen lokalen Lauf, garantiert aber nicht deren Verfuegbarkeit im frischen flachen CI-Checkout. Ohne alte Objekte endet der Aufruf mit CalledProcessError, bevor der eigentliche Hookfall geprueft wird. Das ist eine aus gepruefter Checkout-Konfiguration und Testlogik abgeleitete CI-Fehlerbedingung, keine Behauptung eines von mir ausgefuehrten CI-Laufs.

**Owner:** Testautor/Maintainer. **Empfehlung:** Den Regressionstest von ungarantierter Repository-Historie unabhaengig machen, etwa mit engen versionierten und hashgeprueften Altbyte-Fixtures. Alternativ historische Objekte bewusst im betroffenen CI-Checkout bereitstellen; dann den Quellenimpact erneut pruefen. Nicht durch Skip, abgefangenen Ladefehler oder gelockerte Pins gruen machen. Der Workflow ist eine bestehende Receipt-Quelle; eine Workflow-Korrektur waere anders als der heutige Hook-/Test-Diff potentiell rebindpflichtig. Selbststaendige Testfixtures vermeiden diese zusaetzliche Workflow-Aenderung.
**Trigger:** Vor Lieferung dieser neuen Testanforderung und bei Checkout-/Fixturewechsel.
Keine Selbstkorrektur durch den Reviewer. Der Quellenfreeze wurde nicht uebergangen.

### Gepruefte enge Ausnahme

| Sprache | Alter erlaubter Git-Blob | Neuer erlaubter Git-Blob |
| --- | --- | --- |
| DE | `79d80b6b5641e7f0452572ab934adc95f7b7199b` | `87f54be7bf9e6e8aba1118c1c7c1b2c54cc842f0` |
| EN | `f412c5718e5d1983b67b77b25abdb484e172beea` | `bc9483d1889f7c5f3c62f13215a33224e5fe6b8b` |

Der vollstaendige getrackte Hook und Test sowie ihr Diff wurden gelesen. Die Aenderung betrifft nur `is_reviewed_keynote` und den neuen Test. Der Hook erlaubt ausschliesslich zwei exakte repositoryrelative Deckpfade, mit je eigenem Alt-/Neu-Blobset. Kein Verzeichnisglob, kein generisches .key-Allowlisting und keine sprachuebergreifende gemeinsame Menge.

Die Arbeitsbaumdatei wird mit `git hash-object --no-filters` gegen das passende Set geprueft. Jeder aufgezeichnete ausgehende Commit mit diesem Pfad muss ebenfalls einen Blob aus genau diesem Sprachset enthalten; ein passender Tip allein verdeckt keinen unzulaessigen Zwischenstand. Mindestens ein Historientreffer ist weiterhin erforderlich. Neue und bestehende Remote-Ref-Pfade sammeln ihre ausgehenden Commits unveraendert. Die ganze neue/alte Hashmenge ist durch Leerzeichen begrenzt; unbekannte Hashes, vertauschte Sprachdateien und nachtraeglich veraenderte Arbeitsbaumbytes werden nicht ausgenommen.

Das ist nur die Dateinamenklassifikation fuer bereits identifizierte Keynote-Bytes. Die Inhaltspruefung und der vorgelagerte Gitleaks-Scan des ausgehenden Commitbereichs bleiben unveraendert aktiv. Ein von Gitleaks gemeldeter Fehler oder Fund wird unveraendert in Exit2 ueberfuehrt, bevor die Dateinamen-Ausnahme erreicht wird. Fehlendes Gitleaks hat weiterhin den bereits vorhandenen Regex-Fallback; dieser Review erfindet daraus keinen gleichwertigen Vollscanner.

### Installierter Hook ist gesondert betrachtet

`core.hooksPath` ist nicht gesetzt; der lokale Hookpfad ist `.git/hooks/pre-push`. Ein direkter Vergleich zeigt: Die neue Keynote-Funktion ist bytegleich mit der getrackten Funktion. Der einzige sonstige Unterschied zwischen den beiden heutigen Hooks ist die bereits vorhandene breitere lokale Inhaltsausnahme fuer `hg-forgejo` und Markdown unter `docs/secure-development/`.

Diese lokale Inhaltsausnahme wurde nicht durch den neuen Keynote-Patch eingefuehrt. Sie bleibt sichtbarer vorheriger Kontext, ist keine neue pauschale Freigabe dieses Reviews und wurde nicht durch einen kompletten Installerlauf ueberschrieben. Die getrackte Fixture-Suite beweist nicht die gesamte lokale Sonderkonfiguration. Ich habe den installierten Hook nur statisch verglichen, keinen echten Push damit ausgeloest. Ein vom Hauptagenten angekuendigter realer Outgoing-Range-Prueflauf war beim Bericht keine von mir beobachtete abgeschlossene Ausfuehrung und wird nicht als bestanden ausgewiesen.

### Unabhaengige ZIP-/Plist-Pruefung

Alte Git-Blobs und neue gepinnte Blobs wurden direkt in Speicher gelesen, als ZIP geoeffnet und alle Eintraege dekomprimiert und byteweise ueber SHA256 verglichen. Je Sprache110 Eintraege, keine hinzugefuegten/entfernten Namen. Je Sprache39 `Slide*.iwa`-Eintraege, alle byte-identisch.

- DE aendert nur `Index/Document.iwa`, `Index/ViewState.iwa`, `Index/DocumentStylesheet.iwa`, `Index/Metadata.iwa` und `Metadata/Properties.plist`.
- EN aendert nur dieselben Eintraege ohne `DocumentStylesheet.iwa`.
- Die binaeren Properties-Plists wurden mit dem nativen macOS-`plutil` im Speicher in JSON ueberfuehrt; geaenderte Schluessel sind nur `revision` und `versionUUID`.
- Ein erster XML-Parseversuch erkannte korrekt keinen XML-Plist; er war kein erfolgreicher Inhaltsnachweis. Die anschliessende native Binary-Plist-Konvertierung lieferte den oben beschriebenen Schluesselvergleich.
- CRC-valid wurde vom Hauptagenten berichtet; ich habe keinen eigenen CRC-Prueflauf behauptet. Erfolgreiche ZIP-Dekompression und Eintragsvergleich sind meine eigenen Beobachtungen.
- IWA-Payloads wurden **nicht semantisch dekodiert**. Bytegleiche Slides und eng begrenzte Dateiaenderungen sind keine Behauptung, alle versteckten Document-/Metadata-Inhalte oder sichtbaren Keynote-Effekte semantisch verstanden zu haben. Keine pauschale Secretfreiheit oder A11Y-/Renderingabnahme.

### Eigene und fremde Testevidenz

**Eigener einmaliger fokussierter Lauf:** `python3 -B scripts/tests/test_pre_push_secret_policy.py`; zehn Tests,53.321s, Exit0/OK. Isolierte temporaere Git-Repositories und HOME; kein Commit oder Push im Arbeitsrepository.

Gelesen und durch diesen Lauf abgedeckt: beide exakten Deckpfade, fremder .key-Pfad, Alt-/Neu-Historie fuer neue/bestehende Ref, vertauschte Sprachen fuer beide Versionen, veraenderte Deckbytes, echter Schluesseltext am erlaubten Pfad, private Schluessel-/Tokenmuster, zitierte/leere/Whitespace-Zuweisungen, unerlaubter Anfangsblob trotz wiederhergestelltem Arbeitsbaum/Tip, unerlaubter Zwischencommit bei bestehender Ref und Gitleaks-Fehlerstub. Der Stub testet Hook-Fehlerfortpflanzung, nicht die Erkennungsqualitaet eines echten Gitleaks-Scans. KEY-PIN-IR001 bleibt trotz lokalem Erfolg bestehen.

**Nur vom Hauptagenten berichtet:** zehn Tests49.582s/Exit0, Bash-Syntax/Diffcheck/Composeconfig Exit0; Secretagent-Zusammenfassung High0/Medium1(lokale Konfiguration)/Low4. Diese Werte sind nicht meine erneuten Ausfuehrungen. Keine lokalen Konfigurationsinhalte gelesen oder veroeffentlicht; keine Risikoannahme zu deren Funden. Kein kompletter Suiten-, Build-, Runtime- oder Scannerlauf durch diesen Reviewer.

### Vollstaendige Intake-/Reihen-Inhaltsbewertung im aktuellen Stand

Der bereits in dieser Review-Unterhaltung vollstaendig durchgefuehrte unabhaengige Lesepass aller vier Texte bleibt durch die jetzt erneut geprueften identischen Zielhashes auf den aktuellen Stand anwendbar. Nicht nur Hashes: Individuelle Anforderungen, Abnahmebedingungen, Nichtziele, alle Nachtraege und sechs aktive Folgeprompts wurden inhaltlich beurteilt; hier wird ihre unveraenderte Bedeutung frisch gegen den Hook-/Testscope eingeordnet.

1. **Historische abgeschlossene GSDB-Root:** Bestandsmatrix und priorisierte Gap-Liste fuer alle zwoelf Checklisten; kein Hardening, keine technische/organisatorische Freigabe. AcceptedBaseline akzeptiert nur die Arbeitsbasis, nicht Gap-Schliessung oder Restrisiken. Originaltext und historische Klassifikation bleiben erhalten.
2. **Aktiver H-Intake:** Sieben Grundanforderungen sowie H-344-01..10 und AC-H-344-01..10 verbinden Herkunft/Pins, minimale Rechte, Argument-/Pfad-/Netzwerkgrenzen, Agenten-/Auditdaten,85/80-Testschwellen und getrennte Rechts-/Cloud-/Kryptopruefung. Die enge Dateinamenkorrektur ist mit diesen Grenzen vereinbar, aber ihr Test muss reproduzierbar bleiben. Keine neue Providerwahl, keine Registry-Imageverteilung oder menschliche Freigabe.
3. **Aktiver A-Intake:** A-344-01..04 samt vier AC verlangen echte unabhaengige Hardening-Abnahme, alle50 Delta-Uebergaben inklusive begruendeter AlreadyCovered/N/A-Werte, exakte Head-/Image-/Plattform-/Zeit-/Befehlsbelege und Fehlerzurueckgabe an H. Dieser Hookreview ist weder diese technische Abnahme noch Ersatz fuer offene Plattformnachweise.
4. **Aktiver L-Intake:** FR001..015/AC001..012 sowie L-FR016..023/L-AC013..020 behalten Fork/institutionelles origin/upstream, Gitneutralitaet, providerfreien lokalen Selbstbau, keine fertigen Projekt-Registry-Images, SBOM/Pins/Isolation und persoenliche Template-/Rechtegrenzen. Alle vier IT-Berufe und die vier FI-Tracks bleiben ueber kanonische DE/EN-Lernpfade mit verschiedenen Aufgabenbezuegen abgedeckt. Pilot, WCAG-Rendering und reale Nutzung sind weiterhin gesonderte Open-Nachweise.

Die vollstaendige50er-Zuordnung bleibt47 UpdateRequired,1 AlreadyCovered und2 begrenzte N/A. G01 Standards/Status, G02 sichere Grenzen/Tests, G03 Agentenwirksamkeit, G04 Herkunft/SBOM/Lizenzen, G05 Audit/Datenschutz, G06 regulatorische Rollen, G07 vorhandene Kryptografie, G08 Profil14/Assurance0.1.8, G09 Cloud-Scope und G10 Lern-/Reifebasis sind unveraendert H/A/L zugeordnet. GSDB3.4.4 und157 Kontroll-IDs sind keine neu bestandenen Kontrollen. Open bleibt Open; OpenCode2-Metadaten behalten session_coverage=not-exported. Keine Risikoannahme oder Datenbankinhalte als Ersatz.

Reihe: genau vier Mitglieder, eine Root, drei eindeutige azyklische Bindungskanten; **Completed -> Eligible -> Blocked -> Blocked**. AssessmentBaseline fuehrt zu H, SandboxBaseline zu A, HardCompletionGate zu L. H liefert Nachweise, A prueft unabhaengig und gibt Fehler zurueck, L wartet auf erfolgreichen Abschluss und eigene Startautoritaet. Enabled-Prompts/Eligible erlauben keinen automatischen Lauf. Sicherer Normalflow bleibt beschreibbar ohne Adminzwang; betreute Recovery darf keine Schutzabschaltung oder fehlgeschlagenen Auditexport umgehen. Die vier behobenen USAB-Findings bleiben historische geloeste Befunde, kein neuer Pilotnachweis.

### Aktuelle Bindungen und kein Rebind

Eigene frische Pruefung: **213/213 Quellenbindungen**, je71 pro aktivem Receipt, alle drei aktuellen Intakehashes, alle vier Review-Zielhashes und der gebundene Requesthash stimmen. Keine betroffene Direktquelle auf Hook/Test; kein erfundener Quellenwechsel. Lorentz' separat gelesener [NoAffectedBindings-Bericht](../../specs/intake-authoring-operations/77be933d-e565-4b7d-8149-37687aa00386/no-affected-bindings.md) stimmt damit ueberein. Seine21 Rohsnapshots und sechs Bash-Validatoren sind Lorentz-Evidenz, keine heute wiederholten eigenen Ausfuehrungen.

| Ziel | Aktueller normalisierter SHA256 |
| --- | --- |
| `specs/intake-authoring-archive/ec50344b-6a7b-45bf-b67c-a67f24f56c01/9d9fce68-15cc-490c-afe0-16b98eda8a54/Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md` | `9b1963a5cc1e4f074e8fc918455f0285a0e1138334451523bd957ff21e72026a` |
| `Lastenheft_Secure-Development-Container-Hardening.md` | `b90f4fe498c573d0e5e4036d01aaee76551195f5c2ffa82ae19abb05dadb9560` |
| `Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md` | `18f3c78ce08b757add6c30811a68debc1e5ff3967bfc598a7fa552121affc59f` |
| `intakes/learner-fork-self-build-sandbox.md` | `e447fbf8751a1bf9eb9c53c099fce8272e501c2305f43765f4cba62f0129f338` |

- Kanonisches Review `5c452360-9bf7-44d9-84e0-10cae34e72ea`: frueheres **Ready** bleibt als damaliges Inhaltsurteil erhalten, SHA256 `70c2c820bcd94d0625e3d4894c9eee0bc3c492cd589f7770c19c80d17b86870c`.
- Request SHA256 `48172b0a13091080c1dd6ec5e6ffb2f73423fd9a3ef27c415dc8533ee3505f31`; Manifest SHA256 `936f44533c69d10563b7287a97ec12e16f74af9e0a8e6059b3f0a267e1b9b1bd`.
- Getrackter Hook SHA256 `99267c4a91d11f37a1aab57a730f3ba516508be4e5f2568e12abbc954be9c2ec`; installierter Hook `75a3e033ae2f6927e5094998a99f0e63ef139d3f2271bb234053f2473637f091`; Testdatei `c3673ceefb3f773e80ff238b3afa9d64a72d1d42a39f635ae695c96759a894d3`.
- Gemeinsame Keynote-Funktion SHA256 `521e6f1bfda30afd101778bc3dc4f8dbe6bf9332ea0a04c1550112189a4b4da6`.

Kein Intake-/Receipt-/Request-/Review-Edit und keine Supersession. Dieser neue Bericht ist separate ungebundene Security-Evidenz, kein still hinzugefuegter Receipt-Eingang und kein Umschreiben alter Geschichte. Geschriebene Liefermenge dieses Reviewers: ausschliesslich diese Datei. Fremde0747/2219-Logs, bestehende Archive und lokale Hookcustomization nicht bearbeitet.

**Naechster Schritt:** KEY-PIN-IR001 eng durch den Testautor klaeren/beheben und nur dessen Aenderung nachpruefen; erst danach passende exakte Liefer-/CI-/Reviewgates des separat autorisierten MergeAndSync durch den Hauptagenten. Keine formale Lieferfreigabe durch diesen Bericht. Keine wiederholte Vollsuite oder unveraenderte Intakekampagne erforderlich.

## English

**Current bounded outcome after follow-up: Ready**, zero open findings; KEY-PIN-IR001 is ResolvedAndVerified as documented in the bilingual follow-up below. The initial Medium test/CI finding and initial NeedsRemediation reasoning remain historical evidence. No risk was accepted. Huygens did not author the patch or Lorentz's provenance work; the coordinating agent supplied the reviewer UUID from the spawn result. This report grants no MergeAndSync/runtime/security/product/human acceptance.

**KEY-PIN-IR001:** The new language-specific history test loads old Git blobs with checked git cat-file calls. Both old objects exist in this full local repository, but HEAD contains new deck blobs. The maintenance workflow's checkout has no fetch-depth override and its discovery runs this test; the exact pinned Action manifest defaults to depth1. Thus a fresh shallow CI checkout does not guarantee the old objects and can raise CalledProcessError before exercising the hook. This is a source/configuration-derived failure condition, not a claimed executed CI failure. Owner: test author/maintainer. Prefer self-contained, versioned/hash-verified old-byte fixtures or explicitly supply required history. Do not hide missing objects with skips, caught load failures or weaker pins. A workflow change could affect existing receipt sources; a self-contained test correction avoids that extra workflow delta. Reevaluate before delivering the new test.

**Pin logic:** Only the two exact DE/EN deck paths and their separate two-blob approved sets are accepted. Current unfiltered worktree hash and every collected outgoing historical blob must match the respective language set, with at least one history occurrence. Swapped language blobs, unknown intermediate/tip bytes and a restored worktree hiding bad history remain rejected. No broad path or .key allowlist was added. Content regex and range Gitleaks execution/failure propagation are unchanged. The checked installed function is identical; installed versus tracked hooks differ only in the known pre-existing broader local content exclusions for hg-forgejo and secure-development Markdown. Those exclusions are not introduced or newly approved by this review. Tracked fixture tests do not prove the entire installed customization. No real push was performed by this reviewer; the parent's announced real range check is not claimed as an observed completed result.

**Independent package observations:** Both old/new ZIP pairs have110 entries with no added/removed names; all39 Slide*.iwa payloads per language are identical. DE changes Document/ViewState/DocumentStylesheet/Metadata IWA and Properties.plist; EN lacks the stylesheet change. Native binary-plist conversion and comparison shows only revision/versionUUID changed. An initial XML parse was not successful evidence; native plutil supplied the actual plist comparison. All entries were decompressed and compared in memory. CRC validity is parent-reported, not a separate reviewer CRC run. IWA semantics were not decoded; these observations establish neither all hidden metadata meanings nor rendering/A11Y or blanket secret freedom.

**Own single focused run:** python3 -B scripts/tests/test_pre_push_secret_policy.py,10 tests,53.321s, exit0. It exercised exact/wrong paths, old/new history and language swaps, modified deck/key material, sensitive assignments/tokens, hidden bad history/intermediate commits and a Gitleaks failure stub in isolated temporary repositories/HOME. The stub demonstrates failure propagation, not a real scanner's detection quality. Parent separately reports10 tests49.582s/exit0, syntax/diff/config success and scanner counts; these are not my executions. No private configuration content inspected or copied; no risk acceptance.

**Current full intake/series observation:** The complete substantive four-text read in this independent conversation applies to the freshly hash-verified unchanged inputs. Historical GSDB assessment provides a gap baseline, not remediation or approval. H's original requirements and ten H/AC-H pairs retain evidence-led least privilege, supply-chain provenance, synthetic boundary tests and85/80 thresholds, separate data/privacy/legal/cloud/crypto decisions and14-preset Assurance0.1.8 coverage. A's four A/AC-A pairs require independent authorship, full50-row handoff rationale, exact head/image/platform/time/commands and negative metadata evidence; this hook review is not that acceptance. L's FR001-015/AC001-012 and L-FR016-023/L-AC013-020 retain institutional/fork origin/upstream, hosting neutrality, provider-free local build, no ready image publication and distinct personal template/history/rights gates. All four occupations and four IT-specialist tracks retain existing bilingual novice task paths without duplicate curricula. Normal writable learning needs no admin intervention or security bypass; recovery remains safe/supervised. Pilot, WCAG, platform and actual use observations remain separate/Open.

All50 delta IDs retain47 UpdateRequired,1 AlreadyCovered and2 scoped N/A across G01-G10: standards/status, safe boundaries/tests, agent effectiveness, provenance/SBOM/licences, audit/privacy, regulatory roles, existing crypto, preset/Assurance review, cloud scope and learning/maturity. GSDB3.4.4/157 IDs are not newly passed controls; OpenCode2 keeps session_coverage=not-exported. The series remains four members/one root/three unique acyclic binding edges, Completed -> Eligible -> Blocked -> Blocked. H hands to independent A, failures return to H, and L requires successful A and separate authority; Enabled/Eligible is no start permission.

**No affected bindings:** Independently verified213/213 sources, three active intake targets, all four review targets and the current request binding; no drift or direct changed hook/test source. Lorentz's linked NoAffectedBindings report agrees; its21 snapshots/six Bash validators are separately attributed. Original canonical Ready, receipts, requests, archives and foreign logs remain unchanged. This report is fresh independent unbound evidence, not a new canonical review or silent supersession. Only this file was written. Resolve/review the narrow test reproducibility finding, then leave exact-head delivery/CI/merge gates to the separately authorized parent. No repeated full suite, runtime, build, source repair, commit or push by this reviewer.

## Begrenztes Nachreview KEY-PIN-IR001 / Bounded Follow-Up

### Deutsch

**Aktuelles Urteil: Ready. KEY-PIN-IR001: ResolvedAndVerified.** Dieses Nachreview betrifft nur die eingefrorene Test-/Fixture-Korrektur. Die urspruengliche Feststellung, ihr damaliger NeedsRemediation-Status und die ersten Test-/Quellhashes oben bleiben als historische Erstbeobachtung erhalten; sie beschreiben nicht den korrigierten Test. Keine neue Intake-/Reihen-Kampagne, keine kanonische Reviewumschreibung und keine Risikoannahme.

Der aktualisierte Test verwendet keinen git-cat-file-Zugriff mehr auf Altobjekte. Er liest die zwei aktuellen gepinnten Decks und die neue JSON-Fixture, prueft je Sprache den exakten Input-SHA256, rekonstruiert Altbytes von rechts nach links und prueft die Git-Blob-SHA1 einschliesslich Git-Blob-Header. SHA1 identifiziert hier bestehende Git-Objekte, nicht eine neue kryptografische Sicherheitsgarantie. Die SHA256-Eingangsbindung und bestehenden sprachbezogenen Hook-Pins bleiben massgeblich.

Die Rueckwaertsschleife verlangt pro Patch0 <= start <= end <= limit und setzt limit anschliessend auf start. So werden ungueltige/ueberlappende oder falsch geordnete Bereiche abgelehnt; rechtsseitige Laengenaenderungen verschieben noch anzuwendende linke Offsets nicht. Base64 wird mit validate=True dekodiert. Fehler/Hashabweichungen scheitern als Testfehler statt Skip oder toleriertem Ladefehler. Die unabhaengige strukturierte Fixture-Lesung bestaetigt DE338/EN302 Patches, insgesamt640, mit1171/963, insgesamt2134 vorherigen Literalbytes. Der eigentliche Historien-/Sprachtest und die unveraenderten Hook-Pinsets pruefen die Rekonstruktion zusaetzlich gegen die erlaubten alten Hashes.

**Eigener gezielter Lauf:** Genau fuenf Dateien wurden in ein neu erzeugtes temporaeres Minimalverzeichnis kopiert: Test, getrackter Hook, JSON-Fixture und beide Decks. Vor dem Lauf wurde das Fehlen eines .git-Verzeichnisses und die Dateizahl5 geprueft. Von diesem Verzeichnis aus lief nur:

```text
python3 -B scripts/tests/test_pre_push_secret_policy.py PrePushSecretPolicyTests.test_reviewed_deck_history_allows_only_language_specific_pins
Ran 1 test in 6.883s
OK
Exit 0
```

Der Test erzeugt seine eigenen isolierten Git-Fixtures erst selbst; er kann daher nicht auf Repository-Historie des Minimalverzeichnisses zurueckgreifen. Bestehende/neue Ref-Historie mit alten/neuen Deckbytes sowie beide Sprachvertauschungs-Negativfaelle liefen ohne Skip. Das temporaere Minimalverzeichnis wurde anschliessend entfernt. Kein Commit im Arbeitsrepository, kein Push, keine Runtime. Die restliche Suite wurde nicht wiederholt; unveraenderte Negativmethoden wurden anhand des begrenzten Diffs beibehalten, nicht als erneut von mir ausgefuehrt ausgegeben.

| Aktuelle Quelle | Raw SHA256 |
| --- | --- |
| `scripts/tests/test_pre_push_secret_policy.py` | `54d3d95329957e9bf9f0312b5aaa6bdf58673473c714294d01c8599256f10191` |
| `scripts/hooks/pre-push` | `99267c4a91d11f37a1aab57a730f3ba516508be4e5f2568e12abbc954be9c2ec` |
| `scripts/tests/fixtures/keynote-previous-blobs.json` | `4dea8dec4e6eabb858b3a9dcad471c87100a3ea37375090e6438c242647c0b5e` |
| `docs/praesentationen/exports/workshop-spec-kit.de.key` | `74b72afd157635f08ca080da00c9a5615ff5626eec0d383af3f6ac8c8bbbf191` |
| `docs/praesentationen/exports/workshop-spec-kit.en.key` | `59a6c3d84c8285956d1fcaf72bd3cba178d2f95887dba6226afa98b3148ba6b0` |

Rekonstruierte alte Git-Blobs: DE `79d80b6b5641e7f0452572ab934adc95f7b7199b`, EN `f412c5718e5d1983b67b77b25abdb484e172beea`. Keine Workflowaenderung, keine breitere Pfadmenge, keine gelockerten Pins und kein automatischer Historienfetch im Test. Fixture-Erstellung aus Git-Altbytes war Authoring, nicht Testlaufvoraussetzung.

**Fremde aktuelle Evidenz:** Hauptagent meldet finale zehn Tests47.266s/Exit0, Fixture22395Bytes und erfolgreichen uvx-Precommit-Pass fuer vier Dateien. Das sind keine weiteren eigenen Ausfuehrungen. Lorentz verantwortet den finalen gezielten Quellenimpact fuer die neue ungebundene Fixture; die fruehere NoAffectedBindings-Pruefung oben bleibt auf ihren damaligen Stand bezogen. Keine Intake-/Receipt-/Reviewdatei von mir geaendert. Bereits vollstaendig gelesene unveraenderte Intake-Inhalte wurden nicht erneut kampagnenartig geprueft.

**Naechster Schritt nach diesem Review:** Der Hauptagent kann seine separat autorisierten aktuellen Liefer-/Secret-/CI-/Reviewgates fortsetzen. Dieses Ready gilt fuer die enge Hook-/Fixture-Korrektur, nicht als formale Freigabe, pauschaler Nachweis des installierten lokalen Sonderhooks, Keynote-/IWA-Semantikabnahme oder eigenstaendig ausgefuehrter MergeAndSync. Bekannte Plattform-, Pilot-, Lizenz- und menschliche Grenzen bleiben unveraendert.

### English

**Current bounded outcome: Ready. KEY-PIN-IR001: ResolvedAndVerified.** The initial finding, NeedsRemediation decision and earlier source/test records above remain historical first observations. This follow-up covers only the frozen test/fixture correction, not another full intake campaign or canonical review rewrite. No risk accepted.

The updated test no longer obtains old bytes from git cat-file. It verifies each current deck's exact SHA256, reconstructs the old bytes from JSON reverse patches right-to-left, and verifies the Git blob SHA1 including its header. SHA1 is the existing Git object identifier, not a new security guarantee. The original per-language hook sets and current SHA256 input binding remain unchanged.

Each patch must satisfy0 <= start <= end <= limit, then limit becomes start; invalid, overlapping or misordered ranges fail. Right-to-left application preserves remaining left offsets despite length changes. Base64 decoding is strict, and hash/decoding/range failures are errors rather than skips. Independent fixture inspection confirms338 DE plus302 EN patches,640 total, containing1171 plus963 prior literal bytes,2134 total. The unchanged history cases and hook pins additionally validate reconstructed bytes against the approved old blob identities.

**Own single targeted execution:** Copied exactly five files (test, tracked hook, fixture, two decks) into a new temporary directory, independently confirmed no .git directory and exactly five files, and ran the one method shown above from that directory. It passed one test in6.883s, exit0. The method creates its own isolated Git fixtures and exercised existing/new refs and both old/current language-swap negatives without skipping. The temporary directory was removed. No working-repository commit/push/runtime. No repeated full suite; remaining negative methods stayed unchanged in the reviewed diff rather than being claimed as freshly rerun.

Current file hashes and reconstructed old blob identities are listed above. No workflow change, broader paths, looser pins or runtime history fetch was introduced. Mechanical fixture authoring from old objects does not become a test prerequisite. The coordinating agent separately reports the final10-test47.266s/exit0 run,22395-byte fixture and four-file uvx-precommit success; these are attributed parent evidence, not additional reviewer executions.

Lorentz owns final narrow source-impact validation for the new unbound fixture; the earlier NoAffectedBindings evidence retains its original temporal meaning. No intake/receipt/canonical review was edited by this reviewer and unchanged full intake content was not rereviewed as another campaign. Parent may continue separately authorized current delivery gates. This bounded Ready grants no formal acceptance, whole installed-local-hook assurance, IWA semantic/rendering approval or reviewer-executed MergeAndSync; platform/pilot/rights/human boundaries remain.
