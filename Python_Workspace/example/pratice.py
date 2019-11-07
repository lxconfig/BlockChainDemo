from tkinter import *
import time
import random
class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(250,250,200,200,fill=color)
        nums = [1,2,3,4,5,-1,-2,-3,-4,-5]
        random.shuffle(nums)
        self.x = nums[0]
        self.y = -10
        self.height = self.canvas.winfo_height()
        self.width = self.canvas.winfo_width()

    def Move(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 10
        if pos[3] >= self.height:
            self.y = -10
        if pos[0] <= 0:
            self.x = 10
        if pos[2] >= self.width:
            self.x = -10

tk = Tk()
tk.title("弹球游戏")
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk,width=1000,height=1000)
canvas.pack()
tk.update()
ball = Ball(canvas,'gold')

while 1 :
    ball.Move()
    tk.update()
    time.sleep(0.01)
