# Container-Delegation / Container delegation

## Deutsch

Die verteilte Wartungs-Manpage verweist auf diesen projektspezifischen
Leserpfad. Der vollstaendige Vertrag und die zentrale Umsetzung bleiben in
[Home-Baseline](https://github.com/hindermath/home-baseline/blob/586c142dcbc183aecf2daf13c2726ce09faa19b2/docs/maintenance/container-delegation-2026-09-20.md).
Hier werden keine Level-0-Spezifikationen oder Freigaben dupliziert.

Der neue Pin verwendet [prozessgebundenes Git-Vertrauen](https://github.com/hindermath/home-baseline/blob/4459e744d126d51b832986b09ac1a73cf88c1607/docs/maintenance/container-git-trust.md).
Nach Image-Aktivierung ist für die Wartung keine dauerhafte containerlokale
Git-Vertrauensliste mehr erforderlich; interaktive Aufrufe bleiben unverändert.

Den lokalen Image-Pin, Testnachweise und die noch ausstehende Aktivierung
dokumentiert das [Sandbox-Sitzungsprotokoll](../security/agent-session-log/2026-09-20-1055-maintenance-closeout.md).
Die Owner-Freigabe endet am 31.12.2026. Zugangsdaten bleiben auf dem Host;
Secure-Trader-Wartung erfolgt ausschliesslich in der freigegebenen Sandbox.

Documentation Impact: UpdateRequired. Owner: Repository-Owner. Zielgruppe:
Maintainer; Leserpfad: Wartungs-Manpage. Dokumentklasse: Quellenverweis,
nicht normative Vertragskopie. Distributionsklasse: Source-only; kein
Home-Sync. Bei Pin- oder Freigabeaenderungen erneut pruefen.

## English

The distributed maintenance manual links to this project-specific reader
path. The complete contract and central implementation remain in
[Home-Baseline](https://github.com/hindermath/home-baseline/blob/586c142dcbc183aecf2daf13c2726ce09faa19b2/docs/maintenance/container-delegation-2026-09-20.md).
No Level-0 specifications or approvals are duplicated here.

The new pin uses [process-scoped Git trust](https://github.com/hindermath/home-baseline/blob/4459e744d126d51b832986b09ac1a73cf88c1607/docs/maintenance/container-git-trust.md).
After image activation, maintenance no longer requires a persistent container
Git trust list; interactive calls remain unchanged.

The [sandbox session log](../security/agent-session-log/2026-09-20-1055-maintenance-closeout.md)
records the local image pin, tests and pending activation. Owner authority
expires on 2026-12-31. Credentials stay on the host; Secure Trader maintenance
runs only inside the approved sandbox.

Documentation Impact: UpdateRequired. Repository Owner maintains this
source-only navigation page for maintainers through the maintenance manual.
It is not a normative contract copy and requires no Home sync. Reevaluate
when the pin or approval changes.
