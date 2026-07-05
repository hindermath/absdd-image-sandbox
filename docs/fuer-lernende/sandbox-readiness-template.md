# Sandbox-Readiness-Nachweis (Vorlage) / Sandbox Readiness Evidence (Template)

**Stand / Date:** 2026-07-05
**Zielgruppe / Audience:** 2. Lehrjahr / Year 2
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

---

## Hinweis zur Verwendung / How to Use This Template

**DE:** Diese Vorlage ist dein Arbeitsdokument für die Sandbox-Readiness-Entscheidung im 2. Lehrjahr.
Fülle alle Felder mit `[...]` aus. Abkürzungen wie `Applicable`, `N/A` und `Open` sind im
[GLOSSAR.md](GLOSSAR.md) erklärt. Deine Ausbilderin oder dein Ausbilder legt fest, welche Teile du abgeben
musst.

**EN:** This template is your working document for the sandbox readiness decision in year 2. Fill in all
fields marked with `[...]`. Abbreviations such as `Applicable`, `N/A`, and `Open` are explained in
[GLOSSAR.md](GLOSSAR.md). Your instructor decides which parts you need to submit.

**DE:** Im 2. Lehrjahr ist praktische Sandbox-Nutzung **noch keine harte Pflicht**. Die bewusste
Entscheidung — `Applicable`, `N/A` oder `Open` mit Begründung — ist selbst der Nachweis.

**EN:** In year 2, practical sandbox use is **not yet a hard requirement**. The deliberate decision —
`Applicable`, `N/A`, or `Open` with rationale — is itself the evidence.

---

## Kopfdaten / Header

| Feld / Field | Wert / Value |
|---|---|
| Lernende/r / Learner | `[Name]` |
| Projekt / Project | `Secure CaseTracker` (oder: `[Projektname]`) |
| Sprachpfad / Language path | `[C# / Go / Java / Python / Rust / Swift]` |
| Lehrjahr / Training year | 2. Lehrjahr / Year 2 |
| Datum / Date | `[YYYY-MM-DD]` |
| Zugehöriges Lastenheft / Related intake | `Lastenheft_Secure-CaseTracker-v2_09_Sandbox-und-Betriebsnachweise.md` |

---

## 1 Sandbox-Referenz / Sandbox Reference

**DE:** Trage die öffentliche Referenz-Sandbox und ihre Laufzeit ein.

**EN:** Enter the public reference sandbox and its runtime.

| Feld / Field | Wert / Value |
|---|---|
| Öffentliche Referenz / Public reference | `https://github.com/hindermath/absdd-image-sandbox` |
| Container-Engine | `[Podman / Docker]` |
| Basis-Image | `mcr.microsoft.com/dotnet/sdk:10.0` (gepinnt per Digest) |
| Benutzer im Container / User inside | `adedev` |

---

## 2 Betriebsumgebung / Operating Environment

**DE:** Beschreibe in 2–4 Sätzen, welche Konfiguration das System braucht und woher sie kommt.

**EN:** Describe in 2–4 sentences what configuration the system needs and where it comes from.

```text
[Deine Beschreibung hier / Your description here]

Beispiel / Example:
Die Sandbox startet als Podman-Container auf macOS. Die Konfiguration kommt aus Umgebungsvariablen und
der optionalen Datei opencode.env. Laufzeitannahmen: Ubuntu-Linux, adedev-Benutzer, keine Root-Rechte.
```

---

## 3 Schreibgrenzen und Least Privilege / Write Boundaries and Least Privilege

**DE:** Trage ein, welche Verzeichnisse beschreibbar sind und welche nicht.

**EN:** Enter which directories are writable and which are not.

| Verzeichnis / Directory | Schreibrecht / Write | Zweck / Purpose |
|---|---|---|
| `/workspace` | `[Ja/Nein]` | `[Zweck]` |
| `/rider-projects` (oder anderer Sprachpfad) | `[Ja/Nein]` | `[Zweck]` |
| `/ade-dev-sandbox` | `[Ja/Nein]` | `[Zweck]` |
| Systempfade, `.ssh`, `.gnupg` | `[Nein/No]` | Schreibschutz durch Isolation |
| `[Weitere Einträge falls nötig]` | `[...]` | `[...]` |

**DE:** Schreibgrenzen eingehalten? / Write boundaries respected?

```text
[ ] Ja / Yes — alle Schreibbereiche sind bewusst begrenzt
[ ] Nein / No — Begründung: [...]
```

---

## 4 Netzwerk-Annahmen / Network Assumptions

**DE:** Beschreibe, welche ausgehenden Netzwerkverbindungen benötigt werden oder warum keine nötig sind.

**EN:** Describe which outbound network connections are needed or why none are needed.

| Verbindung / Connection | Benötigt? / Needed? | Zweck / Purpose |
|---|---|---|
| Paketregister (npm, PyPI, crates.io, …) | `[Ja/Nein]` | `[...]` |
| MCR für .NET-Image | `[Ja/Nein]` | `[...]` |
| KI-Provider-Endpunkte | `[Ja/Nein]` | `[...]` |
| Offline-Betrieb geplant / Offline planned | `[Ja/Nein]` | `[...]` |

