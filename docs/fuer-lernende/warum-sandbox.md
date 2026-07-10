# Warum eine Sandbox? / Why a Sandbox?

**Stand / Date:** 2026-07-10
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

**DE:** Dieses Dokument erklärt, **warum** KI-gestützte Entwicklung in einer
abgeschotteten Sandbox stattfinden muss — verständlich ab dem 1. Lehrjahr. Wenn
dir die Grundbegriffe (Container, Image, Mount) noch fehlen, lies zuerst
[container-grundlagen.md](container-grundlagen.md).

**EN:** This document explains **why** AI-assisted development must happen in a
walled-off sandbox — understandable from year 1. If you are still missing the
basics (container, image, mount), read
[container-grundlagen.md](container-grundlagen.md) first.

---

## Das Container-First-Gate / The Container-First Gate

**DE:** Es gibt eine einfache, verbindliche Regel:

> **Jeder Aufruf eines KI-Agenten (Codex, Claude Code, Gemini CLI, GitHub
> Copilot CLI oder OpenCode) für die
> Projektarbeit läuft im Container bzw. in der freigegebenen Sandbox — niemals
> direkt auf dem Arbeitsplatz-Rechner, auf gemeinsamen Servern oder in
> produktionsnahen Umgebungen.**

**EN:** There is one simple, binding rule:

> **Every call of an AI agent (Codex, Claude Code, Gemini CLI, GitHub Copilot
> CLI, or OpenCode) for project work
> runs inside the container or the approved sandbox — never directly on the
> workstation, on shared servers, or in production-near environments.**

**DE:** Das nennen wir das **Container-First-Gate**. „Gate" heißt Tor: Diese
Regel steht **vor** dem ersten Agenten-Aufruf, nicht als späteres Zusatzthema.
In der Lernreihe gilt sie ab der allerersten Einheit (Unit 00).

**EN:** We call this the **Container-First Gate**. A gate is a barrier you pass
through: this rule stands **before** the first agent call, not as a later
add-on. In the learning series it applies from the very first unit (unit 00).

---

## Warum ist das so wichtig? / Why Does This Matter So Much?

**DE:** Ein KI-Agent ist kein reines Textwerkzeug. Er kann **Dateien schreiben,
Befehle ausführen und auf das Netzwerk zugreifen**. Ohne Isolation trifft ein
Fehler oder ein Angriff direkt deinen echten Rechner — mit deinen privaten
Daten, Zugangsdaten und anderen Projekten.

**EN:** An AI agent is not just a text tool. It can **write files, run commands,
and access the network**. Without isolation, a mistake or an attack hits your
real machine directly — with your private data, credentials, and other
projects.

**DE:** Im Container gelten klare Grenzen. Ein Fehlgriff bleibt eingegrenzt:

**EN:** Inside the container, clear boundaries apply. A slip stays contained:

- **DE:** Der Agent kann nur in den freigegebenen Ordnern schreiben.
  **EN:** The agent can write only in the released folders.
- **DE:** Der Rest deines Rechners ist unsichtbar und nicht erreichbar.
  **EN:** The rest of your machine is invisible and unreachable.
- **DE:** Root-Rechte fehlen zur Laufzeit; der Container ist zusätzlich gehärtet.
  **EN:** Root rights are absent at runtime; the container is additionally
  hardened.

---

## Die vier Schutzziele / The Four Protection Goals

**DE:** Eine Sandbox-Nutzung dreht sich immer um vier Fragen. Merke sie dir —
sie kommen in jedem Lehrjahr wieder.

**EN:** Using a sandbox always revolves around four questions. Memorize them —
they return in every training year.

