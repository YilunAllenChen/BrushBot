import os
from time import sleep


mypath = "./Software/"

files = [f for f in os.listdir(mypath)]
print(files)

for file in files:
    print("Uploading " + file)
    try:
        os.system("ampy --port COM5 put " + mypath + file)
        print("Completed.")
    except:
        print("Failure.")
    sleep(1) #Give it a break
print("All files have been uploaded.")