# CLI-Vertrag / CLI Contract

DE: Geplanter Vertrag für bestehende öffentliche Bediengrenzen, keine neue
Netzwerk-API. Die folgenden Erweiterungen sind noch nicht implementiert.
EN: Planned changes to existing user-facing CLI boundaries, not a network API.
The extensions below are not implemented yet.

## Audit-Stopp / Audit Shutdown

| Grenze / Boundary | Bash | PowerShell 7 |
| --- | --- | --- |
| Einstieg / entry | `scripts/compose-down-with-audit.sh` | `scripts/compose-down-with-audit.ps1` |
| Cmdlet | N/A, Shell-Einstieg / shell entry | geplant `Stop-AdeSandboxWithAudit`, approved verb `Stop` |
| Engine | `--podman` oder `--podman-compose` | `-Engine podman` oder `-Engine podman-compose` |
| Vorschau / preview | neu `--dry-run` | neu `-WhatIf` mit SupportsShouldProcess |
| Hilfe / help | `--help`, `-h`; `docs/man/stop-ade-sandbox-with-audit.1` | bilinguale comment-based help, DE zuerst / German first |

DE: Erhalt: bisherige Engineauswahl, Reihenfolge und argv der erlaubten
Compose-Down-Argumente; keine Rekonstruktion über Shellstring. Vorschau wird
vom Wrapper konsumiert und nie an Compose weitergereicht. Sie beschreibt
Export, festen UTC-Cutoff, Zielpfad und Down, ohne Export/Audit- oder Agenten-
Payloadzugriff/Schreibzugriff/Containeraktion. Notwendige Konfiguration darf
nur lesend ausgewertet werden; Vorschau erwirbt keine Ausführungssperre.
Explizite Volume-Löschung bleibt gesonderte
menschlich bestätigte Operation; kein normaler Beispielbefehl enthält -v.
Ungültige Eingaben sind Fehler, kein stiller Fallback.
EN: Preserve engine choice and allowed down-argument order/identity without
shell-string reconstruction. Consume preview flags locally; preview describes
operations without export, audit/agent payload reads, writes or container actions.
Necessary configuration may be read; preview acquires no execution lock.
Volume deletion remains separately human-confirmed and is never a normal
shutdown example. Invalid inputs fail rather than silently falling back.

DE: Reale Ausführung serialisiert Wrapper desselben kanonischen Auditbereichs
mit exklusiver eigener Sperre vor Export. Paralleler Lauf/unklare Altsperre:
nonzero, keine Aktionen; nur der Sperrbesitzer gibt frei, keine automatische
Stale-Lock-Reparatur. Exporterfolg erfordert Exit 0 plus aktuelle zugeordnete
reguläre nichtleere Tagesdatei. Null Sitzungen braucht wahrheitsgemäße
Metadaten-/Leerbestandsaussage, keine erfundene Session. Fehlende/leere Datei
oder Mountabweichung verhindert Retention und Down.
EN: Serialize actual runs with an owned exclusive lock per canonical audit
scope before export. Concurrent/ambiguous stale locks fail without actions;
only the owner releases its lock, never automatic stale repair. Export needs
exit 0 and a current attributable regular nonempty day file. Zero sessions
needs honest metadata/no-data evidence, not invented sessions. Missing/empty
or wrong-mount exports prevent retention and down.

DE: Ablauf: exportiert das laufende Ziel erfolgreich → verifiziert effektiven
Audit-Mount → löscht ausschließlich nach ISO-Dateidatum strikt ältere direkte
reguläre Tagesdateien → führt Down aus. Fehler vor Down verhindern Down.
Aufbewahrung ist 30 Tage mit einmaligem UTC-Tagesbezug; exakt 30 Tage bleiben.
Aktuelle Exportdatei, jüngere Dateien und alle Datenvolumes bleiben erhalten.
Nach erfolgreicher Vorprüfung reicht der Wrapper den echten Down-Exitcode
unverändert durch. Fehler bei Export/Löschung/Pfad/Argumenten bleiben nonzero
mit eindeutiger redigierter Phase, keine Ausgabe privater Pfade/Inhalte.
EN: Successful export precedes audit-mount validation, safe date-based retention
and down. Any prior failure prevents down. Retain exact-30-day/today/newer
files and all data volumes. Preserve down's actual exit status; prior errors
are nonzero with phase-specific redacted diagnostics.

