# Web-Weg A: MVC / Web Route A: MVC

## Deutsch

Dieses eigenständige Paket baut eine C#-Webanwendung mit ASP.NET Core MVC,
Razor, EF Core und SQLite neu auf. Keine fachliche REST-API. Übernimm den
gesamten Inhalt in ein **leeres persönliches Repo**, ohne Dateien zu überschreiben.
Die JSON-Pfade gelten ab dieser Paketwurzel. Lies zuerst Präsentation und
Werkstättenindex, begründe die Wahl in [decision.md](decision.md) und beachte
[basis.md](basis.md). Ein C#-Hello-World-Starter genügt als Ausgangspunkt.

[order.md](order.md) und das [Manifest](specs/intake-series/learning/manifest.json)
zeigen vier Pending-Stufen in einer Draft-Serie. Der andere Web-Weg ist keine
Voraussetzung. Persönlicher Fortschritt und Freigaben gehören nur ins Lernrepo.
[sources.json](sources.json) enthält Herkunft und bewusste Anpassungen, keine
übernommenen Testerfolge oder Freigaben. Private Referenzzugänge sind nicht nötig.

Nach kontrollierter Spec-Kit-/Preset-Vorbereitung und ausgefüllter Entscheidung
den folgenden **Agentenauftrag** bewusst erteilen, nicht in die Shell kopieren:

```text
$speckit-intake-review specs/intake-review-requests/learning.json
```

Er prüft die gesamte Serie. Ein Authoring-Receipt oder vorhandener Prompt
ersetzt kein Review und keinen Startauftrag. Nach aktuellem Review die lokale
Aktivierung über Series-Update und erste Stufe gesondert genehmigen.
Nicht beide Web-Pakete in dasselbe Projekt überlagern. Bei späteren Anpassungen
Intake-/Series-Update mit Archivierung statt Hash-Edit verwenden.

Maintainer prüfen das Paket mit den bestehenden Bash-/PowerShell-Validatoren
und dieser Wurzel als `--repo`/`-Repo`. Strukturprüfung ist keine Produktabnahme.

## English

Rebuild a personal C# MVC/Razor/EF Core/SQLite app without a business REST API.
Copy the complete package into an empty repository without overwriting files.
JSON paths resolve from this package root. Read the presentation/index, record
decision.md and follow basis.md. Start from personal Hello World code.

Four stages are Pending, series Draft; route B is not required. Personal
progress belongs only in the learning repository. Sources record provenance
and adaptation, not inherited approval. No private reference access is required.

After careful Spec Kit/preset setup and the decision, deliberately issue the
full-series review prompt above in the agent. Authoring receipts are not reviews
or execution authority. Activate locally through governed Series Update only
after current review and a human start decision. Never overlay both routes.
Use archive-preserving updates for adaptations, not manual hash changes.

Existing Bash/PowerShell validators take this package as explicit repo root.
They check provenance/order, not working-product acceptance.
