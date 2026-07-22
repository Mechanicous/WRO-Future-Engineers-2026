"""
Obstacle Course template for MadBoy.

Goal:
    Provide the structure for the Obstacle Challenge program while the final
    OpenMV color/sign strategy is still being prepared.

Current assumptions:
    - Rear-wheel drive motor is on port A.
    - OpenMV H7 sends vision results to the SPIKE Prime Hub on port C.
    - Three ultrasonic sensors keep distance awareness.
    - The robot uses the hub gyro for heading correction.
    - The team will not start from the parking area and will not perform
      parking in the final run.
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
OPENMV_PORT = Port.C
FRONT_SENSOR_PORT = Port.D
STEERING_MOTOR_PORT = Port.E
RIGHT_SENSOR_PORT = Port.F


# ---------------------------------------------------------------------------
# Tunable Settings
# ---------------------------------------------------------------------------

DRIVE_MOTOR_DIRECTION = Direction.CLOCKWISE
STEERING_MOTOR_DIRECTION = Direction.CLOCKWISE

DRIVE_POWER = 30
APPROACH_POWER = 22

STEERING_CENTER_DEG = 0
STEERING_LEFT_LIMIT_DEG = -45
STEERING_RIGHT_LIMIT_DEG = 45
STEERING_SPEED_DPS = 500
STEERING_SIGN = 1

FRONT_STOP_MM = 100
OBJECT_CONFIRM_DISTANCE_MM = 100
MAX_VALID_DISTANCE_MM = 2000

SIDE_BALANCE_GAIN = 0.14
GYRO_HEADING_GAIN = 0.45

LOOP_PERIOD_MS = 40
OBSTACLE_TIMEOUT_MS = 180000

VISION_NONE = "none"
VISION_RED = "red"
VISION_GREEN = "green"


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
    try:
        distance = sensor.distance()
    except OSError:
        return None

    if distance is None or distance <= 0:
        return None

    return min(distance, MAX_VALID_DISTANCE_MM)


def wait_for_start():
    hub.light.on(Color.ORANGE)
    print("Obstacle Course ready. Press center button.")

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


def read_openmv_result():
    """
    Return the latest OpenMV result.

    Update this function body with the PUPRemote/LPF2 library call when the
    final OpenMV code is ready. Keep the returned value normalized to one of
    VISION_NONE, VISION_RED, or VISION_GREEN so the strategy code stays simple.
    """
    return VISION_NONE


def calculate_wall_and_heading_steering(left_mm, right_mm, heading_deg, target_heading):
    if left_mm is None and right_mm is None:
        distance_correction = 0
    elif left_mm is None:
        distance_correction = -SIDE_BALANCE_GAIN * right_mm
    elif right_mm is None:
        distance_correction = SIDE_BALANCE_GAIN * left_mm
    else:
        distance_correction = SIDE_BALANCE_GAIN * (left_mm - right_mm)

    heading_error = heading_deg - target_heading
    gyro_correction = -GYRO_HEADING_GAIN * heading_error
    return STEERING_CENTER_DEG + STEERING_SIGN * (distance_correction + gyro_correction)


def calculate_obstacle_avoidance(vision_result):
    """
    Convert OpenMV color/sign detection into a steering offset.

    The final values depend on field testing. This template uses conservative
    starter values that show the expected control path without claiming final
    behavior.
    """
    if vision_result == VISION_RED:
        return STEERING_LEFT_LIMIT_DEG * 0.55

    if vision_result == VISION_GREEN:
        return STEERING_RIGHT_LIMIT_DEG * 0.55

    return 0


def object_confirmed(front_mm, vision_result):
    return front_mm is not None and front_mm <= OBJECT_CONFIRM_DISTANCE_MM and vision_result != VISION_NONE


def run_obstacle_course():
    timer = StopWatch()
    target_heading = read_heading()

    while timer.time() < OBSTACLE_TIMEOUT_MS:
        left_mm = read_distance(left_sensor)
        front_mm = read_distance(front_sensor)
        right_mm = read_distance(right_sensor)
        heading_deg = read_heading()
        vision_result = read_openmv_result()

        base_steering = calculate_wall_and_heading_steering(
            left_mm,
            right_mm,
            heading_deg,
            target_heading,
        )
        obstacle_offset = calculate_obstacle_avoidance(vision_result)
        steering_target = base_steering + obstacle_offset

        if front_mm is not None and front_mm <= FRONT_STOP_MM and vision_result == VISION_NONE:
            hub.light.on(Color.RED)
            stop_robot()
        else:
            hub.light.on(Color.GREEN if vision_result == VISION_GREEN else Color.ORANGE)
            set_steering(steering_target)
            drive_motor.dc(APPROACH_POWER if object_confirmed(front_mm, vision_result) else DRIVE_POWER)

        print(
            "mode:obstacle",
            "left:",
            left_mm,
            "front:",
            front_mm,
            "right:",
            right_mm,
            "heading:",
            heading_deg,
            "vision:",
            vision_result,
        )
        wait(LOOP_PERIOD_MS)

    stop_robot()
    hub.light.on(Color.BLUE)
    print("Obstacle Course complete.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

center_steering()
wait_for_start()
reset_heading()

try:
    run_obstacle_course()
finally:
    stop_robot()