DE: Teilfehler rollen frühere Metadatenlöschungen nicht zurück. Bereits
entfernten Umfang redigiert melden, übrige Daten erhalten, kein Down.
Neuer Lauf braucht eigene Sperre/erneuten Export und behandelt verbliebene
zulässige Dateien idempotent; Pfad-/Dateitypwechsel verhindern Entfernung.
EN: Partial failure does not roll back prior metadata deletion. Report actual
scope, retain remaining data and skip down. Retry requires its own lock and
fresh export with idempotent remaining-file handling; reject path/type drift.

## Hardening-Prüfung / Hardening Validation

DE: Bestehendes Paar `scripts/test-ade-sandbox-hardening.sh` / `.ps1` und
Cmdlet `Test-AdeSandboxHardening` wiederverwenden. Neu geplant:
`--feature-directory specs/004-container-hardening-followup` beziehungsweise
`-FeatureDirectory specs/004-container-hardening-followup`.
`--mode`/`-Mode` und vorhandene Input/Static/Runtime/SupplyChain/Documentation/
Accessibility/All-Modi bleiben bestehen. Ohne neuen Parameter bleibt das
historische Verhalten erhalten; mit Parameter nur Feature-004-Gates, nie
stille Rückkehr zu alten Evidencepfaden. `--dry-run`/`-WhatIf` schreibt und
führt keine Tests aus. man-Page `docs/man/test-ade-sandbox-hardening.1`
und bilinguale PowerShell-Hilfe gemeinsam aktualisieren.
EN: Reuse the paired hardening entrypoints/approved Test cmdlet, adding explicit
feature directory selection. Preserve existing mode vocabulary and legacy
default; explicit Feature 004 never silently uses Feature 003 evidence.
Preview executes no tests and writes nothing; synchronize existing help/man.

DE: Bestehende Exitklassen: 0 verlangter Umfang wirklich belegt; 1 geprüfte
Anforderung fehlgeschlagen; 2 Argument-/Schema-/Pfadfehler; 3 erforderliche
Plattform, Tool oder menschlicher Nachweis nicht verfügbar. Dry-run-Exit 0
bestätigt nur Vorschau, nicht einen Test. Für All ist 0 bei fehlenden
Plattformen oder Pflichtnachweisen unzulässig, auch wenn ein begrenzter
ARM64-Handoff separat möglich bleibt. Fehlende neue Gate-Datei ist Fehler,
nicht Erlaubnis zur Erzeugung einer Erfolgsvorlage.
EN: Keep exit classes: 0 requested scope actually evidenced, 1 failed check,
2 argument/schema/path error, 3 unavailable platform/tool/human proof. Preview
success is not a test pass. All cannot return success for missing mandatory
scope, even if bounded ARM64 handoff is separately permitted. Missing gate
input is an error, never a generated success template.

## Vertragsfälle / Contract Cases

DE: Beide Skriptpaare müssen gleiche Fallmatrizen bestehen: Leerzeichen,
Unicode, führende Optionszeichen, Argumentreihenfolge, unbekannte Optionen,
leere Engine-/Dateipfade, fehlende Programme, Export-/Retention-/Down-Fehler,
Symlink/Reparse-Point, Pfadwechsel und Vorschau ohne Nebeneffekte. Native
Windows-Ausführung und Bash auf macOS/Linux mindestens je Variante; fehlende
Plattform dokumentieren, nicht aus PowerShell auf macOS ableiten.
EN: Both pairs share cases for whitespace/Unicode/option-shaped values,
argument order, bad inputs, missing programs, phase failures, path/link races
and zero-write preview. Native Windows and macOS/Linux Bash need separate
observations; macOS PowerShell is not Windows proof.
