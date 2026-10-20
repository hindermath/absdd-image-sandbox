<!--
Quelle / Source: generische Ausbildungs- und Pruefgrundlage, bereinigt am 2026-06-17.
Dieses Dokument ist organisationsneutral und als generische Ausbildungs- und Pruefgrundlage formuliert.
Source: generic training and review baseline, generalized on 2026-06-17.
This document is organization-neutral and written as a generic training and review baseline.
-->

> **DE:** Diese Checkliste ist generisch und projektunabhaengig. Sie ist als Ausbildungs-, Review- und Haertungsgrundlage gedacht. Eine Nichtanwendbarkeit muss als `N/A` mit kurzer Begruendung dokumentiert werden.
>
> **EN:** This checklist is generic and project-independent. It is intended as a training, review, and hardening baseline. Non-applicability must be documented as `N/A` with a short rationale.

## Checkliste 07 – EU Cyber Resilience Act – Anwendbarkeit / EU Cyber Resilience Act – Applicability

**Dokument-ID / Document ID:** CL-07
**Version / Version:** 2.0.5
**Baseline-Version / Baseline version:** 3.4.4
**Dokumenttyp / Document type:** Kanonische, wiederverwendbare Pruefvorlage / Canonical reusable review template

### Nachweisinstanz / Evidence Instance

Diese Datei ist eine wiederverwendbare Vorlage. Ausgefüllte Projektnachweise werden unter `docs/security/secure-development/<datum>-<scope>/` abgelegt und nennen Projekt, Scope, Prüfdatum, Baseline-Version, verantwortliche Person und Reviewer. / This file is a reusable template. Completed project evidence is stored under `docs/security/secure-development/<date>-<scope>/` and names project, scope, review date, baseline version, responsible person, and reviewer.

### Zweck / Purpose

**DE:** Diese Checkliste hilft dabei, festzustellen, ob ein Produkt oder
Dienst unter den EU Cyber Resilience Act (CRA, Verordnung (EU) 2024/2847)
fällt, welche Pflichten gelten und bis wann sie umzusetzen sind.

**EN:** This checklist helps determine whether a product or service falls
under the EU Cyber Resilience Act (CRA, Regulation (EU) 2024/2847), which
duties apply, and the implementation deadline.

### Geltungsbereich / Scope

**DE:** Alle Produkte mit digitalen Elementen (Hardware, Software, Cloud-
Komponenten), die in der EU bereitgestellt werden. Auch interne Werkzeuge
sollten geprüft werden, falls sie an Externe abgegeben werden.

**EN:** All products with digital elements (hardware, software, cloud
components) made available in the EU. Internal tools should also be
checked if they are shared with external parties.

### Mitgeltende Dokumente / Related Documents

- Richtlinie Sichere Entwicklung
- Verordnung (EU) 2024/2847 (CRA)
- ISO/IEC 27001:2022, A.5.31, A.5.32
- ENISA-Leitfäden zur CRA-Umsetzung

### Wichtige Termine / Key Dates

- **DE:** In Kraft seit 10. Dezember 2024. Regeln zu
  Konformitätsbewertungsstellen gelten ab 11. Juni 2026. Die Pflicht zur
  Schwachstellen- und Vorfallmeldung gilt ab 11. September 2026. Die übrigen
  Pflichten gelten ab 11. Dezember 2027.
- **EN:** In force since 10 December 2024. Rules for conformity assessment
  bodies apply from 11 June 2026. Vulnerability and incident reporting duties
  apply from 11 September 2026. The remaining duties apply from
  11 December 2027.

#### URL-/Ablageverweise / URLs and Storage Locations

**DE:** Diese Links helfen beim Review. Projekt- oder organisationsinterne Dokumente koennen als lokale Arbeitskopie oder als Verweis auf den festgelegten Ablageort ergaenzt werden.

**EN:** These links help during reviews. Project or organization-internal documents can be added as local working copies or references to the defined storage location.

