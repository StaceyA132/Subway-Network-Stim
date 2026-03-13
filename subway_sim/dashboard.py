"""Dashboard for the subway simulation using Tkinter.

Displays train positions, signal states, and alerts in a GUI window.
"""

import tkinter as tk
from tkinter import ttk
import threading
import time

from .track import TrackSegment, Switch
from .train import Train
from .signal import Signal


class Dashboard:
    """Tkinter-based dashboard for monitoring the simulation."""

    def __init__(self, root):
        self.root = root
        self.root.title("Subway Network Dashboard")
        self.root.geometry("600x400")

        # Labels for status
        self.train_label = ttk.Label(root, text="Train: Loading...", font=("Arial", 12))
        self.train_label.pack(pady=10)

        self.signal_label = ttk.Label(root, text="Signal: Loading...", font=("Arial", 12))
        self.signal_label.pack(pady=10)

        self.switch_label = ttk.Label(root, text="Switch: Loading...", font=("Arial", 12))
        self.switch_label.pack(pady=10)

        self.alert_label = ttk.Label(root, text="Alerts: None", font=("Arial", 12), foreground="red")
        self.alert_label.pack(pady=10)

        # Components (will be set by simulation)
        self.segment = None
        self.switch = None
        self.train = None
        self.signal = None

    def update_status(self, train, signal, switch, alert=""):
        """Update the dashboard labels."""
        self.train_label.config(text=f"Train: {train}")
        self.signal_label.config(text=f"Signal: {signal}")
        self.switch_label.config(text=f"Switch: {switch}")
        if alert:
            self.alert_label.config(text=f"ALERT: {alert}")
        else:
            self.alert_label.config(text="Alerts: None")

    def run_simulation(self):
        """Run the simulation in a separate thread to avoid blocking GUI."""
        import logging
        import random

        logging.basicConfig(level=logging.INFO)
        LOGGER = logging.getLogger(__name__)

        # Create components
        self.segment = TrackSegment("A1", length=200.0)
        self.switch = Switch("SW1")
        self.train = Train("T001", speed=5.0)
        self.signal = Signal("S1", initial_state="green")

        self.train.set_segment(self.segment)

        duration = 30  # longer for demo
        start_time = time.time()

        while time.time() - start_time < duration:
            alert = ""

            # Random faults
            if random.random() < 0.1:
                if random.choice([True, False]):
                    self.signal.simulate_fault()
                    alert = "Signal failure!"
                else:
                    self.switch.set_position("diverted")
                    alert = "Switch misalignment!"

            # Move train
            self.train.move(1.0)

            # Check signal
            if not self.signal.allows_passage():
                alert = "Train stopped - signal red!"

            # Update GUI (thread-safe via after)
            self.root.after(0, self.update_status, self.train, self.signal, self.switch, alert)

            time.sleep(1)

        self.root.after(0, lambda: self.alert_label.config(text="Simulation Ended"))


def run_with_dashboard():
    """Run the simulation with Tkinter dashboard."""
    root = tk.Tk()
    dashboard = Dashboard(root)

    # Start simulation in thread
    sim_thread = threading.Thread(target=dashboard.run_simulation)
    sim_thread.start()

    root.mainloop()