'''
class Turtle :
    def __init__(self , x) :
        self.num = x

class Fish :
    def __init__(self , y) :
        self.num = y

class Pool :
    def __init__(self , x , y) :
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self) :
        print("鱼%s条，乌龟%s只" % (self.turtle.num , self.fish.num))

p = Pool(1,10)
p.print_num()
'''
'''
class A:
    def get_a(self):
        print ('a')

class B:
    def get_b(self):
        print ('b')

class C(A, B): 
    pass

a = A()
c = C()
c.get_a()
c.get_b()
A.__bases__ += (B,)
a.get_b()
'''

class PlugIn(object):
    def __init__(self):
        self._exported_methods = []
        
    def plugin(self, owner):
        for f in self._exported_methods:
            owner.__dict__[f.__name__] = f

    def plugout(self, owner):
        for f in self._exported_methods:
            del owner.__dict__[f.__name__]

class AFeature(PlugIn):
    def __init__(self):
        super(AFeature, self).__init__()
        self._exported_methods.append(self.get_a_value)

    def get_a_value(self):
        print ('a feature.')

class BFeature(PlugIn):
    def __init__(self):
        super(BFeature, self).__init__()
        self._exported_methods.append(self.get_b_value)

    def get_b_value(self):
        print ('b feature.')

class Combine:pass

c = Combine()
AFeature().plugin(c)
BFeature().plugin(c)

c.get_a_value()
c.get_b_value()
