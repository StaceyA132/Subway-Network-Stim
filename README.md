# Subway Network Simulation & Monitoring Dashboard

> **Python-based subway network simulation with real-time monitoring & fault injection**

## 📝 Project Overview
This repository contains a Python-based simulation of a subway network system. The simulation models a single track segment with switches, occupancy sensors, signal lights, and a moving train. It includes random fault injection for realistic MTA-like behavior, comprehensive logging, and an optional Tkinter-based dashboard for real-time visualization.

The project demonstrates modular software design, real-time simulation techniques, and GUI development in Python. It's suitable for learning about transit system operations, fault simulation, and monitoring dashboard development.

## 🚆 Key Features

- **Real-time train movement** – Single train moves along a track segment at configurable speed
- **Signal & switch control** – Signal lights (green/red) and track switches with position states
- **Occupancy sensors** – Detect when track segments are occupied by trains
- **Fault simulation** – Random signal failures and switch misalignments for realistic testing
- **Event logging** – Timestamped logging of all system events and alerts
- **Visual dashboard** – Tkinter-based GUI showing real-time status (optional, falls back to console)
- **Modular architecture** – Clean separation of track, train, signal, and dashboard components

## 🛠️ Technologies Used

- **Python 3.9+** – Core simulation logic and control
- **Tkinter** – GUI framework for the monitoring dashboard
- **Logging module** – Structured event logging with timestamps
- **Random** – Fault injection and behavioral simulation
- **Threading** – Background simulation updates for the GUI
- **Setuptools** – Package management and command-line entry points

## 🎯 Skills Demonstrated

- Object-oriented design for simulation components
- Real-time system simulation and state management
- GUI development with Tkinter
- Fault injection and error handling
- Modular package structure and Python packaging
- Version control with Git and GitHub

## 📁 Repository Structure
```
subway_sim/              # Main Python package
├── __init__.py          # Package initialization and run() export
├── main.py              # Entry point with simulation loop and dashboard integration
├── track.py             # TrackSegment, Switch, and OccupancySensor classes
├── train.py             # Train class with movement logic
├── signal.py            # Signal class with states and fault simulation
└── dashboard.py         # Tkinter GUI for real-time monitoring

setup.py                 # Package configuration with entry points
requirements.txt         # Dependency list (currently empty)
.gitignore              # Excludes venv and cache files
README.md               # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or later
- Tkinter (GUI library) - included with most Python installations, but on macOS may require: `brew install python-tk@3.9`

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/StaceyA132/Subway-Network-Stim.git
   cd "Subway Network Simulation & Monitoring Dashboard"
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the package in editable mode:
   ```sh
   pip install -e .
   ```

### Running the Simulation

Start the simulation with the visual dashboard:
```sh
subway-sim
```

Or run directly with Python:
```sh
python -m subway_sim
```

The simulation will:
- Launch a Tkinter window showing real-time status
- Run for ~20 seconds with random fault injection
- Log all events to the console
- Fall back to console-only mode if Tkinter is unavailable

### Alternative: Console Mode
If you prefer console output only, modify `subway_sim/main.py` to call `run_console()` instead of `run()`.

## 📊 Simulation Details

The current simulation includes:
- **Track Infrastructure**: Single 200m track segment with switch and occupancy sensor
- **Train**: Moves at 5 m/s, stops if signal is red
- **Signal**: Green/red states with random fault simulation (10% chance per second)
- **Switch**: Normal/diverted positions with random misalignment faults
- **Dashboard**: Real-time GUI updates showing all component states and event logs

## 🔄 Version Control
This project is hosted on GitHub at: https://github.com/StaceyA132/Subway-Network-Stim

All major features were developed incrementally and committed with descriptive messages, demonstrating proper Git workflow practices.

## 📚 Future Enhancements
The modular design makes it easy to extend with additional features:

- **Multiple Trains**: Add concurrent train movement and collision avoidance
- **Expanded Network**: Multiple track segments forming a complete subway line
- **Conflict Detection**: Advanced monitoring for occupancy conflicts and safety alerts
- **Web Dashboard**: Flask-based web interface for remote monitoring
- **Performance Metrics**: Speed tracking, delay analysis, and efficiency reports
- **Configuration Files**: JSON/YAML for customizable simulation parameters
- **Data Export**: CSV/JSON logs for analysis and visualization

## 🤝 Contributing
Feel free to fork the repository and submit pull requests for new features or improvements!

---

*Built with Python • Simulated with care • Monitored in real-time*

*README updated to reflect completed implementation*
