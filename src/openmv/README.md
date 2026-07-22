# OpenMV H7 Vision Module

This folder is reserved for the OpenMV H7 camera program and integration notes.

## Role

The OpenMV H7 is used for:

- detecting red and green traffic signs/obstacles,
- sending obstacle classification to the SPIKE Prime Hub,
- supporting the Obstacle Challenge strategy.

## Integration Notes

- Communication protocol: UART.
- SPIKE Prime port: C.
- Code libraries: PUPRemote/LPF2 Python libraries package the messages in code.
- Camera mounting: lens about 17.5 cm from the floor, tilted about 5 degrees.
- Current status: obstacle detection and red/green strategy are working in team testing.

## Message Plan

The camera should send obstacle information such as:

- obstacle color,
- obstacle position in the camera frame,
- confidence or detected area,
- whether no valid obstacle is visible.

## Files

| File | Purpose |
| --- | --- |
| `main.py` | OpenMV camera program location; final team-tested code will be added when ready |
| `../lib/openmv/lpf2.py` | LPF2 communication layer used by the camera side |
| `../lib/openmv/pupremote.py` | PUPRemote sensor-side helper used by the camera side |

Copy both OpenMV library files to the OpenMV H7 together with `main.py` when the final camera program is ready.
