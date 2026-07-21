# Build Instructions

Use this document to make the LEGO SPIKE Prime robot reproducible.

The main LEGO design file is `../models/Robot_Design.io`. Open it with Studio 2.0 to view the MadBoy model and follow the included step-by-step building instructions.

## Mechanical Assembly

TODO:

- Open `../models/Robot_Design.io` in Studio 2.0 and follow the included step-by-step instructions.
- Documented LEGO chassis dimensions: about 20 cm long x 13.5 cm wide x 22 cm high.
- Add SPIKE Large Angular Motor mounting steps for rear-wheel drive.
- Documented rear differential gear system: 20-tooth double bevel drive gear into 28-tooth differential gear, with three 12-tooth bevel gears inside the differential.
- Documented SPIKE Medium Angular Motor steering linkage: 12-tooth gear into 20-tooth gear, moving an arm linkage.
- Documented wheelbase, track width, and wheel diameter.
- Documented ultrasonic sensor mount heights and facing directions.
- Documented SPIKE Prime Hub orientation for integrated gyro heading.
- Print or prepare `../models/openmv-camera-case.stl` for the OpenMV H7 camera.
- Documented OpenMV H7 camera lens height and tilt angle. Add field of view and case installation notes after camera calibration.
- Keep the Studio 2.0 model in `../models/` synchronized with the physical robot.

## Electronics And Ports

The current robot uses the LEGO SPIKE Prime Hub, Powered Up motors, three ultrasonic sensors, the hub's integrated gyro/IMU, and a planned OpenMV H7 camera. The hub battery powers LEGO devices connected to the hub. Before each run, charge the hub battery to full, check all cables, make sure the LEGO structure is steady and sturdy, and confirm that every part is in place.

Keep the port map updated in `../schemes/port-map.md`.

Confirmed port map:

| Port | Device |
| --- | --- |
| A | SPIKE Large Angular Motor for rear-wheel drive |
| B | Left ultrasonic sensor |
| C | OpenMV H7 via PUPRemote/LPF2 |
| D | Middle/front ultrasonic sensor |
| E | SPIKE Medium Angular Motor for front steering |
| F | Right ultrasonic sensor |
| Hub IMU | Integrated gyro/heading |

## Chassis Dimensions

| Measurement | Approximate Value | How It Was Measured |
| --- | ---: | --- |
| Length | 20 cm | Front-most point to rear-most point |
| Width | 13.5 cm | Left-most point to right-most point |
| Height | 22 cm | Floor to highest point |
| Wheelbase | 10.3 cm | Front axle center to rear axle center |
| Front track width | 11.2 cm | Center of left front wheel to center of right front wheel |
| Rear track width | 11.2 cm | Center of left rear wheel to center of right rear wheel |
| Wheel diameter | 5.5 cm | Outside tire diameter |

MadBoy fits within the WRO Future Engineers 2026 maximum robot size of 30 cm length x 20 cm width x 30 cm height.

## Rear Differential Drivetrain

The rear drive motor is a LEGO SPIKE Prime Large Angular Motor. It drives a beige 20-tooth double bevel gear, which drives the 28-tooth gear on the LEGO differential. The external gear ratio is approximately 20:28, so the differential output turns at about 0.71x motor-gear speed and gains about 1.4x torque before drivetrain losses.

The LEGO differential must contain three 12-tooth bevel gears inside it. Those internal bevel gears allow the left and right rear wheels to rotate at different speeds during turns.

## Front Steering Linkage

The front steering is powered by a LEGO SPIKE Prime Medium Angular Motor. The motor drives a 12-tooth gear, which drives a 20-tooth gear connected to an arm. This arm moves the steering system and turns the front wheels.

The maximum steering range is about 45 degrees left and 45 degrees right. The Pybricks program clamps steering commands to the same range.

## Sensor And Camera Placement

| Component | Placement |
| --- | --- |
| Left ultrasonic sensor | About 5 cm from the floor, facing outward to the left |
| Middle/front ultrasonic sensor | About 6 cm from the floor, facing forward |
| Right ultrasonic sensor | About 5 cm from the floor, facing outward to the right |
| OpenMV H7 camera | Lens about 17.5 cm from the floor, tilted about 5 degrees |
| SPIKE Prime Hub | Lying flat, with USB port facing the robot's left side |

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

- [ ] Hub battery charged to full.
- [ ] All cables are connected firmly.
- [ ] LEGO structure is rigid, steady, and sturdy.
- [ ] Motors, sensors, camera, and gears are in place.
- [ ] Wheels and gears move freely.
- [ ] Rear differential gear system rotates smoothly and contains three 12-tooth bevel gears.
- [ ] Steering centers correctly and reaches about 45 degrees left/right without binding.
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

