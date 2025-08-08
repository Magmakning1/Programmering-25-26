import keyboard
import pyautogui
import random
import threading
import time
from custom_pyautogui import *

set_pos = False #Virker ikke ennå
if set_pos:
    xcor, ycor = input("Xcor = ? "), input("Ycor = ? ")

random_clicks = False
clicks = 100
repeats = 1

stop_flag = False
active = False
clicker_thread = None

if repeats <= -1 and clicks >= 11:
    clicks = 10
if clicks >= 20 and repeats >= 6:
    repeats = 5

def set_posXY(x,y):
    pyautogui.moveTo(x,y)
    time.sleep(0.01)

def autoclicker():
    global clicks, stop_flag
    stop_flag = False

    def get_clicks():
        return random.randint(0, 3) if random_clicks else clicks

    if repeats <= -1:
        while not stop_flag:
            current_clicks = get_clicks()
            for _ in range(current_clicks):
                pyautogui.click()
            time.sleep(0.01)
    else:
        for _ in range(int(repeats)):
            if stop_flag:
                break
            current_clicks = get_clicks()
            for _ in range(current_clicks):
                if stop_flag:
                    break
                pyautogui.click()
            if stop_flag:
                break

def toggle_autoclicker():
    global active, stop_flag, clicker_thread
    if not active:
        print("Starting autoclicker")
        stop_flag = False
        clicker_thread = threading.Thread(target=autoclicker, daemon=True)
        clicker_thread.start()
        active = True
        if set_pos:
            set_posXY(int(xcor),int(ycor))
        else:
            pass
    else:
        print("Stopping autoclicker")
        stop_flag = True
        active = False
        if set_pos:
            set_posXY(int(xcor),int(ycor))
        else:
            pass


keyboard.add_hotkey("delete", toggle_autoclicker)

keyboard.wait()
