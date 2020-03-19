import pandas as pd

# Series 一维 带标签(索引)数组
# 索引可以指定
t1 = pd.Series(range(10), index=list("ABCDEFGHIJ"))
print(t1)

# 输入字典创建Series时，键作为索引
# 索引多于数据本身时，缺少的数据用NaN表示，并且数据变为float
data = {
    "name": "zhangsan",
    "age": 13,
    "tel": 1351385235
}
t2 = pd.Series(data)
print(t2)

# 获取Series所有的索引和值
print(t2.index)
print(t2.values)

# Series数据的切片
# 跟字典类似，可以根据键或索引取值
print(t2[1])
print(t2["name"])
print(t2[[0,2]])
print(t2[["name", "tel"]])