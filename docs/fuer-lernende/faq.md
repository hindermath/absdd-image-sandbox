# Haeufige Fragen / Frequently Asked Questions

[Einstieg / Start](README.md)

## Wo Fuehre Ich Befehle Aus? / Where Do Commands Run?

**DE:** `podman compose ...` laeuft auf dem Host im Sandbox-Checkout.
Unter Windows ist das entweder PowerShell mit Windows-Podman oder Bash in
Ubuntu/WSL2 mit dessen eigenem Podman. Compiler, Agenten und `specify` laufen
im Container. Die Anleitung nennt Ausfuehrungsort und Shell. Pruefe `id` und
`pwd`, statt dich allein auf den Prompt zu verlassen.

**EN:** Run Podman Compose on the host in the sandbox checkout: either
Windows PowerShell with Windows Podman, or Ubuntu/WSL2 Bash with its own
Podman. Compilers, agents and specify run inside the container. Guides name
the location and shell. Check id and pwd rather than trusting the prompt.

## Brauche Ich Ein GitHub-Konto Oder Einen API-Key? / Do I Need GitHub or an API Key?

**DE:** Nicht fuer den grundlegenden Einstieg. Verwende deinen Fork oder das
institutionelle Git-Repo. GitHub ist nur fuer den direkten GitHub-Weg oder
optionales Copilot-Sign-in erforderlich. Compiler- und Dokumenttests brauchen
keinen KI-Provider. Reale Agentennutzung kann ein genehmigtes Konto und eigene
Anmeldung benoetigen; der Dispatcher umgeht das nicht.

**EN:** Not for the basic introduction. Use your fork or institutional Git
repository. GitHub is required only for the direct GitHub route or optional
Copilot sign-in. Compiler and documentation tests need no AI provider. Real
agent use may need an approved account and sign-in; the dispatcher bypasses
neither.

## Ist ein Template dasselbe wie ein Fork? / Is a Template the Same as a Fork?

**DE:** Nein. Ein Fork bleibt für Updates und Beiträge der Standard. Eine
Template-Kopie beginnt eine unabhängige Historie und ist für bewusst eigene
Sandboxes gedacht. Das [Profil](template-profil.md) ist vorbereitet, nicht
aktiviert. Ein hinzugefügtes `upstream` macht Historien nicht verwandt; alte
Reviews und Statistiken werden dadurch keine eigenen Nachweise. Für ein neues
SysInfo-/Web-Produkt ein leeres Repo und ein Lernpaket verwenden.

**EN:** No. Forks remain the maintenance/contribution default. Templates start
independent history; the profile is prepared, not enabled. Adding upstream
does not join histories or transfer approvals/statistics. Product exercises
still use empty repos plus one learning package.

## Wozu Dienen Die Zwei Env-Dateien? / Why Two Env Files?

**DE:** `.env` legt lokale Compose-Werte fest, besonders Host-Projektpfade.
`opencode.env` ist die optionale lokale Provider-Konfiguration; ohne Provider
bleibt die Vorlage unveraendert. Beide bleiben ungetrackt. Die Installation
erklaert ihre Anlage. Niemals Zugangsdaten in Shell-History, Issues oder
Beispielbefehle schreiben. Auch `config`-Ausgaben vor Weitergabe auf lokale
Pfade und selbst ergaenzte sensible Werte pruefen.

**EN:** `.env` holds local Compose values, especially host project paths.
`opencode.env` is optional local provider configuration; without a provider,
leave the template unchanged. Both remain untracked. Installation explains
creation. Never put credentials in shell history, issues or examples. Before
sharing config output, check for local paths and sensitive values you added.

## Wann Brauche Ich Einen Neubau? / When Must I Rebuild?

| Aenderung / Change | Konsequenz / Consequence |
|---|---|
| Projektdatei im Bind-Mount / project file in a bind mount | sofort im Container sichtbar / immediately visible in container |
| `.env`-Mount oder Compose-Wert / mount or Compose value | Container kontrolliert neu erstellen; kein Image-Neubau nur fuer Mounts / recreate container deliberately; mounts alone need no image rebuild |
| Dockerfile, installierte Werkzeuge oder hineinkopierte Datei / Dockerfile, installed tool or copied file | neues Image bauen und Container daraus neu erstellen / build a new image and recreate container from it |
| bestehender Container nur gestoppt / existing container only stopped | mit bestehendem Image wieder starten / restart using existing image |

