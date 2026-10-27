# Validation Guide: Geplante Prüfung / Planned Validation

DE: **Alle Befehle unten sind spätere Prüfanweisungen, hier nicht ausgeführt.**
Zuerst Tasks erstellen, Analyze und ausdrückliche Implementierungs-/Runtime-
Autorität einholen. Ein roter Test bestätigt den Fehler nur in isolierter
Fixture. Nie globale Maintenance, persönliche Agentenzustände oder den laufenden
Lerncontainer als Testfixture verwenden. Repo-Wurzel ist das aktuelle Checkout
der Sandbox, nicht Level-0 oder ein Produktrepo. Vor jeder Gruppe Quellen/
Revision und Schreibumfang bestätigen.
EN: **Commands below are future instructions, not executed results.** First
generate tasks, analyze readiness and obtain implementation/runtime authority.
Use isolated fixtures, never global maintenance, personal state or the live
learner service. Work from this sandbox checkout and verify input/write scope.

## Voraussetzungen / Prerequisites

DE: Host mit Git, Bash, Python 3 und PowerShell 7 (`-NoProfile`), jq,
podman-compose und geprüften vorhandenen Helfern. Coverage.py, Pester und
weitere Messwerkzeuge nur in gesondert freigegebener gepinnter Testumgebung;
kein automatischer Download beim Test. Versions-/Capabilityfehler als fehlende
Voraussetzung melden, keine Upgrades oder echte Anmeldung nachholen.
Für Runtime separat funktionierender nativer Podman, freier Platz, eigene
Wegwerf-Volumes und Image-ID. Anleitungen gelten erst nach Implementierung
der im [CLI-Vertrag](contracts/cli.md) markierten Erweiterungen.
EN: Require local tools and pinned isolated measurement dependencies. Do not
install them implicitly, upgrade software or sign in to make a check pass.
Runtime additionally requires authorized native Podman and disposable state.
Planned CLI extensions must exist before their commands can be used.

## Q1: Eingabefrische / Input Freshness

DE: Host, Bash aus Repo-Wurzel; kein Container nötig. Bestehende Validatoren
lesen Ziele, Quellen und Review. Erwartung: Exit 0, 67 aktuelle Quellen und
Ready-Reihenreview. Fehler: stoppen, Drift benennen; nicht eigenmächtig
Receipts erneuern. Auch Spec-/Plan-Hash und Clarifications beim Übergang zu
Tasks/Implementierung neu binden.
EN: Host Bash, repository root, no container. Expect current bindings and
review, exit 0. Stop/report drift rather than regenerate receipts silently;
bind current spec/plan hashes at subsequent phase boundaries.

```bash
bash .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh --receipt specs/intake-authoring-receipts/secure-development-container-hardening.json --repo .
bash .specify/presets/intake-review-governance/scripts/validate-intake-review-result.sh --result specs/intake-review-results/sandbox-development-lifecycle.json --repo .
```

DE: Gleichwertiger Receipt-Einstieg auf Host-PowerShell 7:
EN: Equivalent host PowerShell receipt entry:

```powershell
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.ps1 -Receipt specs/intake-authoring-receipts/secure-development-container-hardening.json -Repo .
pwsh -NoProfile -File .specify/presets/intake-review-governance/scripts/validate-intake-review-result.ps1 -Result specs/intake-review-results/sandbox-development-lifecycle.json -Repo .
```

## Q2: Isolierte Regressionen / Isolated Regressions

DE: Host-Bash; Tests müssen HOME, Binärpfade, Netz und Fake-Compose isolieren.
Kein `maintain-agentic-*` direkt auf dem echten Host ausführen. Die bestehenden
Tests gezielt um Retention, neuen Feature-Kontext und Read-only-Vertrag ergänzen.
Neue geplante Tests `test_audit_retention.py` und `test_hardening_followup.py`
werden erst später erstellt; deren Fehlen jetzt ist kein Ausführungsauftrag.
Erwartung: positive Fälle erfolgreich, negative Fälle weisen die konkret
erwartete Ablehnung nach. Unerwarteter Timeout bleibt Fehler, keine Erhöhung.
EN: Host Bash with isolated fixtures, never direct real maintenance. Extend
existing suites and later add the named new tests. Expected negative behavior
must be asserted, not ignored. An unexpected timeout remains a failure.

