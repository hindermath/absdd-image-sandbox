# Dependency Update Policy / Abhaengigkeits-Updates

## Deutsch

Owner ist der Repository-Maintainer. Das `Dockerfile` bleibt die einzige Quelle
fuer Versionswerte und Archiv-Pruefsummen. Das [Pin-Register](../../scripts/config/toolchain-pins.json)
ordnet 29 Versions-ARGs offiziellen Quellen und 28 Gruppen zu; das 30. ARG
`ADE_MSL_PROFILE` ist ein geprüfter Build-Selektor. Python-Version und
Builddatum bewegen sich gemeinsam. Renovate ist abgeloest; historische Evidence
bleibt unveraendert.

[Dependabot](../../.github/dependabot.yml) pflegt Actions, externe pre-commit-
Hooks und Basisimage-Digests im freigegebenen MCR-Tag `10.0.403-resolute`. Hoehere Versionen
sind ausgeschlossen. `docker` bezeichnet das Manifestformat; **Podman bleibt
die verbindliche Build-Engine**. Zeitplan, Gruppierung und Ausschluesse stehen
im [Wartungspfad](../../.github/DEPENDENCY-MAINTENANCE.md). Sicherheitsgruppen
ersetzen keinen Schwachstellen-Scanner fuer beliebige ARGs.

Der [Pin-Workflow](../../.github/workflows/toolchain-pins.yml) prueft montags
06:20 UTC (07:20 MEZ / 08:20 MESZ) die ARGs. Manuell ist `check` der read-only
Standard; `propose` bereitet hoechstens einen Gruppen-PR vor. Gruppen mit offenem
PR werden uebersprungen; maximal fuenf eigene PRs bleiben offen. Kein direktes
Push nach main, kein Force-Update und kein Auto-Merge. Bestehende Gruppen-PRs
werden manuell abgeschlossen, bevor der naechste Vorschlag folgt.

### Quellen und Schutzregeln

Nur feste offizielle HTTPS-Hosts sind erlaubt. Redirects, uebergrosse Antworten,
fehlende oder mehrdeutige Metadaten werden abgewiesen. Ein optionales GH_TOKEN
geht nur an api.github.com. Downloads werden gehasht, niemals ausgefuehrt.
Offline-Fixtures besitzen keinen Netzwerk-Fallback.

- Java LTS25, Node LTS24 und npm12 bleiben ihre freigegebenen Kanaele. APT
  liefert Java-/Node-Patchpakete beim Build. Das Kompatibilitaets-SDK bleibt
  bei .NET10.0.3xx. Andere Feature-Baender brauchen bewusste Freigabe.
- Swift bleibt wegen des gepinnten 6.x-Signierschluessels bei Major6. Ein neuer
  Major erzeugt PolicyHeld; der Schluesselwechsel braucht eigenes Review.
  Auch Patch-Wechsel bleiben PolicyHeld, solange das zentral verteilte
  Level-0-Swift-Register nicht koordiniert aktualisiert wurde. Go-/Rust-PRs
  fuehren die daraus abgeleiteten Versionen der Lernenden-Tabelle mit.
- Andere stabile Releases werden ohne Downgrades vorgeschlagen. GitHub-Assets
  brauchen eindeutige SHA-256-Digests. Go, Maven und .NET verwenden offizielle
  Pruefsummen. PowerShell-Pakete werden von einer festen Microsoft-Quelle
  gestreamt und SHA-256-gehasht. Versionswerte und vollstaendige AMD64-/ARM64-
  Hashes bewegen sich atomar. Syfts Standardversion liest auch das Build-/SBOM-
  Skript aus dem Dockerfile; explizite lokale Overrides bleiben erkennbar.
- Fehlende Hersteller-Evidence blockiert den gesamten Vorschlagslauf als
  Blocked. Der Bericht nennt die betroffene Gruppe. Es gibt keinen unsicheren
  Ersatzwert. PolicyHeld kennzeichnet dagegen eine bewusste Kanalgrenze.

Home Baseline Schema2 bleibt manuell reviewpflichtig: oeffentliche HTTPS-Quelle,
refType commit, exakter 40-stelliger Commit und MIT-Lizenz. Der Build verifiziert
Commit, Lizenz und Lernenden-Anleitung; lokale Maintainer-Kopien sind keine
Quelle. Der eingebettete Spec-Kit-Release-Commit bleibt ebenfalls manuell;
Struktur-/Idempotenztests des Container-Patches und CLI-/Installations-Smokes
sind erforderlich. Diese Inhalts-Pins sind keine ARG-Gruppen.

