# Testing Workflow

Use this file to prove that the LEGO SPIKE Prime robot was tested and improved over time.

Internet-sourced reference values are summarized in `sensor-reference.md`. Team measurements should be recorded below and compared against those references.

## Test Log

| Date | Robot Version | Test | Result | Change Made |
| --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO |

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
| TODO | Left | TODO | TODO | TODO | TODO |
| TODO | Front | TODO | TODO | TODO | TODO |
| TODO | Right | TODO | TODO | TODO | TODO |

## Gyro / IMU Tests

Reference note: no official universal SPIKE Prime gyro drift rate was found. Pybricks documents per-hub full-turn scale variation and supports `heading_correction`, so drift/heading error must be measured on this hub.

| Date | Robot Version | Test | Result | Notes |
| --- | --- | --- | --- | --- |
| TODO | TODO | Heading reset at start line | TODO | TODO |
| TODO | TODO | Drift after 1 minute | TODO | TODO |
| TODO | TODO | Drift after 3 minutes | TODO | TODO |

## OpenMV H7 Vision Tests

| Date | Lighting | Target | Distance | Result | Notes |
| --- | --- | --- | ---: | --- | --- |
| TODO | TODO | Red obstacle | TODO | TODO | TODO |
| TODO | TODO | Green obstacle | TODO | TODO | TODO |

## Control Tuning Notes

| Date | Drive Power | Side Gain | Front Stop | Front Resume | Track Result | Notes |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TODO | TODO | TODO | TODO | TODO | TODO | TODO |

