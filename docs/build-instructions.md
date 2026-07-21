# Build Instructions

Use this document to make the LEGO SPIKE Prime robot reproducible.

The main LEGO design file is `../models/Robot_Design.io`. Open it with Studio 2.0 to view the MadBoy model and follow the included step-by-step building instructions.

## Mechanical Assembly

TODO:

- Open `../models/Robot_Design.io` in Studio 2.0 and follow the included step-by-step instructions.
- Add LEGO chassis dimensions.
- Add SPIKE Large Angular Motor mounting steps for rear-wheel drive.
- Add rear differential gear system assembly steps.
- Add SPIKE Medium Angular Motor steering linkage steps.
- Add wheelbase, track width, and wheel diameter.
- Add ultrasonic sensor mount positions, heights, and angles.
- Add SPIKE Prime Hub orientation for integrated gyro heading.
- Add OpenMV H7 camera mount position, height, angle, and field of view.
- Keep the Studio 2.0 model in `../models/` synchronized with the physical robot.

## Electronics And Ports

The current robot uses the LEGO SPIKE Prime Hub, Powered Up motors, three ultrasonic sensors, the hub's integrated gyro/IMU, and a planned OpenMV H7 camera. The hub battery powers LEGO devices connected to the hub.

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
| Hub IMU | Integrated gyro/heading |
| TODO | OpenMV H7 camera |

## Software Upload

1. Install Pybricks firmware on the SPIKE Prime Hub if it is not already installed.
2. Open `https://code.pybricks.com/`.
3. Connect the SPIKE Prime Hub.
4. Open `../src/pybricks/main.py`.
5. Confirm the port constants match `../schemes/port-map.md`.
6. Upload or run the program from Pybricks Code.
7. Start with the robot lifted so wheels can spin safely.
8. Verify steering center and steering direction.
9. Verify the gyro heading resets to 0 at the start line.
10. Place the robot on the field and test at low `DRIVE_POWER`.

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
- [ ] Integrated gyro heading resets at the start line.
- [ ] OpenMV H7 is mounted securely.
- [ ] OpenMV H7 communication method is documented.
- [ ] Front safety stop threshold tested.
- [ ] `STEERING_SIGN` tested at low speed.
- [ ] Emergency stop or safe shutdown procedure is known by the team.

