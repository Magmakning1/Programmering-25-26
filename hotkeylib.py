import os
import keyboard
import subprocess

class cmd_hotkey:
    def __init__(self,key,command):
        self.key = key
        self.command = command
        keyboard.add_hotkey(str(key),lambda: os.system(str(command)))
        print("command",command,"bound to",key)

class program_hotkey:
    def __init__(self,key,program):
        self.key = key
        self.program = program
        keyboard.add_hotkey(str(key),lambda: subprocess.Popen(["sudo", "-u", "#1000", str(program)]))
        print("program",program,"bound to",key)

def end_hotkey_list():
    print("Hotkey list running until esc pressed")
    keyboard.wait("esc")

if __name__ == "__main__":
    print("Hotkey list not meant to be run by itself. Pleas import to another file")