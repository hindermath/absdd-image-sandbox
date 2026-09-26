# Windows-Mount-Referenz / Windows mount reference

## Deutsch

Der Owner genehmigte die gezielte Windows-Pfadkorrektur und Fortsetzung der
Windows-Flotte sowie Veroeffentlichung und Image-Pin mit MergeAndSync und
Admin-Bypass. Technische Gates bleiben verbindlich. macOS ist primaer;
Windows und Ubuntu/WSL dienen der Kompatibilitaetspruefung.

Der neue exakte Home-Baseline-Pin enthaelt die unveraenderte UTF-8-Korrektur,
den neueren Hauptstand und den begrenzten Windows-Podman-Mountvergleich.
Nur die exakte Uebersetzung nach `/mnt/<laufwerk>/...` wird ergaenzt;
Container-, Benutzer-, Mountmodus-, Ablauf- und Quellhashpruefungen bleiben.
Windows-Regressionssuite: 25 bestanden, 4 plattformspezifisch uebersprungen.
Linux-Container: 28 bestanden, 1 Windows-Test uebersprungen. Die Linux-Pruefung
lief mit read-only Quellmount, ohne Netzwerk und ohne veroeffentlichte Ports.
Ein vorangehender Podman-SSH-Abbruch erforderte einen identischen Wiederholungsversuch.

Der vorherige Windows-Container startete erfolgreich ohne Portfreigaben.
Die verwaiste Sperre wurde wiederherstellbar maschinenlokal archiviert.
Die separate native WSL-Sandbox und ihre Arbeitskopien bleiben unveraendert.
P1-1: Sitzungsnachweis; P1-4: keine neue Rollenfreigabe; P2-3: neuer Build,
SBOM und Aktivierung noch offen. Keine Secrets oder Provider geaendert,
keine Agenten-CLI gestartet, keine Volumes geloescht, kein Quellhash-Bypass.

Dokumentationsauswirkung: UpdateRequired. Owner: Sandbox-Maintainer.
Quelle: Lock-Datei und reale Testergebnisse; Zielgruppe: Wartungsoperatoren;
Leserpfad: Freigabe, Sitzungslog, Build/SBOM. Bilinguale source-only Evidence,
keine Home-Synchronisation aus diesem Repository. Re-Evaluation nach Build,
Aktivierung oder Mountvertragsaenderung. Kein nativer macOS-Pass behauptet.

## English

The owner approved the bounded Windows mount correction, continued Windows
fleet maintenance, publication and image pin under MergeAndSync with admin
bypass, without waiving technical gates. macOS remains primary.

The exact pin includes the UTF-8 correction, newer main and strict Windows
Podman mount translation. Existing identity, user, mount, expiry and source
hash gates remain. Windows: 25 tests passed, 4 platform skips; isolated Linux
container: 28 passed, 1 Windows skip. A transient Podman SSH failure was retried
without configuration changes. Build, SBOM and activation for this pin remain
pending; separate role approvals are not granted by this record.

The previous Windows container started without published ports and its stale
maintenance lock was recoverably archived. The native WSL sandbox is untouched.
No secrets, providers, agent sessions, volume deletion or hash bypass.
Documentation impact is UpdateRequired: maintainer-owned bilingual source-only
operational evidence, reevaluated after build, activation or mount changes.
No Home sync from this repository and no native macOS acceptance claimed.
