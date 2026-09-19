# Secure-Trader-Wartungspaket / Secure Trader maintenance package

## Deutsch

Owner-Auftrag: Ablaufdatum 31.12.2026 eintragen und den begrenzten Rollout
starten. Datum in `../sandbox-freigabe.md` DE/EN ergänzt. Die separate
CISO-/ISB-/KIB-Rollenfreigabe bleibt offen; nicht als abgeschlossen dargestellt.
P1-1: done für dieses Protokoll. P1-4: partial, explizite Owner-Freigabe
mit Ablaufdatum dokumentiert. Andere Compliance-Aufgaben unverändert.

Ausführung ausschließlich im laufenden Container als adedev, ohne neue Mounts,
Provider-Credentials oder Home-Sync. Deterministische Paketinstallation durch
das vorhandene Propagationsskript; keine Spec-Kit-/KI-Feature-Läufe gestartet.
Quelle: veröffentlichter Level-0-Commit
`43d5959222b4d0f31390150fbcf06a80ea7235c3`.
Paketarchiv-SHA-256 auf Host und im Container identisch:
`2947d7d064200e77ff873dfe42b50e4f07a770b687da19de5932619b7296c722`.
Die eingebettete Level-0-Referenz blieb unverändert.

Alle 21 Ziele waren vor Beginn sauber: drei Level-1-Workspaces und jeweils
sechs Level-2-Sprachprojekte für CaseTracker, OrderDesk und ServiceHarvester.
Vorschau, Update und Check-only für alle Ziele erfolgreich: 404 Dateikopien
aktualisiert, anschließend null Paketabweichungen, keine übersprungenen Ziele.

Zusätzlicher Befund in SecureOrderDeskProjects: elf registrierte Befehle
fehlten im singulären OpenCode-Pfad. Nach Sicherung wurden nur diese Dateien
bytegleich dorthin verschoben und betroffene Integrationsmanifest-Pfade
angepasst. Vorhandene abweichende singuläre Inhalte wurden nicht überschrieben.
Übrige ältere Duplikate bleiben erhalten; keine vollständige Bereinigung
beider Verzeichnisse behauptet.

Abnahme: 63 Agenten-Paritätstests (drei je Ziel) und alle Diff-Prüfungen
bestanden. Zusätzlich 36 Linux-Hardening-/TUI-Wrapper-Tests im CSharp-
CaseTracker-Ziel erfolgreich. Kein vollständiger Produktbuild oder Remote-CI-
Nachweis. Container läuft weiter, Neustartzähler 0.

Documentation Impact: UpdateRequired. Owner: Thorsten Hindermann.
Quelle/Leserpfad: Sandbox-Freigabe und dieses Sitzungsprotokoll für Maintainer.
Source-only, DE/EN, kein Home-Sync. NIST SSDF/CWE Top 25: Paketintegrität,
lokaler Änderungsschutz und begrenzte Zielauswahl; keine Produktlogik geändert.
Alle Zieländerungen bleiben lokal uncommitted/unpushed. Remote-Closeout ist
ein getrennter Schritt. Detailprotokolle im Container unter
`/home/adedev/maintenance-rollout-20260919/logs`, lokal zusätzlich unter
`/tmp/secure-trader-rollout.ndbONG/logs`; temporäre Evidence vor Bereinigung sichern.

## English

Recorded the owner's explicit 2026-12-31 expiry and executed the bounded
maintenance rollout inside the running container as adedev. Separate formal
role approval remains open (P1-4 partial); P1-1 session evidence complete.
The package from commit `43d5959222b4d0f31390150fbcf06a80ea7235c3` was hash-verified
across transfer. No new mounts, credentials, embedded-reference update,
Home sync, Spec Kit feature or AI-agent run occurred.

All 21 initially clean repositories passed preview, update and final package
check: 404 file copies updated, zero remaining package drift and zero skipped
targets. Eleven missing OrderDesk workspace OpenCode commands were moved
byte-for-byte after backup; affected manifest paths were updated. Existing
singular contents and remaining older duplicates were preserved.
All 63 parity tests and whitespace checks passed; 36 additional Linux/TUI
wrapper tests passed in the CSharp CaseTracker target. This is not full product
build or remote CI evidence. Container remains running with zero restarts.
Documentation Impact: UpdateRequired; bilingual maintainer evidence, source-only,
no Home sync. Changes remain local and uncommitted/unpushed; remote delivery is
separate. Preserve temporary detailed logs before cleanup.
