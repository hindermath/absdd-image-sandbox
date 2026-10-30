# Intake-Review: Sandbox-Feature-Update / Sandbox Feature Update

## Deutsch

**Ergebnis:** `NeedsRemediation` — Nachbesserung der Begriffserklärungen nötig.
**Modus:** `Single`; ein Ziel, keine Worker, keine Serienmigration.
**Stand:** 2026-10-28. Dieses Review stammt vom selben Chat wie die Erstellung;
es ist kein unabhängiges menschliches Vier-Augen-Review.

Geprüft wurde
`Lastenheft_Sandbox-Feature-Update-Ubuntu2604-OpenCode-Web-MSL.md`,
normalisierte SHA-256
`c84477a1676ebbf42f5c2b0a6f9797f9d1d41857c8d4ebe2bcc2b7cb44586d4b`.
Das Ziel ist ungetrackt; deshalb kein Git-Blob als Beleg. Der Repository-Head
ist `7bb2ffd7630c8d4f52d3600cb6e22b51f413e6b4`; dieser Commit allein
enthält das geprüfte ungetrackte Lastenheft nicht.

### Umfang und Prüfbasis

- Installierter Skill `speckit-intake-review`, Policy-Vorlage und Single-
  Checkliste aus `intake-review-governance` sowie Repository-Guidance.
- Requirements-Konfiguration Schema 2.0: `Aligned`, `de-DE`, Profil `de`,
  `SeriesManifest`; Rollen, Collections und Index vorhanden. Inventar:
  6 physische aktive Intake-Dateien, 3 aktive Serienziele, 4 Serienmitglieder,
  genau ein bisheriges Eligible-Ziel (Container-Hardening). Das neue
  eigenständige Intake muss im Modus SeriesManifest noch kein Mitglied sein.
- Create-Receipt und die drei unveränderlichen lokalen Issue-Snapshots
  #101, #102 und #104: Ziel-/Quellenhashes aktuell, Reihenfolge erhalten.
  Keine zusätzlichen Upstream-Seiten oder laufenden Issues abgerufen;
  deren Live-Status ist kein Ergebnis dieses lokalen Inhaltsreviews.
- 23 deutsche Anforderungen mit englischer Entsprechung und 12
  Abnahmekriterien; fachliche Abdeckung gegen alle drei Snapshots geprüft.
- Bestehende Serie nur als Kontext der vorgeschlagenen Einordnung geprüft;
  keine erneute Vollprüfung oder neue Abnahme ihrer anderen Mitglieder.

### Befund IR701

| Feld | Bewertung |
|---|---|
| Schweregrad | Medium |
| Kategorie | Learning / Language / First-use terminology |
| Owner | Requirements Author / Documentation & Learning Review |
| Status | Open — RemediationRequired; keine Risikoakzeptanz |
| Evidence | Ziel Zeilen 19–36, 127–131, 181–184 und 376–385; installierte Review-Checkliste Zeilen 6–9; AGENTS-Lernendenbasis |

Das Lastenheft setzt ausdrücklich keine Container-, Programmier- oder
Spec-Kit-Erfahrung voraus. Das deutsche Glossar erklärt einige Grundbegriffe,
lässt jedoch beim ersten Gebrauch wesentliche Begriffe wie SELinux,
Bubblewrap, Capability-Drop, Seccomp und LSP ohne Erklärung. Die englische
Einleitung benennt die zu erklärenden Begriffe als Arbeitsauftrag, bietet
aber keine gleichwertigen eigenen Definitionen für Image/Container,
Toolchain, MSL, CLI/TUI, SBOM und Spec Kit. Damit können Leser*innen ohne
das ausgeschlossene Vorwissen die Sicherheits- und Werkzeuganforderungen
nicht in beiden Sprachen gleichwertig verstehen.

**Erforderliche Korrektur:** Begriffe bei ihrem ersten Auftreten kurz auf
B2-Niveau erklären oder vorher ein tatsächlich zweisprachiges Glossar
bereitstellen und lesbar darauf verweisen. Technische Kennungen bleiben
unverändert; es geht um Erklärung, nicht Übersetzung von Optionsnamen.
Beide Sprachfassungen müssen selbständig verständlich sein. Den gesamten
Begriffsbestand systematisch prüfen, nicht nur die Beispiele dieses Befunds.
Danach Ziel-/Receipt-Provenienz autorisiert aktualisieren und das vollständige
Single-Review erneut ausführen. Dieses Review verändert das Ziel nicht.

**Neubewertung:** Nach autorisierter redaktioneller Korrektur einschließlich
aktueller Ziel-/Quellenbindung; erneut gegen die gleiche Lernendenbasis und
das vollständige Lastenheft prüfen. Kein pauschales Ready allein aufgrund
eines ergänzten Glossarworts oder eines grünen Receipt-Validators.

### Vollständiger Checklistenabgleich

