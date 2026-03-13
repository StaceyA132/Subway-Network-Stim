"""Top-level package for the subway network simulation.

This module exposes a simple entry point to start the simulation.  Actual
components (signals, tracks, trains, etc.) should be implemented in their
own submodules; they are imported lazily to avoid circular dependencies during
initialization.

Example usage::

    from subway_sim import run
    run()
"""

__version__ = "0.1.0"

from .main import run  # re-export for convenience

# When the package is imported, nothing else is executed.
