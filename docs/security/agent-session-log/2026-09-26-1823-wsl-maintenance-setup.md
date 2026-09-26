# WSL-Wartungs-Sandbox / WSL maintenance sandbox

## Auftrag und Grenze / Authority and boundary

Der Owner hat am 26.09.2026 die separate Einrichtung und den Start der
Sandbox fuer die vorhandenen WSL-Arbeitskopien ausdruecklich beauftragt.
Fuer die zugehoerigen PRs gilt MergeAndSync mit Admin-Bypass; technische
Pruefungen bleiben verbindlich. Die begrenzte Secure-Trader-Owner-Freigabe
bleibt bis 31.12.2026 massgeblich. Keine neue CISO-/ISB-/KIB-, Provider-,
Modell-, Secret- oder Produktionsfreigabe wird daraus abgeleitet.

The owner explicitly authorized separate sandbox setup and startup for the
existing WSL working copies on 26 September 2026. Related PRs use
MergeAndSync with admin bypass, without waiving technical checks. The
bounded Secure Trader owner approval remains authoritative until
31 December 2026; no additional role, provider, model, secret or production
approval is inferred.

Der Owner hat die Plattformprioritaet klargestellt: macOS ist die primaere
Arbeitsplattform; Windows und Ubuntu/WSL sind Kompatibilitaets-Testplattformen.
Die WSL-spezifischen Einstellungen bleiben maschinenlokal und werden nicht
zum Produktstandard. Dieser Nachweis ersetzt keine native macOS-Abnahme.

The owner clarified that macOS is the primary working platform; Windows and
Ubuntu/WSL are compatibility-test platforms. WSL-specific settings remain
machine-local, not product defaults. This record is not native macOS acceptance.

## Umsetzung / Implementation

- P0-2 / P3-1, Teilfortschritt: Der native Linux-amd64-Build fand einen
  HTTP-404-Fehler beim gepinnten Actionlint-Archiv. Das Release benennt die
  Architektur `amd64`, nicht `x86_64`. Dockerfile und statischer Validator
  verwenden jetzt den veroeffentlichten Namen. Version 1.7.12 und beide
  Architektur-Pruefsummen bleiben unveraendert.
- P3-4, Teilfortschritt: Native rootless Podman-Ausfuehrung in WSL ist
  verfuegbar. Die maschinenlokale Compose-Ergaenzung behaelt
  `no-new-privileges`, `cap_drop: ALL` und Benutzer `adedev` bei. `keep-id`
  bildet die vorhandenen Dateieigentuemer auf die Image-ID 1655:1655 ab.
  Die drei Secure-Trader-Mounts
  sind explizit; die veroeffentlichte Level-0-Quelle ist read-only konfiguriert.
  Die lokale OCI-Runtime-Zuordnung verwendet das vorhandene crun 1.30.1
  passend zu Podman 6.1.2; Ubuntus crun 1.14.1 wies das OCI-Format zurueck.
- P1-1, done: Dieser Nachweis enthaelt nur Betriebsmetadaten. Lokale
  Umgebungsdateien sind untracked, auf Modus 0600 begrenzt und enthalten
  keine Provider-Zugangsdaten.
- P1-4, eskaliert/offen: Der vorhandene Rollenfreigabe-Hinweis bleibt offen.
  Keine menschliche Unterschrift oder Rollenentscheidung wurde simuliert.

P0-2/P3-1 are partially progressed: the Linux-amd64 build exposed a missing
Actionlint asset; the published architecture name is now used without
changing the version or either checksum. P3-4 setup uses native rootless
Podman, preserves the non-root user and hardening, maps existing file owners
with keep-id, and configures the Level 0 source read-only. P1-1 records only
operational metadata; local environment files remain untracked, mode 0600,
and credential-free. P1-4 remains open for the designated human roles.

## Evidence

