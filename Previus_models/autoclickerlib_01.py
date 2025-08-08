import keyboard
import pyautogui
import time
import threading

toggled = False

class Autoclicker:
    _instance_exists = False

    def __init__(self,activatekey,cpc):
        if Autoclicker._instance_exists:
            raise Exception("Error: Only one Autoclicker instance is allowed.")
        Autoclicker._instance_exists = True
        
        print("Autoclicker activated")
        self.cpc = cpc
        self.activatekey = activatekey
        self.thread01 = None
        keyboard.add_hotkey(str(activatekey),self.toggle)
        thread01 = threading.Thread(target=self.clicker,daemon=True)
        thread01.start()
        print("Press esc to quit")
        keyboard.wait("esc")

    def clicker(self):
        global toggled
        while True:
            if toggled:
                pyautogui.click(clicks=int(self.cpc))
                time.sleep(0.001)
            else:
                time.sleep(0.001)
            
    def toggle(self):
        global toggled
        if toggled:
            toggled = False
        else:
            toggled = True
