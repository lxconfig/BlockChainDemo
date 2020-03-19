import numpy as np

# 对生成数组的形状进行操作


# 数组的形状
t1 = np.array(range(12))
print(t1)
# 输出(12,)，表示t1是一个一维数组
print(t1.shape)

t2 = np.array([[1,2,3], [4,5,6]])
print(t2)
# 输出(2, 3)，表示t2是2行3列的二维数组
print(t2.shape)

t3 = np.array([
    [[1,2,3], [4,5,6]],
    [[7,8,9], [10,11,12]]
])
print(t3)
# 输出(2, 2, 3)，表示有2块数据，其中的数据都是2行3列
print(t3.shape)

# 修改数组的形状
t4 = np.arange(12)
# reshape(块数,行数,列数)
t5 = t4.reshape((3,4))
print(t4)
print(t5)

# 将多维数组展开成一维数组
t6 = t5.flatten()
print(t6)