from tkinter import *
import time
import random

class Ball:
    def __init__(self,canvas,paddle,color):   #重写init方法，此方法在实例化对象时会自动调用，并将实例名（对象名）赋值给self，另外两个参数都是自定义的，实例化必须赋值的。
        self.canvas = canvas  #canvas就是画好的窗口对象
        self.paddle = paddle
        self.id = canvas.create_oval(80,80,25,25,fill = color)  #create_oval()函数用来绘制椭圆
        self.canvas.move(self.id,245,100)  #让椭圆移动到画布中心
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]  #自定义x坐标
        self.y = -3 #自定义y坐标
        self.canvas_height = self.canvas.winfo_height()  #获取当前画布的高度，并赋值给canvas_height变量
        self.canvas_width = self.canvas.winfo_width()    #获取当前画布的宽度，并赋值给canvas_width变量

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[0] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
            if pos[3] <= paddle_pos[3] and pos[3] >= paddle_pos[1]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y) #让小球动起来
        pos = self.canvas.coords(self.id)  #利用coords(id)函数,以列表的形式返回小球的四个坐标[x1,y1,x2,y2]
        if pos[1] <= 0:  #如果y1的坐标小于等于0，即小球的顶部走出了窗口，是则重新设置y=1，正数代表向下移动
            self.y = 3
        if pos[3] >= self.canvas_height:  #如果y2的坐标大于等于画布的高度，重新设置y=-1，负数代表向上移动
            self.y = -3
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:   #如果x1的坐标小于等于0，则重新设置为3，正数代表向右移动
            self.x = 3
        if pos[2] >= self.canvas_width:  #如果x2的坐标大于等于画布的宽度，重新设置为-3，负数代表向左移动
            self.x = -3

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10,10,300,50,fill=color)
        self.canvas.move(self.id,250,400)    #将球拍移动到画布中间
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()  #获取画布宽度
        self.canvas_height = self.canvas.winfo_height() #获取画布高度
        
        self.canvas.bind_all('<KeyPress-Up>',self.turn_up)        #将up键绑定到函数turn_up上，即按下up时，调用turn_up函数
        self.canvas.bind_all('<KeyPress-Down>',self.turn_down)
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)  #让球拍动起来
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
        
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0
        
    def turn_up(self,event):  #球拍向上动
        self.y = -2
        
    def turn_down(self,event):
        self.y = 2
    
    def turn_left(self,event):
        self.x = -2
        
    def turn_right(self,event):
        self.x = 2

tk = Tk()
tk.title("Game")  #设置窗体标题
tk.resizable(0,0) #窗体不可改变大小
tk.wm_attributes('-topmost',1) #窗体默认在最前端
canvas = Canvas(tk,width=800,height=800,bd=0,highlightthickness=0)
canvas.pack()
tk.update()  #强制刷新图形，缺少会出问题

paddle = Paddle(canvas,'gold')
ball = Ball(canvas,paddle,'blue') #实例化一个Ball对象，会调用__init__函数

while 1:   #程序的主循环（直到关闭窗体前），不停的画窗体 
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
