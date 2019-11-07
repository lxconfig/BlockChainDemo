from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk,width=1000,height=1000)
canvas.pack()
c = canvas.create_polygon(10,10,10,60,50,35)
'''
print(c)
for x in range(0,60):
    canvas.move(1,5,5)
    tk.update()
    time.sleep(0.05)
for x in range(0,60):
    canvas.move(1,-5,-5)
    tk.update()
    time.sleep(0.05)


def  moveTriangle(event):
    canvas.move(1,5,5)
canvas.bind_all('<KeyPress-t>',moveTriangle)

def moveTriangle(event):
    if event.keysym == 'Up':
        canvas.move(1,0,-3)
    elif event.keysym == 'Down':
        canvas.move(1,0,3)
    elif event.keysym == 'Left':
        canvas.move(1,-3,0)
    elif event.keysym == 'Right':
        canvas.move(1,3,0)
canvas.bind_all('<KeyPress-Up>',moveTriangle)
canvas.bind_all('<KeyPress-Down>',moveTriangle)
canvas.bind_all('<KeyPress-Left>',moveTriangle)
canvas.bind_all('<KeyPress-Right>',moveTriangle)
'''

for x in range(0,60):
    canvas.move(1,0,-5)
    tk.update()
    time.sleep(0.05)
