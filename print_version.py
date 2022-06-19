from pathlib import Path

from setuptools_scm import get_version

root_dir = Path().resolve()
print(f"{root_dir=}")
git_version = get_version(root=str(root_dir))
print(f"{git_version=}")
