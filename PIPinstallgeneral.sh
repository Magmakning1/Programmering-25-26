#!/bin/sh

# if on windows
# venv\Scripts\activate
os_name=$(uname)

python -m venv venv

case "$os_name" in
  Linux|Darwin)
    source venv/bin/activate
    ;;
  MINGW*|MSYS*|CYGWIN*)
    source venv/Scripts/activate
    ;;
  *)
    echo "Unknown OS: $os_name"
    exit 1
    ;;
esac

pip install keyboard tk mouse pyautogui
