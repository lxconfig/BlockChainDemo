import pysnooper
import pendulum

# @pysnooper.snoop()
def main():
    '''
        pendulum是一个用来对时间进行处理的模块，相比datetime更好使用和理解
    '''
    # 显示现在的时间，更加精确
    print("现在的时间是:", pendulum.now())

    print(pendulum.now().to_date_string())



if __name__ == "__main__":
    main()