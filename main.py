#!/usr/bin/env python3

import os
import sys
import subprocess

def goodbye():
    while i < 5:
        # DISCLAIMER: Mapupunta sa blue screen ang computer mo gago. 
        print("Goodbye...")
        os.system("echo 'Hello'")

if __name__ == '__main__':
    i = 1
    yes = True
    x = input("Oh, Press enter muna bago masira buhay mo...")
    if x == '':
        y = input("Sigurado ka ba diyan? [y/N] ")
        if y == '':
            exit(1)
        elif y == 'y':
            goodbye()
        elif y == 'n':
            exit(1)


