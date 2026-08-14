# Python und uv / Python and uv

## Einordnung / Context

**DE:** Python-Projekte liegen standardmäßig unter `/python-projects`. Das
Image enthält Python 3, virtuelle Umgebungen sowie die fest installierten
Werkzeuge `uv` und `uvx`. Anwendungsabhängigkeiten werden nicht global in das
Image installiert.

**EN:** Python projects normally live under `/python-projects`. The image
contains Python 3, virtual environments, and the pinned `uv` and `uvx` tools.
Application dependencies are not installed globally in the image.

## Projekt mit virtueller Umgebung / Project with a Virtual Environment

```bash
cd /python-projects
mkdir hello-sandbox
cd hello-sandbox
uv venv .venv
source .venv/bin/activate
python --version
```

Datei `hello.py` / File `hello.py`:

```python
def greeting(name: str) -> str:
    return f"Hallo, {name}!"


if __name__ == "__main__":
    print(greeting("Sandbox"))
```

```bash
python hello.py
deactivate
```

## Projektabhängigkeiten und Tests / Project Dependencies and Tests

**DE:** Bevorzuge bei einem vorhandenen Projekt dessen `pyproject.toml` und
Lock-Datei. Ein möglicher `uv`-Ablauf ist:

**EN:** For an existing project, prefer its `pyproject.toml` and lock file. A
possible `uv` workflow is:

```bash
uv sync
uv run python -m pytest
```

**DE:** Wenn das Projekt noch keinen Paketvertrag besitzt, dokumentiere zuerst,
ob `requirements.txt`, `pyproject.toml` oder ein anderes Format verwendet
werden soll. Installiere `pytest`, `pip-audit` oder Frameworks nur
projektlokal und mit einer nachvollziehbaren Version.

**EN:** If the project has no dependency contract yet, first document whether
it will use `requirements.txt`, `pyproject.toml`, or another format. Install
`pytest`, `pip-audit`, or frameworks only for the project and with a traceable
version.

## Grenzen / Limits

- **DE:** `.venv/`, Caches und generierte Dateien gehören in die
  projektspezifische `.gitignore`. **EN:** `.venv/`, caches, and generated
  files belong in the project's `.gitignore`.
- **DE:** `python` zeigt im Image auf Python 3. Prüfe trotzdem die Version,
  wenn das Projekt eine Mindestversion verlangt. **EN:** `python` points to
  Python 3 in the image. Still verify the version when the project requires a
  minimum.
- **DE:** Testdaten bleiben fiktiv und enthalten keine produktiven oder
  personenbezogenen Informationen. **EN:** Test data remains fictional and
  contains no production or personal information.

Zurück zum [Toolchain-Index](README.md). / Return to the
[toolchain index](README.md).
