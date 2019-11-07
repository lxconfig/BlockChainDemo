from tkinter import *
'''
def hello():
    print('hello world')
    
tk = Tk()
btn = Button(tk,text = "clike me",command=hello)
btn.pack()
'''

tk = Tk()
canvas = Canvas(tk,width=500,height=200)
canvas.pack()
canvas.create_line(0,0,500,200)

