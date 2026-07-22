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
- OpenMV H7 camera module for vision/color detection.

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
| `pybricks/open_round.py` | Open Round template using gyro heading and ultrasonic distance correction |
| `pybricks/obstacle_course.py` | Obstacle Course template prepared for the final OpenMV obstacle strategy |
| `pybricks/README.md` | Pybricks setup, port constants, and tuning notes |
| `openmv/README.md` | OpenMV H7 vision module notes |
| `openmv/main.py` | OpenMV H7 camera code draft; publish after team review/testing |

## Presentation Status

- Motor and sensor ports are confirmed in `../schemes/port-map.md`.
- Steering sign and front safety stop are tested; steering center and wall-centering consistency remain tuning targets.
- Integrated gyro heading reset is documented; MadBoy-specific drift measurement remains a future calibration task.
- OpenMV H7 communicates with the SPIKE Prime Hub through UART on port C, using PUPRemote/LPF2 Python libraries in code.
- Open Challenge 3-lap behavior and Obstacle Challenge working status are documented in `../docs/tests.md`.

