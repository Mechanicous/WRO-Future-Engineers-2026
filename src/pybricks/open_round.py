"""
Open Round template for MadBoy.

Goal:
    Drive three Open Challenge laps using the SPIKE Prime integrated gyro for
    heading stability and the left/right/front ultrasonic sensors for distance
    correction and safety.

This file is a publishable template. Tune constants on the real field before
using it as the final competition program.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.tools import StopWatch, wait


# ---------------------------------------------------------------------------
# Ports
# ---------------------------------------------------------------------------

DRIVE_MOTOR_PORT = Port.A
LEFT_SENSOR_PORT = Port.B
FRONT_SENSOR_PORT = Port.D
STEERING_MOTOR_PORT = Port.E
RIGHT_SENSOR_PORT = Port.F


# ---------------------------------------------------------------------------
# Tunable Settings
# ---------------------------------------------------------------------------

DRIVE_MOTOR_DIRECTION = Direction.CLOCKWISE
STEERING_MOTOR_DIRECTION = Direction.CLOCKWISE

DRIVE_POWER = 35

STEERING_CENTER_DEG = 0
STEERING_LEFT_LIMIT_DEG = -45
STEERING_RIGHT_LIMIT_DEG = 45
STEERING_SPEED_DPS = 500
STEERING_SIGN = 1

FRONT_STOP_MM = 180
FRONT_RESUME_MM = 260
MAX_VALID_DISTANCE_MM = 2000

SIDE_TARGET_MM = 210
SIDE_BALANCE_GAIN = 0.16
GYRO_HEADING_GAIN = 0.55

LOOP_PERIOD_MS = 40
OPEN_ROUND_TARGET_LAPS = 3
OPEN_ROUND_TIMEOUT_MS = 180000

# Update this with lap counting from your final field logic when available.
ESTIMATED_LAP_TIME_MS = 55000


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
    """Return a filtered ultrasonic reading in millimeters."""
    try:
        distance = sensor.distance()
    except OSError:
        return None

    if distance is None or distance <= 0:
        return None

    return min(distance, MAX_VALID_DISTANCE_MM)


def wait_for_start():
    hub.light.on(Color.ORANGE)
    print("Open Round ready. Press center button.")

    while Button.CENTER not in hub.buttons.pressed():
        wait(20)

    while Button.CENTER in hub.buttons.pressed():
        wait(20)


def reset_heading():
    hub.imu.reset_heading(0)


def read_heading():
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


def stop_robot():
    drive_motor.stop()
    set_steering(STEERING_CENTER_DEG)


def calculate_distance_correction(left_mm, right_mm):
    """Use side sensors to keep the robot balanced between the walls."""
    if left_mm is None and right_mm is None:
        return 0

    if left_mm is None:
        side_error = SIDE_TARGET_MM - right_mm
    elif right_mm is None:
        side_error = left_mm - SIDE_TARGET_MM
    else:
        side_error = left_mm - right_mm

    return STEERING_SIGN * SIDE_BALANCE_GAIN * side_error


def calculate_gyro_correction(current_heading, target_heading):
    """Steer back toward the target heading measured at the start line."""
    heading_error = current_heading - target_heading
    return -STEERING_SIGN * GYRO_HEADING_GAIN * heading_error


def calculate_open_round_steering(left_mm, right_mm, current_heading, target_heading):
    distance_correction = calculate_distance_correction(left_mm, right_mm)
    gyro_correction = calculate_gyro_correction(current_heading, target_heading)
    return STEERING_CENTER_DEG + distance_correction + gyro_correction


def front_is_blocked(front_mm, was_blocked):
    if front_mm is None:
        return True

    if was_blocked:
        return front_mm <= FRONT_RESUME_MM

    return front_mm < FRONT_STOP_MM


def estimated_laps_completed(timer_ms):
    return timer_ms // ESTIMATED_LAP_TIME_MS


def run_open_round():
    timer = StopWatch()
    target_heading = read_heading()
    front_blocked = False

    while timer.time() < OPEN_ROUND_TIMEOUT_MS:
        left_mm = read_distance(left_sensor)
        front_mm = read_distance(front_sensor)
        right_mm = read_distance(right_sensor)
        heading_deg = read_heading()
        lap_count = estimated_laps_completed(timer.time())

        if lap_count >= OPEN_ROUND_TARGET_LAPS:
            break

        front_blocked = front_is_blocked(front_mm, front_blocked)

        if front_blocked:
            hub.light.on(Color.RED)
            stop_robot()
        else:
            hub.light.on(Color.GREEN)
            steering_target = calculate_open_round_steering(
                left_mm,
                right_mm,
                heading_deg,
                target_heading,
            )
            set_steering(steering_target)
            drive_motor.dc(DRIVE_POWER)

        print(
            "mode:open",
            "lap:",
            lap_count,
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
    print("Open Round complete.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

center_steering()
wait_for_start()
reset_heading()

try:
    run_open_round()
finally:
    stop_robot()
