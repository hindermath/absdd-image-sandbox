# Gezielte Container-Reparatur / Targeted container recovery

## Deutsch

Expliziter Auftrag: Daten sichern und ausschließlich den beschädigten
Sandbox-Container ersetzen, alle Volumes erhalten.
P1-1: done für dieses Protokoll; P1-4 bleibt menschliche Freigabe, unverändert.
Andere Compliance-Aufgaben nicht bearbeitet; keine Freigabe fingiert.

Vorher: Container `58a38f937252` im Zustand Created, beschädigter Overlay-Layer.
Sicherung außerhalb des Repositorys in einem privaten lokalen Verzeichnis:
Container- und Volume-Metadaten, beschreibbare Container-Schicht sowie alle
sechs benannten Volumes. TAR-Lesbarkeit geprüft, SHA-256-Prüfsummen abgelegt.
Bind-Mount-Daten wurden nicht kopiert, verändert oder entfernt.

Nur den alten Container ohne Volume-Löschoption entfernt. Anschließend
`podman compose up -d --no-build ade` erfolgreich ausgeführt.
Neuer Container: `bdbf765955a4`, dasselbe Image `4c279f0c0f3a`.
Identität und Erstellungszeit aller sechs Volumes unverändert; alle Mounts
einschließlich Schreibrechten identisch. Benutzer adedev (UID 1655),
Arbeitsverzeichnis /rider-projects, lesender Mount-Zugriff erfolgreich.
`podman system check --quick` nach Reparatur erfolgreich.
Getrennte Folgeaufrufe bestätigen running, Neustartzähler 0.

Kein Image-Build, kein Storage-Reset, kein Prune, keine Konfigurationsänderung,
kein Commit/Push und keine Secure-Trader-Arbeit. VM und Container laufen weiter.
Der technische Laufnachweis ist keine formelle Sandbox-Freigabe und kein
Langzeitstabilitätstest. Sicherungen enthalten möglicherweise private
Agentendaten und bleiben lokal; nicht veröffentlichen.

## English

Authorized recovery: back up data and replace only the damaged container,
preserving every volume. P1-1 session evidence complete; human P1-4 approval
remains unchanged. Backed up metadata, writable container layer and all six
named volumes privately outside the repository; verified TAR readability and
recorded SHA-256 checksums. Bind-mount data remained untouched.
Removed only the old container, without volume deletion. Compose recreated
the service without building, using the same image. All volume identities,
creation times and mount permissions are preserved. The new container runs
as adedev, responds to read-only checks and retains restart count zero across
separate calls. The quick storage check now passes. No reset, prune, build,
configuration change, commit, push or Secure Trader work occurred.
VM and container remain running. This is bounded runtime evidence, not formal
sandbox approval or a long-term stability guarantee. Backups may contain private
agent data and must remain local.
