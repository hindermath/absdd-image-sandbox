# Quellenabgleich nach PR #107 / Source alignment after PR #107

## Auftrag und Grenze / Authority and boundary

DE: Der Nutzer hat am 2. November 2026 die gezielte Quellenaktualisierung mit
bytegleicher Archivierung und unabhängigem Vollreview genehmigt. Danach
folgen Mac-A-Coverage und eine Windows-/WSL2-Übergabe in getrennten Arbeiten.
Dieser Abgleich ändert keine Anforderung, keinen Grenzwert und keine
Startautorität. Kein Commit, Push, Build oder Container-Eingriff.

EN: On 2 November 2026 the user authorized targeted source renewal with
byte-identical archives and an independent full review, followed by separate
Mac-A coverage work and a Windows/WSL2 handoff. This alignment changes no
requirement, threshold or start authority. No commit, push, build or container
operation belongs to this provenance transaction.

## Erklärter Quellenwechsel / Explained source changes

DE: Ausgangspunkt ist `e115fa863e754a83eff212c72f130f6f8543a988`, der Merge
von PR #107. Genau sieben eindeutige Pfade weichen von ihren Bindungen ab.
Alle sieben sind in den drei vorhandenen Receipts für Hardening,
Selbstprüfung und Lernenden-Selbstbau gebunden: 21 betroffene Bindungen.
Der abgeschlossene GSDB-Vorgänger und der Feature-Update-Intake haben keinen
Quellendrift. Alte Hashes passen exakt zu den jeweiligen Git-Vorgängern.
Der maschinenlesbare Operationsnachweis enthält alte und neue Hashes.

EN: The starting point is merge `e115fa863e754a83eff212c72f130f6f8543a988`
from PR #107. Exactly seven unique paths differ from their bindings. Each
occurs in the three existing hardening, acceptance and learner self-build
receipts: 21 affected bindings. The completed GSDB predecessor and the
feature-update intake have no source drift. Prior hashes exactly match the
respective Git predecessors. The operation journal records old/new hashes.

| Quelle / Source | Erklärte Änderung / Explained change | Commit |
|---|---|---|
| `docs/maintenance/gsdb-344-preset-installed-lock.json` | Inventar und Inhaltsdigest des Review-Presets aktualisiert / Review-preset inventory and content digest refreshed | `30f3312a5e7db753ab673517a313f77996a8e147` |
| `scripts/tests/test_toolchain_version_pins.py` | Native Archive, feste Syft-/uv-Prüfsummen und Swift-Signer absichern / Check native archives, fixed Syft/uv digests and Swift signer | `30491d065f5d33b7dc065b923e19a900a32c0772` |
| `Dockerfile` | Gepinnte separate PowerShell-Installation, Signer-/Digest-Prüfung, Agenten-Defaults und Audit-Retention / Separate pinned PowerShell installation, signer/digest checks, agent defaults and audit retention | `30491d065f5d33b7dc065b923e19a900a32c0772` |
| `README.md` | Optionalen Read-only-Betrieb und vertrauliche Prompt-Übergabe mit Abnahmegrenzen erklären / Explain optional read-only operation and confidential prompt delivery with acceptance limits | `30491d065f5d33b7dc065b923e19a900a32c0772` |
| `docs/fuer-lernende/erste-schritte.md` | Sichere Stopp-Vorschau, Audit-Mount und Retention erklären / Explain safe stop preview, audit mount and retention | `30491d065f5d33b7dc065b923e19a900a32c0772` |
| `docs/fuer-lernende/troubleshooting.md` | Fail-closed-Fehlerhilfe ohne Sperr-/Auditumgehung / Fail-closed recovery help without lock/audit bypass | `30491d065f5d33b7dc065b923e19a900a32c0772` |
| `docs/fuer-lernende/alltag.md` | Nichtleeren Tagesexport, 30 UTC-Tage und blockierenden Fehlerpfad erklären / Explain nonempty day export, 30 UTC days and blocking failure path | `30491d065f5d33b7dc065b923e19a900a32c0772` |

## Unveränderte Anforderungen / Preserved requirements

DE: Alle fünf Intake-Texte und alle kopierbaren Folgeprompts bleiben bytegleich.
Die IDs, Reihenfolge, Root und fünf Kanten bleiben erhalten. Der Lifecycle ist
weiterhin `Completed → Eligible → Blocked → Blocked → Blocked`. Die Schwellen
85 % Zweigabdeckung je sicherheitskritischem Modul und 80 % Interface-Abdeckung
werden weder gesenkt noch als erreicht behauptet. Bereits vorhandene
Schutzmaßnahmen zuerst bewerten; keine Neuimplementierung durch diese
Quellenpflege. Feature 003, Feature-004-Artefakte und menschliche Gates bleiben
unverändert. Ein aktueller Quellenhash ist keine technische Abnahme.

EN: All five intake texts and all copyable follow-up prompts remain byte
identical. IDs, order, root and five edges are preserved. Lifecycle remains
`Completed → Eligible → Blocked → Blocked → Blocked`. The thresholds of 85%
branch coverage per security-critical module and 80% interface coverage are
neither lowered nor claimed achieved. Assess existing safeguards first;
source maintenance does not implement new safeguards. Feature 003, Feature
004 artifacts and human gates remain unchanged. A current source hash is not
technical acceptance.

## Reviewübergabe / Review handoff

DE: Vorherige Texte, Receipts, Reihenansichten und Reviewartefakte werden vor
aktiver Mutation bytegleich archiviert. Nur die drei betroffenen Receipts
erhalten neue Receipt-/Operations-IDs; jeweils ist der vorherige Intake die
erste Quelle. Das frühere Serien-Ready wird ausdrücklich ersetzt und ist nur
historisch. Der Autor liefert `PreparedForIndependentReview`, kein neues
Ready. Ein anderer Reviewer prüft alle fünf Intakes vollständig, den ganzen
Graph, Anforderungen, Quellenwechsel, Archivtreue, Verständlichkeit,
Bilingualität und Autoritätsgrenzen.

EN: Previous texts, receipts, series views and review artifacts are archived
byte for byte before active mutation. Only the three affected receipts gain
new receipt/operation IDs, with the previous intake first in each source list.
The old series Ready is explicitly superseded and historical only. The author
delivers `PreparedForIndependentReview`, not a new Ready. Another reviewer
must fully assess all five intakes and the complete graph, requirements,
source changes, archive fidelity, readability, bilingual content and authority.

DE: Offener Punkt: unabhängiges Vollreview. Owner: unabhängiger Reviewer und
Repository Owner. Follow-up: den aktuellen Serien-Reviewauftrag ausführen.
Re-Evaluation-Trigger: jede weitere Änderung an Zieltext, Quelle, Receipt,
Manifest, Graph oder Reviewauftrag. Windows-/WSL2-, praktische Usability-,
WCAG- und menschliche Abnahmen werden dadurch nicht geschlossen.

EN: Open item: independent full review. Owner: independent reviewer and
Repository Owner. Follow-up: execute the current series review request.
Re-evaluation trigger: any further target, source, receipt, manifest, graph
or review-request change. Windows/WSL2, practical usability, WCAG and human
acceptance remain separate and are not closed by this update.
