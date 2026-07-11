# Source Code

This folder contains the active robot software.

## Active Program

`pybricks/main.py`

The project now uses:

- LEGO SPIKE Prime Hub.
- Pybricks MicroPython.
- Three LEGO ultrasonic sensors:
  - Left.
  - Middle/front.
  - Right.

The old Arduino/BMI160/VL53L1X prototype is no longer active. It remains available in Git history for reference, but the repository documentation now follows the LEGO SPIKE Prime design.

## Current Behavior

- Initializes the SPIKE Prime Hub, rear-drive Large Angular Motor, steering Medium Angular Motor, and three ultrasonic sensors.
- Waits for the hub center button before driving.
- Stops when the middle/front ultrasonic sensor reports an unsafe distance.
- Uses left/right ultrasonic distance difference for starter wall-centering steering.
- Prints simple telemetry for tuning.

## Files

| File | Purpose |
| --- | --- |
| `pybricks/main.py` | Active robot program |
| `pybricks/README.md` | Pybricks setup, port constants, and tuning notes |

## TODO

- Confirm the exact motor ports and sensor ports in `../schemes/port-map.md`.
- Tune steering center, steering sign, drive power, and stop thresholds.
- Add final Open Challenge lap logic.
- Add final Obstacle Challenge strategy.
- Add tested values and run data in `../docs/tests.md`.

