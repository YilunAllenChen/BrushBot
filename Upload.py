import os
from time import sleep

port = "COM5"

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