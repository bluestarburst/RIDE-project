"""
Simplified simulation configuration for Donkeycar Bridge
This configuration allows running the donkeycar interface without
requiring the full CPM Lab components and RTI Connext DDS license
"""

# Simulation parameters
SIMULATION_MODE = True

# Vehicle configuration
VEHICLE_ID = 1
MAX_SPEED = 1.0  # m/s
MAX_STEERING_ANGLE = 30.0  # degrees

# Track configuration 
TRACK_WIDTH = 2.0  # meters
TRACK_LENGTH = 10.0  # meters

# Controller options
CONTROLLER_TYPE = "circle"  # or "figure-eight"
CONTROLLER_FREQUENCY = 10  # Hz

# Basic donkeycar configuration
DONKEY_CONFIG = {
    'DRIVE_LOOP_HZ': 20,
    'CAMERA_RESOLUTION': (120, 160),
    'CAMERA_FRAMERATE': 20,
    'STEERING_CHANNEL': 1,
    'THROTTLE_CHANNEL': 0,
    'STEERING_LEFT_PWM': 460,
    'STEERING_RIGHT_PWM': 290,
    'THROTTLE_FORWARD_PWM': 500,
    'THROTTLE_STOPPED_PWM': 370,
    'THROTTLE_REVERSE_PWM': 220,
}