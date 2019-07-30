# BrushBot 2

This Repo serves the BrushBot 2.0 project from its hardware to its software.

## Project Structure
main.py: the program that ESP will execute once it boots up.\
ina219.py: Firmware for ina219 current sensor.\
vl6180Driver.py: Firmware for VL6180x sensor.\
logging.py: Supporting module for ina219 current sensor.
DRV8836.py: Firmware for DRV8836 motor driver.

## Installation
    pip install adafruit-ampy esptool
Then after the these two pip packages are installed, you can modify the files as you need. Once done modifying, connect the esp board to the computer, then run the following command to upload all files under 'Softare' to ESP.

    python Upload.py
If any error occurs, change the 'port' variable in the program into whatever the port is.



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

# Ssage
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