"""
This file contains minor decorative functions like loading animation and other stuff
Delete/Modify it if u want to, idc
"""

#Imports
from time import sleep

def loading():
    print("Delaying", end='')
    for _ in range(3):
        sleep(.5)
        print('.', end='')
        print('', flush=True, end='')
    print('')