Archiv-Hashes, Swift `gpg --assert-signer`, rootless Runtime, entfernte
Capabilities und no-new-privileges bleiben verbindlich. Keine globale npm-
Skriptfreigabe: Nur die bestehenden benannten OpenCode-, Claude-Code-, keytar-
und node-pty-Hooks werden abgeschlossen; Versions-/Modul-Ladechecks bleiben
erforderlich. Ein neuer Kanal oder Installationsmechanismus braucht Review.

### Pruefung und Betrieb

macOS/Linux verwenden die Bash-Oberflaeche, Windows direkt PowerShell7:

```bash
bash scripts/update-toolchain-pins.sh --help
bash scripts/update-toolchain-pins.sh --action Check --json
pwsh -NoProfile -File scripts/tests/test-toolchain-pin-updates.ps1
python3 scripts/check-toolchain-pins.py
```

Check laesst das Repository unveraendert. Exit0 bedeutet vollstaendigen Abgleich,
Exit1 eine blockierte Quelle, Exit2 einen Eingabe-/Vertragsfehler. Prepare
verlangt einen sauberen Commit und ein neues externes Verzeichnis. Verify
prueft offline HEAD, Quellbytes und erlaubte Aenderungen. Apply wird zuerst mit
--dry-run bzw. -WhatIf geprueft und ersetzt ausschliesslich das verifizierte
Dockerfile atomar. Siehe [Manpage](../man/update-toolchain-pins.1.md). Diese
Befehle installieren nichts, starten keine Container und publizieren kein Git.

Nur bereits gepruefter Code auf main darf Quellen abfragen und publizieren.
PRs fuehren Offline-Vertraege auf Linux, macOS und Windows aus. Kein
pull_request_target, keine Host-Zugangsdaten im Container. Der Discovery-Job
hat Leserechte, bindet eine Payload an HEAD und SHA-256 und verlangt vor
Publikation einen isolierten nativen Linux/AMD64-Podman-Build, Toolchain-/
Dokumentations-Smokes und CycloneDX-SBOM. Smokes laufen ohne Netz, ohne
Capabilities und mit no-new-privileges. Vorschlag, Quellbindung, Image-ID, SBOM
und Proof bleiben 14 Tage als Artefakte erhalten. ARM64-Ausfuehrung ist darin
ausdruecklich NotPerformed und bleibt ein separater Nachweis.

Erst danach erhaelt der getrennte Publisher contents/write und
pull-requests/write. Er prueft Payload, aktuellen main-HEAD und erlaubte Pfade
erneut, regeneriert die konfigurierten Statistik-Ausgaben und erstellt einen regulaeren PR.
Er nutzt das kurzlebige GITHUB_TOKEN, kein neues PAT und keinen externen Bot.
Actions muss in den Repository-Einstellungen PRs erstellen duerfen. Token-
erzeugte PR-Workflows koennen **Approve workflows to run** durch einen Menschen
benoetigen; der Vorlauf ersetzt diese PR-Checks nicht.

Vor Merge Hersteller-Release, Hashes, Kanaele, Installation, native Architekturen,
SBOM und erforderliche exakte Head-Checks pruefen. AMD64 beweist weder ARM64
noch Produkt-/Barrierefreiheitsabnahme. Menschliches Review und Branch-Schutz
bleiben verbindlich. Nach Merge erste Dependabot-/Pin-Laeufe und Artefakte
pruefen; bei Blocked die genannte Quelle korrigieren. Die Einrichtung ersetzt
keinen laufenden Container.

## English

The repository maintainer owns this policy. The Dockerfile remains the sole
source of versions and archive hashes. The registry covers 29 version ARGs in
28 groups plus the validated `ADE_MSL_PROFILE` build selector; Python version/date move together. Renovate is retired; historical
evidence is retained. Dependabot maintains Actions, external pre-commit hooks
and the base digest within approved MCR tag `10.0.403-resolute`; higher versions are excluded.
Docker is the manifest ecosystem; **Podman is the required engine**. See the
maintenance guide for schedules, grouping and exclusions. Security groups do
not scan arbitrary ARGs for vulnerabilities.

The pin workflow runs Monday06:20UTC (07:20CET / 08:20CEST). Manual dispatch
defaults to read-only check; propose emits at most one group PR. Groups with
open PRs are skipped and at most five own PRs remain open. There is no direct
main push, force update or auto-merge. Review/close an existing group PR before
its next proposal. Only fixed official HTTPS hosts are read. Redirects,
excessive responses and missing/ambiguous metadata fail closed. GH_TOKEN is
sent only to api.github.com. Downloads are hashed, never executed. Offline
fixtures never fall back to network access.

