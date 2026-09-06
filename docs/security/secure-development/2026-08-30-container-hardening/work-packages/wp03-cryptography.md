# WP03 Krypto-Mindestvorgaben / Minimum Cryptography

**RED-Inspektion:** Das Repository implementiert keine Produktkryptografie,
Passwortspeicherung, MAC-Funktion, Zufallszahlenerzeugung oder
Post-Quanten-Funktion. Anwendbar sind SHA-256-Integritaet, signierte/TLS-
Paketquellen und der Audit ihrer Nutzung. Der reproduzierte
`syft:latest`-Fallback und die ungepinnte Hostsuche fuer Grype/Trivy waren RED.
/ The repository implements no product cryptography. SHA-256 integrity,
signed/TLS package sources, and their audit apply. Movable Syft and unpinned
host scanner fallbacks were RED.

**GREEN/Folgearbeit:** Der Syft-Containerfallback wurde entfernt; nur das
image-integrierte Syft oder exakt Version `1.46.0` auf dem Host ist erlaubt.
Der Scannerpfad verwendet ausschliesslich das offizielle Grype-Image
`v0.117.0` mit Manifest-Digest
`sha256:ddf9e9f204049f3a4a0955ef70873cabab6a31432125ad4f20a490b54950a253`.
Quelle: `https://github.com/anchore/grype/pkgs/container/grype`. / The fallback
is removed and the scanner image is version-and-digest pinned.

`GAP-034` und `GAP-035` bleiben Human-only bei `Platform Owner/Admin`; keine
Schluesselaktion wurde ausgefuehrt. Produktkrypto-Gaps sind N/A mit Trigger
„eigene Krypto-, Secret-, Signatur- oder Authentifizierungsfunktion kommt in
Scope“. TLS-/Hash-/Audit-Punkte bleiben bis zum finalen Build-/Scan-Gate
FollowUp. / Key-management gaps remain human-only; product crypto is reasoned
N/A, while hash/TLS/audit items await final evidence.
