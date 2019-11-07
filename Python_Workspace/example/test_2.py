import time as t
class MyTimer :
    def __init__(self):
        self.unit = ["年", "月", "日", "时", "分", "秒"]
        self.notice = "未开始计时"
        self.begin = 0
        self.end = 0
        
    def __str__(self) :
        return self.notice
    
    __repr__ = __str__
    
    def start(self) :
        self.begin = t.localtime()
        self.notice = "先调用stop()结束计时"
        print("计时开始")

    def stop(self) :
        if not self.begin :
           print("先调用start()开始计时")
        else :
            self.end = t.localtime()
            self.calc()
            print("计时结束")

    def calc(self) :
        self.per = []
        self.notice = "总共运行了"
        for index in range(6) :
            self.per.append(self.end[index] - self.begin[index])
            if self.per[index] :
                self.notice += (str(self.per[index]) + self.unit[index])
        return self.notice
        self.begin = 0
        self.end = 0

    def __add__(self , other) :
        pers = "总共运行了"
        result = []
        for index in range(6) :
            result.append(self.per[index] + other.per[index])
            if result[index] :
                 pers += (str(result[index]) + self.unit[index])
        return pers

t1 = MyTimer()
t2 = MyTimer()
