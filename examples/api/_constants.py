"""Import test constants for examples."""
import sys
from pathlib import Path

# Add tests directory to path for importing constants
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tests"))

from constants import *  # noqa: F401, F403, E402
