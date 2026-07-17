# Lastenheft: Sandbox Secure-Development-Selbstpruefung

**Dokumenttyp:** Spec-Kit Intake / Lastenheft  
**Status:** Vorbereitung fuer spaeteren Spec-Kit-Lauf, kein gestarteter Lauf  
**Repository:** absdd-image-sandbox  
**Zielgruppe:** Fachinformatiker*innen in Ausbildung, Entwickler*innen, Reviewer und KI-Agenten

## Ziel / Goal

Dieses Lastenheft beschreibt einen spaeteren Spec-Kit-Lauf, der die Sandbox selbst gegen die sichere-Entwicklungsbasis prueft. Die Sandbox soll sicher genug gehaertet sein und gleichzeitig arbeitsfaehig bleiben. Sie darf nicht durch zu starke Restriktionen fuer Ausbildung, Spec Kit, KI-Agenten und MSL-basierte Entwicklung unbrauchbar werden.

*This intake describes a later Spec Kit run that checks the sandbox itself against the secure-development baseline. The sandbox should be hardened enough while remaining usable. It must not become unusable for training, Spec Kit, AI agents, and MSL-based development through excessive restrictions.*

## MSL-Zielbild / MSL Target Picture

Die Selbstpruefung betrachtet Entwicklung mit KI-Agenten fuer folgende Memory-Safe Languages: Rust, Swift, C#, F#, Java, Kotlin, Scala, Go, Dart, Python, Ruby, JavaScript, TypeScript, Haskell, OCaml, Erlang, Elixir, Ada und SPARK.

Nicht jede Toolchain muss sofort im Image enthalten sein. Der spaetere Lauf dokumentiert pro Sprache `Supported`, `Open` oder `N/A` mit Begruendung.

## Scope

- Nicht-privilegierte Container-Ausfuehrung und Build-/Runtime-Grenzen pruefen.
- Host-Mounts, Schreibrechte, Agenten-Schreibgrenzen und Deny-Read-Pfade pruefen.
- Netzwerkentscheidung und Egress-Risiko gegen Arbeitsfaehigkeit abwaegen.
- Secrets, Provider-Konfiguration, lokale Profile und Token-Speicher pruefen.
- SBOM, Dependency-Audit, Image-Scan und Tool-Pinning als Evidence planen.
- Spec-Kit-Nutzbarkeit und sieben Governance-Presets pruefen.
- MSL-Toolchain-Matrix fuer aktuelle und geplante Sprachen erstellen.
- C#/.NET, Rust, Go, Python, JavaScript/TypeScript und Java/Kotlin als erste praktische Smoke-Check-Kandidaten betrachten, wenn sie im Image verfuegbar sind.

## Nicht-Ziele / Non-Goals

- Kein sofortiger Umbau des Images.
- Kein Entfernen benoetigter Entwicklungswerkzeuge ohne Ersatzentscheidung.
- Kein Blockieren legitimer Paketregistries ohne dokumentierte Alternative.
- Keine produktive Cloud-Architektur.
- Keine automatische Freigabe der Sandbox.

## Anforderungen / Requirements

1. Der spaetere Lauf bewertet jedes Sicherheitsziel mit `Applicable`, `N/A` oder `Open`.
2. Jede Restriktion muss den Schutzgewinn und die Auswirkung auf Arbeitsfaehigkeit nennen.
3. Die Sandbox muss Lern- und Entwicklungsfluesse fuer Auszubildende verstaendlich dokumentieren.
4. MSL-Unterstuetzung wird als Matrix dokumentiert, nicht pauschal behauptet.
5. Offene Risiken erhalten Folgeaufgaben mit Evidenzpfad.

## Akzeptanzkriterien / Acceptance Criteria

- `spec.md`, `plan.md` und `tasks.md` beschreiben die Balance zwischen Haertung und Nutzbarkeit.
- `docs/security/` enthaelt oder plant Nachweise fuer Isolation, Mounts, Netzwerk, Toolchains, SBOM/Scan und KI-Werkzeuge.
- Die MSL-Support-Matrix ist vorhanden oder als konkrete Aufgabe geplant.
- Arbeitsfaehigkeit fuer Ausbildung, Spec Kit und KI-Agenten wird nicht pauschal geopfert.

## Optimaler Spec-Kit Specify Prompt

```text
/speckit-specify Nutze Lastenheft_Sandbox-Secure-Development-Selbstpruefung.md als verbindliche Eingabedatei. Erstelle die Feature-Spezifikation fuer eine Secure-Development-Selbstpruefung von absdd-image-sandbox.

Ziel: Pruefe, ob die Sandbox sicher genug gehaertet ist und gleichzeitig fuer Ausbildung, Spec Kit, KI-Agenten und MSL-basierte Entwicklung arbeitsfaehig bleibt.

Beruecksichtige:
- Richtlinie Sichere Entwicklung.
- CL_10 Sichere Entwicklungsumgebung.
- CL_12 Agentische KI in Sandbox-Umgebungen.
- Leitlinie_Sichere-Entwicklungs-Sandbox.md.
- MSL-Sprachen: Rust, Swift, C#, F#, Java, Kotlin, Scala, Go, Dart, Python, Ruby, JavaScript, TypeScript, Haskell, OCaml, Erlang, Elixir, Ada und SPARK.
- docs/security/sandbox-freigabe.md, sandbox-isolation.md, network-decision.md, ai-tools-inventory.md, SBOM-/Scan-Skripte und Compose-Dateien.
- Dokumentiere `Supported`, `Open` oder `N/A` pro Toolchain und Pruefpunkt.
```