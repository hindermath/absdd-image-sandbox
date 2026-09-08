# Secure Development Assurance v0.1.3 – absdd-image-sandbox-Feldtest

## Ergebnis und Scope / Result and Scope

**Empfehlung: `ReleaseAccepted`.** absdd-image-sandbox bestaetigt das
unveraenderte Preset `secure-development-assurance-governance` v0.1.3 im
dokumentierten Projektfeldtest. Die Empfehlung betrifft nur die
Preset-Funktion im nichtkommerziellen Ausbildungs- und Beispielprojekt. Sie ist
keine Produkt-, Image-, Pilot-, Projekt-, Risiko-, C5-, Konformitaets- oder
Zertifizierungsfreigabe.

*Recommendation: `ReleaseAccepted`. absdd-image-sandbox confirms the unchanged
v0.1.3 preset in this documented project field test. This covers preset
behavior in a non-commercial training and example project only. It is not a
product, image, pilot, project, risk, C5, conformity, or certification
approval.*

Test-Owner und technischer Reviewer ist `@hindermath`. Kontext:
`docs/security/secure-development/2026-08-30-gsdb-baseline-assessment`, Modus
`development`. Dockerfile, Compose, OCI-Image, Runtime, Pakete, Mounts,
Netzwerk, Secrets und Deployment wurden nicht geaendert.

## Paket- und Lieferbindung / Package and Delivery Binding

| Feld / Field | Nachweis / Evidence |
|---|---|
| Release | `v0.1.3`, Pre-Release |
| Tag-Commit | `0d03aa9ebe8f74a26e331815bca5609fb48d7a14` |
| ZIP SHA-256 | `9023b442b4d82e25bee5a7fe9b73efb7f591a4f265f54061ae6e4a56b9b5c75f` |
| Spec Kit | `0.12.8` |
| Security Governance | `0.6.2`, Prioritaet 10 |
| Assurance-Preset | `0.1.3`, Prioritaet 15 |
| Profil | 13 Presets, exakt |
| Host | macOS 26.6.2, Apple Silicon; Bash 3.2.57; PowerShell 7.6.5 |
| Delivery | absdd-image-sandbox PR #60; Evidence-Commit wird nach der Git-Bindung ergaenzt |

## Technische Pruefung / Technical Validation

| Test | Ergebnis | Exitcode |
|---|---|---:|
| Release-ZIP und SHA-256 | bestanden | 0 |
| 13-Preset-`CheckOnly`, Bash und PowerShell | bestanden | 0 |
| `preset list`/`info`/`resolve`; `specify check` | bestanden | 0 |
| Status in Bash und PowerShell | `Ready`, fachlich gleich | 0 |
| Vier Einzelreviews je Shell | alle `Ready` | 0 |
| Roh-Hash-Snapshot | 7 von 7 Evidence-Dateien unveraendert | 0 |
| Vertrags-, Negativ-, LF-/CRLF-/BOM- und Shell-Paritaet | bestanden | 0 |
| Acht erzeugte Agenten-/Command-Flaechen | bestanden; fehlende Evidence blockiert geregelt | 0 |
| Temporaere Komposition: 13, Disable, Enable, Remove, gueltige 12, Reinstall | bestanden | 0 |
| Historische Bewertungsmatrix | 157 eindeutige IDs; 157 `Open`, unveraendert | 0 |
| Statische Compose-Konfiguration | `podman-compose config` bestanden | 0 |

Die Negativsuite bestaetigt alle vorgesehenen Fail-closed-Pfade mit dem
erwarteten Exitcode 2; der Gesamttest endet mit 0. Der synthetische
C5-/Zertifizierungsfall prueft ausschliesslich sichere Blockierung und ist
keine C5-Pruefung des Projekts. Der praktische Image-Build und Containerstart
sind `N/A`, weil dieser Feldtest keine Image-, Runtime- oder Paketdatei
aendert; die unveraenderte statische Compose-Konfiguration wurde geprueft.

*The negative suite confirms the required fail-closed paths with exit code 2;
the complete suite returns 0. The synthetic C5/certification case tests safe
blocking only and is not a project C5 assessment. Image build and container
startup are N/A because this field test changes no image, runtime, or package
file; the unchanged static Compose configuration was checked.*

## Grenzen und Wiedervorlage / Boundaries and Review Dates

- Baseline, Delta, Closure und Image Impact sind `Ready`;
  `technicalValidation` ist `Fulfilled`.
- `pilotAuthorization`, `projectAcceptance` und `generalRelease` bleiben
  `Open`.
- Technische Evidence-Wiedervorlage: `2027-09-08`.
- C5 sowie CRA und formale Produktkonformitaet: `N/A` im aktuellen
  nichtkommerziellen Ausbildungs-/Beispielscope.
- Regulatorische Scope-Wiedervorlage: `2026-12-31`, frueher bei kommerzieller
  Nutzung, Marktbereitstellung, Kundenuebergabe, Supportvertrag,
  Cloud-Produkt-Runtime, Provider-Assurance oder geaenderter
  Hersteller-/Steward-Rolle.
- Kein Risiko wurde akzeptiert. Restrisiko ist eine unbemerkte Scopeaenderung.

## Abschluss und Dokumentationsauswirkung / Closeout and Documentation Impact

Es besteht keine fachliche Bash-/PowerShell- oder
LF-/CRLF-/UTF-8-BOM-Abweichung. Offene Punkte dieses Projektfeldtests: keine.
Die Community-Einreichung `github/spec-kit#4455`, alle fuenf Projektberichte
und die spaetere zentrale v0.1.3-Entscheidung werden abgewartet.

`UpdateRequired`. Owner: Thorsten Hindermann. Zielgruppen: Maintainer,
technische Reviewer und Lernende. Leserpfad: v0.1.3-Integration -> Feldbericht
-> Security-Scope -> maschinenlesbare Evidence. Deutsch zuerst, Englisch
danach, textorientiert, `sourceOnly`, kein Home-Sync. Neu bewerten bei Preset-,
Baseline-, Image-, Runtime-, Delivery-, Cloud- oder Scopeaenderung.

*There is no substantive shell or line-ending variance and this project field
test has no open finding. Community issue `github/spec-kit#4455`, all five
project reports, and the later central decision remain pending. Documentation
impact is UpdateRequired, source-only, bilingual, text-first, and requires no
Home sync.*
