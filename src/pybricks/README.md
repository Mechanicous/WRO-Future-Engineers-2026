# Pybricks Program

The active program is `main.py`.

## Hardware Assumptions

The current starter code assumes:

- LEGO SPIKE Prime Hub.
- One SPIKE Large Angular Motor for rear-wheel drive.
- One SPIKE Medium Angular Motor for steering.
- SPIKE Prime integrated gyro/IMU for heading feedback.
- Three ultrasonic sensors:
  - Left sensor.
  - Middle/front sensor.
  - Right sensor.
- OpenMV H7 planned for vision/color detection.

The robot uses a rear differential gear system in the drivetrain. This is a mechanical differential, not differential steering.

## Default Port Map

Confirm these constants before running:

| Device | Default Port |
| --- | --- |
| SPIKE Large Angular Motor, rear-wheel drive | A |
| SPIKE Medium Angular Motor, steering | B |
| Left ultrasonic sensor | C |
| Middle/front ultrasonic sensor | D |
| Right ultrasonic sensor | E |
| OpenMV H7 | TODO |

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

## OpenMV H7

OpenMV H7 integration is planned but not implemented in the Pybricks control loop yet. Document the final communication method, wiring, and message format before using OpenMV data in competition code.

