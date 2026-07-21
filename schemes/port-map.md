# LEGO SPIKE Prime Port Map

Keep this file synchronized with `../src/pybricks/main.py`.

| Port | Device | Purpose | Status |
| --- | --- | --- | --- |
| A | SPIKE Large Angular Motor | Rear-wheel drive through differential gear system | Confirmed |
| B | Left ultrasonic sensor | Left wall distance | Confirmed |
| C | OpenMV H7 via PUPRemote/LPF2 | Red/green pillar vision data | Confirmed |
| D | Middle/front ultrasonic sensor | Front obstacle/path distance | Confirmed |
| E | SPIKE Medium Angular Motor | Front steering linkage | Confirmed |
| F | Right ultrasonic sensor | Right wall distance | Confirmed |
| Hub IMU | SPIKE Prime integrated gyro/IMU | Heading and turn feedback | Built in |

## Sensor Placement Notes

Add measurements after the build is finalized:

- Left ultrasonic height from floor: TODO.
- Left ultrasonic angle relative to robot centerline: TODO.
- Middle/front ultrasonic height from floor: TODO.
- Middle/front ultrasonic offset from robot centerline: TODO.
- Right ultrasonic height from floor: TODO.
- Right ultrasonic angle relative to robot centerline: TODO.
- SPIKE Prime Hub orientation and top/front direction: TODO.
- OpenMV H7 camera height, angle, field of view, and Port C LPF2 cable path: TODO.

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

