import machine
import neopixel
import sys
import utime
import vl6180
import DRV8836
from ina219 import INA219
#from configureVL6180 import configureVL6180   #archived.


############    Initiazation Settings - Don't Change    ######################
print("\nInitializing devices...\n")

# Default Reset Pin Definition. Don't Change.
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
#Sensor-enable Initialization
sensor_en = machine.Pin(18, machine.Pin.OUT)
sensor_en.value(1)
#Motor-enable Initialization
sensor_en = machine.Pin(19, machine.Pin.OUT)
sensor_en.value(1)
#I2C Definition. Don't change.
myi2c = machine.I2C(-1,machine.Pin(22),machine.Pin(21))
# Default LED pin. Bot Running Indicator. This LED is right to the left of the ESP board.
led = machine.Pin(32, machine.Pin.OUT)
#LED neoPixel on Pin 37 setup
try:
    neoPixel = neopixel.NeoPixel(machine.Pin(23),2)
    print("\033[92m{}\033[00m" .format("Successfully") + " configured neoPixels")
except:
    print("\033[91m{}\033[00m".format("Failed") + " to configure neoPixels")

# Laser Sensor Initialization
sensors = []
for addr in range (41,48):  # VL6180 sensors should be on i2c addresses 41-48.
    try:
        sensors.append(vl6180.Sensor(myi2c,addr))
        print("\033[92m{}\033[00m" .format("Successfully") + " configured VL6180x sensor at address " + str(addr))
    except:
        print("\033[91m{}\033[00m".format("Failed") + " to initialize VL6180x sensor on i2c address " + str(addr))
# Current Sensor Initialization
shunt_resistance = 0.05      # Change if needed
try:
    ina = INA219(shunt_resistance, myi2c)
    ina.configure()
    print("\033[92m{}\033[00m".format("Successfully") + " configured INA219 sensor at address " + str(ina._address))
except:
    print("\033[91m{}\033[00m".format("Failed") + " to initialize INA219 sensor on address 65.")

try:
    drv = DRV8836.DRV8836(machine.Pin(33),machine.Pin(25),machine.Pin(26),machine.Pin(27))
except Exception as e: print(e)

    
####################    End of Initialization   ################################

# Blink forever
while True:

    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        sys.exit()
    
    
    
    
    #Display all avaiable I2C addresses
    print("Available addresses: | " + str(myi2c.scan()))


    for ndx in range(len(sensors)):
        try:
            print("Sensor " + str(ndx) + " reading: " + str(sensors[ndx].range()))
        except:
            print("Sensor " + str(ndx) + " doesn't work.")

    try:
        print("Bus Voltage: %.3f V" % ina.voltage())
        print("Current: %.3f mA" % ina.current())
        print("Power: %.3f mW" % ina.power())
        print("Current Overflow? " + str(ina.current_overflow()))
    except:
        print("\033[92m {}\033[00m".format("INA219 sensor is malfunctioning."))
    

    
    # Turn LED on and then off
    led.value(1)
    neoPixel[1] = (0,0,10)
    neoPixel[0] = (0,10,0)
    neoPixel.write()
    utime.sleep_ms(500)
    
    led.value(0)
    neoPixel[1] = (0,10,0)
    neoPixel[0] = (0,0,10)
    neoPixel.write()
    utime.sleep_ms(500)
    
