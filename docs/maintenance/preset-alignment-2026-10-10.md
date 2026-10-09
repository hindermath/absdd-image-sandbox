# Fuenf Preset-Updates / Five preset updates

Stand / Date: 2026-10-10. Owner: Thorsten Hindermann.
Documentation Impact: `UpdateRequired`.

DE: Der Owner hat den begrenzten Rollout um Authoring und Review erweitert,
damit Sandbox das zentrale 14er-Profil vollstaendig erfuellt. Die anderen neun
Pakete und alle Prioritaeten bleiben erhalten. Zentrale Quelle ist
[Home Baseline PR #332](https://github.com/hindermath/home-baseline/pull/332),
Merge `224739c59311f5f0d64a3037135095288c0aa756`.

EN: Owner authority expands this bounded rollout to Authoring and Review so
Sandbox matches the central fourteen-preset profile. Preserve nine other
packages and all priorities. The linked central delivery is the integration source.

## Ziel und unveraenderliche Quellen / Target and immutable sources

| Preset | Bisher / Before | Ziel / Target | Priority |
| --- | --- | --- | --- |
| Security | 0.6.2 | 0.7.1 | 10 |
| Architecture | 0.5.2 | 0.6.2 | 20 |
| Intake Authoring | 0.3.4 | 0.3.7 | 64 |
| Intake Review | 0.2.3 | 0.2.4 | 65 |
| Intake Sequencing | 0.2.6 | 0.2.8 | 66 |

- Security: tag commit `7204bccbdf3565d4dd22424c7fa7a15c6a6e0eb3`;
  ZIP SHA-256 `c85a4b924e741a3981dc369adc6233b6f323013fb1d46735555038d322cda18a`.
- Architecture: tag commit `017e91a24a685e23f176e98c07c9ac8d81487cbb`;
  ZIP SHA-256 `ebea0ede13e6d72b8d65ae56b08ae28e07b3814aca3f8e9563b6590d0c88a082`.
- Authoring: tag commit `dbf135e89ba583fb27294f84e487cf1a5826604f`;
  ZIP SHA-256 `fc20a010c2124977249f926677d1bb2b03b81e7cd2a549bc4c7489de837e1427`.
- Review: tag commit `f0f9b3536a58f8c90a79119565af8190809a4bdb`;
  ZIP SHA-256 `c4a21c4a99ba6eed0df3028bc1ee19158f1274d9e440f433c504877c997ed816`.
- Sequencing: tag commit `be69290486175fc8256338200b342bf0e33cbb09`;
  ZIP SHA-256 `07dbd79f76927136494fe0742b0e8044d7cb2625c9d5d8f61fbe05b1e8d980ac`.

DE: Alle fuenf Tag-ZIPs wurden heruntergeladen und gegen diese zentralen
SHA-256-Bindungen geprueft. Nur die fuenf Pakete neu installiert; das volle
14er-Profil in Bash/PowerShell gegen die zentrale Matrix geprueft.

EN: Downloaded all five immutable tag ZIPs and verified these central hashes.
Reinstalled only five packages; checked the complete profile against the central
matrix through both shells.

## Fachlicher Delta und Grenzen / Normative delta and boundaries

DE: Anders als in den beiden anderen Piloten ist dies kein reiner README-Patch:
Security erweitert das getrennte regulatorische Screening fuer Beispielprodukt,
Entwicklungswerkzeuge und Organisation (DS-GVO, KI-VO, CRA, NIS2, DORA);
Architecture praezisiert C5 Typ 1/Typ 2 und Cloud-Evidenz. Die Intake-Updates
bringen aktuelle Herkunfts-, Sprach-/Quellen- und Serienvertraege sowie die
direkt auswertbaren Installationsbefehle mit. Ausbildung bedeutet keine pauschale
regulatorische Ausnahme. Ungeklaerte Rollen bleiben Open, keine Rechtsfreigabe.

EN: Unlike the other two pilots, this is not just a README patch. Security adds
separate regulatory screening for example product, tools and organization;
Architecture clarifies C5 Type 1/Type 2 and cloud evidence. Intake updates bring
current provenance, language/source and series contracts plus parseable install
commands. Education is not a blanket regulatory exemption; unknown roles stay
Open, with no legal approval.

DE: Keine bestehende Intake-/Review-Receipt, Assurance-Matrix, Findings oder
menschliche Entscheidung wird automatisch erneuert. Vor einem Produktlauf sind
Quellen-/Review-Frische, Serienstatus, lokales Modell-Routing und aktuelle
Delivery-Autoritaet eigenstaendig zu pruefen. Kein Spec-Kit-Produktlauf, keine
Community-Einreichung, Release-, Risiko- oder formelle Sandbox-Freigabe.
Dockerfile, home-baseline.lock.json, Images und Volumes bleiben unberuehrt.
Die eingebettete Container-Referenz wird nicht still auf den Hoststand gesetzt.

EN: Do not silently refresh existing intake/review receipts, assurance matrices,
findings or human decisions. Before product work independently recheck freshness,
series, local routing and current delivery authority. No product run, community
submission, release/risk/formal sandbox acceptance. Preserve Dockerfile, embedded
baseline lock, images and volumes; host integration is not an image rollout.

## Liefergates / Delivery gates

DE: Lokal bestanden: zentrales 14er-CheckOnly in beiden Shells, list/info/resolve,
specify check, Architecture (sechs Tests), Security (Vertrag, sechs Beispiele,
neun Negativfaelle), Sequencing (sechs JSON-Vorlagen), Authoring (sieben JSON-
Vorlagen, Installationsbefehl, Konfiguration und Validator-Negativfaelle) sowie
Review (Konfiguration, Validator-/Seriengraph- und Negativfaelle). Beide Intake-
Konfigurationstests belegen Bash/PowerShell-JSON- und Zero-write-Paritaet.
Compose-Konfiguration, pre-commit, Secret-Scan und PSScriptAnalyzer (83 Dateien)
bestanden. Scope-Pruefung bestaetigt neun unveraenderte Pakete/Registry-Eintraege
und gleiche Prioritaeten. Keine ungetestete Container-/Image-Abnahme behauptet.

EN: Local checks passed: full central matrix through both shells, CLI inspection,
installed Architecture/Security/Sequencing and Authoring/Review tests, including
negative cases, series graphs, configuration and zero-write shell parity.
Compose configuration, pre-commit, secret scan and static analysis (83 files)
passed. Scope comparison confirms nine unchanged packages/registry entries and
all priorities. This is not an unexecuted container/image acceptance claim.

DE: Die Projekt-Guidance verlangt menschliche Diff-Sichtung vor Commit und Push.
Dieser Nachweis wird einschliesslich Sitzungsprotokoll zur Sichtung vorgelegt.
Technische Gates: beide Matrix-Checks, installierte Paket-/Intake-Tests,
list/info/resolve, specify check, Compose-Konfigurationspruefung, pre-commit,
Secret-Scan und passende statische Pruefungen. Statistik-Nachlauf erst nach
freigegebenem Quell-Commit auf sauberem Arbeitsbaum, ohne Methodikaenderung.
Danach native PR-CI, exakter Head, Review-Befunde und MergeAndSync/Admin-Bypass;
tatsaechlichen Merge, main-CI und 0/0 im PR-Closeout belegen.

EN: Repository guidance requires human diff review before commit and push.
Present this change with the session log first. Gates cover both matrix checks,
installed tests and CLI inspection, Compose configuration, pre-commit, secret
scan and applicable static checks. Refresh statistics only after the authorized
source commit on a clean tree, preserving methodology. Require exact-head native
CI, addressed review findings, merge and verified main 0/0; record actual results.

Audience / Zielgruppe: Maintainer, Sandbox- und Pilot-Reviewer.
Reader path: README / Statistik-Ledger -> dieser Bericht -> zentrale Matrix -> PR.
Canonical source: immutable preset tags and central profile; owner: maintainer.
Class: integration evidence; inline DE first / EN second, text-readable.
Distribution: repository only, sourceOnly evidence; no additional Home Runtime sync.
Reevaluation: source drift or next product preflight. SSDF/CWE apply to integration;
existing cloud/legal/AI-product applicability is not promoted by installation.
