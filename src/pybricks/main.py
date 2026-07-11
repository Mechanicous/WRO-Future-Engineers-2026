"""
WRO Future Engineers 2026 starter program.

Platform:
    LEGO SPIKE Prime Hub running Pybricks MicroPython.

Sensors:
    left ultrasonic, middle/front ultrasonic, right ultrasonic.

Heading:
    LEGO SPIKE Prime Hub integrated IMU/gyro.

This is a starter control loop for the new LEGO/Pybricks robot. It is not the
final competition strategy yet. Tune the constants and extend the state
machine as the robot design matures.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.tools import StopWatch, wait


# ---------------------------------------------------------------------------
# Port assignments
# ---------------------------------------------------------------------------

# TODO: Confirm these match the real robot and keep schemes/port-map.md in sync.
# The drive motor is the SPIKE Large Angular Motor connected to the rear
# differential. The steering motor is the SPIKE Medium Angular Motor.
DRIVE_MOTOR_PORT = Port.A
STEERING_MOTOR_PORT = Port.B
LEFT_SENSOR_PORT = Port.C
FRONT_SENSOR_PORT = Port.D
RIGHT_SENSOR_PORT = Port.E


# ---------------------------------------------------------------------------
# Robot settings
# ---------------------------------------------------------------------------

DRIVE_MOTOR_DIRECTION = Direction.CLOCKWISE
STEERING_MOTOR_DIRECTION = Direction.CLOCKWISE

# Start slowly while validating the build. Increase only after safety tests.
DRIVE_POWER = 35

# Steering motor angles are relative to the straight-ahead position. Put the
# wheels straight before starting, or reset the angle after mechanically
# centering the steering linkage.
STEERING_CENTER_DEG = 0
STEERING_LEFT_LIMIT_DEG = -45
STEERING_RIGHT_LIMIT_DEG = 45
STEERING_SPEED_DPS = 500

# Flip this to -1 if the robot steers toward the wall instead of away from it.
STEERING_SIGN = 1

# Ultrasonic thresholds are in millimeters.
FRONT_STOP_MM = 180
FRONT_RESUME_MM = 260
MAX_VALID_DISTANCE_MM = 2000

# Side balancing gain converts side-distance error to steering degrees.
SIDE_BALANCE_GAIN = 0.18

LOOP_PERIOD_MS = 40
RUN_TIMEOUT_MS = 180000


# ---------------------------------------------------------------------------
# Hardware
# ---------------------------------------------------------------------------

hub = PrimeHub()
drive_motor = Motor(DRIVE_MOTOR_PORT, positive_direction=DRIVE_MOTOR_DIRECTION)
steering_motor = Motor(
    STEERING_MOTOR_PORT,
    positive_direction=STEERING_MOTOR_DIRECTION,
)

left_sensor = UltrasonicSensor(LEFT_SENSOR_PORT)
front_sensor = UltrasonicSensor(FRONT_SENSOR_PORT)
right_sensor = UltrasonicSensor(RIGHT_SENSOR_PORT)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clamp(value, lower, upper):
    return max(lower, min(upper, value))


def read_distance(sensor):
    """Return a valid ultrasonic distance in mm, or None if it is unusable."""
    try:
        distance = sensor.distance()
    except OSError:
        return None

    if distance is None:
        return None

    if distance <= 0:
        return None

    return min(distance, MAX_VALID_DISTANCE_MM)


def wait_for_start():
    hub.light.on(Color.ORANGE)
    print("Ready. Press the center button to start.")

    while Button.CENTER not in hub.buttons.pressed():
        wait(20)

    while Button.CENTER in hub.buttons.pressed():
        wait(20)

    hub.light.on(Color.GREEN)


def reset_heading():
    """Reset the SPIKE Prime integrated gyro heading at the start line."""
    hub.imu.reset_heading(0)


def read_heading():
    """Return the current integrated gyro heading in degrees."""
    return hub.imu.heading()


def center_steering():
    steering_motor.reset_angle(STEERING_CENTER_DEG)
    steering_motor.run_target(
        STEERING_SPEED_DPS,
        STEERING_CENTER_DEG,
        then=Stop.HOLD,
        wait=True,
    )


def set_steering(target_degrees):
    target_degrees = clamp(
        target_degrees,
        STEERING_LEFT_LIMIT_DEG,
        STEERING_RIGHT_LIMIT_DEG,
    )
    steering_motor.run_target(
        STEERING_SPEED_DPS,
        target_degrees,
        then=Stop.HOLD,
        wait=False,
    )


def calculate_wall_centering(left_mm, right_mm):
    """Calculate a steering correction from the left/right distance difference."""
    if left_mm is None and right_mm is None:
        return STEERING_CENTER_DEG

    if left_mm is None:
        return STEERING_SIGN * STEERING_RIGHT_LIMIT_DEG

    if right_mm is None:
        return STEERING_SIGN * STEERING_LEFT_LIMIT_DEG

    side_error = left_mm - right_mm
    correction = STEERING_SIGN * SIDE_BALANCE_GAIN * side_error
    return STEERING_CENTER_DEG + correction


def stop_robot():
    drive_motor.stop()
    set_steering(STEERING_CENTER_DEG)


def run_open_challenge_starter():
    """Starter loop for wall centering and front safety stop."""
    timer = StopWatch()
    front_blocked = False

    while timer.time() < RUN_TIMEOUT_MS:
        left_mm = read_distance(left_sensor)
        front_mm = read_distance(front_sensor)
        right_mm = read_distance(right_sensor)
        heading_deg = read_heading()

        if front_mm is None:
            front_blocked = True
        elif front_blocked and front_mm > FRONT_RESUME_MM:
            front_blocked = False
        elif not front_blocked and front_mm < FRONT_STOP_MM:
            front_blocked = True

        if front_blocked:
            hub.light.on(Color.RED)
            stop_robot()
        else:
            hub.light.on(Color.GREEN)
            steering_target = calculate_wall_centering(left_mm, right_mm)
            set_steering(steering_target)
            drive_motor.dc(DRIVE_POWER)

        print(
            "left:",
            left_mm,
            "front:",
            front_mm,
            "right:",
            right_mm,
            "heading:",
            heading_deg,
            "blocked:",
            front_blocked,
        )
        wait(LOOP_PERIOD_MS)

    stop_robot()
    hub.light.on(Color.BLUE)
    print("Run timeout complete.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

center_steering()
wait_for_start()
reset_heading()

try:
    run_open_challenge_starter()
finally:
    stop_robot()
