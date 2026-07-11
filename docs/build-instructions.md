# Build Instructions

Use this document to make the LEGO SPIKE Prime robot reproducible.

## Mechanical Assembly

TODO:

- Add LEGO chassis dimensions.
- Add SPIKE Large Angular Motor mounting steps for rear-wheel drive.
- Add rear differential gear system assembly steps.
- Add SPIKE Medium Angular Motor steering linkage steps.
- Add wheelbase, track width, and wheel diameter.
- Add sensor mount positions, heights, and angles.
- Link to build files or build photos in `../models/`.

## Electronics And Ports

The current robot uses the LEGO SPIKE Prime Hub, Powered Up motors, and three ultrasonic sensors. The hub battery powers all connected devices.

Keep the port map updated in `../schemes/port-map.md`.

Default working assumption:

| Port | Device |
| --- | --- |
| A | SPIKE Large Angular Motor for rear-wheel drive |
| B | SPIKE Medium Angular Motor for front steering |
| C | Left ultrasonic sensor |
| D | Middle/front ultrasonic sensor |
| E | Right ultrasonic sensor |
| F | Spare |

## Software Upload

1. Install Pybricks firmware on the SPIKE Prime Hub if it is not already installed.
2. Open `https://code.pybricks.com/`.
3. Connect the SPIKE Prime Hub.
4. Open `../src/pybricks/main.py`.
5. Confirm the port constants match `../schemes/port-map.md`.
6. Upload or run the program from Pybricks Code.
7. Start with the robot lifted so wheels can spin safely.
8. Verify steering center and steering direction.
9. Place the robot on the field and test at low `DRIVE_POWER`.

## Pre-Run Checklist

- [ ] Hub battery charged.
- [ ] LEGO structure is rigid.
- [ ] Wheels and gears move freely.
- [ ] Rear differential gear system rotates smoothly.
- [ ] Steering centers correctly.
- [ ] Drive motor direction is correct.
- [ ] Left ultrasonic sensor reports fresh readings.
- [ ] Middle/front ultrasonic sensor reports fresh readings.
- [ ] Right ultrasonic sensor reports fresh readings.
- [ ] Front safety stop threshold tested.
- [ ] `STEERING_SIGN` tested at low speed.
- [ ] Emergency stop or safe shutdown procedure is known by the team.

