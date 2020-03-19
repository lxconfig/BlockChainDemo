import numpy as np

file_path = "./data.csv"

t1 = np.loadtxt(fname=file_path, dtype="int", delimiter=",")

# 取某一行
# t1[行,列]
print(t1[2])
# :表示所有列,统一理解为所有
print(t1[2,:])

# 取连续的行
# print(t1[2:])

# 取不连续的行
# print(t1[[2,8,10]])

# 取列
# print(t1[:,2])

# 取连续的列
print(t1[:,2:])

# 取不连续的列
print(t1[:,[0,2]])
print("*"*10)

# 取多行多列，第三行到第五行，第二列到第四列
# 取相交的点
print(t1[2:5,1:4])

# 取多个不相邻的点
# 所选取的点是: (0,0) (2,1) (2,3)
print(t1[[0,2,2], [0,1,3]])

print("*"*100)

# numpy中三元运算符 where  clip
t2 = np.arange(12).reshape(3,4)
# 布尔索引
# t2[t2<5] = 5

# where
# 将t2中小于5的改为5，大于5的改为10
t2 = np.where(t2<5, 5, 10)
print(t2)

# clip
# 将t2中小于3的改为3，大于8的改为8
t3 = np.clip(t2, 3, 8)
print(t3)