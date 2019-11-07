'''
class A:
  def __init__(self):
    print("Enter A")
    print("Leave A")
class B(A):
  def __init__(self):
    print("Enter B")
    super(B, self).__init__()
    print("Leave B")
class C(A):
  def __init__(self):
    print("Enter C")
    super(C, self).__init__()
    print("Leave C")
class D(A):
  def __init__(self):
    print("Enter D")
    super(D, self).__init__()
    print("Leave D")
class E(B, C, D):
  def __init__(self):
    print("Enter E")
    super(E, self).__init__()
    print("Leave E")
E()
'''

'''
class A():
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")
class B(A):
    def go(self):
        super(B, self).go()
        print ("go B go!")
class C(A):
    def go(self):
        super(C, self).go()
        print ("go C go!")
    def stop(self):
        super(C, self).stop()
        print ("stop C stop!")
class D(B,C):
    def go(self):
        super(D, self).go()
        print ("go D go!")
    def stop(self):
        super(D, self).stop()
        print ("stop D stop!")
    def pause(self):
        print ("wait D wait!")
class E(B,C):
    pass
a = A()
b = B()
c = C()
d = D()
e = E()
# 说明下列代码的输出结果
a.go()
print('--------')
b.go()
print('--------')
c.go()
print('--------')
d.go()
print('--------')
e.go()
print('--------')
'''

class D :
    pass
class E :
    pass
class F :
    pass
class B(D,E) :
    pass
class C(D,F) :
    pass
class A(B,C) :
    pass
a = A()
A.__mro__
