"""Train components for the subway simulation.

This module defines the Train class, which represents a subway train with
position, speed, and movement logic.
"""

import logging
import time

LOGGER = logging.getLogger(__name__)


class Train:
    """A subway train that moves along tracks."""

    def __init__(self, train_id: str, current_segment=None, speed: float = 10.0):
        self.train_id = train_id
        self.current_segment = current_segment
        self.speed = speed  # m/s
        self.position = 0.0  # position along current segment (0 to segment.length)
        self.direction = 1  # 1 for forward, -1 for backward

    def move(self, delta_time: float):
        """Update train position based on speed and time."""
        if not self.current_segment:
            LOGGER.warning(f"Train {self.train_id} has no segment!")
            return

        # Calculate new position
        delta_distance = self.speed * delta_time * self.direction
        new_position = self.position + delta_distance

        # Check bounds
        if new_position < 0:
            new_position = 0
            self.direction = 1  # reverse or stop?
            LOGGER.info(f"Train {self.train_id} reached start of segment")
        elif new_position > self.current_segment.length:
            new_position = self.current_segment.length
            self.direction = -1  # reverse
            LOGGER.info(f"Train {self.train_id} reached end of segment")

        self.position = new_position
        LOGGER.debug(f"Train {self.train_id} at position {self.position:.1f}m on {self.current_segment.segment_id}")

    def set_segment(self, segment):
        """Assign train to a new segment."""
        if self.current_segment:
            self.current_segment.vacate()
        self.current_segment = segment
        self.position = 0.0
        segment.occupy(self)
        LOGGER.info(f"Train {self.train_id} assigned to segment {segment.segment_id}")

    def __str__(self):
        segment_id = self.current_segment.segment_id if self.current_segment else "None"
        return f"Train({self.train_id}, segment={segment_id}, pos={self.position:.1f}m)"