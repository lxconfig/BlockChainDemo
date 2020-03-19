from matplotlib import pyplot as plt, font_manager

# 准备数据
x = range(11, 31)
y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
z = [1,0,1,0,2,1,2,2,1,3,1,2,4,6,2,1,2,2,1,1]

# 设置中文显示
font = font_manager.FontProperties(
    fname="C://WINDOWS//FONTS//MSYH.TTC",
    size=12
)

# 设置图片大小
plt.figure(figsize=(15, 8), dpi=80)

# 设置x，y轴
x_lables = ["{}岁".format(i) for i in x]
plt.xticks(x, x_lables, fontproperties=font)
plt.yticks(y, fontproperties=font)

# 描述信息
plt.xlabel("年龄 单位(岁)", fontproperties=font)
plt.ylabel("个数 单位(个)", fontproperties=font)
plt.title("11岁至30岁每年男(女)朋友数量变化图", fontproperties=font)

# 设置网格线（根据x，y轴的刻度画网格）
# alpha表示透明度
plt.grid(alpha=0.4)

# 画图，展示
# 同一张图绘制两条折线
# label表示折线的描述
# color表示线条颜色，linestyle表示线条风格，linewidth表示线条粗细
plt.plot(
    x,
    y,
    label='用户A',
    color="black",
    linestyle="--",
    linewidth=5,
    alpha=0.5
)
plt.plot(
    x,
    z,
    label="用户B",
    color="orange",
    linestyle="-.",
    linewidth=5,
    alpha=0.5
)

# 添加图例，配合label使用，默认显示再右上角
# prop表示显示中文
# loc表示图例显示的位置
plt.legend(prop=font, loc="upper left")

plt.show()