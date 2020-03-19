import numpy as np
import random

# 使用numpy生成数组

# 创建数组,类型为ndarray
t1 = np.array([1,2,3,4])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)

t3 = np.arange(4, 10, 2)
print(t3)

# 查看数组中数据的类型
print(t3.dtype)

# 指定数组中数据的类型
t4 = np.arange(10, dtype="i2")
print(t4)
print(t4.dtype)

# 转换已有数组中数据的类型
t5 = np.array([1,1,0,1,0,1,0], dtype=bool)
print(t5)

# astype()转换类型
t6 = t5.astype(int)
print(t6)

# 生成包含小数的数组
t7 = np.array([random.random() for i in range(10)])
print(t7)

# 保留固定位数的小数(四舍五入)
t8 = np.round(t7, 2)
print(t8)