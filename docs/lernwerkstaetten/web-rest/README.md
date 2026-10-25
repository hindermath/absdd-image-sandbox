# Web-Weg B: MVC plus REST / Web Route B: MVC plus REST

## Deutsch

Dieses eigenständige Paket baut eine C#-REST-API und danach einen getrennten
MVC-Client auf. Nur die API besitzt SQLite; der Browser erhält HTML von MVC.
Übernimm den gesamten Paketinhalt ohne Überschreiben in ein **leeres persönliches
Repo**. JSON-Pfade gelten ab dieser Wurzel. Präsentation und Werkstättenindex
zuerst lesen, Wahl B in [decision.md](decision.md) begründen und
[basis.md](basis.md) beachten. Ausgangspunkt ist ein eigener C#-Hello-World-Starter.

[Reihenansicht](order.md) und [Manifest](specs/intake-series/learning/manifest.json)
enthalten vier Pending-Stufen in einer Draft-Serie. Weg A ist keine
Vorbedingung und wird nicht mitkopiert oder als abgeschlossen markiert.
[Quellenbeleg](sources.json) bindet Referenzbeobachtungen und die bewusste
Anpassung an den Entwicklungscontainer. Er übernimmt keine Freigaben.

Nach kontrollierter Spec-Kit-/Preset-Vorbereitung und Entscheidung diesen
**Agentenauftrag**, keinen Shell-Befehl, selbst erteilen:

```text
$speckit-intake-review specs/intake-review-requests/learning.json
```

Vorhandene Authoring-Receipts und Enabled-Prompts sind weder Review noch
Ausführungsfreigabe. Nach aktuellem vollständigem Review lokal per Series-Update
aktivieren und erste Stufe ausdrücklich starten. Folgestufen brauchen
Vorgängerabnahme. Änderungen an Intakes verlangen archivierende Updates;
persönlichen Fortschritt nicht im verteilten Paket festhalten.

Maintainer nutzen vorhandene Bash-/PowerShell-Validatoren mit dieser Wurzel
als `--repo`/`-Repo`. Technisch gültige JSON-Artefakte sind keine Produktabnahme.

## English

Rebuild a C# REST API and then its separate server-side MVC client. Only the
API owns SQLite; the browser receives HTML. Copy the complete package into an
empty personal repo without overwrites. JSON resolves from this root. Read
the presentation/index, record route B and follow basis.md. Begin with Hello World.

The order/manifest contain four Pending stages in a Draft series. Route A is
not required or marked completed. Source evidence binds observations and
adaptations, not approvals. Private reference access is not required.

After deliberate Spec Kit/preset setup and decision, issue the full-series
review prompt above in the agent. Receipts/Enabled prompts grant no execution
authority. Following current full review, activate locally through Series
Update and explicitly start the first stage. Accept predecessors before moving
on. Adaptations need archived updates; personal progress stays in your repo.

Maintainers validate with the existing Bash/PowerShell tools and this package
as explicit root. Valid provenance/JSON does not establish product acceptance.
