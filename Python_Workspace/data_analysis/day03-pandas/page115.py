import pandas as pd
import numpy as np

t1 = pd.DataFrame(np.arange(12).reshape(3,4), index=list("ABC"), columns=list("WXYZ"))
print(t1)

# loc: 通过标签索引数据
# 取行
# print(t1.loc["A"])
print(t1.loc["A", :])

# 取列
print(t1.loc[:, "W"])

# 取连续的行或列
print(t1.loc["A":, "Y":])

# iloc: 通过位置获取数据
# 取第一行的数据
print(t1.iloc[1])

# :后面的数据还会取到
print(t1.iloc[0:2, 2:3])

# 布尔索引
print(t1[t1["W"] > 1])
# 多个条件可以用 & |
print(
    t1[(t1["Y"] > 0) & (t1["Y"] < 2)]
)