import time


def main():
    for i in range(10, 0, -1):
        print("\r倒计时{}秒!".format(i), end="")
        time.sleep(1)
    print("\r倒计时结束")


if __name__ == "__main__":
    main()