Java LTS25, Node LTS24 and npm12 remain approved channels. APT supplies Java/
Node patch packages at build time. The compatibility SDK stays in .NET10.0.3xx.
Swift stays within major6 because of its pinned signing key; a new major
produces PolicyHeld pending key/channel review. Other stable releases may be
proposed without downgrades. GitHub archive assets need unique SHA-256 digests;
Go, Maven and .NET use official checksums. PowerShell packages are streamed
from a fixed Microsoft source and SHA-256 hashed. Versions and complete AMD64/
ARM64 hash sets move atomically. Syft's build/SBOM default also comes from the
Dockerfile; explicit local overrides remain supported. Missing evidence blocks
the entire proposal run and names its group. No insecure fallback is used;
PolicyHeld records a deliberate channel boundary. Swift patch changes are
also held until the canonical Level-0 registry is updated through coordinated
propagation. Go/Rust proposals update their derived learner version rows.

Home Baseline schema2 content pins remain manual: public HTTPS source,
refType commit, exact 40-character commit and MIT license. Builds verify the
commit, license and learner guide; local maintainer copies are not sources.
The embedded Spec Kit release commit also remains manual, with container-patch
structure/idempotency tests and CLI/install smokes. Neither content pin is an
ARG group. Fixed archive hashes, Swift assert-signer, rootless runtime, dropped
capabilities and no-new-privileges remain required. No blanket npm script
approval is introduced; only existing named OpenCode, Claude Code, keytar and
node-pty hooks may be finalized, followed by version/native-module checks.
New channels or install mechanisms require review.

Use the Bash wrapper on macOS/Linux and PowerShell7 directly on Windows.
Commands and the linked manpage above apply to both. Check does not change
the repository: exit0 means complete discovery, exit1 a blocked source, exit2
an input/contract error. Prepare requires a clean commit and a new external
directory. Verify checks source HEAD, bytes and permitted changes offline.
Preview Apply with --dry-run/-WhatIf; it atomically replaces only the verified
Dockerfile. These scripts do not install, start containers or publish Git.

Only reviewed main code may discover/publish. PRs run offline contracts on
Linux, macOS and Windows. No pull_request_target or host credentials inside
containers. The read-only discovery job binds a payload to HEAD/SHA-256 and
requires an isolated native Linux/AMD64 Podman build, toolchain/documentation
smokes and CycloneDX SBOM before publication. Smokes use no network, dropped
capabilities and no-new-privileges. Proposal, source binding, image ID, SBOM
and proof artifacts remain for14days. ARM64 execution is explicitly
NotPerformed and requires separate evidence.

Only then does a separate publisher gain contents/write and pull-requests/write.
It rechecks immutable payloads, current main and permitted paths, regenerates
configured statistics outputs and creates a regular PR using short-lived GITHUB_TOKEN.
No new PAT or external bot is needed. Repository settings must allow Actions
to create PRs. Token-generated PR workflows may need human **Approve workflows
to run**; prior build proof does not replace PR checks. Review official releases,
hashes, channels, installation, native architectures, SBOM and required exact-
head checks before merge. AMD64 proves neither ARM64 nor product/accessibility
acceptance. Human review/branch protection remain binding. Inspect first runs
and artifacts after merge; correct the named source on Blocked. This setup
does not replace any running container.

## Basisimage-Nachweis / Base-image evidence

DE: Dockerfile- und Basisdigest-Aenderungen erhalten im Workflow
[Base image Podman proof](../../.github/workflows/base-image-proof.yml) einen
isolierten nativen Linux/AMD64-Build mit Podman, Offline-Smoke-Tests der
Toolchains und Dokumentationswerkzeuge sowie ein CycloneDX-SBOM. Der Nachweis
bindet PR-Head, Dockerfile-Hash, Image-ID und SBOM-Hash. Der kurzlebige
GitHub-Runner darf unbenoetigte vorinstallierte SDKs entfernen, um den vollen
Build mit mindestens 32 GiB freiem Platz zu starten. Der Job hat nur Leserechte,
keine Publishing-Credentials und verteilt kein Image. Native ARM64-Ausfuehrung,
menschliche Freigabe und Flotten-Rollout bleiben getrennte Nachweise.
Owner: Repository-Maintainer. Neu pruefen bei Basisimage-, Build- oder
Runner-Aenderungen.

EN: Dockerfile and base-digest changes receive an isolated native Linux/AMD64
Podman build, offline toolchain/documentation smoke tests and a CycloneDX SBOM
in [Base image Podman proof](../../.github/workflows/base-image-proof.yml).
Evidence binds the PR head, Dockerfile hash, image ID and SBOM hash. The
disposable GitHub runner may remove unused preinstalled SDKs to start the full
build with at least 32 GiB free space. The job has read-only permissions, no
publishing credentials and publishes no image. Native ARM64 execution, human
approval and fleet rollout remain separate evidence boundaries.
Owner: repository maintainer. Reevaluate after base-image, build or runner changes.
