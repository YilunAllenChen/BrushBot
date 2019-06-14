import machine
import sys
import utime

# Pin definitions
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

# Wait for button 0 to be pressed, and then exit
while True:

    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        sys.exit()

    # Do nothing
    utime.sleep_ms(1)
