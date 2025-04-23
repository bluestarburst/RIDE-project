# Donkeycar Bridge for CPM Lab

This project provides a bridge between the Donkeycar framework and the CPM Lab system, allowing Donkeycar-based vehicles (Python Raspberry Pi cars) to be controlled and visualized within the CPM Lab environment.

## Overview

The Donkeycar Bridge integrates the Donkeycar API with the CPM Lab's distributed control architecture, enabling:

1. **Control of Donkeycars** via CPM Lab's high-level controllers
2. **Visualization** of vehicle movement, control inputs, and camera feeds
3. **Parameter management** compatible with both CPM and Donkeycar systems
4. **Real-time data exchange** between CPM's C++ components and Donkeycar's Python API

## Key Components

### Core Bridge Components

- **DDS Bridge** (`src/dds_bridge.py`): Central communication module that translates between CPM's DDS messages and Donkeycar controls
- **Vehicle Adapter** (`src/vehicle_adapter.py`): Makes a Donkeycar appear as a CPM Lab vehicle
- **Parameter Config** (`src/parameter_config.py`): Sets up CPM parameters for Donkeycar vehicles
- **Visualizer** (`src/visualizer.py`): Sends visualization data to the Lab Control Center

### Visualization Components

- **LCC Integration** (`lcc_integration/`): C++ plugin for the Lab Control Center to display Donkeycar data
  - Camera feed visualization
  - Vehicle path visualization
  - Control input visualization (steering, throttle)

### Example Controllers

- **Circle Controller** (`examples/circle_controller.py`): Makes a Donkeycar drive in a circle
- **Figure Eight Controller** (`examples/figure_eight_controller.py`): Makes a Donkeycar follow a figure-eight trajectory

## Getting Started

### Prerequisites

- CPM Lab system installed and functional
- Donkeycar framework installed
- Raspberry Pi configured with Donkeycar firmware

### Installation

1. Ensure the CPM Lab system is installed and working
2. Install the Donkeycar framework: `pip install -e /path/to/donkeycar`
3. Install the gym-donkeycar package: `pip install -e /path/to/gym-donkeycar`
4. Install the donkeycar_bridge package: `pip install -e .`

### Building the Lab Control Center Integration

```bash
cd lcc_integration
mkdir build && cd build
cmake ..
make
sudo make install
```

### Usage

Start a Donkeycar with the CPM Lab system:

```bash
./launch.sh <vehicle_id> [car_path] [--figure-eight]
```

Options:
- `vehicle_id`: The ID to use for the vehicle in the CPM system
- `car_path`: (Optional) Path to a Donkeycar directory to load configuration from
- `--figure-eight`: (Optional) Use the figure-eight controller instead of the circle controller

## Implementation Status

### Completed Features

- [x] Core DDS bridge for communication between CPM and Donkeycar
- [x] Parameter configuration system for Donkeycar in CPM
- [x] Basic high-level controllers (circle, figure-eight)
- [x] Vehicle state visualization in CPM Lab Control Center
- [x] Camera feed visualization infrastructure
- [x] Position and trajectory visualization
- [x] Control input visualization (steering, throttle gauges)

### Features in Progress

- [ ] Full integration of the camera viewer with Lab Control Center's main UI
- [ ] Physical position tracking with indoor positioning system
- [ ] Error handling and recovery for communication failures
- [ ] Documentation of all API components

### Planned Future Enhancements

- [ ] 3D vehicle models for visualization
- [ ] Neural network visualization for autonomous driving models
- [ ] Multi-camera support
- [ ] Augmented reality overlay for detected objects and predicted paths
- [ ] Performance optimization for high-frequency control
- [ ] Support for multiple simultaneous Donkeycar vehicles
- [ ] Integration with CPM Lab's recording and replay functionality
- [ ] Web-based visualization and control interface

## Architecture

```
                     ┌───────────────┐
                     │   CPM Lab     │
                     │  Ecosystem    │
                     └───────┬───────┘
                             │ DDS
                             ▼
┌───────────────────────────────────────────────┐
│              Donkeycar Bridge                 │
├───────────────┬───────────────┬───────────────┤
│   DDS Bridge  │    Vehicle    │  Parameter    │
│               │    Adapter    │    Config     │
└───────┬───────┴───────┬───────┴───────┬───────┘
        │               │               │
        ▼               ▼               ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│   Donkeycar   │ │ High-Level    │ │ Visualization │
│      API      │ │ Controllers   │ │    System     │
└───────────────┘ └───────────────┘ └───────────────┘
```

## Integration with Lab Control Center

The visualization components integrate with the Lab Control Center through:

1. Vehicle path and position visualization using visualization commands
2. Control input visualization (steering, throttle) as screen overlays
3. Camera feed visualization via a custom QML component

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request

## License

This project is licensed under the same license as the CPM Lab system.

## Next Steps and Roadmap

### Short-term Goals

1. Complete the Lab Control Center integration for camera visualization
2. Add position tracking with indoor positioning system or visual SLAM
3. Improve error handling and system robustness
4. Add comprehensive API documentation

### Medium-term Goals

1. Implement advanced visualization features (3D models, neural network visualization)
2. Support multiple simultaneous Donkeycar vehicles
3. Add more sophisticated controllers and path planning

### Long-term Goals

1. Full integration with CPM Lab's recording and replay functionality
2. Advanced machine learning integration
3. Web-based visualization and control interface
4. Support for complex multi-vehicle scenarios

## Known Issues

- Position tracking currently relies on simulation rather than actual positioning data
- Camera visualization requires manual integration with Lab Control Center
- System startup order is important (Lab Control Center must be running first)
- Communication can be unreliable under heavy network load