import machine
import sys
import utime
import vl6180_Driver



def configureVL6180():
    print("entering vl6180 configuration program.")
    i2c = machine.I2C(-1,machine.Pin(22),machine.Pin(21))
    while(True):
        print("available addresses: " + str(i2c.scan()))
        current_addr = input("Give the current address of the sensor. Default is 41: ")
        target_addr = input("Now give the new address that you want to put the sensor in: ")
        try:
            current_sensor = vl6180_Driver.Sensor(i2c,int(current_addr))
            print("Current sensor at address " + current_addr + " initialized.")
            current_sensor.address(int(target_addr))
            print("Sensor address successfully configured to " + target_addr + ".")
        except:
            print("Something went wrong. Check settings.")