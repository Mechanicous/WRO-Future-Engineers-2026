# Bill Of Materials

List the parts used to build the LEGO SPIKE Prime robot.

Actual team spending for the current robot is 0 USD because the parts used for MadBoy were already available to the team. The estimated costs below are replacement costs for another team trying to reproduce the same electronics in July 2026.

## Main Components

| Part | Quantity | Purpose | Actual Team Cost | Estimated Replacement Cost | Notes |
| --- | ---: | --- | ---: | ---: | --- |
| LEGO SPIKE Prime Hub | 1 | Main controller and power source | 0 USD | about 280 USD | Runs Pybricks MicroPython; market estimate |
| SPIKE Large Angular Motor | 1 | Rear-wheel drive | 0 USD | about 80 USD | Drives the rear differential gear system |
| SPIKE Medium Angular Motor | 1 | Front steering | 0 USD | about 90 USD | Controls the steering linkage |
| LEGO ultrasonic/distance sensor | 3 | Left, middle/front, and right distance sensing | 0 USD | about 150 USD total | Estimated at about 50 USD each |
| OpenMV H7 camera | 1 | Vision and red/green obstacle detection | 0 USD | about 69 USD | Communicates with SPIKE Prime Hub through UART on port C |
| LEGO wheels/tires | 4 | Movement | 0 USD | Already available / variable | Wheel diameter about 5.5 cm |
| LEGO Technic differential/gears | 1 set | Rear differential drive system | 0 USD | Already available / variable | 20-tooth drive gear, 28-tooth differential gear, three 12-tooth bevel gears |
| LEGO Technic beams/frames/pins/gears | 1 build set | Chassis and mounts | 0 USD | Already available / variable | Documented in `../models/Robot_Design.io` |

Estimated replacement subtotal for main electronics: about 669 USD.

## Power Components

| Part | Quantity | Voltage/Current | Notes |
| --- | ---: | --- | --- |
| SPIKE Prime rechargeable battery | 1 | Hub battery | Included with the SPIKE Prime Hub / available to team |
| SPIKE Prime charger/cable | 1 | Charging/upload support | Already available |

## Optional Or Future Components

| Part | Quantity | Purpose | Notes |
| --- | ---: | --- | --- |
| OpenMV communication hardware | 1 | Connect OpenMV H7 to SPIKE Prime Hub | UART communication on port C; PUPRemote/LPF2 used as Python libraries |
| Extra LEGO motor | 0 | Backup or later mechanism | Not used |

## Cost Sources

- LEGO 45601 Large Hub market estimate: BrickPicker / BrickEconomy market listings.
- LEGO 45602 Large Angular Motor estimate: reseller listings.
- LEGO 45603 Medium Angular Motor estimate: BricksDirect / BrickEconomy market listings.
- LEGO 45604 Distance Sensor estimate: Brickipedia MSRP, Investabrick, and current reseller listings.
- OpenMV H7 estimate: DigiKey OpenMV Cam H7 listing.