- Das offizielle Release-API bestaetigt
  `actionlint_1.7.12_linux_amd64.tar.gz` mit SHA-256
  `8aca8db96f1b94770f1b0d72b6dddcb1ebb8123cb3712530b08cc387b349a3d8`.
  Quelle: [Actionlint v1.7.12](https://github.com/rhysd/actionlint/releases/tag/v1.7.12).
- Der aktualisierte statische Validator besteht. Eine ausschliesslich im
  Arbeitsspeicher eingesetzte alte `x86_64`-Zuordnung wird zurueckgewiesen.
- Der reparierte echte Linux-amd64-Build hat alle 69 Schritte erfolgreich
  abgeschlossen (Exit 0). Image-ID:
  `5258a66ef4421f98c1ae45d37c0200dde299171fd6c434820e83f7ee3edcb671`.
  Download, SHA-256-Pruefung und Versionsprobe fuer Actionlint bestehen.
- Alle fuenf Vor-Commit-Pruefungen bestehen, einschliesslich Secret-Scan.
- Compose-Konfiguration und Startvorschau bestehen. Der Container laeuft
  rootless als `adedev`; Inspektion bestaetigt `no-new-privileges`, entfernte
  Capabilities, die drei Workspace-Mounts und die read-only-Level-0-Quelle.
- Der vollstaendige Toolchain-Smoke-Test besteht (Exit 0), einschliesslich
  ausfuehrbarer Beispiele fuer .NET, Java, Go, Rust, Python, PowerShell,
  Node.js und Swift. Die JSON-Probe meldet alle neun Wartungswerkzeuge als
  `Pass`; GitHub-Administration bleibt auf der separaten Host-Steuerung.
- Die Swift-Signaturpruefung meldet eine gute Signatur des gepinnten
  Release-Schluessels, warnt aber vor dessen inzwischen abgelaufener
  Gueltigkeit. Diese Warnung wird nicht als aktuelle Schluesselfreigabe
  umgedeutet; Versions- und Schluesselpin bleiben unveraendert.
- Der Owner hat fuer diesen SBOM-Lauf die vorhandene Host-Version Syft
  1.49.0 ausdruecklich freigegeben. Der Image-Pin 1.46.0 bleibt unveraendert;
  die einmalige Scanner-Auswahl ist keine globale Pin-Aenderung.
- Die CycloneDX-SBOM wurde mit Host-Syft 1.49.0 aus dem gemounteten,
  exakt oben benannten Image erzeugt (Exit 0, kein Registry-Fallback).
  Lokales Artefakt: `sboms/2026-09-26-wsl-maintenance-syft-1.49.0.cdx.json`;
  SHA-256: `405bd4a29542a711f0335b9a09a234a299295a0135f637df56e1fb72a150a51e`.
  Die generierte Datei bleibt wie vorgesehen ausserhalb der Versionierung.
- Der echte `ExecutionContexts.preflight` des Wartungsskripts besteht:
  Owner-Nachweis, Mounts, Benutzer, Werkzeugverfuegbarkeit und unveraenderliche
  kanonische Quellbindung sind gueltig. Die WSL-Sandbox ist fuer den
  begrenzten Wartungsauftrag betriebsbereit. Der Flottenlauf folgt separat.

The official release metadata confirms the retained amd64 checksum. The
static validator accepts the corrected mapping and rejects the old name in
an in-memory negative test. The actual repaired Linux-amd64 build completed
all 69 steps with exit 0 and produced the image ID above, including successful
Actionlint download, checksum and version verification.
Compose configuration and startup preview passed. The rootless container is
running as adedev with the stated hardening and mounts. A local runtime
mapping pairs Podman 6.1.2 with existing crun 1.30.1 after Ubuntu's crun 1.14.1
rejected the OCI format; no product default is changed. The complete toolchain
smoke test passed with executable examples for all eight listed runtimes;
all nine maintenance-tool probes also passed.
All five pre-commit checks pass, including secret scanning. Swift signature
verification reports a good signature from the pinned release key, while
warning that the key has since expired. This is not evidence of current key
approval; the version and key pins are unchanged.
The owner explicitly approved existing host Syft 1.49.0 for this SBOM run;
the image's 1.46.0 pin and global defaults remain unchanged.
Host Syft 1.49.0 generated the local CycloneDX artifact from the exact mounted
image, with exit 0 and no registry fallback; its path and SHA-256 are above.
The generated file remains unversioned. The maintenance execution-context
preflight passed its owner-evidence, mounts, user, tools and immutable-source
checks. The WSL sandbox is ready for the bounded maintenance task; fleet
maintenance itself remains a separate next step.

## Dokumentationsauswirkung / Documentation impact

`UpdateRequired`. Kanonische Quellen: Dockerfile, statischer Validator und
dieser Betriebsnachweis. Owner: Repository-Maintainer. Zielgruppe und
Leserpfad: Sandbox-Betreiber, Build-Fehleranalyse zur Sitzungs-Evidence.
Dokumentklasse: Betriebsnachweis, source-only; Deutsch/Englisch gemeinsam,
keine Navigations- oder CLI-Aenderung, kein Home-Sync fuer dieses Dokument.
Plattformnachweis: Linux amd64 unter WSL; keine neue native macOS-/Windows-
Abnahme. Re-Evaluation bei Architektur-, Release-Asset- oder Mount-Aenderung.
Andere Compliance-Aufgaben bleiben unveraendert und ausserhalb dieses
gezielten Wartungsauftrags. Naechster Schritt: autorisierte Lieferung und
Flottenwartung nach der abgeschlossenen WSL-Kompatibilitaetspruefung.

Decision: UpdateRequired. Canonical sources are the Dockerfile, validator and
this operational record; owner: repository maintainer. Readers are sandbox
operators tracing build failures to session evidence. This bilingual,
source-only record changes no navigation or CLI and needs no Home sync.
Evidence covers Linux amd64 on WSL, not new native macOS/Windows acceptance.
Reevaluate on architecture, asset or mount changes. Other compliance work
remains out of scope. Next: authorized delivery and fleet maintenance after
the completed WSL compatibility check.
