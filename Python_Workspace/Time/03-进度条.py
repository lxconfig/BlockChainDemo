import time
sum = 50         #设置倒计时时间
interval = 0.5   #设置屏幕刷新的间隔时间
for i in range(0,int(sum/interval)+1):
    print("\r正在加载:" + "|" +"*"*i + " "*(int(sum/interval)+1-i)+"|" +str(i)+"%",end="")
    time.sleep(interval)
print("\r加载完成！")