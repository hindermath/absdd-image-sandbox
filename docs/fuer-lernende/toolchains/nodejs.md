# Node.js und npm / Node.js and npm

## Einordnung / Context

**DE:** Node.js und npm sind im Image vorhanden, weil Agenten-CLIs und manche
Projektwerkzeuge sie benötigen. Für allgemeine Node.js-Projekte existiert kein
eigener Standard-Mount. Verwende `/workspace` oder einen ausdrücklich
konfigurierten Projekt-Mount. Abhängigkeiten gehören in `package.json` und die
Lock-Datei des Projekts.

**EN:** Node.js and npm are present because agent CLIs and some project tools
need them. There is no dedicated default mount for general Node.js projects.
Use `/workspace` or an explicitly configured project mount. Dependencies
belong in the project's `package.json` and lock file.

## Kleines Projekt / Small Project

```bash
cd /workspace
mkdir node-sandbox
cd node-sandbox
npm init --yes
```

Datei `math.js` / File `math.js`:

```javascript
export function add(left, right) {
  return left + right;
}
```

Datei `math.test.js` / File `math.test.js`:

```javascript
import assert from "node:assert/strict";
import test from "node:test";
import { add } from "./math.js";

test("adds two values", () => {
  assert.equal(add(2, 2), 4);
});
```

**DE:** Ergänze in `package.json` den Eintrag `"type": "module"` und führe
den eingebauten Test-Runner aus:

**EN:** Add `"type": "module"` to `package.json` and run the built-in test
runner:

```bash
node --test
npm --version
```

## Abhängigkeiten und Grenzen / Dependencies and Limits

- **DE:** Nutze `npm ci`, wenn eine gültige `package-lock.json` vorhanden ist;
  der Befehl installiert exakt daraus. **EN:** Use `npm ci` when a valid
  `package-lock.json` exists; it installs exactly from that file.
- **DE:** TypeScript, Frameworks und projektspezifische CLIs sind nicht als
  globale Werkzeuge garantiert. Installiere sie im Projekt. **EN:** TypeScript,
  frameworks, and project-specific CLIs are not guaranteed globally. Install
  them in the project.
- **DE:** `node_modules/` bleibt ungetrackt. Prüfe neue Installationsskripte
  und Paketquellen vor der Ausführung. **EN:** Keep `node_modules/` untracked.
  Review new install scripts and package sources before execution.
- **DE:** Aktualisiere global installierte Agenten-CLIs nicht mit `npm` im
  laufenden Container; ihre Versionen werden im Dockerfile gepflegt. **EN:** Do
  not update globally installed agent CLIs with `npm` inside the running
  container; their versions are maintained in the Dockerfile.

Zurück zum [Toolchain-Index](README.md). / Return to the
[toolchain index](README.md).