| Schutzziel / Goal | Frage / Question | Wo dokumentiert / Documented in |
|---|---|---|
| **Mounts** | Welche Ordner sieht der Container? / Which folders does the container see? | [sandbox-profil.md](sandbox-profil.md), Abschnitt 2 |
| **Schreibgrenzen / Write boundaries** | Wo darf der Agent schreiben? / Where may the agent write? | [sandbox-profil.md](sandbox-profil.md), Abschnitt 3 |
| **Netzwerk / Network** | Darf der Container ins Internet? / May the container reach the internet? | [sandbox-profil.md](sandbox-profil.md), Abschnitt 4 |
| **Secrets** | Welche Daten dürfen nie hinein? / Which data must never go in? | [sandbox-profil.md](sandbox-profil.md), Abschnitt 5 |

---

## Sandbox und ISO/IEC 27001 / Sandbox and ISO/IEC 27001

**DE:** In Organisationen mit ISO/IEC 27001 (oder gleichwertiger Zertifizierung)
ist das Container-First-Gate **kein Komfort, sondern ein prüfbarer
Kontrollpunkt**. Ein Audit kann verlangen, dass du nachweist, dass KI-Agenten
isoliert gelaufen sind. Vier Controls aus ISO/IEC 27001:2022 Annex A sind
besonders relevant:

**EN:** In organizations with ISO/IEC 27001 (or an equivalent certification),
the Container-First Gate is **not a convenience but an auditable control
point**. An audit may require you to prove that AI agents ran isolated. Four
controls from ISO/IEC 27001:2022 Annex A are especially relevant:

| Control | Thema / Topic | Bezug zur Sandbox / Relation to the sandbox |
|---|---|---|
| **A.5.23** | Sicherheit bei Cloud-Diensten / Security for cloud services | KI-Provider-Endpunkte und Egress werden bewusst entschieden. / AI provider endpoints and egress are a deliberate decision. |
| **A.8.25** | Sicherer Entwicklungszyklus / Secure development life cycle | Sichere Umgebung von Anfang an, nicht nachträglich. / Secure environment from the start, not retrofitted. |
| **A.8.28** | Sichere Programmierung / Secure coding | Riskante Schritte laufen isoliert und nachvollziehbar. / Risky steps run isolated and traceable. |
| **A.8.31** | Trennung von Entwicklung, Test und Produktion / Separation of dev, test, and production | Der Container trennt Experimente vom echten Rechner. / The container separates experiments from the real machine. |

---

## Warum schon im 1. Lehrjahr? / Why Already in Year 1?

**DE:** Vielleicht denkst du: „Ich schreibe im 1. Lehrjahr noch keinen
produktiven Code — warum die Regel jetzt?" Antwort: **Das Risiko entsteht am
Agenten-Aufruf, nicht am Kursfortschritt.** Sobald ein KI-Agent zum ersten Mal
Dateien schreibt oder Befehle ausführt, muss das isoliert geschehen. Deshalb
gilt das Gate ab der ersten Nutzung.

**EN:** You might think: "In year 1 I do not write production code yet — why the
rule now?" Answer: **the risk arises at the agent call, not at course
progress.** As soon as an AI agent writes files or runs commands for the first
time, it must happen isolated. That is why the gate applies from first use.

**DE:** Was im Laufe der Ausbildung wächst, ist nicht die Frage *ob* das Gate
gilt, sondern die **Tiefe deiner eigenen Nachweise**:

**EN:** What grows during training is not *whether* the gate applies, but the
**depth of your own evidence**:

| Lehrjahr / Year | Erwartung / Expectation |
|---|---|
| **1. Lehrjahr / Year 1** | Gate verstehen und einhalten; den ersten kontrollierten Agentenlauf nur im Container starten. Ohne Agentenlauf ist praktische Nutzung `N/A`; mit Agentenlauf ist sie `Applicable`. / Understand and follow the gate; start the first controlled agent run only in the container. Without an agent call, practical use is `N/A`; with an agent call, it is `Applicable`. |
| **2. Lehrjahr / Year 2** | Vollständiges Betriebskonzept vorbereiten und jeden Agentenlauf weiter in der Sandbox ausführen. / Prepare a full operating concept and continue to run every agent call inside the sandbox. |
| **3. Lehrjahr / Year 3 (SI/DV)** | Sandbox tatsächlich nutzen und Betriebsnachweise liefern. / Actually use the sandbox and deliver operating evidence. |

