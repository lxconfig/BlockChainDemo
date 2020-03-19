

def main():
    '''
        展开列表元素
    '''
    a = [[2,4,5], [2,51,5], [4,6,1]]

    b = [k for i in a for k in i]
    print(b)

    # 或者
    def flatten(a):
        ret = []
        for i in a:
            if isinstance(i, list):
                # 用extend是因为每次递归时，都会重新创建一个ret,返回到上次递归
                # 如 第一次递归 ret = [2,4,5]作为flatten(i)的返回值
                ret.extend(flatten(i))
            else:
                ret.append(i)
        return ret
    print(flatten(a))


if __name__ == "__main__":
    main()