```bash
python3 -m unittest scripts.tests.test_audit_storage_metadata scripts.tests.test_audit_shutdown_fail_closed scripts.tests.test_agent_prompt_dispatchers scripts.tests.test_opencode_v2_policy
python3 -m unittest scripts.tests.test_toolchain_version_pins scripts.tests.test_container_architecture scripts.tests.test_home_baseline_reference_pin scripts.tests.test_specify_container_patch
python3 -m unittest scripts.tests.test_linux_maintenance_hardening scripts.tests.test_workspace_storage_maintenance scripts.tests.test_maintenance_execution_context
python3 -m unittest scripts.tests.test_secure_development_container_hardening scripts.tests.test_pre_push_secret_policy scripts.tests.test_gitleaks_swift_fingerprint
python3 -m unittest scripts.tests.test_audit_retention scripts.tests.test_hardening_followup
```

DE: Auf Windows dieselben Python-Testmodule, plattformspezifische Skips
sichtbar halten; gezielte native Reparse-/PWS-Fälle ergänzen. Testaufzeichnung
enthält echte Zahl ausgeführter/übersprungener Fälle, Interpreter und Exitcode.
REV-TEST-TIMING bleibt samt realem stderr-/Capability-/Pfadschwärzungs- und
Timeout-Test erhalten; direkte `/bin/sh`-Prozesse, keine Launcher-Kette.
EN: Windows uses the same modules plus native reparse/PowerShell cases; record
skips, actual test counts, interpreter and exits. Preserve deterministic and
real-process timing/integration checks without launcher chains or new budgets.

DE: Mindest-Retention-Fixtures: eingefrorener UTC-Tag, Datum -31/-30/-29,
heute und Zukunft, ungültiger Name, Schaltjahr/Monatswechsel, Datei mit anderem
mtime, Unterverzeichnis, Symlink/Reparse-Point, geänderter Pfad, Exportfehler,
Löschfehler und Down-Fehler. Erfolgreicher Export vor Entfernung; nie private
DB-Inhalte lesen. Normaler Stopp erhält alle sechs Volumes. Down-Argumente
mit Leerzeichen/Unicode/Optionszeichen bleiben unverändert.
EN: Cover boundary dates, calendar edges, filenames/mtime, links/path races,
phase failures and argument identity. Export precedes deletion; preserve
volumes and never read private database payloads.

## Q3: Statische Konfiguration und Vorschau / Static Configuration and Preview

DE: Host-Bash, keine laufende Machine erforderlich für config. Effektive
Konfiguration nicht in Logs drucken; lokale Pfade/Envwerte könnten privat
sein. Default, Baseline-Override und optionale Read-only-Variante getrennt
prüfen; optionalen Pfad durch eigenen öffentlichen/synthetischen Testcheckout
ersetzen. Geplante neue Datei/Flags erst nach Implementierung verwenden.
EN: Host Bash, no running machine for config. Suppress raw config values;
test default and optional overrides independently with a safe test checkout.
Only use newly planned files/options once implemented.

```bash
podman-compose config >/dev/null
HOME_BASELINE_DIR=/path/to/test-home-baseline-source podman-compose -f compose.yml -f compose.home-baseline.yml config >/dev/null
podman-compose -f compose.yml -f compose.read-only.yml config >/dev/null
bash scripts/compose-down-with-audit.sh --podman --dry-run
bash scripts/test-ade-sandbox-hardening.sh --feature-directory specs/004-container-hardening-followup --mode Static --dry-run
```

```powershell
pwsh -NoProfile -File scripts/compose-down-with-audit.ps1 -Engine podman -WhatIf
pwsh -NoProfile -File scripts/test-ade-sandbox-hardening.ps1 -FeatureDirectory specs/004-container-hardening-followup -Mode Static -WhatIf
```

DE: Erwartung: config Exit 0; Vorschauen zeigen geplante Schritte mit null
Schreib-/Runtimeaktionen und keinem als bestanden ausgegebenen Test. Fehlende
Option/Datei: erst Implementierungsstand prüfen, niemals unkontrolliert starten.
EN: Expect valid config and zero-action previews, not test success. Missing
extensions require checking implementation state, never a real fallback run.

## Q4: Coverage / Coverage

