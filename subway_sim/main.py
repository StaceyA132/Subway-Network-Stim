"""Simple CLI entry point for the subway simulator.

This module defines run() which sets up a basic simulation with tracks, trains, and signals.
"""

import logging
import time

from .track import TrackSegment
from .train import Train
from .signal import Signal

LOGGER = logging.getLogger(__name__)


def run():
    """Start the subway simulation.

    Sets up a simple network and runs a basic simulation loop.
    """

    logging.basicConfig(level=logging.INFO)

    LOGGER.info("Starting subway network simulation")

    # Create components
    segment = TrackSegment("A1", length=200.0)
    train = Train("T001", speed=5.0)  # 5 m/s
    signal = Signal("S1", initial_state="green")

    # Assign train to segment
    train.set_segment(segment)

    # Simulation loop
    duration = 10  # seconds
    start_time = time.time()

    while time.time() - start_time < duration:
        # Move train
        train.move(1.0)  # move for 1 second

        # Check signal
        if not signal.allows_passage():
            LOGGER.warning("Train cannot proceed - signal is red!")
            break

        # Log status
        LOGGER.info(f"Status: {train} | {signal}")

        time.sleep(1)  # real-time delay

    LOGGER.info("Simulation ended")


if __name__ == "__main__":
    run()
