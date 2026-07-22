# Pybricks Program

The active robot program is `main.py`. Separate templates are also provided for
the two WRO Future Engineers challenge modes.

## Hardware

- LEGO SPIKE Prime Hub.
- SPIKE Large Angular Motor for rear-wheel drive.
- SPIKE Medium Angular Motor for steering.
- SPIKE Prime integrated gyro/IMU for heading feedback.
- Three ultrasonic sensors:
  - left,
  - middle/front,
  - right.
- OpenMV H7 for vision/color detection.

The robot uses a rear differential gear system in the drivetrain. This is a mechanical differential, not differential steering.

## Port Map

| Device | Port |
| --- | --- |
| SPIKE Large Angular Motor, rear-wheel drive | A |
| Left ultrasonic sensor | B |
| OpenMV H7 via UART | C |
| Middle/front ultrasonic sensor | D |
| SPIKE Medium Angular Motor, steering | E |
| Right ultrasonic sensor | F |

The judge-facing port map is in `../../schemes/port-map.md`.

## First Run Checklist

1. Put the robot on blocks so the wheels can spin safely.
2. Run the program.
3. Confirm all three ultrasonic readings are printed.
4. Confirm the heading value is printed and near 0 after the start button is pressed.
5. Check that the drive motor direction is correct.
6. Check that steering centers correctly.
7. If steering turns the wrong way, flip `STEERING_SIGN` in `main.py`.
8. Start with low `DRIVE_POWER` before track testing.

## Program Files

| File | Purpose |
| --- | --- |
| `main.py` | Current active starter program used for testing |
| `open_round.py` | Open Round template using gyro heading correction plus left/right/front ultrasonic distance correction |
| `obstacle_course.py` | Obstacle Course template with OpenMV result hooks and structure for the final red/green obstacle strategy |

## OpenMV H7

OpenMV H7 communicates with the SPIKE Prime Hub through UART on port C. PUPRemote/LPF2 are Python libraries used by the code to package messages; they are not the communication protocol.

The final integrated reader/strategy code will be added after team testing is ready to publish.
