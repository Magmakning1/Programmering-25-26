import os
import keyboard
import subprocess
import sys

__all__ = ['cmd_hotkey', 'program_hotkey', 'end_hotkey_list']

def _require_root():
    if os.geteuid() != 0:
        print("[ERROR] This program needs root privileges.")
        sys.exit(1)
    else:
        print("[INFO] Running as root.")

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
        keyboard.add_hotkey(str(key),lambda: subprocess.Popen(["sudo", "-u", "#1000", str(program)]))
        print("program",program,"bound to",key)

def end_hotkey_list():
    print("Hotkey list running until esc pressed")
    keyboard.wait("esc")

if __name__ == "__main__":
    print("Hotkey list not meant to be run by itself. Please import to another file")