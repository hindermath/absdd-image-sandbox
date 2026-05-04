#!/usr/bin/env python3

from pathlib import Path


PATCH = '''\

# Container patch: Windows/WSL bind mounts can reject metadata operations
# used by shutil.copy2/copytree. Spec Kit only needs file contents here.
def _container_copyfile_no_metadata(src, dst, *args, **kwargs):
    return shutil.copyfile(src, dst)


_container_original_copytree = shutil.copytree


def _container_copytree_no_metadata(src, dst, *args, **kwargs):
    kwargs["copy_function"] = _container_copyfile_no_metadata
    return _container_original_copytree(src, dst, *args, **kwargs)


shutil.copy = _container_copyfile_no_metadata
shutil.copy2 = _container_copyfile_no_metadata
shutil.copytree = _container_copytree_no_metadata
'''


def main() -> None:
    candidates = list(
        (Path.home() / ".local/share/uv/tools/specify-cli").glob(
            "lib/python*/site-packages/specify_cli/__init__.py"
        )
    )
    if not candidates:
        raise SystemExit("specify_cli/__init__.py not found")

    target = candidates[0]
    content = target.read_text()
    marker = "def _container_copyfile_no_metadata"
    if marker in content:
        return

    needle = "import shutil\n"
    if needle not in content:
        raise SystemExit("import shutil not found")

    target.write_text(content.replace(needle, needle + PATCH, 1))


if __name__ == "__main__":
    main()
