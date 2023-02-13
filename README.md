Components used:
  raspberry pi 4 model B(8GB RAM),
  L298n, 4x tt gear motors, 4x wheels,
  2x 2600mAh 18650 Li-Ion batteries,
  13000mAh powerbank,
  USB-C cable,
  jumper wires,
  acrylic case

Steps to make this car:
  Step 1:
    Download the code in your raspberry pi(make sure all the files are in the same directory), install RPi.GPIO, pygame and time using " $ pip install RPi.GPIO pygame time ".
  Step 2:
    Assmeble the case and the components.
  Step 3:
    Connect the wires according to the RPIcarSchematic.png file.
  Step 4:
    After completing all the above steps, run main.py and you can control the car using WASD or ↑ → ↓ ← keys.

Controls:
  W or ↑:
    forward
  A or ←:
    left
  S or ↓:
    backward
  D or →:
    right
