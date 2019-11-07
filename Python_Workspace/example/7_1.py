import sys
def moon_weight():
    print('please enter your Earth weight:')
    E_weight=int(sys.stdin.readline())
    print("please entry the ratio:")
    ratio=float(sys.stdin.readline())
    for i in range(1,16):
        print('year %s is %s' % (i,E_weight*ratio))
        E_weight+=1

result= moon_weight()
