from machine import I2C


class TCA9548:
    def __init__(self, i2c, address=0x71):
        self._i2c = i2c
        self._address = address


    def select(device_ndx):
        self._i2c.writeto_mem()