# UPDATE-TOOLCHAIN-PINS(1)

## NAME

update-toolchain-pins — Hersteller-Pins pruefen / inspect official toolchain pins

## SYNOPSIS

```text
bash scripts/update-toolchain-pins.sh [--action Check|Prepare|Verify|Apply]
  [--repo PATH] [--output-directory NEW_EXTERNAL_PATH]
  [--payload-directory EXTERNAL_PATH] [--json] [--dry-run]
pwsh -NoProfile -File scripts/update-toolchain-pins.ps1
  [-Action Check|Prepare|Verify|Apply] [-Repo PATH]
  [-OutputDirectory NEW_EXTERNAL_PATH] [-PayloadDirectory EXTERNAL_PATH]
  [-SkipGroups GROUP,...] [-Json] [-WhatIf]
```

## DESCRIPTION / BESCHREIBUNG

DE: Erfordert PowerShell7. Check liest feste Quellen ohne Repository-Aenderung.
Prepare verlangt einen sauberen Commit und ein neues externes Verzeichnis.
Verify prueft offline Quell-HEAD, Hash und erlaubte Aenderungen. Apply ersetzt
nur das verifizierte Dockerfile atomar. Symlinks, Downgrades, unvollstaendige
Hashes und fremde Aenderungen werden abgewiesen. Kein Containerstart, keine
Installation, kein Push. Vor echtem Apply --dry-run bzw. -WhatIf verwenden.

EN: Requires PowerShell7. Check reads fixed sources without repository writes.
Prepare requires a clean commit and new external directory. Verify checks
source HEAD, hash and permitted changes offline. Apply atomically replaces
only the verified Dockerfile. Symlinks, downgrades, incomplete hashes and
unrelated changes are rejected. No container start, installation or push.
Preview with --dry-run/-WhatIf before applying.

## EXAMPLES / BEISPIELE

```bash
bash scripts/update-toolchain-pins.sh --help
bash scripts/update-toolchain-pins.sh --action Check --json
bash scripts/update-toolchain-pins.sh --action Prepare --output-directory /private/tmp/new-pin-payload
bash scripts/update-toolchain-pins.sh --action Verify --payload-directory /private/tmp/new-pin-payload
bash scripts/update-toolchain-pins.sh --action Apply --payload-directory /private/tmp/new-pin-payload --dry-run
```

DE: Windows verwendet einen neuen externen lokalen Pfad. SkipGroups ist die
PowerShell-Schnittstelle fuer Gruppen mit bereits offenem PR.

EN: Windows uses a new external local path. SkipGroups is the PowerShell
interface for groups that already have an open PR.

## EXIT STATUS / EXITCODES

0: erfolgreich / successful; 1: Quelle blockiert / blocked source;
2: Eingabe-/Vertragsfehler / input/contract error.

## FILES / DATEIEN

Dockerfile: kanonische Werte / canonical values.
scripts/config/toolchain-pins.json: Quellen/Grenzen / sources/boundaries.
Externe Payload / external payload: Dockerfile, proposal.json, report.json.

## SEE ALSO / SIEHE AUCH

[Update-Policy](../security/dependency-update-policy.md),
[Dependabot-Wartung](../../.github/DEPENDENCY-MAINTENANCE.md).
