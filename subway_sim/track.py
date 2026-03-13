"""Track components for the subway simulation.

This module defines classes for track segments, switches, and occupancy sensors.
Tracks form the physical layout of the subway network.
"""

import logging

LOGGER = logging.getLogger(__name__)


class TrackSegment:
    """A basic track segment with occupancy detection."""

    def __init__(self, segment_id: str, length: float = 100.0):
        self.segment_id = segment_id
        self.length = length  # meters
        self.occupied = False
        self.occupying_train = None

    def occupy(self, train):
        """Mark segment as occupied by a train."""
        if self.occupied:
            LOGGER.warning(f"Segment {self.segment_id} already occupied!")
            return False
        self.occupied = True
        self.occupying_train = train
        LOGGER.info(f"Segment {self.segment_id} occupied by train {train.train_id}")
        return True

    def vacate(self):
        """Mark segment as free."""
        if not self.occupied:
            LOGGER.warning(f"Segment {self.segment_id} not occupied!")
            return
        self.occupied = False
        self.occupying_train = None
        LOGGER.info(f"Segment {self.segment_id} vacated")

    def __str__(self):
        return f"TrackSegment({self.segment_id}, occupied={self.occupied})"


class Switch:
    """A track switch (point) that can route trains."""

    def __init__(self, switch_id: str):
        self.switch_id = switch_id
        self.position = "straight"  # "straight" or "diverted"

    def set_position(self, position: str):
        """Set switch position."""
        if position not in ["straight", "diverted"]:
            raise ValueError("Position must be 'straight' or 'diverted'")
        self.position = position
        LOGGER.info(f"Switch {self.switch_id} set to {position}")

    def __str__(self):
        return f"Switch({self.switch_id}, position={self.position})"


class OccupancySensor:
    """Sensor that detects train presence on a track segment."""

    def __init__(self, sensor_id: str, segment: TrackSegment):
        self.sensor_id = sensor_id
        self.segment = segment

    def detect(self):
        """Check if segment is occupied."""
        return self.segment.occupied

    def __str__(self):
        return f"OccupancySensor({self.sensor_id}, segment={self.segment.segment_id})"
