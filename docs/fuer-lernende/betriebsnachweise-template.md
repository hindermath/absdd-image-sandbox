# Betriebsnachweise (Vorlage) / Operational Evidence (Template)

**Stand / Date:** 2026-07-05
**Zielgruppe / Audience:** 3. Lehrjahr, SI-Track und DV-Track / Year 3, SI track and DV track
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

---

## Hinweis zur Verwendung / How to Use This Template

**DE:** Diese Vorlage ist dein Arbeitsdokument für Betriebsnachweise aus der Sandbox-Arbeit im 3. Lehrjahr.
Fülle alle Felder mit `[...]` aus. Betriebsnachweise sind **nachvollziehbare Belege** — keine bloßen
Behauptungen. Ein Nachweis enthält: was gelaufen ist, wann, mit welchem Ergebnis (oder: warum `Open`/`N/A`).

**EN:** This template is your working document for operational evidence from sandbox work in year 3. Fill in
all fields marked with `[...]`. Operational evidence means **traceable proof** — not mere claims. Evidence
contains: what ran, when, with what result (or: why `Open`/`N/A`).

**DE:** Wichtig: Kein Screenshot ohne Alternativtext — nutze Textblöcke mit Datum und Ergebnis, damit die
Nachweise mit Screenreader und Braille-Zeile lesbar sind (WCAG 2.2 AA).

**EN:** Important: No screenshot without alternative text — use text blocks with date and result so that the
evidence is readable with a screen reader and Braille display (WCAG 2.2 AA).

---

## Kopfdaten / Header

| Feld / Field | Wert / Value |
|---|---|
| Lernende/r / Learner | `[Name]` |
| Projekt / Project | `Secure CaseTracker` (oder: `[Projektname]`) |
| Track / Track | `[ ] SI-Track (Operations)  [ ] DV-Track (Digital Networking)` |
| Sprachpfad / Language path | `[C# / Go / Java / Python / Rust / Swift]` |
| Lehrjahr / Training year | 3. Lehrjahr / Year 3 |
| Datum Nachweis / Evidence date | `[YYYY-MM-DD]` |
| Zugehöriges Lastenheft / Related intake | `[Lastenheft-Dateiname]` |

---

## 1 Verwendete Sandbox-Konfiguration / Sandbox Configuration Used

**DE:** Verweise auf das ausgefüllte Sandbox-Profil oder fülle die Kurzform aus.

**EN:** Reference the filled sandbox profile or complete the short form.

| Eigenschaft / Property | Wert / Value |
|---|---|
| Öffentliche Referenz / Public reference | `https://github.com/hindermath/absdd-image-sandbox` |
| Sandbox-Profil-Datei / Sandbox profile file | `docs/fuer-lernende/sandbox-profil.md` (oder: Eigene Instanz) |
| Container-Engine | `Podman` |
| Image-Version (Digest oder Tag) / Image version | `[sha256:... / :latest@...]` |
| Benutzer im Container / User inside | `adedev` |
| Betriebsdatum / Operation date | `[YYYY-MM-DD]` |

---

## 2 Toolchain-Nachweis / Toolchain Evidence

**DE:** Führe `bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh` im Container aus und kopiere
die Ausgabe als Text (nicht als Screenshot). Kürze lange Ausgaben auf die relevanten Zeilen.

**EN:** Run `bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh` inside the container and paste the
output as text (not as a screenshot). Shorten long outputs to the relevant lines.

```text
Datum / Date: [YYYY-MM-DD HH:MM]
Befehl / Command: bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh

Ausgabe (relevante Zeilen) / Output (relevant lines):
[Hier einfügen / Paste here]

Ergebnis / Result: [ ] Alle Sprachen OK  [ ] Offene Punkte: [...]
```

**DE:** Alternativ — manuelle Versionsabfrage:

**EN:** Alternative — manual version query:

