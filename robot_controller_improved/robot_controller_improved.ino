/*
  WRO robot controller

  Current behaviour:
    1. Initializes the BMI160 and three VL53L1X sensors.
    2. Uses the XSHUT pins to assign a unique address to each distance sensor.
    3. Captures the starting yaw angle.
    4. Drives forward while a PID controller holds that heading.
    5. Stops if the front sensor sees a close obstacle or stops updating.

  OpenMV communication is intentionally not included yet.

  IMPORTANT:
  The Servo library uses Timer1 on the Arduino Uno, which disables PWM on
  pins 9 and 10. The motor ENA wire must therefore be connected to D6.
*/

#include <Wire.h>
#include <BMI160Gen.h>
#include <VL53L1X.h>
#include <Servo.h>

// ---------------------------------------------------------------------------
// Pin assignments
// ---------------------------------------------------------------------------

constexpr uint8_t STEERING_PIN = 5;
constexpr uint8_t MOTOR_PWM_PIN = 9;  // Move ENA from D9 to D6.
constexpr uint8_t MOTOR_DIR1_PIN = 13;
constexpr uint8_t MOTOR_DIR2_PIN = 12;

constexpr uint8_t SENSOR_COUNT = 3;
constexpr uint8_t XSHUT_PINS[SENSOR_COUNT] = {2, 3, 4};

enum SensorPosition : uint8_t
{
  FRONT = 0,
  RIGHT = 1,
  LEFT = 2
};

// ---------------------------------------------------------------------------
// Robot settings
// ---------------------------------------------------------------------------

constexpr uint8_t STEERING_CENTER = 120;
constexpr uint8_t STEERING_MIN = 20;
constexpr uint8_t STEERING_MAX = 180;

// Start conservatively; increase this only after testing the safety stop.
constexpr uint8_t DRIVE_SPEED = 255;

constexpr uint16_t FRONT_STOP_MM = 200;
constexpr uint16_t FRONT_RESUME_MM = 260;
constexpr uint16_t DISTANCE_STALE_MS = 250;

constexpr uint32_t CONTROL_PERIOD_US = 10000UL;  // 100 Hz
constexpr uint32_t TELEMETRY_PERIOD_MS = 100UL;  // 10 Hz
constexpr uint16_t TOF_TIMING_BUDGET_US = 33000;
constexpr uint16_t TOF_PERIOD_MS = 50;

constexpr float GYRO_SENSITIVITY = 250.0f / 32768.0f;
constexpr float GYRO_DEAD_ZONE_DPS = 0.02f;
constexpr float RATE_FILTER_ALPHA = 0.25f;

/*
  These gains preserve the steering direction used by the original sketch.
  Tune KP first, then KD, and add only a small amount of KI if needed.
*/
constexpr float HEADING_KP = -2.10f;
constexpr float HEADING_KI = -0.03f;
constexpr float HEADING_KD = -0.08f;
constexpr float INTEGRAL_LIMIT = 80.0f;

// ---------------------------------------------------------------------------
// Devices and state
// ---------------------------------------------------------------------------

Servo steering;
VL53L1X distanceSensors[SENSOR_COUNT];

uint16_t distanceMm[SENSOR_COUNT] = {0, 0, 0};
uint32_t distanceUpdatedAtMs[SENSOR_COUNT] = {0, 0, 0};
bool distanceValid[SENSOR_COUNT] = {false, false, false};

float gyroBiasY = 0.0f;
float filteredRateY = 0.0f;
float yawDegrees = 0.0f;
float targetYawDegrees = 0.0f;

float headingIntegral = 0.0f;
float previousHeadingError = 0.0f;
float filteredHeadingDerivative = 0.0f;
bool headingPidStarted = false;
bool frontBlocked = true;

uint32_t lastGyroUs = 0;
uint32_t lastControlUs = 0;
uint32_t lastTelemetryMs = 0;

// ---------------------------------------------------------------------------
// Motor and steering
// ---------------------------------------------------------------------------

void stopMotor()
{
  analogWrite(MOTOR_PWM_PIN, 0);
}

void moveForward(uint8_t speedValue)
{
  digitalWrite(MOTOR_DIR1_PIN, HIGH);
  digitalWrite(MOTOR_DIR2_PIN, LOW);
  analogWrite(MOTOR_PWM_PIN, speedValue);
}

void setSteering(float correctionDegrees)
{
  const int angle = constrain(
    (int)(STEERING_CENTER + correctionDegrees),
    STEERING_MIN,
    STEERING_MAX
  );

  steering.write(angle);
}