| Prüffeld | Ergebnis und Begründung |
|---|---|
| Identität, Zielgruppe, Zweck, Umfang, Nicht-Ziele | Erfüllt: ein gemeinsamer Feature-Block; technische und Governance-Grenzen explizit. |
| Vorausgesetztes Wissen | Erfüllt: grundlegende Computerbedienung, keine Container-/Programmier-/Spec-Kit-Erfahrung. |
| Begriffserklärung und Sprachgleichwertigkeit | Nicht erfüllt: IR701. Keine menschliche B2-/Usability-Abnahme behauptet. |
| Textorientierte Zustände und Abhängigkeiten | Erfüllt: nummerierter Vorschlag, ausdrückliche Nichtbindung, ergänzendes Mermaid mit Textalternative. |
| Anforderungen | Erfüllt im fachlichen Kern: FU-001–023 getrennt identifiziert, gemeinsam zu erfüllende Teilbedingungen und Grenzen sind testbar. Interne Schichtung/Labelname/Präzedenz sind ausdrücklich spätere Planung. |
| Messbare Abnahme | Erfüllt: FA-001–012 mit Profil-/Architektur-/Image-/Exitcode-Bindung, positiven/negativen Fällen und integriertem Abschluss; fehlende Nachweise bleiben offen. |
| Reihenfolge, Rechte, Risiken | Erfüllt: nach Hardening/vor Selbstprüfung nur vorgeschlagen; aktuelle Autorität ist Dokumentarbeit; LocalImplementation ist nur spätere Obergrenze. |
| Security, Datenschutz, Plattform, A11Y, Lieferkette | Erfüllt als Anforderungsvertrag: Isolation, localhost/Auth, Audit-Metadaten, persistente Daten, native Nachweise, Podman und gepinntes Syft; keine technische oder menschliche Abnahme vorweggenommen. |
| Referenzen und Prompts | Erfüllt: drei gebundene lokale Quellen, datierter Upstream-Kontext, exakte Zielpfade und gesonderte Review-/Serien-/Startautorität in den vorbereiteten Prompts. |
| Secrets, personenbezogene Daten, Format | Erfüllt in der lokalen Textsichtung: striktes UTF-8, keine Credentials/privaten Hostpfade/unnötigen Personendaten gefunden. Kein Produkt- oder Laufzeit-Secret-Scan. |

Quellabdeckung: #101 → Basis, Swift/Versionen, Architektur/SELinux und
.NET-Ausgabepfade; #102 → Web/Auth/Readiness/Clients/Port und Audit;
#104 → sieben Profile, Infrastruktur, Wrapper-/SBOM-Verträge und Profiltests.
Gemeinsame Lernenden-/Security-/A11Y-/Plattformgates und integrierte Abnahme
sind erhalten. Keine weitere fachliche Lücke oder widersprechende
Ausführungsautorität festgestellt.

### Ergebnisgrenzen und nächster Schritt

Zählung: Critical 0, High 0, Medium 1, Low 0. Akzeptierte Risiken 0,
offene Rückfragen 0, Operator-Ausnahmen 0. Es ist eine redaktionelle
Nachbesserung erforderlich, keine neue Produktentscheidung.
Das bestehende Create-Receipt bleibt unverändert `ReadyForReview`; das
separat gespeicherte aktuelle Review lautet `NeedsRemediation`. Keine
historischen Reviews überschrieben (`supersedes: N/A`, erster Review
dieses neuen Ziels).

Die Requirements-Konfiguration und der Authoring-Validator sind bestanden.
Der Review-Result-Validator prüft die Struktur und aktuelle Hashbindung
des getrennten Ergebnisses; das ist keine Produkt-/WCAG-/Plattformfreigabe.
Keine Implementation, Builds, Containeraktionen, Pilotdurchführung,
Modellaufrufe, Commits, Pushes, Remote-Schreibzugriffe oder Serienänderung.

Genau nächster Schritt, hier nicht ausgeführt:

```text
$speckit-intake-repair Lastenheft_Sandbox-Feature-Update-Ubuntu2604-OpenCode-Web-MSL.md — behebe IR701 aus specs/intake-review-results/sandbox-feature-update-2026-10-28.json, aktualisiere die Provenienz und führe anschließend das vollständige Single-Review erneut aus; keine Implementierung, Serienmigration oder Remote-Schreiboperation.
```

## English

**Outcome: NeedsRemediation**, Single mode, one target, zero workers.
The target hash and repository head above bind this local review; the target
is untracked and is not represented by the commit alone. This is a review in
the authoring chat, not independent human four-eyes evidence.

IR701 (Medium, owner Requirements Author / Documentation & Learning Review)
is open and requires remediation. The declared first-year audience assumes
no container/programming/Spec Kit experience, yet SELinux, Bubblewrap,
capability drops, Seccomp and LSP appear without first-use explanations.
The English introduction instructs future authors to explain the basics
instead of providing equivalent definitions. Add concise first-use B2
explanations or a usable bilingual glossary while retaining exact technical
identifiers. Review the complete terminology in both languages, refresh
authorized target/receipt provenance and repeat the full Single review.
Re-evaluate after that correction; a hash or isolated glossary addition alone
does not establish readiness.

The other checklist areas passed at the requirements level: identity,
scope/non-goals, assumed knowledge, textual dependencies/status, testable
requirements, measurable acceptance, bounded authority/order/risks,
security/privacy/accessibility/platform/supply-chain applicability,
references/prompts and local text-format/sensitive-data inspection. The three
bound issue snapshots cover the base/.NET fix, web/auth/readiness and profile
selection plus shared safeguards and integrated acceptance. No other scope
gap was identified. Upstream live status and actual implementation were not
tested or re-reviewed.

Schema-2 requirements configuration is Aligned; the create receipt and all
three source hashes are current. SeriesManifest mode permits a standalone
intake, so no series migration is needed for this review. Existing four-member
ordering and the sole Eligible hardening target remain unchanged.

Counts: 0 Critical, 0 High, 1 Medium, 0 Low; 0 accepted risks, 0 open questions,
0 operator exceptions. No historical review is superseded. The untouched
authoring receipt still says ReadyForReview; the separate current review says
NeedsRemediation. Structural result validation is no product, WCAG, platform
or formal approval. No implementation, builds, runtime, pilot, inference,
commit, push, remote mutation or series change was performed.

The sole next action is the bounded Intake Repair command above, followed
by a complete re-review. That command has not been executed.
