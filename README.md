# BrushBot 2

This Repo serves the BrushBot 2.0 project from its hardware to its software.

## Project Structure
main.py: the program that ESP will execute once it boots up.\
ina219.py: Firmware for ina219 current sensor.\
vl6180Driver.py: Firmware for VL6180x sensor.\
logging.py: Supporting module for ina219 current sensor.\
DRV8836.py: Firmware for DRV8836 motor driver.

## Installation
Before the installation process begins, make sure your BrushBot is connected through FTDI to the computer.

You need to find the port connected to the BrushBot and replace "your_port" in the script below with that port. on Windows it should look like "COMx", mac "dev/xxxxx", linux "USB/ttyx".

Then run the script under the repo directory:

    python install.py your_port

The script provided by this repo will allow you to automatically install the dependencies of computer-brushbot interaction. Afterwards, it will attempt to installing the micropython firmware under the ./_MicroPython_bin directory to the BrushBot connected. This process involves erasing the flash and putting the bin file inside.

Once this is done, you can use the following script to automatically upload all your programs under ./Firmware directory to the robot. The your_port part is the same deal as the one with the install.py script.

    python Upload.py your_port



## INA219 Interface Example

```python
from ina219 import INA219
from machine import I2C

i2c = machine.I2C(-1,machine.Pin(22),machine.Pin(21)) #setup i2c
SHUNT_OHMS = 0.1 # Hardware setup - shunt resistance
ina = INA219(SHUNT_OHMS, i2c) # Create a sensor object
ina.configure() # Default configuration

# Usage
print("Bus Voltage: %.3f V" % ina.voltage())
print("Current: %.3f mA" % ina.current())
print("Power: %.3f mW" % ina.power())
```

## VL6180 Interface Example

```python
import machine
import sys
import utime
import vl6180_Driver

i2c = machine.I2C(-1,machine.Pin(22),machine.Pin(21)) #setup i2
sensor1 = vl6180_Driver.Sensor(i2c,41) # Create a sensor object

# Usage
print("Value read in address 41: " + str(sensor1.range()))
```


## DRV8836 Interface Example

```python
import machine #Required by machine.Pin
import DRV8836

A1 = machine.Pin(33) # Select the four pins used to control
A2 = machine.Pin(25) # the two motors
B1 = machine.Pin(26)
B2 = machine.Pin(27)
drv = DRV8836.DRV8836(A1, A2, B1, B2) # Create the motor driver object

# Usage
drv.testRun() # Test run function.
drv.setLeft(1000) # Set the motor output of left. -1023 ~ 1023.
drv.stop()
```

## TCP-IP
Note: In order for the Controller to work, the server side computer needs to allow TCP/IP inbound/outbound connections on port 23.
