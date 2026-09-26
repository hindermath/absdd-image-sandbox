# Ubuntu-Pakettransport / Ubuntu package transport

## Deutsch

Der Owner genehmigte ausdruecklich, ausschliesslich die Ubuntu-Paketquellen
im Dockerfile auf HTTPS umzustellen und danach Build und Ausfuehrung
fortzusetzen. MergeAndSync mit Admin-Bypass gilt weiterhin fuer die PRs dieses
Auftrags, nicht als Befreiung von technischen Fehlern.

Belegter Ausgangsfehler: Build-Schritt 25 endete mit Exitcode 100, weil die
Ubuntu-HTTP-Quellen im Container nicht erreichbar waren. Ein begrenzter
Vergleich mit demselben Basisimage ergab HTTP-Verbindungsfehler, aber HTTPS
200 OK. Aus der Podman-VM waren beide Protokolle erreichbar.

Die Korrektur ersetzt nur die drei offiziellen Ubuntu-HTTP-URL-Praefixe in
der vorhandenen Deb822-Quelldatei durch HTTPS. Repository-Pfade, Versionen,
Schluessel, Signaturpruefung und Sandbox-Grenzen bleiben unveraendert.
NIST SSDF und CWE Top 25: keine neue Eingabeauswertung oder Vertrauensquelle;
TLS-Pruefung bleibt aktiv. Kein Host-Netzwerkumbau und kein Versionsupgrade.

P1-1: done fuer diesen Nachweis. P2-3: partial, erneuter Build/SBOM gestartet;
Runtime-Abnahme und die 21 Zielupdates noch nicht abgeschlossen. P1-4 und
alle nicht beauftragten Compliance-Punkte bleiben unveraendert.

Dokumentationsauswirkung: UpdateRequired, diese bilinguale Betriebsevidence.
Owner: Sandbox-Maintainer. Leserpfad: Buildfehler -> eng begrenzte Korrektur
-> erneuter Build. Quelle: Dockerfile und reale Befehlsresultate. Source-only,
kein Home-Sync fuer diese Aenderung; keine neue Bedienoption. Re-Evaluation
nach Build und Runtime-Abnahme. Windows-Nachweis, keine native macOS-/Linux-
Abnahme behauptet. Fuer diesen linearen Vorgang ist keine Grafik erforderlich.

## English

The Owner explicitly authorized changing only Ubuntu package source transport
to HTTPS and then resuming build and execution. MergeAndSync/admin bypass
does not waive technical failures. Step 25 failed with exit 100; a bounded
probe in the same base image reproduced the HTTP failure while HTTPS returned
200. Both protocols worked from the Podman VM.

Only the three official Ubuntu URL prefixes change in the existing Deb822
source file. Repositories, versions, keys, signature checks, TLS validation
and sandbox boundaries remain intact. NIST SSDF/CWE Top 25: no new input
execution or trust source. No host network changes or version upgrades.
P1-1 evidence is complete; P2-3 build/SBOM and runtime acceptance remain
partial. The 21 target updates have not run. P1-4 and unrelated compliance
work are unchanged. Documentation impact: UpdateRequired, maintainer-owned
source-only operational evidence; no Home sync or new interface. Reevaluate
after build/runtime acceptance. Windows evidence only, no cross-platform
acceptance claimed.
