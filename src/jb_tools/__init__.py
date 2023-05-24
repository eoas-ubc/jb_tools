from pathlib import Path

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("jb_tools")
except PackageNotFoundError:
    __version__ = "unknown version"

try:
    from ._version import version_tuple
except ImportError:
    version_tuple = (0, 0, "unknown version")

print("in jb_tools init")

