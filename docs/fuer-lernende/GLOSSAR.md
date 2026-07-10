# Glossar / Glossary

**Stand / Date:** 2026-07-05
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

**DE:** Dieses Glossar erklärt Abkürzungen und Fachbegriffe, die im Repository und in den Lernmaterialien
vorkommen. Jeder Eintrag gibt die deutsche Erklärung zuerst, dann die englische Übersetzung des Begriffs.

**EN:** This glossary explains abbreviations and technical terms used in the repository and in the learning
materials. Each entry gives the German explanation first, then the English translation of the term.

---

## Priorisierung / Prioritization

| Kürzel / Abbrev. | Langform / Long form | Erklärung / Explanation |
|---|---|---|
| **P0** | Priorität 0 / Priority 0 | Blockierende Aufgabe — muss zuerst gelöst werden, bevor andere Arbeiten möglich sind. / Blocking task — must be resolved before other work is possible. |
| **P1** | Priorität 1 / Priority 1 | Hohe Dringlichkeit — sollte im nächsten Arbeitsschritt erledigt werden. / High urgency — should be done in the next work step. |
| **P2** | Priorität 2 / Priority 2 | Mittlere Dringlichkeit — wichtig, aber nicht unmittelbar blockierend. / Medium urgency — important but not immediately blocking. |
| **P3** | Priorität 3 / Priority 3 | Geringe Dringlichkeit — sinnvoll, aber aufschiebbar. / Low urgency — useful but deferrable. |

---

## Compliance-Status / Compliance Status

| Kürzel / Abbrev. | Erklärung / Explanation |
|---|---|
| **Applicable** | Diese Anforderung gilt für dieses Projekt und wird umgesetzt. / This requirement applies to this project and is being implemented. |
| **N/A** | Diese Anforderung gilt nicht — mit schriftlicher Begründung. / This requirement does not apply — with a written rationale. |
| **Open** | Diese Anforderung gilt, ist aber noch nicht umgesetzt — eine Folgeaufgabe ist geplant. / This requirement applies but has not yet been implemented — a follow-up task is planned. |
| **AlreadySatisfied** | Diese Anforderung gilt und ist bereits erfüllt — mit Nachweis. / This requirement applies and is already satisfied — with evidence. |
| **FollowUp** | Ein Follow-up-Punkt, der nach einem Audit nachgearbeitet wird. / A follow-up item to be addressed after an audit. |

---

## Checklisten / Checklists

**DE:** Die Checklisten `CL_01` bis `CL_12` gehören zur Richtlinie Sichere Entwicklung. Sie liegen im
Verzeichnis `docs/secure-development/checklisten/`.

**EN:** Checklists `CL_01` to `CL_12` belong to the Secure Development Guideline. They are in the directory
`docs/secure-development/checklisten/`.

| Kürzel / Abbrev. | Titel |
|---|---|
| **CL_01** | Standards-Anwendbarkeit / Standards Applicability |
| **CL_02** | Sichere Softwarearchitektur / Secure Software Architecture |
| **CL_03** | Krypto-Mindestvorgaben / Cryptography Minimum Requirements |
| **CL_04** | Bedrohungsmodellierung / Threat Modeling |
| **CL_05** | Lieferkette und Build-Integrität / Supply Chain and Build Integrity |
| **CL_06** | Schwachstellenoffenlegung / Vulnerability Disclosure |
| **CL_07** | CRA-Anwendbarkeit / CRA Applicability |
| **CL_08** | Sicherheits-Code-Review / Security Code Review |
| **CL_09** | KI-Codeerzeugung / AI Code Generation |
| **CL_10** | Sichere Entwicklungsumgebung / Secure Development Environment |
| **CL_11** | Datenschutz-Folgenabschätzung / Data Protection Impact Assessment |
| **CL_12** | Agentische KI in Sandbox-Umgebungen / Agentic AI in Sandbox Environments |

---

## Rollen / Roles

| Kürzel / Abbrev. | Langform / Long form | Erklärung / Explanation |
|---|---|---|
| **CISO** | Chief Information Security Officer | Leitende Person für Informationssicherheit in einer Organisation. / Lead person for information security in an organization. |
| **ISB** | Informationssicherheitsbeauftragte:r | Deutschsprachiger Titel: verantwortliche Person für Informationssicherheit. / German-language title: person responsible for information security. |
| **KIB** | KI-Beauftragte:r | Verantwortliche Person für KI-Governance und KI-Einsatz in einer Organisation. / Person responsible for AI governance and AI use in an organization. |

---

## Sprache und Barrierefreiheit / Language and Accessibility

