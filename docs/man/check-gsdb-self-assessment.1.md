# check-gsdb-self-assessment(1)

## Name

`check-gsdb-self-assessment` - prueft GSDB-Bereitschaft ohne Spec-Kit-Lauf und bereitet ein Intake vor

*checks GSDB readiness without starting a Spec Kit run and prepares an intake*

## Synopsis

```bash
bash scripts/check-gsdb-self-assessment.sh [--repo PATH] [--check-only] [--dry-run]
```

```powershell
pwsh -NoProfile -File scripts/check-gsdb-self-assessment.ps1 -Repo PATH -CheckOnly
pwsh -NoProfile -File scripts/check-gsdb-self-assessment.ps1 -Repo PATH -WhatIf
```

## Beschreibung / Description

Das Werkzeug fuehrt einen GSDB-Preflight aus. Es prueft, ob die Generische
Secure-Development Basis im Zielrepo vorhanden ist, ob die 12 Checklisten, der
Sammelband, mitgeltende Dokumente, Preset-Verzahnung, MSL-Status,
Governance-Presets und Nachweisorte sichtbar sind.
Bei Intake-Dateien akzeptiert der Preflight sowohl den aktiven Root-Namen als
auch einen nach erfolgreichem Feature-Abschluss archivierten numerischen
Branch-Suffix, zum Beispiel
`Lastenheft_Secure-Development-Hardening.016-secure-development-hardening.md`.
Ein archivierter Nachweis wird nicht als neues aktives Intake dupliziert.

*The tool runs a GSDB preflight. It checks whether the Generic Secure
Development Baseline is present in the target repository and whether the 12
checklists, compendium, related documents, preset alignment, MSL status,
governance presets, and evidence locations are visible.*

*For intake files, the preflight accepts both the active root name and a
numeric branch-suffixed file archived after successful feature completion, for
example
`Lastenheft_Secure-Development-Hardening.016-secure-development-hardening.md`.
An archived record is not duplicated as a new active intake.*

Im normalen Lauf schreibt das Werkzeug `docs/security/gsdb-self-assessment.md`,
erzeugt oder aktualisiert
`Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md` und nimmt dieses Lastenheft in
`Lastenheft_Abarbeitungsreihenfolge.md` auf. Es startet keinen Spec-Kit-Lauf.

*In a normal run, the tool writes `docs/security/gsdb-self-assessment.md`,
creates or updates `Lastenheft_GSDB-Spec-Kit-Intensivpruefung.md`, and adds
that requirements document to `Lastenheft_Abarbeitungsreihenfolge.md`. It does
not start a Spec Kit run.*

## Optionen / Options

| Bash | PowerShell | Bedeutung / Meaning |
|---|---|---|
| `--repo PATH` | `-Repo PATH` | Explizites Repository pruefen; wiederholbar |
| `--preset-profile NAME` | `-PresetProfile NAME` | Explizites Profil; sonst Registry-Eintrag, danach Katalogstandard / Explicit profile, then registry, then catalog default |
| `--registry PATH` | `-Registry PATH` | Alternative Registry-Datei |
| `--home-dir PATH` | `-HomeDir PATH` | Root fuer registry-relative Pfade |
| `--check-only` | `-CheckOnly` | Nur pruefen, nichts schreiben |
| `--fail-on-open` | `-FailOnOpen` | Bei offenen Punkten non-zero beenden |
| `--dry-run` | `-WhatIf` | Schreibaktionen nur anzeigen |

## Beispiele / Examples

```bash
bash scripts/check-gsdb-self-assessment.sh --repo ~/RiderProjects/TinyCalc --check-only
bash scripts/check-gsdb-self-assessment.sh --repo ~/RiderProjects/TinyCalc --dry-run
bash scripts/check-gsdb-self-assessment.sh --dry-run
```

```powershell
pwsh -NoProfile -File scripts/check-gsdb-self-assessment.ps1 -Repo ~/RiderProjects/TinyCalc -CheckOnly
pwsh -NoProfile -File scripts/check-gsdb-self-assessment.ps1 -Repo ~/RiderProjects/TinyCalc -WhatIf
pwsh -NoProfile -File scripts/check-gsdb-self-assessment.ps1 -WhatIf
```

## Grenzen / Boundaries

Der Preflight ist kein Haertungslauf und keine Freigabe. Das erzeugte Lastenheft
ist Intake fuer einen spaeter manuell gestarteten `/speckit-specify`-Lauf.

*The preflight is not a hardening run and not an approval. The generated
requirements document is intake for a later manually started `/speckit-specify`
run.*

## Profilbindung / Profile Binding

DE: Statt bloßer Preset-Verzeichnisse wird die exakte Matrix des zugeordneten
Profils mit Version, Priorität, Aktivierung und Manifestidentität geprüft.
Unbekannte Profile stoppen ohne stillen Fallback. `none` ist eine ausdrückliche
N/A-Entscheidung. Level 0 kann ohne Level-2-Registry-Zeile explizit mit
`--preset-profile project-statistics-fourteen-governance-presets` geprüft werden.

EN: Validate the assigned profile's exact matrix including version, priority,
enabled state, and manifest identity. Unknown profiles stop without fallback.
The explicit none profile records N/A. Use the explicit profile option for
Level 0 when no Level-2 registry row applies. The preflight does not establish
semantic GSDB currency; use the source review and compendium validator too.
