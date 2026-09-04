# WP10 Sichere Entwicklungsumgebung / Secure Development Environment

Die Inspektion umfasste Host-/IDE-Grenzen, Compose-Mappings, lokale Secrets,
CI-Reproduzierbarkeit, Testdaten, Backup, Scriptparitaet und Plattformen. /
Inspection covered host/IDE boundaries, Compose mappings, local secrets, CI
reproducibility, test data, backup, script parity, and platforms.

Repositorylokal vorhanden sind rootless-Podman-Anleitung, explizite Mounts,
read-only .NET-Konfiguration, getrennte State-Volumes, ignorierte lokale
Secretdatei, Secret-Scan, Smoke-Test und VS-Code-Dev-Container-Profil. RED fuer
die neue Hardening-Schnittstelle wurde durch Bash/PowerShell-Paritaet behoben.
Getrennte Windows-Host- und Ubuntu/WSL2-Evidenz sowie Plattformkontrollen
bleiben Open. Entscheidung `DEC-XPLAT-WSL2-2026-09-04` erlaubt dieselbe
physische Windows-Hardware, aber keine gemeinsame Podman-Laufzeit oder
wiederverwendete Evidenz. / Local controls exist; separate Windows-host and
Ubuntu/WSL2 evidence plus platform-admin controls remain open. The approved
decision permits shared hardware but not a shared runtime or reused evidence.

Human-only `GAP-120`, `121`, `124`, `128`–`131` stay Open. Mapping:
FR-006–FR-013, CP-001–CP-005, `GAP-117`–`GAP-133`.
