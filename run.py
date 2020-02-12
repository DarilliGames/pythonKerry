import os
import env

print("Hello KERRRYYYYYYYY")


def gameLoop():
    task = input("What would you like to do - ")
    if task == os.environ.get("Super_Secret"):
        print("You win")

gameLoop()