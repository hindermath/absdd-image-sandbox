# SysInfo: persönliches Praxispaket / Personal Practice Package

## Deutsch

Übernimm den Inhalt dieses Verzeichnisses in ein **leeres** persönliches Repo,
nicht in das Sandbox-Repo. Alle JSON-Pfade beginnen relativ zu diesem
Verzeichnis. Keine Dateien überschreiben. Vorher die SysInfo-Präsentation und
den Werkstättenindex lesen; anschließend eine der sechs Sprachen und den
Projekt-Mount festhalten. Erstelle darin deinen eigenen Hello-World-Starter.

Verbindlich ist [basis.md](basis.md). [Reihenansicht](order.md),
[Serienmanifest](specs/intake-series/learning/manifest.json) und
[Quellenbeleg](sources.json) gehören gemeinsam zum Paket. Letzterer bindet
beobachtete Referenzdateien, nicht deren historische Freigaben. Der neue
datensparsame Lernvertrag hat Vorrang vor unverändertem Referenzverhalten.

**Erster persönlicher Schritt nach der Übernahme:** Spec Kit und verfügbare
Intake-Presets kontrolliert vorbereiten, dann die ganze Serie prüfen lassen.
Im Agenten, nicht in einer Shell:

```text
$speckit-intake-review specs/intake-review-requests/learning.json
```

Das ist ein später selbst zu erteilender Auftrag. Es wurde kein Reviewlauf im
Lernrepo ausgeführt. `ReadyForReview`/`Enabled` in Authoring-Receipts sind keine
Startfreigabe; die Serie bleibt Draft und alle Stufen Pending. Nach fachlichem
Review und eigener Entscheidung den vorgesehenen Series-Update-Prozess für
Aktivierung und erste Eligible-Stufe nutzen. Folgeaufgaben bleiben bis zur
Abnahme des Vorgängers gesperrt; keine ausgelieferten Status hier fortschreiben.

**Validierung ohne Produktstart:** Im Sandbox-Checkout kann der Maintainer
die vorhandenen Authoring-/Serienvalidatoren mit `--repo` beziehungsweise
`-Repo` auf die Wurzel dieses Pakets richten. Das prüft Herkunft und Reihenfolge,
nicht die Anwendung. Im persönlichen Repo entsprechend dessen Wurzel angeben.

## English

Copy this directory's complete contents into an **empty personal repository**,
not the sandbox. JSON paths resolve from this directory. Never overwrite files.
Read the presentation/workshop index, choose one of six languages, record the
approved project mount and create your own Hello World starter.

Keep basis.md, order, manifest, receipts and sources together. Sources describe
observed reference revisions, not inherited approvals. The adapted privacy-first
contract takes precedence over unchanged reference behavior.

Prepare Spec Kit/presets deliberately, then issue the full-series review prompt
above inside the agent. Nothing has been reviewed/executed in your personal repo.
ReadyForReview/Enabled is not execution authority. Draft/Pending remain until
personal review, decision and governed activation. Accept predecessors before
progressing and keep personal statuses out of this distributed package.

Maintainers can run the existing receipt/series validators with this package
as explicit repository root. Such checks establish structure and provenance,
not a working or accepted product.