**DE:** Wichtig: **Agentenloses Lesen und menschliches Review dürfen außerhalb
der Sandbox stattfinden** — auch mit VS Code, JetBrains oder Visual Studio.
Sobald dabei ein Agent aufgerufen wird, gilt das Gate wieder.

**EN:** Important: **agent-free reading and human review may happen outside the
sandbox** — also with VS Code, JetBrains, or Visual Studio. As soon as an agent
is called, the gate applies again.

---

## Typische Anfängerfehler / Common Beginner Mistakes

**DE:** Diese Fehler passieren am häufigsten. Der erste ist der kritischste.

**EN:** These mistakes happen most often. The first is the most critical.

- **DE:** Einen KI-Agenten direkt auf dem Arbeitsplatz-Rechner statt im Container
  starten. **EN:** Starting an AI agent directly on the workstation instead of
  in the container.
- **DE:** Echte Secrets (API-Schlüssel, Passwörter) in Prompts oder Logs.
  **EN:** Real secrets (API keys, passwords) in prompts or logs.
- **DE:** Unbegrenzte Schreib- oder Netzwerkzugriffe zulassen.
  **EN:** Allowing unlimited write or network access.
- **DE:** Echte personenbezogene Daten statt fiktiver Testdaten verwenden.
  **EN:** Using real personal data instead of fictitious test data.
- **DE:** Fehlende Werkzeuge (Toolchains) verschweigen statt als `Open` zu
  notieren. **EN:** Hiding missing toolchains instead of noting them as `Open`.
- **DE:** Agenten-Regeln nur für einen Agenten schreiben (Parität verletzen).
  **EN:** Writing agent rules for only one agent (breaking parity).
- **DE:** Agenten-Caches oder Sessions ins Projekt-Repository committen.
  **EN:** Committing agent caches or sessions into the project repository.

---

## Kurzer Preflight-Check / Short Preflight Check

**DE:** Vor dem ersten Agenten-Aufruf gehst du diese Punkte durch. Nutze nur
Platzhalter wie `<PLATZHALTER-KEIN-ECHTER-WERT>`, nie echte Werte.

**EN:** Before the first agent call, go through these points. Use only
placeholders like `<PLACEHOLDER-NOT-A-REAL-VALUE>`, never real values.

- [ ] **DE:** Eine freigegebene Sandbox/ein Container ist verfügbar.
      **EN:** An approved sandbox/container is available.
- [ ] **DE:** Der Agent wird **im** Container gestartet, nicht auf dem Host.
      **EN:** The agent is started **inside** the container, not on the host.
- [ ] **DE:** Nur benötigte Ordner sind gemountet; Schreibrechte sind begrenzt.
      **EN:** Only needed folders are mounted; write rights are limited.
- [ ] **DE:** Keine echten Secrets in Prompts, Logs, Screenshots, Projektdateien.
      **EN:** No real secrets in prompts, logs, screenshots, or project files.
- [ ] **DE:** Netzwerkzugriff ist begrenzt oder als Risiko dokumentiert.
      **EN:** Network access is limited or documented as a risk.
- [ ] **DE:** Nur fiktive, datensparsame Testdaten.
      **EN:** Only fictitious, data-minimal test data.

**DE:** Die vollständige Preflight-Checkliste pflegt deine Ausbildungsstelle in
der Lernreihe (`Secure-Trader-Sandbox-Preflight.md`).

**EN:** The full preflight checklist is maintained by your training site in the
learning series (`Secure-Trader-Sandbox-Preflight.md`).

---

## Nächster Schritt / Next Step

**DE:** Du verstehst jetzt das Gate und die Schutzziele. Als Nächstes
installierst du Podman und startest den Container:
[installation.md](installation.md).

**EN:** You now understand the gate and the protection goals. Next you install
Podman and start the container: [installation.md](installation.md).
