# Sensor Reference Values

This file records internet-sourced reference values for sensors used on MadBoy. These values are not a replacement for team testing; they are starting points for calibration and test targets.

## LEGO SPIKE Prime Ultrasonic / Distance Sensor

| Item | Reference Value | Source |
| --- | --- | --- |
| Official product range | 1-200 cm | LEGO Education |
| Official product accuracy | +/- 1 cm | LEGO Education |
| Pybricks practical distance range | 40-2000 mm | Pybricks learning material |
| Pybricks invalid/no reading value | 2000 mm | Pybricks API docs |

Notes:

- Use +/- 10 mm as the first acceptance target for controlled distance tests.
- Test each of the three sensors separately because mounting angle, target material, and ultrasonic reflections can change results.
- Pybricks may report 2000 mm when no valid distance is measured, so robot logic should treat 2000 mm as far/open or invalid depending on the state.

## SPIKE Prime Integrated Gyro / IMU

No official universal drift rate for the SPIKE Prime integrated gyro was found. Pybricks documents behavior that matters for calibration:

| Item | Reference Behavior | Source |
| --- | --- | --- |
| Heading source | The hub estimates heading by integrating gyroscope rotation | Pybricks PrimeHub docs |
| Per-hub scale variation | A hub may report a repeatable value different from 360 degrees for one full turn; Pybricks gives 357 degrees for a 360-degree turn as an example | Pybricks PrimeHub docs |
| Correction method | `heading_correction` can scale future `hub.imu.heading()` values after measuring the hub's full-rotation result | Pybricks PrimeHub docs |
| Stationary recalibration | Pybricks can treat the hub as stationary after measurements stay below thresholds for one second | Pybricks PrimeHub docs |
| Default stationary angular threshold | 2 deg/s | Pybricks PrimeHub docs |
| Default stationary acceleration threshold | 2500 mm/s^2 | Pybricks PrimeHub docs |

Competition test target:

- Record measured heading drift while the robot is still for 1 minute and 3 minutes.
- Record heading error after repeated 90-degree and 360-degree turns.
- If the hub consistently under-reports or over-reports a full turn, document the measured value and tune `heading_correction`.

## Sources

- LEGO Education Technic Distance Sensor: https://education.lego.com/en-us/products/lego-technic-distance-sensor/45604/
- Pybricks UltrasonicSensor API: https://docs.pybricks.com/en/latest/pupdevices/ultrasonicsensor.html
- Pybricks sensor learning material: https://pybricks.com/learn/sensors/responding-sensor-values/
- Pybricks PrimeHub IMU docs: https://docs.pybricks.com/en/latest/hubs/primehub.html
- Pybricks gyro calibration discussion: https://github.com/pybricks/support/issues/933

