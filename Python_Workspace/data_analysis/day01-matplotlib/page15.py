from matplotlib import pyplot as plt

# 设置数据
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

# 设置图片大小
# figsize(宽,高)设置图片大小，dpi设置图片清晰度
plt.figure(figsize=(20, 8), dpi=80)

# 画图
plt.plot(x, y)

# 设置x轴的刻度
plt.xticks(x)

# 设置y轴的刻度
plt.yticks(range(min(y), max(y)+1))

# 保存图片
# 参数传入保存地址
# plt.savefig("./t1.png")
# 展示图片
plt.show()