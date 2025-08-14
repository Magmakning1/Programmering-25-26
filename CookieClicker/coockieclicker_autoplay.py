import pyautogui
from PIL import Image
import time
import threading
import hotkeylib
from golden_cookie_colors import mainlist

spilloverTrue = False
waittime = 0

toggled = False
screenshot = None
found = None
generation = 0
foundgens = []

def toggle():
    global toggled
    if toggled:
        toggled = False
        print("Deactivated")
    else:
        toggled = True
        print("Activated")

def spillover():
    global generation, spilloverTrue
    if spilloverTrue:
        if generation >= 10:
            generation = 0
        else:
            pass
    else:
        pass

def colorfinder():
    global screenshot, img, width, height, found, waittime, generation, foundgens
    while True:
        if toggled:
            screenshot = pyautogui.screenshot()
            img = screenshot.convert("RGB")
            width, height = img.size

            for x in range(width // 2,width):
                for y in range(height // 2):
                    if img.getpixel((x,y)) in mainlist:
                        found = (x,y)
                        generation += 1
                        spillover()
                        print(f"Found clicking golden cookie. Gen= {generation}")
                        foundgens.append(generation)
                        break
                if found:
                    break
            if found:
                pyautogui.click(x=found[0],y=found[1])
                found = None
                time.sleep(waittime)
            else:
                generation += 1
                spillover()
                pyautogui.click(x=1100,y=200,clicks=5,interval=0.05)
                print(f"Not Found. Clicking main cookie. Gen= {generation}")
                time.sleep(waittime)
        else:
            time.sleep(1)
hotkeylib.pyfunc_hotkey("delete",toggle)
hotkeylib.pyfunc_hotkey("home",lambda: print(foundgens))
thread1 = threading.Thread(target=colorfinder,daemon=True)
thread1.start()
hotkeylib.wait("key","esc")