import numpy as np

# 数组的计算


# 数组与数进行计算
t1 = np.array(range(10))
print(t1)
# 数组中每个数都会参与计算
print(t1 + 2)

# 数组与数组进行计算
# 只要有一个维度是一样的长度，就可以计算
t2 = np.array(range(20, 30))
print(t2 + t1)

t3 = np.array(range(18)).reshape(3,3,2)
print(t3)

t4 = np.arange(6).reshape(3,2)
print(t4)
print(t3 + t4)