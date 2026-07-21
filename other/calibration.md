# Calibration Notes

Record the calibration procedure used before runs.

Reference sensor values from LEGO and Pybricks are summarized in `../docs/sensor-reference.md`.

## Pre-Run Power And Structure Check

- Charge the SPIKE Prime Hub battery to full.
- Check that all cables are connected firmly.
- Make sure the robot is steady and sturdy.
- Confirm that motors, ultrasonic sensors, OpenMV H7 camera, wheels, and gears are in place.

## Steering Center

- Put the wheels straight before starting the program.
- The current Pybricks program resets the steering motor angle at startup.
- If the robot drifts, adjust the mechanical center first, then tune software constants.

| Date | Robot Version | Steering Center Method | Result | Notes |
| --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO |

## Steering Direction

- Run at low speed.
- Place the robot closer to the left wall than the right wall.
- Confirm it steers away from the left wall.
- If it steers toward the wall, change `STEERING_SIGN` in `../src/pybricks/main.py`.

| Date | STEERING_SIGN | Result | Notes |
| --- | ---: | --- | --- |
| TODO | TODO | TODO | TODO |

## Ultrasonic Sensors

- Verify that left, middle/front, and right sensors report fresh readings.
- Test readings at known distances such as 100 mm, 200 mm, 300 mm, and 500 mm.
- Test angled walls because ultrasonic reflections can change with angle.
- First target: stay within +/- 10 mm under controlled conditions, based on the LEGO Education +/- 1 cm distance sensor reference.

| Sensor | Actual Distance | Measured Distance | Error | Notes |
| --- | ---: | ---: | ---: | --- |
| Left | TODO | TODO | TODO | TODO |
| Middle/front | TODO | TODO | TODO | TODO |
| Right | TODO | TODO | TODO | TODO |

## SPIKE Prime Integrated Gyro

- Place the robot flat on the field.
- The SPIKE Prime Hub is mounted lying flat, with the USB port facing the robot's left side.
- Align the robot to the known starting direction.
- Press the start button so the Pybricks program calls `hub.imu.reset_heading(0)`.
- Record heading drift while the robot is still and after driving.
- No universal drift rate was found in official docs; measure this specific hub and document any `heading_correction` value.

| Date | Robot Version | Test | Result | Notes |
| --- | --- | --- | --- | --- |
| TODO | TODO | Heading reset | TODO | TODO |
| TODO | TODO | Still drift test | TODO | TODO |
| TODO | TODO | Driving drift test | TODO | TODO |

## OpenMV H7 Vision

- Mount the camera at the documented height and angle.
- Calibrate red and green obstacle detection under field lighting.
- Record false positives and false negatives.
- Document the message sent from OpenMV H7 to the main robot logic.

| Date | Lighting | Target | Threshold/Model | Result | Notes |
| --- | --- | --- | --- | --- | --- |
| TODO | TODO | Red obstacle | TODO | TODO | TODO |
| TODO | TODO | Green obstacle | TODO | TODO | TODO |

## Control Tuning

Record values and behavior after each tuning change.

| Date | DRIVE_POWER | SIDE_BALANCE_GAIN | FRONT_STOP_MM | FRONT_RESUME_MM | Test Result | Notes |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TODO | TODO | TODO | TODO | TODO | TODO | TODO |

