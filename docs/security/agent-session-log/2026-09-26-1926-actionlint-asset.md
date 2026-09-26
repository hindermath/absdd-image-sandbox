# actionlint-Asset-Korrektur / actionlint asset correction

## Auftrag und Grenze / Authority and boundary

Der Owner hat die Korrektur des actionlint-Dateinamens, den Abgleich der
Pruefsumme und die Fortsetzung des Image-Builds ausdruecklich freigegeben.
DeliveryMode bleibt MergeAndSync mit Admin-Bypass, ohne technische Fehler
oder Integritaetspruefungen zu umgehen. macOS ist die primaere Plattform;
Windows und Ubuntu unter WSL sind Kompatibilitaetstests.

The owner explicitly authorized correcting the actionlint asset name,
checking its checksum, and continuing the image build. Delivery remains
MergeAndSync with admin bypass, without bypassing technical failures or
integrity checks. macOS is primary; Windows and Ubuntu on WSL are
compatibility-test platforms.

## Ergebnis / Result

- Build-Korrektur: `linux_amd64` statt des nicht veroeffentlichten
  `linux_x86_64`; die entsprechende statische Prueferwartung wurde angepasst.
- actionlint 1.7.12: offizieller SHA-256 unveraendert und im Build bestanden;
  Versionsaufruf erfolgreich. Arm64 und alle anderen Versionen unveraendert.
- P2-3: partial. Alle 69 Image-Build-Schritte bestanden; die anschliessende
  CycloneDX-SBOM wird noch erzeugt.
- Swift: GPG meldet eine gute Signatur, aber einen inzwischen abgelaufenen
  Release-Schluessel. Kein Schluesselwechsel und keine Pruefungsumgehung.
- P1-4: keine neue formelle Rollenfreigabe; vorhandene Grenzen unveraendert.
- Andere Compliance-Aufgaben nicht ausgefuehrt: ausserhalb dieses Auftrags.

The corrected asset downloads and passes the existing SHA-256 and version
checks. The static checker now expects the published amd64 asset name.
Arm64, versions, privileges, mounts, provider configuration, and secrets
are unchanged. All 69 image-build steps passed; SBOM generation remains
pending. Swift GPG verification reports a good signature with an expired
release key; this warning is retained without changing verification.
No macOS build acceptance or formal human-role approval is claimed.

## Dokumentationsauswirkung / Documentation impact

`UpdateRequired`: diese source-only Sitzungsnotiz dokumentiert den engen
Build-Fix fuer Maintainer und Owner. Kanonische Quellen sind Dockerfile,
Pruefskript und die offiziellen actionlint-1.7.12-Release-Pruefsummen.
Navigation: bestehendes Sitzungslog-Verzeichnis; Sprachpartner inline.
Kein Home-Runtime-Sync. Re-Evaluation beim naechsten actionlint-Update.

This source-only maintainer/owner session record documents the bounded fix.
Canonical evidence is the Dockerfile, static checker, and official release
checksums. No Home Runtime sync; reevaluate on the next actionlint update.
