# Maven-Fallback und Quellenabgleich / Maven Fallback and Source Alignment

## Auftrag und Grenzen / Authority and Boundaries

DE: Der Owner beauftragte ausdruecklich die beiden Findings des Abschlussreviews:
offiziellen Apache-Archiv-Fallback ergaenzen und den frueheren Machine-Status
im Impact-Register historisch einordnen. Danach die drei aktiven Intakes
mit erhaltener Identitaet aktualisieren und unabhaengig vollstaendig reviewen.
Keine globale Wartung, Installation, Image-Build, Containeraktion, Commit
oder Push; keine neue Startautoritaet oder menschliche Freigabe.

EN: The owner explicitly commissioned the two final-review findings:
add the official Apache archive fallback and mark the earlier machine state
as historical in the impact register. Then update the three active intakes
with preserved identities and obtain an independent full review. No global
maintenance, installation, image build, container action, commit or push;
no new execution authority or human approval.

## Gezielte Korrekturen / Targeted Corrections

| ID | Aenderung / Change | Nachweisgrenze / Evidence boundary |
|---|---|---|
| REV-MAVEN-FALLBACK | Downloadfehler am Apache-CDN wechselt zum offiziellen Archiv fuer dieselbe Version / a CDN download failure falls back to the official archive for the same version | Maven 3.10.0 und feste SHA-512 unveraendert; fehlerhafte Pruefsumme bleibt harter Fehler, kein Fallback / unchanged version and checksum; checksum mismatch remains fatal, without fallback |
| REV-IMPACT-HISTORY | Fuenf fruehere Machine-Aussagen als historische Untersuchung vor dem Austausch markieren / mark five earlier machine statements as historical investigation before replacement | auf [aktuellen Statusnachtrag](sandbox-current-state-2026-10-25.md) verweisen; AMD64 und menschliche A11Y bleiben Open / link the current status addendum; AMD64 and human A11Y remain Open |

DE: Die zwoelf Tests in `scripts/tests/test_toolchain_version_pins.py`
bestanden vor der Quellenbindung. Fuenf davon fuehren den echten Download-
und Checksummenteil aus dem Dockerfile mit kuenstlichem curl aus: CDN-Erfolg,
Archiv-Fallback, falsche CDN-Pruefsumme, falsche Archiv-Pruefsumme und Ausfall
beider Quellen. Eine echte SHA-512-Pruefung kontrolliert die Testdaten.
Keine Archive werden installiert und keine Netzverbindung wird benoetigt.
Das ist keine neue Image-, Paket- oder Plattformabnahme. Das laufende Image
erhaelt den geaenderten Buildschritt nicht durch diese Quellenpflege.

EN: All twelve toolchain-pin tests passed before source binding. Five execute
the actual Dockerfile download/checksum prefix using fake curl: CDN success,
archive fallback, bad CDN checksum, bad archive checksum and both sources
unavailable. A real SHA-512 verifier checks fixture data. No archive is
installed and no network connection is needed. This grants no new image,
package or platform acceptance. Source maintenance does not update the
running image's build instructions.

## Lineage und Review / Lineage and Review

DE: Operation `3caff22f-59d5-4142-b15b-955ee96a3037` archiviert die vorherigen
Intakes, Receipts, Reihenansichten und Review-Dateien byte-identisch. Die
vorherige Intake-Fassung bleibt jeweils erste Quelle. Neue Receipts binden
die aktualisierten Dockerfile-/Test-Hashes sowie dieses Dokument und das
Impact-Register. Kontroll-IDs, Akzeptanzschwellen und Uebergaben aendern sich
nicht. Die Reihe bleibt `Completed`, `Eligible`, `Blocked`, `Blocked`.

EN: The operation archives previous intakes, receipts, order views and review
files byte-for-byte. Each prior intake remains its first source. New receipts
bind updated Dockerfile/test hashes, this document and the impact register.
Control IDs, acceptance thresholds and handoffs are unchanged. Preserve
Completed, Eligible, Blocked, Blocked.

DE: Das bisherige Review `0298d3b3-7ff1-42d8-a5f7-349d01139cf4` gilt nur
fuer seine archivierten Eingaben und wird ausdruecklich ersetzt. Ergebnis
und Begruendung der unabhaengigen Vollpruefung stehen ausschliesslich im
[neuen Reihenreview](../../specs/intake-review-reports/sandbox-development-lifecycle.md).
Auch ein Ready beurteilt Anforderungen und Quellenbindungen, nicht
technische Erfuellung, menschliche A11Y oder formelle Freigaben. Historische
Session-Logs und fruehere Timing-Matrizen werden nicht umgeschrieben.

EN: The former review applies only to its archived inputs and is explicitly
superseded. The separate series review alone records the independent full
review's outcome and rationale. Even Ready assesses requirements and source
bindings, not technical fulfillment, human A11Y or formal approvals.
Historical session logs and earlier timing matrices remain unchanged.
