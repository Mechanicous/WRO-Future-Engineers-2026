# Pybricks Program

The active program is `main.py`.

## Hardware Assumptions

The current starter code assumes:

- LEGO SPIKE Prime Hub.
- One SPIKE Large Angular Motor for rear-wheel drive.
- One SPIKE Medium Angular Motor for steering.
- Three ultrasonic sensors:
  - Left sensor.
  - Middle/front sensor.
  - Right sensor.

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

The judge-facing port map is in `../../schemes/port-map.md`.

## First Run Checklist

1. Put the robot on blocks so the wheels can spin safely.
2. Run the program.
3. Confirm all three ultrasonic readings are printed.
4. Check that the drive motor direction is correct.
5. Check that steering centers correctly.
6. If steering turns the wrong way, flip `STEERING_SIGN` in `main.py`.
7. Start with low `DRIVE_POWER` before track testing.

