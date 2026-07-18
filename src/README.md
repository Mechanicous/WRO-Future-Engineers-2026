# Source Code

This folder contains the active robot software.

## Active Program

`pybricks/main.py`

The project now uses:

- LEGO SPIKE Prime Hub.
- Pybricks MicroPython.
- LEGO SPIKE Prime integrated gyro/IMU for heading feedback.
- Three LEGO ultrasonic sensors:
  - Left.
  - Middle/front.
  - Right.
- OpenMV H7 camera module for future vision/color detection.

The old Arduino/BMI160/VL53L1X prototype is no longer active. It remains available in Git history for reference, but the repository documentation now follows the LEGO SPIKE Prime design.

## Current Behavior

- Initializes the SPIKE Prime Hub, rear-drive Large Angular Motor, steering Medium Angular Motor, and three ultrasonic sensors.
- Resets and reports the SPIKE Prime integrated gyro heading.
- Waits for the hub center button before driving.
- Stops when the middle/front ultrasonic sensor reports an unsafe distance.
- Completes 3 laps in the Open Challenge round.
- Uses left/right ultrasonic distance difference for wall-centering steering.
- Prints simple telemetry for tuning.

## Files

| File | Purpose |
| --- | --- |
| `pybricks/main.py` | Active robot program |
| `pybricks/README.md` | Pybricks setup, port constants, and tuning notes |
| `openmv/README.md` | Planned OpenMV H7 vision module notes |
| `openmv/main.py` | Placeholder for future OpenMV H7 code |

## TODO

- Confirm the exact motor ports and sensor ports in `../schemes/port-map.md`.
- Tune steering center, steering sign, drive power, and stop thresholds.
- Test integrated gyro heading reset and drift.
- Decide and document how the OpenMV H7 communicates with the SPIKE Prime robot.
- Improve and document Open Challenge lap counting details.
- Add final Obstacle Challenge strategy.
- Add tested values and run data in `../docs/tests.md`.

