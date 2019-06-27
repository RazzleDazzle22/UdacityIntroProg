##  Bryanna Armstrong
##  June 2019

import os
from random import choice 
import platform 
import time
from PIL import Image

def cls():
    var = platform.system() 
    if var == "Windows":
        os.system("cls")
    elif var == "Linux":
        os.system("clear")
    elif var == "Darwin":
        os.system("clear")

def printP(txt, pause=1):
    print(txt)
    time.sleep(pause)

def showImage(img):
    image = Image.open(img)
    image.show()

def start(player):
    player["room"] = 1
    printP("When you enter, you see priceless jewels and lavish decorations.")
    printP("To your right, there is a grand-golden staircase.")
    printP("To your left, there is a long-mysterious hallway.") 

    while True:
        print("Would you like to (1)Go up the stairs or (2)Walk down the hallway?")
        print("Enter 1 or 2.")
        x = input(" ")

        if x == "1":
            printP("You walk up the stairs.")
            room2(player)
            break
        elif x == "2":
            printP("You walk down the hallway.")
            printP("At the end, you see a strange door.")
            printP("Although you are nervous, you bravely enter.")
            room3(player)
            break 
        else:
            printP("Hmm...I did not understand that.") 

def room2(player):
    printP("At the top of the stairs, there is a tiny box.")
    opened = ""
    while True:
        print("Would you like to (1)Open the box " + opened + "or (2)Walk downstairs?") 
        print("Enter 1 or 2.")
        x = input('')

        if x == "1":
            printP("You open up the box and find a hidden clue.")
            showImage("clue.jpeg")
            printP("You put the clue back in the box.")
            opened = "again "

        elif x == "2":
            printP("You leave the box behind and walk downstairs.")
            start(player)
            break 
        else:
            printP("Hmm...I did not understand that.") 

def setup():
    player = {"room": 1, "win": False}
    cls()
    printP("Once upon a time, you were walking through the woods.")
    printP("Accidentally, you stumble across a magical castle.")
    printP("Your curiosity entails you to go inside.")
    start(player)

setup()
