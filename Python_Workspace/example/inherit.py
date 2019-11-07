'''
class Parent:
    def hello(self):
        print("I am your parent")

class Father:
    def hello(self):
        print("I am your father")

class Son(Father,Parent):
    def hello(self):
        super().hello()
        print("who is my parent?")

s = Son()
s.hello()
'''


class Myclass:
    def __init__(self):
        return "sssss"

m = Myclass()
