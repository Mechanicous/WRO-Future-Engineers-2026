# Testing Workflow

Use this file to prove that the LEGO SPIKE Prime robot was tested and improved over time.

Internet-sourced reference values are summarized in `sensor-reference.md`. Team measurements should be recorded below and compared against those references.

## Test Log

| Date | Robot Version | Test | Result | Change Made |
| --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO |
| TODO | MadBoy | Open Challenge 3-lap run | Completes 3 laps | Continue tuning consistency |
| TODO | MadBoy | Ultrasonic 20 cm accuracy check | Left 20.5 cm, front 21.2 cm, right 20.1 cm | Retest front sensor and collect more distances |
| TODO | MadBoy | Front safety stop | Object at 10 cm; robot stopped at about 10 cm +/- 1 cm | Keep front stop threshold conservative |
| TODO | MadBoy | Steering center straight-run check | Robot drifts left or right depending on the last steering adjustment | Improve repeatable steering center reset/calibration |
| TODO | MadBoy | Steering sign test | When closer to the left wall, robot steers right/away from the wall | Keep `STEERING_SIGN = 1` |
| TODO | MadBoy | Wall-centering observation | Sometimes centered; sometimes closer to one wall than the other | Tune `SIDE_BALANCE_GAIN` and improve steering center reset |

## Recommended Tests

- Ultrasonic sensor accuracy test.
- Integrated gyro heading reset and drift test.
- OpenMV H7 red/green detection test.
- Front safety stop test.
- Steering center test.
- Steering sign test.
- Rear differential smoothness test.
- Straight-line wall-centering test.
- Corner behavior test.
- Open Challenge lap consistency test.
- Obstacle detection and avoidance test.
- Hub battery runtime test.
- Full three-minute run test.

## Metrics To Record

- Completed laps.
- Time per lap.
- Number of wall touches.
- Number of obstacle touches.
- Stop distance from obstacle.
- Average left/right distance error.
- Steering correction range.
- Differential gear smoothness and wheel slip.
- Gyro heading drift over time.
- OpenMV red/green classification accuracy.
- Hub battery state before and after run.
- Any manual interventions.

## Ultrasonic Accuracy

Reference target: LEGO lists the Technic Distance Sensor at 1-200 cm with +/- 1 cm accuracy. Pybricks learning material uses 40-2000 mm as the practical ultrasonic range, and the Pybricks API can return 2000 mm when no valid distance is measured.

| Date | Sensor | Actual Distance | Measured Distance | Error | Notes |
| --- | --- | ---: | ---: | ---: | --- |
| TODO | Left | 20.0 cm | 20.5 cm | +0.5 cm | Within +/- 1 cm reference target |
| TODO | Front | 20.0 cm | 21.2 cm | +1.2 cm | Slightly outside +/- 1 cm target; retest |
| TODO | Right | 20.0 cm | 20.1 cm | +0.1 cm | Within +/- 1 cm reference target |

## Gyro / IMU Tests

Reference note: no official universal SPIKE Prime gyro drift rate was found. Pybricks documents per-hub full-turn scale variation and supports `heading_correction`, so drift/heading error should be measured on this hub. As an internet-reported bad-case reference, a FIRST LEGO League forum post reported SPIKE Prime yaw drift as high as about 1 deg/s when the gyro was behaving incorrectly.

| Date | Robot Version | Test | Result | Notes |
| --- | --- | --- | --- | --- |
| TODO | TODO | Heading reset at start line | TODO | TODO |
| Internet reference | SPIKE Prime Hub | Bad-case drift report | Up to about 1 deg/s | Not measured on MadBoy; use only as conservative reference |
| TODO | MadBoy | Drift after 1 minute | TODO | Measure this robot before competition |
| TODO | MadBoy | Drift after 3 minutes | TODO | Measure this robot before competition |

## OpenMV H7 Vision Tests

| Date | Lighting | Target | Distance | Result | Notes |
| --- | --- | --- | ---: | --- | --- |
| TODO | TODO | Red obstacle | TODO | TODO | TODO |
| TODO | TODO | Green obstacle | TODO | TODO | TODO |

## Control Tuning Notes

| Date | Drive Power | Side Gain | Front Stop | Front Resume | Track Result | Notes |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TODO | TODO | TODO | TODO | TODO | TODO | TODO |

