import pandas as pd
import numpy as np

# 创建DataFrame数据
# 包含行索引(index)和列索引(columns)
t1 = pd.DataFrame(np.arange(12).reshape(3,4), index=["A","B","C"], columns=["D","E","F","G"])
print(t1)

# 也可以用字典来创建
a = {
    "name": ['zhangsan', 'lisi'],
    "age": [23,42],
    'tel': [12323532, 135235246],
}

t2 = pd.DataFrame(a)
print(t2)

# 获取行索引、列索引和值
print(t2.index)
print(t2.columns)
print(t2.values)

# 显示头几行
# 默认头5行
t2.head()

# 显示后几行
# 默认后5行
t2.tail()

# 显示t2的概览信息
print(t2.info())

# 计算数据中数字的一些信息
print(t2.describe())

# DataFrame中对数据进行排序
# by: 按什么字段排序
# ascending: 升序/降序，默认升序True
t3 = t2.sort_values(by="age", ascending=True)
print(t3)