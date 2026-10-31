# Stop-AdeSandboxWithAudit(1)

## Name

`Stop-AdeSandboxWithAudit` – ADE nach geprüftem Metadaten-Audit stoppen.

## Aufruf

Auf dem Host in PowerShell 7 und im Repository mit konfiguriertem Podman
Compose Provider:

```powershell
. ./scripts/compose-down-with-audit.ps1
Stop-AdeSandboxWithAudit -Engine podman -WhatIf
Stop-AdeSandboxWithAudit -Engine podman
```

Oder direkt `pwsh -NoProfile -File scripts/compose-down-with-audit.ps1
-Engine podman`. `-DryRun` und `-WhatIf` zeigen die Phasen ohne Mountprüfung,
Export, Sperre, Retention oder Down. Ein erfolgreicher echter Lauf prüft den
Host-Audit-Mount, einen aktuellen nichtleeren Export, behält 30 UTC-Tage und
führt dann `compose down` aus. Die sechs benannten Volumes bleiben bei
normalem Aufruf erhalten. `-Volumes` löscht sie und ist nur für eine eigene,
ausdrückliche Datenverlustentscheidung gedacht. `-RemoveOrphans` und
`-DownArgs` reichen zusätzliche Down-Optionen geordnet weiter.

Bei Fehlern vor Down bleibt die Umgebung laufen. Ursache und Phase stehen
in der Fehlermeldung; bei Retention wird die Zahl bereits entfernter Dateien
angegeben, soweit ermittelbar. Prüfe Auditverzeichnis/Compose-Mount und
wiederhole den Wrapper für einen neuen Export. Entferne keine fremde Sperre
automatisch. Bei `removed=unknown` lässt sich der Umfang nicht belegen.
Die Prüfung schließt gleichzeitige Änderungen durch denselben Hostbenutzer
zwischen Verifikation und Down nicht vollständig aus.

## English

Run the commands above on the host in PowerShell 7 from the repository with
a configured Podman Compose provider. `-DryRun` and `-WhatIf` show the plan
without a mount check, export, lock, retention, or down. A real successful
run checks the audit mount and current nonempty export, keeps 30 UTC days,
then calls `compose down`. Normal use preserves all six named volumes.
`-Volumes` deletes them and requires a separate data-loss decision.
`-RemoveOrphans` and `-DownArgs` pass ordered additional down options.

On failure before down, the environment stays running. Inspect the reported
phase and audit mount, then retry the wrapper for a new export. Never
automatically remove a foreign lock. `removed=unknown` means the deletion
count could not be established. A same-user concurrent change between
verification and down is still possible.
