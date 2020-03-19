import numpy as np

def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        # 按列遍历nan
        temp_col = t1[:, i]
        # 判断每一列中nan的个数
        nan_num = np.count_nonzero(temp_col != temp_col)
        # 不为0说明某一列包含nan
        if nan_num != 0:
            # 找到这一列中，不为nan的数据
            temp_not_nan_col = temp_col[temp_col == temp_col]
            # 找到这一列中，是nan的数据，并赋值为其他数据的均值
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
    return t1

if __name__ == "__main__":
    t1 = np.arange(12).reshape(3,4).astype(float)
    t1[1,2:] = np.nan
    print(t1)
    t1 = fill_ndarray(t1)
    print(t1)