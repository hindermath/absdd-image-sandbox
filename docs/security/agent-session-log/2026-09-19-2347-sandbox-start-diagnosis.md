# Sandbox-Startdiagnose / Sandbox startup diagnosis

## Deutsch

Auftrag: vorhandene Sandbox starten, Fortbestand prüfen und berichten.
P1-1: done für dieses Sitzungsprotokoll. P1-4: unverändert offen;
technischer Start ersetzt keine menschliche Sandbox-Freigabe.
Andere Compliance-Aufgaben nicht bearbeitet: Diagnoseauftrag ohne Härtungsänderung.

Statische Compose-Prüfung erfolgreich. Ein Start aus dem kurzlebigen
Werkzeugprozess meldete Erfolg; im nächsten Aufruf war die VM wieder gestoppt.
Der Start aus einer eigenständigen macOS-Terminal-Sitzung blieb dagegen über
mehrere getrennte Werkzeugaufrufe erhalten. VM und Podman-API antworteten ab
21:45:56 UTC. Dies stützt einen Prozesslebenszyklus-Effekt beim ersten Start,
beweist aber nicht den genauen Signal- oder Beendigungsmechanismus.

`podman compose up -d --no-build` scheiterte mit Exitcode 125:
Die beschreibbare Schicht des vorhandenen Containers verweist auf das fehlende
Overlay-Unterverzeichnis `/var/lib/containers/storage/overlay/diff`.
`podman system check --quick` bestätigt einen beschädigten Layer; keine
Reparaturoption verwendet. Containerstatus bleibt `Created`, Neustarts 0.
Der VM-Datenträger hat rund 31 GiB frei; akuter Platzmangel ist nicht belegt.

Keine Volumes, Images oder Container entfernt, keine Compose-/Mount-/Provider-
Konfiguration geändert. Kein Build, Commit, Push oder Secure-Trader-Lauf.
Nur dieses vorgeschriebene Sitzungsprotokoll hinzugefügt.
Nächster Schritt zur gesonderten Freigabe: Containerdaten sichern und den
beschädigten Container gezielt neu erzeugen; Image nur bei weiterem Befund
neu bauen. Kein pauschaler Storage-Reset oder Prune.

## English

Scope: start the existing sandbox, verify persistence and report. P1-1: done
for this session record; P1-4 human approval remains open. Other compliance
tasks were outside this diagnostic request.
Static Compose validation passed. VM startup from the short-lived tool process
reported success but did not survive the next call. Startup in a separate
macOS Terminal session persisted across independent calls with a working API.
This supports a process-lifecycle explanation, not proof of a specific signal.
The container still fails to start (exit 125): its writable overlay layer
references a missing lower directory. The read-only quick storage check
confirms damage; no repair option was used. State: Created, zero restarts;
about 31 GiB free in the VM. No volumes, images or containers removed; no
configuration changes, build, commit, push or Secure Trader execution.
Next, subject to separate approval: preserve container data and recreate the
affected container, rebuilding the image only if further evidence requires it.
Do not use broad storage reset or prune as a diagnostic shortcut.
