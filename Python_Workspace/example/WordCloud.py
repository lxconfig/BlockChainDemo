# -*- coding:utf-8 -*-
# time: 2019/03/19 16:57
# File: WorldCloud.py
import datetime
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread
start = datetime.datetime.now()
# 读取一个英文txt文件
text = open(r'E:\Python37\test.txt', 'r').read()
# 生成词云
wordcloud = WordCloud(background_color='white', scale=1.5).generate(text)
# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")