from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk,width=1000,height=1000)
canvas.pack()

picture = PhotoImage(file='C:\\Users\\b\\Desktop\\loadgif.gif')
canvas.create_image(100,100,anchor=NW,image=picture)

for i in range(0,10):
    canvas.move(1,10,10)
    tk.update()
    time.sleep(0.05)

def Move_picture(event):
    if event.keysym == 'W':
        canvas.move(1,0,-10)
    elif event.keysym == 'S':
        canvas.move(1,0,10)
    elif event.keysym == 'A':
        canvas.move(1,-10,0)
    elif event.keysym == 'D':
        canvas.move(1,10,0)
canvas.bind_all('<KeyPress-W>',Move_picture)
canvas.bind_all('<KeyPress-S>',Move_picture)
canvas.bind_all('<KeyPress-A>',Move_picture)
canvas.bind_all('<KeyPress-D>',Move_picture)
