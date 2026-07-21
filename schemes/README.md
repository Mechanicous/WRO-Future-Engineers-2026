# Schemes

Add diagrams that show how the LEGO SPIKE Prime robot is connected and how the sensors are placed.

Recommended files:

- `port-map.md` for the active SPIKE Prime port assignments.
- `port-map.png` or `port-map.pdf` for a visual hub connection diagram.
- `sensor-placement.png` or `sensor-placement.pdf` for left, middle/front, and right ultrasonic sensor placement.
- `gyro-and-camera-placement.png` or `gyro-and-camera-placement.pdf` for SPIKE Prime Hub orientation and OpenMV H7 mounting.
- `power-notes.md` if you want to document SPIKE Prime battery behavior and charging procedure.

The 2026 documentation rubric expects power/sensor architecture, sensor placement, calibration, and enough detail for another team to reproduce the robot.

## TODO

- Confirm every SPIKE Prime port in `port-map.md`.
- Add a visual port map.
- Add a sensor placement diagram with distances, heights, and angles.
- Add SPIKE Prime Hub orientation for integrated gyro heading.
- Documented OpenMV H7 camera position and UART communication through SPIKE Prime port C using PUPRemote/LPF2 Python libraries. Add field of view after calibration.
- Documented pre-run power routine: charge the SPIKE Prime Hub battery to full, check all cables, verify the structure is steady and sturdy, and confirm all parts are in place.
