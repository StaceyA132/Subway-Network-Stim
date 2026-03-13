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
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Track diagram canvas
        self.canvas = tk.Canvas(main_frame, width=600, height=300, bg='white')
        self.canvas.pack(pady=10)

        # Status frame
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=10)

        # Status labels
        self.train_label = ttk.Label(status_frame, text="Train: Loading...", font=("Arial", 10))
        self.train_label.pack(side=tk.LEFT, padx=10)

        self.signal_label = ttk.Label(status_frame, text="Signal: Loading...", font=("Arial", 10))
        self.signal_label.pack(side=tk.LEFT, padx=10)

        self.switch_label = ttk.Label(status_frame, text="Switch: Loading...", font=("Arial", 10))
        self.switch_label.pack(side=tk.LEFT, padx=10)

        # Alert frame with visual indicator
        alert_frame = ttk.Frame(main_frame)
        alert_frame.pack(fill=tk.X, pady=10)

        self.alert_canvas = tk.Canvas(alert_frame, width=20, height=20, bg='white')
        self.alert_canvas.pack(side=tk.LEFT, padx=5)

        self.alert_label = ttk.Label(alert_frame, text="Alerts: None", font=("Arial", 10), foreground="green")
        self.alert_label.pack(side=tk.LEFT)

        # Event log
        log_frame = ttk.Frame(main_frame)
        log_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(log_frame, text="Event Log:", font=("Arial", 10, "bold")).pack(anchor=tk.W)

        self.log_text = tk.Text(log_frame, height=8, width=80, font=("Courier", 9))
        scrollbar = ttk.Scrollbar(log_frame, command=self.log_text.yview)
        self.log_text.config(yscrollcommand=scrollbar.set)

        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Initialize canvas elements
        self._draw_track_diagram()

        # Components (will be set by simulation)
        self.segment = None
        self.switch = None
        self.train = None
        self.signal = None

        # Canvas items
        self.train_rect = None
        self.signal_circle = None
        self.switch_indicator = None

    def _draw_track_diagram(self):
        """Draw the initial track diagram."""
        # Main track line
        self.canvas.create_line(50, 150, 550, 150, width=4, fill='black', tags='track')

        # Switch diverging track
        self.canvas.create_line(300, 150, 350, 100, width=3, fill='gray', tags='switch_track')

        # Signal position (left side)
        self.canvas.create_oval(60, 130, 80, 170, fill='gray', outline='black', tags='signal_base')

        # Switch position indicator
        self.canvas.create_rectangle(290, 140, 310, 160, fill='green', tags='switch_indicator')

        # Train initial position
        self.train_rect = self.canvas.create_rectangle(45, 135, 55, 165, fill='blue', tags='train')

        # Signal light
        self.signal_circle = self.canvas.create_oval(60, 130, 80, 170, fill='green', tags='signal')

        # Labels
        self.canvas.create_text(300, 180, text="Main Track", font=("Arial", 10))
        self.canvas.create_text(350, 80, text="Switch Track", font=("Arial", 10))
        self.canvas.create_text(70, 190, text="Signal", font=("Arial", 10))
        self.canvas.create_text(300, 130, text="Switch", font=("Arial", 10))

    def update_status(self, train, signal, switch, alert="", log_message=""):
        """Update the dashboard labels and visuals."""
        self.train_label.config(text=f"Train: {train}")
        self.signal_label.config(text=f"Signal: {signal}")
        self.switch_label.config(text=f"Switch: {switch}")

        # Update alert
        if alert:
            self.alert_label.config(text=f"ALERT: {alert}", foreground="red")
            self.alert_canvas.config(bg='red')
        else:
            self.alert_label.config(text="Alerts: None", foreground="green")
            self.alert_canvas.config(bg='white')

        # Update visual elements
        if self.train:
            # Move train based on position (scale to canvas)
            track_length = 500  # pixels
            train_pos = (self.train.position / 200.0) * track_length + 50  # 200m track length
            self.canvas.coords(self.train_rect, train_pos-5, 135, train_pos+5, 165)

        if self.signal:
            # Update signal color
            if self.signal.faulty:
                color = 'yellow'  # Fault indicator
            elif self.signal.state == 'red':
                color = 'red'
            elif self.signal.state == 'yellow':
                color = 'yellow'
            else:  # green
                color = 'green'
            self.canvas.itemconfig(self.signal_circle, fill=color)

        if self.switch:
            # Update switch indicator
            color = 'green' if self.switch.position == 'straight' else 'orange'
            self.canvas.itemconfig(self.switch_indicator, fill=color)

        # Add to log if message provided
        if log_message:
            timestamp = time.strftime("%H:%M:%S")
            self.log_text.insert(tk.END, f"[{timestamp}] {log_message}\n")
            self.log_text.see(tk.END)

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
            log_msg = ""

            # Random faults
            if random.random() < 0.1:
                if random.choice([True, False]):
                    self.signal.simulate_fault()
                    alert = "Signal failure!"
                    log_msg = f"🚨 SIGNAL FAILURE: {self.signal}"
                else:
                    self.switch.set_position("diverted")
                    alert = "Switch misalignment!"
                    log_msg = f"🚨 SWITCH MISALIGNMENT: {self.switch}"

            # Move train
            old_pos = self.train.position
            self.train.move(1.0)
            new_pos = self.train.position

            # Check signal
            if not self.signal.allows_passage():
                alert = "Train stopped - signal red!"
                log_msg = f"🛑 TRAIN STOPPED: Signal is red at position {new_pos:.1f}m"

            # Log normal status occasionally
            if not log_msg and random.random() < 0.3:  # 30% chance to log status
                log_msg = f"📍 Train at {new_pos:.1f}m, Signal: {self.signal.state}, Switch: {self.switch.position}"

            # Update GUI (thread-safe via after)
            self.root.after(0, self.update_status, self.train, self.signal, self.switch, alert, log_msg)

            time.sleep(1)

        self.root.after(0, lambda: self.update_status(self.train, self.signal, self.switch, "Simulation Ended", "🏁 Simulation completed"))


def run_with_dashboard():
    """Run the simulation with Tkinter dashboard."""
    root = tk.Tk()
    dashboard = Dashboard(root)

    # Start simulation in thread
    sim_thread = threading.Thread(target=dashboard.run_simulation)
    sim_thread.start()

    root.mainloop()