void failStop(const __FlashStringHelper *message)
{
  stopMotor();
  setSteering(0.0f);
  Serial.println(message);

  while (true)
  {
    delay(1000);
  }
}

// ---------------------------------------------------------------------------
// VL53L1X distance sensors
// ---------------------------------------------------------------------------

void initializeDistanceSensors()
{
  // Hold all sensors in reset so they do not answer at the same 0x29 address.
  for (uint8_t i = 0; i < SENSOR_COUNT; ++i)
  {
    pinMode(XSHUT_PINS[i], OUTPUT);
    digitalWrite(XSHUT_PINS[i], LOW);
  }

  delay(10);

  for (uint8_t i = 0; i < SENSOR_COUNT; ++i)
  {
    /*
      Release XSHUT by changing the pin to INPUT. This lets the breakout's
      pull-up select the sensor's correct logic voltage.
    */
    pinMode(XSHUT_PINS[i], INPUT);
    delay(10);

    distanceSensors[i].setTimeout(100);

    if (!distanceSensors[i].init())
    {
      stopMotor();
      Serial.print(F("ERROR: VL53L1X initialization failed at index "));
      Serial.println(i);

      while (true)
      {
        delay(1000);
      }
    }

    distanceSensors[i].setAddress(0x2A + i);
    distanceSensors[i].setDistanceMode(VL53L1X::Long);
    distanceSensors[i].setMeasurementTimingBudget(TOF_TIMING_BUDGET_US);
    distanceSensors[i].startContinuous(TOF_PERIOD_MS);
  }
}

void updateDistanceSensors()
{
  const uint32_t nowMs = millis();

  for (uint8_t i = 0; i < SENSOR_COUNT; ++i)
  {
    if (!distanceSensors[i].dataReady())
    {
      continue;
    }

    const uint16_t reading = distanceSensors[i].read(false);

    if (!distanceSensors[i].timeoutOccurred() && reading > 0)
    {
      distanceMm[i] = reading;
      distanceUpdatedAtMs[i] = nowMs;
      distanceValid[i] = true;
    }
    else
    {
      distanceValid[i] = false;
    }
  }
}

bool isDistanceFresh(SensorPosition position)
{
  return distanceValid[position] &&
         (uint32_t)(millis() - distanceUpdatedAtMs[position]) <=
           DISTANCE_STALE_MS;
}

void updateFrontSafety()
{
  if (!isDistanceFresh(FRONT))
  {
    frontBlocked = true;
    return;
  }

  // Hysteresis prevents rapid stop/start switching near one threshold.
  if (frontBlocked)
  {
    if (distanceMm[FRONT] > FRONT_RESUME_MM)
    {
      frontBlocked = false;
    }
  }
  else if (distanceMm[FRONT] < FRONT_STOP_MM)
  {
    frontBlocked = true;
  }
}

// ---------------------------------------------------------------------------
// BMI160 yaw estimation
// ---------------------------------------------------------------------------

void initializeGyroscope()
{
  if (!BMI160.begin(BMI160GenClass::I2C_MODE))
  {
    failStop(F("ERROR: BMI160 not found"));
  }

  BMI160.setGyroRange(250);

  Serial.println(F("Keep the robot still: calibrating BMI160..."));
  BMI160.autoCalibrateGyroOffset();
  delay(500);

  int16_t gxRaw = 0;
  int16_t gyRaw = 0;
  int16_t gzRaw = 0;
  int32_t sumY = 0;

  constexpr uint16_t SAMPLE_COUNT = 1000;

  for (uint16_t i = 0; i < SAMPLE_COUNT; ++i)
  {
    BMI160.readGyro(gxRaw, gyRaw, gzRaw);
    sumY += gyRaw;
    delay(2);
  }

  gyroBiasY =
    (sumY / (float)SAMPLE_COUNT) * GYRO_SENSITIVITY;

  yawDegrees = 0.0f;
  filteredRateY = 0.0f;
  lastGyroUs = micros();

  Serial.print(F("Gyro Y bias (degrees/s): "));
  Serial.println(gyroBiasY, 6);
}