DE: Host-Bash, isolierte Testumgebung mit zuvor gebundener coverage.py-Version.
Die exakten Tests stammen aus Q2 plus den Fixture-Tests für den gesamten
[namentlichen Nenner](coverage-scope.md). `--source` allein ist kein vollständiger
Nenner: JSON nachträglich auf alle erwarteten Dateien/Quellhashes prüfen und
Subprozesse/Inline-Programme zuordnen. Messartefakte im temporären Verzeichnis,
nicht als aktuelle Freigabe ins Repo schreiben.
EN: Use a pre-bound isolated measurement environment and Q2 plus fixtures for
the complete named scope. Verify actual files/hashes and child/inline programs;
source configuration alone does not establish complete measurement.

```bash
measure_dir="$(mktemp -d "${TMPDIR:-/tmp}/ade004-coverage.XXXXXX")"
COVERAGE_FILE="$measure_dir/.coverage" python3 -m coverage run --branch --source=scripts,spec-kit -m unittest scripts.tests.test_linux_maintenance_hardening scripts.tests.test_agent_prompt_dispatchers scripts.tests.test_audit_storage_metadata scripts.tests.test_audit_shutdown_fail_closed scripts.tests.test_audit_retention scripts.tests.test_hardening_followup
COVERAGE_FILE="$measure_dir/.coverage" python3 -m coverage json -o "$measure_dir/python-coverage.json"
```

DE: Das ist ein messbarer Einstieg, nicht allein die Vollabnahme der 104
Dateien. Fixtures weiterer Helfer müssen im selben gebundenen Messkontext
ergänzt werden; Rohdaten zusammenführen ohne unterschiedliche Revisionen zu
mischen. Je Python-Modul mindestens 85 % Zweig-Outcomes; alle ungemessenen
Dateien/Grenzen explizit zeigen. Shell-/PS-Branchregister mit Fixture-/Trace-
Belegen separat berechnen, Pester-/Zeilenquote nie als Branchquote einsetzen.
Öffentliche Interfaces: reviewed vollständiger Katalog, mindestens 80 % mit
beiden ausgeführten Fallarten und 100 % aller geänderten Interfaces.
Temporäre Messdaten nach Befundsicherung gezielt entfernen.
EN: This is a starting measurement, not full acceptance. Add remaining fixture
groups and merge only same-input data. Require per-module branch thresholds,
show all unmeasured scope, and separately calculate source-bound shell/PS
decision outcomes. Interface thresholds require the complete reviewed catalog.

## Q5: Native Runtime-Abnahme / Native Runtime Acceptance

DE: **Nur mit gesonderter Runtime-Autorität.** Host-Bash auf Apple Silicon;
Machine nicht automatisch starten. Socket dynamisch aus vorhandener
Podman-Machine ermitteln, auf Sockettyp prüfen und lokal `CONTAINER_HOST`
setzen; `DOCKER_HOST` nur für kompatible API-Clients. Windows verwendet den
gemeldeten Pipe/Socket, Ubuntu/WSL2 primär direkten lokalen rootless Podman.
Keine konkreten Hostpfade committen. Vorher laufenden Container, Image und
Volumeinventar erfassen; im Nachweis private Mountpfade redigieren.
EN: Requires separate runtime authority. Discover the native endpoint without
starting machines or committing local paths. Inventory protected runtime/state
first; redact personal mount paths. Windows/WSL2 use their own runtimes.

DE: Eigener lokaler Image-Tag, Cache und `--pull`; dieser Build ersetzt keinen
Compose-Service. Unveränderliche Image-ID anschließend explizit prüfen:
EN: Build a separately tagged cached candidate, never replace the service;
then inspect its immutable identity.

```bash
candidate="localhost/ade004-review:local"
podman build --pull --platform linux/arm64 -t "$candidate" .
image_id="$(podman image inspect --format '{{.Id}}' "$candidate")"
podman image inspect --format '{{.Id}} {{.Os}}/{{.Architecture}}' "$image_id"
podman run --rm --pull=never --network=none --user adedev --entrypoint id "$image_id"
podman run --rm --pull=never --network=none --user adedev -e SMOKE_TEST_ROOT=/tmp/ade004-smoke --entrypoint bash "$image_id" -s < scripts/smoke-test-toolchains.sh
podman run --rm --pull=never --network=none --user adedev --entrypoint bash "$image_id" -s < scripts/smoke-test-documentation.sh
podman run --rm --pull=never --network=none --user adedev --entrypoint bash "$image_id" -s -- --json < scripts/smoke-test-toolchains.sh
```

