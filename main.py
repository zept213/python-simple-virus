#!/usr/bin/env python3

import os
import sys
import subprocess

def cmd(command):
    subprocess.run(command, shell=True)

def main():
    cmd("echo 'hello world'")

if __name__ == '__main__':
    main()
