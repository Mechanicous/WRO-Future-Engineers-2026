# Engineering Decisions

Use this file to show why the team chose each design, not only what the final design is.

## Decision Records

### Decision: Move From Arduino Prototype To LEGO SPIKE Prime

- Date: 2026-07-11
- Context: The team stopped using the Arduino, BMI160, VL53L1X sensors, servo, and custom wiring prototype.
- Options considered: Continue custom Arduino electronics, or rebuild on LEGO SPIKE Prime.
- Decision: Use LEGO SPIKE Prime with Pybricks MicroPython.
- Reasoning: SPIKE Prime gives an integrated hub, battery, ports, LEGO motor/sensor ecosystem, and faster mechanical iteration.
- Tradeoffs: Less direct low-level electronics control, ultrasonic readings may be less precise than ToF sensors, and the robot needs careful LEGO structural rigidity.
- Test evidence: Current LEGO SPIKE Prime robot completes 3 Open Challenge laps.
- Result after testing: LEGO SPIKE Prime remains the active platform.

### Decision: Use Three Ultrasonic Sensors

- Date: 2026-07-11
- Context: The new robot uses LEGO ultrasonic sensors on the left, middle/front, and right.
- Options considered: Camera/vision, ToF sensors, gyroscope, ultrasonic wall sensing.
- Decision: Use left/right ultrasonic sensors for wall distance and middle/front ultrasonic for safety/obstacle distance.
- Reasoning: This matches the new LEGO build and gives simple distance feedback for first autonomous driving tests.
- Tradeoffs: Ultrasonic sensors can reflect poorly from angled surfaces and may need filtering.
- Test evidence: 20 cm ultrasonic calibration recorded for left, middle/front, and right sensors.
- Result after testing: Sensors are usable for wall distance and front safety, with more distance/angle tests recommended.

### Decision: Use Pybricks MicroPython

- Date: 2026-07-11
- Context: The project moved away from Arduino C++.
- Options considered: SPIKE app blocks, LEGO Python, Pybricks MicroPython.
- Decision: Use Pybricks MicroPython.
- Reasoning: Pybricks gives clean text-based Python control of SPIKE Prime motors and sensors and makes tuning constants easy.
- Tradeoffs: Requires Pybricks firmware/workflow and careful documentation so judges can reproduce uploads.
- Test evidence: Active Pybricks program controls motors, reads ultrasonic sensors, and resets/reads hub heading.
- Result after testing: Pybricks remains the active programming platform.

### Decision: Use Rear-Wheel Drive With A Differential Gear System

- Date: 2026-07-11
- Context: The LEGO version uses a SPIKE Large Angular Motor for propulsion and a SPIKE Medium Angular Motor for steering.
- Options considered: Direct rear axle drive, rear-wheel drive with differential gearing, front-wheel drive, differential steering.
- Decision: Use rear-wheel drive through a differential gear system, with a separate front steering motor.
- Reasoning: The differential lets the rear wheels rotate at different speeds in turns, reducing tire scrub and making cornering smoother. The SPIKE Large Angular Motor drives a 20-tooth double bevel gear into the differential's 28-tooth gear, giving an approximate 20:28 reduction for more torque at the rear axle.
- Tradeoffs: The drivetrain is mechanically more complex and needs careful alignment so gears do not bind.
- Test evidence: Current robot completes 3 Open Challenge laps.
- Result after testing: Differential drivetrain retained because it drives smoothly and supports 3-lap Open Challenge runs.

### Decision: Use SPIKE Prime Integrated Gyro

- Date: 2026-07-11
- Context: The SPIKE Prime Hub includes an integrated gyro/IMU that Pybricks can read for heading feedback.
- Options considered: No gyro, external IMU, SPIKE Prime integrated gyro.
- Decision: Use the SPIKE Prime integrated gyro for heading and turn feedback.
- Reasoning: It is built into the hub, reduces wiring, and can be reset/read directly from Pybricks.
- Tradeoffs: Heading accuracy depends on hub orientation, flat placement, reset procedure, and drift testing.
- Test evidence: Hub orientation and heading reset procedure documented; internet reference for bad-case drift recorded.
- Result after testing: MadBoy-specific gyro drift measurement remains a future calibration task.

### Decision: Use OpenMV H7 For Vision

- Date: 2026-07-11
- Context: The Obstacle Challenge requires reliable red/green obstacle awareness.
- Options considered: Ultrasonic-only obstacle strategy, LEGO color sensor, OpenMV H7 camera.
- Decision: Use OpenMV H7 as the vision module.
- Reasoning: OpenMV H7 can run MicroPython vision code on the camera and is suitable for color/object detection experiments. It communicates with the SPIKE Prime Hub through the UART protocol on port C, while the PUPRemote/LPF2 Python libraries handle message packaging in code.
- Tradeoffs: Requires camera mounting, lighting calibration, and reliable UART message handling in the main robot logic.
- Test evidence: Obstacle detection is working and the red/green strategy is ready and working.
- Result after testing: Continue collecting formal run/score evidence.

### Decision: Do Not Use Parking

- Date: 2026-07-21
- Context: The team does not plan to park or start from the parking area.
- Options considered: Implement parking, start from parking area, or skip parking.
- Decision: Do not implement parking behavior for the current strategy.
- Reasoning: The current focus is Open Challenge consistency and working Obstacle Challenge detection/avoidance.
- Tradeoffs: Parking-specific points are not targeted by this strategy.
- Test evidence: Parking is intentionally not used.
- Result after testing: Not planned.

## Risks And Mitigations

| Risk | Impact | Mitigation | Status |
| --- | --- | --- | --- |
| Ultrasonic readings bounce on angled walls | Robot may steer incorrectly | Test at many distances and add filtering if needed | Basic 20 cm test complete; angled-wall testing remains future work |
| Steering motor center depends on last adjustment | Robot drifts left or right after centering | Add a repeatable center reset/calibration procedure before each run | Current test shows drift direction depends on last steering adjustment |
| Rear differential binds or slips | Robot loses speed or turns inconsistently | Check gear alignment and test both rear wheels under load | No binding/slipping observed; LEGO gears drive smoothly |
| Steering sign is reversed | Robot steers into walls | Low-speed sign test and `STEERING_SIGN` constant | Tested: `STEERING_SIGN = 1` steers away from left wall |
| Steering linkage binds at full lock | Front wheels may not reach commanded angle | Limit steering to about 45 degrees left/right and inspect the 12-tooth to 20-tooth gear linkage | Current code clamps to +/-45 degrees |
| Gyro heading drifts | Turns or lap logic become inaccurate | Reset heading at start and run drift tests | Reference value documented; MadBoy drift measurement remains future work |
| OpenMV lighting changes | Red/green classification becomes unreliable | Calibrate thresholds under field lighting | Detection/strategy working; formal lighting accuracy count remains future work |
| LEGO frame flexes during run | Sensor angle and steering geometry change | Reinforce chassis and inspect after each run | Pre-run structure check documented |
| Hub battery is low | Motor power changes | Charge before runs and record battery state | No noticeable slowdown reported; exact runtime not tracked |

## Iterations

| Version | Change | Why It Changed | Evidence |
| --- | --- | --- | --- |
| v0.1 | Arduino prototype with BMI160 and VL53L1X sensors | Initial control experiment | Git history |
| v0.2 | LEGO SPIKE Prime with 3 ultrasonic sensors and Pybricks | New team hardware direction | Current repository |
| v0.3 | Added integrated gyro and OpenMV H7 vision module | Better heading feedback and obstacle color detection | Current repository |
