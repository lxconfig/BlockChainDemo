import numpy as np

# numpy中常用的统计函数
# 不指定轴则是统计整个数组

t1 = np.arange(12).reshape(3,4)
print(t1)

t2 = np.arange(12, dtype=float).reshape(3,4)
t2[2,3] = np.nan
print(t2)

# sum(axis=None): 求和
# axis=0: 表示按0轴(横向)方向，但相加要按列计算
# axis=1: 表示按1轴(纵向)方向，但相加要按行计算
print("axis=0", t1.sum(axis=0))
print("axis=1", t1.sum(axis=1))
# 若数组中存在nan，则nan存在的那一行或一列和为nan
print("*"*50)
print("axis=0", t2.sum(axis=0))
print("axis=1", t2.sum(axis=1))

print("*"*50)

# mean(axis=None): 求均值
# nan的均值为nan
print("axis=0", t1.mean(axis=0))
print("axis=1", t1.mean(axis=1))
print("*"*50)

# np.median(t, axis=None): 求中值
# nan的均值为nan
print("axis=0", np.median(t1,axis=0))
print("axis=1", np.median(t2,axis=1))

print("*"*50)

# max(axis=None): 最大值
# min(axis=None): 最小值
print("axis=0", t1.max(axis=0))
print("axis=1", t1.min(axis=1))

print("*"*50)

# np.ptp(t, axis=None): 求极值(最大值与最小值之差)
print("axis=0", np.ptp(t1,axis=0))
print("axis=1", np.ptp(t2,axis=1))

print("*"*50)

# std(axis=None): 求标准差
print("axis=0", t1.std(axis=0))
print("axis=1", t2.std(axis=1))