```text
Datum / Date: [YYYY-MM-DD]
dotnet --version:   [...]
go version:         [...]
java --version:     [...]
python --version:   [...]
rustc --version:    [...]
swift --version:    [...]
specify version:    [...]
```

---

## 3 Secret-Scan-Nachweis / Secret Scan Evidence

**DE:** Führe einen Secret-Scan durch und dokumentiere das Ergebnis als Text.

**EN:** Run a secret scan and document the result as text.

```text
Datum / Date: [YYYY-MM-DD HH:MM]
Befehl / Command: [bash /ade-dev-sandbox/scripts/scan-agent-secrets.sh oder: pre-commit run --all-files]

Ergebnis / Result:
high=0 medium=0 low=0 total=0

[ ] 0 Funde — kein Secret-Leak gefunden / 0 findings — no secret leak found
[ ] Funde vorhanden — Begründung / Findings present — rationale: [...]
```

---

## 4 Build-Nachweis / Build Evidence

**DE:** Führe einen Build im Container aus und dokumentiere Befehl und Ergebnis.

**EN:** Run a build in the container and document the command and result.

```text
Datum / Date: [YYYY-MM-DD HH:MM]
Verzeichnis / Directory: [/workspace/... oder /rider-projects/...]
Befehl / Command: [dotnet build / go build ./... / mvn compile / python -m build / cargo build / swift build]

Ergebnis / Result:
[ ] Build erfolgreich / Build succeeded
[ ] Build fehlgeschlagen / Build failed — Fehler / Error: [...]
[ ] N/A — kein Build in dieser Einheit / No build in this unit — Begründung / Rationale: [...]
```

---

## 5 Test-Nachweis / Test Evidence

**DE:** Führe die Tests aus und dokumentiere Befehl und Ergebnis.

**EN:** Run the tests and document the command and result.

```text
Datum / Date: [YYYY-MM-DD HH:MM]
Befehl / Command: [dotnet test / go test ./... / mvn test / python -m pytest / cargo test / swift test]

Ergebnis / Result:
[ ] Tests gruen — alle bestanden / Tests green — all passed
[ ] Tests rot / Tests red — Anzahl Fehler / Number of failures: [...]
[ ] N/A — noch keine Tests vorhanden / No tests yet — Begründung / Rationale: [...]
```

---

## 6 Schreibgrenzen eingehalten / Write Boundaries Respected

**DE:** Bestätige, dass die Schreibgrenzen eingehalten wurden.

**EN:** Confirm that write boundaries were respected.

```text
[ ] Alle Schreibvorgänge liefen in erlaubten Verzeichnissen (/workspace, /rider-projects, etc.)
    / All writes happened in allowed directories.

[ ] Keine Schreibvorgänge in Systempfaden, .ssh, .gnupg oder anderen gesperrten Bereichen.
    / No writes to system paths, .ssh, .gnupg, or other denied areas.

[ ] Keine Secrets in Prompts, Logs oder Screenshots.
    / No secrets in prompts, logs, or screenshots.

[ ] Keine echten Personendaten in Sandbox- oder Agentenläufen.
    / No real personal data in sandbox or agent runs.
```

---

## 7 KI-gestützte Arbeit / AI-Assisted Work

**DE:** Falls ein KI-Agent in der Sandbox geschrieben hat, dokumentiere was, wann und in welchem Bereich.

**EN:** If an AI agent wrote files in the sandbox, document what, when, and in which area.

| Feld / Field | Wert / Value |
|---|---|
| Verwendeter Agent / Agent used | `[OpenCode / Codex / Claude / Gemini / keiner]` |
| Veränderte Dateien / Modified files | `[Pfad/e oder: keine / none]` |
| Datum und Uhrzeit / Date and time | `[YYYY-MM-DD HH:MM]` |
| Ergebnis geprüft vor Commit / Result checked before commit | `[ ] Ja / Yes  [ ] Nein — Begründung / No — Rationale: [...]` |
| Agent-Cache committet? / Agent cache committed? | `[ ] Nein / No  [ ] Ja — Korrekturmaßnahme / Yes — Corrective action: [...]` |

