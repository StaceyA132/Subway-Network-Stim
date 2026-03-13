"""Executable module for running the simulation with ``python -m subway_sim``.

This simply proxies to :func:`subway_sim.main.run` so that the package can be
executed as a module.
"""

from .main import run


if __name__ == "__main__":
    run()
