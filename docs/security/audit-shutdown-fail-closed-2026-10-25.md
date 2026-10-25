# Audit-Stopp Bei Exportfehler Sperren / Block Shutdown on Export Failure

## Befund Und Behebung / Finding and Fix

DE: Das unabhaengige zweite Vollreview fand DOC-R12 (High): Beide bestehenden
Stopp-Wrapper setzten nach fehlgeschlagenem Audit-Export `compose down` fort,
auch bei Volume-Loeschung. Der genehmigte Plan erlaubt begrenzte Korrekturen
im referenzierten Sicherheitsweg mit erneuter unabhaengiger Pruefung.
Jetzt wird jeder Exportfehler unveraendert als Fehlercode zurueckgegeben,
bevor `down` erreicht wird. Das gilt auch fuer durchgereichte Argumente;
keine Option umgeht diese Sperre. Erst Exit 0 des Exports erlaubt `down`.
Ein Fehler von `down` bleibt ebenfalls als Exitcode sichtbar.

EN: The second independent full review found DOC-R12, High: both existing
shutdown wrappers continued to compose down after audit failure, including
volume removal. Bounded correction with independent re-review is within the
approved plan. Every export failure now propagates its error code before
down, including forwarded arguments. No option bypasses the stop. Only export
exit 0 permits down; a down error is propagated too.

## Nachweis / Evidence

DE: `scripts/tests/test_audit_shutdown_fail_closed.py` ruft die echten
Repo-Wrapper mit kuenstlichen Engines aus temporaeren Ordnern auf. Testfaelle:

EN: Tests invoke the real repository wrappers with fake engines in temporary
directories. Cases:

| Fall / Case | Erwartung / Expected result |
|---|---|
| Export Exit 7, Bash/PowerShell, podman/podman-compose, ohne und mit Volume-Optionen / with and without volume flags | genau ein Engine-Aufruf, nur Export, Exit 7 / one engine call only, export, exit 7 |
| Export Exit 0, gleiche Varianten / same variants | zuerst Export, dann down, Argumente erhalten / export then down, arguments retained |
| Export Exit 0, down Exit 11, beide Skriptsprachen / both script languages | Exit 11 bleibt erhalten / exit 11 retained |

DE: Drei Tests mit insgesamt 26 Unterfaellen. Kein echter Podman-Aufruf,
Container-Stopp oder Volume-Zugriff durch die Tests. Ein neues Pre-Commit-
Gate bindet Wrapper und Regression zusammen. Bash-/PowerShell-Syntax und
ShellCheck werden separat geprueft. Ausfuehrung auf macOS prueft die beiden
Skriptvarianten, nicht automatisch nativen Windows-/WSL2-Betrieb.

EN: Three tests contain 26 subcases, with no real Podman call, container stop
or volume access. A pre-commit gate binds the wrappers to regression tests.
Shell syntax and ShellCheck are separate checks. Running both script variants
on macOS does not prove native Windows/WSL2 operation.

## Grenzen Und Wiederanlauf / Limits and Restart

DE: Die Wrapper erhalten keine Erlaubnis, den Inhalt von Agentensitzungen
zu exportieren oder fehlende Nachweise zu erfinden. OpenCode-2-Abdeckung und
menschliche Freigaben bleiben im [Nachpruefungsregister](toolchain-followups-2026-10-25.md)
offen. Die Korrektur liegt im Repo; ein vorhandenes Image wird nicht neu
gebaut. Vor produktiver Verwendung sind Plattformnachweise erforderlich.

EN: Wrappers gain no authority to export session content or invent missing
evidence. OpenCode 2 coverage and human approval remain open in the register.
The fix is in repository sources; no existing image is rebuilt. Platform
evidence is required before production use.

DE: Ein erfolgreicher normaler Wrapper-Stopp fuehrt `down` ohne Volume-
Loeschung aus. Der naechste Tag darf daher einen Container aus dem vorhandenen
geprueften Image neu anlegen. [Alltag](../fuer-lernende/alltag.md) verwendet
`--no-build --no-recreate --pull never`: kein Neubau, kein Download und kein
Austausch eines noch vorhandenen Containers. Die erhaltenen benannten
Volumes werden wieder verbunden. Fehlende Images oder geaenderte
Konfigurationen sind zu klaeren, nicht durch Entfernen von Schutzoptionen
zu umgehen. Das korrigiert den Ablaufbefund DOC-R11.

EN: Normal successful shutdown runs down without volume deletion. The next
day can therefore create a container from the existing reviewed image. The
daily guide prevents builds, pulls and replacement of existing containers,
while reconnecting retained named volumes. Missing images or changed
configuration require clarification, not removal of safeguards. This corrects
workflow finding DOC-R11.
