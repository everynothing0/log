#!/usr/bin/python3

import mouse
import sys
import time

DELAY=30

while (True):
    try:
        mouse.move(1000, 500)
        time.sleep(DELAY)
        mouse.move(1000, 600)
        time.sleep(DELAY)
    except KeyboardInterrupt:
        sys.exit()
