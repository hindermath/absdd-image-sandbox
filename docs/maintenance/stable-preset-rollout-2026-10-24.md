# Vierzehn stabile Preset-Patches / Fourteen stable preset patches

Owner: Thorsten Hindermann. Documentation Impact: `UpdateRequired`.

Aktueller Stand / Current state: Konkrete Patch-Sichtung, eng genehmigte
Host-Compose-Ausnahme und Inhaltscommit sind erfolgt. Statistik-Renderer und
Bash-/PowerShell-CheckOnly bestanden nach dem sauberen Inhaltscommit bei
unveraenderter Konfiguration und Methodik. Remote-CI, Review und Merge/Sync
bleiben bis zum tatsächlichen Ergebnis offen. Earlier pending notes retain
their historical pre-approval state; current local technical checks pass.

## Auftrag und Quellen / Authority and sources

DE: Genehmigter Sandbox-Kandidat nach zentraler Lieferung und Home Runtime.
Quelle ist Home Baseline `ded29751`; die vollstaendigen Tag-Commit- und
ZIP-SHA-256-Bindungen stehen im [Quellen-Lock](stable-preset-source-lock-2026-10-24.json).
Alle vierzehn ZIPs wurden vor Installation geprueft. Der zentrale Installer
uebernimmt dasselbe explizite Vierzehner-Profil mit unveraenderten Prioritaeten.
Der [Installations-Lock](stable-preset-installed-lock-2026-10-24.json) bindet
die tatsaechliche Registry und alle installierten Dateien. Die bestehenden
`gsdb-344-preset-*-lock.json` sind die weiterhin von CI konsumierten aktiven
Integrationslocks; sie werden ebenfalls fortgeschrieben, nicht die alten
Assurance-Kontexte oder historischen Feldtestberichte.

EN: Approved sandbox candidate after central delivery and Home Runtime.
Use the same explicit fourteen-preset profile, immutable released sources and
unchanged priorities. Verify all ZIP hashes and bind observed installation.
Existing CI-consumed integration locks track the current installation;
historical assurance contexts and field reports remain unchanged.

## Komposition und Grenzen / Composition and boundaries

DE: `PresetResolver.resolve_content` liest den tatsaechlichen installierten
Projektgraphen. `CommandRegistrar.register_commands` erzeugt Specify, Plan und
Tasks fuer AGY/Codex, Claude, Copilot und den bestehenden OpenCode-Pfad.
Alle sechs Governance-Wrapper bleiben enthalten; SDK und Validatoren bleiben
unveraendert. Kein Root-/Home-Overlay, keine private Profilmigration,
kein Provider-/Modellaufruf, keine Ausfuehrung eines Spec-Kit-Features.

EN: Native SDK resolution and registration derive all maintained command
surfaces from this project's installed graph. Preserve all six wrappers;
change neither SDK nor validators. No Root/Home overlay, private profile
migration, model call or feature execution.

DE: Der unveraenderte Bestandscontainer laeuft als `adedev`, UID/GID 1655,
mit dem Repository unter `/ade-dev-sandbox`. Kein Image-Pull, Neubau,
Compose-/Mount-/Volumewechsel, allgemeiner Home-Sync oder Runtime-Nachlauf.
VM und Container werden nicht fuer diese Lieferung gestoppt. Build und neue
SBOM sind mangels Imageaenderung N/A. Die bestehende GSDB 3.4.4 bleibt
unveraendert. Der [neue Assurance-Kontext](../security/secure-development/2026-10-24-sandbox-stable-presets/evidence-matrix.md)
haelt technische Integritaet, menschliche Sichtung und Produktfreigabe getrennt.

EN: Reuse the existing non-root container and repository mount without image,
Compose, mount, volume or Home changes. Do not stop the running environment.
No image change means build and new SBOM are N/A. Keep GSDB 3.4.4 unchanged
and separate technical integrity, human sighting and product acceptance.

## Pruefung und Sichtungsgrenze / Validation and sighting boundary

DE: Tatsaechliche lokale Pruefergebnisse werden im
[Sitzungsprotokoll](../security/agent-session-log/2026-10-24-stable-presets.md)
und strukturierten Gate-Nachweis erfasst. Fehlende oder noch laufende Gates
sind kein Erfolg; Linux-Containernachweise ersetzen keine Windows-, macOS-,
Screenreader-, Rechts- oder Produktabnahme. Kein neues externes Normenreview.
Vor Commit und Push wird der vollstaendige Diff einschliesslich Sitzungslog
als Patch mit SHA-256 zur ausdruecklichen Sichtung vorgelegt. Der Modus
MergeAndSync mit Admin-Bypass ersetzt weder diese Sichtung noch gruene Checks.

EN: Record actual local outcomes, never pending checks as passes. Linux
container evidence is not cross-platform, accessibility, legal or product
acceptance, nor a fresh external standards review. Present the full patch,
session log and SHA-256 before commit/push. Delivery mode and admin bypass
replace neither explicit sighting nor successful technical checks.

DE: Der Statistik-Renderer verweigert das Schreiben im absichtlich noch
uncommitteten Kandidaten. Die Vorschau und der Ledger-Eintrag sind vorhanden;
der Profil-2-Block wird erst nach gesichtetem Inhaltscommit sauber neu erzeugt.
Das Compose-Pflichtgate ist bis zur ausdruecklich genehmigten Loesung fuer die
fehlenden Container-Clients offen. Keine dieser Grenzen wird umgangen.

EN: Statistics writing correctly requires a clean tree. Preview and ledger
entry are prepared; render Profile 2 after the approved content commit.
The required Compose gate remains open until the missing-container-client
boundary is explicitly resolved. Neither guard is bypassed.

## Sichtung erfolgt / Sighting completed

DE: Der Owner hat den exakten vollstaendigen Kandidaten `7fcafe06f6d8ceb7beeebb2b42ad55aaefcf81c437119083cc514c86fa09a2d3` gesichtet und die Lieferung freigegeben. Die separat genehmigte einmalige Host-Compose-Konfigurationspruefung bestand mit Exit 0; keine Tools wurden nachinstalliert. Ausschliesslich belegte Ergebnisfortschreibung und generierte Statistik bei unveraenderter Konfiguration/Methodik sind danach ohne erneute Einzelsichtung erlaubt. Die vorstehenden offenen Punkte beschreiben den Zustand vor dieser Entscheidung. Produkt- und allgemeine Freigaben bleiben getrennt offen.

EN: The owner sighted the exact full patch and authorized delivery. The explicit one-time host Compose exception passed; no tool installation. Further sighting is waived only for observed result metadata and generated statistics under unchanged configuration/methodology, not functional expansion or product acceptance.