| Kürzel / Abbrev. | Langform / Long form | Erklärung / Explanation |
|---|---|---|
| **CEFR** | Common European Framework of Reference for Languages | Europäischer Referenzrahmen für Sprachen; B2 = obere Mittelstufe, klare und strukturierte Sprache. / European framework for languages; B2 = upper intermediate, clear and structured language. |
| **B2** | CEFR-Niveau B2 | Klare Sätze, Fachinhalte verständlich formuliert, ohne unnötige Fremdwörter. / Clear sentences, technical content phrased comprehensibly, without unnecessary jargon. |
| **WCAG** | Web Content Accessibility Guidelines | Internationale Richtlinien für barrierefreie Web-Inhalte; Level AA ist der Standard-Basis in diesem Projekt. / International guidelines for accessible web content; Level AA is the standard baseline in this project. |
| **AA** | WCAG Level AA | Mittlere Barrierefreiheitsstufe — z. B. Überschriften-Hierarchie, Alt-Texte, Tastaturnavigation, ausreichende Kontrastverhältnisse. / Medium accessibility level — e.g. heading hierarchy, alt texts, keyboard navigation, sufficient contrast ratios. |
| **A11Y** | Accessibility | Kurzform aus dem Englischen: Barrierefreiheit. / Short form from English: accessibility. |

---

## Sicherheitsstandards / Security Standards

| Kürzel / Abbrev. | Langform / Long form | Erklärung / Explanation |
|---|---|---|
| **MSL** | Memory-Safe Language | Programmiersprache, die häufige Speicherfehler (z. B. Buffer Overflow) durch ihr Design verhindert. Beispiele: C#, Go, Java, Python, Rust, Swift. / Programming language that prevents common memory errors (e.g. buffer overflow) by design. Examples: C#, Go, Java, Python, Rust, Swift. |
| **SDLC** | Secure Development Life Cycle | Sicherer Entwicklungslebenszyklus — Prozess, der Sicherheit von der Anforderungsanalyse bis zum Betrieb einbezieht. / Secure Development Life Cycle — process that includes security from requirements to operation. |
| **SBOM** | Software Bill of Materials | Vollständige Liste aller Abhängigkeiten und Komponenten einer Software, ähnlich einer Stückliste. / Complete list of all dependencies and components of software, similar to a parts list. |
| **AI-SBOM** | AI Software Bill of Materials | SBOM speziell für KI-Modelle, Trainings- und Inferenz-Komponenten. / SBOM specifically for AI models, training, and inference components. |
| **VEX** | Vulnerability Exploitability eXchange | Dokument, das erklärt, ob und warum eine bekannte Schwachstelle in einer Komponente in einem konkreten Produkt ausnutzbar ist. / Document explaining whether and why a known vulnerability in a component is exploitable in a specific product. |
| **SLSA** | Supply-chain Levels for Software Artifacts | Framework für Nachweise zur Herkunft und Integrität von Software-Artefakten. / Framework for provenance and integrity evidence of software artifacts. |
| **ASVS** | Application Security Verification Standard | OWASP-Standard für die Überprüfung der Anwendungssicherheit, mit Levels 1–3. / OWASP standard for application security verification, with levels 1–3. |
| **SAMM** | Software Assurance Maturity Model | OWASP-Reifegradmodell für sichere Software-Entwicklung; hilft Organisationen, ihren Stand zu bewerten und zu verbessern. / OWASP maturity model for secure software development; helps organizations assess and improve their posture. |
| **STRIDE** | Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege | Methode zur Bedrohungsmodellierung: sechs Kategorien möglicher Angriffe. / Threat modeling method: six categories of possible attacks. |
| **CAPEC** | Common Attack Pattern Enumeration and Classification | Katalog beschriebener Angriffsmuster, nützlich bei der Bedrohungsmodellierung. / Catalog of described attack patterns, useful in threat modeling. |
| **CRA** | Cyber Resilience Act | EU-Gesetz für Cybersicherheitsanforderungen an Produkte mit digitalen Elementen. / EU law for cybersecurity requirements for products with digital elements. |
| **DPIA** | Data Protection Impact Assessment | Datenschutz-Folgenabschätzung — Prüfung, ob und wie ein Projekt personenbezogene Daten riskant verarbeitet. / Data protection impact assessment — checking whether and how a project processes personal data riskily. |

---

## Governance und Spec-Kit / Governance and Spec Kit

| Kürzel / Abbrev. | Erklärung / Explanation |
|---|---|
| **GSDB** | Generische Sichere-Entwicklung-Basis. Das Rahmenwerk aus Richtlinie, Checklisten und Presets, das in Level-2-Projekte integriert wird. / Generic Secure Development Base. The framework of guideline, checklists, and presets integrated into level-2 projects. |
| **Spec Kit** | Werkzeugkasten für strukturierte Feature-Spezifikation, Planung und Implementierung (`specify-cli`). / Toolbox for structured feature specification, planning, and implementation (`specify-cli`). |
| **Governance-Preset** | Vorkonfiguriertes Regelwerk für Spec-Kit-Läufe (z. B. `security-governance`, `a11y-governance`). / Pre-configured ruleset for Spec Kit runs (e.g. `security-governance`, `a11y-governance`). |
| **Level-2-Projekt** | Konkretes Ausbildungs- oder Entwicklungsprojekt, das auf dem Level-0-Framework (home-baseline) aufbaut. / Concrete training or development project built on the level-0 framework (home-baseline). |

