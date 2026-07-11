# LEGO SPIKE Prime Port Map

Keep this file synchronized with `../src/pybricks/main.py`.

| Port | Device | Purpose | Status |
| --- | --- | --- | --- |
| A | SPIKE Large Angular Motor | Rear-wheel drive through differential gear system | TODO: confirm |
| B | SPIKE Medium Angular Motor | Front steering linkage | TODO: confirm |
| C | Left ultrasonic sensor | Left wall distance | TODO: confirm |
| D | Middle/front ultrasonic sensor | Front obstacle/path distance | TODO: confirm |
| E | Right ultrasonic sensor | Right wall distance | TODO: confirm |
| F | Spare | Future LEGO device if needed | TODO |
| Hub IMU | SPIKE Prime integrated gyro/IMU | Heading and turn feedback | Built in |
| TODO | OpenMV H7 camera | Vision and red/green obstacle detection | Communication method TBD |

## Sensor Placement Notes

Add measurements after the build is finalized:

- Left ultrasonic height from floor: TODO.
- Left ultrasonic angle relative to robot centerline: TODO.
- Middle/front ultrasonic height from floor: TODO.
- Middle/front ultrasonic offset from robot centerline: TODO.
- Right ultrasonic height from floor: TODO.
- Right ultrasonic angle relative to robot centerline: TODO.
- SPIKE Prime Hub orientation and top/front direction: TODO.
- OpenMV H7 camera height, angle, and field of view: TODO.

## Diagram TODO

Add a photo or diagram showing:

- Hub location.
- Cable routing.
- Motor ports.
- Rear differential gear system.
- Sensor ports.
- SPIKE Prime Hub orientation for gyro heading.
- OpenMV H7 mounting and communication path.
- Ultrasonic sensor field of view.

