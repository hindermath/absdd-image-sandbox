# KI-VO-Anwendbarkeit / AI Act applicability

## Deutsch

**Stand:** 2026-10-31; Quelle: [VO (EU) 2024/1689, konsolidiert 27.07.2026](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng), besonders Art. 2–6, 50 und 113. **Status:** Open, qualifizierter Privacy/Legal Review ausstehend.

| Grenze | Beobachtung | Offene Entscheidung |
| --- | --- | --- |
| Produkt | Das Image enthält fremde Agenten-CLIs; es enthält nach der vorliegenden Dockerfile-/Compose-Konfiguration kein eigenes trainiertes oder eingebettetes Modell und wählt keinen Provider vor. | Ob eine konkrete Weitergabe oder Integration ein eigenes KI-System, ein General-Purpose-AI-System oder eine Anbieterrolle schafft, hängt vom tatsächlichen Funktionsumfang und Vertrag ab. |
| Werkzeugbetrieb | Lernende können externe KI-Dienste erst nach eigener Anmeldung und Auswahl nutzen. Der Prompt-Dispatcher autorisiert keine Anmeldung und keine Modellwahl. | Betreiberrolle, Zweck, Nutzende/Betroffene, Datenarten, Region, Transparenz und nach Art. 6/Anhang III eine mögliche Hochrisikoeinstufung je tatsächlicher Nutzung prüfen. Kein Ausschluss allein wegen Unterricht. |
| Organisation | Rechtsträger und Land sind für eine Kopie des Repos unbekannt. | Art. 4 KI-Kompetenz, Art. 5 Verbote, Art. 50 Transparenz und ggf. Anbieter-/Betreiberpflichten sowie Vertrags- und Schulungsregeln durch zuständige Stelle entscheiden. |

Die konsolidierte Fassung nennt als allgemeines Anwendungsdatum **02.08.2026**, mit gestaffelten Ausnahmen in Art. 113: Kapitel I/II im Grundsatz seit **02.02.2025**, ausgewählte Bestimmungen seit **02.08.2025**, Hochrisiko nach Art. 6(2)/Anhang III ab **02.12.2027** und nach Art. 6(1)/Anhang I ab **02.08.2028**. Der Stichtag allein entscheidet keinen Scope. Art. 4 in der Fassung vom 27.07.2026 verlangt Maßnahmen zur KI-Kompetenz bei tatsächlichen Anbietern und Betreibern; er schreibt keinen hier erfundenen individuellen Abschlussnachweis vor.

**Owner/Frist:** Repository Owner mit qualifiziertem Privacy/Legal Review **vor Provideranmeldung, institutionellem Einsatz oder Weitergabe**; kalendarischen Termin setzt der Owner. Trigger sind neues eigenes KI-System/Modell, veränderte Agentenversion/Providerfunktion, neue Zielgruppe oder EU-Rechtsänderung. Bis dahin keine Hochrisiko- oder Konformitätsbehauptung und keine Anbieterfreigabe.

## English

**Open, 2026-10-31.** The image installs third-party agent clients but does not, on the observed Dockerfile/Compose configuration, embed a trained model or preselect an AI provider. Real sign-in, purpose, parties, people affected, model and region must be assessed before use. Article 113 has staged dates, including the general 2 August 2026 date and later high-risk dates; dates do not classify this product. The Repository Owner must obtain qualified Privacy/Legal Review before provider sign-in, institutional deployment or distribution. No training/FOSS exemption, AI-system classification, conformity or approval is inferred from this record.
