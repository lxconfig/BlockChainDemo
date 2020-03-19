from matplotlib import pyplot as plt
from matplotlib import font_manager

y_3 = [11,17,16,11,12,11,12,6,6,7,8,12,15,14,17,18,21,16,17]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22]

x_3 = range(1,20)
x_10 = range(31, 50)

plt.figure(figsize=(20, 8), dpi=80)

font = font_manager.FontProperties(
    fname="C://WINDOWS//FONTS//MSYH.TTC"
)

_x = list(x_3) + list(x_10)
xticks_labels = ["3月{}日".format(i) for i in x_3]
xticks_labels += ["10月{}日".format(i) for i in x_3]
plt.xticks(_x, xticks_labels, rotation=45, fontproperties=font)

# 描述
plt.xlabel("日期", fontproperties=font)
plt.ylabel("温度", fontproperties=font)
plt.title("3月份和10月份温度变化图", fontproperties=font)

# 绘制散点图
plt.scatter(x_3, y_3, label="3月份")
plt.scatter(x_10, y_10, label="10月份")

# 图例
plt.legend(prop=font)

plt.show()