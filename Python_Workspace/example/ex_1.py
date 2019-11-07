import random
secret = random.randint(1,10)
temp=input("请输入数字：")
guess=int(temp)
i=0
while guess != secret and i <= 3:
    temp = input("错了，重新输入：")
    guess=int(temp)
    if guess == secret:
        print("对了")    
    else:
        if guess < secret:
            print("小了")
        else:
            if guess > secret:
                print("大了")
    i = i + 1
    if i > 3:
        print("次数用完了")
print('拜拜')
