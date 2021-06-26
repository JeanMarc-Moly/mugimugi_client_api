#!./.venv/bin/python

from enum import Enum
from pathlib import Path
from sys import argv, exit


class BumpType(Enum):
    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"


try:
    bump = BumpType(argv[1])
except IndexError:
    print(f"Missing bump type, try: {', '.join(t.value for t in BumpType)}")
    exit(1)
except ValueError:
    print(f"Invalid bump type {argv[1]!r}, try: {', '.join(t.value for t in BumpType)}")
    exit(1)

with (Path(__file__).resolve().parents[1] / "VERSION").open(
    mode="r+", encoding="utf-8"
) as f:
    major, minor, patch = f.readline().split(".")
    f.seek(0)
    version = (
        f"{int(major)+1}.0.0"
        if bump is BumpType.MAJOR
        else f"{major}.{int(minor)+1}.0"
        if bump is BumpType.MINOR
        else f"{major}.{minor}.{int(patch)+1}"
    )
    f.write(version)
exit(version)
