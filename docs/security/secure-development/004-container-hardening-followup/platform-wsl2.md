# Ubuntu/WSL2 / Ubuntu on WSL2

**Stand 2026-10-31: UPD-AMD64 Open/Blocked.** Eine getrennte Ubuntu/WSL2-
Umgebung mit Checkout im Linux-Dateisystem, Bash und PowerShell 7, UID
ungleich 0, eigenem rootless Podman, nativem `linux/amd64` Build/Runtime
und beobachtetem Remote-WSL-/Dev-Containers-Zugriff steht hier nicht bereit.
Es gibt daher keinen ausführbaren WSL2-Befehl, Exitcode, Testzeitpunkt,
Image-Digest oder Runtimebeobachtung für den Kandidaten. Der Windows-Podman-
Pfad darf nicht als WSL2-Nachweis kopiert werden.

Owner: Ubuntu/WSL2 Platform Review. Nächste Aktion: nach finalem Code-/
Katalogstand denselben eingefrorenen Git-Head samt Patch-/Imagebindung
in einer eigenen rootless WSL2-Umgebung testen und Befehle, Exits, Zeit,
UID, Architektur, Image-ID, Eingabehashes, IDE-Zugriff und Grenzen hier
eintragen. Frist: vor Ubuntu/WSL2-/AMD64-Unterstützungsclaim. Trigger:
Runner verfügbar, neuer Head, Image- oder Compose-Änderung.

## English

**Open/Blocked on 2026-10-31.** No separate Ubuntu/WSL2 rootless Podman
environment is available. No native `linux/amd64` build/runtime, non-root
UID check, or observed Remote-WSL/Dev Containers attach was run. The
Ubuntu/WSL2 Platform Review must test the same frozen revision independently
and record the commands, exits, time, UID, image identity, input hashes and
limits before an Ubuntu/WSL2 or AMD64 support claim. A Windows Podman result
cannot be reused as WSL2 evidence.
