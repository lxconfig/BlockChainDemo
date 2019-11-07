# -*- coding:utf-8 -*-
# time:2018/12/13 18:51

data = {'name':'goudan',
        'age':18,
        'sex':'m',
        'height':180
}
print(data.items())  #返回可遍历的(键, 值) 元组数组
for key, values in data.items():
    print(key + ':' + str(values))