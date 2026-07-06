# Build Instructions

Use this document to make the robot reproducible.

## Mechanical Assembly

TODO:

- Add chassis dimensions.
- Add motor and steering mounting steps.
- Add sensor mount positions.
- Link to files in `../models/`.

## Electronics

TODO:

- Add battery type and voltage.
- Add motor driver model.
- Add regulator details.
- Add controller board model.
- Link to wiring diagrams in `../schemes/`.

## Software Upload

1. Install the Arduino IDE.
2. Install the required libraries listed in `../src/README.md`.
3. Open `../src/robot_controller_improved/robot_controller_improved.ino`.
4. Select the correct board and port.
5. Confirm the sketch pin constants match the real wiring.
6. Upload the sketch.
7. Power-cycle the robot and keep it still during gyro calibration.

## Pre-Run Checklist

- [ ] Battery charged.
- [ ] Wheels and steering move freely.
- [ ] Motor direction is correct.
- [ ] Servo center is correct.
- [ ] Front, left, and right distance sensors report fresh readings.
- [ ] Gyroscope calibration completed while the robot was still.
- [ ] Emergency stop or safe shutdown procedure is known by the team.

