# Pybricks Program

The active program is `main.py`.

## Hardware Assumptions

The current starter code assumes:

- LEGO SPIKE Prime Hub.
- One drive motor.
- One steering motor.
- Three ultrasonic sensors:
  - Left sensor.
  - Middle/front sensor.
  - Right sensor.

If the robot uses differential drive instead of a steering linkage, update `main.py` and document the change in `../../docs/decisions.md`.

## Default Port Map

Confirm these constants before running:

| Device | Default Port |
| --- | --- |
| Drive motor | A |
| Steering motor | B |
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