- **Richtlinie Sichere Entwicklung / Secure Development Guideline:** [lokale Arbeitsfassung in diesem Repository / local working copy in this repository](../Richtlinie_Sichere-Entwicklung.md)
- **Verfassung / Constitution:** [lokale Arbeitskopie der Verfassung / local working copy of the constitution](../../../constitution.md), [Verfassung im GitHub-Repository home-baseline / constitution in the home-baseline GitHub repository](https://github.com/hindermath/home-baseline/blob/main/constitution.md)
- **Checklisten-Index / Checklist index:** [Übersicht aller Checklisten / overview of all checklists](../README.md)
- **Leitlinie fuer sichere Programmierung / Secure coding guideline:** dieser Leitfaden oder eine projektspezifische gleichwertige Leitlinie / this guide or an equivalent project-specific guideline
- **Secure coding guideline:** this guide or an equivalent project-specific guideline
- **CISA Memory Safe Roadmaps:** [lokale PDF-Kopie des CISA-Dokuments / local PDF copy of the CISA document](../mitgeltende-dokumente/THE-CASE-FOR-MEMORY-SAFE-ROADMAPS-TLP-CLEAR.pdf), [EN-Markdown](../mitgeltende-dokumente/THE-CASE-FOR-MEMORY-SAFE-ROADMAPS-TLP-CLEAR.EN.md), [DE-Lernfassung](../mitgeltende-dokumente/THE-CASE-FOR-MEMORY-SAFE-ROADMAPS-TLP-CLEAR.DE.md), [CISA-Webseite zum Dokument / CISA webpage for the document](https://www.cisa.gov/resources-tools/resources/case-memory-safe-roadmaps)
- **ISO/IEC 27001:2022:** [offizielle ISO-Webseite zur ISO/IEC 27001:2022 / official ISO webpage for ISO/IEC 27001:2022](https://www.iso.org/standard/27001)
- **ISO/IEC 27002:2022:** [offizielle ISO-Webseite zur ISO/IEC 27002:2022 / official ISO webpage for ISO/IEC 27002:2022](https://www.iso.org/standard/75652.html)
- **NIST SSDF SP 800-218:** [NIST-Veröffentlichung SP 800-218 Secure Software Development Framework / NIST publication SP 800-218 Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- **NIST Zero Trust SP 800-207:** [NIST-Veröffentlichung SP 800-207 Zero Trust Architecture / NIST publication SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final)
- **OWASP ASVS:** [OWASP-Projektseite Application Security Verification Standard / OWASP project page Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- **OWASP Cheat Sheet Series:** [OWASP Cheat Sheet Series Projektseite / OWASP Cheat Sheet Series project page](https://cheatsheetseries.owasp.org/)
- **OWASP Proactive Controls:** [OWASP Proactive Controls Projektseite / OWASP Proactive Controls project page](https://owasp.org/www-project-proactive-controls/)
- **OWASP SAMM:** [OWASP SAMM Projektseite / OWASP SAMM project page](https://owaspsamm.org/)
- **OWASP Top 10 for LLM Applications:** [OWASP Top 10 for LLM Applications Projektseite / OWASP Top 10 for LLM Applications project page](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- **CWE Top 25:** [MITRE CWE Top 25 Übersicht / MITRE CWE Top 25 overview](https://cwe.mitre.org/top25/)
- **CAPEC:** [MITRE CAPEC Katalog / MITRE CAPEC catalogue](https://capec.mitre.org/)
- **CycloneDX:** [CycloneDX SBOM-Standard Projektseite / CycloneDX SBOM standard project page](https://cyclonedx.org/)
- **SPDX:** [SPDX SBOM-Standard Projektseite / SPDX SBOM standard project page](https://spdx.dev/)
- **CSAF/VEX:** [OASIS CSAF und VEX Dokumentation / OASIS CSAF and VEX documentation](https://oasis-open.github.io/csaf-documentation/)
- **SLSA:** [SLSA Supply-chain Levels for Software Artifacts Projektseite / SLSA project page](https://slsa.dev/)
- **OpenSSF Scorecard:** [OpenSSF Scorecard Projektseite / OpenSSF Scorecard project page](https://scorecard.dev/)
- **RFC 9116 security.txt:** [RFC 9116 zu security.txt / RFC 9116 for security.txt](https://www.rfc-editor.org/rfc/rfc9116)
- **NIST AI Risk Management Framework:** [NIST AI Risk Management Framework Webseite / NIST AI Risk Management Framework webpage](https://www.nist.gov/itl/ai-risk-management-framework)
- **EU Cyber Resilience Act:** [EU-Amtsblatt zum Cyber Resilience Act / EU Official Journal for the Cyber Resilience Act](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)
- **BSI TR-02102:** [BSI-Webseite zur Technischen Richtlinie TR-02102 / BSI webpage for Technical Guideline TR-02102](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr02102/tr-02102.html)

### Bewertung und Dokumentation / Assessment and Documentation

**DE:** Jeder Prüfpunkt bekommt genau einen Wert je Statusachse. Schreibe die Begründung so, dass eine neue Kollegin oder ein neuer Kollege den Entscheid später ohne Rückfrage versteht.

**EN:** Each checklist item gets exactly one value per status axis. Write the explanation so that a new team member can understand the decision later without asking again.

- **Anwendbarkeit / Applicability:** `Applicable`, `N/A` oder `Open`.
- **Umsetzungsstatus / Implementation status:** `Fulfilled`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed`.

**Pflichtfelder je Prüfpunkt / Required fields per item:** Anwendbarkeit, Umsetzungsstatus, Lernstufe, verantwortliche Rolle, Begründung, Evidenzpfad oder Link, Restrisiko, Neubewertungs-Trigger und nächste Maßnahme mit Zieltermin.

### Durchführungshinweise / Implementation Guidance

**DE:** Nutze diese Checkliste nicht als reine Ja/Nein-Liste. Sie ist ein Arbeits- und Auditdokument. Prüfe jeden Punkt gegen reale Artefakte: Code, Pull Request, Architekturdiagramm, Build-Log, Scan-Ergebnis, Ticket, Betriebsdokumentation oder Freigabeprotokoll. Wenn ein Nachweis noch fehlt, setze den Umsetzungsstatus auf `Not Assessed` oder `Not Fulfilled` und lege eine konkrete Folgeaufgabe an.

**EN:** Do not use this checklist as a simple yes/no list. It is a working and audit document. Check each item against real artefacts: code, pull request, architecture diagram, build log, scan result, ticket, operations document, or approval record. If evidence is missing, set the implementation status to `Not Assessed` or `Not Fulfilled` and create a concrete follow-up task.

**DE:** Schreibe kurze, klare Begründungen. Vermeide Abkürzungen ohne Erklärung. Wenn ein Punkt technisch schwierig ist, beschreibe den aktuellen Stand, das Risiko und den nächsten machbaren Schritt.

**EN:** Write short and clear explanations. Avoid unexplained abbreviations. If an item is technically difficult, describe the current state, the risk, and the next feasible step.

**DE:** Jeder Prüfpunkt muss deshalb drei Fragen beantworten: Was bedeutet die Anforderung im Projektalltag? Was ist konkret zu tun oder zu entscheiden? Welcher Nachweis zeigt das Ergebnis? Verwende Standard-IDs, Toolnamen und Abkürzungen nur zusammen mit einer kurzen Erklärung in Alltagssprache. Wenn ein Punkt für Auszubildende oder neue Teammitglieder nicht selbsterklärend ist, ergänze eine kurze Erklärung in der Begründung.

**EN:** Each item must therefore answer three questions: What does the requirement mean in daily project work? What exactly must be done or decided? Which evidence shows the result? Use standard IDs, tool names, and abbreviations only together with a short plain-language explanation. If an item is not self-explanatory for apprentices or new team members, add a short explanation in the rationale.

### Beispiel / Example

**DE:** Eine intern betriebene reine SaaS-Anwendung kann für CRA „nicht direkt anwendbar" sein. Wird dieselbe Software aber als Produkt oder installierbares Paket an Dritte abgegeben, muss die CRA-Anwendbarkeit neu bewertet und begründet werden.

**EN:** An internally operated pure SaaS application may be "not directly applicable" for CRA. If the same software is delivered to third parties as a product or installable package, CRA applicability must be reassessed and explained.

### A11Y-Hinweise / A11Y Notes

**DE:** Beim Ausfüllen dieser Checkliste müssen alle Nachweise auch textlich verständlich sein. Verweise sollen beschreibende Linktexte haben. Screenshots, Diagramme oder Scan-Auszüge brauchen eine kurze Textbeschreibung. Der Status darf nicht nur über Farbe erkennbar sein.

**EN:** When this checklist is filled in, all evidence must also be understandable as text. References should use descriptive link text. Screenshots, diagrams, or scan extracts need a short text description. The status must not be shown by color alone.

### Wichtige Begriffe / Key Terms

**DE:** Die folgenden Begriffe kommen in dieser Checkliste vor. Die Links springen zum Glossar dieses Kapitels, damit Auszubildende und Entwickler:innen ohne Sicherheits-Spezialwissen die Begriffe direkt nachlesen können.

**EN:** The following terms appear in this checklist. The links jump to this chapter's glossary so that apprentices and developers without specialist security knowledge can look them up directly.

- [CRA / Cyber Resilience Act](#cl-07-glossar-cra)
- [Produkt mit digitalen Elementen / Product with Digital Elements](#cl-07-glossar-product-digital-elements)
- [Kritisches Produkt / Critical Product](#cl-07-glossar-critical-product)
- [Konformitätsbewertung / Conformity Assessment](#cl-07-glossar-conformity-assessment)
- [CE-Kennzeichnung / CE Marking](#cl-07-glossar-ce-marking)
- [Technische Dokumentation / Technical Documentation](#cl-07-glossar-technical-documentation)
- [SBOM / Software Bill of Materials](#cl-07-glossar-sbom)
- [Schwachstellenbehandlung / Vulnerability Handling](#cl-07-glossar-vulnerability-handling)
- [Nicht anwendbar / N/A](#cl-07-glossar-nicht-anwendbar)
- [Evidenz / Evidence](#cl-07-glossar-evidenz)

### Checkliste / Checklist

#### CL-07-01: Produktart bestimmen / Determine Product Class

- **DE:** Produkt, Rolle und Marktbereitstellung anhand Art. 2 und Art. 3 CRA prüfen. Erfasst sind Software/Hardware und erforderliche Daten-Fernverarbeitungslösungen; fehlende lokale Installation allein begründet keine Ausnahme. Eigenständige SaaS-Dienste außerhalb dieser Definition gesondert prüfen. NIS2-Anwendbarkeit folgt aus Einrichtung, Sektor, Größe und nationalem Recht, nicht automatisch aus SaaS. Nichtkommerzielle freie Open-Source-Software und die besondere Steward-Rolle nach Art. 24 unterscheiden. Sektorale Ausnahmen (u. a. MDR/IVDR, Fahrzeuge, Luftfahrt, Schiffsausrüstung) am konkreten Rechtsakt prüfen. Nach Art. 69(2) gelten die allgemeinen Anforderungen für vor dem 11.12.2027 in Verkehr gebrachte Produkte nur bei wesentlicher Änderung ab diesem Datum; Art. 69(3) lässt Art. 14 seit 11.09.2026 trotzdem auch für diese Bestandsprodukte gelten. Je Produkteinheit das Inverkehrbringen prüfen, nicht pauschal das erste Release einer Produktfamilie. (EU) 2025/1535 Art. 1 nimmt Produkte nach (EU) Nr. 168/2013 aus, jedoch nicht die L1e-Pedalfahrzeuge nach dessen Art. 3(94)(b). Anhang III/IV und die technischen Kategorienbeschreibungen aus Durchführungsverordnung (EU) 2025/2392 heranziehen.
- **EN:** Assess product, role and market availability under CRA Articles 2 and 3. Software/hardware and necessary remote data-processing solutions are included; absence of local installation alone establishes no exemption. Assess standalone SaaS outside that definition separately. NIS2 scope depends on entity, sector, size and national law, not automatically on SaaS. Distinguish non-commercial free/open-source software from the steward role under Article 24. Check sector exemptions (including MDR/IVDR, vehicles, aviation and marine equipment) against the applicable act. Under Article 69(2), general requirements apply to products placed on the market before 2027-12-11 only if substantially modified from that date; Article 69(3) nevertheless applies Article 14 to these existing products since 2026-09-11. Assess placing on the market per product unit, not solely the first product-family release. Article 1 of (EU) 2025/1535 excludes products under (EU) No 168/2013, except its Article 3(94)(b) L1e vehicles designed to pedal. Use Annexes III/IV and Implementing Regulation (EU) 2025/2392 for technical category descriptions.
- **Akzeptanz / Acceptance:** Produkt/Version, Rolle, Rechtsfassung, Markt, Ausnahmen und Entscheidungsgrund in `docs/security/cra-applicability.md`; zuständige Prüfung datiert. / Record product/version, role, legal version, market, exemptions and rationale; date the responsible review.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-02: Kritikalität nach Anhang III / Criticality per Annex III

- **DE:** Wichtige Produkte anhand ihrer Kernfunktion Anhang III Klasse I oder II zuordnen. Die Kategorienbeschreibung nach (EU) 2025/2392 und den gewählten Konformitätspfad aus Art. 32 dokumentieren. Klasse I erlaubt Modul A nur bei Erfüllung der Bedingungen aus Art. 32(2); sonst Modul B+C oder H. Klasse II benötigt einen Pfad nach Art. 32(3). Die besondere FOSS-Regel aus Art. 32(5) erlaubt für Klasse-I/II-Produkte interne Kontrolle nur bei öffentlich verfügbarer technischer Dokumentation und darf nicht auf alle Produkte übertragen werden.
- **EN:** Map important products by core functionality to Annex III Class I or II. Record the category description under (EU) 2025/2392 and the selected Article 32 conformity path. Class I allows Module A subject to Article 32(2); otherwise use Module B+C or H. Class II requires an Article 32(3) path. The special FOSS rule in Article 32(5) permits internal control for Class I/II only when technical documentation is publicly available; it is not a blanket exception.
- **Akzeptanz / Acceptance:** Klasse, Rechtsstelle, Bedingungen, Evidence und gegebenenfalls zuständige notifizierte Stelle begründet dokumentiert. / Record class, legal provision, conditions, evidence and any required notified body with rationale.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-03: Kritisch nach Anhang IV / Critical per Annex IV

- **DE:** Anhang IV auf kritische Produkte prüfen: Hardware mit Sicherheitsboxen, Smart-Meter-Gateways und weitere Geräte für fortgeschrittene Sicherheitszwecke einschließlich sicherer Kryptoverarbeitung sowie Smartcards oder ähnliche Geräte einschließlich sicherer Elemente. Art. 8 und Art. 32(4) bestimmen den Pfad: einschlägige delegierte Rechtsakte und verfügbare europäische Zertifizierungsschemata prüfen; soweit die Bedingungen aus Art. 8(1) nicht vorliegen, ist nach Art. 32(4)(b) jeder Pfad aus Art. 32(3) zulaessig: Modul B+C, Modul H oder, soweit verfuegbar und anwendbar, ein europaeisches Cybersicherheitszertifizierungsschema nach Art. 27(9) mit mindestens Vertrauenswuerdigkeitsstufe „substanziell“. Aus dem CRA folgt kein allgemeines EAL4+-Gebot. Produktzertifizierung, Laborakkreditierung und CRA-Notifizierung sind verschiedene Nachweise; konkrete Stelle im offiziellen Notifizierungsregister prüfen.
- **EN:** Check Annex IV for critical products: hardware devices with security boxes, smart-meter gateways and other devices for advanced security purposes including secure cryptoprocessing, and smartcards or similar devices including secure elements. Articles 8 and 32(4) determine the path: assess applicable delegated acts and available European certification schemes; where Article 8(1) conditions are not met, Article 32(4)(b) allows any Article 32(3) route: Module B+C, Module H, or, where available and applicable, a European cybersecurity certification scheme under Article 27(9) at assurance level at least substantial. The CRA does not impose a universal EAL4+ requirement. Product certification, laboratory accreditation and CRA notification are separate proofs; verify any selected body in the official notification register.
- **Akzeptanz / Acceptance:** Anhang-IV-Treffer oder begründetes N/A, geprüfte Rechtsakte/Schemata und Konformitätspfad im CRA-Dossier. / Record Annex IV match or justified N/A, checked acts/schemes and conformity path in the CRA dossier.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-04: Sicherheits-Anforderungen Anhang I Teil I / Annex I Part I Requirements

- **DE:** Anhang I Teil I vollständig und risikobasiert abbilden: Nr. 1 sicheres Design; Nr. 2(a) keine bekannten ausnutzbaren Schwachstellen, (b) sichere Defaults, (c) Sicherheitsupdates, (d) Zugriffsschutz, (e) Vertraulichkeit, (f) Integrität, (g) Datenminimierung für persönliche und andere Daten, (h) Verfügbarkeit, (i) Auswirkungen auf andere Systeme, (j) Angriffsfläche, (k) Exploit-Folgenbegrenzung, (l) Logging mit Opt-out, (m) sichere Löschung und Übertragung. Anwendbarkeit und gesetzliche Bedingungen je Punkt bewerten. Nr. 2(b) umfasst die Rücksetzung in den Originalzustand; eine abweichende Vereinbarung zu sicheren Defaults gilt nur zwischen Hersteller und gewerblichem Nutzer bei einem maßgeschneiderten Produkt, nicht pauschal für Anhang I. Eine Scan-Ausgabe allein beweist keine Erfüllung. Konformitätsvermutung nach Art. 27 nur für die tatsächlich im EU-Amtsblatt für den CRA referenzierten einschlägigen Teile einer Norm annehmen; verwandte RED-/IoT-/Industrienormen sind nicht automatisch CRA-harmonisiert.
- **EN:** Map all of Annex I Part I on a risk basis: point 1 secure design; point 2(a) no known exploitable vulnerabilities, (b) secure defaults, (c) security updates, (d) access protection, (e) confidentiality, (f) integrity, (g) minimisation of personal and other data, (h) availability, (i) impact on other systems, (j) attack surface, (k) exploit mitigation, (l) logging with opt-out, (m) secure erasure and transfer. Assess applicability and statutory conditions per point. Point 2(b) includes resetting to the original state; a different agreement on secure defaults applies only between manufacturer and business user for a tailor-made product, not to Annex I as a whole. A scan alone does not prove fulfilment. Claim Article 27 presumption only for applicable standard parts actually referenced in the EU Official Journal for the CRA; related RED/IoT/industrial standards are not automatically CRA-harmonised.
- **Akzeptanz / Acceptance:** Vollständiges Punkt-Mapping in `docs/security/cra-annex-i-mapping.md` mit Risiko, Umsetzung, Test/Evidence und geprüften Amtsblattreferenzen. / Complete point mapping with risk, implementation, tests/evidence and checked OJ references.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-05: Schwachstellenbehandlung Anhang I Teil II / Annex I Part II Vulnerability Handling

- **DE:** Anhang I Teil II Nr. 1–8 einzeln nachweisen: Komponenten-/Schwachstelleninventar und maschinenlesbare SBOM (rechtlich mindestens Top-Level-Abhängigkeiten; lokale Vollständigkeitsvorgaben gesondert), zügige Behebung und soweit technisch möglich getrennte Sicherheitsupdates, regelmäßige Tests/Reviews, Information über behobene Lücken mit begründeten Offenlegungs-Ausnahmen, CVD-Policy, erreichbarer Meldekontakt, sichere Updateverteilung sowie zügige grundsätzlich kostenlose Sicherheitsupdates. Die Sonderregel für maßgeschneiderte Produkte zwischen Hersteller und gewerblichem Nutzer aus Nr. 8 gesondert prüfen. Vorgegebene Jahresintervalle, konkrete Scanwerkzeuge und SBOM-Formate sind lokale Umsetzung, keine wörtlichen CRA-Pflichten.
- **EN:** Evidence Annex I Part II points 1–8 individually: component/vulnerability inventory and machine-readable SBOM (statutory minimum top-level dependencies; separate local completeness rules), prompt remediation with separate security updates where technically feasible, regular tests/reviews, information on fixed issues with justified disclosure exceptions, CVD policy, reachable reporting contact, secure update delivery, and prompt generally free security updates. Assess the point 8 tailored-product agreement exception between manufacturer and business user separately. Fixed annual intervals, specific scanners and SBOM formats are local implementation choices rather than literal CRA duties.
- **Akzeptanz / Acceptance:** Acht Punkte mit Evidence in `docs/security/cra-annex-i-part-ii-mapping.md`; alter Dateiname `cra-annex-ii-mapping.md` nur als dokumentierter Legacy-Verweis. / Evidence for eight points; document the old misleading filename as a legacy alias only.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-06: Konformitätsbewertung / Conformity Assessment

- **DE:** Den Bewertungspfad anhand Produktkategorie, anwendbaren harmonisierten Standards und geltenden Sonderregeln bestimmen. Bei Klasse I kann Selbstbewertung an Bedingungen gebunden sein; Klasse II und kritische Produkte benötigen grundsätzlich externe Bewertung beziehungsweise ein zulässiges Zertifizierungsschema. Art. 32(5) erlaubt für FOSS-Produkte der Klasse I/II die interne Kontrolle nur bei öffentlich zugänglicher technischer Dokumentation. Keine pauschale Entscheidung aus einer Beispieltabelle ableiten.
- **EN:** Choose the assessment path from product category, applicable harmonised standards, and current exceptions. Class I self-assessment may be conditional; class II and critical products generally require external assessment or an eligible certification scheme. Article 32(5) permits internal control for FOSS Class I/II products only with publicly available technical documentation. Do not decide from an example table alone.
- **Akzeptanz / Acceptance:** Begründeter Pfad mit zuständiger Entscheidung; [CRA Art. 32](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) / Justified route with responsible decision and primary institutional source.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-07: CE-Kennzeichnung / CE Marking

- **DE:** EU-Konformitätserklärung nach Art. 28 und Anhang V (gegebenenfalls vereinfachte Erklärung nach Anhang VI) vor Inverkehrbringen nach Art. 13(12) erstellen. CE-Regeln stehen in Art. 29/30, nicht Art. 32. Für Software ist das CE-Zeichen auf der Erklärung oder der leicht direkt zugänglichen begleitenden Website zulässig; ein Splash-Screen ist keine allgemeine Pflicht. Begleitinformationen nach Anhang II und die erforderlichen Sprachen der Zielmitgliedstaaten prüfen. Nur tatsächlich angewandte, einschlägige Normen und reale Notifizierungs-/Zertifikatsdaten nennen; Beispielnormen oder erfundene Zertifikate sind kein Konformitätsnachweis.
- **EN:** Prepare the EU declaration under Article 28 and Annex V (or simplified declaration under Annex VI where applicable) before placing on the market under Article 13(12). CE rules are in Articles 29/30, not Article 32. Software may carry CE marking on the declaration or an easily/directly accessible accompanying website; a splash screen is not universally required. Check Annex II information and languages required by target Member States. Name only standards actually applied and applicable, and real notification/certificate data; example standards or invented certificates do not establish conformity.
- **Akzeptanz / Acceptance:** Datierte Erklärung, begründeter CE-Ort, Begleitinformationen und Sprachprüfung im Release-Dossier. / Dated declaration, justified CE location, accompanying information and language review in the release dossier.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-08: Technische Dokumentation / Technical Documentation

- **DE:** Technische Dokumentation gemäß Art. 31 und Anhang VII vor Inverkehrbringen erstellen und während des Supportzeitraums aktuell halten. Sie umfasst Produktbeschreibung, Entwurf/Entwicklung, Risikobewertung, Anhang-I-Mapping, angewandte Spezifikationen, Prüfungen, SBOM und nachvollziehbare Schwachstellenbehandlung. Nach Art. 13(13) technische Dokumentation und Konformitätserklärung mindestens zehn Jahre nach Inverkehrbringen oder für den Supportzeitraum aufbewahren, je nachdem, was länger ist. Dies ist keine pauschale Aufbewahrungsfrist für personenbezogene Agentenlogs. Zugriff, Integrität, Aktualisierung und Datenminimierung belegen.
- **EN:** Prepare technical documentation under Article 31 and Annex VII before placing on the market and keep it current during support. Include product description, design/development, risk assessment, Annex I mapping, applied specifications, tests, SBOM and traceable vulnerability handling. Article 13(13) requires retaining technical documentation and the declaration for at least ten years after placing on the market or the support period, whichever is longer. This is not a blanket retention period for personal agent logs. Evidence access control, integrity, updates and data minimisation.
- **Akzeptanz / Acceptance:** Indexiertes CRA-Dossier mit Anhang-VII-Mapping, Quellenstand und begründeter Aufbewahrungsentscheidung. / Indexed CRA dossier with Annex VII mapping, source version and justified retention decision.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-09: Meldepflichten 24 / 72 Stunden / 24- and 72-hour Reports

- **DE:** Hersteller melden aktiv ausgenutzte Schwachstellen und schwerwiegende Sicherheitsvorfälle nach Art. 14 über die Single Reporting Platform gleichzeitig an koordinierenden CSIRT und ENISA: Frühwarnung ohne unangemessene Verzögerung, spätestens 24 Stunden nach Kenntnis, Meldung spätestens nach 72 Stunden. Schwachstellen-Schlussbericht spätestens 14 Tage nach verfügbarer Abhilfe; Vorfall-Schlussbericht spätestens einen Monat nach Vorfallmeldung. Inhalt, Zuständigkeit und Nutzerinformation nach Art. 14 dokumentieren. CRA Art. 16(2), Art. 14(9) und (EU) 2026/881 betreffen eine begründete Verzögerung der CSIRT-Weiterleitung; sie verlängern keine Hersteller-Meldefrist. Art. 14 gilt nach Art. 69(3)/71(2) seit 11.09.2026 auch für zuvor in Verkehr gebrachte, in den CRA-Geltungsbereich fallende Bestandsprodukte. Keine gewöhnliche E-Mail-Adresse als gesetzlichen Plattformersatz ausgeben. Herstellerpflicht ab 11.09.2026, Steward-Pflichten nach Art. 24 ab 11.12.2027 separat behandeln; die [Kommissionsauslegung zu Meldepflichten](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) bestätigt diesen Beginn ausdrücklich für Art. 24(3). Eine zugleich bestehende Herstellerrolle bleibt ab 11.09.2026 gesondert meldepflichtig. Interne Übungen und Bereitschaft nach Risiko organisieren.
- **EN:** Manufacturers report actively exploited vulnerabilities and severe incidents under Article 14 through the Single Reporting Platform simultaneously to the coordinating CSIRT and ENISA: early warning without undue delay, at most 24 hours after awareness, followed by notification within 72 hours. Vulnerability final reports are due within 14 days after a corrective/mitigating measure is available; incident final reports within one month after incident notification. Record content, responsibility and user information under Article 14. CRA Articles 16(2), 14(9) and (EU) 2026/881 concern a justified delay of CSIRT dissemination; they do not extend manufacturer reporting deadlines. Under Articles 69(3)/71(2), Article 14 applies since 2026-09-11 also to existing in-scope products placed on the market earlier. Do not present an ordinary email address as a statutory platform substitute. Distinguish manufacturer duties from 11 September 2026 and steward Article 24 duties from 11 December 2027; the [Commission reporting guidance](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) explicitly confirms that start for Article 24(3). A concurrent manufacturer role retains its separate reporting duties from 11 September 2026. Organise exercises and on-call arrangements according to risk.
- **Akzeptanz / Acceptance:** Runbook mit beiden Meldeketten, Auslösern, Plattformzugang, Vertretung, Quellenstand und Übungsnachweis. / Runbook with both reporting chains, triggers, platform access, deputies, source version and exercise evidence.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-10: Lebenszyklus und Support / Lifecycle and Support

- **DE:** Support nach Art. 13(8) an erwarteter Nutzungsdauer und Produktart ausrichten, grundsätzlich mindestens fünf Jahre; ist die erwartete Nutzung kürzer, entspricht der Support dieser Dauer. Begründung und berücksichtigte Faktoren in der technischen Dokumentation festhalten. Art. 13(9) verlangt, veröffentlichte Sicherheitsupdates mindestens zehn Jahre nach Ausgabe oder für den verbleibenden Supportzeitraum verfügbar zu halten, je nachdem, was länger ist. Supportdauer, Updateverfügbarkeit und Dokumentationsaufbewahrung sind verschiedene Fristen; EOL-Hinweis allein erlaubt keine Verkürzung gesetzlicher Pflichten. Art. 13(18) verlangt Anhang-II-Informationen mindestens zehn Jahre nach Inverkehrbringen oder für den längeren Supportzeitraum zugänglich zu halten; bei Online-Bereitstellung verständlich und nutzerfreundlich online. Nach Art. 13(19) Supportende bereits beim Kauf klar und leicht zugänglich mindestens mit Monat/Jahr nennen und, soweit technisch nach Produktart möglich, bei Supportende einen Nutzerhinweis anzeigen.
- **EN:** Determine support under Article 13(8) from expected use and product type, generally at least five years; if expected use is shorter, support corresponds to that period. Record the rationale and considered factors in technical documentation. Article 13(9) requires issued security updates to remain available for at least ten years after issue or the remaining support period, whichever is longer. Support duration, update availability and document retention are distinct clocks; an EOL notice alone cannot shorten statutory duties. Article 13(18) requires Annex II information to remain available for at least ten years after placing on the market or the longer support period; online provision must remain accessible and user-friendly. Under Article 13(19), clearly state the support end at purchase in an easily accessible way with at least month/year and, where technically feasible for the product, display an end-of-support notification.
- **Akzeptanz / Acceptance:** Begründete, zuständig geprüfte Supportentscheidung mit getrennten Support-, Update-, Dokumentations- und Anhang-II-Informationsfristen, Kauf-/EOL-Hinweisen und Wiedervorlage. / Justified, responsibly reviewed support decision with separate support, update, documentation and Annex II information clocks, purchase/EOL notices and reevaluation.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-11: Hersteller-Pflichten und -Verträge / Manufacturer Duties and Contracts

- **DE:** Hersteller nach Art. 13, Bevollmächtigte nach Art. 18, Importeure nach Art. 19, Distributoren nach Art. 20 und Rollenwechsel nach Art. 21/22 getrennt prüfen. Lieferantenverträge risikobasiert auf Schwachstelleninformation, Support, SBOM, Auditrechte und Zuständigkeiten abstimmen. Eine interne 24-Stunden-Zulieferfrist, Haftungsregel oder Quellcode-Escrow kann eine begründete Vertragsanforderung sein; sie ist keine universelle CRA-Klausel. Vertragspflichten ersetzen nicht die verbleibende Herstellerverantwortung und dürfen nicht pauschal auf alle OSS-Beitragenden übertragen werden.
- **EN:** Distinguish manufacturer Article 13, authorised representative Article 18, importer Article 19, distributor Article 20 and role changes under Articles 21/22. Align supplier contracts on a risk basis for vulnerability information, support, SBOM, audit rights and responsibilities. An internal 24-hour supplier deadline, liability term or source escrow may be a justified contractual requirement; it is not a universal CRA clause. Contracts do not replace remaining manufacturer responsibility and must not be imposed indiscriminately on all OSS contributors.
- **Akzeptanz / Acceptance:** Rollen-/Pflichtenmatrix, geprüfte Verträge und begründete zusätzliche lokale Klauseln dokumentiert. / Record role/duty matrix, reviewed contracts and justified additional local terms.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

#### CL-07-12: Nichtanwendbarkeit dokumentieren / Document Non-Applicability

- **DE:** N/A mit Produkt/Version, Rolle, konkreter Rechtsstelle oder Definition, Begründung, Datum, Owner, Gegenprüfung, nächstem Review und gegebenenfalls Fachberatung dokumentieren. Art. 2(2)(a)/(b) betrifft MDR/IVDR und (c) Fahrzeuge nach (EU) 2019/2144, Art. 2(3) zertifizierte Luftfahrt, 2(4) Schiffsausrüstung, 2(5) delegierte Ausschlüsse, 2(6) identische Ersatzteile, 2(7) ausschließlich nationale Sicherheit/Verteidigung beziehungsweise besondere Verschlusssachen-Verarbeitung; Art. 2(8) begrenzt gesondert Auskunftspflichten bei entgegenstehenden wesentlichen Interessen der nationalen/öffentlichen Sicherheit oder Verteidigung und ist kein N/A-Ausschluss des Produkts. Nichtkommerzielle FOSS anhand Art. 2(1)/3(22) und der kommerziellen Marktbereitstellung abgrenzen; Steward-Pflichten nach Art. 24 gesondert prüfen. Die Fahrzeugausnahme (EU) 2025/1535 mit L1e-Pedal-Rückausnahme und die getrennten Bestandsprodukt-/Meldeentscheidungen nach Art. 69(2)/(3) aus CL-07-01/09 übernehmen. SaaS anhand Art. 2(1), Art. 3(1)/(2) und Erwägungsgrund 12 abgrenzen, nicht über eine erfundene SaaS-Ausnahme. NIS2, DORA und Datenschutz getrennt bewerten. Unbekannte Anwendbarkeit bleibt Open; kein stillschweigendes Weglassen.
- **EN:** Document N/A with product/version, role, exact provision or definition, rationale, date, owner, second review, next review and specialist advice where needed. Article 2(2)(a)/(b) covers MDR/IVDR and (c) vehicles under (EU) 2019/2144; Article 2(3) certified aviation, 2(4) marine equipment, 2(5) delegated exclusions, 2(6) identical spare parts, 2(7) exclusive national security/defence or specified classified-information processing; separately, Article 2(8) limits information-supply duties where disclosure would conflict with essential national/public security or defence interests; it is not a product-scope N/A exclusion. Assess non-commercial FOSS under Articles 2(1)/3(22) and commercial market availability; assess Article 24 steward duties separately. Apply the (EU) 2025/1535 vehicle exclusion with the L1e pedal exception and separate existing-product/reporting decisions under Article 69(2)/(3) from CL-07-01/09. Assess SaaS under Articles 2(1), 3(1)/(2) and recital 12 rather than an invented SaaS exemption. Assess NIS2, DORA and privacy separately. Unknown applicability remains Open; silent omission is not acceptable.
- **Akzeptanz / Acceptance:** Anwendbarkeitsbericht nach CL-01-12 mit genauem Rechtsbezug und dokumentiertem Review. / Applicability report under CL-01-12 with precise legal reference and documented review.
- **Lernstufe / Learning stage:** _Grundlage, Aufbau oder Vertiefung gemaess Lernpfad dokumentieren. / Record foundation, intermediate, or advanced according to the learning path._
- **Verantwortliche Rolle / Responsible role:** _Lernende Person, ausbildende Person, Projektverantwortung oder Security-Rolle benennen. / Name learner, instructor, project owner, or security role._
- **Anwendbarkeit / Applicability:**
  - [ ] `Applicable`
  - [ ] `N/A`
  - [ ] `Open`
- **Umsetzungsstatus / Implementation status:**
  - [ ] `Fulfilled`
  - [ ] `Partly Fulfilled`
  - [ ] `Not Fulfilled`
  - [ ] `Not Assessed`
- **Begründung / Explanation:** _Kurz erklären: Was wurde geprüft? Warum passt der Status? Welche Annahme gilt? Schreibe so, dass eine neue Entwicklerin, ein neuer Entwickler oder eine auszubildende Person den Entscheid ohne Spezialwissen versteht. / Briefly explain: What was checked? Why does the status fit? Which assumption applies? Write so that a new developer or apprentice can understand the decision without specialist security knowledge._
- **Evidenz / Evidence:** _Konkreten Nachweis nennen: Pfad, Link, Ticket, Pull Request, Scan-Report, Konfigurationsdatei, Spec-Kit-Artefakt oder anderes Dokument. Wenn der Nachweis nicht selbsterklärend ist, kurz beschreiben, was er zeigt. / Name concrete evidence: path, link, ticket, pull request, scan report, configuration file, Spec Kit artefact, or other document. If the evidence is not self-explanatory, briefly describe what it shows._
- **Restrisiko / Residual risk:** _Verbleibendes Risiko oder `None` mit kurzer Begründung dokumentieren. / Record remaining risk or `None` with a short rationale._
- **Neubewertungs-Trigger / Re-evaluation trigger:** _Aenderung, Termin oder Ereignis nennen, das eine erneute Prüfung auslöst. / Name the change, date, or event that triggers renewed review._
- **Nächste Maßnahme / Next action:** _Bei `Open`, `Partly Fulfilled`, `Not Fulfilled` oder `Not Assessed` ausfüllen: konkrete Aufgabe, verantwortliche Person, Zieltermin und erwarteter Nachweis. / Fill for `Open`, `Partly Fulfilled`, `Not Fulfilled`, or `Not Assessed`: concrete task, owner, target date, and expected evidence._

### Akzeptanzkriterien gesamt / Overall Acceptance

**DE:** Erfüllt, wenn alle Punkte abgeschlossen sind und das CRA-Dossier
revisionsfest abgelegt ist.

**EN:** Fulfilled when every item is closed and the CRA dossier is stored
in an audit-ready way.

### Glossar / Glossary

**DE:** Dieses Glossar erklärt die wichtigsten Begriffe dieser Checkliste in Alltagssprache. Es ändert keine Anforderungen, sondern macht die vorhandenen Prüfpunkte leichter verständlich.

**EN:** This glossary explains the most important terms in this checklist in plain language. It does not change requirements; it makes the existing review items easier to understand.

<a id="cl-07-glossar-cra"></a>

#### CRA / Cyber Resilience Act

- **DE:** Der Cyber Resilience Act ist eine EU-Verordnung für Produkte mit digitalen Elementen. Er verlangt Sicherheitsanforderungen, Schwachstellenbehandlung und bestimmte Meldungen.
- **EN:** The Cyber Resilience Act is an EU regulation for products with digital elements. It requires security requirements, vulnerability handling, and certain reports.

<a id="cl-07-glossar-product-digital-elements"></a>

#### Produkt mit digitalen Elementen / Product with Digital Elements

- **DE:** Ein Produkt mit digitalen Elementen ist Software oder Hardware mit Softwarebezug, die unter den CRA fallen kann.
- **EN:** A product with digital elements is software or hardware with software relevance that may fall under the CRA.

<a id="cl-07-glossar-critical-product"></a>

#### Kritisches Produkt / Critical Product

- **DE:** Ein kritisches Produkt ist nach CRA besonders sicherheitsrelevant. Die Einstufung kann strengere Prüf- und Dokumentationspflichten auslösen.
- **EN:** A critical product is especially security-relevant under the CRA. The classification can trigger stricter review and documentation duties.

<a id="cl-07-glossar-conformity-assessment"></a>

#### Konformitätsbewertung / Conformity Assessment

- **DE:** Eine Konformitätsbewertung prüft, ob ein Produkt die geltenden Anforderungen erfüllt. Beim CRA kann sie Voraussetzung für die Bereitstellung sein.
- **EN:** A conformity assessment checks whether a product meets applicable requirements. Under the CRA it can be required before making the product available.

<a id="cl-07-glossar-ce-marking"></a>

#### CE-Kennzeichnung / CE Marking

- **DE:** Die CE-Kennzeichnung zeigt, dass ein Produkt nach Erklärung des Herstellers die einschlägigen EU-Anforderungen erfüllt.
- **EN:** CE marking shows that, according to the manufacturer’s declaration, a product meets the relevant EU requirements.

<a id="cl-07-glossar-technical-documentation"></a>

#### Technische Dokumentation / Technical Documentation

- **DE:** Technische Dokumentation beschreibt Produkt, Architektur, Risiken, Sicherheitsmaßnahmen, Tests und Nachweise so, dass Prüfung und Wartung möglich sind.
- **EN:** Technical documentation describes product, architecture, risks, security measures, tests, and evidence so that review and maintenance are possible.

<a id="cl-07-glossar-sbom"></a>

#### SBOM / Software Bill of Materials

- **DE:** Eine SBOM ist eine Stückliste für Software. Sie nennt Komponenten, Versionen und oft Lizenzen, damit Risiken und Schwachstellen schneller gefunden werden.
- **EN:** An SBOM is a bill of materials for software. It lists components, versions, and often licences so that risks and vulnerabilities can be found faster.

<a id="cl-07-glossar-vulnerability-handling"></a>

#### Schwachstellenbehandlung / Vulnerability Handling

- **DE:** Schwachstellenbehandlung umfasst Erkennen, Bewerten, Beheben und Kommunizieren von Schwachstellen. Sie braucht klare Zuständigkeiten und Fristen.
- **EN:** Vulnerability handling covers identifying, assessing, fixing, and communicating vulnerabilities. It needs clear responsibilities and deadlines.

<a id="cl-07-glossar-nicht-anwendbar"></a>

#### Nicht anwendbar / N/A

- **DE:** Nicht anwendbar bedeutet, dass ein Prüfpunkt sachlich nicht zum Projekt passt. Diese Entscheidung braucht immer eine kurze und nachvollziehbare Begründung.
- **EN:** Not applicable means that a review item does not fit the project. This decision always needs a short and traceable reason.

<a id="cl-07-glossar-evidenz"></a>

#### Evidenz / Evidence

- **DE:** Evidenz ist ein prüfbarer Nachweis. Das kann ein Link, Ticket, Scan-Bericht, Pull Request, Protokoll, Architekturdiagramm oder Dokument sein.
- **EN:** Evidence is verifiable proof. It can be a link, ticket, scan report, pull request, record, architecture diagram, or document.

### Versionshistorie / Version History

- **Version 1.0 (2026-04-27):** Erstfassung / Initial version
- **Version 1.1 (2026-04-27):** Erweiterte Durchführungshinweise, Quellen-URLs, Statusfelder und Beispiele / Extended guidance, source URLs, status fields, and examples
- **Version 1.2 (2026-04-30):** CRA-Stichtage und Schlussbericht-Fristen konkretisiert / Clarified CRA key dates and final-report deadlines
- **Version 1.3 (2026-06-15):** Nichtanwendbarkeitsentscheidung mit CL_01-Regulatory-Screening verknüpft; synchron mit Richtlinie Sichere Entwicklung v2.9.0. / Linked non-applicability decisions to CL_01 regulatory screening; synchronized with Richtlinie Sichere Entwicklung v2.9.0.

- **Version 1.4 (2026-06-16):** Verständlichkeit der Durchführungshinweise, Begründungs-, Evidenz- und Maßnahmenfelder für Entwickler:innen und Auszubildende präzisiert; CEFR-B2- und WCAG-2.2-AA-konforme Ausfüllhilfe ergänzt. / Refined understandability of implementation guidance, rationale, evidence, and action fields for developers and apprentices; added CEFR B2 and WCAG 2.2 AA conformant completion help.

- **Version 1.5 (2026-06-17):** Glossar und Begriff-Links für Entwickler:innen und Fachinformatik-Auszubildende ergänzt; wichtige Abkürzungen und Technologien in CEFR-B2-Sprache erklärt. / Added glossary and term links for developers and IT specialist apprentices; explained important abbreviations and technologies in CEFR B2 language.

---

- **Version 2.0.0 (2026-07-10):** Einheitliches zweiachsiges Statusmodell, stabile CL-IDs, Lernstufe, Rollen-, Evidenz-, Restrisiko- und Neubewertungsfelder sowie klare Trennung zwischen Vorlage und Projektnachweis eingeführt; synchron mit sichere-Entwicklung-Basis 3.0.0. / Added the unified two-axis status model, stable CL IDs, learning-stage, role, evidence, residual-risk, and re-evaluation fields, plus clear separation between template and project evidence; synchronized with secure-development baseline 3.0.0.
- **Version 2.0.1 (2026-10-19):** Level-0-Konsolidierung: Baseline-Bindung und fachliche Konsistenz geprüft; Grenzen im Reviewbericht. / Level-0 consolidation: baseline binding and consistency reviewed; limitations recorded in the review report.
- **Version 2.0.2 (2026-10-20):** Primärquellen-Nachprüfung und Baseline-Bindung 3.4.1; Details im Quellenabschluss. / Primary-source follow-up and baseline binding 3.4.1; see source closure report.

- **Version 2.0.3 (2026-10-20):** Bedingten Zertifizierungspfad nach Art. 32(3)(c)/(4)(b) ergaenzt; Baseline 3.4.2. / Added conditional certification route under Article 32(3)(c)/(4)(b); baseline 3.4.2.


- **Version 2.0.4 (2026-10-20):** Unabhängige Reviewkorrekturen und Baseline 3.4.3; siehe [Prüfbericht](../../maintenance/gsdb-independent-fixes-2026-10-20.md). / Independent review corrections and baseline 3.4.3; see review report.

- **Version 2.0.5 (2026-10-20):** Acht P3-Nachbefunde korrigiert, Baseline 3.4.4. / Correct eight P3 follow-up findings, baseline 3.4.4.
