# Source Code

This folder contains the robot control software.

## Arduino Sketch

`robot_controller_improved/robot_controller_improved.ino`

Keep the `.ino` file inside a folder with the same name so the Arduino IDE can open it correctly.

## Current Behavior

- Calibrates the BMI160 gyroscope at startup.
- Assigns unique addresses to three VL53L1X distance sensors.
- Tracks yaw by integrating gyroscope readings.
- Uses PID steering correction to hold the starting heading.
- Stops when the front sensor sees an obstacle closer than the configured threshold.

## Required Libraries

- `Wire`
- `BMI160Gen`
- `VL53L1X`
- `Servo`

## TODO

- Document the exact controller board.
- Document all pin mappings with a matching wiring diagram in `../schemes/`.
- Add OpenMV or camera communication if used.
- Add obstacle challenge state machine logic.
- Add tested PID values and tuning notes in `../docs/tests.md`.

