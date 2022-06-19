from setuptools_scm import get_version
from pathlib import Path
root_dir = Path().resolve()
print(f"{root_dir=}")
code_dir= root_dir / 'src/jbscripts'
git_version = get_version(root=str(root_dir))
print(f"{git_version=}")
version_file = code_dir / 'VERSION.txt'
with open(version_file,'w') as outfile:
    outfile.write(f"{git_version}\n")
print((f"wrote new version number {git_version=}\n"
       f"into file {str(version_file.resolve())}"))


