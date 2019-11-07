from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=800,height=800)
canvas.pack()
canvas.create_rectangle(10,10,200,200)
canvas.create_arc(10,10,200,200,extent=359,style=ARC)
canvas.create_polygon(40,40,300,40,300,90,fill='',outline='blue')
canvas.create_polygon(80,60,100,20,88,90,34,535,fill='pink',outline='yellow')
canvas.create_polygon(110,29,550,32,99,40,11,255,33,555,fill='pink',outline='yellow')

canvas.create_text(500,500,text='woow,ohho',fill='green',font=('幼圆',30))
my_image = PhotoImage(file='C:\\Users\\b\\Desktop\\loadgif.gif')
canvas.create_image(700,700,anchor=CENTER,image=my_image)