---

## 8 Netzwerkzugriffe (DV-Track) / Network Access (DV Track)

**DE:** Nur für den DV-Track: Dokumentiere alle Netzwerkzugriffe mit Zweck und Grenze.

**EN:** DV track only: document all network access with purpose and limit.

| Verbindung / Connection | Erlaubt? / Allowed? | Zweck / Purpose | Status |
|---|---|---|---|
| `[Paketregister / Package registry]` | `[Ja/Nein]` | `[Werkzeuge installieren / Install tools]` | `[Applicable / N/A]` |
| `[Weitere / Additional]` | `[...]` | `[...]` | `[...]` |
| Produktive Daten / Production data | **Nein / No** | Nicht erlaubt / Not allowed | N/A |
| Echte Secrets / Real secrets | **Nein / No** | Nicht erlaubt / Not allowed | N/A |

---

## 9 Abweichungen / Deviations

**DE:** Wenn ausnahmsweise außerhalb der Sandbox gearbeitet wurde: hier dokumentieren. Eine
undokumentierte Abweichung ist ein verstecktes Risiko. Eine begründete Abweichung ist eine bewusste
Entscheidung.

**EN:** If work exceptionally happened outside the sandbox: document it here. An undocumented deviation is a
hidden risk. A justified deviation is a conscious decision.

```text
[ ] Keine Abweichungen. / No deviations.

[ ] Abweichung vorhanden:
    Was lief außerhalb / What ran outside:  [...]
    Grund / Reason:                         [...]
    Auswirkung / Effect:                    [...]
    Restrisiko / Residual risk:             [...]
    Status:                                 [ ] Open  [ ] N/A (begründet / justified)
```

---

## 10 Gesamtbewertung / Overall Assessment

**DE:** Fasse kurz zusammen, ob die Sandbox-Nutzung erfolgreich war.

**EN:** Briefly summarize whether sandbox use was successful.

| Prüfpunkt / Checkpoint | Status |
|---|---|
| Toolchain funktioniert / Toolchain works | `[ ] OK  [ ] Open: [...]` |
| Secret-Scan sauber / Secret scan clean | `[ ] OK  [ ] Open: [...]` |
| Build erfolgreich / Build succeeded | `[ ] OK  [ ] N/A  [ ] Open: [...]` |
| Tests bestanden / Tests passed | `[ ] OK  [ ] N/A  [ ] Open: [...]` |
| Schreibgrenzen eingehalten / Write boundaries respected | `[ ] OK  [ ] Open: [...]` |
| KI-Arbeit geprüft vor Commit / AI work checked before commit | `[ ] OK  [ ] N/A  [ ] Open: [...]` |
| Keine Abweichungen oder begründet dokumentiert | `[ ] OK  [ ] Open: [...]` |

**DE:** Gesamt / Overall:

```text
[ ] Sandbox-Nutzung vollständig und nachvollziehbar nachgewiesen.
    / Sandbox use fully and traceably evidenced.

[ ] Offene Punkte vorhanden — Folgeaufgaben:
    / Open items present — follow-up tasks:
    [...]
```

---

## Unterschrift / Signature

| Feld / Field | Wert / Value |
|---|---|
| Lernende/r / Learner | `[Name, Datum]` |
| Ausbilder/in / Instructor | `[Name, Datum]` (Freigabe / Approval) |

---

## Verweise / References

- [sandbox-profil.md](sandbox-profil.md) — vollständiges Sandbox-Profil
- [sandbox-readiness-template.md](sandbox-readiness-template.md) — Jahr-2-Vorlage
- [GLOSSAR.md](GLOSSAR.md) — Begriffserklärungen
- `docs/secure-development/checklisten/CL_12_Agentische-KI-Sandbox.md` — Checkliste Sandbox-Governance
