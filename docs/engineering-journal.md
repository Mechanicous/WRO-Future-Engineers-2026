# Engineering Journal

Use this document to tell the story of the robot's engineering process, not only the final design. The current robot direction is LEGO SPIKE Prime with Pybricks MicroPython, three ultrasonic sensors, the integrated SPIKE Prime gyro/IMU, and an OpenMV H7 camera.

## Team

- Team name: Mechanicous
- Country/region: TODO
- Members: TODO
- Season: WRO Future Engineers 2026

## 1. Mobility And Mechanical Design

Describe the LEGO chassis, steering, drive system, stability, and mechanical constraints.

Include:

- Why LEGO SPIKE Prime / Technic construction was chosen.
- Rear-wheel drive mechanism using the SPIKE Large Angular Motor.
- Rear differential gear system, gear ratio, wheel diameter, and expected speed.
- Front steering mechanism using the SPIKE Medium Angular Motor, steering limits, and turn radius.
- Wheelbase, track width, sensor positions, and important dimensions.
- Stability, weight distribution, and structural rigidity.
- Mechanical tests and changes between versions.
- Diagrams or links to files in `../models/` and `../v-photos/`.

## 2. Power And Sensor Architecture

Describe how the SPIKE Prime Hub powers the system, how the ultrasonic sensors are placed, how the integrated gyro is used, and how the OpenMV H7 camera is mounted.

Include:

- SPIKE Prime Hub battery and charging procedure.
- Motor and sensor port map.
- Left, middle/front, and right ultrasonic sensor placement.
- SPIKE Prime Hub orientation for integrated gyro heading.
- OpenMV H7 camera position, purpose, and communication method.
- Why ultrasonic sensors were chosen for this version.
- Calibration procedure, gyro reset procedure, vision calibration, and sensor accuracy tests.
- Failure modes such as ultrasonic reflections, loose cables, low battery, or bad sensor angles.
- Diagrams or links to files in `../schemes/`.

## 3. Software Architecture And Obstacle Strategy

Describe the Pybricks software and the robot behavior.

Include:

- Main control loop in `../src/pybricks/main.py`.
- State machine or flowchart.
- Wall-centering strategy using left/right ultrasonic sensors.
- Heading feedback from the SPIKE Prime integrated gyro.
- Front safety and obstacle approach logic using the middle/front ultrasonic sensor.
- Open Challenge lap strategy.
- Obstacle Challenge red/green obstacle strategy using OpenMV H7 when implemented.
- Parking strategy if implemented.
- Edge cases and how the robot recovers.
- Links to `software-architecture.md`.

## 4. Systems Thinking And Engineering Decisions

Explain design tradeoffs and how subsystems interact.

Include:

- Why the team moved from the Arduino prototype to LEGO SPIKE Prime.
- Why Pybricks MicroPython was selected.
- Why three ultrasonic sensors were selected.
- Why the integrated SPIKE Prime gyro is used for heading feedback.
- Why OpenMV H7 is planned for vision/color detection.
- Constraints: size, weight, time, processing, power, reliability, budget, available LEGO parts.
- Major decisions and alternatives considered.
- Iterations from the old prototype to the current LEGO version.
- Risks and mitigations.
- What changed after testing.
- Links to `decisions.md`.

## 5. Reproducibility And GitHub Quality

Explain how someone else can rebuild the robot from this repository.

Include:

- LEGO build instructions, photos, or digital model files.
- Bill of materials.
- SPIKE Prime port map.
- Ultrasonic sensor placement diagram.
- SPIKE Prime Hub orientation and gyro reset notes.
- OpenMV H7 mounting and communication notes.
- Pybricks upload steps.
- Test procedure and tuning values.
- Version or release notes.
- Commit history with meaningful changes.

## Submission Checklist

- [ ] README completed.
- [ ] Engineering journal completed.
- [ ] Pybricks code uploaded in `../src/`.
- [ ] LEGO build files/photos uploaded in `../models/`.
- [ ] Port map and sensor diagrams uploaded in `../schemes/`.
- [ ] Gyro and OpenMV H7 documentation uploaded in `../schemes/`.
- [ ] Vehicle photos uploaded in `../v-photos/`.
- [ ] Team photos uploaded in `../t-photos/`.
- [ ] Demo video link added in `../video/video.md`.
- [ ] Tests documented in `tests.md`.
- [ ] Decisions documented in `decisions.md`.
- [ ] Meaningful commits are visible on GitHub.

