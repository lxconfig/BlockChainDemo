import gevent
from gevent import monkey
import time

# gevent会在所有阻塞操作时，跳转到另一个协程，但是要用gevent实现的阻塞操作才有效果
# 如: time.sleep(0.5)  改为  gevent.sleep(0.5)
# monkey.patch_all()会自动改上述操作
monkey.patch_all()

def task(num):
    for i in range(num):
        print(i)
        time.sleep(0.5)


def main():
    """
        用gevent库完成多任务(协程)
    """
    # 或者
    # g1 = gevent.spawn(task, 3)
    # g1.join()
    gevent.joinall(
        [
            gevent.spawn(task, 10),
            gevent.spawn(task, 6)
        ]
    )


if __name__ == "__main__":
    main()