---

## 5 Secret-Regeln / Secret Rules

**DE:** Bestätige, dass du die Secret-Regeln kennst und einhältst.

**EN:** Confirm that you know and follow the secret rules.

```text
[ ] Secrets kommen nicht in den Quellcode oder in getrackte Config-Dateien.
    / Secrets do not go into source code or tracked config files.

[ ] Secrets kommen nicht in KI-Agenten-Prompts.
    / Secrets do not go into AI agent prompts.

[ ] Secrets kommen nicht in Logs oder Screenshots.
    / Secrets do not go into logs or screenshots.

[ ] Testdaten sind fiktiv und datensparsam.
    / Test data is fictitious and data-minimal.

[ ] opencode.env ist in .gitignore und wird nicht hochgeladen.
    / opencode.env is in .gitignore and will not be uploaded.
```

---

## 6 MSL-Toolchain-Status / MSL Toolchain Status

**DE:** Gib für jede Sprache an, ob die Toolchain in der Sandbox verfügbar ist.

**EN:** For each language, indicate whether the toolchain is available in the sandbox.

| Sprache / Language | Status (`Supported` / `Open` / `N/A`) | Kommentar / Comment |
|---|---|---|
| C# / .NET | `[...]` | `[...]` |
| Go | `[...]` | `[...]` |
| Java | `[...]` | `[...]` |
| Python | `[...]` | `[...]` |
| Rust | `[...]` | `[...]` |
| Swift | `[...]` | `[...]` |

---

## 7 KI-Agenten-Grenzen / AI Agent Boundaries

**DE:** Welche Agenten sind für dieses Projekt geplant oder erprobt? Welche Grenzen gelten?

**EN:** Which agents are planned or tested for this project? Which boundaries apply?

| Eigenschaft / Property | Wert / Value |
|---|---|
| Geplante Agenten / Planned agents | `[OpenCode / Codex / Claude / Gemini / keiner]` |
| Dateien, die der Agent ändern darf / Files the agent may modify | `[Pfad/e]` |
| Dateien, die der Agent **nicht** ändern darf | `[Pfad/e]` |
| Secrets in Prompts / Secrets in prompts | **Verboten / Forbidden** |
| Agent-Caches im Repo committen / Commit agent caches | **Verboten / Forbidden** |

---

## 8 Jahr-2-Entscheidung / Year 2 Decision

**DE:** Entscheide dokumentiert, ob praktische Sandbox-Nutzung für dieses Projekt jetzt `Applicable`, `N/A`
oder `Open` ist. Eine Begründung ist Pflicht — stille Auslassung gilt nicht.

**EN:** Decide, documented, whether practical sandbox use for this project is now `Applicable`, `N/A`, or
`Open`. A rationale is mandatory — silent omission does not count.

| Feld / Field | Wert / Value |
|---|---|
| Entscheidung / Decision | `[ ] Applicable  [ ] N/A  [ ] Open` |
| Begründung / Rationale | `[...]` |
| IDE-Arbeit außerhalb / IDE work outside | `[ ] erlaubt für Lesen/Review / allowed for reading/review` |
| Folgeaufgabe / Follow-up task (wenn Open) | `[...]` |

**DE:** Beispiel-Begründung für `N/A`:

**EN:** Example rationale for `N/A`:

```text
Entscheidung: N/A
Begründung: Container-Mount- und Agent-Kenntnisse wurden im 2. Lehrjahr noch nicht vollständig behandelt.
            Das Sandbox-Konzept ist vorbereitet; praktische Nutzung wird ab dem 3. Lehrjahr erwartet.
IDE-Arbeit: JetBrains Rider / VS Code außerhalb der Sandbox erlaubt für alle Codearbeit.
Folgeaufgabe: Sandbox-Nutzung im 3. Lehrjahr (SI-Track Lerneinheit 02).
```

---

## 9 Betriebsnachweise (Planung) / Operational Evidence (Planning)

**DE:** Im 2. Lehrjahr genügt die Planung der Betriebsnachweise. Im 3. Lehrjahr werden sie tatsächlich
geliefert — nutze dann das [betriebsnachweise-template.md](betriebsnachweise-template.md).

**EN:** In year 2, planning the operational evidence is sufficient. In year 3 they are actually delivered —
then use [betriebsnachweise-template.md](betriebsnachweise-template.md).

| Nachweis / Evidence | Geplant? / Planned? | Anmerkung / Note |
|---|---|---|
| Toolchain-Smoke-Test (Versionsausgabe) | `[ ] Ja  [ ] Nein` | `[...]` |
| Secret-Scan (0 Funde) | `[ ] Ja  [ ] Nein` | `[...]` |
| Build-Erfolg (eine Sprache) | `[ ] Ja  [ ] Nein` | `[...]` |
| Test-Lauf grün | `[ ] Ja  [ ] Nein` | `[...]` |

---

## Unterschrift / Signature

| Feld / Field | Wert / Value |
|---|---|
| Lernende/r / Learner | `[Name, Datum]` |
| Ausbilder/in / Instructor | `[Name, Datum]` (Freigabe / Approval) |
