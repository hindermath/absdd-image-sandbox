# Container-Delegation: Image-Pin / Container delegation: image pin

## Deutsch

Der Owner genehmigte am 20.09.2026 ausdruecklich MergeAndSync mit
Admin-Bypass fuer das Level-0-Delegationspaket und den zugehoerigen Image-Pin.
Technische Gates bleiben verbindlich. Der Wartungsumfang und die
Owner-Freigabe bis 31.12.2026 bleiben unveraendert; Provider, Modelle,
Secrets, Mounts und Rollenfreigaben werden nicht erweitert.

P1-1: Sitzungsnachweis. P1-4: bestehende befristete Owner-Freigabe,
keine ersatzweise formale CISO-/ISB-/KIB-Freigabe. P2-3: imagebezogene
CycloneDX-Stueckliste, kein behaupteter vollstaendiger Vulnerability-Scan.

Die kanonische Bindung steht in `home-baseline.lock.json` und der
Sandbox-Freigabetabelle. Das Paket delegiert lokale Secure-Trader-
Wartungsoperationen in den freigegebenen Container. Authentifiziertes Fetch
bleibt auf dem Host; kein Credential-Transfer, kein Host-Fallback fuer
delegierte Operationen. Paketdateien werden vor Ausfuehrung hashgebunden
gegen die schreibgeschuetzte Image-Referenz geprueft.

Vorbereitung: Audit-Metadaten exportiert, bestehende 20 Mounts und sechs
benannte Volumes inventarisiert. Die private lokale Rueckfallsicherung
`localhost/absdd-image-sandbox-recovery:before-delegation-3725b3e`
bewahrt die alte beschreibbare Container-Schicht und wird nicht publiziert.
Benannte Volumes werden nicht geloescht oder durch Image-Inhalte ersetzt.

Level 0 wurde nach 18 erfolgreichen CI-Checks als PR #305 gemergt;
Pin: `110ac82efb7504e177fdd5e934046d922a2d825c`. Ein transienter TLS-Fehler
beim unveraendert gepinnten Antigravity-Download wurde durch einen
unveraenderten Wiederholungsbuild behoben. Image:
`8ad4642d7b7db6bcbeb3efdc5d20daae1c71a73793cc393e78066de599681775`.
Neun Pin-/Dokumentationstests, alle Pre-commit-Hooks und 22 Delegationstests
im netzwerklosen finalen Image bestanden. Vollstaendige Paket-Hashbindung
und Schreibschutz bestanden; statische Compose-Konfiguration bytegleich.

Finale CycloneDX-1.7-SBOM: 28.970 Komponenten,
`sboms/2026-09-20-localhost-absdd-image-sandbox_ade-delegation-110ac82e.cdx.json`
(ignoriertes lokales Build-Artefakt), SHA-256
`fe49f9b6903a7de8c1c21df501a4a048daa381fd20333897ff30d60c94abf094`.
Nach erneutem Audit-Export wurde nur der Service-Container ueber Compose
ohne Build und ohne Volume-Loeschung neu erzeugt: `221c2120a59d`, running,
UID 1655, Neustartzaehler 0. Alle 20 Mounts sind identisch, ebenso Namen
und Erstellungszeiten der sechs Volumes. Der eingebettete Commit entspricht
dem Lock. Dies ist eine begrenzte Wiederanlaufpruefung, kein
Langzeitstabilitaetsnachweis und noch kein abgeschlossener Wartungslauf.

Documentation Impact: UpdateRequired. Kanonische Quelle: Lock und
Sandbox-Freigabetabelle; Owner: Repository-Owner. Maintainer finden den
Vertrag ueber den bestehenden README-Pfad zur Home-Baseline-Referenz.
Dieses historische Sitzungsprotokoll dokumentiert Evidence, nicht neue
Governance. Deutsch zuerst, Englisch danach. Distribution: Source und
Sandbox-Image; kein Host-Home-Sync durch diese Pin-Aenderung. Re-Evaluation
bei Pin-, Delegations- oder Freigabeaenderungen. Der anschliessende
Flottenwartungslauf ist ein eigener Nachweis und wird nicht vorweggenommen.

## English

On 2026-09-20 the Owner explicitly approved MergeAndSync with admin bypass
for the Level-0 delegation package and corresponding image pin. Technical
gates remain mandatory. Maintenance scope and the Owner approval expiring
on 2026-12-31 are unchanged; no additional provider, model, secret, mount or
formal role authority is granted.

P1-1 records the session; P1-4 retains bounded Owner authority, not formal
CISO/ISB/KIB approval. P2-3 records an image-specific CycloneDX inventory,
not a complete vulnerability assessment. The lock and sandbox approval
table bind the read-only reference. Local Secure Trader maintenance runs
inside the approved container; authenticated fetch stays on the host.
No credentials are transferred and no host fallback is permitted for
delegated operations. Package hashes are checked before execution.

Audit metadata was exported; twenty mounts and six named volumes were
inventoried. A private local recovery image preserves the previous writable
container layer; it must not be published. Named volumes are retained.

Level 0 PR #305 merged after eighteen successful CI checks. The exact pin
is `110ac82efb7504e177fdd5e934046d922a2d825c`. An unchanged build retry
resolved a transient TLS download failure without changing version or hash
pins. The final image is
`8ad4642d7b7db6bcbeb3efdc5d20daae1c71a73793cc393e78066de599681775`.
Nine pin/documentation tests, all pre-commit hooks and twenty-two delegation
tests in the network-disabled image passed. Complete package hash binding
and read-only checks passed; static Compose configuration is byte-identical.
The final CycloneDX 1.7 inventory contains 28,970 components; its local
ignored artifact and SHA-256 are recorded above.

After another audit export, Compose recreated only the service container,
without rebuilding or deleting volumes. Container `221c2120a59d` is running
as UID 1655 with restart count zero. All twenty mounts and the names and
creation times of all six volumes are unchanged. The embedded commit matches
the lock. This is bounded restart evidence, not long-term stability or a
completed fleet maintenance run.

Documentation Impact is UpdateRequired. The lock and approval table are
canonical, owned by the repository Owner and discoverable through the
existing README reference path. This bilingual historical session log is
evidence, not new governance. Source/image distribution only; this pin
change does not run host Home sync. Reevaluate on pin, delegation or
approval changes. Subsequent fleet maintenance requires separate evidence.
