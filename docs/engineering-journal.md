# Engineering Journal

Use this document to tell the story of the robot's engineering process, not only the final design.

## Team

- Team name: TODO
- Country/region: TODO
- Members: TODO
- Season: WRO Future Engineers 2026

## 1. Mobility And Mechanical Design

Describe the chassis, steering, drive system, stability, and mechanical constraints.

Include:

- Why this chassis was chosen.
- Steering and drive mechanism.
- Wheelbase, track width, and important dimensions.
- Torque and speed reasoning.
- Mechanical tests and changes between versions.
- Diagrams or links to files in `../models/` and `../v-photos/`.

## 2. Power And Sensor Architecture

Describe how power is distributed and how sensors are placed.

Include:

- Battery and regulators.
- Motor driver and power wiring.
- Sensor list, purpose, and placement.
- Why these sensors were chosen.
- Calibration procedure.
- Failure modes such as low battery, sensor noise, or glare.
- Diagrams or links to files in `../schemes/`.

## 3. Software Architecture And Obstacle Strategy

Describe the robot behavior and program structure.

Include:

- Main control loop.
- State machine or flowchart.
- Lane or wall-following strategy.
- Obstacle detection and avoidance strategy.
- Parking strategy if implemented.
- PID or control algorithms.
- Edge cases and how the robot recovers.
- Links to `../src/` and `software-architecture.md`.

## 4. Systems Thinking And Engineering Decisions

Explain design tradeoffs and how subsystems interact.

Include:

- Constraints: size, weight, time, processing, power, reliability, budget.
- Major decisions and alternatives considered.
- Iterations from version 1 to later versions.
- Risks and mitigations.
- What changed after testing.
- Links to `decisions.md`.

## 5. Reproducibility And GitHub Quality

Explain how someone else can rebuild the robot from this repository.

Include:

- Build instructions.
- Bill of materials.
- Wiring diagrams.
- CAD/model files.
- Software upload steps.
- Test procedure.
- Version or release notes.
- Commit history with meaningful changes.

## Submission Checklist

- [ ] README completed.
- [ ] Engineering journal completed.
- [ ] Code uploaded in `src/`.
- [ ] CAD or model files uploaded in `models/`.
- [ ] Wiring diagrams uploaded in `schemes/`.
- [ ] Vehicle photos uploaded in `v-photos/`.
- [ ] Team photos uploaded in `t-photos/`.
- [ ] Demo video link added in `video/video.md`.
- [ ] Tests documented in `tests.md`.
- [ ] Decisions documented in `decisions.md`.
- [ ] At least three meaningful commits are visible on GitHub.

