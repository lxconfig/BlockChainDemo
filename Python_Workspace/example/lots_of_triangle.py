from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk,width=800,height=800)
canvas.pack()
colors = ['red','black','green','blue','yellow','orange','purple']
def Triangle(width,height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(width)
    y2 = random.randrange(height)
    x3 = random.randrange(width)
    y3 = random.randrange(height)
    color = random.choice(colors)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill=color)

for i in range(0,100):
    Triangle(800,800)
