#!/usr/bin/env python3

from pathlib import Path


PATCH = '''\

# Container patch: Windows/WSL bind mounts can reject metadata operations
# used by shutil.copy2/copytree. Spec Kit only needs file contents here.
def _container_copyfile_no_metadata(src, dst, *args, **kwargs):
    return shutil.copyfile(src, dst)


def _container_copystat_no_metadata(src, dst, *args, **kwargs):
    return None


_container_original_copytree = shutil.copytree


def _container_copytree_no_metadata(
    src,
    dst,
    symlinks=False,
    ignore=None,
    copy_function=None,
    ignore_dangling_symlinks=False,
    dirs_exist_ok=False,
):
    return _container_original_copytree(
        src,
        dst,
        symlinks=symlinks,
        ignore=ignore,
        copy_function=_container_copyfile_no_metadata,
        ignore_dangling_symlinks=ignore_dangling_symlinks,
        dirs_exist_ok=dirs_exist_ok,
    )


shutil.copy = _container_copyfile_no_metadata
shutil.copy2 = _container_copyfile_no_metadata
shutil.copymode = _container_copystat_no_metadata
shutil.copystat = _container_copystat_no_metadata
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
    patch_start = content.find("\n# Container patch: Windows/WSL bind mounts")
    if patch_start != -1:
        patch_end = content.find("\nimport json", patch_start)
        if patch_end == -1:
            raise SystemExit("existing container patch end not found")
        existing_patch = content[patch_start:patch_end]
        if (
            "def _container_copystat_no_metadata" in existing_patch
            and "def _container_copytree_no_metadata(\n    src," in existing_patch
        ):
            return
        target.write_text(content[:patch_start] + PATCH + content[patch_end:])
        return

    needle = "import shutil\n"
    if needle not in content:
        raise SystemExit("import shutil not found")

    target.write_text(content.replace(needle, needle + PATCH, 1))


if __name__ == "__main__":
    main()
