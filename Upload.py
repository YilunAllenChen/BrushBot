import os, sys
from time import sleep

port = "Invalid_port"


try:
    port = str(sys.argv[1])
    print(port)
except:
    print("Invalid Port")


mypath = "./Firmware/"

files = [f for f in os.listdir(mypath)]
print(files)

for file in files:
    print("Uploading " + file)
    try:
        os.system("ampy --port " + port + " put " + mypath + file)
        print("Completed.")
    except:
        print("Failure.")
    sleep(1) #Give it a break between program writes.
print("All files have been uploaded.")