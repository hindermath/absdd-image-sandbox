# Isolierte Feature-004-Tests / Isolated Feature 004 tests

## Deutsch

Diese Fixture beschreibt nur künstliche Testdaten. Testprozesse erhalten ein frisches temporäres Verzeichnis unter `/tmp` (Windows: das vom Testprozess gemeldete Temp-Verzeichnis) als `HOME`, Projektwurzel, Registry- und Ergebnisablage. Es darf keine persönliche `~/.config`, kein echtes Agentenvolume, kein `opencode.env`, kein Podman-Lerncontainer und kein gemountetes Projekt als Fixture verwendet werden. Jede Testdatei erhält einen eindeutigen Namen; nach dem Test wird nur das eigene temporäre Verzeichnis entfernt.

| Grenze | Testaufbau | Erwartung bei Fehlern |
| --- | --- | --- |
| HOME und Agentenzustand | Temporäres HOME mit künstlichen Metadaten, getrennten Agentenverzeichnissen und ohne echte Token | Kein Zugriff auf das echte HOME; fehlende Zustände bleiben `Open` oder führen zum vorgesehenen Fehler. |
| Projekt und Git | Eigenes temporäres Repository mit harmlosen Dateien, `.gitignore` und gegebenenfalls generierten Verzeichnissen | Symlink/Reparse-Point, fremder Pfad und ungeprüfter Makefile-Inhalt dürfen keinen Host-Effekt auslösen. |
| Registry und Konfiguration | Kleinste gültige JSON-Fixture plus gezielte Mutationen; nur temporäre Pfade | Unbekannte Kommandos, Pfade und fehlende Pflichtfelder werden abgelehnt; keine Anmeldung oder Modellwahl. |
| Compose | Testeigener Fake-Compose-Einstieg, der argv und Exitcode in seinem temporären Verzeichnis festhält | Vorschau ruft Compose nicht auf. Export-/Retention-Fehler verhindern `down`; der echte Compose-Dienst bleibt unberührt. |
| Audit | Künstlicher Audit-Mount mit ISO-Tagesdateien und eigenen Testvolumes | Keine echten Agentenlogs, DB-/WAL-/SHM-, Prompt-, Antwort- oder Credential-Inhalte lesen oder exportieren. |
| Netzwerk und Downloads | Lokale Stub-Antworten oder geschlossene Netzwerkgrenze, keine echten Paketquellen im Unit-Test | Ein fehlender Offline-Beleg bleibt fehlend; kein stiller Netzdownload zum Bestehen eines Tests. |

**Ausführungsort:** Host, jeweilige Test-Shell (`bash` oder `pwsh -NoProfile`) und Repository-Root. Voraussetzungen sind die im Test genannten vorhandenen Werkzeuge; ein Containerstart gehört nicht zur isolierten Prüfung. Erwartetes Ergebnis ist ein expliziter Pass/Fail mit temporärem Pfad und tatsächlichem Exitcode. Bei fehlendem Werkzeug oder einer gesperrten OS-Funktion den Fall als übersprungen/blocked mit Grund protokollieren, nicht einen Erfolg erfinden.

**Absolute Programme:** Ein PATH-Stub ersetzt nur unqualifizierte Aufrufe. Wenn Produktionscode `/usr/bin/...`, einen dynamisch aufgelösten absoluten Binärpfad oder einen Container-Befehl verwendet, muss der Test den Aufruf an der tatsächlichen Prozessgrenze isolieren (etwa per injizierbarem Runner oder einem eigenen Wegwerf-Container). Ein gefälschter PATH allein ist kein Beweis. Auch Vorschauprüfungen dürfen kein Makefile, Git-Hook, Installationsskript oder alternatives Registry-Kommando aus einem fremden Checkout ausführen.

**Native Plattformen:** macOS-Bash/PowerShell auf diesem Host belegen weder Windows-PowerShell noch Ubuntu/WSL2-rootless Podman. Echte Build-/Runtime-Abnahmen brauchen getrennte, ausdrücklich inventarisierte Kandidatenressourcen nach T058; die vorhandene Lernumgebung bleibt erhalten.

## English

Use a fresh temporary HOME, project, registry, audit directory and result directory with synthetic data only. Never use personal agent state, secrets, mounted learner projects or the live Podman service. Fake Compose records arguments and exits in its own temporary area; preview must not call it, and export or retention failure must prevent `down`. Unit tests use offline stubs and report unavailable tools or platform behavior honestly. A PATH stub does not replace an absolute executable: isolate that real process boundary or use an owned disposable container. Run tests from the repository root with the stated host shell and prerequisites, record the actual result and exit, and remove only test-owned temporary resources. macOS results do not prove Windows or Ubuntu/WSL2 behavior.

## Mac-A-Messkonfiguration / Mac-A measurement configuration

DE: `coverage-mac-a.ini` misst Zweige der zehn benannten Python-Dateien mit
explizitem `ADE_COVERAGE_REPO`, auch bei anderem Kindprozess-cwd. Es ersetzt
weder das 106-Dateien-Inventar noch Shell-/PowerShell-Outcomes oder native
Plattformbelege. Erst aktuelle Quellen/Review und die isolierte Messumgebung
pruefen; Rohdaten nicht aus verschiedenen Quellstaenden mischen.
[Aktueller Teilbericht und Reproduktion](../../../../docs/security/secure-development/004-container-hardening-followup/mac-a-coverage-2026-11-02.md)
beschreiben Versionen, tatsaechliche argv, Testumgebung und fehlende Belege.
Die 85-/80-%-Anforderungen bleiben unveraendert; kein globales Maintenance.

EN: The configuration measures the ten named Python files with explicit
ADE_COVERAGE_REPO across child working directories. It does not replace the
106-file inventory, shell outcomes or native platform evidence. Validate
current sources/review and an isolated tool environment first; never merge
different source contexts. The linked report supplies reproduction inputs,
commands, environment and limitations. Keep 85/80 unchanged; no global work.

## T041-T046: gezielte Fortsetzung / Targeted Continuation

DE: `test_feature004_delegation_coverage.py` und
`test_feature004_registry_coverage.py` blockieren echte Transport-/Installer-
Aufrufe. `test_feature004_wrapper_outcomes.py` startet native Host-Shells
gegen einen aufzeichnenden Fake-Python-Kern in eigener temporaerer Kopie.
Keine echte Wartung, kein Podman. Siehe
[Messbericht](../../../../docs/security/secure-development/004-container-hardening-followup/mac-a-coverage-continuation-2026-11-02.md).

EN: The delegation/registry tests intercept real transport/installation.
Wrapper tests run native host shells against a recording fake Python core in
an owned temporary copy. No real maintenance/Podman; the linked report keeps
partial adapter evidence separate from full branch/platform acceptance.
