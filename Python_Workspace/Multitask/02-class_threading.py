import threading
import time

class MyThreading(threading.Thread):
    """通过继承threading.Thread来创建线程"""
    def run(self):
        """run()方法必须定义，其中的代码就是线程要执行的代码"""
        for i in range(3):
            time.sleep(1)
            # name属性保存的是当前线程的名字
            msg = "I am " + self.name + ' @ ' + str(i)
            print(msg)

if __name__ == "__main__":
    t = MyThreading()
    # start()方法会调用run()方法
    t.start()