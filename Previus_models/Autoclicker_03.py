import subprocess
import keyboard
import threading
import time 

active = False
clickerthread = None

def toggle():
    global active
    if not active:
        active = True
    else:
        active = False

def clicker():
    while True:
        if active:
            subprocess.run(["xdotool","click","1"])
            time.sleep(0.001)
        else:
            time.sleep(0.1)

keyboard.add_hotkey("delete", toggle)
clickerthread = threading.Thread(target=clicker, daemon=True)
clickerthread.start()
keyboard.wait()