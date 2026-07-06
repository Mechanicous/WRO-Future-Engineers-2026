# WRO Future Engineers 2026

Engineering materials for a self-driving vehicle competing in the WRO Future Engineers 2026 category.

## Repository Map

- `src/` - robot control software.
- `schemes/` - wiring diagrams, power diagrams, and sensor layout drawings.
- `models/` - CAD, STL, STEP, laser cutting, or CNC files for custom robot parts.
- `v-photos/` - vehicle photos from all required angles.
- `t-photos/` - official and informal team photos.
- `video/video.md` - link to the robot driving demonstration video.
- `docs/engineering-journal.md` - structured engineering journal for the 2026 rubric.
- `docs/software-architecture.md` - software flow, state machine, and obstacle strategy notes.
- `docs/tests.md` - testing workflow, logs, tuning data, and results.
- `docs/decisions.md` - engineering decisions, tradeoffs, iterations, risks, and mitigations.
- `docs/build-instructions.md` - steps to reproduce the robot and upload the software.
- `other/` - BOM, calibration notes, datasets, hardware specs, and extra reproducibility files.

## Current Robot Software

The current Arduino sketch is located at:

`src/robot_controller_improved/robot_controller_improved.ino`

It currently:

- Initializes a BMI160 gyroscope.
- Initializes three VL53L1X distance sensors using XSHUT pins and unique I2C addresses.
- Captures a starting yaw angle.
- Uses a PID controller to hold heading while driving forward.
- Stops the motor when the front distance sensor detects a close obstacle or stops updating.

OpenMV communication and full obstacle challenge behavior are not included yet.

## Build And Upload

1. Open `src/robot_controller_improved/robot_controller_improved.ino` in the Arduino IDE.
2. Install the required Arduino libraries:
   - `BMI160Gen`
   - `VL53L1X`
   - `Servo`
3. Select the correct Arduino-compatible board and port.
4. Confirm the wiring matches the pin constants in the sketch.
5. Upload the sketch.
6. Keep the robot still during BMI160 calibration after startup.

More detailed reproduction steps belong in `docs/build-instructions.md`.

## WRO 2026 Documentation Checklist

Before submission, complete the repository so another team could rebuild the robot:

- Add vehicle photos in `v-photos/`.
- Add team photos in `t-photos/`.
- Add wiring and power diagrams in `schemes/`.
- Add CAD or printable model files in `models/`.
- Add a driving demonstration link in `video/video.md`.
- Complete the engineering journal in `docs/engineering-journal.md`.
- Document software flow, obstacle strategy, and edge cases in `docs/software-architecture.md`.
- Record testing workflow and tuning results in `docs/tests.md`.
- Record engineering decisions, tradeoffs, failures, and iterations in `docs/decisions.md`.
- Keep at least three meaningful Git commits with clear messages.

## Sources Used For This Structure

- WRO 2026 Future Engineers General Rules, Appendix C: Engineering Journal and Documentation Requirements.
- Official WRO Future Engineers engineering materials template folder structure.

