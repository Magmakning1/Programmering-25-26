import sys
import os
import platform
import subprocess

os.system(f"{sys.executable} -m venv venv")

if platform.system() in ['Linux', 'Darwin']:
    python_bin = './venv/bin/python'
else:
    python_bin = '.\\venv\\Scripts\\python.exe'

subprocess.run([python_bin, '-m', 'pip', 'install', 'keyboard', 'tk', 'mouse', 'pyautogui'], check=True)
sys.exit(0)