# Vierzehn Preset-Patches / Fourteen preset patches

Documentation Impact: `UpdateRequired`. Owner: @hindermath.

## Auftrag / Authority

DE: Begrenzter Rollout der bereits veroeffentlichten vierzehn README-Patches.
Zentrale Lieferung: [Home Baseline #335](https://github.com/hindermath/home-baseline/pull/335).
Unveraenderliche Versionen, Tag-Commits und ZIP-SHA-256:
[Quellen-Lock](preset-readme-patch-source-lock-2026-10-18.json).
Prioritaeten bleiben unveraendert; kein Home-only-Runner-Overlay wird kopiert.

EN: Bounded installation of fourteen published README patches after central
delivery. Preserve priorities and immutable package identities; do not import
the Home-only runner overlay. No community submission or wider fleet rollout.

## Technische Evidence / Technical evidence

DE: Die bisherige Installation wurde gegen ihre Tags verglichen: nur drei
erwartete abgeleitete Security-Commands, keine funktionalen lokalen Overlays.
Alle vierzehn Pakete sind mit dem zentralen Installer installiert. Die drei
Claude-Wrapper wurden aus der vollstaendigen vorhandenen Komposition erzeugt;
ein strenger Paritaetstest prueft alle sechs Wrapper auf allen fuenf Flaechen.
Aktuelle Guidance, ihre Vorlagen, Constitution-Spiegel und Profile folgen
derselben Versionierung. Historische Feldtests bleiben unveraendert.

EN: The pre-install audit found only three expected derived commands, no local
functional overlays. Install all fourteen packages through the central
installer. Regenerate Claude wrappers from complete composition and add strict
six-wrapper checks across five maintained surfaces. Preserve historical proof.

DE: Der neue, getrennte Assurance-Kontext
`sandbox-preset-patch-rollout` bindet die tatsaechliche Baseline; vier Gate-
Reviews pruefen ausschliesslich technische Dokumentidentitaet und Integritaet.
Menschliche Pilot-, Projekt- und allgemeine Freigaben bleiben Open.

EN: A distinct training context binds the actual baseline. Four separately
reviewed gates concern technical integrity only, not a new human acceptance,
risk decision, C5/conformity finding, certification or ReleaseAccepted decision.

## Container- und Liefergrenzen / Container and delivery boundaries

DE: Die bereits laufende Podman-VM bleibt erhalten. Vorhandenes Image
`localhost/absdd-image-sandbox_ade:latest` wird ohne Build/Pull gestartet.
Spec Kit im Container: 0.12.8; PowerShell: 7.6.4. Keine Image-, Compose-,
Mount-, Netzwerk-, Provider- oder Geheimnisaenderung. Kein Image-Release;
Build/SBOM-Neuerzeugung ist fuer diese reine Repository-Installation N/A.
Compose-Konfiguration und Repository-Pruefungen werden trotzdem ausgefuehrt.
Allgemeiner schreibender Home-Sync im Container bleibt gesperrt.

EN: Reuse the already running VM and existing image without build or pull.
Container versions are directly observed. No image, mount, network, provider
or credential changes; no image release. Image build/new SBOM is N/A, but
Compose and repository checks still apply. No writing container Home sync.

DE: Noch kein Commit/Push. Vollstaendiger Diff einschliesslich Sitzungsprotokoll
wird vorab mit SHA-256 zur ausdruecklichen menschlichen Sichtung vorgelegt.
Erst nach dieser Sichtung, allen technischen Gates und geklaerten Befunden
erfolgt die beauftragte exakte MergeAndSync-Lieferung mit Admin-Bypass.

EN: No commit/push yet. Present the full diff, session log and SHA-256 for
explicit human sighting first. Deliver only after approval, successful
technical checks and resolved findings. Pending checks are not passes.
