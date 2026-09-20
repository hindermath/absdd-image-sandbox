# Wartungs-Git-Vertrauen / Maintenance Git trust

## Auftrag und Grenze / Scope and boundary

Owner-Auftrag: reproduzierbares Git-Vertrauen für freigegebene Wartungsziele,
anschließend MergeAndSync mit Admin-Bypass. Der eingebettete Level-0-Pin
enthält prozessgebundene, exakte `safe.directory`-Freigaben. Keine globale
Git-Konfiguration wird geschrieben. Interaktive Git-Aufrufe sind nicht
zusätzlich freigegeben. Owner-Ablaufdatum und Mount-/Hashprüfungen bleiben
unverändert. Bestehende Volumes und Zugangsdaten bleiben erhalten.

*Owner request: reproducible trust for approved maintenance targets followed
by MergeAndSync with admin bypass. The embedded Level 0 pin supplies exact
process-scoped Git trust without global Git writes or added interactive
permissions. Approval expiry and mount/hash checks remain unchanged. Preserve
existing volumes and credentials.*

## Evidence und Planbezug / Evidence and plan mapping

P1-1: Sitzungsnachweis ergänzt (`done`). P1-4: keine neue menschliche
Freigabe behauptet; bestehende Owner-Freigabe bleibt maßgeblich.
P0-2/P2-3: exakter Quellpin; Image-Build, SBOM und Aktivierungsnachweise im
zugehörigen PR nachtragen. Übrige Compliance-Aufgaben sind unverändert.
Level 0: 25 gezielte Tests bestanden; 21 reale Ziele mit neuer Worker-Logik
und abgeschalteter Benutzer-/System-Git-Konfiguration bestanden. Reguläre
Aktivierung erst mit geprüftem Image und erneuter Vorprüfung.

*P1-1: session evidence added (done). P1-4: no new human approval claimed;
existing Owner approval remains authoritative. P0-2/P2-3: exact source pin;
record image build, SBOM and activation in the PR. Other compliance tasks
remain unchanged. Level 0 passed 25 focused tests and all 21 live targets with
new worker logic and user/system Git config disabled. Activate only with the
verified image and repeated preflight.*

## Dokumentationsauswirkung / Documentation impact

`UpdateRequired`; Owner: Sandbox-Maintainer; Zielgruppe: Wartungsoperatoren.
Leserpfad: Wartungsnachweis → gepinnte Level-0-Anleitung
`docs/maintenance/container-git-trust.md`. Kanonisch: `home-baseline.lock.json`
und die dort gebundenen Wartungsmodule. Deutsch zuerst/Englisch danach,
textorientierte Betriebsevidence; source-only, kein Home-Sync dieses Repos.
Image-Neubau erforderlich. Re-Evaluation bei Pin-/Mount-/Freigabeänderung.

Nachtrag: Der abschließende Pin `35e4350cba446db0f9a476f8a57720ac1052387e`
enthält zusätzlich die native Windows-Testfixture. Die Wartungslogik bleibt
gegenüber dem vorigen Pin unverändert; die Quellbindung umfasst auch Tests.

*Follow-up: the final pin also includes the native Windows test fixture.
Maintenance logic is unchanged; source bindings include tests as well.*

*UpdateRequired; Owner: sandbox maintainer; audience: maintenance operators.
Read the maintenance evidence and pinned Level 0 operating note at
`docs/maintenance/container-git-trust.md`. Canonical sources are the lock and
bound maintenance modules. German-first bilingual text evidence; source-only,
no Home sync for this repository. Rebuild the image; reevaluate on pin, mount
or approval changes.*
