from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk,width=1000,height=1000)
canvas.pack()
canvas.create_polygon(80,80,180,80,80,200)
for i in range(0,10):
    canvas.move(1,10,0)
    tk.update()
    time.sleep(0.05)

for i in range(0,10):
    canvas.move(1,0,10)
    tk.update()
    time.sleep(0.05)

for i in range(0,10):
    canvas.move(1,-10,0)
    tk.update()
    time.sleep(0.05)

for i in range(0,10):
    canvas.move(1,0,-10)
    tk.update()
    time.sleep(0.05)

