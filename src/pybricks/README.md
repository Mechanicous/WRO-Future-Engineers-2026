# Pybricks Program

This folder contains one program file for each WRO Future Engineers stage.

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
2. Run the program for the current stage.
3. Confirm all three ultrasonic readings are printed.
4. Confirm the heading value is printed and near 0 after the start button is pressed.
5. Check that the drive motor direction is correct.
6. Check that steering centers correctly.
7. If steering turns the wrong way, flip `STEERING_SIGN` in the stage program being tested.
8. Start with low `DRIVE_POWER` before track testing.

## Program Files

| File | Purpose |
| --- | --- |
| `open_round.py` | Open Challenge / Open Round program using gyro heading correction plus left/right/front ultrasonic distance correction |
| `obstacle_course.py` | Obstacle Challenge program location; currently marked `#soon` until the team publishes this stage code |
| `../lib/pybricks/pupremote_hub.py` | Hub-side PUPRemote library for receiving OpenMV H7 data on port C |

## OpenMV H7

OpenMV H7 communicates with the SPIKE Prime Hub through UART on port C. PUPRemote/LPF2 are Python libraries used by the code to package messages; they are not the communication protocol.

The hub-side library is stored at `../lib/pybricks/pupremote_hub.py`. Copy it to the SPIKE Prime Hub together with the final stage program that reads OpenMV data.

The final integrated reader/strategy code will be added after team testing is ready to publish.
