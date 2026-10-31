# Windows-Host / Windows host

**Stand 2026-10-31: UPD-AMD64 Open/Blocked.** Der Owner hat nur macOS ARM64
als verfügbare getrennte Testumgebung genannt. Ein Windows-Host mit
PowerShell 7, Podman Machine, nativem `linux/amd64`, eigenem Build/Runtime
und beobachtetem VS-Code-Zugriff steht hier nicht bereit. Daher gibt es
keinen Windows-Befehl, Exitcode, Testzeitpunkt, Image-Digest oder
Containerbeobachtung für den Feature-004-Kandidaten. macOS PowerShell ist
kein Windows-Nachweis.

Owner: Windows Platform Review. Nächste Aktion: nach finalem Code-/Katalogstand
denselben eingefrorenen Git-Head samt Patch-/Imagebindung auf einem echten
Windows-Host separat bauen, Default und optionalen Read-only-Pfad mit
synthetischen Daten prüfen, VS-Code-Attach beobachten und Befehle, Exits,
Zeit, Architektur, Image-ID, Eingabehashes und Grenzen hier eintragen.
Frist: vor Windows-/AMD64-Unterstützungsclaim. Trigger: Runner verfügbar,
neuer Head, Image- oder Compose-Änderung. Keine bestehende Lernruntime
als Testressource übernehmen.

## English

**Open/Blocked on 2026-10-31.** Only a separate macOS ARM64 environment is
available. No native Windows PowerShell 7, Podman Machine, `linux/amd64`
build/runtime or observed VS Code attach was run. The Windows Platform
Review must test the same frozen revision independently and record commands,
exits, time, image identity, input hashes and limitations before any
Windows/AMD64 support claim. macOS PowerShell is no substitute.