**DE:** Ein `restart` uebernimmt keine neue Mount-Definition und kein neues
Image. Vor Neuerstellung Arbeit sichern und [Audit-Stopp](alltag.md) nutzen;
Volumes erhalten. Ein Neubau ist kein automatisches Update des laufenden
Containers. Maintainer pruefen Image-ID und Evidenz vor Austausch.

**EN:** Restart does not apply a new mount definition or image. Save work
and use audit shutdown before recreation; retain volumes. A rebuild does not
automatically update the running container. Maintainers check image identity
and evidence before replacement.

## Welche Daten Bleiben Erhalten? / Which Data Persists?

**DE:** Projekt-Mounts liegen auf dem Host. Benannte Volumes behalten unter
anderem Agentenzustaende und .NET-Build-Ausgaben. Sonstige beschreibbare
Container-Dateien koennen bei Neuerstellung verloren gehen; `/tmp` ist fuer
kurzlebige Tests. Stoppen ist nicht Loeschen. `down -v` und die Wrapper-Optionen
`-v` beziehungsweise `-Volumes` loeschen Volumes und koennen Anmeldungen
entfernen. Sie gehoeren nicht zum normalen Ende einer Lerneinheit.

**EN:** Project mounts live on the host. Named volumes retain agent state and
.NET build output. Other writable container files may disappear on recreation;
/tmp is for temporary tests. Stopping is not deletion. Volume-removal options
delete volumes and may remove sign-in state. They are not routine shutdown.

## Kann Die KI Meinen Host Beschaedigen? / Can AI Damage My Host?

**DE:** Die Sandbox begrenzt Rechte, ist aber keine absolute Schutzgarantie.
In beschreibbaren Mounts kann ein Agent echte Host-Dateien aendern oder
loeschen. Freigegebene Netzverbindungen koennen Daten uebertragen. Beschraenke
Mounts, nutze fiktive Daten und pruefe Auftraege sowie Aenderungen menschlich.

**EN:** The sandbox restricts rights but is not an absolute guarantee. An
agent can change or delete real host files in writable mounts. Allowed
network connections can transfer data. Limit mounts, use fictional data and
review tasks and changes yourself.

## Was Beweisen Gruene Tests? / What Do Passing Tests Prove?

**DE:** Nur die beschriebenen Checks fuer die genannte Version und Plattform.
ARM64 ist keine AMD64-Abnahme. Eine erzeugte PDF ist kein Nachweis der
PDF-Barrierefreiheit. Eine SBOM ist ein Komponentenverzeichnis, kein
Vulnerabilitaets- oder Freigabenachweis. Ein aktuelles Intake-Review bewertet
Anforderungen, nicht deren technische Erfuellung. Aktuelle Grenzen stehen
in den [Nachpruefungen](../security/toolchain-followups-2026-10-25.md).

**EN:** Only the stated checks for the named version and platform. ARM64 does
not prove AMD64. Creating a PDF does not prove PDF accessibility. An SBOM is
a component inventory, not vulnerability clearance or approval. An intake
review assesses requirements, not their technical fulfillment. See the
follow-ups for current limits.

## Wie Melde Ich Einen Fehler? / How Do I Report a Problem?

**DE:** Notiere Betriebssystem, Architektur, Shell, Image-ID, betroffenen
Schritt, bereinigten Befehl, Exitcode sowie erwartetes und beobachtetes
Ergebnis. Entferne Namen, private Pfade, Tokens und Inhalte aus Prompts oder
Sitzungen. Nicht ganze Env-Dateien oder Agenten-Datenbanken hochladen.
Bei Verdacht auf ein Secret nicht weiter verteilen, sondern die verantwortliche
Person informieren. Danach hilft [Troubleshooting](troubleshooting.md).

**EN:** Record OS, architecture, shell, image ID, failing step, sanitised
command, exit code, expected and observed result. Remove names, private paths,
tokens and prompt/session content. Do not upload entire env files or agent
databases. If a secret may be exposed, stop sharing and inform the responsible
person. Then use troubleshooting.
