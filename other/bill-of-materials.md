# Bill Of Materials

List the parts used to build the LEGO SPIKE Prime robot.

## Main Components

| Part | Quantity | Purpose | Notes |
| --- | ---: | --- | --- |
| LEGO SPIKE Prime Hub | 1 | Main controller and power source | Runs Pybricks MicroPython |
| SPIKE Large Angular Motor | 1 | Rear-wheel drive | Drives the rear differential gear system |
| SPIKE Medium Angular Motor | 1 | Front steering | Controls the steering linkage |
| LEGO ultrasonic sensor | 3 | Left, middle/front, and right distance sensing | Current sensor set |
| OpenMV H7 camera | 1 | Vision and red/green obstacle detection | Communicates with SPIKE Prime Hub through UART on port C |
| LEGO wheels/tires | TODO | Movement | Document diameter and tire type |
| LEGO Technic differential/gears | TODO | Rear differential drive system | Document gear ratio and layout |
| LEGO Technic beams/frames/pins/gears | TODO | Chassis and mounts | Add model/build photos |

## Power Components

| Part | Quantity | Voltage/Current | Notes |
| --- | ---: | --- | --- |
| SPIKE Prime rechargeable battery | 1 | Hub battery | Powers hub, motors, and sensors |
| SPIKE Prime charger/cable | 1 | Charging/upload support | TODO |

## Optional Or Future Components

| Part | Quantity | Purpose | Notes |
| --- | ---: | --- | --- |
| OpenMV communication hardware | 1 | Connect OpenMV H7 to SPIKE Prime Hub | UART communication on port C; PUPRemote/LPF2 used as Python libraries |
| Extra LEGO motor | TODO | Backup or later mechanism | TODO |

