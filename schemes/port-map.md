# LEGO SPIKE Prime Port Map

Keep this file synchronized with `../src/pybricks/main.py`.

| Port | Device | Purpose | Status |
| --- | --- | --- | --- |
| A | SPIKE Large Angular Motor | Rear-wheel drive through differential gear system | Confirmed |
| B | Left ultrasonic sensor | Left wall distance | Confirmed |
| C | OpenMV H7 via UART | Red/green pillar vision data using PUPRemote/LPF2 libraries | Confirmed |
| D | Middle/front ultrasonic sensor | Front obstacle/path distance | Confirmed |
| E | SPIKE Medium Angular Motor | Front steering linkage | Confirmed |
| F | Right ultrasonic sensor | Right wall distance | Confirmed |
| Hub IMU | SPIKE Prime integrated gyro/IMU | Heading and turn feedback | Built in |

## Sensor Placement Notes

- Left ultrasonic height from floor: about 5 cm.
- Left ultrasonic angle relative to robot centerline: faces outward to the left.
- Middle/front ultrasonic height from floor: about 6 cm.
- Middle/front ultrasonic offset from robot centerline: centered at the front.
- Right ultrasonic height from floor: about 5 cm.
- Right ultrasonic angle relative to robot centerline: faces outward to the right.
- SPIKE Prime Hub orientation: hub is lying flat, with the USB port facing the robot's left side.
- OpenMV H7 camera lens height: about 17.5 cm from the floor.
- OpenMV H7 camera angle: tilted about 5 degrees.
- OpenMV H7 communication: UART protocol on SPIKE Prime port C; PUPRemote/LPF2 Python libraries are used by the OpenMV and Pybricks code.
- OpenMV H7 field of view and Port C LPF2 cable path: TODO.

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

