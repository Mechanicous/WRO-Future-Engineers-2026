# Models

Add mechanical design files and reproducible build materials for the LEGO SPIKE Prime robot.

Useful formats:

- LEGO Studio `.io` files.
- Step-by-step build photos.
- Dimension drawings for wheelbase, track width, and sensor placement.
- Custom part CAD only if non-LEGO parts are used.

## Current Model

- `Robot_Design.io` - LEGO Studio 2.0 model for MadBoy. This file includes the step-by-step building instructions for the robot.
- `openmv-camera-case.stl` - 3D printable case for the OpenMV camera.

Open `Robot_Design.io` with Studio 2.0 to inspect the LEGO design and follow the assembly steps.

## External Model Sources

- `openmv-camera-case.stl` comes from the Instructables project [Backpack #1: OpenMV Camera](https://www.instructables.com/Backpack-1-OpenMV-Camera/). Keep this source link with the file for attribution and traceability.

## TODO

- Keep `Robot_Design.io` updated when the physical robot changes.
- Add steering linkage photos and dimensions.
- Rear differential gear layout: SPIKE Large Angular Motor drives a 20-tooth double bevel gear into a 28-tooth LEGO differential gear; the differential contains three 12-tooth bevel gears.
- Add ultrasonic sensor mount photos and measurements.
- Add SPIKE Prime Hub orientation photos for integrated gyro heading.
- Add OpenMV H7 camera mount photos, height, angle, field of view, and case installation notes.
- Current approximate dimensions: length 20 cm, width 13.5 cm, height 22 cm, wheelbase 10.3 cm, front/rear track width 11.2 cm, wheel diameter 5.5 cm.
- Add wheel, axle, and gearing details.
- Include enough detail that another team could rebuild the robot.
