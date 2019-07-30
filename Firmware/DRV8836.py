import machine
import utime


class DRV8836:
    def __init__(self, A1, A2, B1, B2):  # takes in machine.PINs as params.
        self.A1 = machine.PWM(A1, freq=500)
        self.A2 = machine.PWM(A2, freq=500)
        self.B1 = machine.PWM(B1, freq=500)
        self.B2 = machine.PWM(B2, freq=500)

    def setLeft(self,speed):
        if(speed > 1024 or speed < -1024):
            print("Invalid speed entry. Value capped at +-1023.")
        elif(speed > 0):
            self.A1.duty(speed)
            self.A2.duty(0)
        elif(speed < 0):
            self.A1.duty(0)
            self.A2.duty(speed)

    def setRight(self,speed):
        if(speed > 1024 or speed < -1024):
            print("Invalid speed entry. Value capped at +-1023.")
        elif(speed > 0):
            self.B1.duty(speed)
            self.B2.duty(0)
        elif(speed < 0):
            self.B1.duty(0)
            self.B2.duty(speed)
    def stop(self):
        self.A1.duty(0)
        self.A2.duty(0)
        self.B1.duty(0)
        self.B2.duty(0)
            

    def testRun(self):
        for i in range(500):
            self.setLeft(i)
            self.setRight(100-i)
            utime.sleep_ms(10)
        self.stop()