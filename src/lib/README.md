# Third-Party Communication Libraries

This folder stores the PUPRemote/LPF2 libraries used for communication between
the LEGO SPIKE Prime Hub and the OpenMV H7 camera.

## Library Layout

| File | Target Device | Purpose |
| --- | --- | --- |
| `openmv/lpf2.py` | OpenMV H7 camera | Low-level LPF2 communication layer that lets the camera appear as a LEGO Powered Up device |
| `openmv/pupremote.py` | OpenMV H7 camera | Sensor-side PUPRemote interface used by the camera program |
| `pybricks/pupremote_hub.py` | SPIKE Prime Hub | Hub-side PUPRemote interface used by Pybricks programs |

## Upload Notes

- Copy `openmv/lpf2.py` and `openmv/pupremote.py` to the OpenMV H7 together with the final camera program.
- Copy `pybricks/pupremote_hub.py` to the SPIKE Prime Hub together with the final Pybricks program that reads OpenMV data.
- Keep the command/channel names and data formats identical on both sides.

## License Notice

These library files identify themselves as GPL-licensed third-party code by
Anton Vanhoucke & Ste7an / AntonsMindstorms.com. They are included so the robot
software is reproducible. The team's own project files remain under the MIT
License unless a file says otherwise.
