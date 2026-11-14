# Sandbox-Kandidat für Level-0 a56d19ce / Sandbox candidate for Level 0 a56d19ce

Status: Kandidat technisch geprüft und am 15.11.2026 von Thorsten Hindermann exakt als Owner freigegeben; Containerwechsel ausstehend. / Candidate technically checked and exactly owner-approved; activation pending.

## Gegenstand / Subject

- Build-Kontext: `hindermath/absdd-image-sandbox` Commit `79274dcb26a64bba1f982cbdcd517dbc87456f9d`, per `git archive` isoliert; einzige Abweichung ist `home-baseline.lock.json` von `816efa2222f3d2054fb80ac945cea116e657b99a` auf `a56d19cea928edb8048589428828727b76c51d6f`.
- Kandidatenimage: `sha256:53830cee3164a5112067a3681095e7d26f58ce930f452c7f9114592b0e1edb49` (`localhost/absdd-image-sandbox-approval:a56d19ce`), native `linux/arm64`, Profil `all`, Benutzer `adedev`.
- Paketfingerabdruck: `37dee3bcbdb81874ba890110e7a7c4bcab0564e3d0a5f464ea5a62ec2f0ba3fd` für 172 gebundene Level-0-Dateien.
- CycloneDX-SBOM: 34.285 Komponenten; lokale Datei `sboms/2026-11-15-localhost-absdd-image-sandbox-approval-a56d19ce-all-arm64-53830cee3164.cdx.json`, SHA-256 `ffbc1217387f5abfc3c060b4177414f71db8e517bf4215f3a89466b4d025301a`.
- Offline-Smoke-Log: SHA-256 `c70ac1b6b158796f5f287a776c27e13c4269ed4957334da6c85b7210d3103115`, Exit 0. Der absichtlich defekte lokale Link ist ein bestandener Negativtest.

## Technische Prüfung / Technical verification

Lock-Validator, Architekturvorschau, nativer Build mit `--pull`, SBOM-Erzeugung und isolierte Offline-Quellprüfung bestanden. Die 172 Paketdateien waren für den Non-root-Benutzer nicht beschreibbar. Vollständiger Toolchain-/Dokumentations-Smoke ohne Netzwerk mit Capability-Drop und `no-new-privileges` bestanden. Compose-Konfiguration mit lokaler Portbelegung und neuem Image-Override ist statisch gültig; Audit-Stop wurde als Dry-run geprüft. Das bisherige Image `sha256:f7cade21c421c19ee7ecfcbb1f4a44870be87b3dc4d1a851417993b359f43df2` bleibt bis zum verifizierten Wechsel aktiv.

## Owner-Entscheidung und Grenzen / Owner decision and limits

Thorsten antwortete auf die vollständige Frage mit exakter Image-ID, Paketfingerabdruck, 21 Secure-Trader-Repos und Ablaufdatum 31.12.2026: „Ja, exakt dieses Image freigeben“. Der datierte Level-0-Nachweis bindet den Umfang. Die Entscheidung deckt nur Fast-forward-Wartung der drei Level-1- und 18 Level-2-Repositories, keine Produktions-, Modell-, Provider-, Secret- oder allgemeine Datenfreigabe. CISO-/ISB-/KIB-Rollen bleiben offen. Vor Aktivierung sind Auditexport, Volume-Sicherung, Mount-/Security-Preflight und Veröffentlichung des Vertrags erforderlich.

*Thorsten approved the exact image and package for bounded Secure Trader fast-forward maintenance through 31 December 2026. Formal organizational roles remain open. Activation still requires the published contract, verified audit export, backup, and exact container preflight.*
