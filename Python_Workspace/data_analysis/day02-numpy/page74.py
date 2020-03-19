import numpy as np

file_path = "./data.csv"

# 读取csv文件
# loadtxt(fname, dtype, delimiter, skiprows, usecols, unpack)
# fname: 文件路径
# dtype: 指定读取数据的类型,默认np.float
# delimiter: 分隔字符串，默认是空格
# skiprows: 跳过前x行
# usecols: 读取指定的列
# unpack: 转置读取数据,默认False
t1 = np.loadtxt(fname=file_path, delimiter=",", dtype="int")
t2 = np.loadtxt(fname=file_path, delimiter=",", dtype="int",skiprows=2, usecols=2)
# print(t1)
# print(t2)

# numpy中的转置方法
t3 = np.arange(18).reshape((3,6))
print(t3)

# transpose()
print(t3.transpose())

# T
print(t3.T)

# swapaxes()
print(t3.swapaxes(1, 0))