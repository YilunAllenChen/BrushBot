import machine, neopixel, sys, utime # System libraries
import vl6180, DRV8836, networking
from ina219 import INA219 # Customized Libraries




# from configureVL6180 import configureVL6180   #archived.


############    Initiazation Settings - Don't Change    ######################
print("\nInitializing devices. The red LED on the robot should light up.\n")

# WiFi Connections
try:
    wlan = networking.connect('allenchen_hotspot', 'allenchen')
    socket = networking.connect_socket('192.168.137.1')
except:
    print("\033[91m{}\033[00m".format("Failed") + " to connect to hotspot.")



# Default Reset Pin Definition. Don't Change.
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)


# Sensor-enable Initialization
sensor_en = machine.Pin(19, machine.Pin.OUT)
sensor_en.value(0)


# I2C Definition. Don't change.
myi2c = machine.I2C(-1, machine.Pin(22), machine.Pin(21))


# Default LED pin. Bot Running Indicator. This LED is right to the left of the ESP board.
led = machine.Pin(32, machine.Pin.OUT)
led.value(1)


# LED neoPixel on Pin 37 setup
try:
    neoPixel = neopixel.NeoPixel(machine.Pin(23), 2)
    print("\033[92m{}\033[00m" .format(
        "Successfully") + " configured neoPixels")
except:
    print("\033[91m{}\033[00m".format("Failed") + " to configure neoPixels")

utime.sleep(1)


# Laser Sensor Initialization
sensors = []
for addr in range(1, 8):  # VL6180 sensors should be on i2c addresses 41-48.
    try:
        sensors.append(vl6180.Sensor(myi2c))
        print("\033[92m{}\033[00m" .format("Successfully") +
              " configured VL6180x sensor at address " + str(addr))
    except:
        print("\033[91m{}\033[00m".format("Failed") +
              " to initialize VL6180x sensor on i2c address " + str(addr))

utime.sleep(0.2)

# Current Sensor Initialization
shunt_resistance = 0.05      # Change if needed
try:
    ina = INA219(shunt_resistance, myi2c)
    ina.configure()
    print("\033[92m{}\033[00m".format("Successfully") +
          " configured INA219 sensor at address " + str(ina._address))
except:
    print("\033[91m{}\033[00m".format("Failed") +
          " to initialize INA219 sensor on address 65.")

utime.sleep(0.2)

# Motor Driver Initialization
try:
    drv = DRV8836.DRV8836(machine.Pin(33), machine.Pin(25),
                          machine.Pin(26), machine.Pin(27))
    drv.stop()
    motor_en = machine.Pin(18, machine.Pin.OUT)
    motor_en.value(1)
except Exception as e:
    print(e)

utime.sleep(0.2)


####################    End of Initialization   ################################



dataCount = 0

# Blink forever
while True:

    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        sys.exit()

    # Display all avaiable I2C addresses
    print("Available addresses: | " + str(myi2c.scan()))

    for ndx in range(len(sensors)):
        try:
            print("Sensor " + str(ndx) + " reading: " +
                  str(sensors[ndx].range()))
        except:
            print("Sensor " + str(ndx) + " doesn't work.")

    # try to print the values given by the current sensor.
    try:
        data = "Bus Voltage: %.3f" % ina.voltage() + "  |  Current: %.3f mA" % ina.current() + "  |  Power: %.3f mW" % ina.power()
        print(data)
        socket.sendall(data.encode())
        dataCount = dataCount + 1
    except:
        print("\033[92m {}\033[00m".format("INA219 sensor is malfunctioning."))

    # Turn LED on and then off
    neoPixel[1] = (0, 0, 10)
    neoPixel[0] = (0, 10, 0)
    neoPixel.write()
    utime.sleep_ms(1000)
    drv.setLeft(1000)
    drv.setRight(1000)

    neoPixel[1] = (0, 10, 0)
    neoPixel[0] = (0, 0, 10)
    neoPixel.write()

    utime.sleep_ms(1000)
    drv.stop()

    if dataCount >= 10:
        socket.close()