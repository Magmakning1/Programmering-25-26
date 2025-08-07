import turtle

screensize = [700,400]
class Screen:
    def __init__(self,screensize=[700,700],bgcolor=[0,0,0]):
        self.screensize = screensize
        self.color = bgcolor
        self.screen = turtle.Screen()
        self.screen.setup(screensize[0],screensize[1])
        self.screen.screensize(screensize[0],screensize[1])
        self.screen.colormode(255)
        self.screen.bgcolor(bgcolor[0],bgcolor[1],bgcolor[2])
    
    def mainloop(self):
        self.screen.mainloop()