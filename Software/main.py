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



# Blink forever
while True:

    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        sys.exit()
    # Turn LED on and then off
    print("Available addresses: | " + str(i2c.scan()) + " | Value read in address 41: " + str(sensor1.range()))
    led.value(1)
    utime.sleep_ms(500)
    led.value(0)
    utime.sleep_ms(500)