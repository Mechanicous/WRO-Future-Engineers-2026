# Calibration Notes

Record the calibration procedure used before runs.

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

| Sensor | Actual Distance | Measured Distance | Error | Notes |
| --- | ---: | ---: | ---: | --- |
| Left | TODO | TODO | TODO | TODO |
| Middle/front | TODO | TODO | TODO | TODO |
| Right | TODO | TODO | TODO | TODO |

## Control Tuning

Record values and behavior after each tuning change.

| Date | DRIVE_POWER | SIDE_BALANCE_GAIN | FRONT_STOP_MM | FRONT_RESUME_MM | Test Result | Notes |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TODO | TODO | TODO | TODO | TODO | TODO | TODO |

