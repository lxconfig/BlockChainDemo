"""
显示10点-12点每分钟的气温
"""

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager   # 设置中文显示

# windows和linux设置中文显示
# font = {
#     'family': 'MicroSoft YaHei',
#     'weight': 'bold',
#     'size': "10",
# }
# matplotlib.rc('font', **font)

# 另一种设置中文显示的方法，用font_manager类
# fname参数表示字体的路径
# 也可以设置size等其他属性
my_font = font_manager.FontProperties(
    fname="C://WINDOWS//FONTS//MSYH.TTC",
    size="12"
)

# 准备数据
# x轴表示每分钟
x = range(0, 120)

# y轴表示每分钟的气温
y = [random.randint(20, 35) for i in range(0, 120)]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 设置x轴刻度
# 显示字符串
_x = list(x)[::5]
xticks_labels = ["10点{}分".format(i) for i in range(60)]
xticks_labels += ["11点{}分".format(i) for i in range(60)]
# 使数字和字符串一一对应，x轴显示字符串
# rotation表示旋转角度
# fontproperties表示中文字体
plt.xticks(_x, xticks_labels[::5], rotation=45, fontproperties=my_font)
# plt.xticks(x[::10])

# 设置y轴刻度
plt.yticks(range(min(y), max(y)+1), fontproperties=my_font)

# 添加描述信息
plt.xlabel("时间 单位(min)", fontproperties=my_font)
plt.ylabel("温度 单位(℃)", fontproperties=my_font)
plt.title("10点-12点每分钟的气温变化图", fontproperties=my_font)

# 绘图
plt.plot(x, y)

# 展示
plt.show()