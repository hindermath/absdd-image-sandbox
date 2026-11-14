# Sandbox-Kandidat für Owner-Entscheidung / Sandbox candidate for owner decision

Status: Kandidat geprüft; exakte Owner-Freigabe am 14.11.2026 erteilt. Aktivierung ausstehend.

## Gegenstand / Subject

- Build-Kontext: `hindermath/absdd-image-sandbox` HEAD `09afaab7649c2d8233e8fe998d24f46b93149359`, aus `git archive` in einen isolierten temporären Kontext kopiert.
- Einzige Kontextabweichung: `home-baseline.lock.json` Commit-Pin `b232d5881f1d75092ddd9ecb345d210b4213732a` → `816efa2222f3d2054fb80ac945cea116e657b99a`.
- Kandidatenimage: `sha256:f7cade21c421c19ee7ecfcbb1f4a44870be87b3dc4d1a851417993b359f43df2` (`localhost/absdd-image-sandbox-approval:816efa22`), native `linux/arm64`, Profil `all`, Benutzer `adedev`/UID `1655`.
- Eingebettete Level-0-Revision: `816efa2222f3d2054fb80ac945cea116e657b99a`.
- Paketfingerabdruck der 172 gebundenen Textdateien: `40d302d05a0596a3593bad069a12d80755f77bc32ce30f049ed468059547e71f`.
- SBOM: `sboms/2026-11-14-localhost-absdd-image-sandbox-approval-816efa22-all-arm64-f7cade21c421.cdx.json`, CycloneDX 1.7, 34.285 Komponenten, SHA-256 `a336a527b6539141aefb9df3a53a765fc38206b65bc4abdd3993eedd126249ce`.
- Smoke: `smoke.log`, SHA-256 `3f1d842f63109e4e11e8aad1ae766fb8ad5cc90384a8eb023ff8588e71e0e9d7`, Exit 0; Toolchain und Dokumentation erfolgreich. Der absichtlich defekte lokale Link ist ein bestandener Negativtest.

## Technische Prüfung / Technical verification

Lock-Validator, Bash-Syntax, Compose-Konfiguration und ARM64-Build-Vorschau bestanden. Der vollständige Build mit `--pull` und SBOM-Erzeugung war erfolgreich. Ein isolierter Container ohne Projekt-Volumes und ohne Netzwerk bestätigte eingebettete Revision, Non-root-UID und exakte, für den Benutzer nicht beschreibbare Paketdateien. Vollständiger Toolchain-/Dokumentations-Smoke mit Capability-Drop und `no-new-privileges` bestanden. Der bisherige Container `absdd-image-sandbox_ade_1` läuft unverändert auf Image `12359cbf965adf99ac9118a8b11ba6e4019750abe818ca01f3da721110f8f7e9` und ist healthy. Seine sechs persistenten Volumes wurden nicht verändert oder gelöscht.

## Vorgesehener Umfang / Proposed scope

Owner-Freigabe ausschließlich für dieses exakte Kandidatenimage und den genannten Paketfingerabdruck zur Fast-forward-Wartung der 21 Secure-Trader-Repos in der freigegebenen Sandbox, gültig bis 31.12.2026. Keine Produktions-, Modell-, Provider-, Secret-, Daten- oder CISO/ISB/KIB-Freigabe. Vor Containerwechsel bleiben Metadaten-Auditexport, Sicherungsprüfung, Mount-/Security-Preflight und Vertragspublikation als technische Gates offen. Die bisherige allgemeine Freigabe für Image `12359cbf…` wird nicht auf dieses neue Image übertragen.

*Candidate checked, exact owner decision pending. Only the pinned image/package and bounded Secure Trader fast-forward maintenance are proposed. No production, model, provider, secret, data or organizational role approval is inferred. Activation and maintenance remain gated by audit backup, mounts/security checks and a published execution contract.*

P2-3: Kandidaten-Build und Smoke bestanden; Aktivierung offen. P1-4: konkrete neue Owner-Entscheidung und organisatorische Rollenfreigaben offen. Keine der 21 Secure-Trader-Arbeitskopien in dieser Sitzung geändert.

*P2-3: candidate build and smoke passed; activation open. P1-4: exact new owner decision and organizational role approvals remain open. None of the 21 Secure Trader working copies was changed in this session.*

## Owner-Entscheidung / Owner decision

Thorsten Hindermann antwortete auf die vollständige Kandidatenfrage mit Image-ID, Paket-SHA-256, 21 Ziel-Repos und Ablaufdatum: „Freigabe erteilt.“ Diese Entscheidung ist in Level-0 datiert dokumentiert. Der technische Containerwechsel und die 21 Fast-forwards sind weiterhin offen. / Thorsten explicitly approved the exact bounded candidate; activation and target fast-forwards remain pending.
