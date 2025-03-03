# lazyfmri/__init__.py
from importlib.metadata import version

__version__ = version("cxutils")

# Now import core functionality (optional, but typical in __init__.py)
from . import optimal
from . import pycortex

__all__ = ["optimal", "pycortex"]
