import random
from tkinter import *
'''
tk = Tk()
canvas = Canvas(width=800,height=800)
canvas.pack()

def random_rectangle():
    print("please enter the numbers that you want to generate:")
    t = int(input())
    weight = random.randint(1,800)
    height = random.randint(1,800)
    for i in range(0,t):
        x1 = random.randrange(weight)
        y1 = random.randrange(height)
        x2 = random.randrange(weight)
        y2 = random.randrange(height)
        canvas.create_rectangle(x1,y1,x2,y2)

button = Button(tk,text='press',command=random_rectangle)
button.pack()
'''


tk = Tk()
canvas = Canvas(width=800,height=800)
canvas.pack()
def random_rectangle(width,height,fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(width)
    y2 = random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2,fill=fill_color)

random_rectangle(800,800,'#6fd2af')