DE: Offline-Sprach-Smokes brauchen vorab vorbereitete Paketquellen/Caches.
Fehlt etwas, Scope als Blocked dokumentieren; Netzwerk nicht still aktivieren.
Optional erlaubte Download-Smokes separat und synthetisch mit expliziter
Egress-Entscheidung. Smokes allein belegen keine Compose-Mounts/Cap-Drops:
dafür separat erzeugtes Wegwerf-Compose-Projekt mit synthetischen Mounts und
eigenen leeren Volumes aus der Default-/Read-only-Konfiguration, niemals die
produktiven `.env`-/persönlichen Volumenamen wiederverwenden. Dort Identität,
Rootless, /proc-Status, Schreiborte, Projekt-Smokes, localhost-Ports und
beobachteten Dev-Containers-Attach prüfen. Nachher nur Kandidatenressourcen
mit erfasstem Eigentum entfernen; kein system/volume prune.
EN: Offline smokes require prepared caches; missing prerequisites block rather
than silently enabling network. Direct image smokes do not prove Compose
isolation. Use a separate disposable Compose project with synthetic mounts
and unique empty volumes for that proof and observed editor attach. Clean
only inventoried candidate resources, never the live service or global storage.

DE: Windows-PowerShell7-Podman und Ubuntu-WSL2-Bash-rootless-Podman führen
denselben geprüften Head mit `linux/amd64` separat aus. In WSL2 Checkout im
Linux-Dateisystem, `id -u` ungleich 0 und `podman info` rootless; eigener
Build/Runtime und VS Code über Remote WSL/Dev Containers. Je Kontext exakte
argv, Zeit, Image-ID und Eingabehashes, kein Copy/Paste von Ergebnissen.
Mindestbeleg für begrenzten Handoff ist echter macOS/ARM64-Lauf; fehlende
Windows/WSL2-Befunde bleiben UPD-AMD64 Open/Blocked mit Nutzungsgrenze.
Swift-Signal-/Ubuntu-Poppler-Warnungen mit genauer Version reproduzieren,
Programmstart vs swift run vergleichen; keine Warnungsfilter/Runtimepatches.
EN: Windows and WSL2 repeat the reviewed head natively as separate AMD64
contexts, with Linux-filesystem checkout and verified rootless WSL2 runtime.
Record exact commands/inputs/images, never shared results. Real ARM64 proof
is the bounded handoff minimum; missing AMD64 stays restricted. Assess
exact-version warnings without filtering or patching away observations.

## Q6: SBOM und Schwachstellen / Supply Chain and Vulnerabilities

DE: Autorisierter Host-Bash nach Q5, nur eigenes finales Image; derselbe
Inhaltsstand wie Runtimebeleg. Skript benötigt gepinntes Syft aus Image oder
exakt passende Host-Version, keinen beweglichen Fallback. Erzeugt ignorierte
Artefakte, startet kurzlebige Scanner ohne persönliche Volumes. Der Syft-
Vollscan kann als root im Wegwerfcontainer laufen, nicht als Serviceidentität;
die Ausnahme und Grenzen dokumentieren. Scanner/DB-Netzzugriff separat
offenlegen. SBOM-Pfad explizit aus erfolgreicher Ausgabe übernehmen.
EN: Authorized host scan of the exact accepted candidate, with pinned Syft,
ignored outputs and no personal state. Explain disposable full-image root
scan separately from non-root service operation, including scanner/DB access.

```bash
bash scripts/build-and-sbom.sh --skip-build --image "$image_id" --platform linux/arm64
bash scripts/analyze-sbom.sh --file "sboms/<exact-created-file>.cdx.json" --scan --scanner grype --scan-output "sboms/ade004-grype.json"
```

DE: Erwartung: nichtleere CycloneDX-SBOM, Image-/Architektur-/Hashbindung,
Scanbericht mit Datum/DB. Platzhalter erst durch tatsächlichen Dateinamen
ersetzen. Scannerfehler/DB-Ausfall ist kein sauberer Scan. 0 Critical;
fixable High nur mit Fix oder konkreter begründeter VEX-/Open-Disposition
gemäß FR-007. Menschliche Rechte-/Provider-/A11Y-/Sandboxfreigabe separat.
EN: Require nonempty bound SBOM and dated scanner/database results. Substitute
the actual filename; scanner failure is not a clean result. Enforce the
clarified vulnerability policy without inventing human approvals.

