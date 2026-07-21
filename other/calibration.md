# Calibration Notes

Record the calibration procedure used before runs.

Reference sensor values from LEGO and Pybricks are summarized in `../docs/sensor-reference.md`.

## Pre-Run Power And Structure Check

- Charge the SPIKE Prime Hub battery to full.
- Check that all cables are connected firmly.
- Make sure the robot is steady and sturdy.
- Confirm that motors, ultrasonic sensors, OpenMV H7 camera, wheels, and gears are in place.
- Battery runtime note: the hub battery lasts a long time in team testing, but exact runtime has not been tracked yet.

## Steering Center

- Put the wheels straight before starting the program.
- The current Pybricks program resets the steering motor angle at startup.
- If the robot drifts, adjust the mechanical center first, then tune software constants.

| Date | Robot Version | Steering Center Method | Result | Notes |
| --- | --- | --- | --- | --- |
| 2026-07-21 | MadBoy | Center steering before straight run | Drifts left or right depending on the last steering adjustment | Needs repeatable centering reset/calibration before each run |

## Steering Direction

- Run at low speed.
- Place the robot closer to the left wall than the right wall.
- Confirm it steers away from the left wall.
- If it steers toward the wall, change `STEERING_SIGN` in `../src/pybricks/main.py`.

| Date | STEERING_SIGN | Result | Notes |
| --- | ---: | --- | --- |
| 2026-07-21 | 1 | Pass: closer to left wall makes robot steer right/away | Keep current sign unless linkage/code direction changes |

## Ultrasonic Sensors

- Verify that left, middle/front, and right sensors report fresh readings.
- Test readings at known distances such as 100 mm, 200 mm, 300 mm, and 500 mm.
- Test angled walls because ultrasonic reflections can change with angle.
- First target: stay within +/- 10 mm under controlled conditions, based on the LEGO Education +/- 1 cm distance sensor reference.

| Sensor | Actual Distance | Measured Distance | Error | Notes |
| --- | ---: | ---: | ---: | --- |
| Left | 20.0 cm | 20.5 cm | +0.5 cm | Within +/- 1 cm reference target |
| Middle/front | 20.0 cm | 21.2 cm | +1.2 cm | Slightly outside +/- 1 cm target; retest at more distances |
| Right | 20.0 cm | 20.1 cm | +0.1 cm | Within +/- 1 cm reference target |

## SPIKE Prime Integrated Gyro

- Place the robot flat on the field.
- The SPIKE Prime Hub is mounted lying flat, with the USB port facing the robot's left side.
- Align the robot to the known starting direction.
- Press the start button so the Pybricks program calls `hub.imu.reset_heading(0)`.
- Record heading drift while the robot is still and after driving.
- No official universal drift rate was found. Pybricks documents per-hub heading variation, and an internet user report describes bad-case SPIKE Prime yaw drift up to about 1 deg/s when the gyro behaves incorrectly. Measure this specific hub and document any `heading_correction` value.

| Date | Robot Version | Test | Result | Notes |
| --- | --- | --- | --- | --- |
| 2026-07-21 | MadBoy | Heading reset | Procedure documented | Hub lies flat with USB port facing left |
| Internet reference | SPIKE Prime Hub | Bad-case drift report | Up to about 1 deg/s | Not measured on MadBoy |
| Future measurement | MadBoy | Still drift test | Not measured yet | Measure before competition |
| Future measurement | MadBoy | Driving drift test | Not measured yet | Measure before competition |

## OpenMV H7 Vision

- Mount the camera at the documented height and angle.
- Calibrate red and green obstacle detection under field lighting.
- Record false positives and false negatives.
- Send OpenMV H7 data to the SPIKE Prime Hub using UART communication on port C; PUPRemote/LPF2 are the Python libraries used to package the messages.

| Date | Lighting | Target | Threshold/Model | Result | Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-07-21 | Team test lighting | Red obstacle | OpenMV color strategy | Detection/strategy working | Formal accuracy count still needed |
| 2026-07-21 | Team test lighting | Green obstacle | OpenMV color strategy | Detection/strategy working | Formal accuracy count still needed |

## Control Tuning

Record values and behavior after each tuning change.

| Date | DRIVE_POWER | SIDE_BALANCE_GAIN | FRONT_STOP_MM | FRONT_RESUME_MM | Test Result | Notes |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| 2026-07-21 | 35 | 0.18 | 180 mm | 260 mm | Sometimes centered; sometimes closer to one wall than the other | Tune side gain after steering center reset is more repeatable |

