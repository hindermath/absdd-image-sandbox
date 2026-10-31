# BSI C5: Cloud-Compliance-Assurance / Cloud compliance assurance

## Deutsch

**Stand:** 2026-10-31; Quelle: [BSI C5:2026 v1.1.0, 11.08.2026](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/CloudComputing/Anforderungskatalog/2026/C5_2026.pdf?__blob=publicationFile&v=13), [C3A-Scope](cloud-autonomy-applicability.md). **Status:** Open, keine dienstspezifische Anbieterprüfung oder C5-Testierung vorliegend. C5 ist ein Assurance-Rahmen für Cloud-Dienste, keine pauschale Zertifizierung der lokalen Sandbox.

| Scope | Derzeitige Evidenz | C5-Entscheidung |
| --- | --- | --- |
| Lokal gebautes Podman-Image | Kein angebotener Cloud-Dienst oder eigene Cloud-Runtime in `compose.yml`. | Für diese lokale Produkt-Runtime begründetes vorläufiges `N/A`; Architecture Review bestätigt oder korrigiert. |
| Externe Registries, Git-/CI-Hosting, Paketquellen | Als Entwicklungs- und Lieferkettenabhängigkeiten im [Bedrohungsmodell](threat-model.md), nicht als vom Repository betriebene Cloud. | Provider-/Kundenscope, Vertrag und erforderliche Assurance **Open**. |
| Optionaler KI-Provider | Auswahl und Anmeldung sind Nutzerentscheidung; konkrete Dienste/Regionen fehlen. | Assurance **Open** vor Nutzung mit schutzbedürftigen Daten. |

**Berichtsfelder für einen künftig relevanten Dienst:** Provider, eindeutiger Dienst, Region, C5-Fassung und Kriterienumfang, Bericht/prüfende unabhängige Stelle, Berichtsdatum, Ausnahmen, Subdienstleister, kundenseitige Kontrollen und erneute Review-Frist sind erforderlich. **Berichtstyp aktuell `Unknown`**, kein Bericht/Zeitraum/Wirksamkeitsnachweis im Repository. Typ 1 beurteilt Beschreibung, Design und Implementierung zu einem Stichtag; daraus folgt keine operative Wirksamkeit über eine Periode. Typ 2 benötigt Beginn und Ende des Prüfzeitraums und belegte Wirksamkeitsprüfung. Ein unbekannter Typ bleibt Open. Ein Anbieterprospekt oder ein C5-Bericht ersetzt weder eigene Kundenkontrollen noch C3A-, DSGVO- oder Rechtsprüfung.

**Shared Responsibility:** Für eine konkrete Cloud-Auswahl sind Identität/Zugriff, Netzwerk, Verschlüsselung/Schlüssel, Logging, Backups, Incident-Reaktion, Änderungen, Datenportabilität/Exit und Konzentrationsrisiko zwischen Provider und Betreiber zuzuordnen. Hier liegen für keinen konkreten Dienst belegte Provider- und Kundenanteile vor. Das ist eine offene Beschaffungs-/Betriebsfrage, kein technischer Pass.

**O-344-CLOUD:** Repository Owner und Architecture Review; Aktion: Scope je Provider/Dienst/Region und unabhängigen Bericht einschließlich Typ, Zeitraum, Abweichungen und Kundenkontrollen anfordern und bewerten. Frist **vor neuer Cloud-/Providerabhängigkeit oder betroffener Nutzung**; Kalenderdatum setzt der Owner. Trigger: Hosting-/Registry-/KI-Providerwechsel, Cloud-Runtime, neue Vertrags- oder Datenregion. Keine C5-Testierung, Zertifizierung oder Äquivalenz zu C3A behauptet.

## English

**Open, 2026-10-31.** The locally built Podman runtime is provisionally outside a cloud-service assurance assessment, while external hosting, registries and optional AI providers need a concrete service and contract review. No provider-specific C5 report is held; report type is `Unknown`. Type 1 concerns a point in time and cannot prove sustained effectiveness. Type 2 needs an audit period and operating-effectiveness evidence. Provider claims, customer controls, exceptions and C3A/GDPR scope remain separate. The Repository Owner and Architecture Review must assess a relevant report before a new cloud/provider dependency or affected use.
