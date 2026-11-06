"""Build README.md and banner.svg from the profile submodule (profile/dist/github/).

The courses block between <!-- COURSES:START --> and <!-- COURSES:END --> is kept from the current README.md:
the courses-links sync fills it in.

Usage: python3 scripts/build.py   (after `git submodule update --remote profile`)
"""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "profile/dist/github"
COURSES = re.compile(r"<!-- COURSES:START -->.*?<!-- COURSES:END -->", re.S)

readme = ROOT / "README.md"
courses = COURSES.search(readme.read_text()).group(0)
readme.write_text(COURSES.sub(lambda _: courses, (SOURCE / "README.md").read_text()))
shutil.copyfile(SOURCE / "banner.svg", ROOT / "banner.svg")
print(f"{readme}\n{ROOT / 'banner.svg'}")
