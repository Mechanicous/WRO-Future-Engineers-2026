# Software Architecture

This project now uses LEGO SPIKE Prime with Pybricks MicroPython.

## Active Program

Source file:

`../src/pybricks/main.py`

Current control flow:

1. Initialize the SPIKE Prime Hub.
2. Initialize the SPIKE Large Angular Motor for rear-wheel drive, SPIKE Medium Angular Motor for steering, three ultrasonic sensors, and integrated hub gyro.
3. Wait for the hub center button.
4. Center the steering motor and reset the integrated gyro heading.
5. Read left, middle/front, and right ultrasonic distances and gyro heading.
6. Stop if the middle/front sensor reports an unsafe or invalid distance.
7. Compare left and right distances.
8. Convert side-distance error into a steering target.
9. Drive forward while repeating the loop.
10. Complete 3 laps in the Open Challenge round.

## Flowchart

```mermaid
flowchart TD
    A["Startup"] --> B["Initialize SPIKE Prime hub"]
    B --> C["Initialize motors, ultrasonic sensors, and gyro"]
    C --> D["Wait for center button"]
    D --> E["Center steering and reset gyro heading"]
    E --> F["Read distances and heading"]
    F --> G{"Front path safe?"}
    G -- "No" --> H["Stop drive motor"]
    G -- "Yes" --> I["Calculate side-distance steering"]
    I --> J["Drive forward"]
    H --> F
    J --> F
```

## Software Modules

| Area | Current Implementation | Next Work |
| --- | --- | --- |
| Hardware setup | Port constants and Pybricks device objects in `main.py` | Confirm Large Angular Motor and Medium Angular Motor ports |
| Distance reading | `read_distance()` validates ultrasonic readings | Add smoothing if needed |
| Heading reading | `hub.imu.reset_heading()` and `hub.imu.heading()` use the integrated gyro | Test drift and hub orientation |
| Front safety | Stop/resume thresholds with hysteresis | Tune thresholds on track |
| Wall centering | Left/right distance difference with gain | Tune gain and steering sign |
| Run control | Button start and 180-second timeout | Add official lap/end behavior |
| OpenMV vision | OpenMV H7 communicates over UART on SPIKE Prime port C; PUPRemote/LPF2 libraries package the data | Add final red/green obstacle avoidance behavior |
| Obstacle challenge | Not implemented yet | Add obstacle classification and avoidance |

## State Machine Plan

| State | Purpose | Entry Condition | Exit Condition | Status |
| --- | --- | --- | --- | --- |
| Init | Configure hub, motors, sensors, constants | Program starts | Devices ready | Starter code |
| WaitForStart | Hold robot until team starts run | Init complete | Center button pressed | Starter code |
| OpenDrive | Drive using ultrasonic wall centering | Start pressed | 3 laps complete, obstacle, or timeout | Working |
| CornerHandling | Turn through course corners | Corner detected | Straight section found | TODO |
| ObstacleDetect | Detect red/green obstacle with OpenMV H7 | Obstacle Challenge enabled | Obstacle classified | In progress |
| AvoidRed | Pass red obstacle correctly | Red obstacle detected | Safe path restored | TODO |
| AvoidGreen | Pass green obstacle correctly | Green obstacle detected | Safe path restored | TODO |
| Parking | Align and stop in parking zone if used | Final phase | Parked | TODO |
| FailSafeStop | Stop when readings are unsafe | Invalid/close front reading | Manual reset or safe reading | Starter code |

## Edge Cases To Document

- Ultrasonic reading is `None`, too close, or out of range.
- Left/right readings disagree strongly.
- Sensor sees an angled wall and reports a false long distance.
- Gyro heading drifts or is reset while robot is not aligned.
- OpenMV H7 loses red/green accuracy under different lighting.
- Steering sign is reversed.
- Robot starts too close to a wall or obstacle.
- Hub battery is low and motor speed changes.

