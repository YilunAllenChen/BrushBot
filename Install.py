import os, sys

port = "invalid_port"

try:
    port = str(sys.argv[1])
    print(port)
except:
    print("Invalid Port")


print("Installing esptool...\n")
os.system("pip install esptool pynput")
print("\nInstallation Complete.\n\n Erasing Flash on ESP32 Chip...\n")
try:
    os.system("esptool.py --port " + port + " erase_flash")
    print("\nErase Complete. Now installing bin file...\n")
    os.system("esptool.py --chip esp32 --port " + port + " write_flash -z 0x1000 ./_MicroPython_bin/esp32-20190612-v1.11-44-g8b18cfede.bin")

except:
    print("Failed to install. Check your settings.")