float updateYaw()
{
  const uint32_t nowUs = micros();
  float deltaSeconds = (uint32_t)(nowUs - lastGyroUs) / 1000000.0f;
  lastGyroUs = nowUs;

  // Reject a bad interval after startup, debugging, or a long pause.
  if (deltaSeconds <= 0.0f || deltaSeconds > 0.1f)
  {
    deltaSeconds = CONTROL_PERIOD_US / 1000000.0f;
  }

  int16_t gxRaw = 0;
  int16_t gyRaw = 0;
  int16_t gzRaw = 0;
  BMI160.readGyro(gxRaw, gyRaw, gzRaw);

  float rateY = gyRaw * GYRO_SENSITIVITY - gyroBiasY;

  if (fabs(rateY) < GYRO_DEAD_ZONE_DPS)
  {
    rateY = 0.0f;
  }

  filteredRateY += RATE_FILTER_ALPHA * (rateY - filteredRateY);
  yawDegrees += filteredRateY * deltaSeconds;

  return deltaSeconds;
}

// ---------------------------------------------------------------------------
// Heading PID
// ---------------------------------------------------------------------------

void resetHeadingPid()
{
  headingIntegral = 0.0f;
  previousHeadingError = targetYawDegrees - yawDegrees;
  filteredHeadingDerivative = 0.0f;
  headingPidStarted = false;
}

float calculateHeadingCorrection(float deltaSeconds)
{
  const float error = targetYawDegrees - yawDegrees;

  headingIntegral += error * deltaSeconds;
  headingIntegral = constrain(
    headingIntegral,
    -INTEGRAL_LIMIT,
    INTEGRAL_LIMIT
  );

  float derivative = 0.0f;

  if (headingPidStarted && deltaSeconds > 0.0f)
  {
    derivative = (error - previousHeadingError) / deltaSeconds;
  }
  else
  {
    headingPidStarted = true;
  }

  // Reduce steering chatter caused by noisy derivative measurements.
  filteredHeadingDerivative +=
    0.25f * (derivative - filteredHeadingDerivative);

  previousHeadingError = error;

  return HEADING_KP * error +
         HEADING_KI * headingIntegral +
         HEADING_KD * filteredHeadingDerivative;
}

// ---------------------------------------------------------------------------
// Diagnostics
// ---------------------------------------------------------------------------

void printDistance(uint8_t index)
{
  if (isDistanceFresh((SensorPosition)index))
  {
    Serial.print(distanceMm[index]);
  }
  else
  {
    Serial.print(F("NA"));
  }
}

void printTelemetry()
{
  const uint32_t nowMs = millis();

  if ((uint32_t)(nowMs - lastTelemetryMs) < TELEMETRY_PERIOD_MS)
  {
    return;
  }

  lastTelemetryMs = nowMs;

  Serial.print(F("yaw="));
  Serial.print(yawDegrees, 2);
  Serial.print(F(", target="));
  Serial.print(targetYawDegrees, 2);
  Serial.print(F(", front="));
  printDistance(FRONT);
  Serial.print(F(", right="));
  printDistance(RIGHT);
  Serial.print(F(", left="));
  printDistance(LEFT);
  Serial.print(F(", motor="));
  Serial.println(frontBlocked ? F("STOP") : F("RUN"));
}

// ---------------------------------------------------------------------------
// Arduino entry points
// ---------------------------------------------------------------------------

void setup()
{
  pinMode(MOTOR_DIR1_PIN, OUTPUT);
  pinMode(MOTOR_DIR2_PIN, OUTPUT);
  pinMode(MOTOR_PWM_PIN, OUTPUT);
  stopMotor();

  steering.attach(STEERING_PIN);
  setSteering(0.0f);

  Serial.begin(115200);
  // Do not wait for Serial: the robot must also start without a USB cable.

  Wire.begin();
  Wire.setClock(400000);

  initializeGyroscope();
  initializeDistanceSensors();

  Serial.println(F("Initialization complete."));
  Serial.println(F("Starting in 3 seconds..."));
  delay(3000);

  // Start heading control from the robot's current orientation.
  lastGyroUs = micros();
  updateYaw();
  targetYawDegrees = yawDegrees;
  resetHeadingPid();

  lastControlUs = micros();
  lastTelemetryMs = millis();
  Serial.println(F("READY"));
}

void loop()
{
  updateDistanceSensors();
  updateFrontSafety();

  const uint32_t nowUs = micros();

  if ((uint32_t)(nowUs - lastControlUs) < CONTROL_PERIOD_US)
  {
    printTelemetry();
    return;
  }

  lastControlUs = nowUs;

  const float deltaSeconds = updateYaw();
  const float steeringCorrection =
    calculateHeadingCorrection(deltaSeconds);

  setSteering(steeringCorrection);

  if (frontBlocked)
  {
    stopMotor();
  }
  else
  {
    moveForward(DRIVE_SPEED);
  }

  printTelemetry();
}
