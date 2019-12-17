from redis import StrictRedis

def main():
    # 创建一个StrictRedis对象，链接redis数据库
    try:
        sr = StrictRedis(host='localhost', port=6379, db=0)
        # 添加一个key和value，类型为string
        # 返回一个bool值
        result = sr.set('name', 'lixuan123')
        print(result)
        # 获取name的值
        value = sr.get('name')
        print(value)
        # 删除name及对应的值
        # 删除成功返回1
        # 也可删除多个 sr.delete('name', 'age')
        res = sr.delete('name')
        print(res)
        # 返回所有键,返回值是列表
        re = sr.keys()
        print(re)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
