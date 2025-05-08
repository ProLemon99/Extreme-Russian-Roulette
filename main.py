import os
import random

print("Before you get started, just know what you're getting yourself into.")
print("You must know that this script is extremely dangerous, as it will attempt to delete System32.")
print("You have a chance to turn back now. Or you could gamble.")
print("Note: you won't get anything in reward for being lucky either.")

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