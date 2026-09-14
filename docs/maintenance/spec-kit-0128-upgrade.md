# Spec Kit 0.12.8: Sandbox-Upgrade / Sandbox upgrade

## Umfang / Scope

Owner: Thorsten Hindermann. Beauftragt am 2026-09-14: ausschließlich Spec Kit
von 0.8.3 auf 0.12.8 anheben, einschließlich erforderlicher Kompatibilitaet.
Allgemeine Toolchain-Wartung bleibt ausgeschlossen. Bestehende Presets, Intakes,
Agentenkonten, Secrets und persistente Volumes bleiben unveraendert.

Owner: Thorsten Hindermann. The 2026-09-14 authorization covers only the
Spec Kit 0.8.3 to 0.12.8 upgrade and required compatibility work. No general
toolchain maintenance, preset rollout, feature run or account change.

## Quelle und Aenderung / Source and change

Der offizielle [Tag v0.12.8](https://github.com/github/spec-kit/releases/tag/v0.12.8)
loest auf Commit `464d57fe30c72e9a88d279cc49834539ec989c03` auf.
Der Dockerfile pinnt diesen Commit und prueft die installierte Paketversion.
Der bisherige Bind-Mount-Patch benoetigt eine neue Einfuegestelle, weil die
CLI ihre Kopierlogik in separate Module verschoben hat. Er wird vor deren
Import angewendet. Unbekannte Strukturen bleiben blockiert.

The official release tag resolves to the pinned commit. The build verifies
package metadata. The existing copy patch is inserted before the new CLI
imports its split-out modules. Unknown layouts remain blocked.

Die genehmigte Git-Vertrauensausnahme gilt nur fuer den geprueften Pilotmount
`/ade-dev-sandbox`, ausschliesslich pro Prozess mittels `GIT_CONFIG_COUNT`,
`GIT_CONFIG_KEY_0=safe.directory` und `GIT_CONFIG_VALUE_0=/ade-dev-sandbox`.
Kein `safe.directory=*`, keine globale oder ins Image eingebaute Ausnahme.

The approved trust exception is process-scoped to the verified pilot mount.
There is no wildcard, global Git configuration change or image-wide exception.

## Nachweise / Evidence

- Offizieller Tag und Release-Commit per GitHub-API verifiziert.
- Compose-Konfiguration: Exitcode 0.
- Vorheriger Patch mit 0.12.8: reproduzierbarer Build-Abbruch
  `import shutil not found`, Exitcode 1.
- Angepasster Patch: drei Tests unter Linux bestanden (alte Struktur,
  neue Struktur, unbekannte Struktur ohne Schreibzugriff); Exitcode 0.
  Positive Tests pruefen außerdem wiederholte Anwendung und Kopierinhalte.
- Alle fuenf Pre-commit-Hooks bestanden, einschließlich Secret-Scan.
- Image-Build mit `podman compose build --pull=always ade`: Exitcode 0,
  nativ Linux/arm64 auf Podman/macOS. Image-ID:
  `a33180f5cb18158d894792613479d5864e7a28c64d9308b6fbf7f724a36f4842`.
- Laufender Testcontainer: Benutzer `adedev`, `specify --version` liefert
  `specify 0.12.8`. Installierter Kopierpatch aktiv und hashgleich nach
  erneuter Anwendung; Exitcode 0.
- `bash scripts/smoke-test-toolchains.sh`: Exitcode 0; .NET, Java, Go, Rust,
  Python, PowerShell, Node.js und Swift samt `specify check` bestanden.
- Isolierter Host-Bind-Mount: `specify init <neues-verzeichnis>
  --integration opencode --script sh`, Security-Governance-Installation,
  `info`, `resolve`, Disable/Enable, Remove/Reinstall und `check`: Exitcode 0.
  Nur Testartefakte angelegt und anschließend entfernt; keine produktiven
  Preset-Installationen veraendert. Ein zuvor schon existierendes leeres
  Testverzeichnis wurde erwartungsgemaess abgelehnt; der erfolgreiche Lauf
  verwendete ein neues Unterverzeichnis, ohne Force-Ueberschreibung.
- Bestehende Agenten-/Preset-Paritaet: drei Tests bestanden; Exitcode 0.
- `actionlint .github/workflows/documentation-and-sandbox.yml`: Exitcode 0.
- CycloneDX-SBOM aus dem fertigen Image mit image-eigenem Syft 1.46.0
  erzeugt; Exitcode 0. Die erkannten `specify-cli`-Komponenten haben 0.12.8.
  Datei: `2026-09-14-localhost-absdd-statistics-pilot-spec-kit-0.12.8.cdx.json`.
  SHA-256: `8773e14ddce7ffded5eec035247ee565e87918bc97ea5a42c69478fe745fb230`.
- Zusaetzlicher `gitleaks dir`-Vollscan: Exitcode 1, ein Treffer am bereits
  unveraendert vorhandenen oeffentlichen Swift-Signierschluessel-Fingerprint
  in Dockerfile Zeile 157. Kein neu eingefuehrter Secret-Wert; zur menschlichen
  Sichtung dokumentiert, keine Allowlist und keine Scanregel geaendert.
- Native Windows-/WSL-Bind-Mount- und amd64-Image-Pruefung: nicht ausgefuehrt.

The rebuilt Linux/arm64 image and all listed runtime tests passed. The installed
version and active patch were verified, including repeated patch application.
The final-image SBOM identifies Spec Kit 0.12.8. A supplemental full-directory
scan flags the unchanged public Swift signing-key fingerprint; no scan rule
was changed or finding hidden. Native Windows/WSL and amd64 remain untested.

## Gebundene Quelldateien / Bound source files

| Datei / File | SHA-256 |
| --- | --- |
| Dockerfile | `ee7d02c58142459bc90234c444f4007545cf8b133415637ccbe01b6651dd5d54` |
| spec-kit/patch-specify-cli.py | `6766f0bcddaccde3930189ef6ae5a4a3e37f6074c28a154ba7b4bbd3956efbd1` |
| scripts/tests/test_specify_container_patch.py | `89956bea6969bfe6ab3cd3785901240cadf6790bfd9ccd3a2a04822569a40bac` |

Basiscommit: `eb97bf9`. Diese lokalen Inhaltsbindungen ersetzen keinen
spaeteren exakten PR-Head und keine menschliche Abnahme. Das alte Standardimage
bleibt erhalten; der neue Stand liegt vorerst unter einem separaten Test-Tag.

Base commit: `eb97bf9`. Local content hashes do not replace an exact PR head or
human acceptance. Preserve the old default image; the candidate has a separate
test tag until reviewed delivery.

## Dokumentationsauswirkung / Documentation impact

UpdateRequired. Quelle: Dockerfile und Patch; Owner: Thorsten Hindermann.
Zielgruppen: Lernende, Betreiber, Reviewer. Leserpfad: README -> dieses
Upgrade-Protokoll -> Dockerfile/Tests. README und Tool-Inventar werden gemeinsam
aktualisiert; historische 0.8.3-Nachweise bleiben erhalten. ActiveSemantic,
Deutsch zuerst/Englisch danach. Distribution: Sandbox-Image und Repo-Dokumente;
kein Home-Sync. Keine neue CLI-Oberflaeche oder Produkt-API. Wiedervorlage bei
Spec-Kit- oder Patch-Update. Manuelle B2-/Text-Lesbarkeit geprueft; keine
pauschale WCAG-, Zertifizierungs- oder Sicherheitsfreigabe.

UpdateRequired. Dockerfile and patch are canonical; Thorsten owns the record.
Learners, operators and reviewers follow README to this record and the source
or tests. Update README and inventory, preserve historical evidence. Bilingual
active documentation distributed with the sandbox; no Home sync or new API.
Reevaluate on CLI/patch changes. Text readability is reviewed; no blanket
accessibility, certification or security approval is asserted.

## Liefergrenze / Delivery boundary

Menschliche Diff-Pruefung vor Commit und Push bleibt offen. Danach folgen
Commit, regulaeres Statistik-Rendering, PR, Checks am exakten Head und die
autorisierte Lieferung. Der Statistik-Preset-Pilot ist ein separater Schritt.

Human diff review before commit and push remains open. Commit, regular legacy
statistics rendering, PR, exact-head checks and authorized delivery follow.
The statistics preset pilot is a separate next step.
