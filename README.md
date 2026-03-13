# Subway Network Simulation & Monitoring Dashboard

> **Small-scale transit simulation with real-time monitoring & alerts**

## 📝 Project Overview
This repository contains a Python-based simulation of a subway network. The system models multiple lines, stations, trains, signal lights, switches, and occupancy sensors. It runs as a real‑time emulator, continuously updating train positions and infrastructure status, and includes mechanisms for fault injection, conflict detection, logging, and visualization.

Developers and engineers can use the simulation to study operations, exercise monitoring dashboards, and verify alert logic before deploying to physical or larger‑scale systems.

## 🚆 Key Features

- **Real‑time train movement** – Trains progress along predefined routes on simulated schedules.
- **Signal & switch monitoring** – Track state of lights and point devices; support simulated failures and misalignments.
- **Occupancy conflict detection** – Automatically identify when two trains would occupy the same track segment.
- **Event logging** – Every state change, fault, and alert is timestamped for post‑analysis or audit.
- **Dashboard visualization** – Console or web‑based interface (via Flask/Tkinter) displaying network state and active alerts.

## 🛠️ Technologies Used

- **Python** – Core simulation logic and control.
- **Logging module** – Timestamped, leveled event output.
- **Random/Simulation logic** – Behavioral modeling and fault injection.
- **Matplotlib** *(optional)* – Plotting of network status or train trajectories.
- **Flask / Tkinter** *(optional)* – Dashboard front‑end for real‑time display.

## 🎯 Skills Demonstrated

- System‑level simulation of electronics and operations
- Real‑time monitoring & alert generation
- Software/hardware integration patterns
- Data logging and visualization for operational analysis

## 📁 Repository Structure
```
subway_sim/          # Python package for simulation components
  __init__.py        # package initializer
  signal.py          # signal light classes and logic
  track.py           # track segments, switches, occupancy sensors
  train.py           # train movement and routing
  monitor.py         # conflict detection and alerting
  dashboard.py       # optional visualization code
```

*(Note: the files above are placeholders; populate them as the simulation grows.)*

## 🚀 Getting Started
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv && source venv/bin/activate`.
3. Install dependencies (if any) listed in `requirements.txt` or install the
  package in editable mode:

  ```sh
  pip install -e .
  ```

4. Start the simulation:

  ```sh
  # using the installed package
  subway-sim

  # or via the module runner
  python -m subway_sim
  ```

  Both commands invoke the `run()` stub currently defined in
  `subway_sim/main.py`.

## 📚 Further Development
Future enhancements could include:

- WebSocket integration for continuous dashboard updates
- A REST API for external control or data extraction
- Expanded fault models and performance metrics
- Exportable logs for offline visualization

---

Feel free to explore and extend the simulation for research, teaching, or hobby projects! 

*– README generated based on project description provided by user.*
