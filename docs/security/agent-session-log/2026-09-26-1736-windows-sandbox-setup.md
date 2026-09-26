# Windows-Sandbox-Einrichtung / Windows sandbox setup

## Deutsch

Expliziter Owner-Auftrag: fehlende Sandbox einrichten, danach 21 Secure-Trader-
Ziele aktualisieren und die UTF-8-Korrektur verteilen. Zusaetzlich genehmigt:
Korrektur veroeffentlichen, Image-Pin aktualisieren und alle zugehoerigen PRs
mit DeliveryMode MergeAndSync und Admin-Bypass liefern. Technische Fehler
werden dadurch nicht uebergangen.

P1-1: done fuer dieses Sitzungsprotokoll. P1-4: gesonderte Rollenfreigabe
weiterhin offen; bestehende Owner-Freigabe und Ablaufdatum bleiben erhalten.
P2-3: partial, Build und SBOM noch nicht abgeschlossen. Andere Compliance-
Aufgaben nicht bearbeitet, da ausserhalb des ausdruecklichen Auftrags.

Ausgangslage: Windows, laufende Podman-WSL-Maschine, keine Container, Images
oder benannten Volumes vorhanden. Konfiguration mit dem vorhandenen Compose-
Provider ueber Podman validiert. Nur lokale, ignorierte Dateien angelegt:
neutrale opencode.env ohne Zugangsdaten und .env mit den drei vorhandenen
Secure-Trader-Workspace-Zuordnungen. Keine Provider-Anmeldung oder Agenten-CLI
gestartet, keine globalen Vertrauens- oder Sicherheitsregeln geaendert.

Der erste Build mit altem Pin wurde gezielt beendet. Der zweite Build nutzt
den exakt veroeffentlichten UTF-8-Commit aus
[Home Baseline PR 310](https://github.com/hindermath/home-baseline/pull/310).
Lock-Validator und dessen nativer Python-Vertragstest bestanden. Der gezielte
Windows-UTF-8-Regressionstest in Home Baseline bestand ebenfalls. Dort meldet
CI zusaetzliche Drift in Statistikprofil und Skriptreferenz; deren gezielte
Regenerierung hat der Owner separat genehmigt.

Noch kein erfolgreicher Image-Build, keine SBOM, kein laufender Sandbox-
Container, keine bestandene Sandbox-Vorpruefung und keine Aenderung an den
21 Secure-Trader-Zielen nachgewiesen. Historische Freigabe-Evidence bleibt
unveraendert; der neue Pin ist ein Zielstand. Naechster Schritt: technische
Checks abschliessen, liefern, Build/SBOM und Container-Vorpruefung abnehmen;
erst danach die autorisierten Repository-Aenderungen ausfuehren.

Dokumentationsauswirkung: UpdateRequired. Owner: Workspace-/Sandbox-Maintainer.
Zielgruppe und Leserpfad: Wartungsoperatoren, Freigabe -> Sitzungsnachweis ->
naechste sichere Aktion. Kanonische Quellen: Lock-Datei, Compose-Konfiguration
und reale Pruefergebnisse. Dokumentklasse: bilinguale Betriebsevidence,
source-only; keine Home-Synchronisation. Re-Evaluation bei Buildabschluss,
Merge, Mount- oder Freigabeaenderung. Plattformnachweis nur Windows;
keine vollstaendige plattformuebergreifende Abnahme behauptet. Keine Grafik
erforderlich fuer diesen linearen Betriebsnachweis.

## English

The Owner authorized sandbox creation, subsequent updates to the 21 Secure
Trader targets and UTF-8 distribution, then explicitly authorized publication,
the image pin and MergeAndSync with admin bypass for this task's PRs. This
does not waive technical failures. P1-1 session evidence is complete; separate
P1-4 role approval remains open. P2-3 build/SBOM is partial; unrelated work is
out of scope. The Podman WSL machine runs but initially contained no images,
containers or named volumes. Compose validation passed. Local ignored files
contain only a neutral provider environment and the three workspace paths.
No credentials, agent sessions, global trust changes or new approvals.

The old-pin build was stopped; a new build uses the exact published UTF-8
commit. Lock validation, its native Python contract test and the targeted
Windows UTF-8 regression passed. Home Baseline CI reported generated-document
drift, whose targeted regeneration the Owner separately approved. Build,
SBOM, runtime preflight and changes to the 21 targets are not yet proven.
The new pin is a target, not activation evidence. Complete technical gates,
delivery and runtime verification before modifying the authorized targets.
Documentation impact: UpdateRequired, maintainer-owned operational source-only
evidence, German first/English second, no Home sync. Reevaluate after build,
merge, mount or approval changes. Windows-only evidence; no cross-platform
acceptance claimed.
