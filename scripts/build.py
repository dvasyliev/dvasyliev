"""Build README.md and banner.svg from the profile submodule (profile/dist/dvasyliev/).

The courses section is part of that README, and its cards (profile/dist/dvasyliev/courses/) are copied to courses/.

Usage: python3 scripts/build.py   (after `git submodule update --remote profile`)
"""

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "profile/dist/dvasyliev"

shutil.copyfile(SOURCE / "README.md", ROOT / "README.md")
shutil.copyfile(SOURCE / "banner.svg", ROOT / "banner.svg")
shutil.copytree(SOURCE / "courses", ROOT / "courses", dirs_exist_ok=True)  # the course cards the README shows
print(f"{ROOT / 'README.md'}\n{ROOT / 'banner.svg'}\n{ROOT / 'courses'}")
