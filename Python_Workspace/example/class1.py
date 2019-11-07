'''
import turtle
avery=turtle.Pen()
kate=turtle.Pen()


avery.forward(100)
avery.left(60)
avery.forward(50)

kate.backward(150)
kate.right(120)
kate.forward(40)
'''

class Giraffes:
    def fun1(self):
        print("left foot forward")
    def fun2(self):
        print("right foot forward")
    def fun3(self):
        print("forward foot forward")
    def fun4(self):
        print("backward foot forward")
    def dance(self):
        self.fun1()
        self.fun2()
        self.fun3()
        self.fun4()
gg=Giraffes()
gg.dance()


import turtle
Tom=turtle.Pen()
Kate=turtle.Pen()
Michael=turtle.Pen()
Jonh=turtle.Pen()
#上短
Tom.forward(100)
Tom.left(90)
Tom.forward(30)
Tom.right(90)
Tom.forward(20)
#下短
Jonh.forward(100)
Jonh.right(90)
Jonh.forward(30)
Jonh.left(90)
Jonh.forward(20)
#上长
Kate.forward(80)
Kate.left(90)
Kate.forward(80)
Kate.right(90)
Kate.forward(50)
#下长
Michael.forward(80)
Michael.right(90)
Michael.forward(80)
Michael.left(90)
Michael.forward(50)

