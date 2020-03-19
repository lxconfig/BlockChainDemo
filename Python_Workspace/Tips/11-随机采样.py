import random


def main():
    '''
        随机从列表或者字符串中采样
    '''
    a = 'qwrrtydsg'
    b = [3,46,2,6,7,2,1]
    c = random.sample(a, 3)
    d = random.sample(b, 4)

    print(c, d)
    
if __name__ == "__main__":
    main()