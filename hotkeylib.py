import os
import keyboard
import subprocess
import sys
import platform
import time

__all__ = ['cmd_hotkey', 'program_hotkey', 'end_hotkey_list']

def _require_root():
    if platform.system() in ['Linux', 'Darwin']:
        if os.geteuid() != 0:
            print("[ERROR] This program needs root privileges.")
            sys.exit(0)
        else:
            print("[INFO] Running as root.")
    else:
        print("[INFO] No root privileges required on this platform.")

class cmd_hotkey:
    def __init__(self,key,command):
        _require_root()
        self.key = key
        self.command = command
        keyboard.add_hotkey(str(key),lambda: os.system(str(command)))
        print("command",command,"bound to",key)

class program_hotkey:
    def __init__(self,key,program):
        _require_root()
        self.key = key
        self.program = program
        if platform.system() in ['Linux', 'Darwin']:
             keyboard.add_hotkey(str(key),lambda: subprocess.Popen(["sudo", "-u", "#1000", str(program)]))
        else:  
            keyboard.add_hotkey(str(key),lambda: subprocess.Popen([str(program)],shell=True))
        print("program",program,"bound to",key)

class pyfunc_hotkey:
    def __init__(self,key,function):
        _require_root()
        self.key = key
        self.function = function
        keyboard.add_hotkey(str(key),function)
        print("function",function,"bound to",key)

def end_hotkey_list():
    print("Hotkey list running until esc pressed")
    keyboard.wait("esc")

def wait(keyortime="time",wait_time=10,key="esc"):
    if keyortime == "time":
        time.sleep(int(wait_time))
    elif keyortime == "key":
        keyboard.wait(str(key))
    else:
        print("[ERROR]",keyortime,"not an accepted str for keyortime")

if __name__ == "__main__":
    print("Hotkey list not meant to be run by itself. Please import to another file")