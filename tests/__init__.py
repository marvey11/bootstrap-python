""" tests/__init__.py """

import sys
from pathlib import Path

# Since the discovery directory for unit tests is set to "./tests" underneath the base project path we only need to
# select the parent directory once even though this __init__.py file is one level further down in the directory
# structure.
SRC_PATH = str(Path(sys.path[0]) / "src")
print(SRC_PATH)
if SRC_PATH not in sys.path:
    sys.path.insert(1, SRC_PATH)
