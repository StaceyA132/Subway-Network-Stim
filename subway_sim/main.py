"""Simple CLI entry point for the subway simulator.

This module defines run() which currently only prints a placeholder message.
As the simulation is built out, this is where the main loop or Flask/Tk
application would be initialized.
"""

import logging

LOGGER = logging.getLogger(__name__)


def run():
    """Start the subway simulation.

    Currently this prints a message and returns.  Replace this stub with real
    simulation initialization when the core modules (train, track, signal, etc.)
    exist.
    """

    logging.basicConfig(level=logging.INFO)
    LOGGER.info("Starting subway network simulation (stub)")
    print("Simulation started - nothing to run yet.")


if __name__ == "__main__":
    run()
