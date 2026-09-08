# Secure Development Assurance – Projektintegration / Project Integration

## Zweck und freigegebener Umfang / Purpose and Approved Scope

absdd-image-sandbox verwendet ausdrücklich das Profil
`secure-development-assurance-thirteen-governance-presets`: die bisherigen
zwölf Presets unverändert plus Assurance v0.1.3, aktiviert mit Priorität 15.
Die [13er-Matrix](../../scripts/config/spec-kit-secure-development-assurance-governance-presets.json)
und der [Profilkatalog](../../scripts/config/spec-kit-preset-profiles.json)
dokumentieren diese Entscheidung. Ältere Profile und globale Defaults bleiben
erhalten; die lokale Level-2-Registrierung wird erst nach MergeAndSync umgestellt.

*absdd-image-sandbox explicitly opts into the thirteen-preset profile. The original
twelve presets remain unchanged; Assurance v0.1.3 is enabled at priority 15.
Older profiles and global defaults are retained. Local registry assignment
follows successful merge and main synchronization.*

## Produktquelle und Paketbindung / Product Source and Package Binding

- [Eigenständiges GitHub-Repository / Standalone GitHub repository](https://github.com/hindermath/spec-kit-preset-secure-development-assurance-governance).
- Tag `v0.1.3`, Commit `0d03aa9ebe8f74a26e331815bca5609fb48d7a14`.
- [Öffentliches Tag-ZIP / Public tag ZIP](https://github.com/hindermath/spec-kit-preset-secure-development-assurance-governance/archive/refs/tags/v0.1.3.zip).
- SHA-256: `9023b442b4d82e25bee5a7fe9b73efb7f591a4f265f54061ae6e4a56b9b5c75f`.
- Voraussetzung / prerequisite: `security-governance >=0.6.1`; vorhanden / installed: `0.6.2`.

Die explizite Versionsbindung gilt unabhängig von „Latest“. Veröffentlichte
GitHub-Preset-Repositories sind alleinige Produktquellen; lokale Installationen
sind Integrationskopien. [Community-Issue #4455](https://github.com/github/spec-kit/issues/4455)
belegt die Einreichung, nicht automatisch die Aufnahme in den Katalog.

*The explicit version pin is independent of “Latest”. Published standalone
GitHub repositories are the only product sources; installed copies are
integrations. The community issue records submission, not catalog acceptance.*

## Bedienung / Usage

Sicherer Einstieg: `$speckit-secure-development-status [<evidence-dir>]`.
Andere Agentenflächen verwenden `speckit.secure-development-status`.
Ohne Verzeichnis wird der lexikografisch neueste Kontext unter
`docs/security/secure-development/` geprüft. Direkter Aufruf ab Projektwurzel:

```bash
bash .specify/presets/secure-development-assurance-governance/scripts/validate-secure-development-assurance.sh status
```

```powershell
pwsh -NoProfile -File .specify/presets/secure-development-assurance-governance/scripts/validate-secure-development-assurance.ps1 -Action Status
```

Der zweite Befehl lautet
`$speckit-secure-development-review <baseline|delta|closure|image-impact> <context-id> <training|mixed|development>`.
Er benötigt einen ausdrücklichen Auftrag für den benannten Kontext. Die
Installation startet keinen Review, keinen autonomen Lauf und keine GSDB- oder
RL-SE-Selbstprüfung. Ausführliche Bedienung und Fehlerbehebung:
[installierte Paket-README](../../.specify/presets/secure-development-assurance-governance/README.md).

*Start with the read-only status command. Review requires explicit authority
for the named context. Installation does not start reviews, autonomous runs,
GSDB or RL-SE assessments. See the installed package README for complete usage
and troubleshooting. Never shorten the installed validator path.*

## Nachweis und Sicherheitsgrenzen / Evidence and Safety Boundaries

### Wiederaufnahme am 2026-09-07 / Resumption on 2026-09-07

Das öffentliche v0.1.3-Archiv wurde erneut geladen; SHA-256 und alle
installierten Paketdateien stimmen exakt überein. Der Vergleich zum vorherigen
PR-Head `da38035fc078e6781ded5a4b35ee0839954b9afc` schützt 1144 vorhandene
Dateien außerhalb der autorisierten Paket-, Befehls- und Dokumentationspfade.
Alle zwölf übrigen Registry-Einträge und älteren Profile sind unverändert.
Die in PR #57 bestätigten Kontextbindungs- und Risikotypfehler sind durch
das kanonische Release aus Produkt-PR #4 behoben; dessen finaler
Linux-/macOS-/Windows-Vertragstest ist in Workflow-Lauf 34059234091 belegt.

Im ausgewählten Kontext `2026-08-30-gsdb-baseline-assessment` existiert bereits
eine `evidence-matrix.md`. Sie bleibt erhalten. Bash und PowerShell melden
weiterhin `Blocked`, Exitcode 2, wegen der fehlenden `baseline.json`.
Die vier Assurance-Gates und vier menschlichen Entscheidungsgrenzen sind
dadurch nicht aus einem vollständigen Assurance-Vertrag auslesbar. Vor einer
späteren Gate-Prüfung muss der Kontext fachlich in diesen Vertrag überführt
werden. Das Hinzufügen weiterer Indexdateien würde diesen Befund nicht lösen.

*The public v0.1.3 ZIP and installed files match exactly. Comparison with the
previous PR head preserves 1144 existing files, all twelve other registry
entries and older profiles. Canonical product PR #4 fixes the reported
context/risk defects; final cross-platform contract CI is run 34059234091.
The selected context already has an evidence matrix. Both read-only status
commands still block with exit 2 because baseline.json is absent. Gate and
human-decision results cannot be read from an incomplete Assurance contract;
a later substantive migration is required before a gate review.*

Am 2026-09-06 geprüft: öffentliches Archiv mit gebundenem SHA-256,
bytegleich übernommenes Paket, exakte 13er-Matrix und 708 geschützte
Bestandsdateien bytegleich. Die zwölf bisherigen Registereinträge inklusive
Versionen, Aktivierungszuständen und Prioritäten bleiben unverändert.
Vorhandene generierte Befehle bleiben unverändert; ausschließlich die neuen
Status-/Review-Oberflächen werden ergänzt.

Paket-Vertrags-, Negativ-, LF/CRLF/BOM- und Bash-/PowerShell-Paritätstests sowie
Oberflächentests liefen erfolgreich in temporären Projekten. Zusätzlich sind
die temporären Kompositionstests für alle Profile 8 bis 13 bestanden. Kein
produktives Test-Review wurde ausgeführt. Secret-Scan und bestehende PR-CI
bleiben Liefergates; nur die formale Codeowner-Hürde darf nach ausdrücklicher
Freigabe und bestandenen technischen Prüfungen per Admin-Merge übergangen werden.

Lesender Status in beiden Shells: `Blocked` (Exitcode 2), baseline.json fehlt im Kontext 2026-08-30-gsdb-baseline-assessment / baseline.json missing in context 2026-08-30-gsdb-baseline-assessment.
Es liegt damit keine erfolgreiche Assurance-Bewertung vor. Baseline-, Delta-,
Closure- und Image-Impact-Gate sowie `technicalValidation`,
`pilotAuthorization`, `projectAcceptance` und `generalRelease` werden nicht
als erfüllt behauptet. Ohne gültige Evidence gibt es keine verlässlich
auslesbare nächste fachliche Aktion. Eine solche Prüfung bleibt ein separater
Auftrag; die Installation wird deshalb nicht als fachlich `Ready` bezeichnet.

Projektgeführte Baseline 3.1.0, Richtlinien, Checklisten und bestehende
Evidence bleiben erhalten. `CL-02-13 Cloud-Compliance-Assurance` ist ein
C5-Bezug, keine vollständige C5-Kriterien-, Testat- oder Readiness-Prüfung.
`Ready` bezieht sich ausschließlich auf den geprüften Evidence-Kontext und
ersetzt keine menschliche Freigabe oder Zertifizierung.

*The public archive, installed package identity, exact matrix, and
708 protected files were verified. The original twelve registry entries
and existing generated commands are preserved. Isolated contract, negative,
encoding, shell-parity, surface and profile 8–13 tests passed. Secret checks
and existing PR CI remain delivery gates; explicit authority permits bypassing
only the formal Codeowner requirement, never technical failures. Both status
validators fail closed with exit 2: baseline.json fehlt im Kontext 2026-08-30-gsdb-baseline-assessment / baseline.json missing in context 2026-08-30-gsdb-baseline-assessment. No successful gate, human
decision, or next evidence action is inferred. Baseline 3.1.0, policies,
checklists and existing evidence stay unchanged. C5 is a limited relationship,
not attestation, certification, or full readiness. No substantive review starts.*

## Dokumentationsauswirkung / Documentation Impact

Sandbox-spezifisch: ausschließlich Repository-Integration. Dockerfile,
Compose, Image, gepinnte Home-Baseline-Referenz und laufende Container werden
nicht verändert. Kein Build, Publish, Neustart oder Home-Sync.
`podman-compose config` ist bestanden; Details im
[Sitzungslog](../security/agent-session-log/2026-09-06-2154.md).

*Sandbox-specific scope is repository integration only. Dockerfile, Compose,
image, pinned Home Baseline and running containers remain unchanged. No build,
publication, restart or Home sync. Static Compose validation passed; see the
session log for the separate compliance-plan boundaries.*

`UpdateRequired`, Owner: Thorsten Hindermann. Zielgruppen: Lernende, Maintainer
und KI-Agenten. Leserpfad: README → Integrationsnachweis → Paket-README →
lesender Status. Quelle: gebundenes GitHub-Release; lokale Integration:
Profilkatalog und Matrix. Betroffen: README, dieser Nachweis, fünf gemeinsame
Agenten-Dateien und Statistik-Ledger. Dokumentklasse: Bedienung/Governance;
Deutsch zuerst, Englisch danach, CEFR B2 und text-first. Linkpfade, Befehle und
beide Shells werden geprüft. Keine rein visuelle Bedeutungsübertragung.

Repository-Integration, kein Home-Sync und kein weiterer Flotten-Rollout.
Keine Runtime-, API- oder Verhaltensänderung; beide Constitutions auf Auswirkungen
geprüft. TDD/Changed-Code-Coverage für reine Paketübernahme und Dokumentation
`N/A`, Wiedervorlage bei eigener Produktlogikänderung. NIST SSDF und CWE Top 25
gelten; ASVS, neue Produkt-SBOM, Produkt-AI-SBOM und Zero Trust sind für diesen
Integrationsdelta `N/A`, da keine neue Web-/Auth-, Produkt- oder KI-Laufzeit
entsteht. Projektweit bestehende Pflichten werden dadurch nicht aufgehoben.
Wiedervorlage bei Paket-, Profil-, Baseline- oder Laufzeitänderungen.

*Documentation impact is UpdateRequired, owned by Thorsten Hindermann. The
bilingual, text-first reader path connects README, integration record, package
manual and read-only status. Five agent guides are kept aligned. This is
repository integration without Home sync or wider rollout; no runtime, API or
behavior changes. Both constitutions were checked for impact. Product TDD and
changed-code coverage are N/A for package reuse/documentation and must be
revisited for new product logic. SSDF/CWE apply; the other listed scopes add no
new obligations in this delta, without waiving existing project obligations.
Reevaluate at package, profile, baseline or runtime changes.*

## Aktueller Feldteststatus / Current Field-Test Status

Die oben datierten Blockierungsbefunde dokumentieren den jeweiligen
historischen Integrationsstand. Der aktive Evidence-Vertrag wurde danach
vollstaendig migriert und revalidiert. Den aktuellen Stand, alle ausgefuehrten
Pruefungen, Wiedervorlagen und die eng begrenzte Empfehlung `ReleaseAccepted`
fuer Preset v0.1.3 dokumentiert der
[kanonische Feldbericht](secure-development-assurance-v013-field-test.md).
Menschliche Pilot-, Projekt- und allgemeine Freigaben bleiben `Open`.

*The dated blocked findings above preserve their historical integration state.
The active evidence contract was subsequently migrated and revalidated. The
[canonical field report](secure-development-assurance-v013-field-test.md)
records current checks, review dates, and the narrowly scoped
`ReleaseAccepted` recommendation for preset v0.1.3. Human pilot, project, and
general-release decisions remain `Open`.*
