# Audit-Retention und Stopp / Audit retention and shutdown

**Stand:** 2026-10-31, Feature-004-Arbeitsstand. **Scope:** synthetische
Unit- und Fake-Compose-Prüfung; keine Live-Volumes oder echten Sitzungen
wurden geöffnet. Owner: Repository Maintainer; Reviewer: Security Review.

## Ablauf und Grenzen

1. Beide Host-Wrapper legen im kanonischen Auditbereich eine eigene exklusive
   Sperre und einen zufälligen Mountmarker an. Der Container muss genau
   diesen Marker unter `/audit` sehen. Fremde Sperren bleiben unangetastet.
2. Der Exporter erhält einen UTC-Tag und eine zufällige Run-ID. Er schreibt
   Metadaten in eine Tagesdatei und einen `audit-export-run`-Datensatz auch
   bei null erfassten Sitzungen. Der Record nennt `session_metadata_count=0`
   und `session_coverage=filesystem-metadata-only`; OpenCode-2-Datenbanken
   bleiben `session_coverage=not-exported`.
3. Der Host verlangt eine nichtleere reguläre Tagesdatei. Der Container
   verifiziert den aktuellen Run-Record mit der eigenen Run-ID, bevor er
   Retention ausführt. Exit 0 allein genügt nicht. Ein fehlender/falscher
   Mount, eine leere Datei oder ein alter Record blockieren `down`.
4. Der Retention-Kern friert einen UTC-Tag ein, wählt nur direkte reguläre
   `YYYY-MM-DD.jsonl`-Dateien **vor** Tag minus 29 und prüft Typ/Inode vor
   `unlink` erneut. Link, Unterordner, fremde Namen und jüngere Dateien
   werden nicht entfernt. Ein Teilfehler blockiert Down und nennt `removed=N`,
   soweit der Kern die Zahl kennt. Wiederanlauf erzeugt neue Sperre und Export;
   er behauptet kein Rollback.
5. Nur danach wird `compose down` mit erhaltenen Argumenten aufgerufen.
   Ohne explizite Volume-Option bleiben die sechs benannten Volumes erhalten.
   Der Entrypoint-Export ist nur eine Best-effort-Ergänzung und ersetzt diesen
   Pflichtpfad nicht. `sandbox-lifecycle` bietet Build/Up/Recreate, kein Down.

**Nachweis:** `scripts/tests/test_audit_retention.py` deckt feste Datumsgrenzen,
Schaltjahr, mtime, Namen, Links/Unterordner und partielle Löschung ab.
`test_audit_shutdown_fail_closed.py` nutzt nur Fake-Compose für beide Wrapper,
Fehler- und Erfolgspfade, Mount- und Record-Fehler, Lock, Vorschau,
Argumentweitergabe, Down-Exit und Wiederanlauf. `test_audit_storage_metadata.py`
prüft den Export ohne DB-/WAL-/SHM-/Prompt-/Antwortinhalt. Ein vertikaler
Fake-Compose-Fall hält künstliche Projekt- und Agentendateien über den Stopp
hinweg und löscht nur die alte Audit-Tagesdatei. Einzelne Quellen können nach
späteren Änderungen erneut prüfpflichtig werden; aktuelle Testausgänge sind
im Sessionlog festzuhalten.

**Restrisiko:** Ein anderer Prozess mit denselben Host-Rechten kann zwischen
Mount-/Dateiverifikation und Down Dateien oder Mountzustand ändern. Der
dirfd-/No-follow-Kern begrenzt die Retention im Linux-Container; er ist kein
allgemeiner Schutz gegen gleichberechtigte konkurrierende Schreiber oder
Host-Backup-Kopien. Der Parser erfasst nur Metadaten, keine vollständige
Sitzungsabdeckung; UPD-V2-AUDIT bleibt Open. Native macOS/Windows/WSL2-
Laufzeitannahmen sind getrennt zu belegen. Datenschutzfristen können durch
zuständigen Privacy Review abweichen.

## English

**2026-10-31 candidate, synthetic evidence only.** The wrappers acquire
their own audit-area lock, prove the container sees a fresh mount marker,
export current metadata with a run ID, verify a nonempty day file and matching
run record, retain exactly the newest 30 UTC day buckets, then call down.
Zero observed sessions are reported as zero, without claiming full OpenCode 2
session coverage or exporting database contents. Fake-Compose tests cover
failure, retry, preview, argument order and separate project/agent state.
Only direct old regular day files are selected. A partial deletion is reported
and blocks down; no rollback is claimed. Same-user concurrent changes,
backups, live runtime and privacy decisions remain outside this synthetic
proof. The entrypoint hook is best effort only.
