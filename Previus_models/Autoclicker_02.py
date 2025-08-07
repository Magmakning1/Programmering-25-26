import keyboard
import pyautogui
from Custom_libs import custom_pyautogui
import threading
import time
from config_02 import cps, randomcps, speed, ultimatespeed
import random

active = False

def get_cps():
    return random.randint(0,3) if randomcps else cps
def get_speed():
    global speed
    if speed <= 0:
        speed = 1
    if speed >= 101:
        speed = 100
    a = speed - 100
    b = abs(a)
    c = b / 100
    return c

activespeed = get_speed()
def toggle():
    global active
    if not active:
        active = True
    else:
        active = False

keyboard.add_hotkey("delete", toggle)

while True:
    global ultimatespeed
    if active:
        activecps = get_cps()
        pyautogui.click(clicks=activecps)
        if ultimatespeed:
            pass
        else:
            time.sleep(float(activespeed))
    else:
        pass