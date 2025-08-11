import turtle

class Screen:

    def __init__(self, screensize: int, color):
        self.screensize = screensize
        self.colormode = 255
        self.color = color
        print(f"Screen made: size= {screensize}, colormode= {self.colormode}")

        self.screen = turtle.Screen()
        self.screen.setup(screensize, screensize)
        self.screen.screensize(screensize * 2, screensize * 2)
        self.screen.colormode(self.colormode)
        self.screen.bgcolor(self.color)

    def mainloop(self):
        while True:
            self.screen.update()

    def screensize(self):
        return self.screensize

class Turtle:

    def __init__(self, speed: int, color, pensize: int, ishidden: bool):
        self.speed = speed
        self.color = color
        self.pensize = pensize
        self.ishidden = ishidden

        self.turtle = turtle.Turtle()
        self.turtle.speed(self.speed)
        self.turtle.pensize(self.pensize)
        self.turtle.color(self.color)
        if ishidden:
            self.turtle.hideturtle()
        if not ishidden:
            self.turtle.showturtle()

    def move(self, heading, distance):
        self.turtle.setheading(heading)
        self.turtle.forward(distance)

    def goto(self, x, y):
        self.turtle.goto(x,y)

    def tp(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x,y)
        self.turtle.pendown()

    def setx(self, x):
        self.turtle.setx(x)

    def sety(self, y):
        self.turtle.sety(y)

    def xcor(self):
        return self.turtle.xcor()

    def ycor(self):
        return self.turtle.ycor()

    def heading(self):
        return self.turtle.heading()
