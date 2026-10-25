# CI-Korrektur / CI Alignment

## Deutsch

Der Owner hat die gezielte CI-Korrekturrunde für PR #100 und anschließendes
MergeAndSync mit Admin-Bypass bei grünen technischen Checks genehmigt.
Keine Prüfanforderung wird abgeschaltet oder als menschliche Abnahme ausgegeben.

1. Der Windows-Required-Check meldet keinen Secretfund (`high=0`). Der danach
   ausgeführte Homogeneity Guardian scheitert an der veralteten ASCII-
   Projektstatistik. Lokales read-only PowerShell-JSON bestätigt ausschließlich
   `ASCII Statistics Profile 2 drift`. Nach dem Inhaltscommit wird der
   vorhandene Renderer bei unveränderter Konfiguration/Methodik verwendet;
   die generierte Statistik erhält einen getrennten Commit.
2. Der Statistik-Pilot darf die aktuelle Preset-Installation nicht gegen die
   historische 0.1.0-Receipt prüfen. Diese Receipt bleibt unverändert. In beiden
   isolierten Worktrees wird stattdessen der bestehende Integritätsgate-Test
   für die aktiven vollständigen Installations- und Release-Locks ausgeführt.
   Der aktuelle Statistik-Preset ist 0.1.3; sämtliche Payload-Dateien bleiben
   hashgebunden. Negative Fixtures müssen Payload-/Manifeständerungen ablehnen.
3. Der .NET-Setup-Schritt wird von der nicht verfügbaren Floating-Auflösung
   auf SDK 10.0.402 gepinnt, passend zur bereits geprüften MCR-Basis. Die
   [offiziellen Release-Metadaten](https://builds.dotnet.microsoft.com/dotnet/release-metadata/10.0/releases.json)
   nennen diese GA-Version; der dort benannte Linux-x64-SDK-Download wurde
   mit HTTP HEAD 200 geprüft. Keine Änderung am Dockerfile oder Image.

Beide Workflow-Vorstände und die bisherigen Intake-/Receipt-/Review-Artefakte
werden vor Bearbeitung erhalten. Die drei Intake-Texte, sechs Folgeprompts,
Intake-IDs und `Completed → Eligible → Blocked → Blocked` bleiben unverändert.
Neue Quellenbindungen und ein begrenztes unabhängiges Nachreview ersetzen
das vorherige Review für die geänderten Eingaben; kein neuer Produktlauf.

Kein Container-Build/-Neustart, keine globale Wartung, Secret-/Provider-
Konfiguration, Plattformregeländerung oder formale Freigabe. Der technische
Merge-Gate bleibt bestehen; Admin-Bypass ersetzt keine grünen Checks.

## English

The owner authorized bounded CI correction for PR #100 and subsequent
MergeAndSync with admin bypass only after green technical checks. Do not
disable requirements or interpret technical checks as human acceptance.

1. The Windows required job reports no secret finding (`high=0`). Its later
   Homogeneity Guardian fails because ASCII project statistics are stale.
   A local read-only PowerShell JSON run confirms only Profile 2 drift.
   Use the existing renderer after the content commit, with unchanged
   configuration/methodology, then commit generated statistics separately.
2. Preserve the historical 0.1.0 installation receipt. Both isolated pilot
   worktrees instead execute the existing integrity gate against current
   complete installed/release locks. The installed statistics preset is 0.1.3;
   all payload files remain hash-bound. Negative fixtures reject changed
   payloads and manifests.
3. Pin setup to published GA SDK 10.0.402, matching the verified MCR baseline,
   rather than the unavailable floating resolution. Official release metadata
   above names this version; its Linux-x64 download returned HTTP HEAD 200.
   No Dockerfile or image change.

Archive preimages and renew affected bindings. Preserve all three intake texts,
six prompts, identities and lifecycle: Completed, Eligible, Blocked, Blocked.
Independent bounded follow-up supersedes the prior review for changed inputs;
no new product run or execution authority. No build/restart, global maintenance,
secret/provider configuration, platform-rule change or formal approval.
Admin bypass never replaces green technical checks.
