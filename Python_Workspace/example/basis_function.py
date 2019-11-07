
#输入数据的两种方法：
'''
import sys
print("please enter your age:")
q=sys.stdin.readline()
print(q)

'''
'''
print("please enter your age:")
q=input()
b=q.rstrip()
print(q)
print(b)

'''

fruit=['apple','banana','dragon fruit']
length=len(fruit)
for i in range(0,length):
    print("the fruit at index %s is %s" % (i,fruit[i]))
