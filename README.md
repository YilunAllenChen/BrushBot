# BrushBot 2.0

This Repo serves the BrushBot 2.0 project from its hardware to its software.

##INA219 Interface Example

```python
from ina219 import INA219
from machine import I2C

I2C_INTERFACE_NO = 2
SHUNT_OHMS = 0.1

ina = INA219(SHUNT_OHMS, I2C(I2C_INTERFACE_NO))
ina.configure()
print("Bus Voltage: %.3f V" % ina.voltage())
print("Current: %.3f mA" % ina.current())
print("Power: %.3f mW" % ina.power())
```

##VL6180 Interface Example

```python
import machine
import sys
import utime
import vl6180_Driver

#I2C Definition. Don't change.
i2c = machine.I2C(-1,machine.Pin(22),machine.Pin(21))

# Default Reset Pin Definition. Don't Change.
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

# Default LED Pin Definition on the SparkFun board. For testing purposes.
led = machine.Pin(5, machine.Pin.OUT)

# Laser Sensor Initialization
sensor1 = vl6180_Driver.Sensor(i2c,41)

# Print the value read by using .range() function, returns in mm.
print("Value read in address 41: " + str(sensor1.range()))
```