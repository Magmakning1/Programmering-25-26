from easyturtle import *
import turtle
from random import randint
import time
import threading
import hotkeylib

scr = Screen(screensize=[750,750])
t1 = turtle.Turtle()
t1.speed(0)
t1.pensize(5)
t1.color(255,0,0)
toggled = False
running = True
x = 0
screensize = scr.getscreensize()

def toggle():
    global toggled
    if toggled:
        toggled = False
    else:
        toggled = True

def increace():
    global x, toggled, running
    while True:
        if running and toggled:
            x += 1
            time.sleep(0.5)
        else:
            time.sleep(0)

def cords():
    global x
    while True:
        if running:
            print(round(t1.xcor(),0),round(t1.ycor(),0),(" "),x)
            time.sleep(0.5)
        else:
            pass

def border():
    savedheading = t1.heading()
    t1.setheading(0)
    t1.teleport(-screensize[0] / 2,screensize[1] / 2)
    for i in range(2):
        t1.forward(screensize[0])
        t1.right(90)
        t1.forward(screensize[1])
        t1.right(90)       
    t1.teleport(0,0)
    t1.setheading(savedheading)

def setx0():
    global x, running
    running = False
    newx = input("[INPUT] Input int ")
    if newx == "":
        newx = 0
    x = abs(int(newx))
    running = True

border()
thread1 = threading.Thread(target=cords,daemon=True)
thread2 = threading.Thread(target=increace,daemon=True)
thread1.start()
thread2.start()
hotkey1 = hotkeylib.pyfunc_hotkey("delete",setx0)
hotkey2 = hotkeylib.pyfunc_hotkey("home",toggle)

while True:
    if running:    
        t1.color([randint(1,255),randint(1,255),randint(1,255)])
        t1.forward(10)
        t1.right(randint(-x,x))
        if t1.xcor() >= screensize[0] / 2 or t1.xcor() <= -(scr.screensize[0] / 2) or t1.ycor() >= screensize[1] / 2 or t1.ycor() <= -(scr.screensize[1] / 2):
            t1.teleport(0,0)
            t1.clear()
            border()
    else:
        pass