---

## Weitere häufige Begriffe / Other Common Terms

| Begriff / Term | Erklärung / Explanation |
|---|---|
| **Container** | Abgeschlossene Software-Umgebung, die ein Programm und alle seine Abhängigkeiten enthält. Ähnlich wie eine Box, die auf jedem Computer gleich aussieht. / Enclosed software environment that contains a program and all its dependencies. Similar to a box that looks the same on every computer. |
| **Image** | Die Bauvorlage für einen Container, ähnlich einem Rezept. Aus einem Image entstehen beliebig viele gleiche Container. / The build template for a container, similar to a recipe. From one image you can create any number of identical containers. |
| **Registry** | Ein Online-Lager, aus dem Images heruntergeladen werden (hier `mcr.microsoft.com` für das .NET-Basis-Image). / An online store from which images are downloaded (here `mcr.microsoft.com` for the .NET base image). |
| **Sandbox** | Besonders abgeschotteter Container oder Prozess, in dem Fehler und Angriffe nicht nach außen dringen können. / Particularly walled-off container or process in which errors and attacks cannot escape to the outside. |
| **Host** | Dein eigener Rechner (Laptop oder PC), auf dem der Container läuft. / Your own machine (laptop or PC) on which the container runs. |
| **Podman-Machine** | Kleine, versteckte Linux-VM, die Podman auf macOS und Windows braucht, weil Container Linux voraussetzen. Auf Linux entfällt sie. / Small, hidden Linux VM that Podman needs on macOS and Windows because containers require Linux. Not needed on Linux. |
| **Mount** | Ein Verzeichnis, das von außen in den Container eingebunden wird, damit der Container darauf zugreifen kann. / A directory mounted from outside into the container so the container can access it. |
| **Bind-Mount** | Ein Ordner von deinem Rechner (Host), der in den Container eingehängt wird; beide greifen auf dieselben Dateien zu. / A folder from your machine (host) mounted into the container; both access the same files. |
| **Volume** | Ein von Podman verwalteter Speicherbereich, der Daten behält, auch wenn der Container neu startet — kein Ordner auf dem Host. / A storage area managed by Podman that keeps data even when the container restarts — not a folder on the host. |
| **Bridge-Netz** | Standard-Netzwerk von Compose, über das der Container ins Internet erreichen kann. / The default Compose network through which the container can reach the internet. |
| **Digest** | Eindeutige Prüfsumme (Hash) eines Container-Images — stellt sicher, dass immer genau dieselbe Version verwendet wird. / Unique checksum (hash) of a container image — ensures exactly the same version is always used. |
| **Egress** | Ausgehender Netzwerkverkehr vom Container ins Internet. / Outbound network traffic from the container to the internet. |
| **Ingress** | Eingehender Netzwerkverkehr von außen in den Container. / Inbound network traffic from outside into the container. |
| **Least Privilege** | Prinzip der geringsten Rechte — jeder Prozess bekommt nur die Rechte, die er wirklich braucht. / Principle of minimal rights — every process gets only the rights it really needs. |
| **Reproduzierbarkeit** | Gleiche Umgebung, gleiche Eingabe → immer gleiches Ergebnis. Wichtig für nachvollziehbare Nachweise. / Same environment, same input → always the same result. Important for traceable evidence. |
| **Betriebsnachweis** | Nachvollziehbarer Beleg (z. B. Ausgabe eines Tool-Laufs mit Datum), dass ein Werkzeug oder Prozess wie erwartet funktioniert hat. / Traceable evidence (e.g. output of a tool run with date) that a tool or process worked as expected. |
| **Agenten-Parität** | Gleichwertige Behandlung aller KI-Agenten (Claude, Codex, Gemini, OpenCode) — Regeln gelten für alle, nicht nur für einen. / Equal treatment of all AI agents — rules apply to all, not only to one. |
| **Dev Container** | Ein laufender Container, an den sich VS Code vom Host aus anhängt, um direkt darin zu arbeiten. VS Code installiert dafür beim Verbinden selbst einen Remote-Server im Container. / A running container that VS Code attaches to from the host to work inside it directly. VS Code installs a remote server into the container itself when connecting. |
| **LSP** | Language Server Protocol — ein Standard, über den Editoren Sprachfunktionen wie Autovervollständigung und Fehlerprüfung von einem Sprachserver beziehen (z. B. `gopls`, `rust-analyzer`, `sourcekit-lsp`). / Language Server Protocol — a standard through which editors obtain language features like autocompletion and error checking from a language server (e.g. `gopls`, `rust-analyzer`, `sourcekit-lsp`). |
| **IPC-Shim (`code`)** | Ein kleiner Helfer, den VS Code beim Verbinden in den Container legt; er leitet den `code`-Befehl über einen internen Kanal an das bereits geöffnete VS-Code-Fenster weiter. Ohne aktive Verbindung wirkungslos. / A small helper VS Code places into the container when connecting; it forwards the `code` command over an internal channel to the already open VS Code window. Ineffective without an active connection. |
