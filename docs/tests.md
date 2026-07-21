# Testing Workflow

Use this file to prove that the LEGO SPIKE Prime robot was tested and improved over time.

Internet-sourced reference values are summarized in `sensor-reference.md`. Team measurements should be recorded below and compared against those references.

## Test Log

| Date | Robot Version | Test | Result | Change Made |
| --- | --- | --- | --- | --- |
| 2026-07-21 | MadBoy | Open Challenge 3-lap run | Completes 3 laps | Continue tuning consistency |
| 2026-07-21 | MadBoy | Ultrasonic 20 cm accuracy check | Left 20.5 cm, front 21.2 cm, right 20.1 cm | Retest front sensor and collect more distances |
| 2026-07-21 | MadBoy | Front safety stop | Object at 10 cm; robot stopped at about 10 cm +/- 1 cm | Keep front stop threshold conservative |
| 2026-07-21 | MadBoy | Steering center straight-run check | Robot drifts left or right depending on the last steering adjustment | Improve repeatable steering center reset/calibration |
| 2026-07-21 | MadBoy | Steering sign test | When closer to the left wall, robot steers right/away from the wall | Keep `STEERING_SIGN = 1` |
| 2026-07-21 | MadBoy | Wall-centering observation | Sometimes centered; sometimes closer to one wall than the other | Tune `SIDE_BALANCE_GAIN` and improve steering center reset |
| 2026-07-21 | MadBoy | Rear differential smoothness | Drives smoothly using LEGO parts and gears; no binding/slipping observed | Keep checking gear alignment before runs |
| 2026-07-21 | MadBoy | Hub battery qualitative runtime check | Battery lasts a long time in testing; no noticeable slowdown reported | Exact runtime not tracked yet |
| 2026-07-21 | MadBoy | Obstacle detection and strategy status | Detection is working; red/green strategy is ready and working | Add formal run/score evidence later |
| 2026-07-21 | MadBoy | Parking strategy decision | Parking and start-from-parking are not used | No parking behavior planned |

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
| 2026-07-21 | Left | 20.0 cm | 20.5 cm | +0.5 cm | Within +/- 1 cm reference target |
| 2026-07-21 | Front | 20.0 cm | 21.2 cm | +1.2 cm | Slightly outside +/- 1 cm target; retest |
| 2026-07-21 | Right | 20.0 cm | 20.1 cm | +0.1 cm | Within +/- 1 cm reference target |

## Gyro / IMU Tests

Reference note: no official universal SPIKE Prime gyro drift rate was found. Pybricks documents per-hub full-turn scale variation and supports `heading_correction`, so drift/heading error should be measured on this hub. As an internet-reported bad-case reference, a FIRST LEGO League forum post reported SPIKE Prime yaw drift as high as about 1 deg/s when the gyro was behaving incorrectly.

| Date | Robot Version | Test | Result | Notes |
| --- | --- | --- | --- | --- |
| 2026-07-21 | MadBoy | Heading reset at start line | Procedure documented | MadBoy-specific drift not measured yet |
| Internet reference | SPIKE Prime Hub | Bad-case drift report | Up to about 1 deg/s | Not measured on MadBoy; use only as conservative reference |
| Future measurement | MadBoy | Drift after 1 minute | Not measured yet | Measure this robot before competition |
| Future measurement | MadBoy | Drift after 3 minutes | Not measured yet | Measure this robot before competition |

## OpenMV H7 Vision Tests

| Date | Lighting | Target | Distance | Result | Notes |
| --- | --- | --- | ---: | --- | --- |
| 2026-07-21 | Team test lighting | Red obstacle | Not measured | Detection/strategy working | Add formal accuracy count later |
| 2026-07-21 | Team test lighting | Green obstacle | Not measured | Detection/strategy working | Add formal accuracy count later |

## Control Tuning Notes

| Date | Drive Power | Side Gain | Front Stop | Front Resume | Track Result | Notes |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| 2026-07-21 | 35 | 0.18 | 180 mm | 260 mm | Sometimes centered; sometimes closer to one wall | Tune after steering center reset improves |

