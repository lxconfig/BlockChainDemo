import pandas as pd
import numpy as np

t = pd.DataFrame(np.arange(12).reshape(3,4))

t.iloc[[0,2], [2,3]] = np.nan
print(t)

# 判断数据是否是NaN
# pandas中计算时，不把NaN纳入计算

# pd.isnull(t)将NaN置为True
print(pd.isnull(t))
# pd.notnull(t)将NaN置为False
print(pd.notnull(t))

# 删除NaN所在的行列
# dropna(axis=0, how='any', inplace=False)
# inplace: 表示是否原地修改
# t = t.dropna(axis=0, how='any')
# print(t)

# 填充数据
# fillna(d): 直接填充d值
# t = t.fillna(0)
t = t.fillna(t.mean())
print(t)
