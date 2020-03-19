import numpy as np

t1 = np.arange(12).reshape(3,4)
print(t1)

print("*"*50)

# 数组行列交换
# 行交换
t1[[0, 2], :] = t1[[2, 0], :]
print(t1)
print("*"*50)

# 列交换
t1[:, [1, 3]] = t1[:, [3, 1]]
print(t1)

print("*"*50)

# 数组的拼接
t2 = np.arange(12).reshape(3,4)
t3 = np.arange(13,25).reshape(3,4)
# 竖直拼接
t4 = np.vstack((t2, t3))
print(t4)
print("*"*50)

# 水平拼接
t5 = np.hstack((t2,t3))
print(t5)
