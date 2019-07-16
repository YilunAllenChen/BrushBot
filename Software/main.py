import machine
import sys
import utime
import vl6180_Driver
from ina219 import INA219

#I2C Definition. Don't change.
i2c = machine.I2C(-1,machine.Pin(22),machine.Pin(21))

# Default Reset Pin Definition. Don't Change.
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

# Default LED Pin Definition on the SparkFun board. For testing purposes.
led = machine.Pin(5, machine.Pin.OUT)

# Laser Sensor Initialization
sensors = []
for addr in range (41, 48):  # VL6180 sensors should be on i2c addresses 41-48.
    try:
        sensors[addr-41] = vl6180_Driver.Sensor(i2c,addr)
        print("VL6180x sensor at address " + str(addr) + " is configured successfully." )
    except:
        print("Unable to initialize VL6180x sensor on i2c address " + str(addr))

# Current Sensor Initialization
shunt_resistance = 0.1      # Change if needed
try:
    ina = INA219(shunt_resistance, i2c)
    ina.configure()
    print("INA219 sensor at address 65 is configured successfully.")
except:
    print("Unable to initialize INA219 sensor on address 65.")

# Blink forever
while True:

    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        sys.exit()
    # Turn LED on and then off
    print("Available addresses: | " + str(i2c.scan()))
    try:
        print("    Sensor 1: " + str(sensor1.range()))
        print("    Sensor 2: " + str(sensor2.range()))
    except:
        print("one of the VL6180x sensors doesn't work.")

    try:
        print("Bus Voltage: %.3f V" % ina.voltage())
        print("Current: %.3f mA" % ina.current())
        print("Power: %.3f mW" % ina.power())
        print("Current Overflow? " + str(ina.current_overflow()))
    except:
        print("INA219 sensor is malfunctioning.")
    
    led.value(1)
    utime.sleep_ms(500)
    led.value(0)
    utime.sleep_ms(500)