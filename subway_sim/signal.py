"""Signal components for the subway simulation.

This module defines signal lights that control train movement.
"""

import logging

LOGGER = logging.getLogger(__name__)


class Signal:
    """A signal light with states: red, yellow, green."""

    def __init__(self, signal_id: str, initial_state: str = "red"):
        self.signal_id = signal_id
        self.state = initial_state  # "red", "yellow", "green"
        self.faulty = False

    def set_state(self, state: str):
        """Set signal state."""
        if state not in ["red", "yellow", "green"]:
            raise ValueError("State must be 'red', 'yellow', or 'green'")
        if self.faulty:
            LOGGER.warning(f"Signal {self.signal_id} is faulty, cannot change state")
            return
        self.state = state
        LOGGER.info(f"Signal {self.signal_id} set to {state}")

    def simulate_fault(self):
        """Simulate a signal failure."""
        self.faulty = True
        self.state = "red"  # default to red on fault
        LOGGER.warning(f"Signal {self.signal_id} failed!")

    def repair(self):
        """Repair the signal."""
        self.faulty = False
        LOGGER.info(f"Signal {self.signal_id} repaired")

    def allows_passage(self):
        """Check if signal allows train passage."""
        return self.state == "green" and not self.faulty

    def __str__(self):
        return f"Signal({self.signal_id}, state={self.state}, faulty={self.faulty})"