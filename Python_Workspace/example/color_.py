import turtle
t = turtle.Pen()
#t.color(1,1,0)
#t.begin_fill()
#t.circle(120)
#t.end_fill()


def MyCircle(red,green,blue):
    t.color(red,green,blue)
    t.begin_fill()
    t.circle(100)
    t.end_fill()


#t.color(0.9,0.75,0)
#t.begin_fill()
#for i in range(1,19):
#    t.forward(100)
#    if i % 2 == 0:
#        t.left(175)
#    else:
#        t.left(225)
#t.end_fill()

#t.color(0,0,0)
#t.begin_fill()
#t.end_fill()


def share(size,fill):
#    t.color(1,0.38,0.35)
    if fill == True:
        t.begin_fill()
    for i in range(1,9):
        t.forward(size)
        t.left(45)
    t.end_fill()




def MyStar(size,points):
    for i in range(1,points):
        t.forward(100)
        if i % 2 == 0:
            t.left(175)
        else:
            t.left(225)