## Q7: Assurance / Assurance

DE: Host aus Repo-Wurzel, datierter Kontext gemäß Plan erst nach echter
Evidence-Erzeugung; alle Gatewerte `development`. Prüfer schreiben keine
Quellen um. Existierende Assurance-Tests auf isolierte Metadatenmutationen
erweitern: falsche aktive Version/ID/Baseline, Duplikate, nur Fließtext oder
EN/DE-Abweichung trotz neu berechneter Hashes müssen abgelehnt werden.
EN: Validate the actual dated context without changing sources; test metadata
mutations in isolated fixtures, including refreshed hashes on wrong content.

```bash
bash .specify/presets/secure-development-assurance-governance/scripts/validate-secure-development-assurance.sh status docs/security/secure-development/2026-10-26-004-container-hardening-followup
```

```powershell
pwsh -NoProfile -File .specify/presets/secure-development-assurance-governance/scripts/validate-secure-development-assurance.ps1 -Action Status -EvidenceDirectory docs/security/secure-development/2026-10-26-004-container-hardening-followup
```

DE: Erwartung: gleiche fachliche Entscheidungen beider Varianten; positiver
Valide-JSON-Fall schließt Human-only/Open nicht. Ungültige aktive Metadaten
Exit 2 ohne Evidenceänderung. Ready ist bei offenen Pflichtpunkten unzulässig;
keine historischen Records passend machen, kein Contract-Constant neutralisieren.
EN: Require equivalent validation with invalid metadata rejected without
rewriting evidence. Valid JSON is no human approval; no Ready hiding Open.

## Q8: Dokumentation, Parität und Liefermenge / Documentation and Delivery Set

DE: Host-Bash; bestehende Text-/Paritätsregressionen, offline Links und
Whitespace. Lychee prüft lokale Links, nicht WCAG-Konformität oder Rechtslage.
Erwartung: keine inkonsistenten gemeinsamen Regeln, keine privaten Pfade in
Nachweisen. Abweichungen konkret berichten und atomar korrigieren.
EN: Host text/parity checks and offline links establish consistency only, not
accessibility/legal acceptance. Report actual deviations.

```bash
python3 scripts/tests/test_spec_kit_agent_surface_parity.py
python3 scripts/tests/test_learner_documentation_contract.py
lychee --offline --include-fragments --no-progress 'specs/004-container-hardening-followup/**/*.md'
git diff --check
```

DE: Vor späterem Commit den vollständigen ausdrücklich bestimmten Liefer-
satz stagen und `validate-autonomous-delivery-set.* --staged` mit exakt
derselben Liste prüfen, danach Pre-Commit/Gitleaks auf diesem Index. Neue
Dateien im pfaderhaltenden Snapshot mitscannen; nie `.env`, Auditdaten oder
persönliche Keynote-/Agentenzustände als vermeintlichen Testumfang scannen/
loggen oder ungefragt aufnehmen. Bei Scannerfehler stoppen, keine Ausnahmen
auf Verdacht. Dieser Guide erlaubt keinen Commit/Push und führt keinen aus.
EN: Later delivery requires exact staged inventory validation and staged
Pre-Commit/Gitleaks including new files in a path-preserving snapshot. Do not
scan/log private configuration/state as supposed test data or stage unrelated
files. Fail on scanner errors rather than invent exceptions. This guide grants
and performs no commit or push.

## Nachweisablage und Fehlerhilfe / Recording and Recovery

DE: Für jeden Lauf EvidenceRecord gemäß [Datenmodell](data-model.md), inklusive
Schreibscope/Skips/Restpunkten. Alle technischen Gates starten Not Assessed.
Nicht ausgeführt bleibt nicht ausgeführt. Menschlichen A11Y-/First-use-Review,
Datenschutz-/Lizenz-/Cloudentscheidungen und formale Freigaben separat einholen.
Nach erfolgreichem begrenztem technischen Handoff die nächste Selbstprüfung
nur mit eigener Startautorität beginnen. Kein Vollreview allein aus grünen
Hashes oder historischen CI-Läufen ableiten.
EN: Record actual runs, scope, skips and remaining issues. Gates begin Not
Assessed; unexecuted stays unexecuted. Obtain human reviews separately and
start downstream work only under its own authority. Green hashes or old CI
are not a full substantive review.
