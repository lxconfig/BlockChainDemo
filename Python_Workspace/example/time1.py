import time
print(time.asctime())

import sys
def age_joke(age):
    if age>=10 and age<=100:
        print("xxxx")
    else:
        print('you are a bicth')
print("please input you age:")
age=int(sys.stdin.readline())
result=age_joke(age)
