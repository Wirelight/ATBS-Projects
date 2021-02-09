#! python3
#  lookingBusy.py - Nudges the mouse cursor slightly every 10 seconds to prevent idle status.

import pyautogui, time

while True:
    time.sleep(10)
    pyautogui.move(1, 0, duration=0.25)
    pyautogui.move(-1, 0, duration=0.25)